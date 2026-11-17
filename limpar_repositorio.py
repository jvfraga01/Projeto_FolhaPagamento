"""Remove da pasta do projeto os arquivos antigos que voltaram com o histórico recuperado.
Uso (na RAIZ do projeto, depois de copiar o conteúdo da restauração por cima):  python limpar_repositorio.py
Mostra o que removeu. Seguro rodar mais de uma vez. Depois: git add -A  e  git status."""
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
T = ".t" + "xt"  # montado assim para o conversor de .txt não reescrever esta lista
ARQUIVOS = [
    "gitignore" + T, "gitattributes" + T,
    "06_Banco_Dados/LEIA-ME.md", "07_Executavel/LEIA-ME.md", "07_Executavel/Readme.md",
    "08_Manuais/LEIA-ME.md", "09_Homologacao/LEIA-ME.md", "10_Qualidade/LEIA-ME.md", "11_Apresentacao/LEIA-ME.md",
    "10_Qualidade/Ata_de_Revisao_Tecnica_A1", "10_Qualidade/Historico_Git" + T,
    "04_Testes/evidencias/saida_unittest" + T, "04_Testes/evidencias/cobertura" + T,
    "04_Testes/evidencias/resumo_execucao" + T, "04_Testes/Execucao_Testes_A1" + T,
    "Projeto_FolhaPagamento-1.0(Estrutura inicial do projeto.).zip",
]
PASTAS = ["Evidencias", "04_Testes/Prints"]  # duplicadas: as capturas ficam em 04_Testes/evidencias/Prints
removidos = 0
for rel in ARQUIVOS:
    p = RAIZ / rel
    if p.exists():
        p.unlink(); print("[removido]", rel); removidos += 1
for rel in PASTAS:
    p = RAIZ / rel
    if p.is_dir():
        shutil.rmtree(p); print("[removida pasta]", rel); removidos += 1
print(f"{removidos} item(ns) removido(s).")
