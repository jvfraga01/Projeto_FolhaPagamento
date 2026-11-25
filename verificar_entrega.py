"""Confere o projeto ANTES do commit final e do ZIP. Uso (na raiz do projeto):  python verificar_entrega.py
Mostra o que falta, o que sobrou e o que ainda está sem preencher. Não altera nada. Código de saída 1 se houver erro."""
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
OBRIGATORIOS = """README.md
01_Requisitos/Documento_de_Visao.md 01_Requisitos/ERS.md 01_Requisitos/Registro_de_Aceite_de_Desvios.md
02_Analise/Casos_de_Uso.md 02_Analise/Diagramas_UML.md
03_Projeto/Documento_de_Arquitetura.md 03_Projeto/Planejamento_do_Projeto.md
04_Testes/Plano_de_Testes.md 04_Testes/Casos_de_Teste.md 04_Testes/Relatorio_de_Testes.md
04_Testes/evidencias/saida_unittest.md 04_Testes/evidencias/cobertura.md 04_Testes/evidencias/resumo_execucao.md
05_Codigo_Fonte/run.py 05_Codigo_Fonte/gerar_cobertura.py 05_Codigo_Fonte/atualizar_documentos.py
05_Codigo_Fonte/tests/test_sistema.py 05_Codigo_Fonte/tests/test_correcoes_a3.py 05_Codigo_Fonte/INSTALACAO.md
06_Banco_Dados/schema.sql 07_Executavel/README.md
08_Manuais/Manual_do_Usuario.md 08_Manuais/Manual_Tecnico.md
09_Homologacao/Testes_de_Aceitacao.md 09_Homologacao/Termo_de_Homologacao.md
10_Qualidade/Plano_de_Garantia_da_Qualidade.md 10_Qualidade/Registro_de_Defeitos.md 10_Qualidade/Metricas_e_Indicadores.md
10_Qualidade/Relatorio_de_Revisao_Tecnica.md 10_Qualidade/Relatorio_Final_de_Qualidade.md
10_Qualidade/Ata_de_Revisao_Tecnica_A1.md 10_Qualidade/Evidencia_Controle_de_Versao.md 10_Qualidade/Historico_Git.md""".split()
T = ".t" + "xt"  # montado assim para o conversor de .txt->.md não reescrever esta lista
SOBRANDO = ["gitignore" + T, "gitattributes" + T, "10_Qualidade/Ata_de_Revisao_Tecnica_A1",
            "10_Qualidade/Historico_Git" + T, "04_Testes/evidencias/saida_unittest" + T,
            "04_Testes/evidencias/cobertura" + T, "04_Testes/evidencias/resumo_execucao" + T,
            "Projeto_FolhaPagamento-1.0(Estrutura inicial do projeto.).zip"]
erros, avisos = [], []

for f in OBRIGATORIOS:
    if not (RAIZ / f).exists():
        erros.append(f"FALTA: {f}")
for f in SOBRANDO:
    if (RAIZ / f).exists():
        erros.append(f"SOBRA (apagar ou converter): {f}")
for p in RAIZ.rglob("LEIA-ME.md"):
    erros.append(f"SOBRA (duplicado): {p.relative_to(RAIZ)}")
for p in RAIZ.rglob("*"):
    partes = set(p.relative_to(RAIZ).parts)
    if p.is_file() and (partes & {"instance", "htmlcov", "__pycache__"} or p.name in (".coverage", "secret.key") or p.suffix in (".db", ".pyc")):
        if ".git" not in partes:
            avisos.append(f"arquivo local que não deve ir no ZIP (o empacotar_entrega.py o exclui): {p.relative_to(RAIZ)}")
for f in ("README.md", ".gitignore", ".gitattributes"):
    if f != "README.md" and not (RAIZ / f).exists():
        avisos.append(f"na raiz falta {f} (o gitignore.txt/gitattributes.txt não têm efeito)")

# campos em branco
vazios = {}
for p in RAIZ.rglob("*.md"):
    if ".git" in p.relative_to(RAIZ).parts or p.name == "Historico_Git.md":
        continue
    n = len(re.findall(r"<<PREENCHER", p.read_text(encoding="utf-8", errors="ignore")))
    if n:
        vazios[str(p.relative_to(RAIZ))] = n
for f, n in sorted(vazios.items()):
    avisos.append(f"{n} campo(s) <<PREENCHER>> em {f}")

# números coerentes com as evidências
ev = RAIZ / "04_Testes" / "evidencias"
if (ev / "saida_unittest.md").exists():
    saida = (ev / "saida_unittest.md").read_text(encoding="utf-8")
    m = re.search(r"Ran (\d+) tests?", saida) or re.search(r"(\d+) passed", saida)
    if not m:
        erros.append("evidencias/saida_unittest.md não tem o resumo dos testes (nenhum teste rodou?)")
    elif re.search(r"Ran \d+ tests?", saida) and not re.search(r"^OK\s*$", saida, re.M):
        erros.append("a última execução em evidencias/saida_unittest.md NÃO terminou em OK")
    elif re.search(r"\d+ (failed|error)", saida):
        erros.append("a última execução em evidencias/saida_unittest.md tem testes falhando")
    if m:
        dispersos = set()
        for p in RAIZ.rglob("*.md"):
            t = p.read_text(encoding="utf-8", errors="ignore")
            for v in re.findall(r"<!--A:testes-->(.*?)<!--/A-->", t):
                if v != m.group(1):
                    dispersos.add(str(p.relative_to(RAIZ)))
        for p in sorted(dispersos):
            erros.append(f"número de testes desatualizado em {p}: rode gerar_cobertura.py")
        atual = sum(len(re.findall(r"^    def test_", (RAIZ / "05_Codigo_Fonte/tests" / f).read_text(encoding="utf-8"), re.M))
                    for f in ("test_sistema.py", "test_correcoes_a3.py") if (RAIZ / "05_Codigo_Fonte/tests" / f).exists())
        if atual and str(atual) != m.group(1):
            erros.append(f"o código tem {atual} testes, mas a última execução registrada tem {m.group(1)}: rode gerar_cobertura.py de novo")

# referências quebradas e pacote de testes
if not (RAIZ / "05_Codigo_Fonte" / "tests" / "__init__.py").exists():
    erros.append("FALTA 05_Codigo_Fonte/tests/__init__.py: sem ele o unittest roda 0 testes")
for p in RAIZ.rglob("*"):
    if p.is_file() and p.suffix in (".md", ".py", ".bat", ".sh", ".txt") and ".git" not in p.parts and p.name not in ("Historico_Git.md", "verificar_entrega.py"):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"requirements(-dev)?\.md", txt):
            erros.append(f"referência a requirements.md (o arquivo é .txt): {p.relative_to(RAIZ)}")

# limpeza: .bat, executável e pasta 11 não podem mais ser citados (exceto nos arquivos que explicam a dispensa)
EXCECOES = {"verificar_entrega.py", "Historico_Git.md", "Registro_de_Aceite_de_Desvios.md",
            "Relatorio_de_Revisao_Tecnica.md", "Sequencia_das_Evidencias_MM01_MM02.md"}
for p in RAIZ.rglob("*"):
    rel = p.relative_to(RAIZ)
    if (p.is_file() and p.suffix in (".md", ".py", ".sh", ".yml") and ".git" not in rel.parts
            and p.name not in EXCECOES and str(rel) != "README.md"):
        for n, linha in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if re.search(r"\.bat\b|Executavel\.zip|11_Apresentacao", linha):
                erros.append(f"citação de .bat, executável ou pasta 11 em {rel}:{n}")

# placeholders no formato errado (um < só, sem <<, ou >> sobrando)
for p in RAIZ.rglob("*.md"):
    if ".git" in p.parts or p.name == "Historico_Git.md":
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"(?<!<<)PREENCHER", t) or re.search(r">>>", t):
        erros.append(f"placeholder PREENCHER fora do formato <<PREENCHER: ...>> em {p.relative_to(RAIZ)}")

# Termo: decisão marcada exige a resposta do professor guardada em 09_Homologacao/evidencias/
termo = RAIZ / "09_Homologacao" / "Termo_de_Homologacao.md"
if termo.exists():
    tt = termo.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"- \[[xX]\]", tt):
        arqs = re.findall(r"09_Homologacao/evidencias/[^\s`|<>]+", tt)
        # o print de 23/11 é só a conversa que combinou o e-mail; não vale como resposta da homologação
        if not any((RAIZ / a).exists() and "23-11-2026" not in a for a in arqs):
            erros.append("Termo com decisão marcada, mas sem a resposta do professor em 09_Homologacao/evidencias/")

# hashes citados em Termo, Ata e Evidência precisam existir no Historico_Git.md
hist = RAIZ / "10_Qualidade" / "Historico_Git.md"
if hist.exists():
    ht = hist.read_text(encoding="utf-8", errors="ignore")
    for f in ("09_Homologacao/Termo_de_Homologacao.md", "10_Qualidade/Ata_de_Revisao_Tecnica_A1.md",
              "10_Qualidade/Evidencia_Controle_de_Versao.md"):
        if (RAIZ / f).exists():
            for h in set(re.findall(r"\b[0-9a-f]{7,40}\b", (RAIZ / f).read_text(encoding="utf-8", errors="ignore"))):
                if re.search(r"\d", h) and re.search(r"[a-f]", h) and h not in ht:
                    erros.append(f"hash {h} citado em {f} não existe no Historico_Git.md")

# git
if (RAIZ / ".git").exists():
    def git(*a):
        return subprocess.run(["git", *a], cwd=RAIZ, capture_output=True, text=True).stdout
    pendentes = git("status", "--porcelain").splitlines()
    for l in pendentes[:8]:
        avisos.append(f"git, ainda não commitado: {l}")
    if len(pendentes) > 8:
        avisos.append(f"git: mais {len(pendentes) - 8} arquivo(s) não commitado(s) (rode git status)")
    rastreados = [x for x in git("ls-files").splitlines() if re.search(r"instance/|secret\.key|\.db$|(^|/)\.coverage$|htmlcov/|__pycache__", x)]
    for x in rastreados:
        erros.append(f"git rastreia arquivo que não deveria: {x}")
    if "v1.3-A3" not in git("tag").split():
        avisos.append("a tag v1.3-A3 ainda não existe")

print(f"{len(erros)} erro(s), {len(avisos)} aviso(s)\n")
for e in erros:
    print("ERRO  ", e)
for a in avisos:
    print("AVISO ", a)
if not erros and not avisos:
    print("Tudo certo: pode gerar o ZIP com empacotar_entrega.py.")
raise SystemExit(1 if erros else 0)
