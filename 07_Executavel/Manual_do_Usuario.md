# Manual do Usuário — Sistema de Folha de Pagamento

Versão do sistema: 1.3 (A3). As telas são descritas em texto.

## 1. Introdução
O sistema calcula e controla a folha de pagamento mensal de uma empresa pequena. Existem três perfis:

| Perfil | Nível | O que faz |
|---|---|---|
| Administrador/RH | 1 | Cadastra e altera colaboradores, gera a folha, lança vendas e produção, fecha o mês, redefine senhas |
| Financeiro | 2 | Consulta colaboradores, folha e relatório (não altera nada) |
| Colaborador | 3 | Consulta apenas as próprias folhas de meses fechados e seus dados |

Os três tipos de remuneração seguem as fórmulas do cliente:
- **Padrão:** salário base.
- **Comissionado:** salário base + vendas × percentual de comissão.
- **Por Produção:** salário base + quantidade produzida × valor por unidade.

Não há descontos: salário final = salário base + adicionais.

## 2. Instalação
Requisitos: Windows com Python 3.10 ou superior e um navegador atual (Chrome, Edge ou Firefox). Internet só é necessária para baixar o Python e o Flask.

1. Instale o Python em https://www.python.org/downloads/ marcando **Add Python to PATH** (ou deixe o `iniciar.bat` oferecer a instalação).
2. Na pasta `05_Codigo_Fonte`, dê dois cliques em **`iniciar.bat`**.
3. Se o Flask não estiver instalado, o sistema pergunta se pode instalar: responda `S`.
4. O navegador abre sozinho em http://127.0.0.1:5000. Para encerrar o sistema, feche a janela preta.



Comandos de terminal: `05_Codigo_Fonte/INSTALACAO.md`. O escopo verificado é o Windows; Linux e macOS são opcionais e não fazem parte da verificação.

## 3. Configuração
| Item | Como |
|---|---|
| Primeiro acesso | Matrícula `1`, senha `01012000`. O sistema obriga a trocar a senha antes de continuar |
| Senha dos demais usuários | A inicial é a data de nascimento em DDMMAAAA (ex.: 15031990). Também precisa ser trocada no primeiro login |
| Regime opcional de metas | Desligado por padrão. Só use com aceite do cliente: `set REGIME_METAS=1` antes de iniciar |
| Zerar os dados | Feche o sistema e apague a pasta `instance/`; o banco e o admin inicial são recriados |
| Backup | Copie o arquivo `instance/folha.db` |

## 4. Operação

### 4.1 Entrar e trocar a senha
1. Informe matrícula e senha e clique em **Entrar**.
2. Se a senha for a inicial, o sistema abre a tela **Alterar minha senha**. Informe a senha atual, a nova (mínimo 6 caracteres, diferente da inicial) e a confirmação.
3. Para trocar a senha depois, use o menu **Senha**. Para sair, **Sair**.

Mensagens de erro de login são genéricas ("Matrícula ou senha incorretos, ou usuário inativo").

### 4.2 Cadastrar colaborador (RH)
1. Menu **Novo colaborador**.
2. Preencha nome, nascimento, início do contrato, nível de acesso, salário base e tipo. Para Comissionado informe a comissão (%); para Por Produção, o valor por unidade.
3. **Confirmar cadastro**. A matrícula é gerada pelo sistema e a senha inicial é a data de nascimento (DDMMAAAA).

Como digitar valores: `3000,00`, `3.000,00` e `3.000` valem R$ 3.000,00. Com ponto e sem vírgula, o ponto só vale como milhar quando é seguido de exatamente 3 dígitos; `12.50` vale R$ 12,50. Formatos ambíguos como `1,500.00` são recusados. Valores negativos e texto são recusados com mensagem no campo.

### 4.3 Consultar, filtrar e alterar colaboradores
- Menu **Colaboradores** (RH e Financeiro). Filtros combináveis: nome, salário máximo, tipo e status (Ativo, Inativo, Todos).
- RH: **Alterar** edita os dados; a alteração não afeta meses já fechados. **Desabilitar** inativa o colaborador (o histórico é preservado, e ele perde o login na hora); **Reativar** devolve o acesso; **Redefinir senha** volta a senha para a data de nascimento (e exige nova troca no próximo login).
- Não é possível desabilitar a si mesmo nem remover o nível do último administrador ativo.

### 4.4 Gerar a folha do mês (RH)
1. Menu **Folha**, escolha mês e ano e clique em **Gerar / completar folha do mês**. Entram todos os colaboradores com contrato vigente no mês (inclusive os desabilitados depois). Gerar de novo só adiciona quem ainda não tem folha.
2. **Lançar vendas / produção**: informe as vendas (comissionados) e a quantidade (produção) e clique em **Salvar e recalcular**. Enquanto o mês está aberto, a folha usa o salário e os percentuais atuais do cadastro.
3. **Fechar mês**: congela os valores. **Não é possível reabrir.** O sistema pede confirmação.

Mês aberto = prévia; mês fechado = congelado.

### 4.5 Recibo individual
- Colaboradores: menu **Minhas folhas** lista apenas meses fechados; abra o **Recibo** e use **Imprimir recibo**.
- RH e Financeiro abrem o recibo de qualquer colaborador pela lista da folha (mês aberto mostra o aviso "PRÉVIA").
- O recibo mostra matrícula, nome, tipo, salário base, vendas ou produção, adicional e **líquido a receber**.

## 5. Relatórios
Menu **Relatório** (RH e Financeiro): escolha o mês e veja o total da folha, a quantidade de colaboradores, o total por categoria e o detalhamento (matrícula, nome, tipo, salário base, adicionais e salário final). **Imprimir relatório** abre a impressão sem menu nem botões. Mês aberto exibe aviso de prévia.

## 6. Tema e preferências
O botão 🌙/☀️ no menu alterna entre tema claro e escuro; a escolha fica salva no navegador.

## 7. Solução de problemas
| Sintoma | O que fazer |
|---|---|
| "python não é reconhecido" | Use `py` no lugar de `python` ou reinstale o Python marcando Add Python to PATH |
| Porta 5000 em uso | Feche o outro programa ou mude `port=5000` no fim de `run.py` |
| Acesso negado (403) | Seu nível não permite a ação. Colaboradores só veem as próprias folhas de meses fechados |
| "Token de segurança inválido" (400) | Recarregue a página e tente de novo |
| Esqueci a senha | O RH usa **Redefinir senha**; a senha volta a ser a data de nascimento e deve ser trocada |
| Usuário "inativo" | O RH precisa **Reativar** o colaborador |
| Valor gravado errado | Digite com vírgula decimal (`1500,00`) e confira o formulário antes de confirmar |
| Mês fechado por engano | Não há reabertura (regra RN012). Corrija no mês seguinte |
