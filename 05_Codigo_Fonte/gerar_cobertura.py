"""Roda a suíte de testes COM cobertura e grava as evidências em 04_Testes/evidencias/.

Uso (dentro de 05_Codigo_Fonte):   python gerar_cobertura.py [--executor "Nome"]   (ou dois cliques em gerar_cobertura.bat)

Gera:
  04_Testes/evidencias/saida_unittest.md     saída completa do `unittest discover -v`
  04_Testes/evidencias/cobertura.md          `coverage report -m` (por arquivo, com linhas não cobertas)
  04_Testes/evidencias/resumo_execucao.md    data/hora, versões, nº de testes, resultado e % total
  05_Codigo_Fonte/htmlcov/index.html          relatório navegável (não versionado)
Depois de gravar as evidências, chama atualizar_documentos.py, que copia os números reais para os documentos.
Tudo vem da execução real na máquina de quem rodou: nada é escrito à mão.
Código de saída: 0 = testes ok e cobertura >= meta; 1 = algum teste falhou; 2 = cobertura abaixo da meta.
"""
import argparse
import datetime
import getpass
import platform
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
EVID = AQUI.parent / "04_Testes" / "evidencias"
META = 80.0
PY = [sys.executable, "-m"]


def executar(args, **kw):
    return subprocess.run(PY + args, cwd=AQUI, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", **kw)


def garantir_coverage():
    if executar(["coverage", "--version"]).returncode == 0:
        return True
    print("O pacote 'coverage' não está instalado.")
    if input("Instalar agora? É preciso internet. [S/n] ").strip().lower() in ("n", "nao", "não"):
        return False
    r = subprocess.run(PY + ["pip", "install", "-r", str(AQUI / "requirements-dev.txt")], cwd=AQUI)
    return r.returncode == 0


def nome_do_executor():
    ap = argparse.ArgumentParser()
    ap.add_argument("--executor", default="")
    nome = ap.parse_args().executor.strip()
    if not nome and sys.stdin.isatty():
        nome = input("Nome de quem está rodando (Enter = usuário do sistema): ").strip()
    return nome or getpass.getuser()


def main():
    executor = nome_do_executor()
    if not garantir_coverage():
        print("Sem o coverage não há como medir. Veja INSTALACAO.md (seção Testes).")
        return 1
    EVID.mkdir(parents=True, exist_ok=True)
    inicio = datetime.datetime.now()
    executar(["coverage", "erase"])

    print("Rodando os testes com cobertura (pode levar alguns segundos)...")
    testes = executar(["coverage", "run", "--source=app", "-m", "pytest", "-v", "tests"])
    saida = (testes.stdout or "") + (testes.stderr or "")
    (EVID / "saida_unittest.md").write_text(saida, encoding="utf-8")

    rel = executar(["coverage", "report", "-m"])
    (EVID / "cobertura.md").write_text(rel.stdout or rel.stderr, encoding="utf-8")
    executar(["coverage", "html", "-d", "htmlcov"])

    m_ran = re.search(r"(\d+) passed", saida)
    ultima = [l for l in saida.strip().splitlines() if l.strip()][-1:] or ["(sem saída)"]
    m_tot = re.search(r"^TOTAL\s+.*?(\d+(?:\.\d+)?)%\s*$", rel.stdout or "", re.M)
    total = float(m_tot.group(1)) if m_tot else None
    testes_ok = testes.returncode == 0

    linhas = [
        f"Execução em: {inicio:%d/%m/%Y %H:%M}",
        f"Python: {platform.python_version()} | Sistema: {platform.platform()}",
        f"Testes executados: {m_ran.group(1) if m_ran else 'não identificado'}",
        f"Resultado do pytest: {ultima[0]}",
        f"Cobertura total (app/): {f'{total:.1f}%' if total is not None else 'não identificada'}"
        f" (meta {META:.0f}%)",
        f"Meta de cobertura atingida: {'SIM' if total is not None and total >= META else 'NÃO'}",
        f"Executor: {executor}",
    ]
    (EVID / "resumo_execucao.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")

    print("\n" + (rel.stdout or rel.stderr))
    print("\n".join(linhas))
    try:
        import atualizar_documentos
        atualizar_documentos.aplicar(atualizar_documentos.evidencias())
    except Exception as erro:  # a evidência já está gravada; o erro só impede a cópia para os documentos
        print(f"\nAviso: não foi possível atualizar os documentos ({erro}). Rode atualizar_documentos.py.")
    print(f"\nEvidências em: {EVID}\nRelatório navegável: {AQUI / 'htmlcov' / 'index.html'}")
    if not testes_ok:
        print("\nATENÇÃO: há testes falhando. Veja saida_unittest.md e corrija o CÓDIGO, não o teste.")
        return 1
    if total is None or total < META:
        print("\nATENÇÃO: cobertura abaixo da meta. A coluna 'Missing' de cobertumd mostra as linhas sem teste.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
