# Relatório de Testes

Modelo: Anexo I, item 10, mais os relatórios de execução (6.3) e de integração (6.4) do enunciado.
Os números deste relatório são **copiados automaticamente** de `04_Testes/evidencias/` por `05_Codigo_Fonte/atualizar_documentos.py`, que roda no fim de `gerar_cobertura.py`. Nada é digitado à mão.

## 1. Execução automatizada
| Item | Valor |
|---|---|
| Data e hora | <!--A:data-->12/11/2026 19:24<!--/A--> |
| Executor | <!--A:executor-->Pedro da Silva Kolling<!--/A--> |
| Python / sistema | <!--A:ambiente-->3.13.3 / Windows-11-10.0.26200-SP0<!--/A--> |
| Comando | `python gerar_cobertura.py` (`coverage run --source=app -m unittest discover -v`) |
| Testes executados | <!--A:testes-->?<!--/A--> |
| Resultado | <!--A:resultado-->======================== 74 passed in 61.83s (0:01:01) ========================<!--/A--> |
| Cobertura total (`app/`) | <!--A:cobertura-->92%<!--/A--> (<!--A:stmts-->634<!--/A--> linhas, <!--A:miss-->48<!--/A--> sem cobertura); meta de 80% |
| Evidências brutas | `evidencias/saida_unittest.md`, `evidencias/cobertura.md`, `evidencias/resumo_execucao.md` |

## 2. Cobertura por arquivo
<!--AUTO:tabela_cobertura-->
| Arquivo | Linhas | Sem cobertura | Cobertura | Linhas não cobertas |
|---|---|---|---|---|
| `app/__init__.py` | 92 | 12 | 87% | 17-20, 116-120, 128-130 |
| `app/auth.py` | 77 | 1 | 99% | 48 |
| `app/colaboradores.py` | 159 | 12 | 92% | 28-29, 32, 34, 38-40, 43, 81, 110-111, 182 |
| `app/db.py` | 26 | 0 | 100% | — |
| `app/folha.py` | 172 | 19 | 89% | 17, 72-74, 76-77, 79-84, 116, 145-148, 249, 251 |
| `app/regras.py` | 108 | 4 | 96% | 37, 55, 82-83 |
| **Total** | **634** | **48** | **92%** | |
<!--/AUTO-->

## 3. Níveis de teste: unitário, integração e sistema (6.3 e 6.4)
Todas as classes abaixo estão em `05_Codigo_Fonte/tests/`. Resultado de cada nível = resultado da execução da seção 1 (todos os testes da suíte passam ou a suíte inteira é marcada como falha).

| Nível | Classes de teste | Testes | O que cobre |
|---|---|---|---|
| **Unitário** (sem banco nem web) | `CalculoTest`, `RegimeMetasTest`, `MilharTest` | 20 | Cálculo das 3 remunerações, arredondamento, negativos, zero, novo calculador, modo opcional de metas, conversão de dinheiro e percentual |
| **Integração: persistência** | `PersistenciaTest`, `PrimeiraExecucaoTest`, `BancoFolhaFechadaTest` | 5 | Dados sobrevivem a reabrir a aplicação; banco novo cria o admin; triggers do banco recusam alterar mês fechado |
| **Integração: fluxos de negócio** | `FolhaTest`, `FolhaRegimeMetasTest`, `LancamentosTest`, `ReativacaoETermoDeContratoTest`, `EdicaoTest`, `CadastroMilharTest`, `FiltrosTest` | 26 | Cadastro, alteração, filtros, gerar → lançar → fechar, reativar, fim de contrato |
| **Integração: relatórios e recibos** | `ListaEReciboTest` | 2 | Lista de colaboradores e recibo (o resumo do relatório, total 16.900,00, é verificado em `FolhaTest` e `FiltrosTest`) |
| **Integração: segurança entre componentes** | `LoginTest`, `PermissaoTest`, `SenhaTest`, `ForcaTrocaSenhaTest` | 20 | Login, CSRF, 403 sem dados, troca e redefinição de senha, troca obrigatória |
| **Sistema (interface estática)** | `ImpressaoTest` | 1 | CSS de impressão e botões de imprimir |

Soma por nível: 20 + 5 + 26 + 2 + 20 + 1 = 74 testes no código. O total executado na última medição é o da seção 1 (a tabela só muda quando testes são adicionados).

## 4. Casos manuais
Os casos que dependem de uma pessoa (CT037-M e CT039) e seus resultados estão em `09_Homologacao/Testes_de_Aceitacao.md`, seção C. A persistência com `iniciar.bat` faz parte do CT037-M.

## 5. Indicadores dos casos de teste (Anexo I)
Contagens e percentuais calculados no bloco de métricas de `10_Qualidade/Metricas_e_Indicadores.md`.
