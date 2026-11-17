# Testes de Aceitação

Entregável A3 (6.5): cenário testado, resultado esperado, resultado obtido e situação final.
Regra deste arquivo: **só se escreve "Obtido" o que foi realmente observado**. Onde ainda não houve execução, fica `<<PREENCHER>>`.

## A. Critérios de aceitação do cliente (T1, seção 9)
Verificados pela suíte automatizada. Última execução registrada: 10/11/2026 (61 testes, todos OK; `04_Testes/evidencias/saida_unittest.txt`). A suíte atual tem 70 testes; reexecução: <<PREENCHER: após rodar gerar_cobertura.py>>.

| ID | Cenário (critério do cliente) | Esperado | Obtido | Situação | Casos |
|---|---|---|---|---|---|
| AC01 | Cadastrar os três tipos de colaborador | Padrão, Comissionado e Por Produção cadastrados com matrícula gerada | Testes automáticos aprovados em 10/11/2026 | Aprovado | CT001, CT002, CT003 |
| AC02 | Validar dados obrigatórios e valores inválidos | Nome vazio, valores negativos e texto no lugar de número recusados, nada gravado | Os casos CT004–CT007 e CT042 foram aprovados em 10/11/2026; CT046 e CT047 (valores com ponto de milhar e texto) são novos | Aprovado (CT046 e CT047 aguardam reexecução) | CT004–CT007, CT042, CT046, CT047 |
| AC03 | Calcular corretamente cada categoria | Padrão 3.000,00; Comissionado 3.150,00; Produção 1.247,50 (exemplos do T1) | Testes automáticos aprovados em 10/11/2026 | Aprovado | CT015–CT019 |
| AC04 | Gerar folha individual e consolidada | Folha do mês e recibo individual com os campos exigidos | Testes automáticos aprovados em 10/11/2026 (CT020, CT029-A); conteúdo do recibo em CT029-M, novo | Aprovado (CT029-M aguarda reexecução) | CT020, CT029-A, CT029-M |
| AC05 | Exibir o total geral da folha | Total geral 16.900,00 na massa padrão | Testes automáticos aprovados em 10/11/2026 | Aprovado | CT021 |
| AC06 | Permitir novos tipos de remuneração | Calculador novo registrado sem alterar os existentes | Testes automáticos aprovados em 10/11/2026 | Aprovado | CT031 |

## B. Casos que eram manuais e foram automatizados
Passam a valer como executados quando a suíte de 70 testes for rodada e registrada em `04_Testes/evidencias/`.

| ID | Caso | Cenário | Esperado | Obtido | Situação |
|---|---|---|---|---|---|
| MA01 | CT009 | RH e Financeiro abrem Colaboradores | Lista com matrícula, nome, tipo, salário e status | <<PREENCHER: após reexecução>> | <<PREENCHER>> |
| MA02 | CT012 | RH altera Paulo Padrao; folha fechada anterior permanece | Cadastro novo; folha fechada intacta | <<PREENCHER: após reexecução>> | <<PREENCHER>> |
| MA03 | CT023 | Troca e redefinição de senha | Troca exige senha atual; redefinição volta ao DDMMAAAA | <<PREENCHER: após reexecução>> | <<PREENCHER>> |
| MA04 | CT029-M | Conteúdo do recibo e botão Imprimir | Todos os campos do recibo; PRÉVIA só em mês aberto | <<PREENCHER: após reexecução>> | <<PREENCHER>> |
| MA05 | CT037-A | Banco novo cria admin e 1º login obriga a troca | Admin 1 / nível 1; redireciona para a troca de senha | <<PREENCHER: após reexecução>> | <<PREENCHER>> |
| MA06 | CT052, CT053 | Troca obrigatória da senha inicial (BUG002) | Fluxo bloqueado até trocar; login sem credenciais | <<PREENCHER: após reexecução>> | <<PREENCHER>> |
| MA07 | CT043 | Cobertura de testes | Total ≥ 80% | 92,2% (`evidencias/cobertura.txt`, execução de 10/11/2026 21:09, com 61 testes) | Aprovado (nova medição com 70 testes: <<PREENCHER>>) |
| MA08 | CT044 | Execução no Windows | Mesmo comportamento esperado | Suíte executada em Windows 11 / Python 3.13.3 em 10/11/2026, 61 testes OK | Aprovado |

Executor das execuções de 10/11/2026: João Vitor Fraga.

## C. Casos que dependem de uma pessoa (roteiros em `08_Manuais/` e abaixo)
| ID | Caso | Cenário | Esperado | Obtido | Situação | Data | Responsável |
|---|---|---|---|---|---|---|---|
| MM01 | CT030 | Pré-visualização de impressão do recibo e do relatório | Menu e botões ocultos; legível em preto e branco | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> |
| MM02 | CT037-M | Apagar `instance/`, dois cliques em `iniciar.bat`, entrar com 1 / 01012000 | Navegador abre sozinho; login; troca obrigatória de senha | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> |
| MM03 | CT039 | Roteiro de usabilidade (5 tarefas, 3 participantes que não desenvolveram) | Critério do Plano de Testes (seção Usabilidade) | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> |

## Resumo
| Indicador | Valor |
|---|---|
| Critérios do cliente aprovados | 6 de 6 (AC01–AC06, via suíte automática) |
| Casos antes manuais, hoje automatizados | 6 (aguardam reexecução da suíte) |
| Casos manuais restantes | 3 (CT030, CT037-M, CT039) |
