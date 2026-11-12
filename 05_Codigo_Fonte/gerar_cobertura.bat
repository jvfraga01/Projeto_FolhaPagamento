@echo off
chcp 65001 >nul
cd /d "%~dp0"
set "PY="
where py >nul 2>nul && set "PY=py"
if not defined PY where python >nul 2>nul && set "PY=python"
if not defined PY (
  echo Python nao encontrado. Veja INSTALACAO.md.
  pause
  exit /b 1
)
%PY% gerar_cobertura.py
pause
