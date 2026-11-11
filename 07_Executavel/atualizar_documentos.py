"""Atualiza os documentos (.md) com os números REAIS da última execução, sem edição manual.

Lê 04_Testes/evidencias/ (gerado por gerar_cobertura.py) e os registros do projeto, e reescreve:
  - marcadores em linha   <!--A:chave-->valor<!--/A-->        (testes, resultado, cobertura, stmts, miss, data, executor, ambiente)
  - blocos                <!--AUTO:nome-->...<!--/AUTO-->     (tabela_cobertura, metricas)
Uso:  python atualizar_documentos.py      (o gerar_cobertura.py já chama este script ao terminar)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
EVID = RAIZ / "04_Testes" / "evidencias"
CASOS = RAIZ / "04_Testes" / "Casos_de_Teste.md"
ACEITE = RAIZ / "09_Homologacao" / "Testes_de_Aceitacao.md"
ERS = RAIZ / "01_Requisitos" / "ERS.md"
DEFEITOS = RAIZ / "10_Qualidade" / "Registro_de_Defeitos.md"


def ler(p):
    return Path(p).read_text(encoding="utf-8")


def virgula(x):
    return str(x).replace(".", ",")


def linhas_tabela(texto, prefixo):
    return [[c.strip() for c in l.strip().strip("|").split("|")] for l in texto.splitlines()
            if l.startswith(prefixo)]


def evidencias():
    saida = ler(EVID / "saida_unittest.txt")
    m = re.search(r"Ran (\d+) tests?", saida)
    fim = [l for l in saida.strip().splitlines() if l.strip()][-1]
    cob = ler(EVID / "cobertura.txt").splitlines()
    arquivos = []
    total = None
    for l in cob:
        m2 = re.match(r"^(\S+)\s+(\d+)\s+(\d+)\s+([\d.]+)%\s*(.*)$", l)
        if m2 and m2.group(1) != "TOTAL":
            arquivos.append(m2.groups())
        elif l.startswith("TOTAL"):
            m3 = re.match(r"^TOTAL\s+(\d+)\s+(\d+)\s+([\d.]+)%", l)
            total = m3.groups()
    resumo = ler(EVID / "resumo_execucao.txt")
    campo = lambda r: (re.search(r, resumo) or [None, "não identificado"])[1].strip()
    return {
        "testes": m.group(1) if m else "?", "ok": fim.strip() == "OK",
        "resultado": "OK, nenhum teste falhou" if fim.strip() == "OK" else fim.strip(),
        "stmts": total[0], "miss": total[1], "cobertura": virgula(total[2]) + "%",
        "data": campo(r"Execução em:\s*(.+)"),
        "ambiente": campo(r"Python:\s*(.+)").replace(" | Sistema: ", " / "),
        "executor": campo(r"Executor:\s*(.+)"), "arquivos": arquivos,
        "meta": float(total[2]) >= 80.0,
    }


def tabela_cobertura(ev):
    ls = ["| Arquivo | Linhas | Sem cobertura | Cobertura | Linhas não cobertas |", "|---|---|---|---|---|"]
    for nome, st, mi, cv, falta in ev["arquivos"]:
        ls.append(f"| `{nome.replace(chr(92), '/')}` | {st} | {mi} | {virgula(cv)}% | {falta or '—'} |")
    ls.append(f"| **Total** | **{ev['stmts']}** | **{ev['miss']}** | **{ev['cobertura']}** | |")
    return "\n".join(ls)


def metricas(ev):
    casos = linhas_tabela(ler(CASOS), "| CT")
    auto = [c for c in casos if c[5].startswith("Auto")]
    manual = [c for c in casos if c[5].startswith("Manual")]
    man_res = [r for r in linhas_tabela(ler(ACEITE), "| MM")]
    man_ok = [r for r in man_res if len(r) > 5 and r[5].startswith("Aprovado")]
    man_exec = [r for r in man_res if len(r) > 5 and r[5].startswith(("Aprovado", "Reprovado"))]
    auto_ok = len(auto) if ev["ok"] else 0
    executados = len(auto) + len(man_exec)
    aprovados = auto_ok + len(man_ok)
    # requisitos: RF/RN definidos na ERS; atendido = coberto por caso Auto aprovado ou manual aprovado
    ers = ler(ERS)
    ids = sorted({r[0] for r in linhas_tabela(ers, "| RF0") + linhas_tabela(ers, "| RN0")
                  if re.fullmatch(r"R[FN]\d{3}", r[0])})
    ok_codes = {c[0] for c in auto} if ev["ok"] else set()
    ok_codes |= {r[1] for r in man_ok}
    cobertos = {i for c in casos if c[0] in ok_codes for i in re.findall(r"R[FN]\d{3}", c[1])}
    faltam = [i for i in ids if i not in cobertos]
    d = [r for r in linhas_tabela(ler(DEFEITOS), "| BUG")]
    corr = [r for r in d if r[4].split()[0] in ("Corrigido", "Homologado", "Fechado")]
    abertos = [r for r in d if r not in corr and not r[4].startswith("Não procede")]
    graves = [r[0] for r in abertos if r[2] in ("Crítica", "Alta")]
    pct = lambda a, b: virgula(f"{100 * a / b:.1f}") + "%" if b else "—"
    codigos = {c[0].split("-")[0] for c in casos}
    out = [
        "| Métrica (PGQ) | Meta | Resultado | Como foi calculado |", "|---|---|---|---|",
        f"| Cobertura de testes | ≥ 80% | **{ev['cobertura']}** ({'meta atingida' if ev['meta'] else 'ABAIXO DA META'}) | `coverage report`, {ev['stmts']} linhas, {ev['miss']} sem cobertura ({ev['data']}) |",
        f"| Testes automatizados | — | **{ev['testes']}** executados: {ev['resultado']} | `evidencias/saida_unittest.txt` |",
        f"| Casos de teste planejados | — | **{len(codigos)}** códigos em {len(casos)} linhas | `Casos_de_Teste.md` ({len(auto)} Auto, {len(manual)} Manual) |",
        f"| Casos executados | — | **{executados}** de {len(casos)} linhas | Auto executados na suíte + manuais com resultado em `Testes_de_Aceitacao.md` |",
        f"| Casos aprovados ÷ executados | ≥ 95% | **{pct(aprovados, executados)}** ({aprovados}/{executados}) | Auto aprovados (suíte OK) + manuais aprovados |",
        f"| Requisitos atendidos | 100% | **{pct(len(ids) - len(faltam), len(ids))}** ({len(ids) - len(faltam)}/{len(ids)} RF e RN) | RF/RN com ao menos um caso aprovado; sem caso aprovado: {', '.join(faltam) or 'nenhum'} |",
        f"| Defeitos encontrados | acompanhar | **{len(d)}** | `Registro_de_Defeitos.md` |",
        f"| Defeitos corrigidos | 100% dos críticos e altos | **{len(corr)}** de {len(d)} | críticos/altos abertos: {', '.join(graves) or 'nenhum'} |",
        f"| Densidade de defeitos | acompanhar | **{virgula(f'{len(d) / max(len(ids), 1):.2f}')}** defeitos por requisito | defeitos ÷ {len(ids)} RF/RN |",
        "", "```mermaid", "pie title Situação dos casos de teste",
        f'    "Aprovados" : {aprovados}', f'    "Reprovados" : {executados - aprovados}',
        f'    "Não executados" : {len(casos) - executados}', "```",
    ]
    return "\n".join(out)


def aplicar(ev):
    blocos = {"tabela_cobertura": tabela_cobertura(ev), "metricas": metricas(ev)}
    simples = {k: ev[k] for k in ("testes", "resultado", "cobertura", "stmts", "miss", "data", "executor", "ambiente")}
    alterados = 0
    for p in sorted(RAIZ.rglob("*.md")):
        if any(x in p.parts for x in ("evidencias", ".git", "instance", "htmlcov")):
            continue
        t = ler(p)
        n = t
        for k, v in simples.items():
            n = re.sub(rf"(<!--A:{k}-->).*?(<!--/A-->)", lambda m: m.group(1) + v + m.group(2), n)
        for k, v in blocos.items():
            n = re.sub(rf"(<!--AUTO:{k}-->).*?(<!--/AUTO-->)", lambda m: m.group(1) + "\n" + v + "\n" + m.group(2), n, flags=re.S)
        if n != t:
            p.write_bytes(n.encode("utf-8"))
            alterados += 1
            print(f"[atualizado] {p.relative_to(RAIZ)}")
    print(f"{alterados} arquivo(s) atualizado(s) com a execução de {ev['data']} ({ev['testes']} testes, {ev['cobertura']}).")


if __name__ == "__main__":
    aplicar(evidencias())
