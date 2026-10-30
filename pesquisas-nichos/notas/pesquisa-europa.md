---
name: pesquisa-europa
description: 28/10 Europe research (PT, ES, IT, FR, DE) for euro offers: top 10 per country, where the files are, the winners, and the method lessons (SearchAPI instead of the browser)
metadata:
  type: project
---

On 2026-10-28 the user asked to find gaps in European countries to sell in euro. They wanted more than professions: norms with deadlines, templates and spreadsheets, and an arbitrage of the offers validated in EscalaLow, ending in a top 10 per country by niche.

**Files:** `Desktop/ofertas/3 - EU/pesquisas/brechas-europa-2026-10-28/`
- `CONSOLIDADO-V2.md` (round 2, the final one);
- `<pais>/TOP10-V2.md`;
- `arbitragem-br-eu/`;
- `profissoes-extra/`;
- `meta_busca.py` (SearchAPI with a credit cap per country);
- `escalalow-ofertas-validadas.json` (213 BR offers).

**No. 1 per country:**
- PT: Agenda Verde, recibos verdes (36).
- IT: Termometro 85k, forfettario (34). The Excel competitor charges €69.97.
- ES: opositores docentes, simulator (33).
- DE: Kita Beobachtungs-Kompass (33).
- FR: CRPE oral (31).

**Repeats across countries:**
- Sanitary inspection simulator, i.e. the Consultora translated (IT, PT, ES, FR).
- Bimby/Thermomix and air fryer recipes, plus sugar-free and anti-inflammatory recipes.
- Cognitive stimulation for the elderly (nobody native sells it).
- Children's printable activities.

**Risks:** BR sellers are already in IT (dentist and psychologist kits at €19.99, 30+ creatives), in PT (consultorioemdia.shop dentist kit, and PT-PT clones of BR offers), and in DE (Pflege at €7.90). Consumer prices in PT run €4.90–14.90. Spaniards and Germans search for templates ending in "gratis"/"kostenlos". Spain has elections on 29/11.

**Method lessons:**
- 5 agents using the Meta Ad Library in the shared built-in browser got the IP throttled after about 15–20 searches. Use SearchAPI via `meta_busca.py`, with a cap of 250 credits per country.
- In SearchAPI `/me`, `remaining_credits` = 0 is NOT the plan balance. Use monthly_allowance minus current_month_usage.
- The month's usage was 8,559 of 10,000 on 28/10; the cycle renews on 08/11.
- Etsy blocks with 403 or captcha.

User did not answer if consultorioemdia.shop is theirs. Related: [[pesquisa-es-profissoes-normas]], [[escalalow]], [[nichos-ticket-ltv]].

**29/10 psicólogo+dentista em PT/FR/ES/DE** (`3 - EU/pesquisas/psicologo-dentista-4-paises-2026-10-29.md`): nenhum país tem o sinal da Itália (BR a €19,99 há 30+ dias). ES dentista 43,7k sem vendedor (6,5); ES psicólogo 47,4k com Herramientas Terapéuticas 68d + vários BR/LATAM novos (6); PT psicólogo >26k sem vendedor (5); PT dentista 12,8k, Consultório em Dia ~2,5d (4,5, monitorar); FR e DE em espera (zero kits, softwares fortes, alemão/francês).
