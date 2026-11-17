# Relatório de Revisão Técnica (A3)

Entregável 6.8. Registro da revisão de 10/11/2026 (ata: `Ata_de_Revisao_Tecnica_A1.md`). Participantes: ver ata.

## Não conformidades e problemas encontrados
| # | Problema | Origem | Severidade |
|---|---|---|---|
| 1 | Valor "1.500" gravado como R$ 1,50 | Avaliação A3 de 10/11/2026 (leitura) | Alta (BUG001) |
| 2 | Credencial do admin exibida na tela de login | Avaliação A3 | Alta (BUG002) |
| 3 | Banco aceitava reabrir mês e inserir folha em mês fechado, contra RN012 | Avaliação A3 | Média (BUG003) |
| 4 | `reativar` perde a data de fim de contrato original | Avaliação A3 | Média (BUG004) |
| 5 | `gerar` não remove quem perdeu o contrato no mês aberto | Avaliação A3 | Baixa (BUG005) |
| 6 | Massa de teste depende da data de execução | Avaliação A3 | Baixa (BUG006) |
| 7 | Critério de usabilidade divergente entre ERS e Plano | Reavaliação A1 | Documental |
| 8 | Nome da tag A3 divergente; ata sem extensão; `.gitignore` e `.gitattributes` com nome errado | Avaliação A3 | Documental |
| 9 | Entregáveis de A3 só com README (sem evidências de execução, cobertura, defeitos, manuais) | Avaliação A3 | Processo |

## Correções realizadas (10/11/2026)
| # | Correção | Evidência |
|---|---|---|
| 1 | `_decimal` interpreta ponto de milhar | CT046, CT047 |
| 2 | Troca obrigatória da senha inicial e remoção da dica no login (RF021) | CT052, CT053, CT037-A |
| 3 | Triggers em `schema.sql` para período e INSERT em folha fechada | CT048 |
| 4 | 26 testes novos (senha, edição, lançamentos, lista, recibo, primeira execução); medição de cobertura automatizada | `04_Testes/evidencias/`; 61 testes OK e 92,2% em 10/11/2026; reexecução dos 70: <<PREENCHER>> |
| 5 | Critério de usabilidade unificado; tag `v-A3`; arquivos renomeados | ERS, Plano, PGQ, README |
| 6 | Registro de Defeitos, Relatório de Testes, Testes de Aceitação, Termo, manuais e relatórios criados | pastas 04, 08, 09, 10 |
| 7 | Portabilidade restrita ao Windows (RNF009) | ERS, Plano, CT044 |

Pendentes: BUG004–BUG006, execução dos 3 casos manuais (CT030, CT037-M, CT039), preenchimento dos campos `<<PREENCHER>>`.

## Lições aprendidas (propostas a partir dos fatos; a equipe confirma ou ajusta)
- Declarar "aprovado" só com evidência de execução: a cobertura e a saída dos testes passaram a ser geradas por script e guardadas no repositório.
- Revisar documentos junto com o código: vários apontamentos eram divergências entre ERS, Plano e implementação (RN012, critério de usabilidade, tag).
- Automatizar o que parecia manual reduz risco de não execução: 6 casos manuais viraram testes automáticos.
- Tratar entrada de dados com formatos reais do usuário (ponto de milhar) evita erro silencioso em valor monetário.
- Decisões de segurança "por simplicidade" (senha inicial visível) merecem revisão no início, não no fim.
- <<PREENCHER: lições adicionais da equipe>>
