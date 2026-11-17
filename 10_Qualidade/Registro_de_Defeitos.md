# Registro de Defeitos

Modelo: Anexo I, item 9. Fluxo do PGQ: **Novo → Em_Correcao → Corrigido → Homologado → Fechado**.
Origem dos BUG001–BUG006: Avaliação A3 provisória de 10/11/2026 (achados por leitura de código).
"Corrigido" significa que a correção está no código e os testes correspondentes passaram na execução de 10/11/2026; "Homologado" exige a validação formal da equipe (<<PREENCHER: data e responsável da homologação>>).

| ID | Descrição | Severidade | Prioridade | Status | Responsável | Solução aplicada | Teste que comprova |
|---|---|---|---|---|---|---|---|
| BUG001 | `parse_reais("1.500")` devolvia 150 centavos (R$ 1,50): ponto de milhar era lido como decimal e gravado sem aviso. | Alta | Alta | Corrigido (Correção #1); testes CT046–CT048 aprovados em 10/11/2026 | <<PREENCHER: responsável>> | `regras._decimal` passou a tratar grupos de 3 dígitos com ponto como milhar ("1.500" = R$ 1.500,00); "12.50" e "0.500" seguem decimais; "1,500.00" (formato americano) é recusado. | CT046, CT047 |
| BUG002 | A tela de login exibia matrícula e senha do admin inicial enquanto a senha não fosse trocada. | Alta | Média | Corrigido (Correção #3), aguardando reexecução da suíte | <<PREENCHER: responsável>> | Decisão da equipe em 10/11/2026: forçar a troca. A dica foi removida do login; quem entra com a senha inicial só acessa a tela de senha e o logout, e a nova senha não pode ser a inicial (RF021). | CT052, CT053, CT037-A |
| BUG003 | O banco permitia reabrir período fechado (`UPDATE periodo`) e inserir folha em período fechado, ao contrário de ERS RN012 e UC011 ("nem pelo banco"). | Média | Alta | Corrigido (Correção #1); testes CT046–CT048 aprovados em 10/11/2026 | <<PREENCHER: responsável>> | Triggers `folha_fechada_no_insert`, `periodo_fechado_no_update` e `periodo_fechado_no_delete` em `schema.sql` (cópia em `06_Banco_Dados/`). O fechamento ABERTO→FECHADO continua permitido. | CT048 |
| BUG004 | `reativar` zera `data_fim_contrato` e perde a data original de término. | Média | Média | Novo | <<PREENCHER: responsável>> | Pendente. | A definir |
| BUG005 | `gerar` em mês aberto não remove quem deixou de ter contrato vigente depois da primeira geração. | Baixa | Baixa | Novo | <<PREENCHER: responsável>> | Pendente. | A definir |
| BUG006 | O admin inicial nasce com `data_inicio_contrato = hoje`; a contagem de colaboradores da folha de testes depende da data de execução. | Baixa | Baixa | Novo | <<PREENCHER: responsável>> | Pendente. | A definir |

Datas de abertura e de correção de cada defeito: <<PREENCHER: datas reais>>.

## Resumo (conferir com a tabela acima)
| Indicador | Valor |
|---|---|
| Defeitos registrados | 6 |
| Com correção no código | 3 (BUG001, BUG002, BUG003) |
| Abertos (Novo) | 3 (BUG004, BUG005, BUG006) |
| Críticos abertos | 0 |
| Altos abertos | 0 |
| Defeitos descobertos pela execução da suíte | 0 (61 testes aprovados na execução de 10/11/2026; reexecução dos 70: <<PREENCHER>>) |
