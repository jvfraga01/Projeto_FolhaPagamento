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

Técnicas: caixa-preta (partição de equivalência e valores-limite, por exemplo vendas = meta, meta − 1 centavo, percentual no teto de 10% (somente no modo opcional de metas)) e caixa-branca (cobertura de desvios das rotas).

## Ambiente
| Item | Descrição |
|---|---|
| SO | Windows 10/11 (Linux e macOS fora do escopo de verificação) |
| Banco | SQLite 3 (arquivo temporário nos testes automatizados) |
| Framework | Python 3.10+ (verificado com 3.13.3), Flask 3.1, Werkzeug |
| Navegador (manual) | Chrome ou Edge atual |
| Dados de teste | Administrador inicial e colaboradores criados pelos próprios testes em diretório temporário (massa padrão descrita em `Casos_de_Teste.md`) |
| Modo de cálculo | Padrão: fórmulas do cliente. Modo com metas (opcional): variável `REGIME_METAS=1`, usado só nos casos CT035 e CT045 |

## Ferramentas
`unittest` (execução), Flask test client (requisições), `coverage.py` (cobertura), Git (versionamento), planilha/tabela do Registro de Defeitos.

Comandos:
```bash
python -m unittest discover -v
python -m coverage run --source=app -m unittest discover
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
| **A1 (planejamento + automação inicial)** | Plano e casos escritos (45 na A1; 58 na A3) com massa de dados e resultado esperado; casos marcados "Auto" implementados e aprovados na suíte; casos manuais com roteiro definido e marcados "execução planejada"; nenhum defeito crítico ou alto conhecido. |
| **A3 (execução final)** | Todos os casos executados (automáticos e manuais), com resultado obtido, data e responsável registrados; cobertura ≥ 80% medida com `coverage.py`; Registro de Defeitos e Relatório de Testes atualizados; nenhum defeito crítico ou alto aberto; ≥ 95% dos casos aprovados. |

## Conformidade com o cliente
Testes verdes comprovam o sistema apenas contra os critérios escritos. Para comprovar aderência ao cliente:
- o cálculo padrão é verificado contra os **exemplos do documento do cliente** (CT016, CT017, CT019: comissão = vendas × percentual; produção = quantidade × valor unitário);
- o modo com metas (CT035, CT045) é **opcional** e seu resultado só vale como conforme após o aceite do desvio D1 em `01_Requisitos/Registro_de_Aceite_de_Desvios.md`;
- (D1 a D6) têm aceito registrado (29 e 30/10/2026); Teste aprovado + desvio aceito = "validado pelo cliente".

## Roteiro de Usabilidade (RNF001, CT039)
**Participantes:** 2 pessoas que não programaram as telas (colegas, familiares ou outros alunos): uma com conta **RH** (T1 a T5) e outra com conta **Financeiro** (T1, T4 e T5: o perfil só consulta, então T2 e T3 não se aplicam a ela). As tarefas T1 e T5 do perfil **Colaborador** (nível 3) são verificadas na rodada do CT037-M com uma conta nível 3. **Ambiente:** Chrome ou Edge, sistema recém-instalado, massa de dados padrão. **Facilitador:** analista de testes (QA), que observa sem ajudar (na aplicação de 11/11/2026, o facilitador foi Luiggi Bortolini).

| Tarefa | Perfil | Resultado esperado | Medida |
|---|---|---|---|
| T1. Entrar no sistema e trocar a própria senha | Todos | Senha trocada sem consultar o manual | Tempo ≤ 2 min; ≤ 1 erro |
| T2. Cadastrar um colaborador Comissionado | RH | Colaborador aparece na lista com matrícula | Tempo ≤ 3 min; ≤ 2 erros |
| T3. Gerar a folha do mês, lançar vendas e consultar o resumo | RH | Resumo mostra total, quantidade e total por categoria | Tempo ≤ 5 min; ≤ 2 erros |
| T4. Filtrar a folha por tipo e salário máximo | RH ou Financeiro | Lista só com os registros esperados | Tempo ≤ 2 min; ≤ 1 erro |
| T5. Abrir e imprimir o próprio recibo de mês fechado | Todos | Pré-visualização limpa, sem menu | Tempo ≤ 2 min; ≤ 1 erro |

**Critério de aprovação:** todas as tarefas aplicáveis ao perfil de cada participante (RH: T1 a T5; Financeiro: T1, T4 e T5) concluídas sem ajuda, dentro dos limites de tempo e de erros, e nota média ≥ 4 em "foi fácil de usar" (escala 1 a 5). **Registro:** tabela com participante, perfil, conta usada em cada tarefa, tempo, erros, comentários e data. Resultado registrado em `09_Homologacao/Testes_de_Aceitacao.md`, linha MM02.

## Verificação de Persistência (RNF003, CT040)
1. Automático: `PersistenciaTest` grava um colaborador, descarta a aplicação, recria a aplicação sobre o mesmo arquivo e confirma que o registro (salário 1.234,56) permanece.
2. Manual: faz parte do CT037-M, executado com o pacote `07_Executavel/Projeto_FolhaPagamento_Executavel.zip` (iniciar o atalho, trocar a senha, cadastrar, fechar a janela, reabrir e consultar o mesmo cadastro); resultado e capturas em `09_Homologacao/Testes_de_Aceitacao.md`, linhas MM01 e MM01-B.

## Critérios de Aprovação
Ver PGQ: ≥ 95% dos casos aprovados, 0 defeitos críticos e 100% dos requisitos atendidos.

## Situação atual
- Suíte automatizada: <!--A:testes-->74<!--/A--> testes na última execução (<!--A:resultado-->OK, nenhum teste falhou<!--/A-->, <!--A:data-->12/11/2026 19:30<!--/A-->, <!--A:ambiente-->3.13.3 / Windows-11-10.0.26200-SP0<!--/A-->) e cobertura de <!--A:cobertura-->92%<!--/A--> sobre `app/`. Detalhes: `04_Testes/Relatorio_de_Testes.md`.
- Dos 58 casos, **os marcados "Auto" estão automatizados**. O CT039 (roteiro de usabilidade) foi aplicado em 11/11/2026 (linha MM02 em `09_Homologacao/Testes_de_Aceitacao.md`) e fica **parcial** até registrar a conta usada por P2 em T2 e T3 e a rodada do perfil Colaborador. O CT037-M tem a rodada 1 parcial (MM01) e a rodada com o pacote final (MM01-B) ainda por executar. O CT043 (cobertura) e o CT044 (Windows) são executados por `gerar_cobertura.py`.
- Casos por tipo, aprovados e requisitos atendidos: `10_Qualidade/Metricas_e_Indicadores.md` (calculado das evidências).
- Aceite do cliente para os desvios D1 a D6: registrado em 29 e 30/10/2026 (ver Registro de Aceite).

## Responsabilidades e riscos
Responsável pela execução: Analista de testes (QA). Riscos: desvios D1–D6 com aceite registrado em 29 e 30/10/2026; ver `03_Projeto/Planejamento_do_Projeto.md`.

