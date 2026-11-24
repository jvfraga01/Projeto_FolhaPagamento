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

Casos que dependem de uma pessoa. O resultado de cada um está na tabela abaixo, e o script de métricas lê as linhas que começam com `MM`. A coluna "Situação" deve **começar** com `Aprovado` ou `Reprovado`: enquanto estiver como `<<PREENCHER: ...>>`, o caso conta como não executado. A persistência com `run.py` faz parte do CT037-M (linha MM01); os dois casos são executados na rodada B, em uma sessão só, com o ZIP final descompactado em pasta limpa (evidências em `04_Testes/evidencias/Prints/`, prefixos `MM01B_` e `MM02B_`; roteiro em `04_Testes/evidencias/Sequencia_das_Evidencias_MM01B_MM02B.md`). A rodada preliminar de 11/11/2026 foi substituída pela rodada B e fica só como histórico em `Sequencia_das_Evidencias_MM01_MM02.md`.

| Código | Caso | Descrição | Critério | Resultado | Situação | Data | Responsável |
|---|---|---|---|---|---|---|---|
| MM01 | CT037-M | Abrir com `run.py` em pasta limpa e persistência após reabrir | Navegador abre sozinho; login e troca obrigatória funcionam; o colaborador cadastrado continua na lista depois de reabrir | <<PREENCHER: resultado observado em MM01-B (matrícula do colaborador cadastrado e se a lista reabriu igual)>> | <<PREENCHER: Aprovado ou Reprovado>> | <<PREENCHER: data da sessão>> | <<PREENCHER: nome do executor>> |
| MM02 | CT039 | Roteiro de usabilidade com 2 integrantes da equipe (autorizado pelo professor em <<PREENCHER: data>>) | Todas as tarefas aplicáveis ao perfil de cada participante sem ajuda, dentro dos limites de tempo e de erros do Plano, e nota média ≥ 4 | P1 (RH): <<PREENCHER: n>> de 5 tarefas sem ajuda; P2 (Financeiro): <<PREENCHER: n>> de 3 tarefas aplicáveis sem ajuda; notas <<PREENCHER: nota P1>> e <<PREENCHER: nota P2>> (média <<PREENCHER: média>>). Registro detalhado abaixo | <<PREENCHER: Aprovado ou Reprovado>> | <<PREENCHER: data da sessão>> | <<PREENCHER: nome do facilitador>> |

### Registro do roteiro de usabilidade (MM02 / CT039)

Aplicado por <<PREENCHER: nome do facilitador>> em <<PREENCHER: data da sessão>>, sem ajuda aos participantes. Medidas esperadas conforme `Plano_de_Testes.md`, seção "Roteiro de Usabilidade". Cada participante é identificado pela matrícula, e o menu aparece em todas as capturas (`MM02B_NN_...png`). Tempo e erros são os observados em cada tarefa, um registro por linha.

Participantes: P1 = <<PREENCHER: nome do participante RH>>; P2 = <<PREENCHER: nome do participante Financeiro>>; P3 (Colaborador, nível 3, apenas T1 e T5) = <<PREENCHER: nome do participante nível 3>>.

| Participante | Perfil | Conta usada (matrícula) | Tarefa | Medida esperada | Sem ajuda? | Tempo | Erros | Comentários |
|---|---|---|---|---|---|---|---|---|
| P1 | RH | <<PREENCHER: matrícula>> | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P1 | RH | <<PREENCHER: matrícula>> | T2. Cadastrar colaborador Comissionado | ≤ 3 min; ≤ 2 erros | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P1 | RH | <<PREENCHER: matrícula>> | T3. Gerar a folha, lançar vendas e consultar o resumo | ≤ 5 min; ≤ 2 erros | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P1 | RH | <<PREENCHER: matrícula>> | T4. Filtrar a folha por tipo e salário máximo (tela Folha de pagamento) | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P1 | RH | <<PREENCHER: matrícula>> | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P2 | Financeiro | <<PREENCHER: matrícula>> | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P2 | Financeiro | não se aplica ao perfil Financeiro | T2. Cadastrar colaborador Comissionado | não se aplica | não se aplica | não se aplica | não se aplica | O cadastro exige nível 1 (`colaboradores.py:119`) |
| P2 | Financeiro | não se aplica ao perfil Financeiro | T3. Gerar a folha, lançar vendas e consultar o resumo | não se aplica | não se aplica | não se aplica | não se aplica | Gerar, fechar e lançar vendas exigem nível 1 (`folha.py:140, 199, 243`) |
| P2 | Financeiro | <<PREENCHER: matrícula>> | T4. Filtrar a folha por tipo e salário máximo (tela Folha de pagamento) | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P2 | Financeiro | <<PREENCHER: matrícula>> | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P3 | Colaborador (nível 3) | <<PREENCHER: matrícula>> | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |
| P3 | Colaborador (nível 3) | <<PREENCHER: matrícula>> | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | <<PREENCHER: Sim/Não>> | <<PREENCHER: tempo>> | <<PREENCHER: nº>> | <<PREENCHER: comentário>> |

**Resumo por participante**

| Participante | Tarefas concluídas sem ajuda | Nota "foi fácil de usar" (1 a 5) |
|---|---|---|
| P1 (RH) | <<PREENCHER: n>> de 5 | <<PREENCHER: nota>> |
| P2 (Financeiro) | <<PREENCHER: n>> de 3 aplicáveis | <<PREENCHER: nota>> |
| Média (P1 e P2) | | <<PREENCHER: média>> |

O perfil Colaborador (P3, T1 e T5) é verificado na mesma sessão e não entra na média das notas.

Critério de aprovação: todas as tarefas aplicáveis ao perfil de cada participante (RH: T1 a T5; Financeiro: T1, T4 e T5) concluídas sem ajuda, dentro dos limites de tempo e de erros do Plano, e nota média ≥ 4. Resultado: <<PREENCHER: Aprovado ou Reprovado, conforme a tabela acima>>.
