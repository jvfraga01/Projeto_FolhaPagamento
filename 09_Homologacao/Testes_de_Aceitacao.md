# Testes de Aceitação

Entregável 6.5: cenário testado, resultado esperado, resultado obtido e situação final.
Os cenários são os critérios de aceitação do cliente (T1, seção 9). Os resultados referem-se à última execução da suíte automatizada: <!--A:testes-->?<!--/A--> testes, <!--A:resultado-->======================== 74 passed in 61.83s (0:01:01) ========================<!--/A-->, em <!--A:data-->12/11/2026 19:24<!--/A--> (`04_Testes/evidencias/saida_unittest.txt`), executor <!--A:executor-->Pedro da Silva Kolling<!--/A-->. Se a suíte falhar, a situação das linhas abaixo deixa de valer.

| ID | Cenário | Esperado | Obtido (valores verificados pelas asserções) | Situação | Casos |
|---|---|---|---|---|---|
| AC01 | Cadastrar os três tipos de colaborador | Padrão, Comissionado e Por Produção cadastrados, com matrícula gerada | Três colaboradores gravados com os dados de cada tipo; matrículas sequenciais e únicas; senha inicial = data de nascimento | Aprovado | CT001, CT002, CT003, CT008 |
| AC02 | Validar dados obrigatórios e valores inválidos | Recusar nome vazio, valores negativos e texto no lugar de número, sem gravar | Nome vazio, salário -5, percentual -1, valor por unidade -1, "abc" e "1.5000" recusados (HTTP 400 ou erro de validação); nenhum registro criado | Aprovado | CT004–CT007, CT042, CT046, CT047 |
| AC03 | Calcular corretamente cada categoria | Exemplos do T1 | Padrão 3.000,00 → 3.000,00; Comissionado (base 3.000,00, vendas 5.000,00, 3%) → 3.150,00; vendas 4.999,99 → 3.150,00; Produção (base 1.000,00, 2,50/un) 99 un → 1.247,50 e 200 un → 1.500,00, sem bônus | Aprovado | CT015–CT019 |
| AC04 | Gerar folha individual e consolidada | Folha do mês e recibo com os campos exigidos | Folha de março/2026 com os 5 colaboradores da massa; recibo mostra matrícula, nome, tipo, salário base, vendas, adicional e líquido, com aviso PRÉVIA só em mês aberto | Aprovado | CT020, CT029-A, CT029-M |
| AC05 | Exibir o total geral da folha | Total = soma dos salários finais | Total geral 16.900,00; por categoria: Comissionado 3.150,00 e Produção 2.250,00; 5 colaboradores | Aprovado | CT021 |
| AC06 | Permitir novos tipos de remuneração | Novo calculador sem alterar os existentes | Tipo EXPERIMENTAL (adicional fixo de 100,00) → 1.100,00; os 3 tipos existentes mantêm os resultados | Aprovado | CT031 |
## C. Casos manuais

Casos que dependem de uma pessoa. O resultado de cada um está na tabela abaixo, e o script de métricas lê as linhas que começam com `MM`. A persistência com `iniciar.bat` faz parte do CT037-M, ainda não executado.

| Código | Caso | Descrição | Critério | Resultado | Situação | Data | Responsável |
|---|---|---|---|---|---|---|---|
| MM02 | CT039 | Roteiro de usabilidade com 2 participantes | ≥ 4 de 5 tarefas sem ajuda e nota média ≥ 4 | P1 (RH) e P2 (Financeiro): 5 de 5 tarefas sem ajuda, 0 erros, cerca de 1 a 2 min por tarefa; notas 5 e 5 (média 5,0). Registro detalhado abaixo | Aprovado | 11/11/2026 | Luiggi Bortolini |

### Registro do roteiro de usabilidade (MM02 / CT039)

Aplicado por Luiggi Bortolini em 11/11/2026, sem ajuda aos participantes. Medidas esperadas conforme `Plano_de_Testes.md`, seção "Roteiro de Usabilidade". Os tempos são aproximados, informados pelo facilitador.

| Participante | Perfil | Tarefa | Medida esperada | Sem ajuda? | Tempo | Erros | Comentários |
|---|---|---|---|---|---|---|---|
| P1 | RH | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | T2. Cadastrar colaborador Comissionado | ≤ 3 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | T3. Gerar a folha, lançar vendas e consultar o resumo | ≤ 5 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | T4. Filtrar a folha por tipo e salário máximo | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | T2. Cadastrar colaborador Comissionado | ≤ 3 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | T3. Gerar a folha, lançar vendas e consultar o resumo | ≤ 5 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | T4. Filtrar a folha por tipo e salário máximo | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |

**Resumo por participante**

| Participante | Tarefas concluídas sem ajuda | Nota "foi fácil de usar" (1 a 5) |
|---|---|---|
| P1 | 5 de 5 | 5 |
| P2 | 5 de 5 | 5 |
| Média | | 5,0 |

Critério de aprovação: pelo menos 4 das 5 tarefas sem ajuda para os dois participantes, dentro dos limites de tempo e de erros do Plano, e nota média ≥ 4. Resultado: Aprovado.
