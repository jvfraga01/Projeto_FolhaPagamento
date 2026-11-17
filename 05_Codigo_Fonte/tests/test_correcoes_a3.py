"""Testes da Correção #1 (A3): ponto de milhar (BUG001), imutabilidade no banco (BUG003)
e lacunas de cobertura apontadas na avaliação (senha, edição, lançamentos, texto no lugar de número).
Rodar com:  python -m unittest discover -v
"""
import os
import re
import sqlite3
import tempfile
import unittest

from app import create_app, regras
from app.db import get_db
from tests import test_sistema


class MilharTest(unittest.TestCase):
    """CT046 - BUG001: '1.500' valia R$ 1,50; no padrão brasileiro vale R$ 1.500,00."""

    def test_ponto_de_milhar_sem_virgula(self):
        self.assertEqual(regras.parse_reais("1.500"), 150000)
        self.assertEqual(regras.parse_reais("2.500"), 250000)
        self.assertEqual(regras.parse_reais("1.234.567"), 123456700)
        self.assertEqual(regras.parse_reais("R$ 1.500"), 150000)

    def test_ponto_decimal_e_virgula_continuam_validos(self):
        self.assertEqual(regras.parse_reais("1.500,00"), 150000)
        self.assertEqual(regras.parse_reais("1.234,56"), 123456)
        self.assertEqual(regras.parse_reais("1500"), 150000)
        self.assertEqual(regras.parse_reais("12.50"), 1250)
        self.assertEqual(regras.parse_reais("0.500"), 50)
        self.assertEqual(regras.parse_reais("2.5"), 250)

    def test_percentual_com_ponto(self):
        self.assertEqual(regras.parse_percentual("3.5"), 350)
        self.assertEqual(regras.parse_percentual("3,00"), 300)
        with self.assertRaises(ValueError):
            regras.parse_percentual("10.000")  # vira 10000% e passa de 100%

    def test_formato_ambiguo_e_recusado(self):
        with self.assertRaises(ValueError):
            regras.parse_reais("1,500.00")

    def test_pontos_em_formato_invalido_sao_recusados(self):
        for texto in ("1.5000", "01.500", "1..500", "1.50.0", "1.2345"):  # D-04
            with self.assertRaises(ValueError, msg=texto):
                regras.parse_reais(texto)


class BaseCorrecoes(test_sistema.BaseTest):
    def _status_login(self, matricula, senha):
        c = self.app.test_client()
        html = c.get("/login").get_data(as_text=True)
        token = re.search(r'name="csrf_token" value="([^"]+)"', html).group(1)
        return c.post("/login", data={"matricula": matricula, "senha": senha,
                                      "csrf_token": token}).status_code

    def _fechar_marco(self):
        adm, p, f = self.gerar_e_lancar()
        self.post(adm, f"/folha/{p}/fechar")
        return adm, p, f


class CadastroMilharTest(BaseCorrecoes):
    """CT047."""

    def _cadastro(self, adm, nome, **extra):
        dados = {"nome": nome, "data_nascimento": "1995-06-20", "data_inicio_contrato": "2026-01-01",
                 "nivel_acesso": "3", "tipo": "PADRAO", "salario_base": "3000,00"}
        dados.update(extra)
        return self.post(adm, "/colaboradores/novo", dados)

    def test_cadastro_com_ponto_de_milhar_grava_valor_correto(self):
        adm = self.cliente(self.admin)
        self.assertEqual(self._cadastro(adm, "Milhar Teste", salario_base="1.500").status_code, 302)
        c = get_db().execute("SELECT salario_base_centavos FROM colaborador WHERE nome='Milhar Teste'").fetchone()
        self.assertEqual(c["salario_base_centavos"], 150000)

    def test_cadastro_com_texto_no_lugar_de_numero_e_recusado(self):
        adm = self.cliente(self.admin)
        self.assertEqual(self._cadastro(adm, "Texto Salario", salario_base="abc").status_code, 400)
        self.assertEqual(self._cadastro(adm, "Texto Comissao", tipo="COMISSIONADO",
                                        percentual_comissao="dez").status_code, 400)
        self.assertEqual(self._cadastro(adm, "Texto Producao", tipo="PRODUCAO",
                                        valor_unidade="x").status_code, 400)
        n = get_db().execute("SELECT COUNT(*) FROM colaborador WHERE nome LIKE 'Texto %'").fetchone()[0]
        self.assertEqual(n, 0)


class BancoFolhaFechadaTest(BaseCorrecoes):
    """CT048 - BUG003: o banco também recusa reabrir o mês e inserir folha em mês fechado."""

    def test_banco_recusa_reabrir_e_apagar_periodo_fechado(self):
        adm, p, f = self._fechar_marco()
        db = get_db()
        with self.assertRaises(sqlite3.DatabaseError):
            db.execute("UPDATE periodo SET status='ABERTO' WHERE id=?", (p,))
        db.rollback()
        with self.assertRaises(sqlite3.DatabaseError):
            db.execute("DELETE FROM periodo WHERE id=?", (p,))
        db.rollback()
        self.assertEqual(db.execute("SELECT status FROM periodo WHERE id=?", (p,)).fetchone()["status"],
                         "FECHADO")

    def test_banco_recusa_insert_de_folha_em_periodo_fechado(self):
        adm, p, f = self._fechar_marco()
        extra = self.novo("Extra Tardio", 3, "PADRAO", 100000)
        db = get_db()
        with self.assertRaises(sqlite3.DatabaseError):
            db.execute("INSERT INTO folha (periodo_id, matricula, nome, tipo, salario_base_centavos,"
                       " total_centavos) VALUES (?,?,?,?,?,?)",
                       (p, extra, "Extra Tardio", "PADRAO", 100000, 100000))
        db.rollback()
        n = db.execute("SELECT COUNT(*) FROM folha WHERE matricula=?", (extra,)).fetchone()[0]
        self.assertEqual(n, 0)

    def test_periodo_aberto_continua_aceitando_novos_colaboradores(self):
        adm, p, f = self.gerar_e_lancar()
        extra = self.novo("Extra Aberto", 3, "PADRAO", 100000)
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 3})
        n = get_db().execute("SELECT COUNT(*) FROM folha WHERE periodo_id=? AND matricula=?",
                             (p, extra)).fetchone()[0]
        self.assertEqual(n, 1)


class SenhaTest(BaseCorrecoes):
    """CT049 - RF011 (parte automática)."""

    def test_troca_de_senha_com_senha_atual_correta(self):
        joao = self.cliente(self.joao)
        r = self.post(joao, "/senha", {"atual": "15031990", "nova": "nova1234", "confirma": "nova1234"})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(self._status_login(self.joao, "nova1234"), 302)
        self.assertEqual(self._status_login(self.joao, "15031990"), 401)

    def test_troca_recusada_senha_errada_curta_ou_confirmacao_diferente(self):
        joao = self.cliente(self.joao)
        for atual, nova, confirma in (("errada", "nova1234", "nova1234"),
                                      ("15031990", "123", "123"),
                                      ("15031990", "nova1234", "outra1234")):
            r = self.post(joao, "/senha", {"atual": atual, "nova": nova, "confirma": confirma})
            self.assertEqual(r.status_code, 200, (atual, nova, confirma))
        self.assertEqual(self._status_login(self.joao, "15031990"), 302)  # senha não mudou

    def test_rh_redefine_senha_para_data_de_nascimento(self):
        joao = self.cliente(self.joao)
        self.post(joao, "/senha", {"atual": "15031990", "nova": "nova1234", "confirma": "nova1234"})
        adm = self.cliente(self.admin)
        r = self.post(adm, f"/colaboradores/{self.joao}/redefinir-senha")
        self.assertEqual(r.status_code, 302)
        self.assertEqual(self._status_login(self.joao, "15031990"), 302)
        self.assertEqual(self._status_login(self.joao, "nova1234"), 401)


class EdicaoTest(BaseCorrecoes):
    """CT050 - RF009 (parte automática)."""

    def _dados(self, **extra):
        d = {"nome": "Paulo Silva", "data_nascimento": "1990-03-15", "data_inicio_contrato": "2026-01-01",
             "data_fim_contrato": "", "nivel_acesso": "3", "tipo": "PADRAO", "salario_base": "2600,00"}
        d.update(extra)
        return d

    def test_editar_atualiza_cadastro_e_preserva_mes_fechado(self):
        adm, p, f = self._fechar_marco()
        self.assertEqual(adm.get(f"/colaboradores/{self.padrao}/editar").status_code, 200)
        r = self.post(adm, f"/colaboradores/{self.padrao}/editar", self._dados())
        self.assertEqual(r.status_code, 302)
        db = get_db()
        c = db.execute("SELECT nome, salario_base_centavos FROM colaborador WHERE matricula=?",
                       (self.padrao,)).fetchone()
        self.assertEqual((c["nome"], c["salario_base_centavos"]), ("Paulo Silva", 260000))
        fo = db.execute("SELECT nome, total_centavos FROM folha WHERE id=?", (f[self.padrao],)).fetchone()
        self.assertEqual((fo["nome"], fo["total_centavos"]), ("Paulo Padrao", 250000))

    def test_editar_com_dado_invalido_nao_grava(self):
        adm = self.cliente(self.admin)
        r = self.post(adm, f"/colaboradores/{self.padrao}/editar", self._dados(salario_base="abc"))
        self.assertEqual(r.status_code, 400)
        c = get_db().execute("SELECT nome, salario_base_centavos FROM colaborador WHERE matricula=?",
                             (self.padrao,)).fetchone()
        self.assertEqual((c["nome"], c["salario_base_centavos"]), ("Paulo Padrao", 250000))

    def test_ultimo_administrador_ativo_nao_perde_o_nivel(self):
        db = get_db()
        db.execute("UPDATE colaborador SET status='Inativo' WHERE matricula=1")  # admin inicial
        db.commit()
        adm = self.cliente(self.admin)
        r = self.post(adm, f"/colaboradores/{self.admin}/editar",
                      self._dados(nome="Ana RH", salario_base="5000,00", nivel_acesso="2"))
        self.assertEqual(r.status_code, 400)
        nivel = db.execute("SELECT nivel_acesso FROM colaborador WHERE matricula=?", (self.admin,)).fetchone()[0]
        self.assertEqual(nivel, 1)


class LancamentosTest(BaseCorrecoes):
    """CT051."""

    def test_tela_de_lancamentos_em_mes_aberto_e_fechado(self):
        adm, p, f = self.gerar_e_lancar()
        r = adm.get(f"/folha/{p}/lancamentos")
        self.assertEqual(r.status_code, 200)
        html = r.get_data(as_text=True)
        self.assertIn("Lançamentos de Março/2026", html)
        self.assertIn("Salvar e recalcular", html)
        self.post(adm, f"/folha/{p}/fechar")
        html = adm.get(f"/folha/{p}/lancamentos").get_data(as_text=True)
        self.assertIn("Mês fechado", html)
        self.assertNotIn("Salvar e recalcular", html)

    def test_texto_no_lugar_de_numero_nao_salva_nada(self):
        adm, p, f = self.gerar_e_lancar(vendas="5000,00", qtd="100")
        self.post(adm, f"/folha/{p}/lancamentos",
                  {f"vendas_{f[self.joao]}": "abc", f"qtd_{f[self.maria]}": "dez"})
        db = get_db()
        vendas = db.execute("SELECT vendas_centavos FROM folha WHERE id=?", (f[self.joao],)).fetchone()[0]
        qtd = db.execute("SELECT quantidade_produzida FROM folha WHERE id=?", (f[self.maria],)).fetchone()[0]
        self.assertEqual((vendas, qtd), (500000, 100))


class ForcaTrocaSenhaTest(BaseCorrecoes):
    """CT052 e CT053 - BUG002: a senha inicial (data de nascimento) precisa ser trocada no 1º login."""

    def _entrar_sem_liberar(self, matricula, senha="15031990"):
        c = self.app.test_client()
        html = c.get("/login").get_data(as_text=True)
        token = re.search(r'name="csrf_token" value="([^"]+)"', html).group(1)
        r = c.post("/login", data={"matricula": matricula, "senha": senha, "csrf_token": token})
        return c, r

    def test_login_com_senha_inicial_exige_a_troca(self):
        c, r = self._entrar_sem_liberar(self.admin)
        self.assertEqual(r.status_code, 302)
        self.assertIn("/senha", r.headers["Location"])
        r = c.get("/colaboradores")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/senha", r.headers["Location"])
        self.assertEqual(c.get("/senha").status_code, 200)

    def test_trocar_a_senha_libera_o_acesso(self):
        c, _ = self._entrar_sem_liberar(self.joao)
        r = self.post(c, "/senha", {"atual": "15031990", "nova": "nova1234", "confirma": "nova1234"})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(c.get("/meus-dados").status_code, 200)

    def test_nova_senha_nao_pode_ser_a_inicial(self):
        c, _ = self._entrar_sem_liberar(self.joao)
        r = self.post(c, "/senha", {"atual": "15031990", "nova": "15031990", "confirma": "15031990"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(c.get("/meus-dados").status_code, 302)  # continua bloqueado

    def test_com_senha_ja_trocada_entra_direto(self):
        c, _ = self._entrar_sem_liberar(self.joao)
        self.post(c, "/senha", {"atual": "15031990", "nova": "nova1234", "confirma": "nova1234"})
        c2, r = self._entrar_sem_liberar(self.joao, "nova1234")
        self.assertEqual(r.status_code, 302)
        self.assertNotIn("/senha", r.headers["Location"])
        self.assertEqual(c2.get("/meus-dados").status_code, 200)

    def test_redefinicao_pelo_rh_volta_a_exigir_a_troca(self):
        c, _ = self._entrar_sem_liberar(self.joao)
        self.post(c, "/senha", {"atual": "15031990", "nova": "nova1234", "confirma": "nova1234"})
        adm = self.cliente(self.admin)
        self.post(adm, f"/colaboradores/{self.joao}/redefinir-senha")
        c3, _ = self._entrar_sem_liberar(self.joao)
        self.assertEqual(c3.get("/meus-dados").status_code, 302)

    def test_tela_de_login_nao_exibe_credencial_do_admin(self):
        html = self.app.test_client().get("/login").get_data(as_text=True)
        self.assertNotIn("01012000", html)
        self.assertNotIn("Primeiro acesso", html)


class PrimeiraExecucaoTest(unittest.TestCase):
    """CT037-A: banco novo cria o administrador (1 / 01012000) e o 1º login obriga a trocar a senha."""

    def test_banco_novo_cria_admin_e_exige_troca(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = os.path.join(pasta, "novo.db")
            app = create_app({"TESTING": True, "SECRET_KEY": "teste", "DATABASE": caminho})
            self.assertTrue(os.path.exists(caminho))
            with app.app_context():
                a = get_db().execute(
                    "SELECT nivel_acesso, status FROM colaborador WHERE matricula = 1").fetchone()
                self.assertEqual((a["nivel_acesso"], a["status"]), (1, "Ativo"))
            c = app.test_client()
            html = c.get("/login").get_data(as_text=True)
            token = re.search(r'name="csrf_token" value="([^"]+)"', html).group(1)
            r = c.post("/login", data={"matricula": "1", "senha": "01012000", "csrf_token": token})
            self.assertEqual(r.status_code, 302)
            self.assertIn("/senha", r.headers["Location"])
            self.assertIn("/senha", c.get("/colaboradores").headers["Location"])


class ListaEReciboTest(BaseCorrecoes):
    """CT009 e CT029-M: conteúdo da lista de colaboradores e do recibo."""

    def test_lista_de_colaboradores_para_rh_e_financeiro(self):
        for m in (self.admin, self.fin):
            r = self.cliente(m).get("/colaboradores")
            self.assertEqual(r.status_code, 200)
            html = r.get_data(as_text=True)
            for esperado in ("Matrícula", "Joao Comum", "Comissionado", "R$ 3.000,00", "Ativo"):
                self.assertIn(esperado, html)

    def test_recibo_mostra_os_campos_e_o_botao_imprimir(self):
        adm, p, f = self.gerar_e_lancar()
        aberto = adm.get(f"/folha/{f[self.joao]}").get_data(as_text=True)
        self.assertIn("PRÉVIA", aberto)
        self.post(adm, f"/folha/{p}/fechar")
        html = self.cliente(self.joao).get(f"/folha/{f[self.joao]}").get_data(as_text=True)
        for esperado in ("RECIBO DE PAGAMENTO", "Matrícula", "Joao Comum", "Comissionado",
                         "Salário base", "R$ 3.000,00", "Vendas no mês", "R$ 5.000,00",
                         "LÍQUIDO A RECEBER", "R$ 3.150,00", "data-print"):
            self.assertIn(esperado, html)
        self.assertNotIn("PRÉVIA", html)


class ReativacaoETermoDeContratoTest(BaseCorrecoes):
    """CT056 (BUG004) e CT057 (BUG005)."""

    def test_reativar_preserva_folhas_fechadas_e_volta_a_entrar_nas_novas(self):
        adm, p, f = self._fechar_marco()
        self.post(adm, f"/colaboradores/{self.padrao}/desabilitar")
        db = get_db()
        self.assertIsNotNone(db.execute("SELECT data_fim_contrato FROM colaborador WHERE matricula=?",
                                        (self.padrao,)).fetchone()[0])
        self.post(adm, f"/colaboradores/{self.padrao}/reativar")
        c = db.execute("SELECT status, data_fim_contrato FROM colaborador WHERE matricula=?",
                       (self.padrao,)).fetchone()
        self.assertEqual((c["status"], c["data_fim_contrato"]), ("Ativo", None))
        fo = db.execute("SELECT total_centavos FROM folha WHERE id=?", (f[self.padrao],)).fetchone()
        self.assertEqual(fo["total_centavos"], 250000)  # folha fechada continua igual
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 5})
        n = db.execute("SELECT COUNT(*) FROM folha f JOIN periodo p ON p.id=f.periodo_id "
                       "WHERE p.mes=5 AND f.matricula=?", (self.padrao,)).fetchone()[0]
        self.assertEqual(n, 1)

    def test_gerar_remove_da_folha_aberta_quem_perdeu_o_contrato_no_mes(self):
        adm, p, f = self.gerar_e_lancar()
        db = get_db()
        db.execute("UPDATE colaborador SET data_fim_contrato='2026-02-28' WHERE matricula=?", (self.padrao,))
        db.commit()
        self.post(adm, "/folha/gerar", {"ano": 2026, "mes": 3})
        n = db.execute("SELECT COUNT(*) FROM folha WHERE periodo_id=? AND matricula=?",
                       (p, self.padrao)).fetchone()[0]
        self.assertEqual(n, 0)
        n = db.execute("SELECT COUNT(*) FROM folha WHERE periodo_id=?", (p,)).fetchone()[0]
        self.assertEqual(n, 4)  # os demais continuam


class ImpressaoTest(unittest.TestCase):
    """CT030: regras de impressão do CSS e botões de impressão nas telas (a pré-visualização
    visual fica no roteiro de demonstração)."""

    def test_css_de_impressao_oculta_menu_e_botoes(self):
        pasta = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app")
        with open(os.path.join(pasta, "static", "style.css"), encoding="utf-8") as f:
            css = f.read()
        bloco = css[css.index("@media print"):]
        for seletor in (".navbar", "button", ".filtros"):
            self.assertIn(seletor, bloco)
        self.assertIn("display:none", bloco.replace(" ", ""))
        for tela in ("recibo.html", "relatorio.html"):
            with open(os.path.join(pasta, "templates", tela), encoding="utf-8") as f:
                html = f.read()
            self.assertIn("data-print", html)


if __name__ == "__main__":
    unittest.main()
