"""Busca na Biblioteca de Anúncios via SearchAPI com TETO de créditos por país (1 crédito por chamada).
Uso: python3 meta_busca.py <PAIS> "<termo>" [paginas=1]
Imprime: total de anúncios ativos e anunciantes com ≥30 dias e ≥3 criativos (dias | criativos | página | link | texto).
Salva tudo em <pais>/dados/meta_api.jsonl. NÃO use o navegador na Biblioteca de Anúncios (bloqueia o IP)."""
import json, sys, os, datetime, urllib.parse, urllib.request
TETO = 250
PAIS = {"PT": "portugal", "ES": "espanha", "IT": "italia", "FR": "franca", "DE": "alemanha"}
c, termo = sys.argv[1].upper(), sys.argv[2]; pags = int(sys.argv[3]) if len(sys.argv) > 3 else 1
base = os.path.dirname(os.path.abspath(__file__)); pasta = os.path.join(base, PAIS[c], "dados"); os.makedirs(pasta, exist_ok=True)
cont = os.path.join(pasta, "creditos_usados.txt"); usados = int(open(cont).read()) if os.path.exists(cont) else 0
if usados + pags > TETO: sys.exit(f"TETO de {TETO} créditos atingido ({usados} usados). Pare de buscar no Meta.")
K = open("/Users/vitorhugo/Desktop/ofertas/1-BR/escalalow/.chave").read().strip()
H = datetime.datetime.now(datetime.timezone.utc); ads, tok, total = [], None, None
for _ in range(pags):
    p = dict(engine="meta_ad_library", active_status="active", search_type="keyword_exact_phrase", q=termo, country=c, api_key=K)
    if tok: p["next_page_token"] = tok
    d = json.loads(urllib.request.urlopen("https://www.searchapi.io/api/v1/search?" + urllib.parse.urlencode(p), timeout=60).read())
    usados += 1; total = total or d.get("search_information", {}).get("total_results"); ads += d.get("ads", [])
    tok = (d.get("pagination") or {}).get("next_page_token")
    if not tok: break
open(cont, "w").write(str(usados))
pg = {}
for a in ads:
    if not a.get("start_date"): continue
    dias = (H - datetime.datetime.fromisoformat(a["start_date"].replace("Z", "+00:00"))).days; s = a.get("snapshot") or {}
    o = pg.setdefault(a["page_id"], {"page": a.get("page_name", ""), "page_id": a["page_id"], "dias": 0, "n": 0, "link": "", "txt": ""})
    o["n"] += a.get("collation_count") or 1
    if dias > o["dias"]: o.update(dias=dias, link=s.get("link_url") or "", txt=((s.get("body") or {}).get("text") or s.get("title") or "")[:200].replace("\n", " "))
bons = sorted([o for o in pg.values() if o["dias"] >= 30 and o["n"] >= 3], key=lambda o: -o["dias"])
with open(os.path.join(pasta, "meta_api.jsonl"), "a") as f: f.write(json.dumps({"termo": termo, "total": total, "lidos": len(ads), "anunciantes": list(pg.values())}, ensure_ascii=False) + "\n")
print(f"[{c}] \"{termo}\": {total} anúncios ativos | lidos {len(ads)} | {len(bons)} anunciantes ≥30d/≥3cr | créditos usados {usados}/{TETO}")
for o in bons[:10]: print(f"  {o['dias']}d {o['n']}cr | {o['page'][:40]} | {o['link'][:60]} | {o['txt'][:110]}")
