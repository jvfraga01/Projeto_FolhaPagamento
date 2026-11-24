# Sequência das Evidências Manuais, rodada B: MM01-B (CT037-M) e MM02-B (CT039)

Esta rodada substitui a preliminar de 11/11/2026 (`Sequencia_das_Evidencias_MM01_MM02.md`, mantida como histórico). Ela é feita numa única sessão, com o ZIP final descompactado em pasta limpa e iniciado por `run.py`. As capturas ficam em `04_Testes/evidencias/Prints/` com os nomes abaixo. Todo campo `<<PREENCHER: ...>>` só pode ser preenchido com o que foi observado na sessão.

## 1. Identificação da rodada

| Campo | Valor |
|---|---|
| Data da sessão | <<PREENCHER: data real>> |
| Executor do MM01-B | <<PREENCHER: nome>> |
| Facilitador do MM02-B | <<PREENCHER: nome>> |
| Participantes (P1 RH, P2 Financeiro, P3 Colaborador nível 3) | <<PREENCHER: nomes e matrículas>> |
| Autorização do professor para participantes da equipe | <<PREENCHER: data>> |
| Sistema operacional | <<PREENCHER: edição e versão do Windows>> |
| Navegador | <<PREENCHER: nome e versão>> |
| Python | <<PREENCHER: saída de `python --version`>> |
| Flask | <<PREENCHER: versão da saída de `pip show flask`>> |
| Versão testada | <<PREENCHER: tag, commit ou SHA-256 do ZIP final>> |
| Resultado do MM01-B | <<PREENCHER: Aprovado ou Reprovado>> |
| Resultado do MM02-B | <<PREENCHER: Aprovado ou Reprovado>> |

## 2. MM01-B / CT037-M: abrir com `run.py` e persistir após reabrir

Pasta limpa, descompactada do ZIP final. Uma captura por passo, nesta ordem.

| Passo | Captura | O que deve aparecer | Feito |
|---|---|---|---|
| 1 | `MM01B_01_pasta_com_run_py.png` | Pasta com `run.py` e o relógio do Windows visível | <<PREENCHER: sim/não>> |
| 2 | `MM01B_02_console_e_login.png` | Console iniciado e tela de login em `127.0.0.1:5000/login` | <<PREENCHER: sim/não>> |
| 3 | `MM01B_03_login_preenchido.png` | Matrícula `1` e senha `01012000` preenchidas | <<PREENCHER: sim/não>> |
| 4 | `MM01B_04_troca_obrigatoria_senha.png` | Tela de troca obrigatória e, em seguida, a mensagem de sucesso (pode ser uma segunda captura `MM01B_04b_...`) | <<PREENCHER: sim/não>> |
| 5 | `MM01B_05_cadastro_formulario_e_confirmacao.png` | Formulário preenchido e a confirmação com a matrícula gerada (pode ser `MM01B_05b_...`) | <<PREENCHER: sim/não>> |
| 6 | `MM01B_06_lista_antes_de_fechar.png` | Lista com o colaborador, antes de fechar | <<PREENCHER: sim/não>> |
| 7 | `MM01B_07_console_fechado.png` | Console fechado | <<PREENCHER: sim/não>> |
| 8 | `MM01B_08_run_py_aberto_de_novo.png` | `run.py` aberto de novo (console e login) | <<PREENCHER: sim/não>> |
| 9 | `MM01B_09_lista_depois_de_reabrir.png` | Mesma lista, com o mesmo colaborador | <<PREENCHER: sim/não>> |

## 3. MM02-B / CT039: usabilidade por perfil

Cada participante é identificado pela matrícula, e o menu aparece na captura. O tempo e os erros de cada tarefa vão para `09_Homologacao/Testes_de_Aceitacao.md` (seção C), um registro por tarefa.

| Perfil | Tarefa | Captura | Matrícula | Observações |
|---|---|---|---|---|
| P1 RH | T1 | `MM02B_01_RH_T1_troca_senha.png` | <<PREENCHER: matrícula>> | |
| P1 RH | T2 | `MM02B_02_RH_T2_cadastro.png` | <<PREENCHER: matrícula>> | |
| P1 RH | T3 | `MM02B_03_RH_T3_folha_lancamentos_resumo.png` | <<PREENCHER: matrícula>> | |
| P1 RH | T4 | `MM02B_04_RH_T4_filtro_na_tela_Folha_de_pagamento.png` | <<PREENCHER: matrícula>> | O filtro está em `folha.py:65-67`. Não usar a lista de Colaboradores |
| P1 RH | T5 | `MM02B_05_RH_T5_recibo_impressao.png` | <<PREENCHER: matrícula>> | |
| P2 Financeiro | T1 | `MM02B_06_FIN_T1_troca_senha.png` | <<PREENCHER: matrícula>> | |
| P2 Financeiro | T2 e T3 | (nenhuma) | | Não se aplicam: cadastro, geração e lançamento exigem nível 1 (`colaboradores.py:119`, `folha.py:140, 199, 243`) |
| P2 Financeiro | T4 | `MM02B_07_FIN_T4_filtro_na_tela_Folha_de_pagamento.png` | <<PREENCHER: matrícula>> | Tela Folha de pagamento |
| P2 Financeiro | T5 | `MM02B_08_FIN_T5_recibo_impressao.png` | <<PREENCHER: matrícula>> | |
| P3 Colaborador (nível 3) | T1 | `MM02B_09_COL_T1_troca_senha.png` | <<PREENCHER: matrícula>> | Conta de nível 3 |
| P3 Colaborador (nível 3) | T5 | `MM02B_10_COL_T5_recibo_impressao.png` | <<PREENCHER: matrícula>> | Conta de nível 3 |

## 4. Depois da sessão

1. Copiar o resultado do MM01-B e do MM02-B para as linhas MM01 e MM02 de `09_Homologacao/Testes_de_Aceitacao.md`. A coluna "Situação" começa com `Aprovado` ou `Reprovado`.
2. Rodar `python 05_Codigo_Fonte/atualizar_documentos.py` para que as métricas (casos executados e aprovados, requisitos atendidos) incluam o MM01 e o MM02.
3. Atualizar a data real em `03_Projeto/Planejamento_do_Projeto.md` (marco "Fim da execução dos testes de aceitação") e retirar a pendência dos roteiros em `10_Qualidade/Relatorio_Final_de_Qualidade.md` (seção 5) e `10_Qualidade/Relatorio_de_Revisao_Tecnica.md`.
