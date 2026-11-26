# Sequência das Evidências Manuais, rodada B: MM01 (CT037-M) e MM02 (CT039)

## 1. Identificação da rodada

| Campo | Valor |
|---|---|
| Data e hora | 24/11/2026, de 20:41 (MM01B_01) a 21:09 (MM02B_31), lidas no relógio do Windows e no nome dos arquivos |
| Executor do MM01 | Pedro Kolling (o console mostra `C:\Users\pedro\AppData\Local...`)>> |
| P1 (RH, matrícula 2, Pedro Kolling) | Pedro Kolling |
| P2 (Financeiro, matrícula 4, Yuri) | Yuri Soares Dutra |
| Facilitador do MM02 | João Vitor Fraga |
| Windows | Windows 11 |
| Navegador | Opera GX e LVL8 |
| Python e Flask | 3.12 e 3.1.3 |
| Versão testada | 1.3 . A pasta é `Downloads\Projeto_FolhaPagamento-develop\Projeto_FolhaPagamento-develop\05_Codigo_Fonte` (ZIP da branch do GitHub) |
| Resultado do MM02/CT039 | Aprovado |

## 2. MM01 / CT037-M: iniciar, trocar a senha, cadastrar, fechar e reabrir

Conta: Administrador, matrícula 1 (`1 / 01012000`).

| Passo do CT037-M | Capturas | O que se vê | Prova |
|---|---|---|---|
| Pasta com `run.py` | MM01B_01 | Explorador em `...\05_Codigo_Fonte`, `run.py` selecionado, menu "Abrir com > Python". Relógio 20:41 | Comprovado |
| Console e tela de login | MM01B_02, 09 | 02: `127.0.0.1:5000/login` com campos vazios (20:42). 09: console "Sistema rodando em http://127.0.0.1:5000" com o log desde as 20:42:11 | Comprovado |
| Login `1 / 01012000` | MM01B_03 | Matrícula 1 e senha preenchida (20:42) | Comprovado |
| Troca obrigatória e sucesso | MM01B_04 a 06 | 04: "Alterar minha senha" com o menu "Administrador (Admin/RH)". 05: campos preenchidos. 06: "Senha alterada com sucesso" e a lista só com o Administrador | Comprovado |
| Cadastrar um colaborador | MM01B_07, 08 | 07: formulário com Pedro Kolling, Padrão, R$ 8.000,00, nível 1. 08: "Colaborador cadastrado. Matrícula 2" e a lista antes de fechar | Comprovado |
| Fechar o console | (nenhuma) | Sem captura do fechamento. O log novo de MM01B_12 começa às 20:49:57, o que mostra um servidor reiniciado | **Lacuna** (indireta) |
| Abrir de novo | MM01B_10, 11, 12 | 10 (20:48) e 11 (20:49): `run.py` aberto de novo pelo Explorador. 12: console com log novo e tela de login | Comprovado |
| Mesmo cadastro depois de reabrir | MM01B_13 | Lista com Administrador e Pedro Kolling, R$ 8.000,00 (20:50) | Comprovado |

## 3. MM02 / CT039: capturas por tarefa e por conta

| Tarefa | Conta (matrícula, nível) | Capturas | O que se vê |
|---|---|---|---|
| RH T1 | 2 Pedro Kolling, nível 1 | MM02B_01 a 03 | 01: `run.py` (20:55). 02: login com matrícula 2. 03: "Senha alterada com sucesso", menu "Pedro Kolling (Admin/RH)" |
| RH T2 | 2 | MM02B_04, 05 | 04: formulário de Joao, Comissionado, R$ 5.000,00, 5%, nível 3. 05: "Colaborador cadastrado. Matrícula 3" |
| RH T3 | 2 | MM02B_06 a 10 | 06: "Nenhuma folha gerada ainda". 07: folha de Novembro/2026 aberta (prévia), total R$ 13.000,00. 08 e 09: lançamentos de Joao (0,00 e 50000). 10: "Lançamentos salvos e folha recalculada", total R$ 15.500,00 |
| RH T4 | 2 | MM02B_11 a 14 | Folha com filtro de salário máximo 5000, depois tipos Comissionado, Por Produção ("Nenhuma folha encontrada") e Padrão |
| RH T5 | 2 | MM02B_15 a 17 | 15: "Minhas folhas" com Novembro/2026. 16: recibo de Pedro Kolling, R$ 8.000,00. 17: pré-visualização de impressão (Salvar como PDF) |
| Preparação do Financeiro | 2 | MM02B_18, 19 | Cadastro de Yuri: Padrão, R$ 6.000,00, nível 2. "Colaborador cadastrado. Matrícula 4" |
| Financeiro T1 | 4 Yuri, nível 2 | MM02B_20 a 23 | 20: `run.py` (21:03). 21: login com matrícula 4. 22: "Alterar minha senha", menu "Yuri (Financeiro)" sem "Novo colaborador". 23: "Senha alterada com sucesso" e lista sem a coluna "Ações" |
| Financeiro T4 | 4 | MM02B_24 a 27 | Folha de Novembro/2026 fechada (congelada), filtros Padrão, Comissionado, Por Produção e salário máximo 7000 |
| Preparação do T5 | 2 | MM02B_28 | Lançamentos de Dezembro/2026 na conta de Pedro. Yuri foi cadastrado depois do fechamento de Novembro, e por isso o recibo dele é de Dezembro |
| Financeiro T5 | 4 | MM02B_29 a 31 | 29: "Minhas folhas" com Dezembro/2026. 30: recibo de Yuri, R$ 6.000,00. 31: pré-visualização de impressão |

Conferências feitas sobre as imagens: Joao, R$ 5.000,00 + 50.000,00 × 5% = R$ 7.500,00 (MM02B_10); 0 + 7.500 + 8.000 = R$ 15.500,00 (MM02B_10).

## 4. Correspondência entre os nomes originais e os novos

| Nome original | Nome novo |
|---|---|
| `Captura de tela 2026-11-24 204149.png` | `MM01B_01_pasta_run_py_20h41.png` |
| `Captura de tela 2026-11-24 204232.png` | `MM01B_02_login_tela_inicial_20h42.png` |
| `Captura de tela 2026-11-24 204251.png` | `MM01B_03_login_1_preenchido_20h42.png` |
| `Captura de tela 2026-11-24 204311.png` | `MM01B_04_troca_senha_obrigatoria_tela_20h43.png` |
| `Captura de tela 2026-11-24 204546.png` | `MM01B_05_troca_senha_preenchida_20h45.png` |
| `Captura de tela 2026-11-24 204600.png` | `MM01B_06_senha_alterada_com_sucesso_20h46.png` |
| `Captura de tela 2026-11-24 204708.png` | `MM01B_07_cadastro_formulario_Pedro_Kolling_20h47.png` |
| `Captura de tela 2026-11-24 204717.png` | `MM01B_08_cadastro_confirmado_matricula_2_20h47.png` |
| `Captura de tela 2026-11-24 204827.png` | `MM01B_09_console_antes_de_fechar_20h48.png` |
| `Captura de tela 2026-11-24 204852.png` | `MM01B_10_reabrir_run_py_1_20h48.png` |
| `Captura de tela 2026-11-24 204945.png` | `MM01B_11_reabrir_run_py_2_20h49.png` |
| `Captura de tela 2026-11-24 205008.png` | `MM01B_12_console_novo_e_login_apos_reabrir_20h50.png` |
| `Captura de tela 2026-11-24 205033.png` | `MM01B_13_lista_apos_reabrir_com_Pedro_Kolling_20h50.png` |
| `Captura de tela 2026-11-24 205518.png` | `MM02B_01_RH_T1_iniciar_run_py_20h55.png` |
| `Captura de tela 2026-11-24 205547.png` | `MM02B_02_RH_T1_login_matricula_2_20h55.png` |
| `Captura de tela 2026-11-24 205623.png` | `MM02B_03_RH_T1_senha_alterada_menu_RH_20h56.png` |
| `Captura de tela 2026-11-24 205741.png` | `MM02B_04_RH_T2_formulario_Joao_nivel3_20h57.png` |
| `Captura de tela 2026-11-24 205747.png` | `MM02B_05_RH_T2_confirmado_matricula_3_20h57.png` |
| `Captura de tela 2026-11-24 205810.png` | `MM02B_06_RH_T3_folha_vazia_20h58.png` |
| `Captura de tela 2026-11-24 205819.png` | `MM02B_07_RH_T3_folha_gerada_aberta_20h58.png` |
| `Captura de tela 2026-11-24 205825.png` | `MM02B_08_RH_T3_lancamentos_Joao_0_20h58.png` |
| `Captura de tela 2026-11-24 205837.png` | `MM02B_09_RH_T3_lancamentos_Joao_50000_20h58.png` |
| `Captura de tela 2026-11-24 205845.png` | `MM02B_10_RH_T3_lancamentos_salvos_folha_recalculada_20h58.png` |
| `Captura de tela 2026-11-24 205933.png` | `MM02B_11_RH_T4_filtro_salario_max_5000_20h59.png` |
| `Captura de tela 2026-11-24 205943.png` | `MM02B_12_RH_T4_filtro_Comissionado_20h59.png` |
| `Captura de tela 2026-11-24 205951.png` | `MM02B_13_RH_T4_filtro_Por_Producao_20h59.png` |
| `Captura de tela 2026-11-24 205958.png` | `MM02B_14_RH_T4_filtro_Padrao_20h59.png` |
| `Captura de tela 2026-11-24 210041.png` | `MM02B_15_RH_T5_minhas_folhas_Novembro_21h00.png` |
| `Captura de tela 2026-11-24 210049.png` | `MM02B_16_RH_T5_recibo_Pedro_Kolling_21h00.png` |
| `Captura de tela 2026-11-24 210058.png` | `MM02B_17_RH_T5_impressao_recibo_21h00.png` |
| `Captura de tela 2026-11-24 210259.png` | `MM02B_18_FIN_prep_cadastro_Yuri_formulario_nivel2_21h02.png` |
| `Captura de tela 2026-11-24 210306.png` | `MM02B_19_FIN_prep_cadastro_Yuri_confirmado_matricula_4_21h03.png` |
| `Captura de tela 2026-11-24 210328.png` | `MM02B_20_FIN_T1_iniciar_run_py_21h03.png` |
| `Captura de tela 2026-11-24 210404.png` | `MM02B_21_FIN_T1_login_matricula_4_21h04.png` |
| `Captura de tela 2026-11-24 210410.png` | `MM02B_22_FIN_T1_troca_senha_menu_Financeiro_21h04.png` |
| `Captura de tela 2026-11-24 210432.png` | `MM02B_23_FIN_T1_senha_alterada_com_sucesso_21h04.png` |
| `Captura de tela 2026-11-24 210514.png` | `MM02B_24_FIN_T4_filtro_Padrao_21h05.png` |
| `Captura de tela 2026-11-24 210522.png` | `MM02B_25_FIN_T4_filtro_Comissionado_21h05.png` |
| `Captura de tela 2026-11-24 210530.png` | `MM02B_26_FIN_T4_filtro_Por_Producao_21h05.png` |
| `Captura de tela 2026-11-24 210545.png` | `MM02B_27_FIN_T4_filtro_salario_max_7000_21h05.png` |
| `Captura de tela 2026-11-24 210814.png` | `MM02B_28_FIN_prep_RH_lancamentos_Dezembro_21h08.png` |
| `Captura de tela 2026-11-24 210909.png` | `MM02B_29_FIN_T5_minhas_folhas_Dezembro_21h09.png` |
| `Captura de tela 2026-11-24 210916.png` | `MM02B_30_FIN_T5_recibo_Yuri_21h09.png` |
| `Captura de tela 2026-11-24 210924.png` | `MM02B_31_FIN_T5_impressao_recibo_21h09.png` |
