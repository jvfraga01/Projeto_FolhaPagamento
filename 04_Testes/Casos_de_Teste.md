# 8. Especificação de Casos de Teste

Total: **45 casos** (mínimo exigido: 20).

**Legenda de tipo**
- **Auto**: automatizado em `05_Codigo_Fonte/tests/test_sistema.py` (44 testes, aprovados na execução de 27/10/2026; reexecutar a cada entrega com `python -m unittest discover -v`).
- **Manual (planejado)**: roteiro de execução manual **ainda não executado**; o resultado obtido será registrado na A3 com data e responsável.
- Casos que têm uma parte automática e outra manual aparecem em **duas linhas** (sufixos `-A` e `-M`).

**Massa de dados padrão** (criada pelos testes automatizados): Ana RH (nível 1, Padrão, 5.000,00); Fabio Financeiro (nível 2, Padrão, 4.000,00); Joao Comum (nível 3, Comissionado, base 3.000,00, comissão 3,00%); Maria Comum (nível 3, Por Produção, base 2.000,00, valor por unidade 2,50); Paulo Padrao (nível 3, Padrão, 2.500,00). Todos com nascimento 15/03/1990 (senha inicial 15031990) e contrato desde 01/01/2026.

**Regra de cálculo usada nos resultados esperados:** fórmulas do cliente (sem meta, bônus ou teto), exceto nos casos marcados como *modo com metas (opcional)*.

Resultado obtido e situação final de cada caso manual serão preenchidos na execução (A3).

| Código | Requisito | Objetivo | Dados e passos | Resultado esperado | Tipo | Teste automatizado |
|---|---|---|---|---|---|---|
| CT001 | RF001, RF002 | Cadastrar colaborador Padrão válido | Entrar como RH; Novo colaborador; nome "Novo Fulano", nascimento 01/12/2000, início do contrato 01/01/2026, nível 3, salário 2000,00, tipo Padrão; confirmar | Cadastro criado (HTTP 302); matrícula gerada; aparece na lista; entra com a senha inicial 01122000 | Auto | FiltrosTest.test_cadastro_valida_e_cria_com_senha_de_nascimento |
| CT002 | RF003 | Cadastrar colaborador Comissionado | Novo colaborador; nome "Carla Comissao", nascimento 20/06/1995, início 01/01/2026, nível 3, salário 3000,00, tipo Comissionado, comissão 3,00 | Cadastro salvo (302); no banco: tipo COMISSIONADO, salário 300000 centavos, comissão 300 pontos-base; campo de comissão aparece só para esse tipo | Auto | FiltrosTest.test_cadastro_comissionado_e_producao |
| CT003 | RF004 | Cadastrar colaborador por Produção | Novo colaborador; nome "Pedro Producao", nascimento 20/06/1995, início 01/01/2026, nível 3, salário 3000,00, tipo Por Produção, valor por unidade 2,50 | Cadastro salvo (302); no banco: tipo PRODUCAO, valor por unidade 250 centavos | Auto | FiltrosTest.test_cadastro_comissionado_e_producao |
| CT004 | RN002 | Recusar nome vazio | Novo colaborador com nome em branco; confirmar | Não grava; erro no campo nome (HTTP 400) | Auto | FiltrosTest.test_cadastro_valida_e_cria_com_senha_de_nascimento |
| CT005 | RN003 | Recusar salário negativo | Novo colaborador com salário -5; confirmar | Não grava; erro no campo salário | Auto | FiltrosTest.test_cadastro_valida_e_cria_com_senha_de_nascimento; CalculoTest.test_valores_negativos_sao_recusados |
| CT006 | RN004, RN005 | Recusar vendas e percentual negativos | (a) Lançamentos: vendas -5 para o comissionado; (b) cadastro Comissionado com comissão -1 | (a) nada é salvo (vendas anteriores mantidas); (b) HTTP 400 e nenhum colaborador criado | Auto | FolhaTest.test_valores_invalidos_nos_lancamentos_nao_salvam; FiltrosTest.test_recusa_percentual_e_valor_unidade_negativos |
| CT007 | RN006, RN007 | Recusar quantidade e valor por unidade negativos | (a) quantidade -3 (conversão de inteiro); (b) cadastro Por Produção com valor por unidade -1 | (a) ValueError "Não pode ser negativo"; (b) HTTP 400 e nenhum colaborador criado | Auto | CalculoTest.test_valores_negativos_sao_recusados; FiltrosTest.test_recusa_percentual_e_valor_unidade_negativos |
| CT008 | RN001 | Matrícula única, gerada pelo sistema | Cadastrar "Seq Um" e "Seq Dois" seguidos; tentar inserir uma matrícula repetida direto no banco | Matrículas diferentes e sequenciais (a segunda = primeira + 1); o banco recusa a duplicada | Auto | FiltrosTest.test_matricula_unica_e_sequencial |
| CT009 | RF005 | Consultar a lista de colaboradores | Entrar como RH e como Financeiro; abrir Colaboradores | Lista com matrícula, nome, tipo, salário e status; resposta HTTP 200 | Manual (planejado) | — |
| CT010 | RF018 | Filtros combinados | Filtrar nome "comum" + tipo Comissionado; depois salário máximo 2500,00 + status Ativo | Primeiro filtro: só Joao; segundo: Maria aparece e Joao não | Auto | FiltrosTest.test_filtros_de_colaboradores_combinados |
| CT011 | RF018 | Filtro de status | Desabilitar Maria; listar Ativos e depois Inativos | Ativos não mostra Maria; Inativos mostra | Auto | FiltrosTest.test_filtro_de_status |
| CT012 | RF009 | Alterar colaborador | RH abre Alterar em Paulo Padrao, muda nome para "Paulo Silva" e salário para 2600,00, salva; abrir folha de mês fechado anterior | Cadastro atualizado; folha fechada continua com nome e 2.500,00 originais | Manual (planejado) | — |
| CT013 | RF013 | Desabilitar colaborador | RH desabilita Joao, que está logado em outra sessão | Sessão cai na hora; login recusado; histórico preservado | Auto | LoginTest.test_usuario_desabilitado_perde_acesso_na_hora_e_pode_voltar |
| CT014 | RF013 | Reativar colaborador | RH reativa Joao | Joao volta a conseguir entrar | Auto | LoginTest.test_usuario_desabilitado_perde_acesso_na_hora_e_pode_voltar |
| CT015 | RF006, RN008 | Cálculo do tipo Padrão | Salário 3.000,00 tipo Padrão | Adicional 0,00; total 3.000,00 | Auto | CalculoTest.test_padrao_recebe_so_o_salario |
| CT016 | RF006, RN008 | Comissão = vendas × percentual | Base 3.000,00; comissão 3%; vendas 5.000,00 | Adicional 150,00; total 3.150,00 | Auto | CalculoTest.test_comissionado_vendas_vezes_percentual |
| CT017 | RF006, RN008 | Vendas abaixo de 5.000,00 continuam gerando comissão (fórmula do cliente) | Base 3.000,00; comissão 3%; vendas 4.999,99 | Adicional 150,00 (149,9997 arredondado); total 3.150,00 (não zera) | Auto | CalculoTest.test_comissionado_sem_meta_vendas_abaixo_de_5000 |
| CT018 | RF006, RN008 | Percentual cadastrado acima de 10% é aplicado sem teto | Base 0,00; comissão cadastrada 15,00%; vendas 1.000,00 | Percentual aplicado 15,00%; adicional 150,00 | Auto | CalculoTest.test_comissionado_percentual_cadastrado_sem_teto |
| CT019 | RF006, RN008 | Cálculo por Produção = quantidade × valor unitário | Base 1.000,00; valor unitário 2,50; produzir 99, 100 e 200 un | 99 un: adicional 247,50, total 1.247,50; 100 un: 250,00; 200 un: 500,00, total 1.500,00 (sem bônus) | Auto | CalculoTest.test_producao_quantidade_vezes_valor |
| CT020 | RF007, RF014, RF015 | Gerar folha, lançar e totalizar | RH gera a folha de março/2026; lança vendas 5.000,00 (Joao) e produção 100 un (Maria) | Joao 3.150,00; Maria 2.250,00; Paulo 2.500,00; modo padrão: meta 0 em todas as linhas | Auto | FolhaTest.test_gera_calcula_e_totaliza; FolhaTest.test_modo_padrao_nao_gera_meta |
| CT021 | RF008 | Resumo da folha | Após o CT020, abrir Relatório de março/2026 | Total geral 16.900,00 (5.000,00 + 4.000,00 + 3.150,00 + 2.250,00 + 2.500,00); Comissionado 3.150,00; Produção 2.250,00; quantidade de colaboradores 5 | Auto | FolhaTest.test_gera_calcula_e_totaliza; FiltrosTest.test_resumo_do_relatorio_com_totais |
| CT022 | RF010 | Login válido, inválido e logout | Entrar com senha errada; depois correta; sair | Errada: 401 e mensagem; correta: entra; após sair, páginas redirecionam ao login | Auto | LoginTest.test_login_logout_e_senha_errada; LoginTest.test_rotas_exigem_login |
| CT023 | RF011 | Trocar e redefinir senha | Joao troca a própria senha informando a atual; RH redefine a de Maria | Troca exige a senha atual; redefinição volta ao DDMMAAAA (15031990) | Manual (planejado) | — |
| CT024 | RF012 | Nível 3 sem acesso à gestão | Joao tenta abrir /colaboradores, /folha, /relatorio e ações POST | HTTP 403 em todos, sem dados | Auto | PermissaoTest.test_nivel3_nao_acessa_areas_de_gestao |
| CT025 | RN015 | Nível 3 não vê folha de outro | Joao abre /folha/<id da Maria>; abre /minha-folha?matricula=outro; tenta ver mês aberto | 403 sem o nome do outro; parâmetro ignorado; mês aberto negado | Auto | PermissaoTest.test_nivel3_nao_ve_folha_de_outro_nem_recebe_dados; test_minha_folha_ignora_parametros_da_url; test_nivel3_so_ve_folha_de_mes_fechado |
| CT026 | RF012 | Financeiro só consulta | Fabio abre listas/relatório e tenta criar, lançar, fechar | Leitura 200; alterações 403 | Auto | PermissaoTest.test_financeiro_le_mas_nao_altera |
| CT027 | RF016, RN012 | Folha fechada fica congelada | Fechar março/2026; alterar o salário de Joao para 9.999,99 no cadastro; tentar lançar e regerar; UPDATE direto no banco | Valores do mês não mudam (salário 3.000,00); lançamento 403; banco recusa | Auto | FolhaTest.test_folha_fechada_fica_congelada_mesmo_mudando_o_cadastro |
| CT028 | RN013 | Sem reabertura e uma folha por mês | Tentar reabrir; gerar o mesmo mês duas vezes | Sem rota de reabertura (404); apenas 1 folha por colaborador | Auto | FolhaTest.test_nao_ha_reabertura_nem_segunda_folha_no_mes |
| CT029-A | RF017 | Recibo individual (acesso e valores) | Joao abre Minhas folhas e o recibo de março/2026 fechado; tenta o recibo da Maria | Recibo próprio 200; recibo de outro 403 | Auto | PermissaoTest.test_nivel3_nao_ve_folha_de_outro_nem_recebe_dados |
| CT029-M | RF017 | Recibo individual (aparência) | Abrir o recibo no navegador e conferir os campos | Mostra matrícula, nome, tipo, salário base, adicional e líquido; botão Imprimir | Manual (planejado) | — |
| CT030 | RF020 | Imprimir relatório e recibo | Clicar em Imprimir e ver a pré-visualização | Menu e botões ocultos; texto legível em preto no branco | Manual (planejado) | — |
| CT031 | RNF004 | Novo tipo de remuneração sem alterar os existentes | Registrar em CALCULADORES o tipo EXPERIMENTAL com adicional fixo de R$ 100,00; calcular com base 1.000,00; recalcular os 3 tipos existentes (base 1.000,00, vendas 5.000,00, 100 un, 3%, valor 2,50) antes e depois | EXPERIMENTAL: total 1.100,00; Padrão, Comissionado e Por Produção com resultados idênticos aos de antes do registro | Auto | CalculoTest.test_novo_calculador_sem_alterar_os_existentes |
| CT032 | RNF005 | Proteção CSRF | Enviar POST sem token | HTTP 400, nada executado | Auto | LoginTest.test_post_sem_csrf_e_recusado |
| CT033 | RNF005 | Escape de HTML e sigilo do hash | Cadastrar nome '<script>alert(1)</script>'; abrir páginas e procurar o hash | Script aparece como texto; hash nunca exibido | Auto | FiltrosTest.test_nome_com_html_e_escapado; LoginTest.test_nao_vaza_hash_de_senha |
| CT034 | RN014 | Desabilitado aparece nos meses em que trabalhou | Desabilitar Paulo com fim de contrato em 31/03/2026; ver folha de março e de maio | Aparece em março; não aparece em maio | Auto | FolhaTest.test_desabilitado_aparece_nos_meses_em_que_trabalhou |
| CT035 | RN011 (opcional) | **Modo com metas (opcional):** meta cresce no mês seguinte | Com REGIME_METAS ligado: bater a meta em março e gerar abril | Meta de abril: comissionado 7.000,00; produção 150 un | Auto | FolhaRegimeMetasTest.test_meta_cresce_no_mes_seguinte_se_bateu |
| CT036 | RF013 | Não desabilitar a si mesmo nem o último admin | Ana tenta desabilitar a própria conta | Recusado; status continua Ativo | Auto | LoginTest.test_nao_desabilita_a_si_mesmo_nem_o_ultimo_admin |
| CT037 | RF010, RNF006 | Primeira execução cria banco e admin | Apagar a pasta instance/; dar dois cliques em iniciar.bat; entrar com 1 / 01012000 | Banco criado; login do admin funciona; aviso de primeiro acesso na tela | Manual (planejado) | — |
| CT038 | RN003 | Salário zero válido | Cadastrar "Salario Zero", tipo Padrão, salário 0,00; calcular Comissionado com base 0,00, vendas 1.000,00, comissão 3% | Cadastro aceito (302), salário 0 centavos; cálculo: adicional 30,00 e total 30,00; Padrão com 0,00 = total 0,00 | Auto | FiltrosTest.test_cadastro_com_salario_zero_e_aceito; CalculoTest.test_salario_zero_valido |
| CT039 | RNF001 | Usabilidade (roteiro) | Executar o roteiro de usabilidade do Plano de Testes (5 tarefas, 3 participantes) | Critérios do roteiro atendidos (ver Plano de Testes, seção Usabilidade) | Manual (planejado) | — |
| CT040 | RNF003 | Persistência após encerrar e reabrir | Cadastrar colaborador (salário 1.234,56); encerrar o aplicativo; reabrir com o mesmo arquivo de banco; consultar | O colaborador existe com salário 123456 centavos. Manual complementar na A3: fechar a janela do `iniciar.bat`, reabrir e consultar | Auto | PersistenciaTest.test_dados_sobrevivem_ao_reabrir_a_aplicacao |
| CT041 | RNF007 | Arredondamento em centavos | Base 0,00; comissão 3%; vendas 1.000,50 e depois 4.999,99 | 30,015 → 30,02 (meio para cima); 149,9997 → 150,00; valores em inteiros | Auto | CalculoTest.test_arredondamento_meio_para_cima_em_centavos |
| CT042 | RNF002 | Validação antes do cálculo e da gravação | Enviar nome vazio, salário -5, vendas -5 e quantidade -3 | Todas recusadas com mensagem; nada é calculado nem gravado | Auto | CalculoTest.test_valores_negativos_sao_recusados; FolhaTest.test_valores_invalidos_nos_lancamentos_nao_salvam; FiltrosTest.test_cadastro_valida_e_cria_com_senha_de_nascimento |
| CT043 | RNF008 | Cobertura de testes ≥ 80% | `python -m coverage run -m unittest discover` e `python -m coverage report -m` | Total ≥ 80% (meta; ainda não medida) | Manual (planejado, A3) | — |
| CT044 | RNF009 | Portabilidade | Instalar e executar nos sistemas Windows 10/11 e Ubuntu 22.04; abrir login e consultar colaboradores | Mesmo comportamento nos dois sistemas | Manual (planejado, A3) | — |
| CT045 | RN009 (opcional) | **Modo com metas (opcional):** meta não batida zera o adicional | Com REGIME_METAS ligado: Joao vendas 4.999,99 e Maria 99 un | Joao total 3.000,00; Maria total 2.000,00 | Auto | FolhaRegimeMetasTest.test_meta_nao_batida_zera_adicional_na_folha; RegimeMetasTest.test_meta_nao_batida_zera_adicional |

## Resumo por requisito (cobertura de casos)
Cada requisito abaixo tem ao menos um caso associado na Matriz de Rastreabilidade (`01_Requisitos/ERS.md`).

| Requisito | Casos | Como é verificado |
|---|---|---|
| RF001–RF020 | CT001–CT037, CT045 | Conforme a matriz de rastreabilidade |
| RN001–RN008, RN012–RN018 | CT001–CT008, CT015–CT021, CT027, CT028, CT034, CT038 | Casos diretos |
| RN009–RN011 (opcionais) | CT035, CT045 | Somente no modo com metas |
| RNF001 | CT039 | Roteiro de usabilidade (execução na A3) |
| RNF002 | CT042 (CT004–CT007) | Entradas inválidas recusadas antes do cálculo |
| RNF003 | CT040 | Reabertura do banco |
| RNF004 | CT031 | Calculador experimental |
| RNF005 | CT024, CT025, CT032, CT033 | Segurança |
| RNF006 | CT037 | Primeira execução |
| RNF007 | CT041 | Arredondamento e centavos |
| RNF008 | CT043 | Medição de cobertura (A3) |
| RNF009 | CT044 | Execução em dois sistemas (A3) |

Itens marcados como "Manual (planejado)" não foram executados e não contam como evidência até o registro na A3.
