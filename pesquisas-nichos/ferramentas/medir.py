# Arbitragem BR→EU (28/10/2026): tipos de produto validados no Brasil (EscalaLow, ≥60d/≥15 ativos) medidos em 5 países.
# 1 página (até 30 anúncios) por termo, frase exata, só ativos. Saída: total de anúncios e anunciantes ≥30d com ≥3 criativos.
import json, time, urllib.parse, urllib.request, datetime, os
K = open("/Users/vitorhugo/Desktop/ofertas/1-BR/escalalow/.chave").read().strip()
HOJE = datetime.datetime(2026, 10, 28, tzinfo=datetime.timezone.utc)
C = {  # conceito: {país: termo}
 "moldes de costura": {"PT": "moldes de costura", "ES": "patrones de costura", "IT": "cartamodelli", "FR": "patrons de couture", "DE": "Schnittmuster"},
 "crochê": {"PT": "croché", "ES": "ganchillo", "IT": "uncinetto", "FR": "crochet", "DE": "Häkelanleitung"},
 "macramê": {"PT": "macramé", "ES": "macramé", "IT": "macramè", "FR": "macramé", "DE": "Makramee"},
 "cartonagem": {"PT": "cartonagem", "ES": "cartonaje", "IT": "cartonaggio", "FR": "cartonnage", "DE": "Kartonage"},
 "projetos marcenaria": {"PT": "projetos de carpintaria", "ES": "planos de carpintería", "IT": "progetti in legno", "FR": "plans de menuiserie", "DE": "Bauanleitung"},
 "plantas de casa": {"PT": "plantas de casas", "ES": "planos de casas", "IT": "progetti di case", "FR": "plans de maison", "DE": "Hauspläne"},
 "atividades p/ imprimir": {"PT": "atividades para imprimir", "ES": "actividades para imprimir", "IT": "attività da stampare", "FR": "activités à imprimer", "DE": "Arbeitsblätter"},
 "alfabetização": {"PT": "aprender a ler", "ES": "lectoescritura", "IT": "imparare a leggere", "FR": "apprendre à lire", "DE": "Lesen lernen"},
 "estimulação cognitiva": {"PT": "estimulação cognitiva", "ES": "estimulación cognitiva", "IT": "stimolazione cognitiva", "FR": "stimulation cognitive", "DE": "Gedächtnistraining"},
 "TDAH": {"PT": "PHDA", "ES": "TDAH", "IT": "ADHD", "FR": "TDAH", "DE": "ADHS"},
 "receitas sem glúten": {"PT": "receitas sem glúten", "ES": "recetas sin gluten", "IT": "ricette senza glutine", "FR": "recettes sans gluten", "DE": "glutenfreie Rezepte"},
 "receitas p/ diabéticos": {"PT": "receitas para diabéticos", "ES": "recetas para diabéticos", "IT": "ricette per diabetici", "FR": "recettes pour diabétiques", "DE": "Rezepte für Diabetiker"},
 "air fryer": {"PT": "receitas air fryer", "ES": "recetas air fryer", "IT": "ricette friggitrice ad aria", "FR": "recettes airfryer", "DE": "Airfryer Rezepte"},
 "marmitas/meal prep": {"PT": "marmitas", "ES": "batch cooking", "IT": "meal prep", "FR": "batch cooking", "DE": "Meal Prep"},
 "cosmético natural": {"PT": "cosmética natural", "ES": "cosmética natural", "IT": "cosmetici naturali", "FR": "cosmétiques maison", "DE": "Naturkosmetik"},
 "radiestesia": {"PT": "radiestesia", "ES": "radiestesia", "IT": "radiestesia", "FR": "radiesthésie", "DE": "Radiästhesie"},
 "orações": {"PT": "orações", "ES": "oraciones", "IT": "preghiere", "FR": "prières", "DE": "Gebete"},
 "inglês": {"PT": "aprender inglês", "ES": "aprender inglés", "IT": "imparare l'inglese", "FR": "apprendre l'anglais", "DE": "Englisch lernen"},
 "pão/salgados p/ vender": {"PT": "para vender", "ES": "para vender", "IT": "da vendere", "FR": "à vendre", "DE": "zum Verkaufen"},
 "musicalização infantil": {"PT": "música para bebés", "ES": "estimulación temprana", "IT": "Montessori", "FR": "Montessori", "DE": "Montessori"},
 "planner/organização": {"PT": "planner", "ES": "planner", "IT": "planner", "FR": "planner", "DE": "Planner"},
 "receitas fitness": {"PT": "receitas fit", "ES": "recetas fit", "IT": "ricette light", "FR": "recettes healthy", "DE": "Abnehmen Rezepte"},
}
def call(**p):
    p.update(engine="meta_ad_library", active_status="active", api_key=K, search_type="keyword_exact_phrase")
    return json.loads(urllib.request.urlopen("https://www.searchapi.io/api/v1/search?" + urllib.parse.urlencode(p), timeout=60).read())
out = {}
for conc, pt in C.items():
    for c, t in pt.items():
        try: d = call(q=t, country=c)
        except Exception as e: print("ERRO", c, t, e, flush=True); continue
        pg = {}
        for a in d.get("ads", []):
            if not a.get("start_date"): continue
            dias = (HOJE - datetime.datetime.fromisoformat(a["start_date"].replace("Z", "+00:00"))).days
            s = a.get("snapshot") or {}
            o = pg.setdefault(a["page_id"], {"page": a.get("page_name", ""), "dias": 0, "n": 0, "link": "", "txt": ""})
            o["n"] += a.get("collation_count") or 1
            if dias > o["dias"]:
                o["dias"] = dias; o["link"] = s.get("link_url") or ""
                o["txt"] = ((s.get("body") or {}).get("text") or s.get("title") or "")[:140].replace("\n", " ")
        bons = sorted([o for o in pg.values() if o["dias"] >= 30 and o["n"] >= 3], key=lambda o: -o["dias"])
        out[f"{conc}|{c}"] = {"termo": t, "total": d.get("search_information", {}).get("total_results"), "anunciantes": len(pg), "bons": bons}
        time.sleep(0.4)
    print(conc, " ".join(f"{c}:{out.get(f'{conc}|{c}',{}).get('total')}/{len(out.get(f'{conc}|{c}',{}).get('bons',[]))}" for c in pt), flush=True)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resultado.json"), "w"), ensure_ascii=False, indent=1)
