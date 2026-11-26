# 7. Executável


Dispensado pelo professor em 23/11/2026 (evidência: `09_Homologacao/evidencias/resposta_professor_23-11-2026.jpeg`; registro em `01_Requisitos/Registro_de_Aceite_de_Desvios.md`).

O sistema é Python/Flask e roda com `python 05_Codigo_Fonte/run.py` (ou dois cliques em `run.py`). Primeiro acesso: matrícula 1, senha 01012000; a troca é obrigatória.
O teste do sistema aberto a partir do ZIP do projeto, em pasta limpa, está registrado em `09_Homologacao/Testes_de_Aceitacao.md` (MM01-B).

- `Projeto_FolhaPagamento_Executavel.zip`: pacote pronto para uso (código, `INSTALACAO.md`, manuais e `LEIA-ME`), **sem** banco, chave secreta nem arquivos temporários. Gerado por `empacotar_entrega.py`.
- O atalho se chama `run.py` em todos os pacotes.clique com o botão direito do mouse vá em abrir com e escolha python, rode `python run.py` na pasta `05_Codigo_Fonte`, que faz o mesmo.
- Uso: descompactar em qualquer pasta e dar clicar com o botão direito do mouse vá em abrir com e escolha python. (o sistema oferece instalar o Python e o Flask, se faltarem). Primeiro acesso: matrícula 1, senha 01012000; a troca é obrigatória.
- Para refazer o pacote depois de qualquer mudança no código: `python verificar_entrega.py` e depois `python empacotar_entrega.py`, **na raiz do projeto completo** (repositório ou ZIP completo). Esses dois scripts não vão dentro deste pacote, porque ele só tem código, banco, manuais e instalação.
- Conferência em instalação limpa (feita antes da entrega): descompactar este ZIP em pasta vazia, `pip install -r 05_Codigo_Fonte/requirements.txt`, `python 05_Codigo_Fonte/run.py` e abrir http://127.0.0.1:5000. O resultado fica registrado em `09_Homologacao/Testes_de_Aceitacao.md` (MM01-B).

