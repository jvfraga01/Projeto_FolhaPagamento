# Evidência de Controle de Versão

Comprova o histórico exigido pelo PGQ (Git, ramo `main`, tags de entrega).

| Item | Valor |
|---|---|
| URL do repositório | https://github.com/jvfraga01/Projeto_FolhaPagamento |
| Ramo principal | `main` |
| Tag da entrega A1 | `v1.2-A1` |
| Tag da entrega A3 | a criar na A3 |
| Último commit de conteúdo (antes desta evidência) | `<<HASH>>` |
| Data da exportação do histórico | <<DATA>> |
| Arquivo com o log completo | `10_Qualidade/Historico_Git.txt` |

> A tag aponta para o commit final, que inclui este arquivo e o `Historico_Git.txt`. Por isso o hash acima é o do
> último commit de conteúdo, feito antes da evidência.

## Como gerar a evidência
Na raiz do repositório clonado, execute `10_Qualidade/exportar_historico_git.bat` (Windows) ou
`10_Qualidade/exportar_historico_git.sh` (Linux/macOS). Será criado o arquivo `10_Qualidade/Historico_Git.txt`
com hash, autor, data e mensagem de cada commit, além da lista de tags e do endereço do repositório remoto.

Para publicar a tag da revisão entregue:
```bash
git tag -a v1.2-A1 -m "Entrega A1 revisada"
git push origin v1.2-A1
```

## Convenção de commits
Mensagens curtas no imperativo, indicando o artefato: `docs: atualiza ERS`, `feat: modo opcional de metas`,
`test: casos de persistência`. Cada integrante deve aparecer como autor dos commits do que produziu.
