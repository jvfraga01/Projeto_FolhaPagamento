# Evidência de Controle de Versão

Comprova o histórico exigido pelo PGQ (Git, ramo `main`, tags de entrega).

| Item | Valor |
|---|---|
| URL do repositório | **<<PREENCHER: https://github.com/USUARIO/Projeto_FolhaPagamento>>** |
| Ramo principal | `main` |
| Tag da entrega A1 | `v1.2-A1` (criar/atualizar para a revisão entregue; ver abaixo) |
| Tag da entrega A3 | `v-A3` (A3) |
| Commit da revisão entregue | **<<PREENCHER: hash curto do commit>>** |
| Data da exportação | **<<PREENCHER>>** |

## Como gerar a evidência
Na raiz do repositório clonado, execute `10_Qualidade/exportar_historico_git.bat` (Windows) ou
`10_Qualidade/exportar_historico_git.sh` (Linux/macOS). Será criado o arquivo `10_Qualidade/Historico_Git.txt`
com hash, autor, data e mensagem de cada commit, além da lista de tags e do endereço do repositório remoto.
Anexe esse arquivo à entrega e preencha a tabela acima.

Para publicar a tag da revisão entregue:
```bash
git tag -a v1.2-A1 -m "Entrega A1 revisada"
git push origin main --tags
```

## Convenção de commits
Mensagens curtas no imperativo, indicando o artefato: `docs: atualiza ERS`, `feat: modo opcional de metas`,
`test: casos de persistência`. Cada integrante deve aparecer como autor dos commits do que produziu.
