---
name: meta-varredura-low-ticket
description: Meta Ad Library sweep by generic low-ticket terms (2026-10-07/08). Method, extractor and the winners found
metadata:
  type: project
---

On 2026-10-07 the user asked to sweep the Meta Ad Library with generic low-ticket terms (format + offer language) to see what really sells. Cutoff set by the user: ad active ≥30 days AND many creatives (≥3 per advertiser).

**Files:**
- Report: /Users/vitorhugo/Desktop/ofertas/1-BR/pesquisas/meta-low-ticket-2026-10-07/RELATORIO.md
- Raw data: resultados.txt
- Extractor: extrator.js

**How the extractor works:**
- Runs in the built-in browser via javascript_tool.
- The tab is hidden, so infinite scroll doesn't fire. It clicks the "Ver mais" button up to 14 times, giving about 150 ads per term.
- It uses exact-phrase search.
- An info-product filter (checkout/landing domain, or digital words in the text) drops shops.

**Facebook blocks:**
- localStorage keys get wiped.
- fetch to 127.0.0.1 is blocked by CSP.
- So paste the script on every call.

**What finds info products:** format terms find them ("modelos prontos", "projetos prontos", "atividades prontas", "planilhas prontas", "apostila"). Price terms only return e-commerce.

**Winners:**
- Dentista docs 216d x10.
- Altas Habilidades protocol 108d x15.
- Psicomotricista docs 97d x10.
- Autism activities 171d.
- TDAH 77d.
- NR-1 43d.
- Cartonagem projetos 84d x28.
- +5.000 moldes 151d.
- Caseirinhos 127d x80.
- Docinhos 33d x36.

Related: [[offer-selection-framework]], [[foco-profissionais]].

**Deep run 2026-10-08 (robo_meta.py, Playwright headless, no login):**
- **Scale:** 120 terms, ~22k ads, 748 candidates.
- **Real scale signal:** the per-advertiser page (`view_all_page_id`) shows "~N resultados", the total active ads.
- **Page id:** read from the React fiber prop adCardFragment.page_id. The profile id in the card link does NOT work.
- **Blocks:** Facebook IP-blocks anonymous heavy use. The block came after ~20 min at full speed, then lasted 3h+ the second time.
- **Pacing that works:** 45–75 s between terms, 25–45 s between advertisers, 15 clicks per term. Stop retrying for hours when blocked; religar.sh restarts the robot.
- **Results:** OFERTAS-ESCALADAS-POR-NICHO.md
- **Top professional signals:**
  - HOF document kits: 82 / 62 / 18 ads, up to 545d.
  - Odontologia docs: 32 ads, 218d.
  - Psicólogo prontuário CRP: 43 ads, 290d.
  - Psicopedagogia avaliação (Clubinho): 89 ads.
  - AEE autism activities: 210 ads.
  - Psicomotricidade: 28 ads.
  - Arquiteto docs: 430d.
  - Perito médico laudos.
  - EngBox.
  - Avaliação física: 68 ads.

**Next step decided 2026-10-08:**
- The robot was stopped at the user's request after repeated blocks. About 90 advertisers had been checked, so roughly 660 candidates remain unchecked. Progress is saved in the robot's own files.
- The plan is to build our own low-ticket "spy" platform on **SearchAPI** (Meta Ad Library engine).
  - Pricing: US$40/mo for 10k credits, 1 credit per call (~25 ads per call).
  - Signals used: total_results = active ads on the page; collation_count = how many copies a creative has (the scale signal).
  - Media links on Facebook's servers expire, so creatives must be downloaded right away.
- Planned usage, about 8.1k credits/mo: top 150 checked daily, about 450 checked weekly, 50 discovery terms a week. The low-ticket filter (≤R$97, price read from the checkout or sales page) runs locally.
- Backup option: ScrapeCreators, US$47 for 25k credits that don't expire.
- Waiting on the user to create the free SearchAPI account (100 searches) and send the API key. I must never create the account myself.
- Never use proxy rotation or fake accounts to evade Facebook's blocks.
