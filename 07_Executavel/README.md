# 7. Executável

O sistema é Python/Flask e roda com dois cliques em `05_Codigo_Fonte/iniciar.bat` (Windows).

-- Dispensado pelo professor em <<23/11/2026>> (evidência da Fase 1); o sistema roda com python 05_Codigo_Fonte/run.py

- `Projeto_FolhaPagamento_Executavel.zip`: pacote pronto para uso (código, `iniciar.bat`, `INSTALACAO.md`, manuais e `LEIA-ME`), **sem** banco, chave secreta nem arquivos temporários. Gerado por `empacotar_entrega.py`.
- O atalho se chama `iniciar.bat` em todos os pacotes. Na primeira abertura o Windows pode avisar "fornecedor desconhecido" (o arquivo não tem assinatura digital): clique em **Executar**. Se o navegador de e-mail ou o antivírus bloquear o `.bat`, rode `python run.py` na pasta `05_Codigo_Fonte`, que faz o mesmo.
- Uso: descompactar em qualquer pasta e dar dois cliques em `iniciar.bat` (o sistema oferece instalar o Python e o Flask, se faltarem). Primeiro acesso: matrícula 1, senha 01012000; a troca é obrigatória.
- Para refazer o pacote depois de qualquer mudança no código: `python verificar_entrega.py` e depois `python empacotar_entrega.py`, **na raiz do projeto completo** (repositório ou ZIP completo). Esses dois scripts não vão dentro deste pacote, porque ele só tem código, banco, manuais e instalação.
- Conferência em instalação limpa (feita antes da entrega): descompactar este ZIP em pasta vazia, `pip install -r 05_Codigo_Fonte/requirements.txt`, `python 05_Codigo_Fonte/run.py` e abrir http://127.0.0.1:5000. O resultado fica registrado em `09_Homologacao/Testes_de_Aceitacao.md` (MM01-B).
