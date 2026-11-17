# Registro de Defeitos

Modelo: Anexo I, itens 9 e 20. Fluxo do PGQ: **Novo → Em_Correcao → Corrigido → Homologado → Fechado**. Status adicional: **Não procede** (comportamento esperado, justificado e coberto por teste).
Origem: avaliações A3 de 10/11/2026 e 11/11/2026 (leitura de código e execução). "Corrigido" = correção no código com teste de regressão aprovado na suíte. "Responsável" = papel de desenvolvimento conforme `03_Projeto/Planejamento_do_Projeto.md` (João Vitor Fraga, arquiteto/desenvolvedor).

| ID | Descrição | Severidade | Prioridade | Status | Responsável | Abertura | Correção | Solução aplicada | Teste |
|---|---|---|---|---|---|---|---|---|---|
| BUG001 | `parse_reais("1.500")` devolvia R$ 1,50: ponto de milhar lido como decimal e gravado sem aviso. | Alta | Alta | Corrigido | João Vitor Fraga | 10/11/2026 | 10/11/2026 | `regras._decimal` trata grupos de 3 dígitos como milhar; "1,500.00" é recusado. | CT046, CT047 |
| BUG002 | A tela de login exibia matrícula e senha do admin inicial. | Alta | Média | Corrigido | João Vitor Fraga | 10/11/2026 | 10/11/2026 | Troca obrigatória da senha inicial (RF021); dica removida do login. | CT052, CT053, CT037-A |
| BUG003 | O banco permitia reabrir período fechado e inserir folha em período fechado (contra RN012). | Média | Alta | Corrigido | João Vitor Fraga | 10/11/2026 | 10/11/2026 | Triggers `folha_fechada_no_insert`, `periodo_fechado_no_update` e `periodo_fechado_no_delete`. | CT048 |
| BUG004 | `reativar` limpa `data_fim_contrato`. | Média | Média | Não procede | João Vitor Fraga | 10/11/2026 | 11/11/2026 | Reativar significa contrato retomado; a data de fim anterior não faz mais sentido. O histórico fica nas folhas fechadas, que não mudam. Comportamento registrado e testado. | CT056 |
| BUG005 | `gerar` em mês aberto não removia quem perdeu o contrato no mês. | Baixa | Baixa | Corrigido | João Vitor Fraga | 10/11/2026 | 11/11/2026 | `folha.gerar` remove da folha aberta quem não tem mais contrato no mês e informa a quantidade. | CT057 |
| BUG006 | O admin inicial nasce com início de contrato = hoje; a massa de teste dependia do dia da execução. | Baixa | Baixa | Corrigido | João Vitor Fraga | 10/11/2026 | 11/11/2026 | `BaseTest` fixa o início do admin inicial em data futura; sem efeito no sistema. | Toda a suíte de folha (CT020, CT021) |
| BUG007 | `parse_reais("1.5000")` e `"01.500"` viravam R$ 1,50 sem aviso (mesma família do BUG001). | Média | Alta | Corrigido | João Vitor Fraga | 11/11/2026 | 11/11/2026 | Ponto sem vírgula só vale como milhar (grupos de 3 dígitos) ou decimal de até 2 casas; o restante é recusado. | CT046 |
| BUG008 | O pacote de entrega continha `instance/secret.key`, `folha.db`, `.coverage`, `htmlcov/` e `__pycache__/`. | Média | Alta | Corrigido | João Vitor Fraga | 11/11/2026 | 11/11/2026 | `empacotar_entrega.py` monta o ZIP sem esses itens. A chave local é regenerada ao apagar `instance/`. | Processo (conferir o conteúdo do ZIP) |

Resumo, taxa de correção e densidade: `10_Qualidade/Metricas_e_Indicadores.md` (calculado do quadro acima).
