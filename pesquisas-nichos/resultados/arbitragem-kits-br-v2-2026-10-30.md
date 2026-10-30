# Arbitragem de kits brasileiros validados para outros países — v2 (30/10/2026)

> **Avisos de ambiente (ler antes)**
> - A v1 (`3 - EU/pesquisas/arbitragem-kits-br-2026-10-29.md`) **não estava acessível** neste ambiente (container na nuvem, sem o Desktop). Os seis vendedores citados no prompt (Editura Gold, CareTable, ABA Tools, Catechesi 360, Mister Shop, Tłuste Gary) foram procurados do zero. Não dá para fazer um "antes × depois" linha a linha com a v1; a seção 1 diz o que mudou em relação ao que o prompt descreve da v1.
> - **SearchAPI indisponível** (sem chave aqui e sem crédito até 08/11). Toda medição foi feita com o conector Meta (`ads_library_search`, só anúncios ATIVOS).
> - **DIAS REAIS** = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página. Nº de anúncios = `estimated_total_count` da busca por `page_ids`. Moeda = `currency` da conta de anúncios (USD/BRL/CLP/MXN/COP em página europeia = operador de fora; EUR/PLN/RON/CZK = conta local).
> - **Limite do conector:** a busca devolve no máximo 50 anúncios, do mais NOVO para o mais antigo. Página com mais de 50 anúncios esconde os antigos. Contornei fatiando por `search_terms` dentro do `page_id` (ex.: nome do produto) ou por `countries`. Foi assim que o ABA Tools saiu de "15 dias" para **90,6 dias** e a Editura Gold de "≥30 dias" para **441,6 dias**. Quando nem fatiando apareceu anúncio antigo, o número vem como "≥ X d".
> - **Páginas de vendas não abriram:** a rede do container bloqueia facebook.com e os domínios de venda (edituragold.ro deu "host não resolvido"; hotmart.com, payhip.com e wikipedia.org aparecem negados no proxy). Os **preços reais** abaixo vêm do **título do anúncio** quando o vendedor escreve o preço ali. O resto está como VERIFICAR, sem estimativa.
> - **Busca web esgotada:** a cota de WebSearch da sessão (200 buscas, compartilhada com os agentes irmãos) acabou no meio da pesquisa. Tamanho de mercado e normas **não foram confirmados por fonte oficial** nesta rodada; tudo que depende disso está marcado VERIFICAR.
> - Base BR: `dados/escalalow-ofertas-validadas.json` (213 ofertas; índice = posição, base 0).

---

## 1. Resumo (o que mudou em relação à v1 descrita no prompt)

1. **Nenhuma estimativa "est." sobrou.** Cada vendedor tem dias medidos por `page_id` (tabela 3). Preço só aparece quando está escrito no anúncio. O resto está como VERIFICAR.
2. **Os seis vendedores nomeados, remedidos:**
   - **ABA Tools:** **90,6 d** na Itália (USD, operador BR).
     - Pelo `page_id` puro pareciam 15 dias, porque a onda de 133 anúncios de 15/10 escondia os antigos.
     - Fatiando por "schede logopedia", apareceu o criativo "Meno preparazione, sedute più leggere", no ar desde ~31/07.
     - **É o único kit BR PROVADO num país europeu nesta varredura.**
   - **Editura Gold** (Romênia, RON, editora local):
     - a página tem **441,6 d** (histórias terapêuticas infantis);
     - o livro para diabéticos tem **153,2 d**;
     - dieta autoimune, 303,6 d; anti-inflamatória, 221,5 d; fígado gordo, 122,6 d.
   - **Tłuste Gary Przepisy bez cukru** (Polônia, PLN, local): **86,3 d**, 42 anúncios. Vende receitas sem açúcar, keto, air fryer e lancheira escolar.
   - **Catechesi 360** (Itália, USD): **3,8 d**, 17 anúncios, **"Tutto a €19,90"** (preço no anúncio).
     - Abriu um clone espanhol, **Catequesis 360**, com 0,8 d.
     - É TESTE, não PROVADO.
   - **CareTable** e **Mister Shop:** **não encontrados.** A busca por nome no conector é aproximada e devolve ruído. VERIFICAR o `page_id` na v1.
3. **Achado novo e forte: há uma onda BR nesta semana (25–30/10).** Dezenas de páginas novas, com conta em USD/BRL/CLP/MXN, lançaram ao mesmo tempo em IT/ES/PL/RO/GR/CZ/DE/FR:
   - catequese, quadros elétricos, alfabetização, fichas de terapia, receitas sem açúcar/diabetes, STL, costura e estimulação cognitiva;
   - muitas usam personas locais falsas (ex.: "Camille Dubois", "Marco Ferri", "Peyton Ashford").
   - Quase nenhuma tem 30 dias.
   - **Consequência:** a maioria das brechas "ninguém vende" da v1 virou "todo mundo começou ontem". O sinal útil agora é **quem continuar ativo daqui a 30 dias** (re-checar 27–30/11).
4. **Os mercados que já compram, com vendedor local antigo, são RO (Editura Gold) e PL (Tłuste Gary, Zmiana Sylwetki, CKO).** Os dois países pagam na moeda local, o que é um bloqueio de checkout (ver VERIFICAR).

**Top 5 do ranking (detalhe na seção 5):**

| # | Oportunidade | País | Régua | Nota |
|---|---|---|---|---|
| 1 | Kit de sessões ABA/logopedia para terapeutas (documentos + app) | IT | PROVADO (ABA Tools 90,6 d) | **7,5** |
| 2 | Kit de estimulação cognitiva para idosos / animadores (documentos + app) | FR | BRECHA | **6,5** |
| 3 | Fichas/histórias terapêuticas infantis + recursos emocionais (pais e profissionais) | RO | PROVADO (Editura Gold 441,6 d, local) | **6,5** |
| 4 | Recursos emocionais/educativos infantis para pais e professores | ES | PROVADO (Laura Educa 57,1 d, EUR local) | **6,0** |
| 5 | Kit de atividades para idosos para "Betreuungskräfte" | DE | TESTE (The Resource Lab ~3 d, 149 anúncios na DE) | **5,5** |

---

## 2. Kits BR de origem (EscalaLow, índices do JSON)

| Tipo de kit | Ofertas BR (índice: nome, dias, anúncios, preço) |
|---|---|
| Receitas para diabéticos / sem açúcar | 60: "Tem diabetes e fica em dúvida…" (80 d, 28, WhatsApp, sem preço); 86: 500 Receitas para Diabéticos (70 d, 22, sem preço); 202: +50 pães para diabéticos (135 d, 10, sem preço); 6: 365 Receitas sem açúcar/glúten/lactose (161 d, 112, R$ 10) |
| Estimulação cognitiva (idosos) | 83: Kit de Estimulação Cognitiva, Neuromente (169 d, 22, R$ 10); 194: "Sua mãe, seu pai… passa muito tempo sem fazer atividade", Cantinho das Atividades (65 d, 11, sem preço); 65 e 124: "Um presente que cuida de quem você ama…" (102 d e 85 d, WhatsApp) |
| Fichas de terapia infantil / psicopedagogia / ABA | 62: Kit Consultório Lúdico (91 d, 28, R$ 17); 187: 60 modelos dos 4 aos 16 anos (152 d, 11, R$ 27,90); 23: Kit Destrava Atendimento (211 d, 52, R$ 37,90); 130: Kit de Programas Transformação, Inovaba (o nome sugere ABA, VERIFICAR; 183 d, 16, R$ 47); 55: Baralho de Perguntas Terapêuticas (51 d, 29, R$ 37); 196: Kit Acalmar (57 d, 11, R$ 27) |
| Catequese / religioso | **Não há kit de catequese no JSON.** O mais próximo é o 150, São Bento (questionário + kit, 71 d, 14, sem preço). A origem BR do Catechesi 360 está como VERIFICAR (pode estar na base de 24/10). |
| Atividades infantis | 10: 5.000 atividades infantis (91 d, 85, WhatsApp); 49: +150 Dinâmicas (49 d, 31, R$ 17); 182: Kit +50 Atividades (70 d, 11, R$ 37); 33: +300 Dinâmicas de Arte (75 d, 43) |
| Alfabetização | 14: Kit da Família Silábica (82 d, 74, R$ 29,90); 53: +200 Dinâmicas para Alfabetização (63 d, 29, R$ 9,90); 142: Alfa Kids (165 d, 14, R$ 57); 178: Combo das Sílabas (57 d, 12, R$ 10); 73: Grafismo Fonético (461 d, 25, R$ 37) |
| Quadros elétricos / eletricista | 191: Quadros Elétricos Realistas (188 d, 11, R$ 67); 32: Apostila de Comandos Elétricos (53 d, 44); 35: Tabela Digital do Eletricista (61 d, 42); 54: Manual Prático do Eletricista Residencial (63 d, 29) |
| STL | 1: Modelos STL para vender (49 d, 178); 12: +500 STL Católicos (50 d, 77, R$ 10,90); 38: 300 STL Nicho Pet (56 d, 41, R$ 29,90); 59: Pack Elite STL (107 d, 28) |
| Costura | 5: +2000 Moldes de Costura (93 d, 116, R$ 37); 28: Moldes Digitais em PDF (364 d, 50, R$ 25); 114: +100 Moldes de Vestidos Infantis (82 d, 18) |

---

## 3. Vendedores medidos por `page_id` (dias reais em 30/10/2026)

Legenda de régua: **PROVADO** = 30+ dias no país/idioma/moeda. **TESTE** = sinal sem vendedor antigo. **BRECHA** = ninguém vende.

### 3.1 Os seis vendedores do prompt

| Vendedor | page_id | País/idioma | Moeda | Anúncios ativos | **Dias reais** | Produto (do anúncio) | Preço | Régua |
|---|---|---|---|---|---|---|---|---|
| **ABA Tools** | 108617997275390 | IT (+ EN veiculado na IT); BR = 0 | USD | 133 (IT 95) | **90,6 d** (fatia "schede logopedia"; a onda nova é de 15/10, 14,2 d) | "+500 Attività ABA Naturalistiche"; "Meno preparazione, sedute più leggere"; EN "+500 Naturalistic ABA Activities for Autism" | VERIFICAR | **PROVADO IT** |
| **Editura Gold** | 105441754726580 | RO | RON | 280 | **441,6 d** (histórias terapêuticas); diabetes 153,2 d; autoimune 303,6 d; anti-inflamatória 221,5 d; fígado gordo 122,6 d | "Cartea de care orice diabetic are nevoie"; "Planul alimentar al celor mai longevivi diabetici"; "Povești Terapeutice pentru Fricile Copiilor I e II"; "366 Povești de Seară"; "111 Rețete pentru Ficat Gras"; gramática da 5ª série para professores; ansiedade (308 p.) | VERIFICAR (formato físico × e-book também) | **PROVADO RO** (vendedor local) |
| **Tłuste Gary Przepisy bez cukru** | 103107748512330 | PL | PLN | 42 (todos vistos) | **86,3 d** | "50 przepisów… do śniadaniówki"; "Keto pudełka do pracy" (NOWOŚĆ 28/10); "Przepisy LOW CARB Air Fryer"; "MEGA PAKIET Air Fryer" | VERIFICAR | **PROVADO PL** (vendedor local) |
| **Catechesi 360** | 1209523738921107 | IT (+ EN) | USD | 17 | **3,8 d** | "450+ attività pronte per il catechismo"; "450+ Ready-to-Use Catechism Activities" | **€19,90** ("Tutto a €19,90") | TESTE |
| **CareTable** | não encontrado | — | — | — | — | Busca por nome devolve ruído (o conector não faz frase exata) | — | VERIFICAR page_id |
| **Mister Shop** | não encontrado | — | — | — | — | idem | — | VERIFICAR page_id |

### 3.2 Outros vendedores relevantes achados na varredura

| Vendedor | page_id | País | Moeda | Anúncios | Dias reais | Produto | Preço | Régua |
|---|---|---|---|---|---|---|---|---|
| Zmiana Sylwetki | 107925794059194 | PL | PLN | 57 | **≥142,5 d** (40 vistos) | "Przepisy z niskim IG", "120 przepisów fit", "14 E-BOOKÓW GRATIS", air fryer, "BLACK FRIDAY 2026" | VERIFICAR | PROVADO PL (local, saturado) |
| Laura Educa | 109425057952071 | ES | EUR | 54 | **≥57,1 d** (30 vistos) | "+200 páginas para trabajar con adolescentes", "Ayúdalo a gestionar la frustración", "50% OFF +5 BONOS GRATIS", Natal | VERIFICAR | PROVADO ES (local) |
| CKO – Centrum Kształcenia Online | 102793901372198 | PL | PLN | 6 na fatia "pamięć seniorów" | **28,4 d** | "Ćwiczenia na pamięć dla seniorów" + cursos com certificado (cuidador de idosos, demência) | VERIFICAR | TESTE forte (quase 30 d) |
| Bernadette | 620917691113491 | FR | EUR | ≥1 | 55,9 d | "Onde de la Mémoire" (produto não identificado) | VERIFICAR | VERIFICAR |
| Nova Skills | 1233949879806171 | RO + 10 idiomas | USD | 186 | RO "12 volume, câte unul pentru fiecare funcție": 13,7 d | farmacologia em PT-PT/SK/FR/NL/HE/TR/GR/CZ; gestão de obras (RO) | VERIFICAR | TESTE (operador BR multi-idioma) |
| The Resource Lab | 1123744187496255 | DE (149), IT, FR, HU, EN | USD | 149 só DE/AT/CH | ≥2,9 d (50 vistos) | DE "1.000 fertige Beschäftigungsangebote", "6 Bände + 5 Sonderbände", "100 Kurzaktivierungen in 10 Minuten", "Die Bibliothek für die soziale Betreuung"; IT "6 volumi + 5 volumi speciali"; também massagem e psicoterapia (DE) | VERIFICAR | TESTE (operador BR multi-nicho) |
| Seduta Pronta | 1447072035149109 | IT | USD | 3 | 1,7 d | "La seduta di domani, già pronta" | VERIFICAR | TESTE |
| The Mind Market | 884241854764422 | IT (2) e PT-PT | USD | 2 na IT | 1,7 d | "96 sedute pronte da stampare", "Laboratorio Pronto"; PT-PT "Ritmolândia 50 aulas de música prontas" | VERIFICAR | TESTE |
| Professora Maria | 1407583632419764 | ES | **BRL** | ≥1 | 1,8 d | "Fichas Visuales de Estimulación Cognitiva para Adultos Mayores" | VERIFICAR | TESTE |
| Tu Evolución Activa | 939481805922579 | RO | USD | ≥10 | 2,8 d | sem título (★★★★★) | VERIFICAR | TESTE |
| Mi Colega T.O | 1485100974676859 | ES | CLP | 26 (com MenteCloud) | 2,2 d | "+1.500 actividades listas para imprimir", "+180 sesiones listas en 1 minuto" | **US$ 17,99** ("Recupera tus noches · US$17,99") | TESTE |
| MenteCloud.com | 1317896694749207 | ES | CLP | idem | 6,6 d | "¡Accede ahora! (4.9/5)" | VERIFICAR | TESTE |
| Digital Home | 1285293408008330 | RO | USD | ≥1 | 0,7 d | "90 de fișe de lucru TCC gata pentru ședință" | VERIFICAR | TESTE |
| Fișe de Terapie pentru Adolescenți | 1279676471906222 | RO | EUR | ≥1 | <1 d | "131 de pagini, 80 de instrumente în română" | VERIFICAR | TESTE |
| Praxis Editorial | 1274332672438046 | GR | USD | ≥5 | 0,5 d | "+500 Δραστηριότητες Εργοθεραπείας" | VERIFICAR | TESTE |
| Attivita Premium | 1417738841431443 | IT | USD | 14 na fatia "quaderni" | 2,7 d | "8 quaderni, un percorso passo passo", "Dal pregrafismo alle prime frasi", "GLI e GNA non lo bloccano più" | **€7,90** ("2.500 schede così, a 7,90 €") | TESTE |
| Bindie | 1838422066369870 | CZ | CZK | 6 | 0 d (criados 30/10) | "První písmenka začínají hrou", "30 podzimních aktivit pro děti" | VERIFICAR | TESTE |
| Catequesis 360 | 1028759070329896 | ES | USD | ≥25 | 0,8 d | "¡Descubre Catequesis 360!" | VERIFICAR (no IT é €19,90) | TESTE |
| Corriere della Fede | 1310207422178013 | IT | USD | ≥10 | <1 d | advertorial "Un sacerdote rivela perché il 73% dei ragazzi abbandona la fede" | VERIFICAR | TESTE |
| Dziennik Wiary / Wzrastać w Wierze | 1286078767928026 / 1295960413599453 | PL | EUR | ≥10 | <1 d | mesmo molde de advertorial ("Jeśli masz dziecko, przeczytaj to") | VERIFICAR | TESTE |
| Bibliotheca Catholica | 1333178613218865 | PL | USD | ≥1 | 0,8 d | "Biblioteka Katolika – jednorazowa płatność" | VERIFICAR | TESTE |
| Viva Leve Mulher | 676647748861348 | ES | USD | 36 na ES | 3,8 d | pão sem glúten e sobremesas sem açúcar; "Recetas primero, el pago después" | VERIFICAR | TESTE |
| Dulce Modo on | 1088516177681629 | ES | MXN | 3 na ES | 4,7 d | "Adquiérelo por menos de lo que cuesta un café" | VERIFICAR | TESTE |
| L'Arte di Nutrirsi Bene | 1383022004888902 | IT | MXN | ≥100 na IT | ≥2,0 d | "+10.478 DOWNLOAD ★★★★★" | VERIFICAR | TESTE |
| Peyton Ashford | 846728461848088 | IT | USD | ≥1 | 4,9 d | "3 libri sull'alimentazione adatta al diabete al prezzo di 1" | VERIFICAR | TESTE |
| Ma Table Saine / Camille Dubois | 1336755276192574 / 710403968818808 | FR | USD | ≥5 cada | <2 d | "4.9/5"; "plats keto avec votre Thermomix" | VERIFICAR | TESTE |
| Claude Ingegneria Elettrica PRO | 1388019914391217 | IT | **BRL** | ≥1 | 0,8 d | "500+ Progetti Elettrici + 4 Bonus" | **€27** (no título) | TESTE |
| Studio Quadri / Marco Ferri | 721617357705716 / 1391669727368636 | IT | USD | ≥2 cada | 1,0 d / 0,5 d | "Progetta i tuoi quadri in 15 minuti"; "Quadri elettrici professionali in meno di 15 minuti" | VERIFICAR | TESTE |
| Tablero Studio | 603360102852473 | ES | USD | ≥4 | 1,9 d | "Diseña tus cuadros eléctricos en minutos" | VERIFICAR | TESTE |
| Sebastián Torrez | 1067088809830736 | IT | USD | ≥5 | 0,8 d | "+150 file STL di auto" | VERIFICAR | TESTE |
| William Vyralstl | 1356118524248182 | EU (multi) | USD | ≥1 | <1 d | "Get access for less than $17" | **< US$ 17** (no título) | TESTE |
| Entre Mujeres | 1180416348492259 | ES | USD | ≥5 | 0,6 d | "200+ patrones digitales en PDF" | VERIFICAR | TESTE |
| Vanessa Agudelo | 221946127676821 | ES | COP | ≥3 | 0,7 d | guia de costura de 140 páginas | VERIFICAR | TESTE |
| Sweet Crafts | 1178674435322096 | IT | USD | ≥5 | <1 d | "LA BOTTEGA DEL FELTRO™" (moldes de feltro) | VERIFICAR | TESTE |
| Mais Educação | 100131258840707 | PT (vazando do BR) | **BRL** | ≥7 | <1 d | "1001 Atividades para Estimular a Mente" | VERIFICAR | não prova PT |

---

## 4. Varredura por tipo de kit × país

Total = `estimated_total_count` da busca, só anúncios ativos, que inclui ruído.

| Kit | PT-PT | ES | IT | FR | DE | PL | RO | CZ | GR | EN |
|---|---|---|---|---|---|---|---|---|---|---|
| **Estimulação cognitiva** | 45; só serviços + BR vazando (Mais Educação, BRL) → **BRECHA local** | 155; serviços e software (NeuronUP) + Professora Maria (BRL, 1,8 d) → **TESTE** | 64; centros + Seduta Pronta, The Mind Market, The Resource Lab (todos ≤2 d) → **TESTE** | 48 em "stimulation cognitive" (ruído); **2** em "exercices mémoire seniors" → **BRECHA** | 61; The Resource Lab "1.000 fertige Beschäftigungsangebote" (≤3 d) → **TESTE** | 12; CKO 28,4 d (PLN) → **TESTE forte** | 30; Nova Skills 13,7 d, Tu Evolución Activa 2,8 d → **TESTE** | não varrido | não varrido | frase longa vira ruído; CareTable não achado → VERIFICAR |
| **Receitas diabéticos / sem açúcar** | não varrido | 45; Viva Leve Mulher 3,8 d, Dulce Modo on 4,7 d → TESTE lotado | 68; L'Arte di Nutrirsi Bene ≥2 d, Peyton Ashford 4,9 d → TESTE lotado | 42; Ma Table Saine, Camille Dubois (<2 d) → TESTE | 73; nutra, sem kit de receitas → BRECHA de kit (nutra domina) | 49; Tłuste Gary 86 d, Zmiana Sylwetki ≥142 d, Luckydiets, psicodietistas → **PROVADO, saturado** | Editura Gold diabetes 153 d → **PROVADO** | — | — | — |
| **Fichas terapia infantil / ABA / TO** | — | 18; Mi Colega T.O (CLP, US$ 17,99, 2,2 d), MenteCloud 6,6 d → TESTE | 9 em "schede logopedia": **ABA Tools 90,6 d** → **PROVADO** | — | The Resource Lab "40 Interventionen", "Therapiematerial" (≤3 d) → TESTE | — | Digital Home, Fișe de Terapie pentru Adolescenți (<1 d); Editura Gold (histórias terapêuticas 441 d, local) → **PROVADO (formato livro)** | — | Praxis Editorial (+500 εργοθεραπεία, <1 d) → TESTE | ABA Tools EN veiculado na IT |
| **Catequese** | — | 89; Catequesis 360 0,8 d, Valentina Herrera (BRL), Raquel Ferrero; Laura Educa (local, não é catequese) → TESTE | 28; Catechesi 360 3,8 d (€19,90), Corriere della Fede (<1 d) → TESTE | — | — | 76; Dziennik Wiary, Wzrastać w Wierze, Bibliotheca Catholica (<1 d) → TESTE | — | — | — | Catechesi 360 EN (3,8 d) |
| **Atividades / alfabetização** | — | não varrido (ver Laura Educa) | 79 em "schede didattiche"; Attivita Premium (€7,90, 2,7 d) → TESTE | — | — | **1.767** em "karty pracy"; mercado LOCAL maduro (Mathers.pl, CudaEdukacji, Pomabajki, RELYA) → saturado | 135 em "fișe de lucru"; Liliana's Music Class e outros, novos → TESTE | 201; Bindie (CZK, 0 d) → TESTE | 66; Praxis Editorial → TESTE | — |
| **Quadros elétricos** | — | 74; Tablero Studio 1,9 d; resto formação → TESTE | 75; Claude Ingegneria (€27, BRL), Studio Quadri, Marco Ferri (≤1 d) → TESTE | — | — | — | — | — | — | — |
| **STL** | busca conjunta em 9 países: 169; Sebastián Torrez (IT, 0,8 d), William Vyralstl (<US$ 17), 3D AI Studio (serviço), herzensvorlagenwerk (Etsy DE) → TESTE | | | | | | | | | |
| **Costura** | — | 172; Entre Mujeres (0,6 d), Vanessa Agudelo (COP); cursos locais → TESTE | 173; Sweet Crafts (feltro), Marina Deco (USD); ArteModa local → TESTE | — | — | — | — | — | — | — |

"—" = não varrido nesta rodada (orçamento do conector e da busca web). A v1 cobria PT-PT, FR, DE e EN para vários desses kits; ficam como VERIFICAR para a próxima rodada com o SearchAPI (crédito volta em 08/11).

### Leitura

1. **A onda BR de 25–30/10 é o fato do mês.** Os mesmos moldes aparecem clonados em vários países no mesmo dia:
   - "Catechesi 360" → "Catequesis 360";
   - "Corriere della Fede" → "Dziennik Wiary" / "Wzrastać w Wierze";
   - The Resource Lab e Nova Skills, em 10+ idiomas.

   As contas são USD/BRL/CLP/MXN e as personas, locais e falsas. A régua de PROVADO não vale para elas ainda: só daqui a 30 dias dá para saber quem vendeu.
2. **Onde já existe compra comprovada, o vendedor é local e cobra na moeda local:**
   - Editura Gold (RON);
   - Tłuste Gary, Zmiana Sylwetki e CKO (PLN);
   - Laura Educa (EUR, ES).

   Para entrar nesses mercados é preciso checkout em RON/PLN, ou aceitar cobrar em EUR (VERIFICAR conversão).
3. **O único kit de operador BR já validado fora do Brasil, nesta varredura, é o ABA Tools na Itália (90,6 d).** Ele é próximo do modelo do usuário (kit para profissional + sessões prontas). O concorrente acabou de dobrar a aposta: 133 anúncios criados em 15/10.
4. **França segue vazia** para estimulação cognitiva em PDF (2 anúncios no total), igual à nota de 28/10 ("cognitive stimulation for the elderly — nobody native sells it"). É BRECHA, e a demanda não está provada.

---

## 5. Ranking 0–10

Critérios: prova no país (peso maior), encaixe no modelo do usuário (kit de documentos + app por profissão), concorrência atual, ticket e barreiras (moeda, idioma, checkout).

| # | Oportunidade | País/idioma | Régua | Evidência principal | Nota | Por quê |
|---|---|---|---|---|---|---|
| 1 | Kit de sessões ABA/logopedia para terapeutas (programas, registros, app) | IT | **PROVADO** | ABA Tools, 90,6 d, USD, 133 anúncios (95 na IT) | **7,5** | Único kit BR provado na Europa nesta varredura. Encaixa em "kit por profissão". Concorrente BR único, porém agressivo. A base BR tem um kit parecido (índice 130, Inovaba, 183 d, R$ 47; o nome sugere ABA, VERIFICAR). Diferenciar com documentos e normas italianas (VERIFICAR: linhas-guia ISS sobre autismo, figura do TNPEE/logopedista). |
| 2 | Kit de estimulação cognitiva para idosos / animadores de EHPAD (documentos + app de atividades) | FR | **BRECHA** | 2 anúncios em "exercices mémoire seniors"; só software (NeuronUP France) e oficinas presenciais | **6,5** | Nenhum vendedor de PDF/kit, e a onda BR ainda não chegou à FR nesse tema. Base BR provada (índice 83, 169 d). O risco é a demanda não provada; teste barato. |
| 3 | Histórias/fichas terapêuticas infantis (medos, birras, divórcio, emoções) | RO | **PROVADO** (local) | Editura Gold: 441,6 d, 280 anúncios, RON | **6,5** | Mercado comprador há mais de 1 ano. O vendedor é editora local. Formato físico ou e-book VERIFICAR. Checkout em RON VERIFICAR. A onda BR de fichas de terapia (Digital Home, Fișe de Terapie pentru Adolescenți) entrou em 29–30/10. |
| 4 | Recursos emocionais/educativos infantis para pais e professores | ES | **PROVADO** (local) | Laura Educa: ≥57,1 d, 54 anúncios, EUR | **6,0** | Prova em euro na Espanha. Os chilenos (Mi Colega T.O, US$ 17,99; MenteCloud) chegaram há 2–7 d. Encaixa em "fichas de terapia infantil" para psicólogos e TO. |
| 5 | Atividades prontas para "Betreuungskräfte" (Seniorenbeschäftigung) | DE | **TESTE** | The Resource Lab: 149 anúncios na DE/AT/CH, ≥2,9 d | **5,5** | Profissão regulamentada com público grande (VERIFICAR: §43b/§53b SGB XI e nº de Betreuungskräfte). Concorrente BR único e muito recente. O alemão exige tradução de qualidade. |
| 6 | Estimulação cognitiva / exercícios de memória para idosos | PL | TESTE forte | CKO, 28,4 d, PLN, e-book + cursos | 5,5 | Quase 30 d com vendedor local. Público de cuidadores (CKO vende curso de "opiekun osób starszych"). Checkout em PLN/BLIK VERIFICAR. |
| 7 | Estimulação cognitiva | ES | TESTE | Só Professora Maria (BRL, 1,8 d) + software/serviços | 5,5 | Quase brecha em euro. O BR já entrou (BRL). Espanhol neutro não prova a ES. |
| 8 | Sessões prontas de estimulação / logopedia | IT | TESTE | Seduta Pronta, The Mind Market, The Resource Lab (≤2 d) | 5,0 | Mesma praça do #1; três BR novos ao mesmo tempo. |
| 9 | Receitas sem açúcar / IG baixo / diabetes | PL | PROVADO (local, saturado) | Tłuste Gary 86,3 d; Zmiana Sylwetki ≥142,5 d; Luckydiets; psicodietistas | 5,0 | Demanda provada, mas o mercado local é forte (14 e-books grátis por pedido, Black Friday). Só entra com nicho estreito (ex.: diabetes tipo 2 + app de glicemia). |
| 10 | Receitas para diabéticos | RO | PROVADO (local) | Editura Gold, livro de diabetes, 153,2 d | 5,0 | Prova clara. Um único vendedor local, que é editora (formato VERIFICAR). Checkout em RON. |
| 11 | Catequese (450+ atividades) | IT, ES, PL | TESTE | Catechesi 360 3,8 d (€19,90); Catequesis 360 0,8 d; Corriere della Fede, Dziennik Wiary, Wzrastać w Wierze, Bibliotheca Catholica (<1 d) | 4,5 | Onda simultânea de 6+ páginas. Ninguém provado. Fora do modelo "profissão" (catequistas são voluntários). Re-checar 27/11. |
| 12 | Fichas de terapia (TCC / adolescentes / TO) | RO, GR | TESTE | Digital Home, Fișe de Terapie pentru Adolescenți, Praxis Editorial (<1 d) | 4,5 | Onda BR de 29–30/10. Na RO, a demanda é sustentada pela Editura Gold (#3). |
| 13 | Quadros elétricos (projetos prontos) | IT, ES | TESTE | Claude Ingegneria (€27), Studio Quadri, Marco Ferri, Tablero Studio (≤2 d) | 4,0 | Quatro BR entraram em 28–29/10. A norma local (VERIFICAR: CEI 64-8 IT / REBT ES) é diferencial possível, mas ninguém provou venda. |
| 14 | Alfabetização (cadernos progressivos) | IT | TESTE | Attivita Premium €7,90 (2,7 d) | 4,0 | Ticket muito baixo e concorrente BR novo. |
| 15 | Receitas para diabéticos | ES, IT, FR | TESTE lotado | Viva Leve Mulher, Dulce Modo on, L'Arte di Nutrirsi Bene, Peyton Ashford, Ma Table Saine, Camille Dubois (todos <5 d) | 3,5 | Muitos LATAM/BR entrando ao mesmo tempo, sem prova. Na DE, o tema é dominado por nutra. |
| 16 | Atividades / fichas escolares | PL | PROVADO (local, saturado) | 1.767 anúncios em "karty pracy" (Mathers.pl, CudaEdukacji, Pomabajki, RELYA) | 3,5 | Mercado local maduro; não compensa entrar sem diferencial. |
| 17 | STL (pacotes de arquivos) | IT, multi | TESTE | Sebastián Torrez, William Vyralstl (<US$ 17) (<1 d) | 3,0 | Fora do modelo do usuário. Público concorrido (Etsy, Cults, Printables). |
| 18 | Moldes de costura | ES, IT | TESTE | Entre Mujeres, Vanessa Agudelo (COP), Sweet Crafts (<1 d) | 3,0 | Fora do modelo. Onda LATAM/BR nova. |
| 19 | Alfabetização / atividades | CZ | TESTE | Bindie (CZK, 0 d) | 3,0 | Um único anunciante, criado hoje. |
| — | Qualquer kit | PT-PT | sem prova | Só anúncios BR em BRL vazando para PT (Mais Educação) | — | Não prova Portugal; ver notas de 28/10 (preço de consumo em PT entre €4,90 e €14,90). |

---

## 6. Lista final de VERIFICAR

**Vendedores e páginas**
1. **CareTable** e **Mister Shop**: recuperar o `page_id` (e o país) na v1 do Desktop e remedir. A busca por nome no conector não acha. Hipótese não confirmada: CareTable seria estimulação cognitiva em EN/DE.
2. **ABA Tools**: preço, plataforma, bumps, garantia e se há app (abrir a página de vendas no Mac). Confirmar o país de entrega dos anúncios EN (US/GB?) e se há fatia ES/PT antiga.
3. **Editura Gold**: domínio da loja, formato (livro físico com frete × PDF), preços em RON e se aceita EUR. Se é editora local ou operador com página antiga.
4. **Tłuste Gary**, **Zmiana Sylwetki** e **CKO**: preço em PLN, plataforma (BLIK?) e formato (e-book × assinatura).
5. **Laura Educa**: produto exato (recursos emocionais? caderno para adolescentes?), preço em EUR e plataforma. Também se os 24 anúncios não vistos chegam a 90+ d (fatiar por termo).
6. **Catechesi 360 / Catequesis 360**: se há kit BR de catequese na base `escalalow-ofertas-24-10.json` (não há na de 213). Confirmar o €19,90 na página.
7. **Bernadette (FR) "Onde de la Mémoire"** (55,9 d, EUR): o que vende. Se for kit de memória, a FR deixa de ser BRECHA pura.
8. **The Resource Lab** e **Nova Skills**: se existem anúncios com mais de 30 dias por trás da onda de 27–29/10 (fatiar por produto, como no ABA Tools).

**Mercado e normas** (sem fonte oficial nesta rodada; a busca web esgotou)
9. IT: número de logopedistas, TNPEE e terapeutas ABA; linhas-guia ISS sobre autismo e exigência de registro de sessões.
10. FR: número de EHPAD e de animadores; norma que exija programa de atividades/estimulação documentado.
11. DE: número de Betreuungskräfte (§43b/§53b SGB XI) e Richtlinien de documentação de atividades.
12. RO e PL: tamanho do público pagante em RON/PLN; Hotmart/Kiwify cobram nessas moedas? Alternativa local (PayU, BLIK)?
13. ES: público de psicólogos e TO infantis; norma de documentação clínica (Lei 41/2002), se servir de gancho.

**Re-checagens com data**
14. **27–30/11/2026:** remedir todas as páginas da onda de 25–30/10 (tabela 3.2). Quem estiver com 30+ dias vira PROVADO e muda o ranking (catequese, quadros elétricos, fichas de terapia RO/GR, receitas ES/IT/FR).
15. **Após 08/11 (crédito do SearchAPI):** varrer o que ficou "—" na tabela 4 (PT-PT, FR, DE e EN para receitas, catequese, alfabetização e quadros; GR e CZ para os outros kits), com frase exata e `total_results`.

---

## 7. Método e limitações (resumo)

- Conector Meta `ads_library_search`, `ad_active_status: ACTIVE`, `countries` ISO-2, `limit` de 3 a 50. Cerca de 55 consultas.
- Dias: o menor `ad_delivery_start_time` visto. Quando a página tem mais de 50 anúncios, fatiei por termo (`search_terms` + `page_ids`) ou por país (`countries` + `page_ids`). Valores com "≥" são limite inferior.
- A busca por termo no conector **não é frase exata**: termos longos ou nomes próprios raros devolvem ruído (ex.: "CareTable", "Mister Shop", "imparare a leggere" com 25 mil resultados).
- Sem página de vendas (rede bloqueada) e sem busca web após a cota: preço só do título do anúncio; mercado e normas VERIFICAR.
- Dados brutos de cada consulta em `/tmp/claude-0/-home-user-ofertas/65e3a336-5a5d-550f-88e2-a220d0284836/scratchpad/medidas.md` (temporário).
