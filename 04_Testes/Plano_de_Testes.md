# 7. Plano de Testes

## Escopo
**Será testado:** cadastro e manutenção de colaboradores, filtros, cálculo de remuneração (3 tipos, pelas fórmulas do cliente; metas como modo opcional), geração/lançamento/fechamento da folha, relatórios, autenticação, autorização por nível, validações (RN001–RN007) e segurança básica (CSRF, XSS, vazamento de hash).
**Não será testado:** desempenho com grande volume, compatibilidade com navegadores antigos, itens fora do escopo do Documento de Visão.

## Estratégia
Testes automatizados para regras e rotas, mais roteiro manual para itens visuais (impressão, aparência).

| Nível | Objetivo | Alvo | Técnica |
|---|---|---|---|
| Unitário | Validar cada regra isolada | `regras.py` (cálculo, metas, dinheiro) | `unittest`, sem banco |
| Integração | Validar rotas + banco juntos | Fluxos: cadastro → folha → fechamento, permissões, filtros | Flask test client + SQLite temporário |
| Sistema | Validar o sistema completo | Instalação, login e uso pelas telas | Execução manual guiada |
| Aceitação | Confirmar que atende o cliente | Critérios de aceitação da ERS | Roteiro com o responsável pelo projeto |

Técnicas: caixa-preta (partição de equivalência e valores-limite, por exemplo vendas = meta, meta − 1 centavo, percentual no teto de 10%) e caixa-branca (cobertura de desvios das rotas).

## Ambiente
| Item | Descrição |
|---|---|
| SO | Windows 10/11 e Ubuntu 22.04 |
| Banco | SQLite 3 (arquivo temporário nos testes automatizados) |
| Framework | Python 3.12, Flask 3.1, Werkzeug |
| Navegador (manual) | Chrome ou Edge atual |
| Dados de teste | Administrador inicial e colaboradores criados pelos próprios testes em diretório temporário (massa padrão descrita em `Casos_de_Teste.md`) |
| Modo de cálculo | Padrão: fórmulas do cliente. Modo com metas (opcional): variável `REGIME_METAS=1`, usado só nos casos CT035 e CT045 |

## Ferramentas
`unittest` (execução), Flask test client (requisições), `coverage.py` (cobertura), Git (versionamento), planilha/tabela do Registro de Defeitos.

Comandos:
```bash
python -m unittest discover -v
python -m coverage run -m unittest discover
python -m coverage report -m
```

## Critérios de Entrada
- Requisitos (ERS) aprovados e casos de teste escritos.
- Sistema compila/inicia sem erro e banco criado.
- Ambiente de teste disponível.

## Critérios de Saída
Os critérios são avaliados **por ciclo**, para não misturar o que é da A1 com o que está reservado à A3.

| Ciclo | Critério de saída |
|---|---|
| **A1 (planejamento + automação inicial)** | Plano e 45 casos escritos com massa de dados e resultado esperado; casos marcados "Auto" implementados e aprovados na suíte; casos manuais com roteiro definido e marcados "execução planejada"; nenhum defeito crítico ou alto conhecido. |
| **A3 (execução final)** | Todos os casos executados (automáticos e manuais), com resultado obtido, data e responsável registrados; cobertura ≥ 80% medida com `coverage.py`; Registro de Defeitos e Relatório de Testes atualizados; nenhum defeito crítico ou alto aberto; ≥ 95% dos casos aprovados. |

## Conformidade com o cliente
Testes verdes comprovam o sistema apenas contra os critérios escritos. Para comprovar aderência ao cliente:
- o cálculo padrão é verificado contra os **exemplos do documento do cliente** (CT016, CT017, CT019: comissão = vendas × percentual; produção = quantidade × valor unitário);
- o modo com metas (CT035, CT045) é **opcional** e seu resultado só vale como conforme após o aceite do desvio D1 em `01_Requisitos/Registro_de_Aceite_de_Desvios.md`;
- (D1 a D6) têm aceito registrado (29 e 30/10/2026); Teste aprovado + desvio aceito = "validado pelo cliente".

## Roteiro de Usabilidade (RNF001, CT039)
**Participantes:** 3 pessoas que não participaram do desenvolvimento (uma por perfil: RH, Financeiro, Colaborador). **Ambiente:** Chrome ou Edge, sistema recém-instalado, massa de dados padrão. **Facilitador:** analista de testes (QA), que observa sem ajudar.

| Tarefa | Perfil | Resultado esperado | Medida |
|---|---|---|---|
| T1. Entrar no sistema e trocar a própria senha | Todos | Senha trocada sem consultar o manual | Tempo ≤ 2 min; ≤ 1 erro |
| T2. Cadastrar um colaborador Comissionado | RH | Colaborador aparece na lista com matrícula | Tempo ≤ 3 min; ≤ 2 erros |
| T3. Gerar a folha do mês, lançar vendas e consultar o resumo | RH | Resumo mostra total, quantidade e total por categoria | Tempo ≤ 5 min; ≤ 2 erros |
| T4. Filtrar a folha por tipo e salário máximo | Financeiro | Lista só com os registros esperados | Tempo ≤ 2 min; ≤ 1 erro |
| T5. Abrir e imprimir o próprio recibo de mês fechado | Colaborador | Pré-visualização limpa, sem menu | Tempo ≤ 2 min; ≤ 1 erro |

**Critério de aprovação:** pelo menos 4 das 5 tarefas concluídas sem ajuda por todos os participantes aplicáveis, e nota média ≥ 4 em "foi fácil de usar" (escala 1 a 5). **Registro:** tabela com participante, tarefa, tempo, erros, comentários e data. Execução planejada para a A3.

## Verificação de Persistência (RNF003, CT040)
1. Automático: `PersistenciaTest` grava um colaborador, descarta a aplicação, recria a aplicação sobre o mesmo arquivo e confirma que o registro (salário 1.234,56) permanece.
2. Manual (A3): iniciar com `iniciar.bat`, cadastrar um colaborador, fechar a janela, iniciar de novo e consultar a lista; o colaborador deve continuar lá, assim como a folha fechada.

## Critérios de Aprovação
Ver PGQ: ≥ 95% dos casos aprovados, 0 defeitos críticos e 100% dos requisitos atendidos.

## Situação atual (30/10/2026)
- Suíte automatizada com **44 testes**, todos aprovados na execução de 30/10/2026 (reexecutar e registrar data a cada entrega).
- Dos 45 casos, **os marcados "Auto" estão automatizados**; os marcados "Manual (planejado)" (CT009, CT012, CT023, CT029-M, CT030, CT037, CT039, CT043, CT044) **ainda não foram executados**.
- Cobertura ainda não medida (meta de 80% para a A3).
- Aceite do cliente para os desvios D1 a D6: registrado em 29 e 30/10/2026 (ver Registro de Aceite).

## Responsabilidades e riscos
Responsável pela execução: Analista de testes (QA). Riscos: desvios D1–D6 com aceite registrado em 29 e 30/10/2026; ver `03_Projeto/Planejamento_do_Projeto.md`.

