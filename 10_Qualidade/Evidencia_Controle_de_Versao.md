# Evidência de Controle de Versão

Comprova o histórico exigido pelo PGQ (Git, ramo `main`, tags de entrega).

| Item | Valor |
|---|---|
| URL do repositório | https://github.com/jvfraga01/Projeto_FolhaPagamento |
| Ramo principal | `main` |
| Tag da entrega A1 | `v1.2-A1` |
| Tag da entrega A3 | `v1.3-A3` |
| Commit da tag A3 | <<PREENCHER: saída de `git rev-list -n 1 v1.3-A3`, hash curto>> |
| Último commit de conteúdo (antes desta evidência) | <<PREENCHER: hash curto do último commit de conteúdo>> |
| Data da exportação do histórico | 24/11/2026 |
| Arquivo com o log completo | `10_Qualidade/Historico_Git.md` |

> A tag `v1.3-A3` aponta para o último commit de conteúdo; esta evidência é commitada logo depois.

## Como gerar a evidência
Na raiz do repositório clonado, execute `python 10_Qualidade/exportar_historico_git.py`.
Será criado o arquivo `10_Qualidade/Historico_Git.md`
com hash, autor, data e mensagem de cada commit, além da lista de tags e do endereço do repositório remoto.

## Convenção de commits
Mensagens curtas no imperativo, indicando o artefato: `docs: atualiza ERS`, `feat: modo opcional de metas`,
`test: casos de persistência`. Cada integrante deve aparecer como autor dos commits do que produziu.
