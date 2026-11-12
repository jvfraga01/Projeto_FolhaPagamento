# Roteiro de Apresentação e Demonstração (15 minutos)

Papéis conforme `03_Projeto/Planejamento_do_Projeto.md`. Antes de começar: apagar `05_Codigo_Fonte/instance/`, abrir `iniciar.bat`, deixar o navegador em http://127.0.0.1:5000 e ter este roteiro e `Apresentacao.pptx` abertos.

| Tempo | Parte | Quem (papel) | O que mostrar |
|---|---|---|---|
| 0:00–2:00 | Problema, escopo e requisitos do cliente (slides 1–3) | Gerente / analista de requisitos | Fórmulas do T1; perfis; desvios D1–D6 aceitos |
| 2:00–4:00 | Arquitetura e decisões (slides 4–5) | Arquiteto / desenvolvedor | Camadas, `regras.py` puro, centavos, triggers no banco |
| 4:00–10:00 | **Demonstração** (abaixo) | Arquiteto / desenvolvedor | Sistema rodando |
| 10:00–13:00 | Qualidade: testes, cobertura, defeitos, métricas (slides 6–8) | Analista de testes (QA) | `Relatorio_de_Testes.md`, `Metricas_e_Indicadores.md`, `Registro_de_Defeitos.md` |
| 13:00–15:00 | Homologação e conclusão (slides 9–10) | Documentação / homologação | Termo de Homologação, pendências, lições aprendidas |

## Passo a passo da demonstração (6 minutos)
1. **Primeiro acesso e troca obrigatória (1 min):** entrar com matrícula `1`, senha `01012000`. A tela de login não mostra credenciais. O sistema leva à troca de senha; tentar abrir "Colaboradores" antes de trocar mostra o bloqueio. Trocar a senha.
2. **Cadastro (1 min):** Novo colaborador, tipo Comissionado, salário `3.000,00`, comissão `3,00`. Mostrar matrícula gerada. Tentar salário `abc`: erro no campo e nada gravado. Mostrar que `1.500` vale R$ 1.500,00.
3. **Folha (2 min):** Folha → gerar o mês → Lançar vendas `5.000,00` → conferir R$ 3.150,00 → Fechar mês (confirmação; não reabre).
4. **Relatório e recibo (1 min):** Relatório com total, quantidade e total por categoria. Abrir um recibo e **Imprimir**: na pré-visualização, menu e botões somem (CT030).
5. **Controle de acesso (1 min):** entrar como colaborador nível 3 (senha inicial DDMMAAAA, trocar). Ele só vê "Minhas folhas" de meses fechados; digitar na URL `/colaboradores` mostra 403 sem dados.

## Plano B
Se o navegador ou o sistema falhar, mostrar a execução de `python gerar_cobertura.py` e `04_Testes/evidencias/` (testes e cobertura) e o capítulo de casos CT052, CT053 e CT048 em `Casos_de_Teste.md`.

## Antes do dia
Rodar `python gerar_cobertura.py`, conferir os números nos slides 6 a 8 com `Relatorio_de_Testes.md` e `Registro_de_Defeitos.md`, e rodar `python empacotar_entrega.py`.
