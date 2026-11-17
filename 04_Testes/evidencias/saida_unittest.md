# Saída dos testes

```text
test_banco_recusa_insert_de_folha_em_periodo_fechado (tests.test_correcoes_a3.BancoFolhaFechadaTest.test_banco_recusa_insert_de_folha_em_periodo_fechado) ... ok
test_banco_recusa_reabrir_e_apagar_periodo_fechado (tests.test_correcoes_a3.BancoFolhaFechadaTest.test_banco_recusa_reabrir_e_apagar_periodo_fechado) ... ok
test_periodo_aberto_continua_aceitando_novos_colaboradores (tests.test_correcoes_a3.BancoFolhaFechadaTest.test_periodo_aberto_continua_aceitando_novos_colaboradores) ... ok
test_cadastro_com_ponto_de_milhar_grava_valor_correto (tests.test_correcoes_a3.CadastroMilharTest.test_cadastro_com_ponto_de_milhar_grava_valor_correto) ... ok
test_cadastro_com_texto_no_lugar_de_numero_e_recusado (tests.test_correcoes_a3.CadastroMilharTest.test_cadastro_com_texto_no_lugar_de_numero_e_recusado) ... ok
test_editar_atualiza_cadastro_e_preserva_mes_fechado (tests.test_correcoes_a3.EdicaoTest.test_editar_atualiza_cadastro_e_preserva_mes_fechado) ... ok
test_editar_com_dado_invalido_nao_grava (tests.test_correcoes_a3.EdicaoTest.test_editar_com_dado_invalido_nao_grava) ... ok
test_ultimo_administrador_ativo_nao_perde_o_nivel (tests.test_correcoes_a3.EdicaoTest.test_ultimo_administrador_ativo_nao_perde_o_nivel) ... ok
test_com_senha_ja_trocada_entra_direto (tests.test_correcoes_a3.ForcaTrocaSenhaTest.test_com_senha_ja_trocada_entra_direto) ... ok
test_login_com_senha_inicial_exige_a_troca (tests.test_correcoes_a3.ForcaTrocaSenhaTest.test_login_com_senha_inicial_exige_a_troca) ... ok
test_nova_senha_nao_pode_ser_a_inicial (tests.test_correcoes_a3.ForcaTrocaSenhaTest.test_nova_senha_nao_pode_ser_a_inicial) ... ok
test_redefinicao_pelo_rh_volta_a_exigir_a_troca (tests.test_correcoes_a3.ForcaTrocaSenhaTest.test_redefinicao_pelo_rh_volta_a_exigir_a_troca) ... ok
test_tela_de_login_nao_exibe_credencial_do_admin (tests.test_correcoes_a3.ForcaTrocaSenhaTest.test_tela_de_login_nao_exibe_credencial_do_admin) ... ok
test_trocar_a_senha_libera_o_acesso (tests.test_correcoes_a3.ForcaTrocaSenhaTest.test_trocar_a_senha_libera_o_acesso) ... ok
test_css_de_impressao_oculta_menu_e_botoes (tests.test_correcoes_a3.ImpressaoTest.test_css_de_impressao_oculta_menu_e_botoes) ... ok
test_tela_de_lancamentos_em_mes_aberto_e_fechado (tests.test_correcoes_a3.LancamentosTest.test_tela_de_lancamentos_em_mes_aberto_e_fechado) ... ok
test_texto_no_lugar_de_numero_nao_salva_nada (tests.test_correcoes_a3.LancamentosTest.test_texto_no_lugar_de_numero_nao_salva_nada) ... ok
test_lista_de_colaboradores_para_rh_e_financeiro (tests.test_correcoes_a3.ListaEReciboTest.test_lista_de_colaboradores_para_rh_e_financeiro) ... ok
test_recibo_mostra_os_campos_e_o_botao_imprimir (tests.test_correcoes_a3.ListaEReciboTest.test_recibo_mostra_os_campos_e_o_botao_imprimir) ... ok
test_formato_ambiguo_e_recusado (tests.test_correcoes_a3.MilharTest.test_formato_ambiguo_e_recusado) ... ok
test_percentual_com_ponto (tests.test_correcoes_a3.MilharTest.test_percentual_com_ponto) ... ok
test_ponto_de_milhar_sem_virgula (tests.test_correcoes_a3.MilharTest.test_ponto_de_milhar_sem_virgula) ... ok
test_ponto_decimal_e_virgula_continuam_validos (tests.test_correcoes_a3.MilharTest.test_ponto_decimal_e_virgula_continuam_validos) ... ok
test_pontos_em_formato_invalido_sao_recusados (tests.test_correcoes_a3.MilharTest.test_pontos_em_formato_invalido_sao_recusados) ... ok
test_banco_novo_cria_admin_e_exige_troca (tests.test_correcoes_a3.PrimeiraExecucaoTest.test_banco_novo_cria_admin_e_exige_troca) ... ok
test_gerar_remove_da_folha_aberta_quem_perdeu_o_contrato_no_mes (tests.test_correcoes_a3.ReativacaoETermoDeContratoTest.test_gerar_remove_da_folha_aberta_quem_perdeu_o_contrato_no_mes) ... ok
test_reativar_preserva_folhas_fechadas_e_volta_a_entrar_nas_novas (tests.test_correcoes_a3.ReativacaoETermoDeContratoTest.test_reativar_preserva_folhas_fechadas_e_volta_a_entrar_nas_novas) ... ok
test_rh_redefine_senha_para_data_de_nascimento (tests.test_correcoes_a3.SenhaTest.test_rh_redefine_senha_para_data_de_nascimento) ... ok
test_troca_de_senha_com_senha_atual_correta (tests.test_correcoes_a3.SenhaTest.test_troca_de_senha_com_senha_atual_correta) ... ok
test_troca_recusada_senha_errada_curta_ou_confirmacao_diferente (tests.test_correcoes_a3.SenhaTest.test_troca_recusada_senha_errada_curta_ou_confirmacao_diferente) ... ok
test_arredondamento_meio_para_cima_em_centavos (tests.test_sistema.CalculoTest.test_arredondamento_meio_para_cima_em_centavos) ... ok
test_comissionado_percentual_cadastrado_sem_teto (tests.test_sistema.CalculoTest.test_comissionado_percentual_cadastrado_sem_teto) ... ok
test_comissionado_sem_meta_vendas_abaixo_de_5000 (tests.test_sistema.CalculoTest.test_comissionado_sem_meta_vendas_abaixo_de_5000) ... ok
test_comissionado_vendas_vezes_percentual (tests.test_sistema.CalculoTest.test_comissionado_vendas_vezes_percentual) ... ok
test_dinheiro (tests.test_sistema.CalculoTest.test_dinheiro) ... ok
test_novo_calculador_sem_alterar_os_existentes (tests.test_sistema.CalculoTest.test_novo_calculador_sem_alterar_os_existentes) ... ok
test_padrao_recebe_so_o_salario (tests.test_sistema.CalculoTest.test_padrao_recebe_so_o_salario) ... ok
test_producao_quantidade_vezes_valor (tests.test_sistema.CalculoTest.test_producao_quantidade_vezes_valor) ... ok
test_salario_zero_valido (tests.test_sistema.CalculoTest.test_salario_zero_valido) ... ok
test_valores_negativos_sao_recusados (tests.test_sistema.CalculoTest.test_valores_negativos_sao_recusados) ... ok
test_cadastro_com_salario_zero_e_aceito (tests.test_sistema.FiltrosTest.test_cadastro_com_salario_zero_e_aceito) ... ok
test_cadastro_comissionado_e_producao (tests.test_sistema.FiltrosTest.test_cadastro_comissionado_e_producao) ... ok
test_cadastro_valida_e_cria_com_senha_de_nascimento (tests.test_sistema.FiltrosTest.test_cadastro_valida_e_cria_com_senha_de_nascimento) ... ok
test_filtro_de_status (tests.test_sistema.FiltrosTest.test_filtro_de_status) ... ok
test_filtros_de_colaboradores_combinados (tests.test_sistema.FiltrosTest.test_filtros_de_colaboradores_combinados) ... ok
test_matricula_unica_e_sequencial (tests.test_sistema.FiltrosTest.test_matricula_unica_e_sequencial) ... ok
test_nome_com_html_e_escapado (tests.test_sistema.FiltrosTest.test_nome_com_html_e_escapado) ... ok
test_recusa_percentual_e_valor_unidade_negativos (tests.test_sistema.FiltrosTest.test_recusa_percentual_e_valor_unidade_negativos) ... ok
test_resumo_do_relatorio_com_totais (tests.test_sistema.FiltrosTest.test_resumo_do_relatorio_com_totais) ... ok
test_meta_cresce_no_mes_seguinte_se_bateu (tests.test_sistema.FolhaRegimeMetasTest.test_meta_cresce_no_mes_seguinte_se_bateu) ... ok
test_meta_nao_batida_zera_adicional_na_folha (tests.test_sistema.FolhaRegimeMetasTest.test_meta_nao_batida_zera_adicional_na_folha) ... ok
test_desabilitado_aparece_nos_meses_em_que_trabalhou (tests.test_sistema.FolhaTest.test_desabilitado_aparece_nos_meses_em_que_trabalhou) ... ok
test_folha_fechada_fica_congelada_mesmo_mudando_o_cadastro (tests.test_sistema.FolhaTest.test_folha_fechada_fica_congelada_mesmo_mudando_o_cadastro) ... ok
test_gera_calcula_e_totaliza (tests.test_sistema.FolhaTest.test_gera_calcula_e_totaliza) ... ok
test_modo_padrao_nao_gera_meta (tests.test_sistema.FolhaTest.test_modo_padrao_nao_gera_meta) ... ok
test_nao_ha_reabertura_nem_segunda_folha_no_mes (tests.test_sistema.FolhaTest.test_nao_ha_reabertura_nem_segunda_folha_no_mes) ... ok
test_valores_invalidos_nos_lancamentos_nao_salvam (tests.test_sistema.FolhaTest.test_valores_invalidos_nos_lancamentos_nao_salvam) ... ok
test_login_logout_e_senha_errada (tests.test_sistema.LoginTest.test_login_logout_e_senha_errada) ... ok
test_nao_desabilita_a_si_mesmo_nem_o_ultimo_admin (tests.test_sistema.LoginTest.test_nao_desabilita_a_si_mesmo_nem_o_ultimo_admin) ... ok
test_nao_vaza_hash_de_senha (tests.test_sistema.LoginTest.test_nao_vaza_hash_de_senha) ... ok
test_post_sem_csrf_e_recusado (tests.test_sistema.LoginTest.test_post_sem_csrf_e_recusado) ... ok
test_rotas_exigem_login (tests.test_sistema.LoginTest.test_rotas_exigem_login) ... ok
test_usuario_desabilitado_perde_acesso_na_hora_e_pode_voltar (tests.test_sistema.LoginTest.test_usuario_desabilitado_perde_acesso_na_hora_e_pode_voltar) ... ok
test_financeiro_le_mas_nao_altera (tests.test_sistema.PermissaoTest.test_financeiro_le_mas_nao_altera) ... ok
test_minha_folha_ignora_parametros_da_url (tests.test_sistema.PermissaoTest.test_minha_folha_ignora_parametros_da_url) ... ok
test_nivel3_nao_acessa_areas_de_gestao (tests.test_sistema.PermissaoTest.test_nivel3_nao_acessa_areas_de_gestao) ... ok
test_nivel3_nao_ve_folha_de_outro_nem_recebe_dados (tests.test_sistema.PermissaoTest.test_nivel3_nao_ve_folha_de_outro_nem_recebe_dados) ... ok
test_nivel3_so_ve_folha_de_mes_fechado (tests.test_sistema.PermissaoTest.test_nivel3_so_ve_folha_de_mes_fechado) ... ok
test_dados_sobrevivem_ao_reabrir_a_aplicacao (tests.test_sistema.PersistenciaTest.test_dados_sobrevivem_ao_reabrir_a_aplicacao) ... ok
test_meta_batida_usa_percentual_cadastrado (tests.test_sistema.RegimeMetasTest.test_meta_batida_usa_percentual_cadastrado) ... ok
test_meta_cresce_quando_bate_e_nunca_cai_abaixo_do_minimo (tests.test_sistema.RegimeMetasTest.test_meta_cresce_quando_bate_e_nunca_cai_abaixo_do_minimo) ... ok
test_meta_nao_batida_zera_adicional (tests.test_sistema.RegimeMetasTest.test_meta_nao_batida_zera_adicional) ... ok
test_producao_com_meta_e_bonus (tests.test_sistema.RegimeMetasTest.test_producao_com_meta_e_bonus) ... ok
test_progressao_1_ponto_a_cada_2_mil_e_teto_de_10 (tests.test_sistema.RegimeMetasTest.test_progressao_1_ponto_a_cada_2_mil_e_teto_de_10) ... ok

----------------------------------------------------------------------
Ran 74 tests in 56.549s

OK
```
