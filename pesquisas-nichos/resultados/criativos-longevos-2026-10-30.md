# Criativos que sustentam 90+ dias — v2 (30/10/2026)

> **Avisos de ambiente**
> - A v1 (29/10) e os arquivos do Desktop **não estavam acessíveis** neste ambiente (container na nuvem). Esta versão foi feita do zero, com as notas do usuário (`notas/*.md`) e os page_ids já medidos pelos agentes irmãos em `resultados/` como ponto de partida.
> - **SearchAPI indisponível** (sem chave neste container e créditos zerados até 08/11/2026). Toda medição foi feita com o **conector Meta** (`ads_library_search`, só anúncios ATIVOS).
> - DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` da busca por page_id. Limite do conector: devolve no máximo 50 anúncios, do mais novo para o mais antigo; em página com >50 ativos o "mais antigo" é um piso (≥).
> - **Limite do método para criativos:** neste conector o resultado traz só o TÍTULO do link, as datas de criação e de veiculação, a moeda e o link do snapshot. Ele NÃO traz o corpo, o vídeo/imagem, a duração nem o botão (CTA). Para inferir o corpo usei "sondagem por palavra" (`page_ids` + `search_terms`); o formato foi lido pelos sinais do título (ver seção 2). Formato exato, duração, gancho dos 3 primeiros segundos e CTA ficaram VERIFICAR.
> - **Rede:** WebFetch barrado (host não resolve) em www.facebook.com (Biblioteca de Anúncios em HTML), childminderresourcehut.co.uk e edituragold.ro; agentes irmãos registraram o mesmo para hotmart, payhip, kiwify, lovable e outros. Para liberar: configurações do ambiente na nuvem → Network access → Allowed domains. WebSearch funcionou, mas não achou as lojas/preços dos vendedores.
> - Nenhuma compra feita e nenhum formulário preenchido.

## 0. Status da gravação
- [x] Lista de vendedores e page_ids
- [x] Medição por page_id (dias, nº anúncios, moeda)
- [x] Anúncios mais antigos x mais novos por página (pelo título + sondagem de corpo)
- [ ] Páginas de vendas (preço, plataforma, bumps, garantia): BLOQUEADO pela rede → VERIFICAR
- [x] Padrões por nicho/país
- [x] 9 testes (3 hooks × 3 bodies) por oferta nossa (8 ofertas)
- [x] Ranking 0–10
- [x] Lista final VERIFICAR

## Resumo
- **Só 6 dos 9 vendedores têm hoje anúncio ativo com 90+ dias:**
  - Childminder Resource Hut (UK): 485,6 d; 23 de 35 anúncios com 90+ d.
  - Editura Gold (RO): ≥ 441,6 d; 280 anúncios.
  - Qualitiva (CO): 276,0 d.
  - Abogados de Éxito (MX): 273,2 d.
  - OpoEsquemas (ES): 149,3 d.
  - Care Daily (UK): 132,1 d.
- **Os outros 3 não chegam a 90 d hoje:** Kit Studio Blindato 42,8 d, Kit di Documenti Psicologici 36,0 d e Kontrola Sanepidu 28,5 d.
- **O que faz um criativo durar:**
  - manchete de BENEFÍCIO simples e sem data ("Safeguarding Simplified!", "Documentos listos para adaptar");
  - medo/norma no CORPO;
  - vencedor nunca desligado;
  - criativo velho relançado;
  - várias versões de mídia por anúncio;
  - carrossel/catálogo quando há vários produtos.
- **Ganchos de ano/norma duram ~4 meses** e são trocados pelo ano seguinte.
- **Brecha direta nas nossas ofertas italianas:** os concorrentes IT (mesmo operador, conta USD) NÃO usam norma nem fiscalização. "Ispezione" aparece em 1 de 28 corpos; "privacy" em 1 de 35.
- **Top do ranking de testes:**
  1. Valigetta Dentista IT: 8,5.
  2. Jornada MX: 8,0.
  3. Psicólogo IT: 8,0.
  4. Dentista CO: 7,5.
  5. Maletín Psicólogo MX: 7,0.
- **Diferença para a v1:** não dá para comparar (v1 inacessível).

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
| 12/02/2026 (259,8) | "Learning Fans - Pack \| Pocket Pathway - Development Matters \| 7 Features of Effective Practice \| ... \| British Values & Cultural Capital" | carrossel de 6 produtos | — |
| 12/02/2026 (259,7) | "NEW 2025 Early Years Inspection Pack" ×3 + "Next Steps - Display" ×3 | carrossel | contém "Ofsted" |
| 13/02/2026 (258,7) | "Childminder Resource Hut \| NEW 2025 EYFS!! \| Safeguarding Reforms! \| Instant Download \| Create Your Own Folder \| We Have Made it Simple!" | carrossel de 6 cards (cada card = uma promessa) | contém "Ofsted" e "Safeguarding" |
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
- Os de prazo ("EYFS 2026", "September 2026 READY!") vivem enquanto a norma é o assunto do momento (4+ meses) e são trocados pelo ano seguinte ("2027 Calendar").
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

### 3.1 Regras que aparecem em quase todos os longevos
1. **A manchete que dura é um benefício simples, sem data.** Exemplos:
   - "Safeguarding Simplified!" (485 d);
   - "Copilul tău își ascunde emoțiile? Ajută-l cu o simplă poveste." (442 d);
   - "Documentos listos para adaptar" (274 d);
   - "Tutte le carte del tuo studio, già pronte" (o mais velho do Blindato, 43 d);
   - "Oltre 270 documenti per psicologi" (o mais velho do Psicologici, 36 d).
2. **O medo (inspeção, visita, multa) vai no CORPO, não na manchete.** Childminder: 11 de 35 corpos citam Ofsted. Qualitiva: 10 de 32 citam "visita". Kontrola: 4 de 12 citam "kontroli".
3. **Gancho com ano/norma vive enquanto a norma é notícia (~4 meses) e é trocado pelo ano seguinte.** Ex.: "September 2026 READY!" (127 d) → "The 2027 Childcare Calendar" (out/2026); "Aktualizacja na 2027" (Kontrola).
4. **Vencedor não é desligado; lote novo entra por cima.** Care Daily: 6 de 6 do lote de 19/06 seguem ativos. Childminder: 23 de 35 têm 90+ d.
5. **Criativo velho é relançado (data de criação meses antes da veiculação).**
   - Childminder: criado em 16/10/2025, relançado em 10/04/2026.
   - Editura Gold: criado em 11/09/2025, relançado em 13/04 e 04/07/2026.
   - OpoEsquemas: criado 10/06, relançado 23/06 e 04/08.
   - Kontrola: criado 01/10, relançado 06/10 e 17/10.
6. **Várias versões dentro do mesmo anúncio** (manchete repetida 2–6×): Care Daily (×4 em todos), Editura Gold (×2–6), Childminder (×2–4).
7. **Carrossel/catálogo para quem tem vários produtos.** OpoEsquemas vive 149 d com 1 carrossel de 5 produtos. Childminder tem catálogo de 203 d. Editura Gold migrou em out/2026 para carrosséis em que cada card é um benefício (o "body" vira cards).
8. **Escada de produto atrás do anúncio longevo.** Qualitiva: kit → autoavaliação → diagnóstico → auditoria → curso com data. Childminder: kit digital → cópia impressa → físicos → calendário anual.

### 3.2 Por país / nicho
| País / nicho | Vendedor longevo | O que sustenta | O que é novo (out/2026) | Lição para nós |
|---|---|---|---|---|
| UK / early years | Childminder Resource Hut (485 d) | "Simplified", "NEW <produto> <ano>", Ofsted no corpo, catálogo, físico + digital, isca grátis "EYFS 2026 FREE Guide" | produtos 2027 (calendário), "Safeguarding Decoded A–Z" | 1 produto novo por mês, sem desligar os antigos; ano da norma no nome do produto |
| UK / care agencies | Care Daily (132 d) | 6 frases curtas de identidade/dor, uma por segmento, inimigo = a pasta | nada desde 17/08 | uma manchete por SUBSEGMENTO da profissão; "a pasta" como vilão |
| RO / livros de saúde e família | Editura Gold (≥ 442 d) | pergunta ao pai/mãe + solução simples; equação "1 história/noite = criança mais calma"; número exato; "os médicos esquecem 2 exames" | carrossel de benefícios, Coleção, nicho professor | número + autoridade omitida ("o que o fiscal pede e ninguém te conta") |
| CO / habilitação saúde | Qualitiva (276 d) | "Documentos listos para adaptar" + "visita" no corpo + WhatsApp | autoavaliação Res. 3100, curso "este sábado" | kit como porta de entrada; checklist de visita como 2º ângulo |
| MX / advogado | Abogados de Éxito (273 d) | habilidade específica ("Domina el proceso civil oral"); WhatsApp em 34/34 | 19 criativos num dia com "Garantizamos tu aprendizaje", "Paso a paso y desde cero" | no MX, testar fechamento por WhatsApp e garantia na manchete |
| ES / oposições | OpoEsquemas (149 d) | 1 carrossel de catálogo, verba baixa, sem troca | nada | carrossel de catálogo aguenta meses sem refresh |
| IT / dentista e psicólogo (operador estrangeiro) | Blindato (43 d), Psicologici (36 d) | "tutto già pronto", "stampa solo quello che ti serve", número de documentos | nota "4,9/5" na manchete em todos os lotes | **nenhum usa norma/fiscalização** (1 corpo em 28 cita "ispezione"; 1 em 35 cita "privacy") → nosso diferencial |
| PL / salão (sanepid) | Kontrola Sanepidu (28 d) | sem escrever do zero; "veja o que falta no salão"; garantia 12 meses; "Aktualizacja na 2027" | clone Sophie Collins (USD): "Procedury gotowe do wywieszenia", "Twoje logo na każdej kartce" | autoauditoria e "pronto para pendurar na parede" são ângulos copiáveis |

### 3.3 O que NÃO deu para ver (limite do método)
- Vídeo x imagem, duração, os 3 primeiros segundos, texto do corpo completo e botão (CTA) de cada anúncio: VERIFICAR abrindo os `ad_snapshot_url` num navegador com acesso ao facebook.com (ex.: https://www.facebook.com/ads/library/?id=1903735520425764 para o "Safeguarding Simplified!" de 485 d).

## 4. 9 testes (3 hooks × 3 bodies) por oferta nossa

**Estrutura igual para todas as ofertas** (cada teste = 1 hook × 1 body; 3 × 3 = 9 anúncios):
- **H1, benefício sem data** (regra 3.1-1; o tipo que dura 270–485 d).
- **H2, norma/fiscalização com data ou multa** (regra 3.1-3; vida útil ~4 meses; trocar o ano em jan/2027).
- **H3, identidade/dor numa frase** (padrão Care Daily, 132 d sem troca).
- **B1, "pronto + número + imprima só o que precisa"** (padrão Blindato/Qualitiva/Childminder).
- **B2, autoauditoria: checklist no app + a norma/multa NO CORPO** (padrão Childminder/Qualitiva/Kontrola).
- **B3, carrossel de 6 cards, cada card um benefício; último card = preço/garantia; na LATAM, versão com fechamento por WhatsApp** (padrão Editura Gold novo, OpoEsquemas, Abogados de Éxito).

**Proposta de 3 primeiros segundos (NÃO observado nos concorrentes; vídeos não acessíveis):** para H1, a pasta de papéis bagunçada → o celular com o app; para H2, a tela do checklist marcando o item que falta, com a data/multa na legenda; para H3, o profissional atendendo e o texto da frase de identidade.

**Regras de operação tiradas dos longevos:**
- não desligar vencedor;
- lote novo entra por cima;
- relançar (duplicar) o vencedor a cada 60–90 d;
- 2–4 versões de mídia dentro de cada anúncio;
- nota/estrela na manchete SÓ se houver avaliação real. Os concorrentes IT usam "4,9/5", mas isso só tem 3–4 semanas de vida, não é prova de longevidade.

### 4.1 La Valigetta del Dentista (IT, €27/€19) — concorrente: Kit Studio Blindato (43 d, sem gancho de norma)
- **H1:** "Lo studio in regola, senza scrivere niente da zero." *(PT: o consultório em dia, sem escrever nada do zero)*
- **H2:** "Separatore di amalgama mancante: sanzione da 4.000 a 20.000 €. Il tuo studio è a posto?" *(multa das notas 28/10, BASE-LEGAL-IT)*.
  - Variante só para o Lazio: "Sedazione in studio: nel Lazio serve l'autorizzazione entro il 07/02/2027 (DGR 669/2026)."
- **H3:** "Hai aperto uno studio per curare i denti, non per compilare moduli."
- **B1:** "Consensi, schede, registri e protocolli già pronti: [N] documenti + app. Metti il tuo logo e stampi solo quello che ti serve." *([N] = nº real do nosso kit, VERIFICAR)*
- **B2:** "Check dello studio in 10 minuti: l'app ti mostra cosa manca. Registro del controllo di qualità RX (sanzione 6.000–12.000 €), separatore di amalgama, corso datore di lavoro 16 h entro il 24/05/2027, ECM con il 15% di radioprotezione. Ogni voce ha il suo modulo pronto."
- **B3 (carrossel):** "Consensi informati pronti | Registri obbligatori | Scadenze 2027 in un foglio | Tutto nell'app | Il tuo logo su ogni foglio | [preço vigente: €19 ou €27, VERIFICAR] una sola volta"
- **Não usar:** RENTRI (não se aplica mais ao estúdio individual, L.199/2025).

### 4.2 Psicólogo Itália (kit + app) — concorrente: Kit di Documenti Psicologici (36 d, "Oltre 270 documenti", sem norma)
- **H1:** "Consensi, privacy e cartelle: tutto pronto, con il tuo nome sopra."
- **H2:** "Usi l'intelligenza artificiale nello studio? Con la L. 132/2025 il paziente va informato. Hai già il modulo?" *(gancho das notas 28/10; artigo e redação exata: VERIFICAR na BASE-LEGAL-IT do psicólogo)*
- **H3:** "Hai studiato per ascoltare le persone, non per scrivere moduli."
- **B1:** "[N] modelli pronti (consenso informato, informativa privacy, anamnesi, piano di trattamento, informativa sull'uso dell'IA) + app. Stampi solo quello che ti serve."
- **B2:** "Checklist dello studio in 10 minuti: l'app ti dice cosa manca e ti dà il modulo." *(lista de obrigações: usar só o que estiver confirmado na BASE-LEGAL-IT, VERIFICAR)*
- **B3 (carrossel):** "Informativa IA (L. 132/2025) | Consenso informato | Privacy | Cartella clinica | Tutto nell'app | [preço] una sola volta"
- **Diferença para o concorrente:** ele vende QUANTIDADE ("270 documenti"); nós vendemos a norma nova + app. Testar também "Oltre [N] documenti, già aggiornati alla L. 132/2025" (número + norma no mesmo título).

### 4.3 Maletín del Psicólogo (México) — já no ar (criativos mx01–mx05, conteúdo não acessível aqui)
- **H1:** "Tu consultorio en orden: formatos listos para adaptar." *(estrutura do anúncio de 274 d da Qualitiva)*
- **H2:** "¿Tu expediente clínico aguantaría una queja?" *(sem citar NOM até confirmar se a NOM-004-SSA3-2012 se aplica ao psicólogo: VERIFICAR)*
- **H3:** "No estudiaste psicología para hacer papeleo."
- **B1:** "[N] formatos listos + app: consentimiento informado, aviso de privacidad, notas de sesión, plan de tratamiento. Imprime solo lo que necesitas."
- **B2:** "Revisa en 10 minutos qué le falta a tu expediente: checklist en la app y el formato listo para cada punto."
- **B3 (carrossel + WhatsApp):** 6 cards de benefício. Testar duas versões:
  - fechamento direto no checkout;
  - "¿Dudas? Escríbenos por WhatsApp" (Abogados de Éxito tem WhatsApp nos 34 corpos e roda há 273 d no MX).

### 4.4 Termometro 85k (IT, forfettario) — referência: Simple Budget Excel (página de 620 d; gancho "Non superare gli 85k" com 67 d, relatório irmão de funil)
- **H1:** "Il tuo forfettario sotto controllo, in una schermata."
- **H2:** "Dal 1° gennaio 2027 il forfettario passa al nuovo TUIR (D.Lgs. 117/2026). Sai già quanto puoi ancora fatturare?"
- **H3:** "Secondo anno da forfettario? Saldo e acconto al 100% arrivano insieme. Li hai messi da parte?"
- **B1:** "Inserisci le fatture: vedi quanto ti manca a 85.000 € (e a 100.000 €) e quanto accantonare tra imposta (15% o 5%) e INPS."
- **B2:** "Il calendario 2026–2027 delle scadenze con promemoria, più il bollo da 2 € sulle fatture." *(limite do bollo: VERIFICAR)*
- **B3 (carrossel):** "Quanto manca a 85k | Quanto accantonare | Secondo anno senza sorprese | Scadenze 2027 | Sul telefono | Strumento di calcolo indicativo, non costituisce consulenza fiscale"

### 4.5 Agenda Verde (PT, recibos verdes) — mesmo motor do Termometro; nenhum vendedor medido nesta pesquisa
- **H1:** "Os seus recibos verdes organizados num só sítio."
- **H2:** "Sabe quanto ainda pode faturar este ano sem perder a isenção de IVA?" *(limite do art. 53.º do CIVA para 2026: VERIFICAR antes de pôr número)*
- **H3:** "Não passou a trabalhar por conta própria para ter medo das Finanças."
- **B1:** "Passe cada recibo e veja quanto guardar para IRS e Segurança Social." *(taxas: VERIFICAR)*
- **B2:** "Calendário de obrigações 2026–2027 com lembretes." *(datas: VERIFICAR)*
- **B3 (carrossel):** 6 cards de benefício. Preço de referência PT: €4,90–14,90 (notas 28/10).

### 4.6 Registro de Jornada México (PyME e contador) — prazo 01/01/2027; nenhum kit de formatos visto (relatório irmão advogado-contador)
- **H1:** "Control de asistencia listo: formatos y app, sin empezar de cero."
- **H2:** "Desde el 1 de enero de 2027 el registro electrónico de jornada es obligatorio. ¿Tu empresa ya lo lleva?" *(fonte: reforma da LFT no DOF de 01/05/2026, transitório 5º, confirmada por 4 fontes no relatório irmão; o código DOF 5786537 ainda é VERIFICAR)*
- **H3:** "Contador: en diciembre todos tus clientes te van a preguntar por la jornada 2027."
- **B1:** "Reglamento interior adaptado a 46 horas, formato de registro de jornada, aviso a los trabajadores y calculadora de horas extra 2027."
- **B2:** "Autodiagnóstico en 10 minutos: qué te falta para enero. La multa va de 250 a 5,000 UMA."
- **B3 (carrossel + WhatsApp):** 6 cards de benefício. Testar a versão com WhatsApp (padrão MX).
- **Janela:** lançar até meados de novembro. O H2 perde força depois de jan/2027; aí entra o H1.

### 4.7 Dentista Colômbia — referência: Qualitiva (276 d, "Documentos listos para adaptar")
- **H1:** "Documentos de habilitación listos para adaptar a tu consultorio odontológico."
- **H2:** "¿Te llega la visita de habilitación? Revisa en 10 minutos qué te falta (Res. 3100 de 2019)." *(NUNCA prometer a data da Res. 914, 03/01/2027: o MinSalud vai substituí-la)*
- **H3:** "Estudiaste odontología para atender pacientes, no para llenar formatos."
- **B1:** "Protocolos, consentimientos y formatos listos + app de bitácoras diarias."
- **B2:** "Checklist de la visita de habilitación + tutorial del REPS paso a paso."
- **B3 (carrossel + WhatsApp):** 6 cards de benefício.
- **Diferença para a Qualitiva:** ela vende para IPS e consultórios em geral e sobe para consultoria/curso. Nós somos o kit específico do dentista, com app.

### 4.8 Psicólogo Colômbia (versão curta) — referência: Psicólogo Organizado (176 d, relatório irmão)
- Reusar 4.7 trocando a profissão.
- **H2:** "Tu historia clínica se guarda 15 años (Res. 839 de 2017). ¿Está completa?" *(prazo de guarda das notas 29/10; redação: VERIFICAR)*

## 5. Ranking 0–10

### 5.1 Pacotes de 9 testes: qual oferta ganha mais com os padrões longevos (ordem para rodar)
Critério: concorrente PROVADO sem o ângulo que temos + força do gancho com data/multa confirmada + a oferta já estar na fila do usuário.

| # | Oferta | Nota | Régua | Por quê |
|---|---|---|---|---|
| 1 | La Valigetta del Dentista (IT) | **8,5** | PROVADO + PRAZO | Concorrente com 28 anúncios e 43 d só com "tudo pronto" + nota; 1 corpo em 28 cita inspeção. Temos multas e prazos confirmados (separador €4–20k, RX €6–12k, curso 16 h até 24/05/2027, Lazio 07/02/2027). 1ª da fila |
| 2 | Registro de Jornada (MX) | **8,0** | PRAZO + BRECHA | Prazo duro 01/01/2027, nenhum kit de formatos visto; no MX o padrão longevo é fechar por WhatsApp (34/34 no Abogados de Éxito). Lançar até meados de nov. |
| 3 | Psicólogo Itália | **8,0** | PROVADO + PRAZO | Concorrente com 35 anúncios e 36 d vende quantidade ("270 documenti"); ninguém usa a L. 132/2025 (IA). 2ª da fila |
| 4 | Dentista Colômbia | **7,5** | PROVADO | O anúncio "Documentos listos para adaptar" da Qualitiva tem 274 d; a "visita" está no corpo de 10 dos 32. Falta só o kit específico do dentista |
| 5 | Maletín del Psicólogo (MX) | **7,0** | PROVADO (relatório irmão: Psique y Ciencia 33 d, Recursos Legales PRO 98 d) | Já está no ar: os 9 testes entram como lote novo por cima de mx01–mx05, sem desligar nada |
| 6 | Termometro 85k (IT) | **6,5** | PROVADO (gancho "85k" com 67 d em página de 620 d) + PRAZO (novo TUIR 01/01/2027) | Gancho do 2º ano é forte; o concorrente é Excel a €69,97 |
| 7 | Psicólogo Colômbia | **6,5** | PROVADO (176 d) | Reusa 4.7; prazo de guarda de 15 anos ainda VERIFICAR |
| 8 | Agenda Verde (PT) | **5,0** | TESTE | Nenhum vendedor medido aqui; números da norma (limite de IVA, taxas) todos VERIFICAR |

### 5.2 Padrões criativos: força da evidência de longevidade
| # | Padrão | Nota | Evidência (dias reais) |
|---|---|---|---|
| 1 | Manchete de benefício simples, sem data ("Simplified", "listos para adaptar", "già pronte") | **9,0** | Childminder 485 d; Editura Gold 442 d; Qualitiva 274 d; o mais velho do Blindato e do Psicologici |
| 2 | Não desligar vencedor; somar lotes por cima | **8,5** | Care Daily 6/6 do lote vivos há 132 d; Childminder 23/35 com 90+ d |
| 3 | Relançar (duplicar) o criativo antigo | **8,0** | Childminder (out/2025 → abr/2026), Editura Gold (set/2025 → abr e jul/2026), OpoEsquemas, Kontrola |
| 4 | Medo/norma no CORPO, benefício na manchete | **7,5** | Ofsted em 11/35 (Childminder); "visita" em 10/32 (Qualitiva) |
| 5 | Ano da norma no gancho, trocado todo ano | **7,5** | "September 2026 READY!" 127 d → "2027 Calendar"; "Aktualizacja na 2027" |
| 6 | 2–6 versões de mídia por anúncio | **7,0** | Care Daily ×4; Editura Gold ×2–6 |
| 7 | Carrossel/catálogo multi-produto | **7,0** | OpoEsquemas 149 d; catálogo Childminder 203 d |
| 8 | Frase de identidade/dor por subsegmento | **6,5** | Care Daily 132 d |
| 9 | Fechamento por WhatsApp (LATAM) | **6,5** | Abogados de Éxito 34/34, 273 d; Qualitiva 5/32 |
| 10 | Isca grátis da norma ("FREE Guide") | **5,5** | Childminder "EYFS 2026 FREE Guide" 106 d |
| 11 | Nota "4,9/5" na manchete | **5,0** | só 3–5 semanas (Blindato/Psicologici); usar só com avaliação real |
| 12 | Garantia na manchete | **4,5** | Abogados 16 d, Kontrola 14 d; ainda sem prova de longevidade |

## 6. VERIFICAR

1. **Criativos em si (o pedido central):** formato (vídeo/imagem), duração, gancho dos 3 primeiros segundos, corpo completo e CTA dos anúncios longevos. Precisa abrir os `ad_snapshot_url` com acesso a facebook.com (bloqueado aqui). IDs prioritários:
   - 1903735520425764 e 26641118152245663 (Childminder, "Safeguarding Simplified!", 485 d);
   - 1475189860484430 e 714873231606916 (Editura Gold, 442 e 413 d);
   - 1775994443070987 e 4282667305301672 (Qualitiva, 274 e 276 d);
   - 1464440009019094 (Abogados de Éxito, 273 d);
   - 1410205870865315 (OpoEsquemas, 149 d);
   - 3467755123400186 e 2313042699224174 (Care Daily, 132 d);
   - 2156165774968058 (Blindato, 43 d);
   - 1041975655490252 (Psicologici, 36 d).
2. **Kontrola Sanepidu "90+ dias":** hoje o anúncio ativo mais antigo é de 01/10/2026 (28,5 d). Conferir com o SearchAPI depois de 08/11 (inclui inativos) se houve criativos de 90+ d que foram desligados. Mesma checagem para o "90+" atribuído a Kit Studio Blindato (42,8 d) e Kit di Documenti Psicologici (36,0 d).
3. **Editura Gold:** 280 anúncios. Só medi por recorte; o mais antigo real pode ser anterior a 14/08/2025. Também conferir se vende livro físico ou e-book e por quanto (edituragold.ro bloqueado).
4. **Preços, plataforma, bumps e garantia** de TODOS os 9 vendedores. Sites bloqueados (ENOTFOUND): childminderresourcehut.co.uk, edituragold.ro, facebook.com. A busca web não achou as lojas de Care Daily, Qualitiva, Kontrola Sanepidu, Abogados de Éxito nem OpoEsquemas. Preço do Blindato (€19,99) vem das notas de 28/10.
5. **Abogados de Éxito:** confirmar se os anúncios usam o botão clique-para-WhatsApp (os 34 corpos citam "WhatsApp"; os títulos vazios sugerem isso).
6. **Care Daily:** confirmar se é kit de políticas ou software de registros ("Your records deserve better than a ring binder").
7. **Nossas ofertas, números a pôr nos criativos:**
   - nº real de documentos de cada kit ([N] nos bodies);
   - preço vigente da Valigetta (€19 ou €27);
   - redação exata da obrigação da L. 132/2025 (psicólogo IT);
   - se a NOM-004-SSA3-2012 se aplica ao psicólogo no MX;
   - limite do bollo (IT);
   - limite de isenção de IVA do art. 53.º CIVA 2026 e taxas de IRS/SS (PT);
   - código DOF 5786537 (jornada MX);
   - redação da guarda de 15 anos (Res. 839/2017, CO).
8. **Sophie Collins (PL, conta USD):** clone multinicho que entrou em 23–25/10 (gabinete + divórcio/guarda). Re-checar em 12/11 e 27–28/11, junto com a Romênia.
9. **Conteúdo de mx01–mx05** (Maletín MX), para não duplicar ângulo nos 9 testes novos.
