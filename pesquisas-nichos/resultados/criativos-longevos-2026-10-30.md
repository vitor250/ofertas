# Criativos que sustentam 90+ dias — v2 (30/10/2026)

> **Avisos de ambiente**
> - A v1 (29/10) e os arquivos do Desktop **não estavam acessíveis** neste ambiente (container na nuvem). Esta versão foi feita do zero, com as notas do usuário (`notas/*.md`) e os page_ids já medidos pelos agentes irmãos em `resultados/` como ponto de partida.
> - **SearchAPI indisponível** (sem chave neste container e créditos zerados até 08/11/2026). Toda medição foi feita com o **conector Meta** (`ads_library_search`, só anúncios ATIVOS).
> - DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` da busca por page_id. Limite do conector: devolve no máximo 50 anúncios, do mais novo para o mais antigo; em página com >50 ativos o "mais antigo" é um piso (≥).
> - **Limite do método para criativos:** o conector devolve TEXTO (body, título do link, descrição, CTA), datas, plataformas e moeda. Ele NÃO devolve o vídeo/imagem nem a transcrição. Por isso "formato", "duração" e "gancho dos 3 primeiros segundos" só estão preenchidos quando o próprio texto/título revela (ex.: "vídeo", "carrossel", catálogo `{{product.name}}`) ou quando a captura de pré-visualização funcionou; o resto está marcado VERIFICAR.

## 0. Status da gravação
- [ ] Lista de vendedores e page_ids
- [ ] Medição por page_id (dias, nº anúncios, moeda)
- [ ] Anúncios mais antigos x mais novos por página
- [ ] Páginas de vendas (preço, plataforma, bumps, garantia)
- [ ] Padrões por nicho/país
- [ ] 9 testes (3 hooks × 3 bodies) por oferta nossa
- [ ] Ranking 0–10
- [ ] Lista final VERIFICAR

## 1. Vendedores e page_ids (medição de 30/10/2026, só ATIVOS)

| # | Vendedor (page_id) | País / idioma / moeda da conta | Nicho / produto | Nº anúncios ativos | Anúncio ativo mais antigo | DIAS REAIS | Anúncios com 90+ d | Régua |
|---|---|---|---|---|---|---|---|---|
| 1 | Childminder Resource Hut (564585390322776) | UK / inglês / GBP | childminder e creche (Ofsted, EYFS): packs de inspeção, safeguarding, displays físicos, calendários | 35 (todos visíveis) | 01/07/2025 | **485,6** | **23 de 35** | PROVADO forte |
| 2 | Editura Gold (105441754726580) | RO / romeno / RON | editora: livros de "povești terapeutice" para crianças, saúde (tiroide, colesterol, dieta autoimune), ansiedade, gramática para professores | **280** (só 50 visíveis por consulta; medi por recorte de termo) | 14/08/2025 (achado no recorte "povești terapeutice") | **≥ 441,6** (piso) | muitos (só nos recortes: ≥ 25) | PROVADO forte (não é kit de documento: é livro, formato VERIFICAR) |
| 3 | Qualitiva Soluciones (574842992375227) | CO / espanhol / COP | habilitação de IPS e consultórios (Res. 3100): documentos, diagnóstico, auditoria, curso | 32 (todos visíveis) | 26/01/2026 | **276,0** | **10 de 32** | PROVADO |
| 4 | Abogados de Éxito (1255927857876624) | MX / espanhol / MXN | curso para advogado (redação jurídica, processo civil oral) | 34 (todos visíveis) | 29/01/2026 | **273,2** | **6 de 34** | PROVADO (curso, não kit) |
| 5 | OpoEsquemas (319121182004656) | ES / espanhol / EUR | oposições AGE: caderno de resumos, livros de testes, temário, curso | 3 | 02/06/2026 | **149,3** | **3 de 3** | PROVADO (pouca verba) |
| 6 | Care Daily (412861181906925) | UK / inglês / GBP | políticas prontas para care agencies (domiciliary care, supported living, children's homes) | 8 | 19/06/2026 | **132,1** | **7 de 8** | PROVADO |
| 7 | Kit Studio Blindato - APP (1294553453740890) | IT / italiano / USD (operador estrangeiro, provável BR) | kit de documentos do dentista + app | 28 | 17/09/2026 | **42,8** | 0 | PROVADO (30+), **não é 90+** |
| 8 | Kit di Documenti Psicologici (1316795101520270) | IT / italiano / USD (mesmo operador do #7, ver relatório irmão de funil) | kit do psicólogo ("Oltre 270 documenti") | 35 | 23/09/2026 | **36,0** | 0 | PROVADO (30+), **não é 90+** |
| 9 | Kontrola Sanepidu (388263394381460) | PL / polonês / PLN | procedimentos sanitários para salão de beleza | 12 | 01/10/2026 | **28,5** | 0 | **Hoje NÃO passa de 30 d** (o prompt diz 90+; a página trocou os criativos ou a v1 mediu outra coisa → VERIFICAR) |

Observações da medição:
- Os itens 7, 8 e 9 estão no prompt como "90+ dias", mas hoje o anúncio ativo mais antigo deles tem 43, 36 e 28 dias. Mantive na análise porque são os concorrentes diretos das nossas ofertas (dentista IT, psicólogo IT) e o modelo de salão PL, mas eles NÃO entram como exemplo de criativo de 90+.
- Kontrola Sanepidu tem uma página irmã nova, "Kontrola sanepidu w gabinecie lekarskim" (1302627286276800, 1 anúncio de 27/10, "Aktualizacja procedur w gabinecie medycznym – poradnik"), e um clone de operador estrangeiro, **Sophie Collins** (1423844567472797, conta USD, 57 anúncios, os mais antigos de 23/10 = 7 d), que mistura gabinete ("46 gotowych zgód", "RODO gotowe na recepcji", "Twoje logo na każdej kartce", "Sterylizacja krok po kroku, na ścianie") com um nicho novo de prova para divórcio/guarda ("Przestań się tłumaczyć. Pokaż daty.", "Co zanieść adwokatce na pierwsze spotkanie?").
- `currency` é a moeda da CONTA de anúncios, não a do preço.

## 2. Por vendedor: anúncios mais antigos ainda ativos x novos

**Como ler.** O conector só devolve o título do link (`ad_creative_link_title`), a data de criação, a data de início de veiculação e a moeda. Ele NÃO devolve o texto do corpo, o vídeo, a imagem nem o botão. Para saber o que está no CORPO, usei "sondagem por palavra": busca com `page_ids` + `search_terms`; o anúncio só volta se a palavra estiver no texto (ex.: "Safeguarding" trouxe anúncios com título "Key Rings"). Sinais de formato que dá para ler no título:
- título repetido 2–6 vezes com " | " = o anúncio tem várias versões (formato flexível / variações de mídia);
- títulos diferentes em sequência ("Produto A | Produto B | ...") = carrossel ou coleção com vários cards;
- `{{product.name}}` = anúncio de catálogo (Advantage+ catálogo);
- `default_collection_headline` = formato Coleção;
- título vazio = anúncio sem headline de link (comum em clique-para-WhatsApp e em vídeo sem título) → VERIFICAR.
- **Duração do vídeo, gancho dos 3 primeiros segundos e CTA: VERIFICAR em todos** (Biblioteca em HTML bloqueada: facebook.com não resolve neste container).

### 2.1 Childminder Resource Hut (UK, GBP) — 485,6 d, 35 anúncios, 23 com 90+ d
**Mais antigos ainda ativos (90+ d):**
| Início (dias) | Título do link | Formato (pelo título) | Corpo (sondagem) |
|---|---|---|---|
| 01/07/2025 (485,6) | "Safeguarding Simplified!" | 2 versões | "Safeguarding" no título; NÃO contém "Ofsted" |
| 02/02/2026 (269,4) | "IN STOCK NOW!" | 4 versões (produto físico) | — |
| 04/02/2026 (267,9) | "NEW 2025 Early Years Inspection Pack" ×3 + "Today's Fruit" + "Eat Your Veggies - Display" | carrossel: pack digital + displays físicos | contém "Ofsted" |
| 10/02/2026 (261,7) | "DOWNLOAD NOW!!" | 1 | — |
| 12/02/2026 (259,8) | "Learning Fans - Pack | Pocket Pathway - Development Matters | 7 Features of Effective Practice | ... | British Values & Cultural Capital" | carrossel de 6 produtos | — |
| 12/02/2026 (259,7) | "NEW 2025 Early Years Inspection Pack" ×3 + "Next Steps - Display" ×3 | carrossel | contém "Ofsted" |
| 13/02/2026 (258,7) | "Childminder Resource Hut | NEW 2025 EYFS!! | Safeguarding Reforms! | Instant Download | Create Your Own Folder | We Have Made it Simple!" | carrossel de 6 cards (cada card = uma promessa) | contém "Ofsted" e "Safeguarding" |
| 10/04/2026 (202,9) e 03/05 (179,4) | `{{product.name}}` ×11 | catálogo (Advantage+) | um deles contém "Ofsted" |
| 10/04/2026 (202,8) | "Safeguarding Simplified!" | **criado em 16/10/2025 e relançado em 10/04/2026** | contém "Safeguarding" |
| 13/04 e 25/05/2026 | "Key Rings" (chaveiros físicos) | 1 | contém "Safeguarding" e "Ofsted" |
| 10/05/2026 (173,0) | "NEW - Safe Sleep - Ultimate Compliance Pack - 2026" | 1 | — |
| 25/05/2026 (157,4) | "NEW - The Early Years Development Statement Bank" | 1 | — |
| 24/06/2026 (127,6) | "Trusted by 40,000+ Early Years Pros" | 1 | contém "Ofsted" |
| 24/06 e 25/06/2026 | "NEW! Inspection Ready - September 2026 - Action Plan & Guide" / "September 2026 READY!" | 1 cada | contém "Ofsted" |
| 15/07/2026 (106,6) | "🚨 EYFS 2026 Get the FREE Guide" | isca grátis | contém "Safeguarding" |
| 15/07/2026 (106,6) | "GET A PRINTED COPY!!" | 1 | contém "Safeguarding" |

**Novos (últimos 30 d):** 17/10 "NEW! The 2027 Childcare Calendar", "NEW - Safeguarding Decoded - The Ultimate A-Z", "Childminder Resource Hut"; 28/09 e 28/10 "Key Rings"; 20/09 "GRAB a printer copy…".
**Leitura:**
- O mais longevo (485 d) é uma promessa curta de SIMPLIFICAR a obrigação ("Safeguarding Simplified!"), sem data e sem citar Ofsted.
- Os de prazo ("EYFS 2026", "September 2026 READY!") vivem enquanto a norma é a assunto do momento (4+ meses) e são trocados pelo ano seguinte ("2027 Calendar").
- Ele NÃO desliga o que funciona: soma um produto "NEW" a cada 1–2 meses e deixa os antigos rodando (66% dos anúncios têm 90+ d).
- Relança criativo antigo: anúncios criados em 16/10/2025 e 02/02/2026 começaram a rodar de novo em abril e maio de 2026.
- Mistura digital + físico (chaveiros, displays, cópia impressa) e usa catálogo.
- 11 dos 35 corpos citam "Ofsted": o medo vai no corpo, a manchete fica no benefício.

### 2.2 Editura Gold (RO, RON) — ≥ 441,6 d, 280 anúncios
**Mais antigos achados (recortes por termo dentro da página):**
| Início (dias) | Título do link | Formato | Produto |
|---|---|---|---|
| 14/08/2025 (441,6) | "Copilul tău își ascunde emoțiile? Ajută-l cu o simplă poveste." ×4 | 4 versões | povești terapeutice (crianças) |
| 11/09/2025 (413,1) | "O poveste pe seară = un copil mai atent, mai încrezător și liniștit." ×3 (5 anúncios) | 3 versões | idem |
| criado 11/09/2025 → relançado 13/04/2026 e 04/07/2026 | "Copilul tău își ascunde emoțiile? Ajută-l cu o simplă poveste." | relançamento | idem |
| 30/12/2025 (303,6) | "📖 316 pagini cu sfaturi și rețete pentru dieta autoimună" ×2–4 | várias versões | dieta autoimune |
| 22/03/2026 (221,5) | "📘 Vindecă-ți trecutul printr-o experiență practică și personală" ×2–6 | várias versões | autoajuda |
| 13/05/2026 (169,6) | "Probleme cu inima și colesterolul? Cartea asta te poate ajuta" ×2–3; "📉 Carte: 10 metode prin care reduci natural colesterolul" | várias versões | colesterol |
| 23/05/2026 (159,2) | "Medicii omit 2 analize importante pentru tiroidă. Află care sunt!" ×2–3; "🦋 Pentru persoanele cu probleme la tiroidă" | várias versões | tiroide |

**Novos (out/2026):** carrosséis "Editura Gold | <benefício 1> | <benefício 2> | ..." com 6–7 cards (ex.: "21 povești și lecții prețioase | „Nox, prietenul care aduce liniște” | ..."; "Nu renunța la ouă și lactate | Încearcă 111 rețete sățioase | Primești un meniu de 7 zile | ..."), formato Coleção (`default_collection_headline`, 01–07/10), carrossel multi-produto ("Povești Terapeutice ... | 111 Rețete pentru Ficat Gras | Salvează-mi tiroida! | Colesterolul sub control | 366 Povești de Seară | Eu pe cine aleg?"), e nichos novos: gramática da 5ª série para PROFESSORES ("Pentru profesori: predă gramatica folosind o metodă inovativă", "Manual auxiliar scris de o profesoară"), ansiedade, divórcio.
**Leitura:**
- Ganchos que duram 300–440 d: pergunta ao pai/mãe + solução simples ("Seu filho esconde as emoções? Ajude com uma história simples"); equação ("Uma história por noite = criança mais atenta"); número concreto ("316 páginas", "10 métodos", "2 exames que os médicos esquecem").
- Os novos trocam a manchete única por carrossel em que cada card é um benefício: o "body" vira cards.
- Volume enorme (280) e reaproveitamento: criativo de set/2025 relançado em 2026.
- Preço e formato (livro físico ou e-book): VERIFICAR (edituragold.ro não resolve neste container).

### 2.3 Qualitiva Soluciones (CO, COP) — 276,0 d, 32 anúncios, 10 com 90+ d
**Mais antigos (90+ d):** 26/01/2026 (276 d) ×2 sem título (corpo contém "visita"); 29/01 a 01/02/2026 (270–274 d): "Documentos listos para adaptar" ×5 (um contém "WhatsApp") + 2 sem título; 09/04/2026 (203 d) "Agenda tu diagnóstico hoy".
**Quase 90 d:** 01/08/2026 (89,8 d) "Agenda tu diagnóstico hoy" ×3.
**Novos:** 25–29/08 "Audita HC y mide adherencia a GPC" ×2; 02/09 e 24/09 "Documentos listos para adaptar"; 05/10 e 24/10 "Evalúa tu cumplimiento de la Resolución 3100" (corpo com "visita" e "WhatsApp"); 26/10 "👩‍⚕️ Curso Express de Habilitación IPS este sábado" (WhatsApp); 14/10, 19/10 e 28/10 carrossel "Qualitiva Soluciones | | | | | | |" (7–8 cards sem título); vários sem título.
**Leitura:**
- O criativo de 9 meses é a promessa simples "Documentos listos para adaptar" (esforço/tempo). O medo da visita de habilitação aparece no CORPO (10 de 32 citam "visita").
- Os novos sobem a escada: autoavaliação da Res. 3100 → diagnóstico → auditoria de prontuário → curso com data ("este sábado"). O kit é a porta de entrada.
- Fechamento por WhatsApp em 5 de 32.

### 2.4 Abogados de Éxito (MX, MXN) — 273,2 d, 34 anúncios, 6 com 90+ d
**Mais antigos (90+ d):** 29/01/2026 (273 d) sem título (corpo cita "oral"); 07/02 (265 d) e 12/02 (260 d) sem título; 31/03 (212 d) sem título; 29/05 (153 d) "Domina el proceso civil oral" e "CURSO DE REDACCIÓN JURÍDICA".
**Novos:** 14/10/2026: **19 anúncios "Garantizamos tu aprendizaje." criados no mesmo quarto de hora** (teste em volume de várias mídias com a mesma manchete); 16–17/10 "Paso a paso y desde cero." + 4 sem título; 09/10 ×2 sem título.
**Leitura:**
- **Os 34 corpos contêm "WhatsApp"**: o funil é conversa (provável clique-para-WhatsApp; os títulos vazios reforçam). VERIFICAR o botão.
- 19 de 34 citam "oral": o tema que sustenta a página desde janeiro é o processo oral.
- O longevo promete uma HABILIDADE específica ("Domina el proceso civil oral"); os novos testam redução de risco ("Garantizamos tu aprendizaje") e facilidade ("Paso a paso y desde cero").

### 2.5 OpoEsquemas (ES, EUR) — 149,3 d, 3 anúncios, 3 com 90+ d
- Os 3 anúncios são o MESMO carrossel de 5 produtos: "Cuaderno Resúmenes (MEGARESUMIDO) Administrativo del Estado | Libro Tests Auxiliar Administrativo del Estado | Libro Tests Administrativo del Estado | Temario Auxiliar Administrativo Estado 2024 | Curso FOCUS AGE (Administrativo)".
- Criados em 02/06 e 10/06/2026; um deles relançado em 23/06 e outro em 04/08. Nenhum criativo novo desde então.
- **Leitura:** catálogo em carrossel com verba baixa roda 5 meses sem troca. O ano velho no título ("Temario ... 2024") não matou o anúncio. Preço: VERIFICAR (busca web não achou a loja; referência de mercado: temário PDF AGE de outro vendedor a 59 €, preparaoposiciones.com).

### 2.6 Care Daily (UK, GBP) — 132,1 d, 8 anúncios, 7 com 90+ d
- **Lote de lançamento 19/06/2026 (132 d), 6 anúncios criados no mesmo minuto, TODOS ainda ativos**, cada um com 4 versões da mesma manchete:
  - "You didn't start a care agency to do admin."
  - "Equip your carers. Keep your carers."
  - "Supported living policies. Not adapted. Written."
  - "Replace the folder. Start fresh."
  - "The children can't wait. Your policies shouldn't either."
  - "Your records deserve better than a ring binder."
- 21/06 (131 d) "Domiciliary care policies, ready to customise" (o único corpo que cita "CQC").
- 17/08 (73 d) "Your records deserve better than a ring binder." (versão única). Nada novo desde agosto.
- **Leitura:** frases curtas de identidade/dor, uma por segmento (domiciliar, supported living, lar de crianças), e o inimigo é a PASTA ("ring binder", "Replace the folder"). Nenhum anúncio do lote foi desligado. Ponto em aberto: "records deserve better than a ring binder" sugere que o produto pode ser software de registros, não só kit → VERIFICAR (busca web não achou o site).

### 2.7 Kit Studio Blindato - APP (IT, conta USD) — 42,8 d, 28 anúncios
- **Mais antigo:** 17/09/2026 "🦷 Tutte le carte del tuo studio, già pronte"; depois 29/09 "Stampa solo quello che ti serve".
- **Lotes:** 05–07/10 (6× "⭐⭐⭐⭐⭐ 4,9/5"), 09/10 ("Stampa solo...", "Ogni foglio della giornata, pronto"), 21/10 (11: "4.9/5 · Kit Studio Blindato · 4,9 su 5", "4.9/5 · Stampa solo quello che ti serve", "Ogni foglio...", "Tutte le carte..."), 23–25/10 (5× "⭐⭐⭐⭐⭐ 4.9/5 · 🦷 Tutte le carte del tuo studio, già pronte").
- **Corpo:** "ispezione" aparece em 1 de 28; "NAS", "garanzia", "tempo" e "19,99" em nenhum.
- **Leitura:** o que vive mais é o benefício "tudo pronto" + "imprima só o que precisa". Depois ele colou nota 4,9/5 na manchete. **Não usa norma nem fiscalização**: é exatamente a nossa brecha (Lazio DGR 669/2026, curso do datore, multas do separador de amálgama e do controle de qualidade do Rx).

### 2.8 Kit di Documenti Psicologici (IT, conta USD) — 36,0 d, 35 anúncios
- **Mais antigos:** 23–24/09/2026 "Oltre 270 documenti per psicologi 📄".
- **Lotes:** 06–07/10 (8× "⭐⭐⭐⭐⭐ 4,9/5"), 21/10 (7: "Oltre 270 documenti..." + "4,9/5"), 22–26/10 (≥ 18× "⭐⭐⭐⭐⭐ 4.9/5 · Kit di Documenti Psicologici · 4,9 su 5").
- **Corpo:** "privacy" em 1 de 35.
- **Leitura:** o NÚMERO de documentos é o gancho que mais dura; a nota 4,9/5 virou o padrão dos lotes novos. Nenhum gancho de norma (a nossa: divulgação de uso de IA, L.132/2025).

### 2.9 Kontrola Sanepidu (PL, PLN) — 28,5 d hoje, 12 anúncios
- 01/10/2026: "Procedury bez pisania od zera" ×4 e "Sprawdź, czego brakuje w salonie".
- 06/10 e 17/10: "Sprawdź, czego brakuje w salonie" (criados em 01/10 e relançados).
- 15–16/10: "Procedury z 12-miesięczną gwarancją" ×2 e carrossel "Kontrola Sanepidu | Aktualizacja na 2027" ×4.
- 28/10: "Sprawdź, czego brakuje w salonie".
- Corpo com "kontroli": 4 de 12.
- **Leitura:** quatro ângulos: (1) sem escrever do zero; (2) autoauditoria "veja o que falta no salão"; (3) garantia de 12 meses; (4) atualização para 2027. O clone Sophie Collins (USD) entrou em 23–25/10 com "Procedury gotowe do wywieszenia" (procedimentos prontos para pendurar), "Wszystkie terminy na cały rok" (todos os prazos do ano numa folha) e "Twoje logo na każdej kartce" (seu logo em cada folha).

## 3. Padrões por nicho/país

(em preenchimento)

## 4. 9 testes (3 hooks × 3 bodies) por oferta nossa

(em preenchimento)

## 5. Ranking 0–10

(em preenchimento)

## 6. VERIFICAR

(em preenchimento)
