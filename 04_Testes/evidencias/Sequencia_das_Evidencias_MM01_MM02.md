# Sequência das Evidências Manuais: MM01 (CT037-M) e MM02 (CT039)

> **Rodada preliminar de 11/11, substituída pela rodada B.** A rodada B de 24/11/2026, feita com `python run.py`, está em `Sequencia_das_Evidencias_MM01B_MM02B.md`. Este arquivo fica como histórico, e as capturas `01_` a `24_` mostram `iniciar.bat` e o aviso do Windows, que não fazem parte da rodada B.

Este arquivo relaciona cada captura da pasta `04_Testes/evidencias/Prints/` ao passo que ela comprova, na ordem em que os passos foram executados. Ele atende aos itens 2 e 3 de "O que falta para a entrega final" da Avaliação A3 de 13/11/2026 (conclusão do MM01/CT037-M e validação do MM02 com as permissões previstas).

As capturas foram renomeadas para o padrão `NN_<teste>_<descrição>.png`, em que `NN` é a posição na sequência (01 a 24). Os nomes antigos (`MM01_Evidencia_N.png`) estão na seção 6.

Tudo o que consta como "visto" abaixo foi lido nas próprias imagens. O que não aparece nelas está marcado como "não registrado (rodada preliminar)".

---

## 1. Identificação da rodada

| Campo | Valor |
|---|---|
| Data observada nas capturas | 11/11/2026. O relógio do Windows marca 21:30 (captura 01), 21:31 (03), 21:47 (14) e a impressão do recibo traz 21:55 (22) |
| Executor | Pedro da Silva Kolling. A captura 02 mostra o caminho `C:\Users\pedro\Downloads\...` |
| Facilitador do MM02 | Conforme `09_Homologacao/Testes_de_Aceitacao.md`, seção C: Luiggi Bortolini |
| Sistema operacional | não registrado (rodada preliminar) |
| Navegador | Opera GX |
| Python e Flask | não registrado (rodada preliminar) |
| Versão do sistema testada | não registrado (rodada preliminar) |
| Resultado do MM01/CT037-M | não registrado (rodada preliminar) |

## 2. Ressalva sobre a versão testada

As capturas 01, 02 e 06 a 09 mostram a pasta `05_Codigo_Fonte`, e o aviso do Windows (02, 07, 08 e 09) indica origem em `C:\Users\pedro\Downloads\Projeto_FolhaPagamento_...`. Nessa pasta já existem `__pycache__` e `htmlcov` (gerados por execuções anteriores), e os arquivos estão datados de 11/11/2026 21:11. A captura 01 mostra a página do GitHub ao fundo, com o último commit `6294a72` "1 hour ago".

Portanto, **estas capturas não mostram o ZIP `07_Executavel/Projeto_FolhaPagamento_Executavel.zip` descompactado em pasta limpa**, que é o procedimento descrito no CT037-M, e elas antecedem os commits de 12/11/2026. A avaliação pede "a versão exata do executável que será entregue". Há duas saídas, e a escolha é da equipe:

1. Repetir o CT037-M com o ZIP final, em pasta limpa, e substituir ou complementar estas capturas.
2. Manter estas capturas e declarar no relatório, de forma explícita, que elas se referem à versão de 11/11/2026 (commit: não registrado (rodada preliminar)), registrando o MM01 como "Aprovado com ressalvas".

## 3. MM01 / CT037-M: abrir pelo atalho e persistir após reabrir

Passos do CT037-M: descompactar em pasta limpa, dois cliques no atalho, entrar com `1 / 01012000`, trocar a senha, cadastrar um colaborador, fechar a janela, abrir de novo e consultar a lista.

| Passo | Capturas | O que se vê | Situação da prova |
|---|---|---|---|
| Descompactar em pasta limpa | (nenhuma) | Ver ressalva da seção 2 | **Sem prova** |
| Dois cliques em `iniciar.bat` | 01, 02 | 01: pasta `05_Codigo_Fonte` com `iniciar` selecionado (21:30). 02: aviso do Windows "O fornecedor não pôde ser verificado" para `iniciar.bat` | Comprovado |
| Navegador abre sozinho no login | 03 | `127.0.0.1:5000/login`, campos vazios (21:31) | Comprovado |
| Entrar com `1 / 01012000` | (nenhuma) | O preenchimento não foi capturado. O redirecionamento da captura 04 indica que o login ocorreu | Indireta |
| Troca obrigatória da senha | 04, 05 | 04: tela "Alterar minha senha" com o usuário "Administrador (Admin/RH)". 05: mensagem "Senha alterada com sucesso" e a lista só com o Administrador (matrícula 1) | Comprovado |
| Cadastrar um colaborador | (nenhuma) | O formulário e a mensagem de confirmação não foram capturados. O resultado (Pedro Kolling, matrícula 2, Comissionado, R$ 2.500,00, 5,00%) aparece só nas capturas 10 e 11 | **Lacuna** |
| Fechar a janela | (nenhuma) | Não há captura do encerramento do console | **Lacuna** |
| Abrir de novo pelo atalho | 06, 07, 08, 09 | 06: pasta com `iniciar` selecionado. 07, 08 e 09: o mesmo aviso do Windows em três recortes do mesmo momento. A tela de fundo mostra o roteiro com o passo "abra de novo pelo `iniciar.bat`" | Comprovado (sem relógio visível) |
| Mesmo cadastro continua na lista | 10, 11 | Lista com Administrador e Pedro Kolling, sem mensagem de confirmação, o que indica carga nova da página. 10 mostra o console do servidor ao lado; 11 mostra a mesma lista em tela cheia | Comprovado em parte: falta a prova do cadastro anterior |

## 4. MM02 / CT039: capturas por tarefa e por conta

Regras do sistema para confirmar a conta de cada tarefa (conforme `colaboradores.py` e `folha.py`, `@nivel_exigido`): cadastrar, alterar, lançar vendas, gerar e fechar a folha exigem nível 1 (Admin/RH). O nível 2 (Financeiro) consulta colaboradores e folha. O nível 3 (Comum) vê apenas "Minhas folhas" e "Meus dados".

| Tarefa do Plano | Perfil | Capturas | O que se vê | Conta usada |
|---|---|---|---|---|
| T1. Entrar e trocar a própria senha | Colaborador (Comum) | 12, 13 | 12: "Pedro Kolling (Comum)" com o aviso "Por segurança, troque a senha inicial antes de continuar". 13: "Minhas folhas" vazia ("Nenhuma folha fechada ainda") | Visível: Pedro Kolling, matrícula 2 |
| T1. Entrar e trocar a própria senha | Admin/RH | 04, 05 | Ver seção 3 | Visível: Administrador, matrícula 1 |
| Início de sessão com a matrícula 4 | A confirmar | 15 | Tela de login com matrícula `4` e senha de 8 caracteres. Na lista (14), a matrícula 4 é Jose Patricio | não registrado (rodada preliminar) |
| T2. Cadastrar colaborador Comissionado | Exige nível 1 | 16, 17 | 16: formulário "Novo colaborador" preenchido (Luiggi, Comissionado, R$ 2.500,00, nível 3 Comum). 17: "Colaborador cadastrado. Matrícula 5" e a lista com Luiggi | não registrado (rodada preliminar) |
| T3. Lançar vendas, gerar e fechar a folha | Exige nível 1 | 18, 19, 20 | 18: "Lançamentos de Novembro/2026" com vendas 0,00. 19: "Lançamentos salvos e folha recalculada", mês ABERTO (prévia), total R$ 25.980,00. 20: "Folha fechada...", mês FECHADO (congelado) | não registrado (rodada preliminar) |
| T5. Abrir e imprimir o próprio recibo | Colaborador (Comum) | 21, 22 | 21: recibo de Pedro Kolling, matrícula 2, vendas R$ 22.000,00, comissão 5,00% = R$ 1.100,00, líquido R$ 3.600,00. 22: visualização de impressão (cabeçalho "11/11/2026, 21:55", rodapé `127.0.0.1:5000/folha/2`, destino "Microsoft Print to PDF") e menu "(Comum)" | Visível: Pedro Kolling, matrícula 2 |
| Consulta e filtros | Somente consulta | 23, 24 | Lista de Colaboradores sem a coluna "Ações". 23: tipo "Comissionado" escolhido, mas ainda com o resultado do filtro anterior (só Padrão). 24: salário máximo 5000, Administrador, Luiggi e Pedro Kolling | não registrado (rodada preliminar) |

Conferências aritméticas feitas sobre as imagens: 22.000,00 × 5% = 1.100,00 e 2.500,00 + 1.100,00 = 3.600,00 (captura 21); 0 + 13.000 + 2.680 + 3.600 + 6.700 = 25.980,00 (captura 19).

## 5. Lacunas que a equipe precisa fechar

1. **Versão testada** (seção 2): repetir com o ZIP final ou declarar a ressalva.
2. **Cadastro e encerramento no CT037-M:** faltam o formulário e a confirmação de cadastro, a lista antes de fechar e o fechamento da janela. Sem eles, as capturas 10 e 11 não provam que é o "mesmo cadastro" criado antes de fechar.
3. **Relógio ausente nas capturas 02, 04 a 13, 15 a 21, 23 e 24:** a ordem delas foi deduzida (seção 7). Se houver hora registrada em outro lugar (histórico do navegador, console), vale anotá-la.
4. **Conta de cada tarefa do MM02:** o código só permite T2 e T3 com nível 1, mas as capturas 16 a 20 não mostram quem estava logado. Registrar matrícula e perfil, ou refazer a rodada com a conta RH identificada.
5. **T4 (filtrar a folha):** o Plano descreve o filtro na folha, e as capturas 23 e 24 mostram o filtro na lista de Colaboradores. Capturar o filtro na tela "Folha de pagamento" ou ajustar a descrição da tarefa.
6. **Participante Financeiro:** não há captura de T1 e T5 para ele. Associar P1 e P2 de `Testes_de_Aceitacao.md` às matrículas usadas.
7. **Consolidação final:** com a seção 1 preenchida, copiar o resultado do MM01 para `09_Homologacao/Testes_de_Aceitacao.md` (seção C) e para o relatório de testes, usando esta sequência como referência.

## 6. Correspondência entre os nomes antigos e os novos

A coluna "Confiança" indica o quanto a posição na sequência está sustentada pelo conteúdo da imagem.

| Nova posição | Nome antigo | Nome novo | Confiança |
|---|---|---|---|
| 01 | `MM01_Evidencia_1.png` | `01_MM01_pasta_com_iniciar_bat.png` | Alta (relógio 21:30) |
| 02 | `MM01_Evidencia_2.png` | `02_MM01_aviso_seguranca_windows.png` | Alta |
| 03 | `MM01_Evidencia_3.png` | `03_MM01_tela_login_primeira_abertura.png` | Alta (relógio 21:31) |
| 04 | `MM01_Evidencia_4.png` | `04_MM01_troca_obrigatoria_senha_admin.png` | Alta |
| 05 | `MM01_Evidencia_5.png` | `05_MM01_senha_alterada_lista_so_admin.png` | Alta |
| 06 | `MM01_Evidencia_6.png` | `06_MM01_reabertura_pasta_com_iniciar_bat.png` | Média |
| 07 | `MM01_Evidencia_7.png` | `07_MM01_reabertura_aviso_seguranca.png` | Média |
| 08 | `MM01_Evidencia_9.png` | `08_MM01_reabertura_aviso_seguranca_vista_ampla.png` | Média |
| 09 | `MM01_Evidencia_20.png` | `09_MM01_reabertura_aviso_seguranca_recorte.png` | Média |
| 10 | `MM01_Evidencia_8.png` | `10_MM01_reabertura_lista_com_Pedro_Kolling.png` | Média |
| 11 | `MM01_Evidencia_10.png` | `11_MM01_reabertura_lista_com_Pedro_Kolling_tela_cheia.png` | Média |
| 12 | `MM01_Evidencia_11.png` | `12_MM02_colaborador_troca_senha_inicial.png` | Média |
| 13 | `MM01_Evidencia_12.png` | `13_MM02_colaborador_minhas_folhas_vazio.png` | Média |
| 14 | `MM01_Evidencia_13.png` | `14_MM02_lista_4_colaboradores_21h47.png` | Alta (relógio 21:47) |
| 15 | `MM01_Evidencia_14.png` | `15_MM02_login_matricula_4.png` | **Baixa** |
| 16 | `MM01_Evidencia_16.png` | `16_MM02_T2_cadastro_Luiggi_formulario.png` | Alta |
| 17 | `MM01_Evidencia_15.png` | `17_MM02_T2_cadastro_Luiggi_confirmado_matricula_5.png` | Alta |
| 18 | `MM01_Evidencia_17.png` | `18_MM02_T3_lancamentos_novembro_2026.png` | Alta |
| 19 | `MM01_Evidencia_18.png` | `19_MM02_T3_folha_recalculada_mes_aberto.png` | Alta |
| 20 | `MM01_Evidencia_19.png` | `20_MM02_T3_folha_fechada_novembro_2026.png` | Alta |
| 21 | `MM01_Evidencia_22.png` | `21_MM02_T5_recibo_na_tela_Pedro_Kolling.png` | Alta |
| 22 | `MM01_Evidencia_21.png` | `22_MM02_T5_impressao_recibo_21h55.png` | Alta (relógio 21:55) |
| 23 | `MM01_Evidencia_23.png` | `23_MM02_consulta_colaboradores_filtro_tipo.png` | **Baixa** |
| 24 | `MM01_Evidencia_24.png` | `24_MM02_consulta_colaboradores_filtro_salario_maximo.png` | Média (Luiggi já existe, então vem depois da 17) |

Os nomes 12 a 24 usam o prefixo `MM02` porque as telas correspondem às tarefas do roteiro de usabilidade (T1 a T5) e à conta Colaborador, e não aos passos do CT037-M. A avaliação chama as 24 capturas de "MM01"; se a equipe preferir manter o prefixo único, basta trocar `MM02` por `MM01` nos nomes.

## 7. Como a ordem foi definida

- **Relógios visíveis:** 21:30, 21:31, 21:47 e 21:55 fixam as capturas 01, 03, 14 e 22.
- **Mensagens de confirmação:** a captura 17 ("Colaborador cadastrado") vem depois do formulário 16. A 19 ("Lançamentos salvos") vem depois da 18, e a 20 ("Folha fechada") vem depois da 19.
- **Estado dos dados:** Pedro Kolling aparece a partir da 10, e Luiggi só a partir da 17. "Nenhuma folha fechada ainda" (13) só é possível antes do fechamento (20).
- **Recibo:** a tela do recibo (21) vem antes da janela de impressão (22).
- **Reabertura:** as capturas 07, 08 e 09 têm o mesmo fundo (roteiro aberto no passo de reabrir), por isso foram agrupadas após a 05. A 06 aparece como a seleção de `iniciar` imediatamente anterior.
- **Pontos de menor certeza:** 15 (login da matrícula 4) e 23 (filtro de tipo) não têm relógio nem mensagem que fixem a posição. Se a equipe souber a ordem real, é só trocar o prefixo numérico.
