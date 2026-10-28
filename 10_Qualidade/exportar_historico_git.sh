#!/usr/bin/env bash
# Gera 10_Qualidade/Historico_Git.txt com a evidência do controle de versão.
# Execute dentro do repositório Git (raiz do projeto).
set -e
SAIDA="10_Qualidade/Historico_Git.txt"
{
  echo "Exportado em: $(date '+%d/%m/%Y %H:%M')"
  echo; echo "== Repositório remoto =="; git remote -v
  echo; echo "== Ramos =="; git branch -a
  echo; echo "== Tags =="; git tag -n
  echo; echo "== Commits (hash | autor | data | mensagem) =="
  git --no-pager log --date=iso --pretty=format:'%h | %an | %ad | %s'
  echo; echo; echo "== Commits por autor =="; git shortlog -sn HEAD
} > "$SAIDA"
echo "Arquivo gerado: $SAIDA"
