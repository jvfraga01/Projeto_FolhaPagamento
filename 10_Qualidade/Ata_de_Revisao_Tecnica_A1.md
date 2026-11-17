# Ata de Revisão Técnica

Registro exigido pelo PGQ (seção "Revisões Técnicas"). Revisão realizada em 10/11/2026 sobre os artefatos da A1 e o estado do sistema para a A3. As respostas do checklist foram redigidas a partir das evidências do repositório; **a equipe deve confirmar antes de assinar**.

| Campo | Valor |
|---|---|
| Projeto | Sistema de Folha de Pagamento (Grupo 10) |
| Entrega | A1 (revisada) e preparação da A3 |
| Data da revisão | 10/11/2026 |
| Participantes | João Vitor Fraga da Rocha; <<PREENCHER: demais participantes da revisão>> |
| Itens revisados | ERS e matriz; casos de uso e sequências; plano e casos de teste; `regras.py`, `folha.py`, `auth.py`; testes automatizados; resultados da execução de 10/11/2026 |
| Versão/commit revisado | <<PREENCHER: hash curto do commit>> |

## Checklist do PGQ
| Pergunta | Resposta | Observação |
|---|---|---|
| Atende ao requisito? | Parcial | Fórmulas do T1 cobertas por testes (CT015–CT019). Defeitos BUG004–BUG006 seguem abertos. |
| Segue o padrão de código? | Não verificado com ferramenta | PEP 8 conferido por leitura; o flake8 previsto no PGQ ainda não foi executado. |
| Valida entradas? | Sim | CT004–CT007, CT042, CT046, CT047; BUG001 (ponto de milhar) corrigido. |
| Checa permissão no backend? | Sim | CT024–CT026, CT025 e demais testes de `PermissaoTest`. |
| Tem teste? | Sim | 61 testes OK e 92,2% de cobertura em 10/11/2026; 70 testes no código após as correções. |
| Documentação atualizada? | Parcial | Manuais e relatórios criados em 10/11/2026; campos `<<PREENCHER>>` pendentes. |
| Sem dados sensíveis no código? | Parcial | Banco e `secret.key` fora do Git pelo `.gitignore`; no histórico, `instance/` chegou a ser commitado (commit a2d6225): <<PREENCHER: conferir se havia secret.key>>. |

## Itens encontrados e ações
| # | Item | Autor | Revisor | Ação | Responsável | Prazo | Situação |
|---|---|---|---|---|---|---|---|
| 1 | BUG001: "1.500" gravado como R$ 1,50 | <<PREENCHER>> | <<PREENCHER>> | Corrigir `_decimal` e testar (CT046, CT047) | <<PREENCHER>> | <<PREENCHER>> | Corrigido |
| 2 | BUG002: credencial do admin exibida no login | <<PREENCHER>> | <<PREENCHER>> | Forçar a troca da senha inicial (RF021, CT052, CT053) | <<PREENCHER>> | <<PREENCHER>> | Corrigido, aguardando reexecução |
| 3 | BUG003: banco permitia reabrir mês e inserir folha em mês fechado | <<PREENCHER>> | <<PREENCHER>> | Triggers em `schema.sql` (CT048) | <<PREENCHER>> | <<PREENCHER>> | Corrigido |
| 4 | Critério de usabilidade divergente entre ERS e Plano | <<PREENCHER>> | <<PREENCHER>> | Unificar no critério do Plano | <<PREENCHER>> | <<PREENCHER>> | Corrigido |
| 5 | Nome da tag A3 divergente (`v-A3` contra "a criar") | <<PREENCHER>> | <<PREENCHER>> | Unificar em `v-A3`, a criar na entrega final | <<PREENCHER>> | <<PREENCHER>> | Corrigido nos documentos |
| 6 | BUG004, BUG005, BUG006 (média e baixa) | <<PREENCHER>> | <<PREENCHER>> | Decidir correção ou ressalva | <<PREENCHER>> | <<PREENCHER>> | Aberto |
