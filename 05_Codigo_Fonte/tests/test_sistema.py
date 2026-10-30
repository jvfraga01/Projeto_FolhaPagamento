"""Testes: cálculo, permissões (backend), folha congelada e filtros.
Rodar com:  python -m unittest discover -v
"""
import os
import re
import tempfile
import unittest

from werkzeug.security import generate_password_hash

from app import create_app, regras
from app.db import get_db


class CalculoTest(unittest.TestCase):
    """Modo padrão = fórmulas do cliente (sem metas, progressão, bônus ou teto)."""

    def test_padrao_recebe_so_o_salario(self):
        r = regras.calcular("PADRAO", 300000)
        self.assertEqual((r["adicionais"], r["total"]), (0, 300000))

    def test_salario_zero_valido(self):
        self.assertEqual(regras.calcular("PADRAO", 0)["total"], 0)
        r = regras.calcular("COMISSIONADO", 0, vendas=100000, percentual_base=300)
        self.assertEqual((r["adicionais"], r["total"]), (3000, 3000))

    def test_comissionado_vendas_vezes_percentual(self):
        # vendas 5.000,00 x 3% = 150,00
        r = regras.calcular("COMISSIONADO", 300000, vendas=500000, percentual_base=300)
        self.assertEqual((r["adicionais"], r["total"]), (15000, 315000))

    def test_comissionado_sem_meta_vendas_abaixo_de_5000(self):
        # cliente: 4.999,99 x 3% = 149,9997 -> 150,00 (arredondado); não zera o adicional
        r = regras.calcular("COMISSIONADO", 300000, vendas=499999, percentual_base=300)
        self.assertEqual((r["adicionais"], r["total"]), (15000, 315000))

    def test_comissionado_percentual_cadastrado_sem_teto(self):
        # 15% cadastrado é aplicado integralmente (sem teto de 10%)
        r = regras.calcular("COMISSIONADO", 0, vendas=100000, percentual_base=1500)
        self.assertEqual((r["pct"], r["adicionais"]), (1500, 15000))

    def test_producao_quantidade_vezes_valor(self):
        r = regras.calcular("PRODUCAO", 100000, quantidade=99, valor_unidade=250)
        self.assertEqual((r["adicionais"], r["total"]), (24750, 124750))
        r = regras.calcular("PRODUCAO", 100000, quantidade=100, valor_unidade=250)
        self.assertEqual(r["adicionais"], 25000)
        r = regras.calcular("PRODUCAO", 100000, quantidade=200, valor_unidade=250)
        self.assertEqual((r["adicionais"], r["total"]), (50000, 150000))  # sem bônus de 2%

    def test_arredondamento_meio_para_cima_em_centavos(self):
        # 1.000,50 x 3% = 30,015 -> 30,02 (meio para cima, RNF007)
        r = regras.calcular("COMISSIONADO", 0, vendas=100050, percentual_base=300)
        self.assertEqual(r["adicionais"], 3002)
        # 4.999,99 x 3% = 149,9997 -> 150,00
        r = regras.calcular("COMISSIONADO", 0, vendas=499999, percentual_base=300)
        self.assertEqual(r["adicionais"], 15000)

    def test_novo_calculador_sem_alterar_os_existentes(self):
        # RNF004: adicional fixo de R$ 100,00 registrado só em CALCULADORES.
        antes = {t: regras.calcular(t, 100000, vendas=500000, quantidade=100,
                                    percentual_base=300, valor_unidade=250)
                 for t in ("PADRAO", "COMISSIONADO", "PRODUCAO")}
        regras.CALCULADORES["EXPERIMENTAL"] = lambda d: {"atingiu": True, "pct": 0, "adicionais": 10000}
        try:
            self.assertEqual(regras.calcular("EXPERIMENTAL", 100000)["total"], 110000)
            for t, esperado in antes.items():
                r = regras.calcular(t, 100000, vendas=500000, quantidade=100,
                                    percentual_base=300, valor_unidade=250)
                self.assertEqual(r, esperado, t)
        finally:
            del regras.CALCULADORES["EXPERIMENTAL"]

    def test_valores_negativos_sao_recusados(self):
        with self.assertRaises(ValueError):
            regras.calcular("PADRAO", -1)
        with self.assertRaises(ValueError):
            regras.parse_reais("-10")
        with self.assertRaises(ValueError):
            regras.parse_inteiro("-3")

    def test_dinheiro(self):
        self.assertEqual(regras.parse_reais("1.234,56"), 123456)
        self.assertEqual(regras.reais(123456), "R$ 1.234,56")
        self.assertEqual(regras.senha_inicial("1990-03-15"), "15031990")


class RegimeMetasTest(unittest.TestCase):
    """Modalidade OPCIONAL (RN009-RN011), só ativa com regime_metas=True / REGIME_METAS=1."""

    def test_meta_nao_batida_zera_adicional(self):
        r = regras.calcular("COMISSIONADO", 300000, meta=500000, vendas=499999,
                            percentual_base=300, regime_metas=True)
        self.assertEqual(r["adicionais"], 0)
        self.assertFalse(r["atingiu"])

    def test_meta_batida_usa_percentual_cadastrado(self):
        r = regras.calcular("COMISSIONADO", 300000, meta=500000, vendas=500000,
                            percentual_base=300, regime_metas=True)
        self.assertEqual((r["adicionais"], r["total"]), (15000, 315000))

    def test_progressao_1_ponto_a_cada_2_mil_e_teto_de_10(self):
        r = regras.calcular("COMISSIONADO", 0, meta=500000, vendas=900000,
                            percentual_base=300, regime_metas=True)
        self.assertEqual(r["pct"], 500)
        r = regras.calcular("COMISSIONADO", 0, meta=500000, vendas=9_000_000,
                            percentual_base=300, regime_metas=True)
        self.assertEqual(r["pct"], 1000)

    def test_producao_com_meta_e_bonus(self):
        kw = dict(meta=100, valor_unidade=250, regime_metas=True)
        self.assertEqual(regras.calcular("PRODUCAO", 100000, quantidade=99, **kw)["adicionais"], 0)
        self.assertEqual(regras.calcular("PRODUCAO", 100000, quantidade=100, **kw)["adicionais"], 25000)
        r = regras.calcular("PRODUCAO", 100000, quantidade=200, **kw)
        self.assertEqual((r["pct"], r["adicionais"]), (200, 50000 + 1000))

    def test_meta_cresce_quando_bate_e_nunca_cai_abaixo_do_minimo(self):
        self.assertEqual(regras.proxima_meta("COMISSIONADO"), 500000)
        self.assertEqual(regras.proxima_meta("COMISSIONADO", 500000, 500000), 700000)
        self.assertEqual(regras.proxima_meta("COMISSIONADO", 700000, 100), 700000)


class BaseTest(unittest.TestCase):
    REGIME_METAS = False  # padrão: fórmulas do cliente

    def setUp(self):
        self.pasta = tempfile.TemporaryDirectory()
        self.app = create_app({"TESTING": True, "SECRET_KEY": "teste",
                               "REGIME_METAS": self.REGIME_METAS,
                               "DATABASE": os.path.join(self.pasta.name, "t.db")})
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.admin = self.novo("Ana RH", 1, "PADRAO", 500000)
        self.fin = self.novo("Fabio Financeiro", 2, "PADRAO", 400000)
        self.joao = self.novo("Joao Comum", 3, "COMISSIONADO", 300000, pct=300)
        self.maria = self.novo("Maria Comum", 3, "PRODUCAO", 200000, un=250)
        self.padrao = self.novo("Paulo Padrao", 3, "PADRAO", 250000)

    def tearDown(self):
        self.ctx.pop()
        self.pasta.cleanup()

    def novo(self, nome, nivel, tipo, salario, pct=0, un=0, inicio="2026-01-01"):
        db = get_db()
        cur = db.execute(
            """INSERT INTO colaborador (nome, data_nascimento, data_inicio_contrato, nivel_acesso,
                   senha_hash, tipo, salario_base_centavos, percentual_comissao_bp,
                   valor_unidade_centavos) VALUES (?,?,?,?,?,?,?,?,?)""",
            (nome, "1990-03-15", inicio, nivel, generate_password_hash("15031990"), tipo,
             salario, pct, un))
        db.commit()
        return cur.lastrowid

    def cliente(self, matricula=None, senha="15031990"):
        c = self.app.test_client()
        if matricula:
            r = c.get("/login")
            token = re.search(r'name="csrf_token" value="([^"]+)"', r.get_data(as_text=True)).group(1)
            r = c.post("/login", data={"matricula": matricula, "senha": senha, "csrf_token": token})
            self.assertEqual(r.status_code, 302, "login deveria funcionar")
        return c

    def post(self, c, url, dados=None):
        with c.session_transaction() as s:
            s.setdefault("csrf", "tok")
            token = s["csrf"]
        return c.post(url, data={**(dados or {}), "csrf_token": token})

    def gerar_e_lancar(self, ano=2026, mes=3, vendas="5000,00", qtd="100"):
        adm = self.cliente(self.admin)
        self.post(adm, "/folha/gerar", {"ano": ano, "mes": mes})
        p = get_db().execute("SELECT id FROM periodo WHERE ano=? AND mes=?", (ano, mes)).fetchone()["id"]
        f = {r["matricula"]: r["id"] for r in get_db().execute("SELECT id, matricula FROM folha WHERE periodo_id=?", (p,))}
        self.post(adm, f"/folha/{p}/lancamentos",
                  {f"vendas_{f[self.joao]}": vendas, f"qtd_{f[self.maria]}": qtd})
        return adm, p, f


class LoginTest(BaseTest):
    def test_login_logout_e_senha_errada(self):
        c = self.cliente()
        r = c.get("/login")
        token = re.search(r'name="csrf_token" value="([^"]+)"', r.get_data(as_text=True)).group(1)
        r = c.post("/login", data={"matricula": self.joao, "senha": "errada", "csrf_token": token})
        self.assertEqual(r.status_code, 401)
        c = self.cliente(self.joao)
        self.assertEqual(c.get("/meus-dados").status_code, 200)
        self.post(c, "/logout")
        self.assertEqual(c.get("/meus-dados").status_code, 302)

    def test_rotas_exigem_login(self):
        c = self.cliente()
        for url in ("/colaboradores", "/folha", "/relatorio", "/minha-folha", "/colaboradores/novo"):
            self.assertEqual(c.get(url).status_code, 302, url)

    def test_post_sem_csrf_e_recusado(self):
        c = self.cliente(self.admin)
        self.assertEqual(c.post("/folha/gerar", data={"ano": 2026, "mes": 3}).status_code, 400)

    def test_usuario_desabilitado_perde_acesso_na_hora_e_pode_voltar(self):
        joao = self.cliente(self.joao)
        adm = self.cliente(self.admin)
        self.post(adm, f"/colaboradores/{self.joao}/desabilitar")
        self.assertEqual(joao.get("/meus-dados").status_code, 302)  # sessão derrubada
        r = self.cliente().post("/login")  # sem token
        self.assertEqual(r.status_code, 400)
        self.post(adm, f"/colaboradores/{self.joao}/reativar")
        self.cliente(self.joao)  # consegue entrar de novo

    def test_nao_vaza_hash_de_senha(self):
        for m in (self.admin, self.fin, self.joao):
            c = self.cliente(m)
            for url in ("/meus-dados", "/minha-folha", "/colaboradores", "/folha"):
                self.assertNotIn("scrypt", c.get(url).get_data(as_text=True))

    def test_nao_desabilita_a_si_mesmo_nem_o_ultimo_admin(self):
        adm = self.cliente(self.admin)
        self.post(adm, f"/colaboradores/{self.admin}/desabilitar")
        st = get_db().execute("SELECT status FROM colaborador WHERE matricula=?", (self.admin,)).fetchone()
        self.assertEqual(st["status"], "Ativo")


class PermissaoTest(BaseTest):
    def test_nivel3_nao_acessa_areas_de_gestao(self):
        c = self.cliente(self.joao)
        for url in ("/colaboradores", "/colaboradores/novo", f"/colaboradores/{self.maria}/editar",
                    "/folha", "/relatorio", f"/folha/1/lancamentos"):
            self.assertEqual(c.get(url).status_code, 403, url)
        for url in ("/folha/gerar", f"/colaboradores/{self.maria}/desabilitar",
                    f"/colaboradores/{self.maria}/redefinir-senha", "/folha/1/fechar"):
            self.assertEqual(self.post(c, url).status_code, 403, url)

    def test_nivel3_nao_ve_folha_de_outro_nem_recebe_dados(self):
        adm, p, f = self.gerar_e_lancar()
        self.post(adm, f"/folha/{p}/fechar")
        joao = self.cliente(self.joao)
        r = joao.get(f"/folha/{f[self.maria]}")
        self.assertEqual(r.status_code, 403)
        self.assertNotIn("Maria", r.get_data(as_text=True))
        self.assertEqual(joao.get(f"/folha/{f[self.joao]}").status_code, 200)
        # id inexistente também não revela nada
        self.assertEqual(joao.get("/folha/99999").status_code, 403)

    def test_minha_folha_ignora_parametros_da_url(self):
        adm, p, f = self.gerar_e_lancar()
        self.post(adm, f"/folha/{p}/fechar")
        joao = self.cliente(self.joao)
        html = joao.get(f"/minha-folha?matricula={self.maria}&nome=Maria").get_data(as_text=True)
        self.assertNotIn("Maria", html)
        self.assertIn("Março/2026", html)

    def test_nivel3_so_ve_folha_de_mes_fechado(self):
        adm, p, f = self.gerar_e_lancar()
        joao = self.cliente(self.joao)
        self.assertEqual(joao.get(f"/folha/{f[self.joao]}").status_code, 403)
        self.post(adm, f"/folha/{p}/fechar")
        self.assertEqual(joao.get(f"/folha/{f[self.joao]}").status_code, 200)

    def test_financeiro_le_mas_nao_altera(self):
        adm, p, f = self.gerar_e_lancar()
        fin = self.cliente(self.fin)
        for url in ("/colaboradores", "/folha", "/relatorio", f"/folha/{f[self.maria]}"):
            self.assertEqual(fin.get(url).status_code, 200, url)
        for url in ("/colaboradores/novo", f"/folha/{p}/lancamentos"):
            self.assertEqual(fin.get(url).status_code, 403, url)
        for url in ("/folha/gerar", f"/folha/{p}/fechar", f"/colaboradores/{self.joao}/desabilitar"):
            self.assertEqual(self.post(fin, url).status_code, 403, url)


class FolhaTest(BaseTest):
    def test_gera_calcula_e_totaliza(self):
        adm, p, f = self.gerar_e_lancar(vendas="5000,00", qtd="100")
        linhas = {r["matricula"]: r for r in get_db().execute("SELECT * FROM folha WHERE periodo_id=?", (p,))}
        self.assertEqual(linhas[self.joao]["total_centavos"], 300000 + 15000)   # 3% de 5.000
        self.assertEqual(linhas[self.maria]["total_centavos"], 200000 + 25000)  # 100 x 2,50
        self.assertEqual(linhas[self.padrao]["total_centavos"], 250000)
        html = adm.get(f"/relatorio?periodo={p}").get_data(as_text=True)
        self.assertIn("Total pago por categoria", html)

    def test_folha_fechada_fica_congelada_mesmo_mudando_o_cadastro(self):
        adm, p, f = self.gerar_e_lancar()
        self.post(adm, f"/folha/{p}/fechar")
        db = get_db()
        db.execute("UPDATE colaborador SET salario_base_centavos = 999999 WHERE matricula=?", (self.joao,))
        db.commit()
        # não dá para recalcular, regerar nem editar
        self.assertEqual(self.post(adm, f"/folha/{p}/lancamentos", {f"vendas_{f[self.joao]}": "9999,00"}).status_code, 403)
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 3})
        r = db.execute("SELECT salario_base_centavos, total_centavos FROM folha WHERE matricula=? AND periodo_id=?",
                       (self.joao, p)).fetchone()
        self.assertEqual(r["salario_base_centavos"], 300000)
        # nem direto no banco
        with self.assertRaises(Exception):
            db.execute("UPDATE folha SET total_centavos = 1 WHERE periodo_id=?", (p,))

    def test_nao_ha_reabertura_nem_segunda_folha_no_mes(self):
        adm, p, f = self.gerar_e_lancar()
        self.assertEqual(adm.get("/folha/%d/reabrir" % p).status_code, 404)
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 3})
        n = get_db().execute("SELECT COUNT(*) FROM folha WHERE periodo_id=? AND matricula=?", (p, self.joao)).fetchone()[0]
        self.assertEqual(n, 1)

    def test_modo_padrao_nao_gera_meta(self):
        adm, p, f = self.gerar_e_lancar(mes=3)
        metas = {r["meta"] for r in get_db().execute("SELECT meta FROM folha WHERE periodo_id=?", (p,))}
        self.assertEqual(metas, {0})

    def test_desabilitado_aparece_nos_meses_em_que_trabalhou(self):
        adm, p, f = self.gerar_e_lancar(mes=3)
        self.post(adm, f"/folha/{p}/fechar")
        self.post(adm, f"/colaboradores/{self.padrao}/desabilitar")
        db = get_db()
        db.execute("UPDATE colaborador SET data_fim_contrato='2026-03-31' WHERE matricula=?", (self.padrao,))
        db.commit()
        self.assertIn("Paulo", adm.get(f"/folha?periodo={p}").get_data(as_text=True))
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 5})
        p5 = db.execute("SELECT id FROM periodo WHERE mes=5").fetchone()["id"]
        self.assertNotIn("Paulo", adm.get(f"/folha?periodo={p5}").get_data(as_text=True))

    def test_valores_invalidos_nos_lancamentos_nao_salvam(self):
        adm, p, f = self.gerar_e_lancar(vendas="1000,00")
        self.post(adm, f"/folha/{p}/lancamentos", {f"vendas_{f[self.joao]}": "-5"})
        v = get_db().execute("SELECT vendas_centavos FROM folha WHERE id=?", (f[self.joao],)).fetchone()[0]
        self.assertEqual(v, 100000)


class FolhaRegimeMetasTest(BaseTest):
    REGIME_METAS = True

    def test_meta_cresce_no_mes_seguinte_se_bateu(self):
        adm, p, f = self.gerar_e_lancar(mes=3, vendas="5000,00", qtd="100")
        self.post(adm, f"/folha/{p}/fechar")
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 4})
        p2 = get_db().execute("SELECT id FROM periodo WHERE mes=4").fetchone()["id"]
        meta = lambda m: get_db().execute("SELECT meta FROM folha WHERE periodo_id=? AND matricula=?", (p2, m)).fetchone()["meta"]
        self.assertEqual(meta(self.joao), 700000)  # 5.000 + 2.000
        self.assertEqual(meta(self.maria), 150)    # 100 + 50

    def test_meta_nao_batida_zera_adicional_na_folha(self):
        adm, p, f = self.gerar_e_lancar(vendas="4999,99", qtd="99")
        linhas = {r["matricula"]: r for r in get_db().execute("SELECT * FROM folha WHERE periodo_id=?", (p,))}
        self.assertEqual(linhas[self.joao]["total_centavos"], 300000)
        self.assertEqual(linhas[self.maria]["total_centavos"], 200000)


class PersistenciaTest(unittest.TestCase):
    def test_dados_sobrevivem_ao_reabrir_a_aplicacao(self):
        with tempfile.TemporaryDirectory() as pasta:
            cfg = {"TESTING": True, "SECRET_KEY": "teste", "DATABASE": os.path.join(pasta, "p.db")}
            app1 = create_app(cfg)
            with app1.app_context():
                db = get_db()
                db.execute(
                    """INSERT INTO colaborador (nome, data_nascimento, data_inicio_contrato, nivel_acesso,
                           senha_hash, tipo, salario_base_centavos) VALUES (?,?,?,?,?,?,?)""",
                    ("Persistente", "1990-03-15", "2026-01-01", 3,
                     generate_password_hash("15031990"), "PADRAO", 123456))
                db.commit()
            del app1  # "encerra" a aplicação
            app2 = create_app(cfg)  # "reabre" com o mesmo arquivo
            with app2.app_context():
                c = get_db().execute("SELECT salario_base_centavos FROM colaborador WHERE nome='Persistente'").fetchone()
                self.assertIsNotNone(c)
                self.assertEqual(c["salario_base_centavos"], 123456)


class FiltrosTest(BaseTest):
    def test_filtros_de_colaboradores_combinados(self):
        adm = self.cliente(self.admin)
        html = adm.get("/colaboradores?nome=comum&tipo=COMISSIONADO").get_data(as_text=True)
        self.assertIn("Joao", html)
        self.assertNotIn("Maria", html)
        html = adm.get("/colaboradores?salario_max=2500,00&status=Ativo").get_data(as_text=True)
        self.assertIn("Maria", html)
        self.assertNotIn("Joao", html)

    def test_filtro_de_status(self):
        adm = self.cliente(self.admin)
        self.post(adm, f"/colaboradores/{self.maria}/desabilitar")
        self.assertNotIn("Maria", adm.get("/colaboradores").get_data(as_text=True))
        self.assertIn("Maria", adm.get("/colaboradores?status=Inativo").get_data(as_text=True))

    def test_nome_com_html_e_escapado(self):
        adm = self.cliente(self.admin)
        self.novo("<script>alert(1)</script>", 3, "PADRAO", 100)
        html = adm.get("/colaboradores").get_data(as_text=True)
        self.assertNotIn("<script>alert(1)", html)

    def test_cadastro_valida_e_cria_com_senha_de_nascimento(self):
        adm = self.cliente(self.admin)
        base = {"data_nascimento": "2000-12-01", "data_inicio_contrato": "2026-01-01",
          "nivel_acesso": "3", "tipo": "PADRAO"}
  r = self.post(adm, "/colaboradores/novo", {**base, "nome": "", "salario_base": "2000,00"})  # CT004
  self.assertEqual(r.status_code, 400)
  r = self.post(adm, "/colaboradores/novo", {**base, "nome": "Fulano Negativo", "salario_base": "-5"})  # CT005
  self.assertEqual(r.status_code, 400)
  n = get_db().execute("SELECT COUNT(*) FROM colaborador WHERE nome IN ('', 'Fulano Negativo')").fetchone()[0]
  self.assertEqual(n, 0)
        r = self.post(adm, "/colaboradores/novo", {
            "nome": "Novo Fulano", "data_nascimento": "2000-12-01", "data_inicio_contrato": "2026-01-01",
            "nivel_acesso": "3", "tipo": "PADRAO", "salario_base": "2000,00"})
        self.assertEqual(r.status_code, 302)
        m = get_db().execute("SELECT matricula FROM colaborador WHERE nome='Novo Fulano'").fetchone()[0]
        self.cliente(m, senha="01122000")  # senha inicial = DDMMAAAA

    def _cadastro(self, adm, nome, tipo, **extra):
        return self.post(adm, "/colaboradores/novo", {
            "nome": nome, "data_nascimento": "1995-06-20", "data_inicio_contrato": "2026-01-01",
            "nivel_acesso": "3", "tipo": tipo, "salario_base": "3000,00", **extra})

    def test_cadastro_comissionado_e_producao(self):
        adm = self.cliente(self.admin)
        self.assertEqual(self._cadastro(adm, "Carla Comissao", "COMISSIONADO",
                                        percentual_comissao="3,00").status_code, 302)
        self.assertEqual(self._cadastro(adm, "Pedro Producao", "PRODUCAO",
                                        valor_unidade="2,50").status_code, 302)
        db = get_db()
        c = db.execute("SELECT * FROM colaborador WHERE nome='Carla Comissao'").fetchone()
        self.assertEqual((c["tipo"], c["salario_base_centavos"], c["percentual_comissao_bp"]),
                         ("COMISSIONADO", 300000, 300))
        p = db.execute("SELECT * FROM colaborador WHERE nome='Pedro Producao'").fetchone()
        self.assertEqual((p["tipo"], p["valor_unidade_centavos"]), ("PRODUCAO", 250))

    def test_cadastro_com_salario_zero_e_aceito(self):
        adm = self.cliente(self.admin)
        self.assertEqual(self._cadastro(adm, "Salario Zero", "PADRAO", salario_base="0,00").status_code, 302)
        c = get_db().execute("SELECT salario_base_centavos FROM colaborador WHERE nome='Salario Zero'").fetchone()
        self.assertEqual(c["salario_base_centavos"], 0)

    def test_recusa_percentual_e_valor_unidade_negativos(self):
        adm = self.cliente(self.admin)
        r = self._cadastro(adm, "Neg Comissao", "COMISSIONADO", percentual_comissao="-1")
        self.assertEqual(r.status_code, 400)
        r = self._cadastro(adm, "Neg Producao", "PRODUCAO", valor_unidade="-1")
        self.assertEqual(r.status_code, 400)
        n = get_db().execute("SELECT COUNT(*) FROM colaborador WHERE nome LIKE 'Neg %'").fetchone()[0]
        self.assertEqual(n, 0)

    def test_matricula_unica_e_sequencial(self):
        adm = self.cliente(self.admin)
        self._cadastro(adm, "Seq Um", "PADRAO")
        self._cadastro(adm, "Seq Dois", "PADRAO")
        m = [r[0] for r in get_db().execute(
            "SELECT matricula FROM colaborador WHERE nome LIKE 'Seq %' ORDER BY matricula")]
        self.assertEqual(len(set(m)), 2)
        self.assertEqual(m[1], m[0] + 1)
        with self.assertRaises(Exception):  # UNIQUE/PK impede duplicidade no banco
            get_db().execute("INSERT INTO colaborador (matricula, nome, data_nascimento, data_inicio_contrato,"
                             " nivel_acesso, senha_hash, tipo, salario_base_centavos) VALUES (?,?,?,?,?,?,?,?)",
                             (m[0], "Dup", "1990-01-01", "2026-01-01", 3, "x", "PADRAO", 0))

    def test_resumo_do_relatorio_com_totais(self):
        adm, p, f = self.gerar_e_lancar(vendas="5000,00", qtd="100")
        html = adm.get(f"/relatorio?periodo={p}").get_data(as_text=True)
        # total geral = 5.000 + 4.000 + 3.150 + 2.250 + 2.500 = 16.900,00
        for esperado in ("R$ 16.900,00", "R$ 3.150,00", "R$ 2.250,00"):
            self.assertIn(esperado, html)


if __name__ == "__main__":
    unittest.main()
