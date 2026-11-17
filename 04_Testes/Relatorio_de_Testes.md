# Relatório de Testes

Modelo: Anexo I, item 10. Os números abaixo vêm da execução real de 10/11/2026 registrada em `04_Testes/evidencias/` (gerada por `05_Codigo_Fonte/gerar_cobertura.py`), feita **antes** da correção do BUG002. Depois dela, a suíte passou a ter 70 testes: rodar `gerar_cobertura.py` de novo e atualizar a seção "Reexecução" ao final.

## Execução automatizada
| Item | Valor |
|---|---|
| Data e hora | 10/11/2026 21:09 |
| Executor | João Vitor Fraga |
| Python / sistema | 3.13.3 / Windows 11 (10.0.26200) |
| Comando | `python gerar_cobertura.py` (`coverage run --source=app -m unittest discover -v`) |
| Testes executados | 61 (44 em `tests/test_sistema.py` + 17 em `tests/test_correcoes_a3.py`) |
| Testes no código hoje | 70 (44 + 26 em `tests/test_correcoes_a3.py`); os 9 novos cobrem BUG002, CT009, CT029-M e CT037-A |
| Resultado | OK: nenhum teste falhou |
| Cobertura total (`app/`) | 92,2% (619 linhas, 48 sem cobertura); meta de 80% atingida |
| Evidências | `evidencias/saida_unittest.txt`, `evidencias/cobertura.txt`, `evidencias/resumo_execucao.txt` |

## Cobertura por arquivo
| Arquivo | Linhas | Sem cobertura | Cobertura | Linhas não cobertas |
|---|---|---|---|---|
| `app/__init__.py` | 86 | 12 | 86,0% | 17-20, 108-112, 120-122 |
| `app/auth.py` | 76 | 1 | 98,7% | 47 |
| `app/colaboradores.py` | 159 | 12 | 92,5% | 28-29, 32, 34, 38-40, 43, 81, 110-111, 182 |
| `app/db.py` | 26 | 0 | 100,0% | — |
| `app/folha.py` | 168 | 19 | 88,7% | 17, 72-74, 76-77, 79-84, 116, 145-148, 242, 244 |
| `app/regras.py` | 104 | 4 | 96,2% | 35, 49, 76-77 |
| **Total** | **619** | **48** | **92,2%** | |

## Indicadores dos casos de teste (Anexo I)
| Indicador | Quantidade |
|---|---|
| Planejados | 53 casos (CT001–CT053) |
| Automatizados e aprovados em 10/11/2026 | os casos marcados "Auto" (61 testes, todos OK) |
| Executados por ferramenta | CT043 (cobertura: 92,2%) e CT044 (suíte no Windows 11) |
| Manuais pendentes | CT030, CT037-M, CT039: resultado em `09_Homologacao/Testes_de_Aceitacao.md` |
| Reprovados | 0 nos automatizados |

Contagem por linhas de `Casos_de_Teste.md`: <<PREENCHER: contar as linhas "Auto" e "Manual" após as alterações; no estado anterior eram 43 Auto + 9 Manual>>.

## Reexecução após a correção do BUG002 (70 testes)
| Item | Valor |
|---|---|
| Data, hora e executor | <<PREENCHER>> |
| Testes executados / resultado | <<PREENCHER: ex.: Ran 70 tests ... OK>> |
| Cobertura total (`app/`) | <<PREENCHER: % de `cobertura.txt`>> |
| Observação | Substituir as tabelas acima pelos números novos ou manter as duas execuções, com data. |
