"""Monta o ZIP da entrega SEM banco, chave secreta nem arquivos temporários.

Uso (na raiz do projeto, depois de rodar gerar_cobertura.py):   python empacotar_entrega.py
Gera:
  ../Projeto_FolhaPagamento_v1.3-A3.zip   projeto completo para enviar ao avaliador
Fora do ZIP: .git, instance/ (banco e secret.key), htmlcov/, .coverage, __pycache__/, .venv/, *.pyc, *.db, ZIPs.
"""
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
NOME = RAIZ.name
PASTAS_FORA = {".git", "instance", "htmlcov", "__pycache__", ".venv", ".pytest_cache"}
ARQUIVOS_FORA = {".coverage", "secret.key"}
SUFIXOS_FORA = {".pyc", ".db", ".zip"}


def incluir(caminho: Path) -> bool:
    partes = set(caminho.relative_to(RAIZ).parts)
    return (caminho.is_file() and not (partes & PASTAS_FORA) and caminho.name not in ARQUIVOS_FORA
            and caminho.suffix not in SUFIXOS_FORA)


def zipar(destino: Path, arquivos, prefixo: str):
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(arquivos):
            z.write(f, f"{prefixo}/{f.relative_to(RAIZ).as_posix()}")
    print(f"[ok] {destino}  ({len(arquivos)} arquivos)")


def main():
    todos = [p for p in RAIZ.rglob("*") if incluir(p)]
    completo = RAIZ.parent / f"{NOME}_v1.3-A3.zip"
    zipar(completo, todos, NOME)
    nomes = zipfile.ZipFile(completo).namelist()
    sensiveis = [n for n in nomes
                 if set(n.split("/")) & (PASTAS_FORA | ARQUIVOS_FORA) or n.endswith((".db", ".pyc"))]
    if sensiveis:
        print("ERRO: arquivos indevidos no pacote:", sensiveis)
        return 1
    print("Conferência: nenhum banco, chave secreta ou arquivo temporário no pacote.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
