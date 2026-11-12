# Ata de Revisão Técnica

Registro exigido pelo PGQ (seção "Revisões Técnicas"). Revisão realizada em 10/11/2026, com complemento em 11/11/2026, sobre os artefatos da A1 e o estado do sistema para a A3. As respostas do checklist foram conferidas contra as evidências do repositório (`04_Testes/evidencias/`).

| Campo | Valor |
|---|---|
| Projeto | Sistema de Folha de Pagamento (Grupo 10) |
| Entrega | A1 (revisada) e preparação da A3 |
| Data da revisão | 10/11/2026 (complemento em 11/11/2026) |
| Participantes | João Vitor Fraga da Rocha, Luiggi Bortollini, Yuri Soares Dutra, Pedro da Silva Kolling|
| Itens revisados | ERS e matriz; casos de uso e sequências; plano e casos de teste; `regras.py`, `folha.py`, `auth.py`; testes automatizados; resultados da execução de 10/11/2026 |
| Versão/commit revisado | ffb2753 |

## Checklist do PGQ
| Pergunta | Resposta | Observação |
|---|---|---|
| Atende ao requisito? | Sim | Fórmulas do T1 cobertas por testes (CT015–CT019); defeitos em `Registro_de_Defeitos.md` corrigidos ou justificados. |
| Segue o padrão de código? | Não verificado com ferramenta | PEP 8 conferido por leitura; o flake8 previsto no PGQ ainda não foi executado. |
| Valida entradas? | Sim | CT004–CT007, CT042, CT046, CT047; BUG001 (ponto de milhar) corrigido. |
| Checa permissão no backend? | Sim | CT024–CT026, CT025 e demais testes de `PermissaoTest`. |
| Tem teste? | Sim | <!--A:testes-->70<!--/A--> testes, <!--A:resultado-->OK, nenhum teste falhou<!--/A-->, cobertura <!--A:cobertura-->92,3%<!--/A--> (<!--A:data-->11/11/2026 07:32<!--/A-->). |
| Documentação atualizada? | Sim | Manuais, relatórios, métricas e registros criados; números atualizados automaticamente das evidências. |
| Sem dados sensíveis no código? | Sim, com conferência pendente | Banco e `secret.key` fora do Git pelo `.gitignore` e do pacote (`empacotar_entrega.py`). No histórico, `instance/` foi commitado e apagado (commit a2d6225): conferir com `git show --stat a2d6225` se havia `secret.key` (BUG008). |

## Itens encontrados e ações
| # | Item | Autor | Revisor | Ação | Responsável | Prazo | Situação |
|---|---|---|---|---|---|---|---|
| 1 | BUG001 e BUG007: valores com ponto de milhar | João Vitor Fraga | Avaliador A3 | Corrigir `_decimal` e testar (CT046, CT047) | João Vitor Fraga | 11/11/2026 | Corrigido |
| 2 | BUG002: credencial do admin no login | João Vitor Fraga | Avaliador A3 | Forçar a troca da senha inicial (RF021) | João Vitor Fraga | 11/11/2026 | Corrigido |
| 3 | BUG003: banco aceitava reabrir mês e inserir folha | João Vitor Fraga | Avaliador A3 | Triggers em `schema.sql` (CT048) | João Vitor Fraga | 11/11/2026 | Corrigido |
| 4 | BUG004 a BUG006 | João Vitor Fraga | Avaliador A3 | Corrigir ou justificar (CT056, CT057) | João Vitor Fraga | 11/11/2026 | Corrigidos ou não procede |
| 5 | BUG008: pacote com `secret.key` e banco | João Vitor Fraga | Avaliador A3 | `empacotar_entrega.py` | João Vitor Fraga | 11/11/2026 | Corrigido |
| 6 | Critério de usabilidade, tag, duplicados e versão | Equipe | Avaliador A3 | Unificar (tag `v1.3-A3`, versão 1.3, critério do Plano) | Equipe | 11/11/2026 | Corrigido |
