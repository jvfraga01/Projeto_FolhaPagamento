# Testes de Aceitação

Entregável 6.5: cenário testado, resultado esperado, resultado obtido e situação final.
Os cenários são os critérios de aceitação do cliente (T1, seção 9). Os resultados automáticos referem-se à última execução da suíte: <!--A:testes-->74<!--/A--> testes, <!--A:resultado-->OK, nenhum teste falhou<!--/A-->, em <!--A:data-->17/11/2026 18:20<!--/A--> (`04_Testes/evidencias/saida_unittest.md`), executor <!--A:executor-->João Vitor Fraga<!--/A-->. Se a suíte falhar, a situação das linhas abaixo deixa de valer. Resultado por requisito: `01_Requisitos/ERS.md`, seção final.

## A. Critérios de aceitação do cliente (T1, seção 9)
| ID | Cenário | Esperado | Obtido (valores verificados pelas asserções) | Situação | Casos | Data | Responsável |
|---|---|---|---|---|---|---|---|
| AC01 | Cadastrar os três tipos de colaborador | Padrão, Comissionado e Por Produção cadastrados, com matrícula gerada | Três colaboradores gravados com os dados de cada tipo; matrículas sequenciais e únicas; senha inicial = data de nascimento | Aprovado | CT001, CT002, CT003, CT008 | <!--A:data-->17/11/2026 18:20<!--/A--> | <!--A:executor-->João Vitor Fraga<!--/A--> |
| AC02 | Validar dados obrigatórios e valores inválidos | Recusar nome vazio, valores negativos e texto no lugar de número, sem gravar | Nome vazio, salário -5, percentual -1, valor por unidade -1, "abc" e "1.5000" recusados (HTTP 400 ou erro de validação); nenhum registro criado | Aprovado | CT004–CT007, CT042, CT046, CT047 | <!--A:data-->17/11/2026 18:20<!--/A--> | <!--A:executor-->João Vitor Fraga<!--/A--> |
| AC03 | Calcular corretamente cada categoria | Exemplos do T1 | Padrão 3.000,00 → 3.000,00; Comissionado (base 3.000,00, vendas 5.000,00, 3%) → 3.150,00; vendas 4.999,99 → 3.150,00; Produção (base 1.000,00, 2,50/un) 99 un → 1.247,50 e 200 un → 1.500,00, sem bônus | Aprovado | CT015–CT019 | <!--A:data-->17/11/2026 18:20<!--/A--> | <!--A:executor-->João Vitor Fraga<!--/A--> |
| AC04 | Gerar folha individual e consolidada | Folha do mês e recibo com os campos exigidos | Folha de março/2026 com os 5 colaboradores da massa; recibo mostra matrícula, nome, tipo, salário base, vendas, adicional e líquido, com aviso PRÉVIA só em mês aberto | Aprovado | CT020, CT029-A, CT029-M | <!--A:data-->17/11/2026 18:20<!--/A--> | <!--A:executor-->João Vitor Fraga<!--/A--> |
| AC05 | Exibir o total geral da folha | Total = soma dos salários finais | Total geral 16.900,00; por categoria: Comissionado 3.150,00 e Produção 2.250,00; 5 colaboradores | Aprovado | CT021 | <!--A:data-->17/11/2026 18:20<!--/A--> | <!--A:executor-->João Vitor Fraga<!--/A--> |
| AC06 | Permitir novos tipos de remuneração | Novo calculador sem alterar os existentes | Tipo EXPERIMENTAL (adicional fixo de 100,00) → 1.100,00; os 3 tipos existentes mantêm os resultados | Aprovado | CT031 | <!--A:data-->17/11/2026 18:20<!--/A--> | <!--A:executor-->João Vitor Fraga<!--/A--> |

## B. Casos que eram manuais e foram automatizados
O resultado vale pela mesma execução da suíte acima (cada caso aponta o teste em `04_Testes/Casos_de_Teste.md`).

| ID | Caso | Cenário | Esperado | Obtido | Situação |
|---|---|---|---|---|---|
| MA01 | CT009 | RH e Financeiro abrem Colaboradores | Lista com matrícula, nome, tipo, salário e status | Resposta 200 para os dois perfis, com os campos exigidos | Aprovado |
| MA02 | CT012 | RH altera Paulo Padrao com março fechado | Cadastro novo; folha fechada intacta | Cadastro com nome e salário novos (302); folha de março continua "Paulo Padrao", 2.500,00 | Aprovado |
| MA03 | CT023 | Troca e redefinição de senha | Troca exige a atual; redefinição volta ao DDMMAAAA | Troca válida (antiga 401, nova 302); recusas com 200; redefinição devolve 15031990 | Aprovado |
| MA04 | CT029-M | Conteúdo do recibo | Todos os campos e botão Imprimir | Campos e botão presentes; PRÉVIA ausente em mês fechado | Aprovado |
| MA05 | CT037-A | Banco novo cria admin e 1º login obriga a troca | Admin 1, nível 1, ativo; redireciona para /senha | Admin criado; login 1 / 01012000 redireciona para a troca | Aprovado |
| MA06 | CT052, CT053 | Troca obrigatória da senha inicial | Fluxo bloqueado até trocar; login sem credenciais | Demais páginas redirecionam para /senha; após trocar, acesso liberado; tela de login sem credenciais | Aprovado |
| MA07 | CT030 | Regras de impressão | Menu, botões e filtros ocultos na impressão | CSS de impressão com as regras; botão Imprimir no recibo e no relatório | Aprovado |
| MA08 | CT043 | Cobertura de testes | Total ≥ 80% | <!--A:cobertura-->92,4%<!--/A--> (`evidencias/cobertura.md`) | Aprovado |
| MA09 | CT044 | Execução no Windows | Mesmo comportamento esperado | Suíte executada em <!--A:ambiente-->3.13.3 / Windows-11-10.0.26200-SP0<!--/A-->, resultado <!--A:resultado-->OK, nenhum teste falhou<!--/A--> | Aprovado |

## C. Casos que dependem de uma pessoa
O script de métricas lê as linhas que começam com `MM`. Só "Aprovado" ou "Reprovado" na coluna Situação conta como executado.

| Código | Caso | Descrição | Critério | Resultado | Situação | Data | Responsável |
|---|---|---|---|---|---|---|---|
| MM01 | CT037-M | Rodada 1, a partir da pasta de código-fonte: abrir o atalho, trocar a senha, cadastrar, reabrir e consultar (24 capturas, sequência abaixo) | Navegador abre; troca obrigatória; cadastro; mesmo cadastro na lista depois de reabrir | Capturas 01 a 11: atalho, login, troca obrigatória da senha, reabertura e lista com o mesmo cadastro (10 e 11). Faltam o formulário de cadastro e o encerramento da janela (lacunas na sequência); o relógio mostra 11/11/2026 21:30 a 21:55 | Parcial: falta repetir com o pacote final (MM01-B) | 11/11/2026 | Pedro Kolling |
| MM01-B | CT037-M | Rodada 2, com a versão exata de `07_Executavel/Projeto_FolhaPagamento_Executavel.zip` em pasta limpa, incluindo a captura do formulário de cadastro e do encerramento da janela | Os mesmos passos, com as capturas `evidencias/Prints/MM01B_NN_*.png` e o registro em `Sequencia_das_Evidencias_MM01_MM02.md` | <<PREENCHER: resultado de cada passo e nome das capturas>> | <<PREENCHER: Aprovado ou Reprovado>> | <<PREENCHER>> | <<PREENCHER>> |
| MM02 | CT039 | Roteiro de usabilidade com 2 participantes | Todas as tarefas aplicáveis ao perfil sem ajuda, dentro dos limites, e nota média ≥ 4 | P1 (RH): 5 de 5 tarefas; P2 (Financeiro): tarefas aplicáveis T1, T4 e T5 concluídas; notas 5 e 5 (média 5,0). Registro e conta usada em cada tarefa abaixo | Aprovado | 11/11/2026 | Luiggi Bortolini |

### Sequência de capturas
A relação de cada captura com o passo que ela comprova, a ressalva sobre a versão testada e as lacunas estão em `04_Testes/evidencias/Sequencia_das_Evidencias_MM01_MM02.md`. As 24 imagens ficam em `04_Testes/evidencias/Prints/`, numeradas na ordem de execução (`NN_MM01_...` e `NN_MM02_...`).

### Registro do roteiro de usabilidade (MM02 / CT039)
Aplicado por Luiggi Bortolini em 11/11/2026, sem ajuda aos participantes. Medidas esperadas conforme `Plano_de_Testes.md`, seção "Roteiro de Usabilidade". Os tempos são aproximados, informados pelo facilitador. O perfil Financeiro só consulta (RF012), então T2 e T3 se aplicam à conta RH.

| Participante | Perfil | Conta usada | Tarefa | Medida esperada | Sem ajuda? | Tempo | Erros | Comentários |
|---|---|---|---|---|---|---|---|---|
| P1 | RH | RH | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | RH | T2. Cadastrar colaborador Comissionado | ≤ 3 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | RH | T3. Gerar a folha, lançar vendas e consultar o resumo | ≤ 5 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | RH | T4. Filtrar a folha por tipo e salário máximo | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P1 | RH | RH | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | Financeiro | T1. Entrar e trocar a própria senha | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | <<PREENCHER: conta usada, ou "não se aplica ao perfil Financeiro">> | T2. Cadastrar colaborador Comissionado | ≤ 3 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | <<PREENCHER: conta usada, ou "não se aplica ao perfil Financeiro">> | T3. Gerar a folha, lançar vendas e consultar o resumo | ≤ 5 min; ≤ 2 erros | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | Financeiro | T4. Filtrar a folha por tipo e salário máximo | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |
| P2 | Financeiro | Financeiro | T5. Abrir e imprimir o próprio recibo de mês fechado | ≤ 2 min; ≤ 1 erro | Sim | cerca de 1 a 2 min | 0 | Achou didático e fácil de entender como usar |

Perfil Colaborador (nível 3): T1 aparece nas capturas 12 e 13, e T5 nas capturas 21 e 22 (`04_Testes/evidencias/Prints/`).

**Resumo por participante**

| Participante | Tarefas aplicáveis concluídas sem ajuda | Nota "foi fácil de usar" (1 a 5) |
|---|---|---|
| P1 (RH) | 5 de 5 | 5 |
| P2 (Financeiro) | 3 de 3 (T1, T4, T5), conforme o registro acima | 5 |
| Média | | 5,0 |

Critério de aprovação: todas as tarefas aplicáveis ao perfil de cada participante concluídas sem ajuda, dentro dos limites de tempo e de erros do Plano, e nota média ≥ 4. Resultado: Aprovado.
