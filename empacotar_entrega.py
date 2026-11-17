"""Monta os ZIPs da entrega SEM banco, chave secreta nem arquivos temporários.

Uso (na raiz do projeto, depois de rodar gerar_cobertura.py):   python empacotar_entrega.py
Gera:
  07_Executavel/Projeto_FolhaPagamento_Executavel.zip   pacote pronto para uso (código + instalação + manuais)
  ../Projeto_FolhaPagamento_v1.3-A3.zip                 projeto completo para enviar ao avaliador
Fora dos dois ZIPs: .git, instance/ (banco e secret.key), htmlcov/, .coverage, __pycache__/, .venv/, *.pyc, *.db, ZIPs.
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


def nome_no_zip(f: Path, prefixo: str) -> str:
    """Atalhos .bat entram como iniciar(.bat): e-mail e antivírus costumam barrar .bat dentro de ZIP.
    O Manual do Usuário e o README explicam como renomear (ou use python run.py)."""
    rel = f.relative_to(RAIZ).as_posix()
    if rel.endswith(".bat"):
        rel = rel[:-4] + "(.bat)"
    return f"{prefixo}/{rel}"


def zipar(destino: Path, arquivos, prefixo: str):
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(arquivos):
            z.write(f, nome_no_zip(f, prefixo))
    print(f"[ok] {destino}  ({len(arquivos)} arquivos)")


def main():
    todos = [p for p in RAIZ.rglob("*") if incluir(p)]
    executavel = [p for p in todos if p.relative_to(RAIZ).parts[0] in ("05_Codigo_Fonte", "06_Banco_Dados", "08_Manuais")
                  or p.name in ("README.md",) and p.parent == RAIZ]
    destino_exe = RAIZ / "07_Executavel" / "Projeto_FolhaPagamento_Executavel.zip"
    destino_exe.parent.mkdir(exist_ok=True)
    zipar(destino_exe, executavel, NOME)
    # o ZIP do executável entra no ZIP completo (07_Executavel/), que por isso inclui esse único .zip
    completo = RAIZ.parent / f"{NOME}_v1.3-A3.zip"
    arquivos = todos + [destino_exe]
    zipar(completo, arquivos, NOME)
    sensiveis = [n for n in zipfile.ZipFile(completo).namelist()
                 if set(n.split("/")) & (PASTAS_FORA | ARQUIVOS_FORA) or n.endswith((".db", ".pyc"))]
    if sensiveis:
        print("ERRO: arquivos indevidos no pacote:", sensiveis)
        return 1
    print("Conferência: nenhum banco, chave secreta ou arquivo temporário no pacote.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
