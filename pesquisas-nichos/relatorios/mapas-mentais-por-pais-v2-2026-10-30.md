# Mapas mentais, esquemas, resumos, flashcards e simulados por país — v2 — 30/10/2026

Refeita do zero a partir da v1 (`mapas-mentais-por-pais-2026-10-29.md`). Esta versão troca as datas estimadas por datas publicadas (ou VERIFICAR), mede os dias por `page_id` e traz preço, formato e texto dos anúncios quando consegui abrir.

## Como foi medido (e o que ficou limitado)
- **Dias** = hoje (30/10/2026) menos a data de início do anúncio ATIVO mais antigo visível da página. Em página com muitos anúncios a lista corta, então o número é um **mínimo** (marcado `≥`).
- **Conector `ads_library_search`** (ativos): medi por `page_id` OpoEsquemas, ZaufanyNauczyciel, My Nurse Notes, Concorsi in Mappe, Emma Schneider, Prefortia, Nitidomed, Guias Práticos, Nuvora, Mapa Didáctico de la Biblia, Sofía Herrera, Dra Laura Martin, Editorial Esquematízate, Étudefacile e outras. Rodei também buscas por termo em ES, FR, DE, IT e PT.
- **SearchAPI (texto, link e dias do corpo do anúncio):** funcionou só para as primeiras ~25 consultas (PL, US e parte de ES) e depois **os créditos zeraram**: `/me` mostra 10.000 de 10.000 usados no ciclo que termina em 08/11, e o servidor passou a devolver HTTP 429. Outros agentes consumiram a cota ao mesmo tempo. Tudo o que estava na fila e não rodou está em "VERIFICAR" no fim. **Precisa de recarga do plano para terminar a cobertura.**
- Preço só aparece quando consegui abrir a página do vendedor (WebFetch) ou quando estava no título do anúncio.
- Regra: **PROVADO** = vendedor de material de estudo (não academia de ticket alto) com anúncio ativo há 30+ dias no país/moeda. **TESTE** = vendedores com menos de 30 dias ou só academias. **PRAZO** = prova/convocatória com data oficial.

---

## Medições por vendedor (dias reais)

| Vendedor (page_id) | País / moeda | Anúncios ativos | Dias | O que vende / preço | Classe |
|---|---|---|---|---|---|
| ZaufanyNauczyciel.pl (838665652654203) | PL / PLN | 105 | **≥ 68** (SearchAPI, anúncio da biologia) | PDF de notas por matéria + "pewniaki". **Biologia: 49 zł (de 99 zł), PDF, 5,0 em 17 avaliações, promete 1543 páginas; um comprador recebeu 523 páginas e o vendedor explicou que são 3 arquivos.** Matura + E8 | PROVADO |
| enotatki.pl "Matura 2027 notatki" (794313660745548) | PL / PLN | 1 | 68 | **PDF com respostas aos 76 "pytań jawnych" de polonês, 29 zł (de 99 zł)**, e-mail em 1 min | PROVADO (pequeno) |
| Oswoić matmę (103449049213694) | PL / PLN | 2 | **206** | Pacote de notas gráficas + fiszki, matemática E8 | PROVADO (pequeno) |
| Testly (103584472242348) | PL / PLN | 8 | **111** | Questões reais p/ egzamin zawodowy (ex.: técnico em eletrorradiologia, MED.04). Preço VERIFICAR | PROVADO (vocacional) |
| Zdana Matura (1188380697699893) | PL | 1 | 16 | Matura de inglês | TESTE |
| OpoEsquemas (319121182004656) | ES / EUR | **3** | **149** | "Cuaderno Resúmenes (MEGARESUMIDO)", livros de testes Administrativo/Auxiliar do Estado, curso FOCUS AGE. Preço VERIFICAR | PROVADO (pouco volume, produto físico/curso) |
| Academia Prefortia – Guardia Civil (1470045239962805) | ES / EUR | ≥ 40 | **≥ 53** | Livros-resumo de ascenso (Cabo/Sargento), Guía Estrella (isca), curso "133ª". É academia | Academia provada |
| Editorial-esquematizate.es (106101570913247) | ES / EUR | ≥ 8 | ≥ 2 (lista cortada) | Temarios esquematizados 2027 por especialidade e **por CCAA**: Maestros, Secundaria, FP, **Educador/a Infantil e PTIS·ATE em PDF**; docentes em anillas físicas. Preços dos temarios NÃO aparecem na página; compra por "Código de Compra" pedido por WhatsApp. Supuestos online: 4,95 € (7 dias), 24,95 €/mês, 198 € único | TESTE |
| Nuvora Digital Store (1288382994365212) | ES / EUR | ≥ 25 | 1 | "La Constitución en esquemas + 300 test", "Guía + 3 bonus por 14,90 €", também extranjería e receitas | TESTE |
| Emma Schneider (1290103417523122) | ES / **BRL** (vendedor BR) | 53 | **≥ 8** (v1 viu 13; lista cortada) | "La Constitución entera en 42 páginas", "Toda la Constitución en 20 minutos". Preço VERIFICAR | TESTE (BR em moeda errada) |
| My Nurse Notes (107734932379817) | US / USD | 56 | **84** | "NCLEX Review Cheat sheet 400 pages", "Nursing Textbooks are Scam!", bundle impresso + digital com flashcards de farmacologia e Med-Surg (270 cartões) | PROVADO |
| ShopBloomwings (1124729214062164) | US / USD | 3+ | **59** | Cheat sheet do real estate exam nacional ("Skip the Filler") | PROVADO |
| StarkLifestyle (1030020273527646) | US / USD | 18+ (52 na v1) | 8 | Livro de "32 páginas" vs "500+ pages"; Black Friday | TESTE com volume |
| Real Estate Exam Cram & Prep (1113629338506379) | US / USD | 1 | 101 | Real estate/seguros/hipoteca (curso/app), 1 anúncio | Parcial |
| Concorsi in Mappe (1350053468191248) | IT / **USD** (BR) | 15 | **11** | "Meno pagine. Più chiarezza.", "Una sera. Un tema." Preço VERIFICAR | TESTE |
| Guias Práticos (101022082469947) | IT/DE / **USD** (BR) | 69 | **1** (todos nascem em 28–29/10) | "Allievi Carabinieri in 100 Mappe Visive", "Polizia Locale in 120 Schede Visuali", "Sachkundeprüfung §34a in 100 Lernkarten" | TESTE |
| **Sofía Herrera (1205419289331646)** | DE/FR/PL/GR / EUR (operador LATAM/BR) | **123** | **≥ 4** | "Deine Prüfung in 250 Lernkarten", "+250 fiches visuelles de l'ambulancier", PL "Powtarzaj każdy temat w 5 minut", grego | TESTE (novo, escala em 4 países) |
| **Dra Laura Martin (1274719509066382)** | PT/FR/IT/ES/HU / EUR | **74** | **≥ 2** | "250+ fiches visuelles + 8 bonus", "250+ mappe. Una sola biblioteca.", "Modulo Concorsi Pubblici incluso", "Repasa TCAE en 5 minutos", "Lisez un ECG en 8 étapes" | TESTE (novo) |
| Étudefacile (1299578486577349) | FR / **USD** | ≥ 15 | **≥ 7** | "X, en dessins": La Bible, neurologia, compta, astrologia, carrelage, les gestes qui sauvent | TESTE |
| Amélie Boissieu (1363004406903385) | FR / **USD** | 5+ | ≥ 8 | "Kit Comptable Pratique 2027 · 7 cahiers + 6 bonus" | TESTE |
| Mémo Territorial (1472925959218868) | FR / **USD** | 1+ | 8 | Concours territorial | TESTE |
| Cartes de Fluidité (1212359138623437) | FR / USD | 20+ | 1 | Cartões de fluência (idioma) | TESTE |
| My Patient (981063601765491) | FR / EUR | 1+ | < 1 | "Tout l'IFSI pour le prix d'un livre !" (enfermagem) | TESTE |
| Sportwissenschaft-Karten (1384907808039519) | DE / **USD** | 4+ | 3 | Cartões de ciência do esporte | TESTE |
| Nitidomed (1533871263132078) | MX / MXN | 4 | 1 | "48,000 tarjetas de Anki para el ENARM" | TESTE |
| Mapa Didáctico de la Biblia (958179187385380) | LATAM-ES / **BRL** | 20 (v1) | **257** | Bíblia em mapas | PROVADO |
| Ray A. Gapuz Review System (744606885578254) | PH / PHP | 3+ | ≥ 7 | NCLEX review (centro de revisão) | Academia |
| Nursing Nerds (1364130306765102) | US / USD | 4+ | 8 | "FREE Today!" (isca grátis NCLEX) | Isca |
| Bugle Prep (1307805909093773) | US / USD | 1+ | 2 | Prova de Fire Lieutenant de Massachusetts em **12/04/2027** (texto do anúncio), capítulo 1 grátis | Nicho |

Locais que aparecem mas são academia/editora (não contam como provado): pm_oposiciones, Esfera oposiciones, Opositatest, Centro de preparación Junta de Andalucía (ES); Tilde Insegna, Quizly, concorsi_essentials, Peer4Med, AIMS (IT); Nathan "Réussir mon CRPE" (86 dias, editora), EDN.fr (109 dias), CPCM (147 dias) (FR); leichterlernen.org (IHK, ≥ 17 dias), Jägerschmiede (Jagdprüfung, ≥ 29 dias), Thieme (DE).

---

## Brechas encontradas (uma a uma)

| # | País | Profissão / prova | Quem vende hoje | Há quantos dias | Tipo de brecha |
|---|---|---|---|---|---|
| 1 | **ES** | Constitución + oposiciones AGE em esquemas e testes | OpoEsquemas (local, 3 anúncios, livro/curso), Nuvora (1 d, 14,90 €), Emma Schneider (BR, BRL) | 149 d / 1 d / ≥ 8 d | Local provado mas pequeno; entrantes novos. Ninguém combina esquema + testes + contador da prova + plano diário |
| 2 | **ES** | Educador/a Infantil e PTIS·ATE por comunidade autónoma | Editorial Esquematízate (PDF por CCAA) | ≥ 2 d | Compra via WhatsApp e preço oculto: sobra espaço para checkout simples. Só um vendedor |
| 3 | **ES** | TCAE / celador / enfermagem | Dra Laura Martin (1 anúncio TCAE) | ≥ 2 d | Nenhum local vende esquemas de TCAE em low ticket nos anúncios ativos que vi |
| 4 | **PL** | Policja (test do policial) | **Ninguém** (0 anúncios ativos em PL para "test na policjanta") | — | Nicho vazio no termo medido |
| 5 | **PL** | Egzamin zawodowy (técnico: eletrorradiologia etc.) | Testly (questões) | 111 d | Só um vendedor de questões; ninguém com notas/mapas |
| 6 | **PL** | E8 matemática em notas gráficas + fiszki | Oswoić matmę; ZaufanyNauczyciel | 206 d; ≥ 68 d | Provado, mas pouca concorrência de "mapas" (fiszki existe) |
| 7 | **PL** | Matura demais matérias (geografia, polonês-epoki, inglês) | ZaufanyNauczyciel; Zdana Matura (inglês) | ≥ 68 d; 16 d | Concorrente principal cobre biologia/química/matemática; inglês só um novo |
| 8 | **PT** | Concursos públicos em mapas mentais | **Ninguém ≥ 30 d** (0 resultados para "mapas mentais concurso"); Dra Laura (PT-PT) | 1 d | Vazio no termo; só um entrante |
| 9 | **IT** | Concorsi em mappe (Carabinieri, Polizia Locale, scuola) | Concorsi in Mappe (BR, USD), Guias Práticos (BR, USD), Dra Laura (BR, EUR) | 11 d / 1 d / ≥ 3 d | Todos de fora, em moeda errada ou novos; locais são academias/simulador |
| 10 | **DE** | Lernkarten por profissão (§34a, Rettungs/Heilpraktiker etc.) | Sofía Herrera (EUR), Guias Práticos (USD), Sportwissenschaft-Karten (USD); locais: leichterlernen.org, Jägerschmiede | ≥ 4 d / 1 d / 3 d; ≥ 17 d / ≥ 29 d | Nenhum low ticket ≥ 30 d; locais em IHK/caça com apostilas |
| 11 | **FR** | Fiches visuais de IFSI / ambulancier / comptabilité | Sofía Herrera, Dra Laura, Étudefacile (USD), Amélie Boissieu (USD), My Patient (EUR) | ≥ 4 d, ≥ 2 d, ≥ 7 d, ≥ 8 d, < 1 d | Escala ainda sem prova de 30 dias; vários em USD |
| 12 | **FR** | Concours territorial / fonction publique em mémo | Mémo Territorial (USD) | 8 d | Um vendedor, moeda errada |
| 13 | **FR** | Bible en dessins | Étudefacile | ≥ 6 d | Só um, novo |
| 14 | **LATAM-ES** | Biblia en mapas | Mapa Didáctico de la Biblia (BRL) | 257 d | Moeda errada (BRL a público ES): provado por BR |
| 15 | **US** | Real estate license nacional (cheat sheet) | ShopBloomwings (59 d), StarkLifestyle (8 d), Real Estate Exam Cram (101 d, 1 anúncio) | 59 / 8 / 101 | Provado, aberto a mais vendedores |
| 16 | **US** | NCLEX cheat sheet e flashcards | My Nurse Notes (84 d) e muitos outros | 84 | Saturado |
| 17 | **PH / NG / CA** | NCLEX para enfermeiras estrangeiras (preço local) | Ray Gapuz (PHP, review center), RNursing Notes (PHP, 1 d), Nurse Forte (NGN), RN.NursePro (CAD) | ≥ 7 d … 0 d | Poucos materiais baratos em moeda local; não consegui confirmar PDF/preço |
| 18 | **US** | Concursos de bombeiro por estado (ex.: MA Fire Lieutenant) | Bugle Prep | 2 d | Nicho minúsculo com data (12/04/2027) |
| 19 | **MX** | ENARM | Nitidomed e cursos | 1 d | Tudo novo; sem low ticket provado |

---

## Ranking 0–10

Critérios: prova Meta (0–2) + tamanho (0–2) + data confirmada (0–2) + ticket (0–2) + facilidade/saturação (0–2).

| # | País × prova | Evidência (dias, anúncios, preço) | Data da prova (fonte) | Tamanho | Risco | Nota | Classe |
|---|---|---|---|---|---|---|---|
| 1 | **PL – Matura 2027 (notas + pewniaki + 76 pytań jawnych)** | ZaufanyNauczyciel ≥ 68 d, 105 anúncios, 49 zł; enotatki 68 d a 29 zł; Oswoić matmę 206 d | **Escrita 4–24/05/2027**, orais 6–31/05; resultados 09/07/2027 (CKE via Portal Oświatowy) | 322.859 na matura 2026 (v1; fonte da imprensa, VERIFICAR no CKE) | Idioma polonês exige revisão nativa; já tem líder com 105 anúncios | **8,5** | PROVADO + PRAZO |
| 2 | **ES – Constitución/oposiciones AGE em esquemas + testes** | OpoEsquemas 149 d (3 anúncios); Nuvora 1 d a 14,90 €; Emma Schneider (BR) ≥ 8 d | Administrativo C1: resolução BOE-A-2025-26262, exame em 23/05/2026 (já ocorreu, fonte secundária). **OEP 2026 (RD 387/2026), 27.232 plazas; convocatória 2027 NÃO publicada: VERIFICAR** | Constitución cai em quase toda oposición | Academias dominam o geral; sem data de prova futura | **7,5** | PROVADO local (pequeno) |
| 3 | **US – Real estate exam (cheat sheet nacional)** | Bloomwings 59 d; Stark 8 d (18+ anúncios); Exam Cram 101 d | Contínua (agendamento) | 300–400 mil/ano (v1, estimativa, VERIFICAR) | Saturação crescente; Stark entrou agora | **7,5** | PROVADO (59 d) |
| 4 | **LATAM-ES – Biblia en mapas** | Mapa Didáctico 257 d, BRL | Sem prova (devoção) | Grande | Já tem BR; moeda BRL é a brecha | **7,0** | PROVADO (BR) |
| 5 | **US – NCLEX** | My Nurse Notes 84 d, 56 anúncios | Contínua. Pass rate 2025: 86,7% dos 192.916 formados nos EUA na 1ª tentativa (resumo do relatório NCSBN de jun/2026; PDF não consegui ler) | 192.916 só 1ª tentativa EUA-RN (NCSBN, via resumo); a v1 dizia 328 mil sem fonte: **não confirmado** | Saturado; saúde exige cuidado | **7,0** | PROVADO |
| 6 | **ES – Guardia Civil** | Prefortia ≥ 53 d (academia + livros) | Convocatória BOE-A-2026-9982 (08/05/2026), 3.240 plazas; 1ª prova 11/07/2026 (calendário secundário). **OEP 2027: VERIFICAR** | 3.240 plazas | Academia, não low ticket puro | **6,5** | Academia provada |
| 7 | **IT – Concorsi em mappe** | Concorsi in Mappe 11 d, Guias Práticos 1 d, Dra Laura ≥ 3 d | Carabinieri 2026: bando março/2026, 3.081 vagas, prova 20–21/04/2026 (já passou). **Concorso docenti: bando não publicado em 13/10, esperado a partir de nov/2026: VERIFICAR** | 3.081 vagas; docenti 220 mil+ inscritos PNRR3 (v1) | Todos novos; sem local provado | **6,5** | TESTE |
| 8 | **DE/FR/IT/PT/PL – "250 fichas visuais por profissão"** | Sofía Herrera 123 anúncios ≥ 4 d; Dra Laura 74 anúncios ≥ 2 d | Sem prova única | Multi-país | É a mesma operação testando 5 idiomas; ainda sem 30 dias | **6,0** | TESTE |
| 9 | **PL – Egzamin zawodowy (técnicos)** | Testly 111 d, 8 anúncios | Datas por sessão: VERIFICAR | Médio | Só questões; preço VERIFICAR | **6,0** | PROVADO (1 vendedor) |
| 10 | **MX – ENARM** | Nitidomed 1 d (4 anúncios) | ENARM 2026 aplicado 28–30/09/2026 (v1, secundária). **ENARM 2027: VERIFICAR** (ciclo anterior: pré-registro abr–mai, prova set) | 66.278 inscritos 2025 (v1) | Cursos fortes, tudo novo | **6,0** | TESTE |
| — | CO – DIAN 2676 | Simulacros de academias | **Prova escrita 08/11/2026** (Guia do Aspirante, via Grupo Geard; CNSC/SIMO: VERIFICAR) | 1.900+ vagas | Em 9 dias: tarde demais | 4,5 | PRAZO curto |
| — | FR – IFSI, comptabilité, territorial | Todos BR/USD ou novos (< 10 d) | VERIFICAR | — | Sem prova de 30 d | 5,0 | TESTE |

### O que mudou em relação à v1
1. **Datas:** a v1 usava 2027 "estimado pelo ciclo". Agora: matura 2027 tem data publicada (4–24/05/2027). Para AGE 2027, Guardia Civil 2027, Carabinieri 2027, docenti IT e ENARM 2027, **não há data publicada** e ficou VERIFICAR.
2. **Espanha caiu de 9,0 para 7,5:** OpoEsquemas tem só 3 anúncios (149 dias), Nuvora e Emma são de 1 e ≥ 8 dias, e a prova AGE 2026 já passou.
3. **Polônia subiu para 1º:** tem data publicada, líder com ≥ 68 dias e 105 anúncios, mais três pequenos locais (29 zł, 49 zł, 206 dias), e dá para ver preço e produto.
4. **Preços reais:** biologia 49 zł (de 99), pytań jawnych 29 zł, Nuvora 14,90 €, Esquematízate supuestos 4,95/24,95 €.
5. **Novos achados:** Sofía Herrera (123 anúncios, 5 idiomas) e Dra Laura Martin (74 anúncios) rodando "250 fichas visuais" em EUR, Étudefacile/Amélie Boissieu/Mémo Territorial em FR com USD, Editorial Esquematízate com PDF por CCAA, Bloomwings (59 d) no real estate, Testly (111 d) e Oswoić matmę (206 d) na Polônia.
6. **Números fracos:** a v1 dizia 328 mil para NCLEX; agora só confirmo 192.916 formados nos EUA na 1ª tentativa, via resumo do relatório NCSBN 2025. O total real incluindo repetentes e estrangeiros ficou VERIFICAR.

---

## Datas oficiais (fonte e URL)

| Prova | Data | Fonte |
|---|---|---|
| Matura 2027 | Escrita 4–24/05/2027; oral 6–31/05; sessão adicional 1–16/06 (escrita); resultado 09/07/2027; poprawkowy 23–24/08/2027 | [Portal Oświatowy – Matura 2027 harmonogram](https://www.portaloswiatowy.pl/komunikaty-men-i-cke/matura-2027-harmonogram-27906.html) · [Interia](https://wydarzenia.interia.pl/matura/news-matura-2027-cke-podala-terminy-przyszlorocznych-egzaminow,nId,23531625). Dias por matéria: um site diz polonês 4/05, matemática 5/05; outro conflita. Confirmar no CKE |
| Egzamin ósmoklasisty 2027 | Existe harmonogram | [Portal Oświatowy](https://www.portaloswiatowy.pl/komunikaty-men-i-cke/egzamin-osmoklasisty-2027-harmonogram-27897.html) (datas não extraídas: VERIFICAR) |
| AGE Administrativo C1 | Convocatória BOE-A-2025-26262 (18/12/2025); exame 23/05/2026 (secundária) | [BOE-A-2026-3515](https://www.boe.es/boe/dias/2026/02/16/pdfs/BOE-A-2026-3515.pdf) · [Red Opositor](https://redopositor.com/blog/es-cuando-es-examen-administrativo-estado-2026/) |
| OEP 2026 AGE | Real Decreto 387/2026, 27.232 plazas | [RTVC](https://rtvc.es/la-oferta-de-empleo-publico-para-2026-con-27-232-plazas-para-el-estado-5-marzo-2026/) · [INAP](https://laadministracionaldia.inap.es/noticia.asp?id=1520238); cifras divergem entre fontes, conferir no BOE |
| Guardia Civil 2026 | BOE-A-2026-9982 (08/05/2026), 3.240 plazas; 1ª prueba 11/07/2026 | [Red Opositor calendário](https://redopositor.com/blog/es-calendario-oposiciones-guardia-civil-2026-fechas/) · [Academia Jesús Ayala](https://academiajesusayala.com/convocatoria-oposiciones-guardia-civil-2026-3240-plazas/); distribuição de plazas diverge |
| Policía Nacional Escala Básica | BOE 10/07/2026, 2.704 plazas; data da 1ª prova **não confirmada** (26/09 é orientativa) | [BOE-A-2026-15042](https://www.boe.es/boe/dias/2026/07/10/pdfs/BOE-A-2026-15042.pdf) · [Red Opositor](https://redopositor.com/blog/es-convocatoria-policia-nacional-2026-plazas-fechas/) |
| Allievi Carabinieri 2026 | Bando em março/2026, 3.081 vagas; prova desde 20–21/04/2026 (fontes divergem); bando 2027: VERIFICAR | [QdS](https://qds.it/concorso-allievi-carabinieri-data-prova-scritta/) · [Fanpage](https://www.fanpage.it/attualita/concorso-nellarma-dei-carabinieri-reclutamento-di-3081-allievi-bando-requisiti-e-come-fare-domanda/) |
| Concorso docenti Itália | Sem bando em 13/10/2026; hipótese não oficial: bando a partir de novembro, nomeações 01/09/2027 | [Tecnica della Scuola](https://www.tecnicadellascuola.it/concorso-docenti-2027-struttura-del-nuovo-bando-e-requisiti) · [Italia Oggi](https://www.italiaoggi.it/settori/scuola/scuola-nuovo-concorso-per-i-docenti-posti-disponibili-requisiti-e-procedure-tutti-i-dettagli-p7ovdtv4) |
| DIAN 2676 | Prova escrita 08/11/2026 | [Grupo Geard – guia de pruebas](https://www.grupogeard.com/blog/guia-pruebas-escritas-dian-2676-evaluaran-puntajes-recomendaciones) (secundária; CNSC/SIMO a confirmar) |
| ENARM | 2026: pré-registro 03/04–29/05/2026; 2025: prova 23–25/09/2025. **2027 sem convocatória** | [Excélsior](https://www.excelsior.com.mx/salud/enarm-2026-abre-registro-fechas-requisitos-y-sedes-examen-para-residencias-medicas) |
| NCLEX | Contínua. 2025: 192.916 formados nos EUA, 1ª tentativa, RN, 86,7% de aprovação | [NCSBN 2025 Exam Stats](https://ncsbn.org/public-files/2025_NCLEXExamStats_Final.pdf) (PDF não legível aqui; número vem de resumo) · [GoodNurse](https://goodnurse.com/article/276/nclex-pass-rates-2026-every-official-ncsbn-statistic-rn-pn) |
| Fire Lieutenant MA | 12/04/2027 | Texto do anúncio da Bugle Prep (não verificado em fonte oficial) |

---

## Recomendação
1. **PL matura 2027** (nota 8,5) é a única com vendedor provado, preço visível e data publicada. Entrar com notas gráficas + fiszki + os 76 pytań jawnych + contador até 04/05/2027. Pré-requisito: revisor nativo.
2. **ES Constitución/AGE** só se for com diferencial (esquema + testes comentados + plano por data), pois o local provado é pequeno e tem 3 entrantes novos. Esperar a convocatória 2027 para ancorar data.
3. **Bíblia em mapas em ES/FR** é a brecha de "moeda errada": BR vende em BRL há 257 dias para público ES; em FR só o Étudefacile (USD, ≥ 6 dias). Fora de prova, sem prazo.
4. Monitorar **Sofía Herrera** e **Dra Laura Martin** (page_ids acima): se passarem de 30 dias com 100+ anúncios, o formato "250 fichas por profissão" fica provado em DE/FR/IT/PT.

## O que continuou VERIFICAR
- **Cobertura que não rodou por falta de crédito SearchAPI:** US (NCLEX flashcards, ASVAB, CNA, TEAS, bar exam, firefighter, NREMT, PMP, Series 7, CDL, insurance, Praxis, phlebotomy), GB/CA/AU (Life in the UK, driving theory, OSCE), MX (COMIPEMS, UNAM, USICAMM, CENEVAL), CO (ICFES, CNSC), PE (nombramiento, SERUMS), AR/CL/EC, PL (radcowski, NCLEX), IT (riassunti, quiz, infermieri, OSS, medicina, patente), PT (código da estrada, PSP, GNR, enfermagem), FR (gendarmerie, police, ATSEM, aide-soignant), DE (Einbürgerungstest, Heilpraktiker, Pflege, Polizei, Steuerberater, MedAT), ES (celador, justicia, correos, enfermería, Policía Local) e Bíblia em IT/DE/PL/PT.
- Dias exatos (lista cortada) de: Emma Schneider, Prefortia, Sofía Herrera, Dra Laura Martin, Editorial Esquematízate, ZaufanyNauczyciel (≥ 68 d com SearchAPI; conector deu ≥ 54 d).
- Preço de: OpoEsquemas, Emma Schneider, Concorsi in Mappe, Guias Práticos, My Nurse Notes, Bloomwings, Stark (página 404), Testly, Sofía Herrera, Dra Laura, Étudefacile.
- Datas ainda não publicadas: AGE/Justicia 2027, Guardia Civil 2027, Policía Nacional (1ª prova), Carabinieri 2027, concorso docenti IT, ENARM 2027, egzamin zawodowy, E8 2027 (dias por matéria).
- Tamanhos não confirmados em fonte oficial: 322.859 candidatos da matura 2026; 328 mil NCLEX (a v1); 300–400 mil real estate; 66.278 ENARM 2025.
- Se "Sofía Herrera" e "Dra Laura Martin" são a mesma operação: não consegui provar.
