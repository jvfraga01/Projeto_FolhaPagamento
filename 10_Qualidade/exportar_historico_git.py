"""Gera 10_Qualidade/Historico_Git.md com a evidência do controle de versão.

Uso (de qualquer pasta dentro do repositório):   python 10_Qualidade/exportar_historico_git.py
Escreve em UTF-8, sem depender do console do Windows.
"""
import datetime
import subprocess
import sys
from pathlib import Path


def git(*args, raiz):
    r = subprocess.run(["git", "--no-pager", *args], cwd=raiz, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"Erro ao rodar git {' '.join(args)}:\n{r.stderr}")
    return r.stdout.rstrip()


def main():
    aqui = Path(__file__).resolve().parent
    raiz = Path(git("rev-parse", "--show-toplevel", raiz=aqui))
    saida = raiz / "10_Qualidade" / "Historico_Git.md"
    partes = [
        "# Histórico do Git", "",
        f"Exportado em: {datetime.datetime.now():%d/%m/%Y %H:%M}", "", "```text",
        "== Repositório remoto ==", git("remote", "-v", raiz=raiz), "",
        "== Ramos ==", git("branch", "-a", raiz=raiz), "",
        "== Tags ==", git("tag", "-n", raiz=raiz), "",
        "== Commits (hash | autor | data | mensagem) ==",
        git("log", "--date=iso", "--pretty=format:%h | %an | %ad | %s", raiz=raiz), "",
        "== Commits por autor ==", git("shortlog", "-sn", "HEAD", raiz=raiz),
        "```", "",
    ]
    saida.write_text("\n".join(partes), encoding="utf-8")
    print(f"Arquivo gerado: {saida}")


if __name__ == "__main__":
    main()
