# 2. Especificação de Requisitos de Software (ERS)

## Introdução
 Objetivo:  especificar os requisitos do Sistema de Folha de Pagamento.
 Escopo:  conforme o Documento de Visão.
 Fontes:  Requisitos do Cliente (RF001–RF009, RN001–RN008, RNF001–RNF004), sistema anterior e decisões do responsável pelo projeto (RF010 em diante). Os desvios em relação ao cliente estão listados abaixo e controlados em `01_Requisitos/Registro_de_Aceite_de_Desvios.md`.

 Definições e siglas 
| Termo | Significado |
|---|---|
| RF / RN / RNF | Requisito funcional / Regra de negócio / Requisito não funcional |
| Período | Mês/ano de uma folha (ABERTO ou FECHADO) |
| Meta | Valor mínimo de vendas (R$) ou produção (un) do mês para ter direito ao adicional |
| Adicional | Comissão (comissionado) ou produtividade (produção) somada ao salário base |
| Nível 1/2/3 | Perfis Administrador-RH / Financeiro / Colaborador |
| Exclusão lógica | Mudar o status para Inativo, sem apagar o registro |

## Requisitos Funcionais
| ID | Descrição | Origem |
|---|---|---|
| RF001 | Cadastrar colaborador com matrícula (gerada pelo sistema), nome, salário base, tipo, data de nascimento e datas de contrato. | Cliente |
| RF002 | Cadastrar colaborador  Padrão  (recebe apenas o salário base). | Cliente |
| RF003 | Cadastrar colaborador  Comissionado  informando o percentual de comissão; as vendas são lançadas por mês (RF015). | Cliente |
| RF004 | Cadastrar colaborador  por Produção  informando o valor por unidade; a quantidade é lançada por mês (RF015). | Cliente |
| RF005 | Consultar a lista de colaboradores com dados cadastrais e remuneratórios. | Cliente |
| RF006 | Calcular automaticamente o salário final conforme o tipo de remuneração, usando exatamente as fórmulas do cliente (RN008). | Cliente |
| RF007 | Gerar a folha (matrícula, nome, tipo, salário final) de todos os colaboradores do mês. | Cliente |
| RF008 | Emitir o resumo da folha: custo total, quantidade de colaboradores e total por categoria. | Cliente |
| RF009 | Manter cadastros: incluir, alterar, consultar e remover (a remoção é  lógica , ver RF013). | Cliente |
| RF010 | Autenticar por matrícula e senha; encerrar sessão (logout). Existe um administrador inicial criado com o banco. | Responsável |
| RF011 | Permitir que o usuário altere a própria senha. O RH pode redefinir a senha de outro usuário para a senha inicial. | Responsável |
| RF012 | Controlar o acesso por nível (1, 2 e 3)  no backend , inclusive por URL direta. | Responsável |
| RF013 | Desabilitar e reativar colaborador, preservando todo o histórico. | Responsável |
| RF014 | Gerar a folha de um mês (período), incluindo quem tinha contrato no mês, mesmo que hoje esteja desabilitado. | Responsável |
| RF015 | Lançar as vendas (R$) e a produção (un) do mês e recalcular a folha aberta. | Responsável |
| RF016 | Fechar o mês, congelando os valores calculados (sem reabertura). | Responsável |
| RF017 | Consultar as próprias folhas (meses fechados) e emitir/imprimir o recibo individual. | Responsável |
| RF018 | Filtrar colaboradores (nome, salário máximo, tipo, status) e folha (nome, salário máximo, tipo), de forma combinada. | Responsável |
| RF019 | **(Opcional, desativado por padrão)** Calcular metas mensais progressivas (RN009 a RN011), somente quando o modo com metas for ativado (`REGIME_METAS=1`) e aceito pelo cliente. | Responsável |
| RF020 | Imprimir o relatório consolidado e o recibo. | Cliente (relatórios) |

## Regras de Negócio
| ID | Descrição | Origem |
|---|---|---|
| RN001 | Toda matrícula é única (gerada automaticamente pelo sistema). | Cliente |
| RN002 | O nome do colaborador é obrigatório. | Cliente |
| RN003 | O salário base não pode ser negativo. | Cliente |
| RN004 | O valor de vendas não pode ser negativo. | Cliente |
| RN005 | O percentual de comissão não pode ser negativo. | Cliente |
| RN006 | A quantidade produzida não pode ser negativa. | Cliente |
| RN007 | O valor por unidade produzida não pode ser negativo. | Cliente |
| RN008 | O salário final é calculado automaticamente pelo sistema, **sem meta, progressão, bônus ou teto**: Padrão = salário base; Comissionado = salário base + (vendas × percentual de comissão); Por Produção = salário base + (quantidade produzida × valor por unidade). | Cliente |
| RN009 | **[Opcional – modo com metas]** Se a meta do mês não for atingida, o adicional é R$ 0,00 (o salário base é mantido). | Responsável |
| RN010 | **[Opcional – modo com metas]** Meta atingida: comissão = vendas × percentual; o percentual sobe 1 ponto a cada R$ 2.000,00 vendidos acima da meta, até o teto de 10%. Produção: unidades × valor da unidade, com bônus de 1% a cada 50 un acima da meta, até 10%. | Responsável / equipe* |
| RN011 | **[Opcional – modo com metas]** Meta mínima de vendas R$ 5.000,00 (produção: 100 un). A meta do mês seguinte sobe um passo (R$ 2.000,00 / 50 un) se a anterior foi batida; senão repete. Meta de folha já gerada não muda. | Responsável / equipe |
| RN012 | Folha de mês fechado é imutável (inclusive no banco) e não pode ser reaberta. | Responsável |
| RN013 | Existe uma única folha por colaborador por mês. | Responsável |
| RN014 | Entram na folha do mês os colaboradores com contrato vigente naquele mês. | Responsável |
| RN015 | O nível 3 só acessa as próprias folhas e somente de meses fechados. | Responsável |
| RN016 | Colaboradores nunca são excluídos fisicamente. | Responsável |
| RN017 | Senhas são guardadas com hash; a senha inicial é a data de nascimento em DDMMAAAA. | Responsável |
| RN018 | Não há descontos: salário final = salário base + adicionais. | Responsável |

## Requisitos Não Funcionais
| ID | Descrição | Origem |
|---|---|---|
| RNF001 | Interface amigável e intuitiva (menu por perfil, tema claro/escuro). | Cliente |
| RNF002 | Validar os dados de entrada antes de qualquer cálculo. | Cliente |
| RNF003 | Armazenar os registros de forma persistente (SQLite). | Cliente |
| RNF004 | Permitir novos tipos de remuneração sem alterar os cálculos existentes (calculadores registrados em `CALCULADORES`). | Cliente |
| RNF005 | Segurança: hash de senha, proteção CSRF, escape de saída (XSS), cabeçalho CSP, cookie HttpOnly/SameSite, SQL parametrizado. | Responsável |
| RNF006 | Instalação e uso simples: iniciar com dois cliques; banco e administrador criados automaticamente. | Responsável |
| RNF007 | Precisão monetária: valores em centavos inteiros, arredondamento meio-para-cima. | Equipe |
| RNF008 | Testabilidade: regras de negócio isoladas em módulo puro; cobertura de testes ≥ 80%. | PGQ |
| RNF009 | Portabilidade: Windows, Linux e macOS com Python 3.10+. | Equipe |

## Desvios em relação ao documento do cliente (para validação)
Situação possível: **Resolvido** (comportamento do cliente preservado), **Pendente de aceite** (implementado, mas sem registro de aprovação). O registro de aprovação de cada item fica em `01_Requisitos/Registro_de_Aceite_de_Desvios.md`.

| ID | Desvio | Tratamento adotado | Situação |
|---|---|---|---|
| D1 | Metas, progressão, bônus e teto de comissão (RN009–RN011) alteram as fórmulas do cliente. | O cálculo **padrão** segue exatamente as fórmulas do cliente (RN008). O regime de metas virou modalidade **opcional**, desligada por padrão (`REGIME_METAS=1` para ligar) e só deve ser usada após aceite. | **Resolvido** (padrão = cliente); regime opcional Aceito em 30/10/2026 |
| D2 | Vendas e produção lançadas por mês (RF015) em vez de informadas só no cadastro (RF003/RF004). | Cadastro guarda percentual e valor por unidade; o total do mês é lançado na folha. | Aceito em 29/10/2026 |
| D3 | Remoção lógica no lugar de exclusão física (RF009 → RF013, RN016). | Colaborador fica Inativo; histórico preservado; some da lista padrão e da folha de meses sem contrato. | Aceito em 29/10/2026 |
| D4 | Folha mensal apenas de quem tem contrato no mês (RF007 → RN014). | Filtro por datas de contrato. | Aceito em 29/10/2026 |
| D5 | Matrícula gerada automaticamente (RF001, RN001). O cliente exige matrícula no cadastro, sem definir o mecanismo. | Sequencial gerada pelo banco (`AUTOINCREMENT`). | Aceito em 29/10/2026 |
| D6 | Funções extras: login, perfis, competência mensal, fechamento, recibo (RF010–RF012, RF014, RF016–RF018). | Ampliação de escopo; não altera as fórmulas do cliente. | Aceito em 30/10/2026 |

> Enquanto um desvio estiver "Pendente de aceite", o requisito conta como **implementado**, mas não como **validado pelo cliente**.

## Critérios de Aceitação
| Requisito | Critério |
|---|---|
| RF001–RF004 | Cadastrar os três tipos; matrícula gerada e exibida na lista; campos obrigatórios validados. |
| RF005, RF018 | Lista exibe nome, tipo, salário e status; filtros combinados retornam somente o esperado. |
| RF006, RN008 | Padrão: 3.000,00 → 3.000,00. Comissionado (3%), base 3.000,00: vendas 5.000,00 → total 3.150,00; vendas 4.999,99 → adicional 150,00 (arredondado) e total 3.150,00; percentual cadastrado de 15% é aplicado sem teto. Produção, base 1.000,00 e valor 2,50: 99 un → adicional 247,50 e total 1.247,50; 100 un → 250,00; 200 un → 500,00 (sem bônus). |
| RF019 (opcional) | Só com `REGIME_METAS=1`: vendas abaixo da meta → adicional 0,00; percentual sobe 1 ponto a cada R$ 2.000,00 acima da meta e nunca passa de 10%; produção abaixo de 100 un → 0,00. Validado pelo cliente somente após o aceite de D1. |
| RF007, RF014 | Folha do mês lista todos com contrato vigente e o total confere com a soma dos salários finais. |
| RF008, RF020 | Resumo mostra total, quantidade e total por categoria; relatório pode ser impresso. |
| RF009, RF013 | Alterar atualiza o cadastro sem afetar meses fechados; desabilitar impede login e mantém o histórico; reativar devolve o acesso. |
| RF010, RF011 | Login com credenciais válidas entra; inválidas são recusadas; troca de senha exige a senha atual. |
| RF012, RN015 | Nível 3 recebe 403 (sem dados) ao acessar a folha de outro ou áreas de gestão; Financeiro não altera nada. |
| RF015, RF016, RN012 | Lançamentos recalculam a folha aberta; após fechar, qualquer alteração é recusada (aplicação e banco). |
| RN001–RN007 | Valores inválidos ou negativos são recusados com mensagem. |
| RNF001 | Roteiro de usabilidade (CT039): as 5 tarefas são concluídas sem ajuda, com 0 erros de navegação em pelo menos 4 das 5. |
| RNF002 | Dado inválido (nome vazio, valor negativo, texto no lugar de número) é recusado antes de qualquer cálculo ou gravação (CT042). |
| RNF003 | Dados cadastrados continuam disponíveis após encerrar e reabrir o sistema (CT040). |
| RNF004 | Um novo calculador pode ser incluído sem modificar os existentes: adicional fixo de R$ 100,00 sobre base de R$ 1.000,00 resulta em R$ 1.100,00 e os 3 tipos existentes mantêm os resultados (CT031). |
| RNF007 | 1.000,50 × 3% = 30,02 (meio para cima); valores guardados em centavos inteiros (CT041). |

## Matriz de Rastreabilidade
Casos de uso (UC) em `02_Analise/Casos_de_Uso.md`; casos de teste (CT) em `04_Testes/Casos_de_Teste.md`.
**Status técnico:** Implementado = existe no sistema. **Aceite do cliente:** Validado / Pendente (ver `Registro_de_Aceite_de_Desvios.md`). Requisitos "Cliente" sem desvio dependem apenas da homologação final (A3).

| Requisito             | Caso de Uso   | Classe / Módulo                   | Caso de Teste                 | Status        | Aceite do cliente |
|---|---|---|---|---|---|
| RF001, RF002          | UC001         | Colaborador (`colaboradores.py`)  | CT001, CT004, CT005, CT008, CT038 | Implementado | Matrícula automática: pendente (D5) |
| RF003                 | UC001         | Colaborador, CalculoComissionado  | CT002                         | Implementado  | Lançamento mensal: pendente (D2) |
| RF004                 | UC001         | Colaborador, CalculoProducao      | CT003                         | Implementado  | Lançamento mensal: pendente (D2) |
| RF005, RF018          | UC002         | Colaborador (lista/filtros)       | CT009, CT010, CT011           | Implementado  | Homologação A3 |
| RF006, RN008          | UC003         | `regras.py` (calculadores)        | CT015–CT019                   | Implementado  | Fórmulas = cliente; homologação A3 |
| RF019, RN009–RN011    | UC003         | `regras.py` (modo com metas)      | CT035, CT045                  | Implementado (opcional) | Pendente (D1) |
| RF007, RF014, RN014   | UC003         | Folha, Periodo (`folha.py`)       | CT020, CT034                  | Implementado  | Pendente (D4) |
| RF008, RF020          | UC004         | Folha (relatório)                 | CT021, CT030                  | Implementado  | Homologação A3 |
| RF009, RN016          | UC005         | Colaborador                       | CT012                         | Implementado  | Exclusão lógica: pendente (D3) |
| RF013                 | UC006         | Colaborador                       | CT013, CT014, CT036           | Implementado  | Pendente (D3) |
| RF010                 | UC008         | Autenticação (`auth.py`)          | CT022, CT037                  | Implementado  | Pendente (D6) |
| RF011                 | UC007, UC009  | Autenticação                      | CT023                         | Implementado  | Pendente (D6) |
| RF012, RN015          | UC008         | Autorização (`@nivel_exigido`)    | CT024, CT025, CT026           | Implementado  | Pendente (D6) |
| RF015                 | UC010         | Folha (lançamentos)               | CT006, CT007, CT020           | Implementado  | Pendente (D2) |
| RF016, RN012, RN013   | UC011         | Periodo, Folha                    | CT027, CT028                  | Implementado  | Pendente (D6) |
| RF017                 | UC012         | Folha (recibo)                    | CT029-A, CT029-M              | Implementado  | Pendente (D6) |
| RN001                 | UC001         | Banco (`AUTOINCREMENT`)           | CT008                         | Implementado  | Pendente (D5) |
| RN002–RN007           | UC001, UC010  | Validação (`regras.py`)           | CT004–CT007, CT038            | Implementado  | Homologação A3 |
| RN017, RN018          | UC008, UC003  | `auth.py`, `regras.py`            | CT001, CT015, CT022           | Implementado  | Pendente (D6) |
| RNF001                | UC001–UC012   | Interface (`templates/`)          | CT039                         | Implementado; execução planejada A3 | Homologação A3 |
| RNF002                | UC001, UC010  | Validação (`regras.py`, rotas)    | CT042, CT004–CT007            | Implementado  | Homologação A3 |
| RNF003                | todos         | `db.py`, `schema.sql` (SQLite)    | CT040                         | Implementado  | Homologação A3 |
| RNF004                | —             | `CALCULADORES`                    | CT031                         | Implementado  | Homologação A3 |
| RNF005                | UC008         | Segurança (`__init__.py`)         | CT024, CT025, CT032, CT033    | Implementado  | — (requisito da equipe) |
| RNF006                | UC008         | `iniciar.bat`, `iniciar.sh`, `db.py` | CT037                      | Implementado; execução planejada A3 | — (requisito da equipe) |
| RNF007                | UC003         | `regras.py` (centavos)            | CT041, CT016, CT019           | Implementado  | — (requisito da equipe) |
| RNF008                | —             | `regras.py` isolado; `coverage.py`| CT043                         | Estrutura pronta; medição planejada A3 | — (requisito do PGQ) |
| RNF009                | —             | Python 3.10+ / Flask              | CT044                         | Planejado A3  | — (requisito da equipe) |
