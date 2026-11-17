# Relatório Final de Qualidade

Entregável 6.12. Cada resultado cita a evidência; o que ainda não foi medido está como `<<PREENCHER>>`.

## 1. Situação dos requisitos
| Grupo | Situação | Evidência |
|---|---|---|
| RF001–RF009 (cliente) | Implementados; cálculo pelas fórmulas do T1 | Testes CT001–CT021 |
| RF010–RF018, RF020 (responsável) | Implementados; desvios D2–D6 aceitos em 29 e 30/10/2026 | `01_Requisitos/Registro_de_Aceite_de_Desvios.md` |
| RF019 (modo opcional de metas) | Implementado, desligado por padrão; aceito (D1) em 30/10/2026 | CT035, CT045 |
| RF021 (troca obrigatória da senha inicial) | Implementado | CT052, CT053, CT037-A |
| RN001–RN018 | Implementadas; RN012 também garantida no banco (BUG003) | CT027, CT028, CT048 |
| RNF001 (usabilidade) | Implementado; execução do roteiro pendente | CT039 |
| RNF002–RNF005, RNF007 | Atendidos nos testes | CT040–CT042, CT031, CT024–CT033 |
| RNF006 (dois cliques) | Implementado; execução manual pendente | CT037-A (auto), CT037-M (manual) |
| RNF008 (cobertura ≥ 80%) | Atendido: 92,2% em 10/11/2026 (61 testes) | `04_Testes/evidencias/cobertura.txt` |
| RNF009 (portabilidade) | Verificado no Windows 11 | CT044 |

Matriz de rastreabilidade completa: `01_Requisitos/ERS.md`.

## 2. Resultados dos testes
| Indicador | Resultado |
|---|---|
| Testes automatizados no código | 70 (44 + 26) |
| Última execução registrada | 10/11/2026: 61 testes, todos OK (antes das correções do BUG002) |
| Reexecução dos 70 | <<PREENCHER: gerar_cobertura.py>> |
| Casos de teste planejados | 53 (CT001–CT053) |
| Casos manuais pendentes | 3: CT030, CT037-M, CT039 |
| Casos aprovados / executados | <<PREENCHER: após a reexecução e os manuais>> |
| Testes de aceitação | `09_Homologacao/Testes_de_Aceitacao.md` |

## 3. Métricas (PGQ)
| Métrica | Meta | Resultado |
|---|---|---|
| Cobertura de testes | ≥ 80% | 92,2% (10/11/2026); nova medição: <<PREENCHER>> |
| Requisitos atendidos | 100% | <<PREENCHER: RF/RN com teste aprovado ÷ total, após a reexecução>> |
| Casos de teste aprovados | ≥ 95% | <<PREENCHER>> |
| Defeitos críticos abertos | 0 | 0 |
| Defeitos corrigidos | 100% dos críticos e altos | Altos: BUG001 e BUG002 corrigidos; 0 críticos |
| Densidade de defeitos | acompanhar | 6 defeitos registrados |

Defeitos: 6 registrados, 3 corrigidos (BUG001, BUG002, BUG003) e 3 abertos de severidade média ou baixa (BUG004, BUG005, BUG006). Detalhe em `Registro_de_Defeitos.md`.

## 4. Evidências
Saída dos testes e cobertura (`04_Testes/evidencias/`), Registro de Defeitos, Relatório de Testes, Ata e Relatório de Revisão Técnica, histórico Git (`Historico_Git.txt` e `Evidencia_Controle_de_Versao.md`: <<PREENCHER: reexportar o histórico e preencher hash e data>>), aceite dos desvios (`01_Requisitos/evidencias/`).

## 5. Conclusões
- O sistema segue as fórmulas do cliente e tem autorização verificada no backend; a folha fechada é imutável também no banco.
- Os critérios de aprovação do PGQ são atendidos quanto à cobertura e a defeitos críticos e altos. Faltam, para fechar: reexecução da suíte, os 3 casos manuais e o Termo de Homologação com a decisão da equipe e do cliente.
- Riscos remanescentes: BUG004 a BUG006, SQLite com poucas escritas simultâneas, sem bloqueio por tentativas de login, verificação apenas no Windows.
