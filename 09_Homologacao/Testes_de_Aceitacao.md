# Testes de Aceitação

Entregável 6.5: cenário testado, resultado esperado, resultado obtido e situação final.
Os cenários são os critérios de aceitação do cliente (T1, seção 9). Os resultados referem-se à última execução da suíte automatizada: <!--A:testes-->74<!--/A--> testes, <!--A:resultado-->OK, nenhum teste falhou<!--/A-->, em <!--A:data-->17/11/2026 19:08<!--/A--> (`04_Testes/evidencias/saida_unittest.md`), executor <!--A:executor-->João Vitor Fraga<!--/A-->. Se a suíte falhar, a situação das linhas abaixo deixa de valer.

| ID | Cenário | Esperado | Obtido (valores verificados pelas asserções) | Situação | Casos |
|---|---|---|---|---|---|
| AC01 | Cadastrar os três tipos de colaborador | Padrão, Comissionado e Por Produção cadastrados, com matrícula gerada | Três colaboradores gravados com os dados de cada tipo; matrículas sequenciais e únicas; senha inicial = data de nascimento | Aprovado | CT001, CT002, CT003, CT008 |
| AC02 | Validar dados obrigatórios e valores inválidos | Recusar nome vazio, valores negativos e texto no lugar de número, sem gravar | Nome vazio, salário -5, percentual -1, valor por unidade -1, "abc" e "1.5000" recusados (HTTP 400 ou erro de validação); nenhum registro criado | Aprovado | CT004–CT007, CT042, CT046, CT047 |
| AC03 | Calcular corretamente cada categoria | Exemplos do T1 | Padrão 3.000,00 → 3.000,00; Comissionado (base 3.000,00, vendas 5.000,00, 3%) → 3.150,00; vendas 4.999,99 → 3.150,00; Produção (base 1.000,00, 2,50/un) 99 un → 1.247,50 e 200 un → 1.500,00, sem bônus | Aprovado | CT015–CT019 |
| AC04 | Gerar folha individual e consolidada | Folha do mês e recibo com os campos exigidos | Folha de março/2026 com os 5 colaboradores da massa; recibo mostra matrícula, nome, tipo, salário base, vendas, adicional e líquido, com aviso PRÉVIA só em mês aberto | Aprovado | CT020, CT029-A, CT029-M |
| AC05 | Exibir o total geral da folha | Total = soma dos salários finais | Total geral 16.900,00; por categoria: Comissionado 3.150,00 e Produção 2.250,00; 5 colaboradores | Aprovado | CT021 |
| AC06 | Permitir novos tipos de remuneração | Novo calculador sem alterar os existentes | Tipo EXPERIMENTAL (adicional fixo de 100,00) → 1.100,00; os 3 tipos existentes mantêm os resultados | Aprovado | CT031 |
## C. Casos manuais

Casos que dependem de uma pessoa. O resultado de cada um está na tabela abaixo, e o script de métricas lê as linhas que começam com `MM`. A rodada preliminar de 11/11/2026 (capturas `01_` a `24_` em `04_Testes/evidencias/Prints/`, feita com o atalho antigo, que não faz parte da rodada B) foi **substituída pela rodada B de 24/11/2026**, executada com `python run.py` e registrada nas capturas `MM01B_NN_...` e `MM02B_NN_...` da mesma pasta. O passo a passo de cada captura está em `04_Testes/evidencias/Sequencia_das_Evidencias_MM01B_MM02B.md`. Os testes manuais foram feitos por integrantes da equipe, conforme resposta do professor de 23/11/2026 (`09_Homologacao/evidencias/resposta_professor_23-11-2026.jpeg`).

| Código | Caso | Descrição | Critério | Resultado | Situação | Data | Responsável |
|---|---|---|---|---|---|---|---|
| MM01 | CT037-M | Iniciar com `python run.py`, trocar a senha, cadastrar um colaborador, fechar e reabrir | Login `1 / 01012000` e troca obrigatória funcionam; o colaborador cadastrado continua na lista depois de reabrir | Login e troca de senha do Administrador conferidos (MM01B_03 a 06). Cadastro de Pedro Kolling, matrícula 2 (MM01B_07 e 08). Servidor reiniciado, com log novo (MM01B_12). Lista reaberta com Administrador e Pedro Kolling (MM01B_13). Ressalvas na nota abaixo da tabela | Aprovado | 24/11/2026 | <<PREENCHER: executor do MM01 (as capturas mostram o caminho C:\Users\pedro)>> |
| MM02 | CT039 | Roteiro de usabilidade com 2 participantes (P1 RH, P2 Financeiro) | Todas as tarefas aplicáveis ao perfil concluídas sem ajuda, dentro dos limites de tempo e de erros do Plano, e nota média ≥ 4 | P1 (RH, matrícula 2): T1 a T5, 5 de 5 aplicáveis, chegaram ao resultado esperado nas capturas MM02B_01 a 17. P2 (Financeiro, matrícula 4): 3 de 3 aplicáveis (T1, T4 e T5), capturas MM02B_20 a 31. Ajuda, tempos, erros e notas: <<PREENCHER: conferir o registro abaixo>> | <<PREENCHER: Aprovado ou Reprovado, depois de registrar tempos, erros e notas abaixo>> | 24/11/2026 | <<PREENCHER: facilitador>> |

**Ressalvas do MM01 (conferir antes da entrega)**

- Versão testada: a pasta das capturas é `Downloads\Projeto_FolhaPagamento-develop\Projeto_FolhaPagamento-develop\05_Codigo_Fonte` (ZIP da branch do GitHub), e não o ZIP final de entrega. Commit ou SHA-256: <<PREENCHER: hash do commit ou do ZIP usado>>.
- A pasta `instance` já aparece em MM01B_01, antes da primeira execução. O login `1 / 01012000` e a lista só com o Administrador em MM01B_06 indicam banco novo. <<PREENCHER: confirmar se a pasta `instance` estava vazia>>.
- Não há captura do fechamento do console. O reinício aparece no log novo de MM01B_12, que começa às 20:49:57, depois do log de MM01B_09, que termina às 20:47:23.
- Versões de Python, Flask, Windows e navegador: <<PREENCHER: saída de `python --version`, `pip show flask`, versão do Windows e navegador>>.

### Registro do roteiro de usabilidade (MM02 / CT039)

Rodada B, aplicada em 24/11/2026 por integrantes da equipe. Medidas esperadas conforme `Plano_de_Testes.md`, seção "Roteiro de Usabilidade". Perfil Financeiro: T2 e T3 não se aplicam, porque cadastro, geração da folha e lançamentos exigem nível 1 (`colaboradores.py:119`, `folha.py:140, 199, 243`).

| Participante | Nome | Perfil | Conta usada (matrícula) |
|---|---|---|---|
| P1 | <<PREENCHER: nome de quem executou como P1>> | RH (nível 1) | 2 (Pedro Kolling) |
| P2 | <<PREENCHER: nome de quem executou como P2>> | Financeiro (nível 2) | 4 (Yuri) |
| Facilitador | <<PREENCHER: nome do facilitador>> | QA | não se aplica |

| Participante | Perfil | Conta usada (matrícula) | Tarefa | Medida esperada | Sem ajuda? | Tempo | Erros | Capturas |
|---|---|---|---|---|---|---|---|---|
| P1 | RH | 2 | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_01 a 03 |
| P1 | RH | 2 | T2. Cadastrar colaborador Comissionado | ≤ 3 min; ≤ 2 erros | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_04 e 05 |
| P1 | RH | 2 | T3. Gerar a folha, lançar vendas e consultar o resumo | ≤ 5 min; ≤ 2 erros | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_06 a 10; o resumo (tela Relatório) não foi capturado: <<PREENCHER: nova captura>> |
| P1 | RH | 2 | T4. Filtrar a folha por tipo e salário máximo | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_11 a 14 |
| P1 | RH | 2 | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_15 a 17; o fechamento do mês não foi capturado |
| P2 | Financeiro | 4 | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_20 a 23 |
| P2 | Financeiro | 4 | T2. Cadastrar colaborador Comissionado | não se aplica ao perfil Financeiro | não se aplica | não se aplica | não se aplica | menu sem "Novo colaborador" em MM02B_22 |
| P2 | Financeiro | 4 | T3. Gerar a folha, lançar vendas e consultar o resumo | não se aplica ao perfil Financeiro | não se aplica | não se aplica | não se aplica | menu sem lançamentos |
| P2 | Financeiro | 4 | T4. Filtrar a folha por tipo e salário máximo | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_24 a 27 |
| P2 | Financeiro | 4 | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: min:s>> | <<PREENCHER: nº>> | MM02B_29 a 31 (recibo de Dezembro/2026; a preparação está em MM02B_28) |

**Perfil Colaborador (nível 3)**: T1 e T5 com uma conta nível 3. Verificação do Plano, fora do critério dos 2 participantes.

| Perfil | Conta usada (matrícula) | Tarefa | Resultado | Capturas |
|---|---|---|---|---|
| Colaborador | 3 (Joao, nível 3) | T1. Entrar e trocar a própria senha | <<PREENCHER: resultado e tempo>> | <<PREENCHER: MM02B_32 em diante>> |
| Colaborador | 3 (Joao, nível 3) | T5. Abrir e imprimir o próprio recibo de mês fechado | <<PREENCHER: resultado e tempo>> | <<PREENCHER: capturas>> |

**Resumo por participante**

| Participante | Tarefas aplicáveis concluídas sem ajuda | Nota "foi fácil de usar" (1 a 5) |
|---|---|---|
| P1 (RH) | <<PREENCHER: nº>> de 5 aplicáveis | <<PREENCHER: nota>> |
| P2 (Financeiro) | <<PREENCHER: nº>> de 3 aplicáveis | <<PREENCHER: nota>> |
| Média | | <<PREENCHER: média>> |

Critério de aprovação: todas as tarefas aplicáveis ao perfil de cada participante (RH: T1 a T5; Financeiro: T1, T4 e T5) concluídas sem ajuda, dentro dos limites de tempo e de erros do Plano, e nota média ≥ 4. Resultado: <<PREENCHER: Aprovado ou Reprovado>>.
