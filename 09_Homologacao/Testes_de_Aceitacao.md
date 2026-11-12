# Testes de Aceitação

Entregável 6.5: cenário testado, resultado esperado, resultado obtido e situação final.
Os cenários são os critérios de aceitação do cliente (T1, seção 9). Os resultados referem-se à última execução da suíte automatizada: <!--A:testes-->70<!--/A--> testes, <!--A:resultado-->OK, nenhum teste falhou<!--/A-->, em <!--A:data-->11/11/2026 07:32<!--/A--> (`04_Testes/evidencias/saida_unittest.txt`), executor <!--A:executor-->João Vitor Fraga<!--/A-->. Se a suíte falhar, a situação das linhas abaixo deixa de valer.

| ID | Cenário | Esperado | Obtido (valores verificados pelas asserções) | Situação | Casos |
|---|---|---|---|---|---|
| AC01 | Cadastrar os três tipos de colaborador | Padrão, Comissionado e Por Produção cadastrados, com matrícula gerada | Três colaboradores gravados com os dados de cada tipo; matrículas sequenciais e únicas; senha inicial = data de nascimento | Aprovado | CT001, CT002, CT003, CT008 |
| AC02 | Validar dados obrigatórios e valores inválidos | Recusar nome vazio, valores negativos e texto no lugar de número, sem gravar | Nome vazio, salário -5, percentual -1, valor por unidade -1, "abc" e "1.5000" recusados (HTTP 400 ou erro de validação); nenhum registro criado | Aprovado | CT004–CT007, CT042, CT046, CT047 |
| AC03 | Calcular corretamente cada categoria | Exemplos do T1 | Padrão 3.000,00 → 3.000,00; Comissionado (base 3.000,00, vendas 5.000,00, 3%) → 3.150,00; vendas 4.999,99 → 3.150,00; Produção (base 1.000,00, 2,50/un) 99 un → 1.247,50 e 200 un → 1.500,00, sem bônus | Aprovado | CT015–CT019 |
| AC04 | Gerar folha individual e consolidada | Folha do mês e recibo com os campos exigidos | Folha de março/2026 com os 5 colaboradores da massa; recibo mostra matrícula, nome, tipo, salário base, vendas, adicional e líquido, com aviso PRÉVIA só em mês aberto | Aprovado | CT020, CT029-A, CT029-M |
| AC05 | Exibir o total geral da folha | Total = soma dos salários finais | Total geral 16.900,00; por categoria: Comissionado 3.150,00 e Produção 2.250,00; 5 colaboradores | Aprovado | CT021 |
| AC06 | Permitir novos tipos de remuneração | Novo calculador sem alterar os existentes | Tipo EXPERIMENTAL (adicional fixo de 100,00) → 1.100,00; os 3 tipos existentes mantêm os resultados | Aprovado | CT031 |
