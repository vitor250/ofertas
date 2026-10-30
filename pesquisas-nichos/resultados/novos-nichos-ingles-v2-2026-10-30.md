# Novos nichos nos países de língua inglesa — v2 (30/10/2026)

Países: UK, AU, NZ, CA, IE, ZA (US como complemento).
Data de referência: 30/10/2026.

## Avisos de método
- A v1 (`3 - EU/pesquisas/novos-nichos-ingles-2026-10-29.md`) NÃO estava acessível neste ambiente (arquivo do Desktop). Usei a lista de candidatos e as lacunas citadas no prompt.
- SearchAPI indisponível (sem chave aqui e sem crédito até 08/11/2026). Medição feita com o conector Meta (`ads_library_search`, só anúncios ATIVOS): DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
- WebFetch BLOQUEADO neste container (rede só com domínios permitidos: falharam childminderresourcehut.co.uk, provider360.com.au, payhip.com e até gov.uk). Para abrir páginas de vendas e fontes oficiais, esses domínios precisam ser liberados nas configurações de rede da sessão. Preços e números oficiais abaixo vêm de resultados do WebSearch (trechos indexados) com a URL da fonte; o que não apareceu no trecho ficou VERIFICAR.
- WebSearch: a cota de buscas da sessão (200 por turno, compartilhada entre todos os agentes irmãos) ESGOTOU no meio desta pesquisa. Ficaram sem confirmação oficial nesta v2: short-lets Irlanda, nº de care agencies CQC, FHRS, CDM/RAMS, registro de childminders na Irlanda (Tusla), NZ ECE e Canadá. Esses itens estão marcados VERIFICAR (rodar de novo em outra sessão).
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende.

## Status
(em andamento)

## 1. Varredura na Biblioteca de Anúncios (por nicho e país)

Conector Meta, só anúncios ATIVOS, 30/10/2026. A busca do conector é "solta" (termos genéricos devolvem anúncios de dorama/novela); por isso usei termos técnicos de cada norma.

| Nicho | País | Termos usados | O que apareceu | Régua |
|---|---|---|---|---|
| Childminders / early years (Ofsted, EYFS) | UK | childminder Ofsted, "childminder", EYFS, early years policies, nursery policies, Ofsted ready | Childminder Resource Hut 486 d / 35 anúncios (GBP); Minding Kids 45 d (isca); clonadores novos: Florence JP (NGN, 8 d), Little Sparks (USD, 4 d), Year Sorted EYFS (1 d), Estimulación en casa (EYFS, ≤5 d) | **PROVADO + PRAZO** |
| Care agencies (CQC) | UK | CQC policies, care agency policies, domiciliary care policies | Care Daily 132 d (políticas prontas por tipo de serviço); CareDocs Direct 65 d (Fiverr $25); resto é consultoria (HQM, Compliance Supports "Save £701", Total Care Advisory) e SaaS (Health Connect £70/mês) | **PROVADO** (poucos) |
| NDIS | AU | NDIS provider templates, NDIS policies, NDIS progress notes templates, independent support worker | 78 anúncios só de serviço de registro (A$1.375–1.800+); Provider360 486 d / 59 anúncios; nenhum kit barato para os ~245 mil não registrados | PROVADO (serviço caro) / BRECHA de preço |
| Landlords (Renters' Rights Act) | UK | "Renters' Rights Act", landlord templates, landlord compliance pack, landlord document pack | 225 anúncios sobre a lei, quase todos de imobiliárias (iscas grátis) e NRLA; PDF Blueprints Store 6 d; Proper Templates UK (Etsy) 0 d | **PRAZO** + TESTE |
| Food hygiene (FHRS) | UK | "food hygiene rating", HACCP pack, "Safer Food Better Business" | Só restaurantes exibindo nota 5 e o app Leafe; OpsReady "Food Business Owners: £19.99 Pack" 3 d | TESTE |
| Short-lets | IE, UK, AU | short term letting register, Airbnb host, Airbnb host guidebook, holiday let welcome book | Nada de kit (só Lodgify e administradoras) | BRECHA sem prova de demanda |
| Tradespeople RAMS | UK | "RAMS" templates, risk assessment templates tradesmen | myramsapp 92 d (SaaS £20/mês), Safe Trade ≥69 d (SaaS), HazardCo, Style Contractor "125+ Contractor Documents" (bundle há 14 d) | PROVADO como SaaS / kit TESTE |
| Tradies SWMS (equivalente AU do RAMS) | AU, NZ | SWMS templates | **SWMS Kit 29 d, "8 electrician SWMS – A$59", gancho "SA fall rule: 2 m from 1 July 2026"**; Sync or SWMS 27 d; Site Paperwork (IA) 1 d; SiteConnect (NZ) | quase PROVADO (low ticket com preço no anúncio) |
| Early childhood (ACECQA/EYLF) | AU | EYLF templates, family day care educator, early childhood educators documentation | The Educators Domain (planners 2027) 3 d; The Grounded Educator 3 d; Estimulación en casa (EYLF) ≤5 d; OWNA (SaaS) | TESTE |
| ECE centres | NZ | learning stories ECE, ECE compliance | ECE Learning Unlimited 138 d (assinatura "70+ Policies… From $79/month", NZD+AUD); LIGHTN ECEDocs 66 d; Quliance 14 d / 17 anúncios | PROVADO (assinatura B2B) |
| Childminders / ECCE | IE | childminder, Tusla inspection, Aistear planning | Só isca de faculdade UK, MindMe.ie (marketplace) e Estimulación en casa (Aistear, <1 d) | BRECHA / TESTE |
| Dayhome / ECE | CA | dayhome provider, early childhood educator resources, home daycare forms | Só dayhomes captando famílias, prefeituras recrutando e PD (Learn Through Active Play 145 d, curso) | BRECHA sem prova |
| POPIA / ECD / CAPS | ZA | POPIA compliance templates, ECD centre registration, CAPS lesson plans | Só cursos NQF4 e TeacherMom 1 d | nada |
| Dentista (complemento) | US | Dental Kit Canva | **Lic. Zulma Laguna 29 d, 8 anúncios, 4 criativos novos em 27/10**; Dental Marketing Vault (kit de marketing $1) | quase PROVADO |
| Home daycare (complemento) | US | daycare templates | **Organized Daycare 55 d** ("Ready Before She Knocks") | PROVADO |
| Dentista CQC | UK | dental practice compliance CQC | Só SaaS ("Dentistry", demo, 50 d) e cursos de Registered Manager | BRECHA sem prova (já descartado em 29/10) |

## 2. Vendedores medidos (DIAS REAIS, nº de anúncios, moeda, página de vendas)

Medição por `page_ids` (só ATIVOS), 30/10/2026. "Dias" = idade do anúncio ativo mais antigo da página.

| Vendedor (page_id) | País/moeda | Anúncios ativos | Dias reais | Produto / sinal | Régua |
|---|---|---|---|---|---|
| Childminder Resource Hut (564585390322776) | UK / GBP | 35 | 486 (desde 01/07/2025) | Loja de recursos para childminders: "Early Years Inspection Pack", "Inspection Ready – September 2026 Action Plan & Guide", "Safe Sleep Ultimate Compliance Pack 2026", "Safeguarding Decoded A–Z", "Development Statement Bank", calendário 2027, chaveiros e itens físicos ("IN STOCK NOW", catálogo `{{product.name}}`). Alega "Trusted by 40,000+ Early Years Pros". Criativos novos em 20/10/2026. | PROVADO (forte) |
| Outstanding Childminding Resources by Minding Kids (525244184206334) | UK / GBP | 5 | 45 | Isca grátis "Safeguarding Check Chart" com versões England / Scotland / Wales (funil para loja). | PROVADO (fraco: isca) |
| Florence JP Publishing Studio (1244461232087215) | anúncio no UK, moeda NGN | 1 | 8 | "OFSTED Registration Bundle for Childminders/Nannies" (operador nigeriano). | TESTE (clonador entrando) |
| Care Daily (412861181906925) | UK / GBP | 8 | 132 (desde 19/06/2026) | Políticas prontas para care agencies: domiciliary care, supported living, children's homes ("Replace the folder", "Your records deserve better than a ring binder"). | PROVADO |
| Provider360 (106526261665719) | AU / AUD | 59 | 486 (desde 01/07/2025) | Pacotes de documentação/registro NDIS ("24 Hrs Branded Documentation", "Money-Back Guarantee", "Mega Black Friday Sale", isca "FREE NDIS Registration Roadmap"). Serviço + documentos, ticket alto (concorrentes em A$699–1.800). | PROVADO (ticket alto) |
| PDF Blueprints Store (1258550840671955) | UK / GBP | 2 | 6 | "Practical tools for landlords in England" (PDF low ticket ligado ao Renters' Rights Act). | TESTE |
| The Estate Agent Consultancy (132236203313997) | UK / GBP | 11 | 316 | Isca "11 Instruction-Winning Letters. FREE" para corretores; funil de coaching, não kit pago. | Sinal de isca, não PROVADO para kit |
| Proper Templates UK (841784112351783) | UK / EUR (Etsy) | 1 | 0 | Loja Etsy de templates UK. | TESTE |
| OpsReady Group (1127279927132772) | UK / GBP | 1 | 3 | "Food Business Owners: £19.99 Pack" (pacote de documentos para negócio de comida). | TESTE (preço £19,99 visível no anúncio) |
| Style Contractor Solutions (2216865148571498) | UK / GBP | 4 | 41 (anúncio do bundle: 14) | "125+ Contractor Documents. One Complete Bundle." + serviço de acreditação/ISO 9001. | PROVADO fraco (página mista serviço + bundle) |
| myramsapp (396132990239368) | UK / GBP | 12 | 92 | App de RAMS por assinatura, "Unlimited RAMS from £20 per month". | PROVADO (SaaS, não kit) |
| Safe Trade Solutions (731336926739492) | UK / GBP | 3+ | ≥69 (anúncio de trial 31/07) | Gerador de RAMS (trial grátis 14 dias). | PROVADO fraco (SaaS) |
| NDIS consultorias (NEXUS Compliance, Provider Path, EnableUs, Regis, ISO Professionals, ISO Consulting, NDIS Audit Help etc.) | AU / AUD | 78 anúncios no termo "NDIS policies" | maioria < 30 | Registro NDIS como serviço: A$1.375 (enfermeiros), A$1.500, A$1.800+GST; ganchos "SIL changes start 1 July 2026", "NDIS Registration 2026–2027", "add aged care". | Mercado de SERVIÇO caro; kit low ticket = BRECHA de preço |
| The Educators Domain (6057109234) | AU / AUD | 2 | 3 | Planners 2027 para educadores (A3 weekly program, Directors desk, Critical Reflection Journal, OSHC) e "Learning Story Packs". Marca antiga, anúncios sazonais novos. | TESTE (sazonal) |
| The Grounded Educator (1438937019297550) | AU / AUD | 4 | 3 | Recursos para educadores (sem título claro). | TESTE |

| ECE Learning Unlimited (106795547791748) | NZ + AU / NZD e AUD | 9 | 138 (desde 14/06/2026) | Assinatura para centros ECE: "70+ Policies, Always Current", "Walk Into ERO Confident", "Subscribe From $79/month", webinars e "Practical Tools Resource", 50% OFF. | PROVADO (assinatura) |
| LIGHTN / ECEDocs (760130433840230) | NZ / NZD | 6 | 66 | "Stay Compliant with ECEDocs" (políticas/documentos de ECE em software). | PROVADO (SaaS) |
| Quliance ECE Compliance Tool (1030545083484191) | NZ / NZD | 17 | 14 | App de compliance ECE: "HS121 Compliance Made Easy" (checagem de sono), "Centre Manager? Wrap up 2026". | TESTE (app novo, escalando criativos) |
| South London College UK (1147600535349816) | anúncio no IE, GBP | 2 | 65 | Isca "FREE Childminder Guide" (funil de curso). | isca |
| MindMe.ie (497810120230050) | IE / EUR | 1 | 195 | Marketplace de babás/childminders ("254,000+ members"), não vende kit. | — |
| TeacherMom (355625962145044) | ZA / ZAR | 1 | 1 | Recurso para professor (CAPS). | TESTE |
| **SWMS Kit (1305255946007345)** | AU / AUD | 3 | 29 (desde 01/10/2026; faz 30 em 31/10) | Kits de SWMS (Safe Work Method Statement, o "RAMS" australiano) por ofício: "**8 electrician SWMS – A$59**", "SWMS templates builders accept", gancho de norma "**SA fall rule: 2 m from 1 July 2026**". | TESTE → vira PROVADO amanhã se seguir ativo |
| Syncorswms (106521145842985) | AU / USD | 1 | 27 | "Sync or SWMS: Premier Source for SWMS & Construction Safety Documentation Templates". | TESTE |
| Site Paperwork (1259393673932465) | AU / AUD | 4 | 1 | Gerador de SWMS por IA ("One paragraph in. Full SWMS out."). | TESTE |
| SiteConnect (108804558118253) | NZ / NZD | 2+ | ≥19 | App de SWMS/RAMS para equipes. | SaaS |
| CareDocs Direct (1178206642051081) | UK / GBP | 2 | 65 | Gig no Fiverr: políticas e procedimentos de care "for $25". | PROVADO fraco (serviço barato) |
| Compliance Supports (227964520409222) | UK / GBP | 3 | 2 | "Full CQC Support — Save £701 Right Now" (serviço). | serviço |
| Little Sparks Elearning (1328490097003455) | UK / USD | 3 | 4 | E-learning para childminders: "Safer Recruitment Mastery", "Advanced Safeguarding Leadership", "The Childminder's Own Child" (casado com o EYFS de set/2026). | TESTE |
| Lic. Zulma Laguna (778739435326228) — complemento EUA | US / USD | 8 | 29 (desde 01/10/2026) | Kit dental em inglês: "Dental Docs, Done for You", "Lawyer-Reviewed Dental Consents & Forms", "Get Your Dental Clinic Inspection-Ready in 1 Hour"; 4 criativos NOVOS em 27/10. Nota anterior: "Dental Kit in Free Canva $27". | quase PROVADO (re-checar 31/10–05/11, como já estava na fila) |
| Organized Daycare (1023693544156702) | entrega só nos EUA (0 anúncios no AU), conta em AUD | 5 | 55 | "Ready Before She Knocks" (pasta pronta para a visita do fiscal de licença da creche/home daycare). | PROVADO (EUA, complemento) |
| **Estimulación en casa - Kids (563516643501385)** | operador LATAM, USD; anúncios em UK, AU, IE, HU, RO, PL, IT | **100** | ≤5 nos amostrados (50 de 100) | Planejamento anual pronto de pré-escola POR CURRÍCULO NACIONAL: "Your **EYFS** year, ready-made · ages 3–5" (UK), "Your **EYLF** year…" (AU), "Your **Aistear** year…" (IE), "Made for mixed ECCE rooms too", húngaro, romeno, polonês ("WOPFU i IPET już napisane + 120 zajęć"), italiano ("Il PEI già scritto + 120 attività", "Nuove Indicazioni 2026"). Clonagem em massa começou ~25/10/2026. | TESTE (onda nova de clonador; re-checar 12–20/11) |
| Year Sorted EYFS (1421173097745019) | UK / USD | 5 | 1 | "Your whole year, in editable Word", "New to Reception? Every day planned", "Provision + observations, every week". | TESTE |

Nichos varridos SEM vendedor low ticket encontrado no conector: FHRS/"food hygiene rating" (só restaurantes exibindo nota 5 e o app Leafe), "Safer Food Better Business" (só ruído), "EYLF templates" (0 resultados), "NDIS progress notes templates" (0), "childminding templates" (0), Irlanda "Tusla inspection" (0) e "short term letting register" (0), África do Sul "POPIA compliance templates" (0) e "ECD centre registration" (só cursos NQF4), NZ "healthy homes landlord" (só administradoras e e-book grátis da Crockers).

(continua abaixo)

## 3. Mercado e normas (fontes oficiais)

### 3.1 Childminders e early years — Inglaterra (Ofsted / EYFS)
- **Tamanho:** 24.700 childminders registrados no Ofsted em 31/03/2026 (−630 no ano; entraram 1.690, saíram 2.320). Também 27.900 provedores em "non-domestic premises" (nurseries/pre-schools) e 6.860 home childcarers; total 59.700 provedores. Fonte: GOV.UK, "Main findings: childcare providers and inspections as at 31 March 2026" (publicado 09/07/2026) — https://www.gov.uk/government/statistics/childcare-providers-and-inspections-as-at-31-march-2026/main-findings-childcare-providers-and-inspections-as-at-31-march-2026
- **Ciclo Ofsted (mudou em 2026):** carta do DfE (mar/2026) troca a janela de 6 anos por **4 anos** entre inspeções, com implantação completa até **março/2030**; novos registrados a partir de 01/04/2026 devem ser inspecionados em geral em **18 meses** (antes: 30 meses). Fontes: https://www.gov.uk/government/publications/early-years-register-providers-inspection-requirements-for-ofsted/inspection-of-early-years-register-providers-requirements-for-ofsted e https://assets.publishing.service.gov.uk/media/69c3dae623fcbcd838a6f63a/Requirements_for_early_education_and_childcare_inspections_letter_from_DfE_to_Ofsted.pdf . Página do Ofsted "how Ofsted inspects childminders" ainda mostra o ciclo antigo (atualizada em mar/2024).
- **Novo framework de inspeção com "report cards":** em vigor desde **10/11/2025** (escala de 5 pontos no lugar do julgamento de uma palavra). Entre 10/11/2025 e 31/03/2026, 1.723 inspeções, 1.027 de childminders (Coram PACEY). Fonte: https://www.corampacey.org.uk/?p=378050 e https://www.gov.uk/government/publications/early-years-inspection-toolkit-operating-guide-and-information/early-years-inspection-information-for-use-from-november-2025
- **EYFS atualizado em 01/09/2026:** novo statutory framework (inclui regras de safeguarding, referência escrita e checagens antes de nova pessoa começar, notificações ao Ofsted sobre quem mora/trabalha na casa, cães de raça proibida) + toolkit de inspeção do Ofsted atualizado a partir de 01/09/2026. Fontes: https://earlyyears.blog.gov.uk/2026/06/12/how-safeguarding-and-childrens-welfare-and-wellbeing-underpin-the-september-2026-updates-to-early-years-inspections/ , https://www.corampacey.org.uk/september-changes-for-childminders/ , https://ndna.org.uk/wp-content/uploads/2026/07/EYFS-Comparison-Table-Sept-2026.pdf
- **Leitura:** é exatamente o gancho que o Childminder Resource Hut usa ("Inspection Ready – September 2026", "Safeguarding Decoded"). Ciclo mais curto (6→4 anos) + novos em 18 meses = mais gente com inspeção marcada todo ano.

### 3.2 NDIS (Austrália)
- **Tamanho:** fim de 2024 = **21.387 provedores registrados** e **245.762 não registrados** (267.149 no total). Fonte: relatório trimestral out–dez/2024 da NDIS Commission e resposta ao Parlamento de NSW — https://www.parliament.nsw.gov.au/lcdocs/other/22827/AQON%20-%20Careseekers%20-%20received%2024%20December%202025.pdf . O número em 30/06/2026 está no relatório Q4 2025-26 (https://www.ndiscommission.gov.au/sites/default/files/2026-09/Quarterly%20Performance%20Report%20-%20Q4%202025-26.pdf), mas o trecho indexado não traz o total → VERIFICAR.
- **Norma com data:** registro OBRIGATÓRIO para provedores de **SIL (supported independent living) e plataformas** desde **01/07/2026** (anunciado em dez/2025; citado no relatório Q3 2025-26 — https://www.ndiscommission.gov.au/sites/default/files/2026-05/Quarterly%20Performance%20Report%20-%20Q3%202025-26.PDF). Os anúncios das consultorias usam isso ("SIL changes start 1 July 2026").
- **Leitura:** quem anuncia vende SERVIÇO de registro (A$1.375 a A$1.800+GST; Provider360 há 486 dias). Os ~245 mil não registrados (support workers autônomos) não têm kit barato anunciado: a busca "independent support worker sole trader NDIS" achou só 2 anúncios de trabalhadores, nenhum vendedor de kit → BRECHA de preço (kit A$27–47 com contrato de serviço, progress notes, incident report, fatura NDIS, checklist do Code of Conduct + app de registro diário). Risco: público pulverizado e pouca dor de prazo para quem não é registrado.

### 3.3 Early childhood Austrália (ACECQA / NQF)
- **Tamanho:** **18.197 serviços aprovados** no NQF Snapshot Q2 2026 (+1% no ano), 17.820 centre-based (98%); family day care ≈ 377 serviços (cálculo por diferença; Q1 2026 = 387). 92% dos serviços avaliados atingem o padrão nacional. Fontes: https://thesector.com.au/article/nqf-snapshot-q2-2026-quality-ratings-year-quarter-comparison e https://www.acecqa.gov.au/nqf/snapshots
- **Normas com data:** desde **27/02/2026**: regras de dispositivos digitais (restrição de celular pessoal), treinamento obrigatório de child protection/child safety para todos os trabalhadores e voluntários e o National Early Childhood Worker Register; penalidades máximas TRIPLICADAS desde **01/01/2026**. Prazo de treinamento de 27/08/2026 aparece só em escritório de advocacia (CBP) → VERIFICAR. Fontes: https://www.acecqa.gov.au/node/1113871 , https://www.education.gov.au/node/20468 , https://www.cbp.com.au/insights/publications/child-safety-compliance-under-the-new-national-law-a-legal-perspective-for-ecec-providers
- **Leitura:** comprador típico é o centro (diretor), que já compra SaaS (OWNA, ECE Learning Unlimited a partir de $79/mês). Para kit low ticket o público seria o EDUCADOR (learning stories, programação, reflexão crítica) — The Educators Domain vende planners 2027, mas só com anúncios sazonais de 3 dias. Nenhum vendedor PROVADO de kit low ticket no AU encontrado.

### 3.4 Landlords — Inglaterra (Renters' Rights Act 2025)
- **Roadmap:** Fase 1 em **01/05/2026** (fim do section 21 "no fault", contratos passam a Assured Periodic Tenancies). Fase 2 a partir do fim de 2026: **PRS Database** e depois o **Ombudsman** obrigatório para todo landlord privado. Fase 3: Decent Homes Standard no setor privado em 2035 ou 2037 (fontes divergem → VERIFICAR). Fontes: https://www.simmons-simmons.com/en/publications/cmiir2g2200b0ujfok41uipmz/renters-rights-act-2025-implementation-roadmap , https://www.trowers.com/insights/governmental-roadmap-for-implementation-of-the-renters-rights-act-2025-confirmed , https://www.wardhadaway.com/insights/updates/renters-rights-act-implementation-dates/
- **PRAZO forte:** o banco de dados "**Register your rental property**" entra no ar em **15/12/2026**, começando pelas **West Midlands** e indo região por região nos 12 meses seguintes; taxa de **£65 por imóvel por ano** (registro do landlord + registro de cada imóvel); PRS Database Regulations 2026 publicadas em 09/09/2026 (alguns escritórios ainda chamam de draft → VERIFICAR). Base: pouco mais de **5 milhões de imóveis alugados** no setor privado na Inglaterra (MHCLG, via NRLA). Fontes: https://www.hcrlaw.com/news-and-insights/renters-rights-act-2025-private-rented-sector-database-to-go-live-from-15-december-2026/ , https://www.nrla.org.uk/resources/renters-rights/landlord-database-register-your-rental-property-service , https://www.winkworth.co.uk/articles/preparing-for-the-landlord-database-what-documents-should-you-have-ready , https://www.mpamag.com/uk/news/general/englands-private-rented-sector-database-to-cost-sector-327m-a-year-nrla-warns/592243
- **Nº de landlords:** não confirmado nesta sessão (English Private Landlord Survey) → VERIFICAR.
- **Leitura (landlords):** a Biblioteca está cheia de imobiliárias usando o tema como isca (webinars, "Free Landlord Health Check", checklist grátis) e a NRLA ("Join Over 110,000 Landlords", "Get Ahead Of EPC C 2029"). Vendedor low ticket de PDF só o PDF Blueprints Store (6 dias). Gancho: "Pasta do landlord pronta para o Register your rental property" (documentos que o registro pede: gas safety, EICR, EPC, deposit, information sheet) + app de prazos de certificados por imóvel.

## 4. Ranking 0–10
(em andamento)

## 5. VERIFICAR
(em andamento)
