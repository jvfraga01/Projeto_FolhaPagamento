# Relatório de Revisão Técnica (A3)

Entregável 6.8. Revisões de 10/11/2026 e 11/11/2026 (ata: `Ata_de_Revisao_Tecnica_A1.md`; defeitos: `Registro_de_Defeitos.md`).

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
| 8 | Tag A3 divergente; ata sem extensão e duplicada; `.gitignore`/`.gitattributes` duplicados; `LEIA-ME.md` repetidos | Avaliação A3 | Documental |
| 9 | Entregáveis de A3 só com README (sem evidências de execução, cobertura, defeitos, manuais) | Avaliação A3 | Processo |
| 10 | `parse_reais("1.5000")` e `"01.500"` aceitos como R$ 1,50 | Avaliação de 11/11/2026 | Média (BUG007) |
| 11 | Pacote de entrega com `instance/secret.key`, banco, `.coverage`, `htmlcov/` | Avaliação de 11/11/2026 | Média (BUG008) |
| 12 | Números de testes e cobertura divergentes entre documentos; relatórios com campos em branco | Avaliação de 11/11/2026 | Documental |
| 13 | CT043 e CT044 com tipo incoerente; 5 testes sem caso associado; sem relatório de integração nem arquivo de métricas | Avaliação de 11/11/2026 | Documental |

## Correções realizadas
| # | Correção | Data | Evidência |
|---|---|---|---|
| 1 | `_decimal`: ponto de milhar e recusa de formatos ambíguos (BUG001, BUG007) | 10 e 11/11/2026 | CT046, CT047 |
| 2 | Troca obrigatória da senha inicial e remoção da dica no login (BUG002, RF021) | 10/11/2026 | CT052, CT053, CT037-A |
| 3 | Triggers para período fechado (BUG003) | 10/11/2026 | CT048 |
| 4 | `gerar` remove quem perdeu o contrato; reativar documentado e testado; massa de teste sem dependência de data (BUG004–BUG006) | 11/11/2026 | CT056, CT057 |
| 5 | `gerar_cobertura.py` registra o executor e atualiza os documentos; `empacotar_entrega.py` monta o ZIP limpo (BUG008) | 11/11/2026 | `04_Testes/evidencias/` |
| 6 | Números dos documentos passam a vir das evidências (marcadores automáticos); relatório de níveis de teste; `Metricas_e_Indicadores.md` | 11/11/2026 | Relatórios 04 e 10 |
| 7 | Casos CT054–CT057 criados; CT030 automatizado; CT043 e CT044 reclassificados; CT039 simplificado | 11/11/2026 | `Casos_de_Teste.md` |
| 8 | Versão 1.3 (A3) e tag `v1.3-A3` unificadas; duplicados removidos; apresentação, roteiro e pacote em `07_Executavel/` criados | 11/11/2026 | READMEs, pastas 07 e 11 |

Pendentes (dependem de pessoas): roteiros MM01 e MM02, Termo assinado, commit e tag finais.

## Lições aprendidas
- Declarar "aprovado" só com evidência: cobertura e saída dos testes são geradas por script e guardadas no repositório.
- Números repetidos em vários documentos divergem; copiá-los automaticamente das evidências evita o problema.
- Revisar documentos junto com o código: vários apontamentos eram divergências entre ERS, Plano e implementação.
- Tratar entradas reais do usuário (ponto de milhar) evita erro silencioso em valor monetário, e a correção precisa cobrir a família inteira de casos, não só o exemplo.
- Decisões de segurança "por simplicidade" (senha inicial visível) merecem revisão no início do projeto.
- Conferir o que vai dentro do pacote de entrega: chave secreta e banco local não devem sair da máquina.
