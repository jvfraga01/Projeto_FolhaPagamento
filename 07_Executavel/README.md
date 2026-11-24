# 7. Executável

O sistema é Python/Flask e roda com dois cliques em `05_Codigo_Fonte/run.py` (Windows) ou com `python 05_Codigo_Fonte/run.py`. O atalho `iniciar.bat` foi retirado do projeto; por isso não há mais o aviso de "fornecedor desconhecido" do Windows.

Pacote executável separado: dispensado pelo professor em <<23/11/2026>> (evidência da Fase 1). O ZIP completo do projeto é o que se entrega e se testa.

- Primeiro acesso: matrícula 1, senha 01012000; a troca é obrigatória.
- Se o Flask não estiver instalado, o `run.py` oferece instalá-lo; a alternativa é `pip install -r 05_Codigo_Fonte/requirements.txt` (ver `05_Codigo_Fonte/INSTALACAO.md`).
- Conferência em instalação limpa: descompactar o ZIP final em pasta vazia, executar `python 05_Codigo_Fonte/run.py` e abrir http://127.0.0.1:5000. O resultado fica registrado em `09_Homologacao/Testes_de_Aceitacao.md` (linha MM01, rodada B).
- Para refazer o ZIP depois de qualquer mudança: `python verificar_entrega.py` e depois `python empacotar_entrega.py`, na raiz do projeto completo.
