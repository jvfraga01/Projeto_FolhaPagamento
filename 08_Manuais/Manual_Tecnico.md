# Manual Técnico — Sistema de Folha de Pagamento

Base: `03_Projeto/Documento_de_Arquitetura.md`, `05_Codigo_Fonte/INSTALACAO.md` e o código-fonte.

## 1. Arquitetura
Aplicação web monolítica em camadas, com páginas renderizadas no servidor (Flask + Jinja2) e banco SQLite.

| Camada | Responsabilidade | Arquivos |
|---|---|---|
| Interface | Telas, formulários, tema claro/escuro, impressão | `app/templates/`, `app/static/` |
| Rotas / Controle | Receber requisições, autorizar por nível, validar, orquestrar | `app/auth.py`, `app/colaboradores.py`, `app/folha.py`, `app/__init__.py` |
| Negócio | Cálculo, metas, conversão de dinheiro, validações puras | `app/regras.py` |
| Persistência | Conexão e esquema | `app/db.py`, `app/schema.sql` |

Decisões principais: regras isoladas em módulo puro (testáveis sem banco), cálculo por estratégias registradas em `CALCULADORES`, dinheiro em centavos inteiros, autorização no backend e folha mensal como "fotografia".

## 2. Modelo de dados
Três tabelas (`schema.sql`; cópia em `06_Banco_Dados/schema.sql`).

| Tabela | Conteúdo |
|---|---|
| `colaborador` | Pessoa e login: matrícula (PK, autoincremento), nome, datas, nível (1–3), status (Ativo/Inativo), `senha_hash`, tipo, salário e parâmetros (`percentual_comissao_bp`, `valor_unidade_centavos`) |
| `periodo` | Mês da folha (`ano`, `mes`, `status` ABERTO/FECHADO), único por (ano, mês) |
| `folha` | Uma linha por colaborador e mês, com os valores daquele momento; único por (período, matrícula); `total = salário base + adicionais` |

Convenções: dinheiro em centavos (inteiro); percentuais em pontos-base (5,50% = 550). `CHECK` impede valores negativos.

Triggers (imutabilidade de mês fechado, mesmo por acesso direto ao banco): `folha_fechada_no_update`, `folha_fechada_no_delete`, `folha_fechada_no_insert`, `periodo_fechado_no_update` (impede reabrir) e `periodo_fechado_no_delete`. O fechamento ABERTO→FECHADO é permitido.

## 3. Estrutura do código
```
05_Codigo_Fonte/
├── run.py, iniciar.bat, iniciar.sh        inicialização
├── gerar_cobertura.py / .bat / .sh        testes + cobertura + evidências
├── .coveragerc, requirements*.txt         configuração e dependências
├── app/
│   ├── __init__.py       fábrica do app, sessão, CSRF, CSP, troca obrigatória de senha, filtros, erros
│   ├── auth.py           login, logout, troca de senha, decorators de permissão
│   ├── colaboradores.py  cadastro, alteração, status, redefinição de senha, meus dados
│   ├── folha.py          geração, lançamentos, fechamento, recibo, relatório
│   ├── regras.py         dinheiro, metas e cálculo
│   ├── db.py, schema.sql
│   └── templates/, static/
└── tests/  test_sistema.py, test_correcoes_a3.py
```

Rotas principais: `/login`, `/logout`, `/senha`, `/colaboradores` (+ `/novo`, `/<matricula>/editar|desabilitar|reativar|redefinir-senha`), `/meus-dados`, `/folha` (+ `/gerar`, `/<id>`, `/<periodo>/lancamentos`, `/<periodo>/fechar`), `/minha-folha`, `/relatorio`.

## 4. Segurança
| Controle | Implementação |
|---|---|
| Autorização | `@nivel_exigido(...)` e `@login_obrigatorio`; o nível 3 só acessa a própria folha de mês fechado (matrícula sempre da sessão) |
| Sessão | Cookie HttpOnly, SameSite=Lax, 8 h; usuário revalidado a cada requisição (desabilitado perde o acesso) |
| CSRF | Token em todo POST (`validar_csrf`) |
| Saída | Jinja2 com escape automático; CSP `default-src 'self'` |
| Senhas | Hash scrypt (Werkzeug); senha inicial = data de nascimento, **troca obrigatória no primeiro login** (RF021): a sessão recebe `trocar_senha` e `exigir_troca_de_senha` só libera `/senha`, `/logout` e arquivos estáticos |
| SQL | Sempre parametrizado (`?`) |
| Login | Mensagem genérica; tempo constante com hash falso; a tela não exibe credenciais |

## 5. Dependências
| Item | Versão |
|---|---|
| Python | 3.10 ou superior (verificado no Windows 11 com 3.13.3) |
| Flask | 3.1.3 ou superior (`requirements.txt`) |
| coverage | 7.0 ou superior, só para medir cobertura (`requirements-dev.txt`) |
| SQLite | Embutido no Python |

## 6. Build, execução e deploy
Não há build. Execução local: `python run.py` (ou `iniciar.bat`), em http://127.0.0.1:5000. Deploy = copiar a pasta `05_Codigo_Fonte` para a máquina e iniciar. `SECRET_KEY` pode ser definida no ambiente; se ausente, é gerada em `instance/secret.key`. `REGIME_METAS=1` liga o modo opcional de metas.

## 7. Testes e cobertura
```bash
cd 05_Codigo_Fonte
python -m unittest discover -v
python gerar_cobertura.py          # roda tudo com cobertura e salva em 04_Testes/evidencias/
```
Última medição: <!--A:testes-->70<!--/A--> testes, <!--A:resultado-->OK, nenhum teste falhou<!--/A-->, cobertura <!--A:cobertura-->92,3%<!--/A--> sobre `app/` (<!--A:data-->11/11/2026 07:32<!--/A-->). Detalhes: `04_Testes/Relatorio_de_Testes.md`.

## 8. Manutenção
| Tarefa | Como |
|---|---|
| Novo tipo de remuneração | Escrever a função em `regras.py`, registrar em `CALCULADORES`, incluir o tipo em `schema.sql` (`CHECK` de `tipo`) e em `TIPOS`; criar testes |
| Mudar parâmetros de metas | Constantes no topo de `regras.py` (modo opcional) |
| Backup/restauração | Copiar `instance/folha.db` |
| Alterar o esquema | Editar `schema.sql` e `06_Banco_Dados/schema.sql` juntos (devem ser idênticos). `CREATE ... IF NOT EXISTS` não altera bancos já criados |
| Regra de mudança | Mudança de regra de negócio em relação ao cliente só entra como padrão com aceite registrado (PGQ) |

## 9. Limitações conhecidas
SQLite com poucas escritas simultâneas; sem cálculo proporcional (pró-rata); sem bloqueio por tentativas de login; verificação apenas no Windows; defeitos conhecidos e suas soluções em `10_Qualidade/Registro_de_Defeitos.md`.
