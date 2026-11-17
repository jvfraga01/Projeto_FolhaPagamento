@echo off
rem Gera 10_Qualidade\Historico_Git.md (chama o script Python, que escreve em UTF-8).
cd /d "%~dp0"
where py >nul 2>nul && (py exportar_historico_git.py) || (python exportar_historico_git.py)
pause
