@echo off
rem Gera 10_Qualidade\Historico_Git.txt com a evidencia do controle de versao.
rem Execute dentro do repositorio Git (raiz do projeto).
set SAIDA=10_Qualidade\Historico_Git.txt
(
  echo Exportado em: %date% %time%
  echo.
  echo == Repositorio remoto ==
  git --no-pager remote -v
  echo.
  echo == Ramos ==
  git --no-pager branch -a
  echo.
  echo == Tags ==
  git --no-pager tag -n
  echo.
  echo == Commits - hash, autor, data e mensagem ==
  git --no-pager log --date=iso --pretty=format:"%%h | %%an | %%ad | %%s"
  echo.
  echo.
  echo == Commits por autor ==
  git --no-pager shortlog -sn HEAD
) > %SAIDA%
echo Arquivo gerado: %SAIDA%
pause
