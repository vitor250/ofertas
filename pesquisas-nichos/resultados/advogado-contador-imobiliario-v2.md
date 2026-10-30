# Advogado, contador e imobiliário por país (v2)

Data de referência: 30/10/2026. Gravado aos poucos.

## Resumo
- **Top 3:** (1) México, Kit "Jornada 2027" para PyME e contador, **8,0** (prazo 01/01/2027; o adjacente "Kit Reglamento Interno Inteligente" já roda há 34 d). (2) México, Kit do advogado para o juicio oral do CNPCF, **7,5** (Abogados de Éxito vende em MXN há 273 d; CNPCF automático em 01/04/2027). (3) Argentina, kit do advogado por área, **6,0**, empatado com Espanha, Kit do abogado "MASC obrigatório", **6,0** (brecha).
- Nenhum kit de DOCUMENTOS para advogado, contador ou agente imobiliário tem prova de 30+ dias em ES, IT, PT, CO ou CL. O que prova idade são cursos/manuais (MX) e o "reglamento interno" vendido a PyMEs (USD).
- A v1 não estava acessível; nenhuma página de vendas pôde ser aberta (rede bloqueada); a busca web esgotou no meio. Ver seção 6.

## Avisos de método
- A v1 (29/10, `advogado-contador-imobiliario.md`) NÃO estava acessível neste ambiente. Usei a lista de candidatos e os itens a confirmar escritos no próprio prompt.
- SearchAPI indisponível (sem chave aqui e sem crédito até 08/11). Medições feitas com o conector Meta (`ads_library_search`, só anúncios ATIVOS). DIAS REAIS = 30/10/2026 menos o menor `ad_delivery_start_time` entre os anúncios ativos da página.
- **Bloqueio de rede:** neste container o WebFetch e o curl NÃO alcançam nenhum site externo (facebook.com, boe.es, dof.gob.mx, stan.store, hotmart.com, até google.com e wikipedia deram ENOTFOUND/000). Por isso NENHUMA página de vendas pôde ser aberta diretamente. Preço/conteúdo só entram quando apareceram em trecho indexado pelo WebSearch (que funciona); o resto fica VERIFICAR. Normas e números foram confirmados via WebSearch com fonte oficial citada (URL), sem abrir o PDF.
- **Limite do conector Meta:** a busca por `page_ids` devolve no máximo 50 anúncios, sempre os MAIS NOVOS primeiro. Para páginas com mais de 50 anúncios ativos o "dias reais" é só um PISO (≥ X dias); o anúncio mais antigo fica invisível. O conector também não devolve o link de destino nem o texto do anúncio, só o título do link.
- Epoch de referência: 30/10/2026 00:00 UTC = 1793318400.

## 1. Vendedores (página de vendas + Biblioteca de Anúncios)

Medição no conector Meta em 30/10/2026, só anúncios ATIVOS, por `page_id`.

### 1.1 Advogados (espanhol)

| Vendedor (page_id) | País provável / moeda | Anúncios ativos | DIAS REAIS | Produto (título do link) | Página de vendas | Régua |
|---|---|---|---|---|---|---|
| **Abogados de Éxito** (1255927857876624) | México / MXN | 34 (todos visíveis) | **273 d** (mais antigo 29/01/2026); lotes novos 14/10 e 17–18/10 | "CURSO DE REDACCIÓN JURÍDICA" (desde 29/05), "Domina el proceso civil oral" (desde 29/05), "Paso a paso y desde cero", "Garantizamos tu aprendizaje" | Não aberta (rede bloqueada; busca web não achou o domínio). Preço VERIFICAR | **PROVADO MX** (curso/manual, não kit de documentos). O gancho "proceso civil oral" conversa com o CNPCF |
| **Manuales Jurídicos** (2171543346464337) | México / MXN | 72 | **≥ 8 d** (piso; 22 anúncios mais antigos invisíveis) | "Manual paso a paso y desde cero", "Explicación paso a paso", "Paso a paso y desde cero para su uso inmediato" | Não aberta. Preço VERIFICAR | Escala forte agora (13 criativos novos em 30/10). Mesmo título de link de Abogados de Éxito ("Paso a paso y desde cero") → provável MESMO operador abrindo 2ª página (VERIFICAR) |
| **Ratio Studio** (1227357643798350) | Argentina (ART, amparos de salud) / USD | **216** | ≥ 1,8 d (piso; 166 invisíveis) | "Guía Práctica de ART para Abogados", "...de Amparos de Salud", "...de Daños y Perjuicios", "...de Derecho de Familia", "...de Registro de Marcas" | Não aberta; busca web não achou. Preço VERIFICAR | Volume altíssimo, idade desconhecida → VERIFICAR com SearchAPI após 08/11. Coleção de guias por área (formato "1 área = 1 produto") |
| **Tubibliotecajuridica** (777997355400950) | Colômbia / COP | 3 | 2,3 d | Biblioteca jurídica (link para Instagram) | — | TESTE |
| **Rai Lomer** (100828309790367) | Espanha / EUR | 10 | 9,0 d | "Agente de IA para Abogados", "Expedientes sin perseguir", "Del email al borrador" | — | TESTE; é SaaS/serviço de IA, não kit |
| **Automatiza juridico** (1178070148732039) | México / conta em USD, preço em MXN | 25 (todos visíveis) | **0,8 d** (todos de 29/10) | "Claude para Abogados – Edición México": guia + 53 ferramentas + 8 bônus, **MXN 349 pagamento único, 10 dias de garantia**; a mesma página roda criativos para CONTADOR ("correo falso del SAT", "le pasaron una CIEC", "papeles del mes", "otro contador cobra menos") | Não aberta; preço e garantia lidos no título do anúncio | TESTE (nasceu ontem). Mostra o preço-âncora do MX para kit profissional: MXN 349 (~R$ 105) |
| **Dra. Catalina Leal** (801292493075440) | USD | 1+ | VERIFICAR | "Claude para Abogados" | — | TESTE |
| **Abogadologia** (322764450912522) | Argentina / ARS | 2 | 16,8 d (desde 13/10/2026) | "Pack Jurídico Argentino" | Não aberta; busca web esgotada antes de achar | TESTE (perto de virar prova; re-checar 13/11) |
| **Leg-TECH** (307460479128102) | Peru / PEN | 5 | **231,8 d** (desde 12/03/2026) | "RECLAMA TU BALOTARIO" (banco de questões de exame/concurso) + WhatsApp | — | PROVADO no Peru, mas nicho de EXAME (concurso), não kit de prática |
| **Braszka&Merkel** (531264847705050) | Argentina / ARS | 1+ visto | 153 d (anúncio de 29/05/2026) | "Sumate al curso mas completo" (curso) | — | Curso, fora do formato |
| Productos Digitales ANT, Escuela Jurídica (PEN), La 2da Ley (PEN), Instituto Castelar (ARS, diplomatura derecho inmobiliario) | — | — | ≤ 3 d nos anúncios vistos | cursos/ebooks | — | ruído/TESTE |

Busca "modelos de escritos judiciales abogados" em AR, CO, CL, PE: só 12 anúncios ativos no total. **Colômbia e Chile: zero kit de escritos para advogado** nessa busca → BRECHA (sem vendedor).

Busca de controle **Espanha** ("plantillas abogados escritos", país ES): só 2 anúncios no país (Rai Lomer e Catalina Leal), nenhum kit de documentos → **BRECHA ES** para kit de advogado.
Busca de controle **Itália** ("avvocati modelli", "kit avvocato", "commercialista modelli excel", país IT): só SaaS de IA (Trovanorma.it), webinars (Dirittodautore.it) e coaching de imobiliária (Titolare Top). Nenhum kit low ticket para avvocato ou commercialista → **BRECHA IT**.

### 1.2 "Reglamento interno" para PyMEs (jurídico-trabalhista, vendido a empregador)

| Vendedor (page_id) | Moeda | Anúncios ativos | DIAS REAIS | Produto | Régua |
|---|---|---|---|---|---|
| **Coach Augusto Jimenez** (103857225566410) | USD | 39 (todos visíveis) | **33,6 d** (desde 26/09/2026) | "Kit Reglamento Interno Inteligente" | PROVADO (≥30 d) mas em USD e espanhol neutro → **não prova país** |
| **Jime Bauer** (1167773503086017) | USD | 81 | ≥ 5,0 d (piso; 31 invisíveis) | "Reglamento Interno Inteligente: ordena tu negocio y despide con papeles", "+1.400 PyMEs ya lo usan" | Mesmo produto da página acima → mesmo operador com 2 páginas (VERIFICAR). Soma 120 anúncios ativos |

Leitura: o produto vende ao DONO de PyME (não ao advogado). Encaixa como adjacente do "Registro de jornada México" que já está na fila (mesmo comprador, mesma dor trabalhista). País não identificado: "despide con papeles" é genérico; VERIFICAR se o checkout/ moeda local aponta MX, CO, PE ou EC.

### 1.2b "Jornada 40 horas / registro de jornada" no México (comprador: PyME e contador)

Busca "jornada 40 horas", país MX: **142 anúncios ativos**. Nos 30 mais novos:
- **Capacita Plus** (855201231005670, MXN): 5 anúncios, TODOS de 30/10/2026 ("Reducción de la jornada laboral 2027", "De 48 a 46 horas en 2027 | Horas extra: doble y triple | Nómina y control de asistencia"). Curso. 0 dias.
- **DFP Company** (1877740239137659, MXN): 1 anúncio de 29/10 ("NUEVO REGLAMENTO LABORAL 2027"). 0,3 d.
- **Humand** (SaaS de RH, conta ARS): "Enero 2027: el registro de jornada ya es obligatorio".
- Canacintra Yucatán (câmara empresarial, oficina), Imec LAB (consultoria), Contador Mx ("ChatGPT e IA para calcular impuestos"), Despacho Contable S&A (serviço).
- Busca "registro de jornada 40 horas formatos" (MX): **0 anúncios**.

Leitura: a onda de conteúdo sobre 01/01/2027 começou AGORA (29–30/10). Há cursos, SaaS e consultoria; **nenhum kit low ticket de formatos** (reglamento interior adaptado, bitácora/registro de jornada, aviso aos trabalhadores, calculadora de horas extra 2027) visto. É PRAZO + BRECHA, janela de ~2 meses.

### 1.3 Imobiliário (espanhol)

| Vendedor (page_id) | Moeda | Anúncios | DIAS REAIS | Produto | Régua |
|---|---|---|---|---|---|
| **Organizagram** (322793330917707) | BRL (operador BR) | 11 anúncios com "Inmobiliario" (filtro page_id + termo) | **42,6 d** no "Pack Agente Inmobiliario" (desde 17/09/2026); último lote 20/10 | Pack de posts/artes para agente imobiliário em espanhol. No BR o mesmo operador vende "Pack Corretor de Imóveis" R$ 67,90 e "Pack Contabilidade Pro" (base EscalaLow 24/10) | PROVADO em espanhol (≥30 d), mas conta BRL e espanhol neutro → não prova país. É pack de marketing, não kit de documentos |
| **Educenter** (781213098400687) | PEN (Peru) | 30 (todos visíveis) | **338 d** (desde 26/11/2025) | Títulos genéricos ("ADQUIERE AQUÍ", "+ 1000 DESCARGAS", "CONTÁCTANOS"); apareceu na busca "plantillas agentes inmobiliarios" | Longevo no Peru, mas o PRODUTO não foi identificado (VERIFICAR: pode ser loja de plantillas multinicho) |

Busca "plantillas agentes inmobiliarios" (sem país): 29 anúncios ativos no total; o resto é software/CRM (Agent CRM, Inmoview), cursos de flipping (Peru) e coaching (Alejandro de Lobbie, COP). Nenhum kit de DOCUMENTOS (contrato de exclusividade, ficha de captação, checklist de due diligence) para agente imobiliário em espanhol → **BRECHA**.

Busca "agente inmobiliario plantillas contrato encargo" (ES) e "agente immobiliare modelli kit" (IT): **0 anúncios** → BRECHA nos dois.
Busca "consultor imobiliário modelos" (PT): 5 anúncios, só anúncios de imóveis e uma "Laura Martins" (EUR, 15 d, "Todo o seu trabalho, arrumado e à mão", produto VERIFICAR). Busca "minutas advogados modelos" (PT): **0** → BRECHA PT (mercado pequeno).

### 1.3b Contador (espanhol)

- Busca "contadores kit" (MX): 213 anúncios ativos; os mais novos são kits de PROMPTS de IA (Automatiza juridico MXN 349; Udemia.IA "Domina Claude en 7 días"), todos com ≤ 3 dias. Nenhum kit de DOCUMENTOS para despacho contable com ≥ 30 dias visto.
- Busca "plantillas para contadores" (MX, AR, CO, PE, CL, ES, EC): 78 anúncios; cursos (ICADEM, Cetec), "Eve Muriel Contadora" (ARS, curso "tu propio estudio contable"), lojas peruanas de plantillas com 1 anúncio de hoje (Emprende Fácil, Tienda Digital Perú). Nenhum PROVADO.
- Busca "contadores formatos plantillas excel" (CO, AR, CL): 1 anúncio (Guatemala). → BRECHA em CO/AR/CL.

### 1.4 Imobiliário (inglês)

| Vendedor (page_id) | Moeda | Anúncios ativos | DIAS REAIS | Produto | Página de vendas | Régua |
|---|---|---|---|---|---|---|
| **Kim Buckner Realtor/Coach** (233861516485778) | USD (EUA) | 4 | 3 anúncios de produto com 0,3–0,6 d (29–30/10); 1 anúncio sem título desde 04/04/2024 (938 d, provavelmente institucional, VERIFICAR) | "35 Agent Templates for $97", "Get 17 Years of Systems for $97", "Get the Collection. Get Your Saturdays Back." | Stan Store (trecho do Google): "ROOTED Exclusive: The Business Operating System" US$ 99 (de US$ 247), "sistemas de 17 anos como corretora, líder de imobiliária e coach". stan.store bloqueado aqui; conteúdo e bumps VERIFICAR | TESTE (o anúncio de US$ 97 nasceu ontem) |
| **Modern Agent Social Club** (285925431957367) | USD | 96 | ≥ 23,1 d (piso; 66 invisíveis) | Assinatura de posts para corretor ("Never wonder what to post again", "Meet your AI Brand Coach") | — | Concorrente de ASSINATURA, não kit; idade real VERIFICAR |
| **Tiny Tomato** (161177674439003) | CAD (Canadá) | 13 | 146 d | Branding/lead gen para realtor ("$5,988 Realtor Branding Discount") | — | Alto ticket, fora do formato |
| Elevated Agent, keys.and.kits, LocalLead | USD | poucos | 1–6 d | cartas do Papai Noel para clientes, kits, marketing mensal US$ 29 | — | TESTE/ruído |

Leitura EUA: mercado grande (1,44 mi realtors), mas o espaço de "templates para agente" já é ocupado por assinaturas e SaaS; o único kit low ticket (Kim Buckner, US$ 97) nasceu ontem.

## 2. Normas e prazos (fonte oficial)

Confirmado por WebSearch (o texto oficial não pôde ser aberto; ver aviso de rede). Fonte oficial citada quando o próprio buscador devolveu o domínio do governo.

| Norma | O que foi confirmado | Fonte | Status |
|---|---|---|---|
| **CNPCF – Código Nacional de Procedimientos Civiles y Familiares (MX)** | Decreto publicado no **DOF em 07/06/2023**. Vigência por declaratoria de cada Congresso (máx. 120 dias entre declaratoria e vigência). Sem declaratoria, entra **automaticamente em todo o país em 01/04/2027**. CDMX: declaratoria em 03/07/2024, entrada escalonada; supletória a partir de 15/11/2025 | ordenjuridico.gob.mx (wo124796, wo125098); síntese SCJN do DOF 07/06/2023 (scjn.gob.mx); declaratoria PJBC (transparencia.pjbc.gob.mx) | CONFIRMADO. Falta o mapa estado a estado de quem já tem data (VERIFICAR) |
| **Jornada de 40 h (MX) – reforma constitucional** | Decreto que reforma o art. 123 publicado no DOF em **03/03/2026** (segundo vários veículos; um fala em 01/05). Redução de 2 h/ano: 48 h (2026) → 46 (2027) → 44 (2028) → 42 (2029) → **40 h (2030)**, a partir de 01/01 de cada ano | cronica.com.mx 03/03/2026; politica.expansion.mx 04/03/2026; jdsupra | Data do DOF da reforma constitucional = VERIFICAR no dof.gob.mx (fontes divergem 03/03 x 01/05) |
| **Jornada de 40 h (MX) – reforma da LFT** | Decreto da Ley Federal del Trabajo publicado no **DOF de 01/05/2026** (edição vespertina). Transitório 2º: escala 48→40 h. Transitório 4º: horas extras de 9 (2026) para 12 (2030). **Transitório 5º: registro ELETRÔNICO de jornada obrigatório a partir de 01/01/2027** (art. 132, fr. XXXIV). Multa de **250 a 5.000 UMA** (art. 994, fr. IV Bis) | Pérez-Llorca (nota 05/2026), Deloitte Flash Legal, Tax Today México, AMCP-DF 05/05/2026, link DOF nota_detalle código 5786537 | CONFIRMADO por 4 fontes concordantes; código DOF 5786537 a conferir |
| **MASC Espanha – LO 1/2025, de 2 de janeiro** (eficiência do Serviço Público de Justiça) | Publicada no BOE em 03/01/2025, **vigente desde 03/04/2025**. Tentativa prévia de MASC (mediação, conciliação, oferta vinculante confidencial, etc.) é **requisito de procedibilidade** nos processos declarativos (livro II) e especiais (livro IV) da LEC (art. 5). Só vale para ações iniciadas após a vigência. Critérios judiciais ainda divergentes (ex.: monitório) | ICAM (web.icam.es), Tirant (dossier de unificação de critérios), Sepín, KPMG legal alert 06/2025, Audiencia Provincial de Barcelona (acordos 10/2025) | CONFIRMADO. Não há prazo futuro: é dor contínua (cada ação cível precisa do "papel do MASC") |
| **Cartabia (IT) – processo civil** | D.Lgs. 10/10/2022 n. 149 (lei delegada 206/2021) em vigor desde **28/02/2023**. "Correttivo" em vigor desde **novembro/2024** (D.Lgs. 164/2024, número citado pelo prompt; a busca confirmou o mês, não o número). Tribunal unificado para pessoas, menores e famílias em implantação progressiva desde 10/2024. Novidade 2026: D.L. 19/02/2026 n. 19, conv. L. 20/04/2026 n. 50, mexeu nos arts. 696 e 696-bis c.p.c. (fonte isolada) | italiaoggi.it, agendadigitale.eu, iusletter/Altalex, ficha editorial | Datas 2023/2024 CONFIRMADAS; nº do correttivo e o D.L. 19/2026 = VERIFICAR na Gazzetta/Normattiva. Não achei prazo NOVO de Cartabia em 2026–2027 que sirva de gancho |

Leitura dos prazos:
- **01/01/2027 (MX, registro eletrônico de jornada + 46 h)** é o prazo mais próximo e mais forte. O comprador é a PyME e o CONTADOR que faz a folha. Casa com o "Reglamento Interno Inteligente" que já roda há 34 dias (Coach Augusto Jimenez) e com o item "Jornada México" da fila do usuário.
- **01/04/2027 (MX, CNPCF automático)**: todo advogado cível/familiar do país passa ao rito oral nacional. Abogados de Éxito já vende "Domina el proceso civil oral" há 153 dias.
- MASC (ES) e Cartabia (IT) não têm prazo novo; servem como conteúdo do kit, não como gancho de urgência.

## 3. Tamanho de mercado (nº de advogados, contadores, corretores)

| País | Profissão | Número | Fonte | Status |
|---|---|---|---|---|
| México | Abogados (ocupados) | **445 mil** (2026-T1; 422 mil em 2025-T4); informalidade 21,8% | Data México / ENOE (economia.gob.mx/datamexico/es/profile/occupation/abogados) | CONFIRMADO |
| México | Contadores y Auditores (ocupação 2121) | **470 mil** (2026-T1; 441 mil em 2025-T4). Subgrupo 212 amplo: 534 mil | Data México (…/occupation/contadores-y-auditores) | CONFIRMADO |
| México | Agentes de Bienes Raíces (4223) | **103 mil** (2026-T1); informalidade 37,4%; CDMX 24,5 mil, Jalisco 11,7 mil, NL 6,1 mil | Data México (…/occupation/agentes-de-bienes-raices) | CONFIRMADO |
| Espanha | Abogados | **~149,7 mil ejercientes** e 237,2 mil colegiados (83 Colegios, censo início 2025) | Consejo General de la Abogacía via Legal Today (revista AJA nº 1.015, 27/02/2025) | CONFIRMADO (dado de 2025; censo fim-2025 não achado) |
| Itália | Avvocati | **228.641 inscritos na Cassa Forense em 2025** (211.464 ativos); 233.260 em 2024 | X Rapporto Censis/Cassa Forense 2026 (censis.it) | CONFIRMADO |
| Itália | Commercialisti | **119.050 inscritos no Albo no fim de 2025** (−0,8%) | Rapporto 2026 sull'Albo, Fondazione Nazionale Commercialisti / CNDCEC | CONFIRMADO |
| EUA | Realtors (NAR) | **1.438.569 membros** (junho/2026; 1.463.352 um ano antes) | nar.realtor (CEO Nykia Wright, Legislative Meetings 06/2026) | CONFIRMADO |

| Argentina | Abogados | ~126 mil (ESTIMATIVA de imprensa, Día del Abogado 08/2025); CPACF (CABA) "quase 90 mil matriculados" (El Cronista) x padrão eleitoral ~71 mil | diariojornada.com.ar; cronista.com | VERIFICAR (não é dado oficial) |
| Colômbia, Chile, Peru, Portugal | Advogados/contadores | não confirmado (orçamento de busca web esgotou) | — | VERIFICAR |

## 4. Ranking 0–10 por país/nicho

Régua do prompt: PROVADO = vendedor com anúncio ativo há 30+ dias NO país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = norma com data; BRECHA = ninguém vende. Espanhol neutro/USD não prova país.

| # | País | Nicho / produto sugerido | Nota | Régua | Por quê |
|---|---|---|---|---|---|
| 1 | **México** | **Kit "Jornada 2027" para PyME e contador**: reglamento interior adaptado a 46 h, formato de registro de jornada (papel + app), aviso aos trabalhadores, calculadora de horas extra 2027 (9 h → dobro/triplo), checklist de multa 250–5.000 UMA | **8,0** | PRAZO + adjacente PROVADO | Prazo duro **01/01/2027** (registro eletrônico obrigatório, transitório 5º da LFT, DOF 01/05/2026). "Kit Reglamento Interno Inteligente" roda há **34 d** (Coach Augusto Jimenez, 39 anúncios) e a 2ª página (Jime Bauer) tem 81 anúncios. Onda de cursos começou 29–30/10 (Capacita Plus, DFP), sem kit de formatos. 470 mil contadores + PyMEs. Já é o item "Jornada México" da fila do usuário; precisa lançar até meados de novembro |
| 2 | **México** | **Kit do advogado para o juicio oral civil y familiar (CNPCF)**: escritos-modelo no novo código, roteiros de audiência preliminar/julgamento, tabela de prazos, app de prazos | **7,5** | PROVADO (curso) + PRAZO | Abogados de Éxito vende em **MXN há 273 d** (34 anúncios; "Domina el proceso civil oral" há 153 d). Manuales Jurídicos (mesmo título de anúncio, provável mesmo dono) acelerou: 72 anúncios, 13 criativos novos hoje. CNPCF entra **automaticamente em todo o país em 01/04/2027**. 445 mil advogados. Nenhum vendedor visto oferece KIT de documentos (são cursos/manuais) |
| 3 | **Argentina** | Kit do advogado por área (ART/riesgos del trabajo, amparos de salud, família, danos) | **6,0** | TESTE forte | Ratio Studio tem **216 anúncios ativos** com 5 guias por área (idade real não medível; piso 1,8 d). Abogadologia "Pack Jurídico Argentino" em ARS há 16,8 d. ~126 mil advogados (estimativa). Risco: ARS, checkout, inflação |
| 4 | **Espanha** | Kit do abogado "MASC obrigatório" (modelos de requerimento de MASC, oferta vinculante confidencial, certificado/declaração de tentativa, checklist por tipo de ação) | **6,0** | BRECHA + norma vigente | Zero kit de abogado em ES (só SaaS de IA: Rai Lomer 9 d, Catalina Leal). 149,7 mil ejercientes. LO 1/2025 vigente desde 03/04/2025 e com critérios judiciais divergentes = dor diária. Sem prazo futuro; espanhóis buscam "gratis" |
| 5 | **México** | Kit de documentos para despacho contable (carta de encargo, solicitação de papéis do mês, avisos de golpe "correo falso del SAT", proteção de CIEC/e.firma) + prompts | **5,5** | TESTE | Automatiza juridico (MXN 349, 10 d de garantia) testa isso desde 29/10 junto com o kit de advogado; Udemia.IA e outros kits de prompt entrando. Bom como order bump do #1 |
| 6 | **Espanhol (LATAM/ES)** | Kit de DOCUMENTOS do agente imobiliário (contrato de exclusividade, ficha de captação, checklist de documentos do imóvel, relatório de visita) | **5,5** | BRECHA (documentos) + PROVADO adjacente (marketing) | Organizagram vende "Pack Agente Inmobiliario" (posts) em espanhol há **42,6 d** (conta BRL, não prova país). Ninguém vende documentos. MX tem 103 mil agentes de bienes raíces. ES e IT: zero anúncios |
| 7 | **Itália** | Kit do avvocato (atos pós-Cartabia) | **5,0** | BRECHA | 228,6 mil avvocati, zero kit low ticket (só SaaS Trovanorma). Sem prazo novo em 2026–27; jurídico italiano exige revisão profissional. Faz sentido só depois do Psicólogo/Dentista IT |
| 8 | **Itália** | Kit do commercialista | **4,5** | BRECHA | 119 mil inscritos, zero vendedor. O usuário já tem o Termometro 85k (lado do forfettario); vender ao commercialista é outro público |
| 9 | **Colômbia / Chile** | Kit do advogado ou do contador | **4,5** | BRECHA | Zero anúncios de kit nas buscas. Tamanho de mercado não confirmado (VERIFICAR) |
| 10 | **EUA** | Templates para realtor | **4,0** | TESTE | Kim Buckner US$ 97 nasceu em 29/10; espaço tomado por assinaturas (Modern Agent Social Club, 96 anúncios) e SaaS. 1,44 mi realtors, mas concorrência madura |
| 11 | **Peru** | Banco de questões (balotario) jurídico | **3,5** | PROVADO, fora do formato | Leg-TECH 231,8 d em PEN, mas é exame/concurso, não kit de prática |
| 12 | **Portugal** | Advogado / imobiliário | **3,0** | BRECHA pequena | Zero vendedor; mercado não medido aqui |

### Principais apostas
- **Certeira com prazo:** #1 (Jornada 2027 MX). Mesmo comprador do "Reglamento Interno Inteligente" que já prova 34 dias; janela fecha em 01/01/2027.
- **Certeira sem pressa:** #2 (CNPCF MX). Prova de 273 dias em MXN no mesmo público; prazo 01/04/2027 dá tempo para lançar em jan–fev.
- **Teste barato:** #3 (Argentina, re-medir Ratio Studio após 08/11) e #4 (Espanha MASC).

### Diferenças em relação à v1
A v1 não estava acessível, então não dá para comparar nota a nota. O que esta versão acrescenta, com medição de 30/10:
- Idade real medida por page_id: Abogados de Éxito 273 d (MXN), Coach Augusto Jimenez 33,6 d (USD), Kim Buckner com anúncios de produto de 0,3–0,6 d (ou seja, NÃO é prova), Ratio Studio e Manuales Jurídicos com mais de 50 anúncios (só piso de idade).
- Ligação Coach Augusto Jimenez = Jime Bauer (mesmo produto) e Abogados de Éxito ≈ Manuales Jurídicos (mesmo título de anúncio).
- Vendedores novos que a lista do prompt não tinha: Automatiza juridico (MXN 349), Abogadologia (ARS), Leg-TECH (PEN, 232 d), Organizagram ES (42,6 d), Capacita Plus/DFP (onda "40 horas" de 29–30/10).
- Normas confirmadas com datas: CNPCF (DOF 07/06/2023, automático 01/04/2027), LFT 40 h (DOF 01/05/2026, registro eletrônico 01/01/2027, multa 250–5.000 UMA), LO 1/2025 (vigente 03/04/2025), Cartabia (28/02/2023; correttivo 11/2024).
- Números confirmados: MX 445 mil advogados, 470 mil contadores, 103 mil agentes imobiliários; ES 149,7 mil ejercientes; IT 228,6 mil avvocati e 119 mil commercialisti; EUA 1,44 mi realtors.

## 5. VERIFICAR

Páginas de vendas (nenhuma pôde ser aberta; rede bloqueada):
1. Preço, plataforma, conteúdo, bumps e garantia de: Abogados de Éxito, Manuales Jurídicos, Ratio Studio, Coach Augusto Jimenez, Jime Bauer, Abogadologia, Organizagram "Pack Agente Inmobiliario", Educenter (qual é o produto?), Laura Martins (PT). Kim Buckner: confirmar na stan.store se o "ROOTED Exclusive" de US$ 99 é o mesmo dos anúncios de US$ 97. Automatiza juridico: preço MXN 349 e garantia de 10 dias vêm só do título do anúncio.
2. Os 5 vendedores da lista do prompt NÃO localizados pelo nome no conector (sem page_id, v1 inacessível): **Recursos Legales PRO, Todo Digital, Cer Solutions, Destreza Digital, April Academy**.

Idade real (re-medir com SearchAPI após 08/11, que pagina além de 50 anúncios):
3. Manuales Jurídicos (72 anúncios; piso 8 d), Ratio Studio (216; piso 1,8 d), Jime Bauer (81; piso 5 d), Modern Agent Social Club (96; piso 23 d).
4. Abogadologia: re-checar em 13/11 (completa 30 d).
5. Kim Buckner: o que é o anúncio sem título ativo desde 04/04/2024 (938 d).

País e operador:
6. País-alvo de Coach Augusto Jimenez e Jime Bauer (conta USD, espanhol neutro). Confirmar se são o mesmo operador.
7. Confirmar se Manuales Jurídicos e Abogados de Éxito são o mesmo dono.

Normas:
8. CNPCF: quais estados (e a Federação) já publicaram declaratoria e com que data; quem fica para o automático de 01/04/2027.
9. Data do DOF da reforma CONSTITUCIONAL das 40 h (03/03/2026 segundo vários veículos x 01/05/2026) e o código DOF 5786537 da reforma da LFT.
10. Número do correttivo Cartabia (D.Lgs. 164/2024, citado pelo prompt) e o D.L. 19/02/2026 n. 19 (conv. L. 50/2026) que teria mexido nos arts. 696/696-bis c.p.c.

Mercado:
11. Argentina: número oficial de advogados (estimativa 126 mil; CPACF 90 mil x 71 mil no padrão).
12. Colômbia, Chile, Peru e Portugal: nº de advogados e contadores; Espanha: nº de agentes imobiliários.

## 6. O que bloqueou
- **Rede:** WebFetch/curl sem acesso a qualquer site externo (ENOTFOUND/000 até em google.com). Nenhuma página de vendas nem texto oficial aberto.
- **SearchAPI:** sem chave aqui e sem crédito até 08/11.
- **Busca web:** o orçamento de WebSearch da sessão (200 chamadas, compartilhado com os agentes irmãos) acabou no meio da pesquisa; números de AR/CO/CL/PE/PT e preços de Abogadologia/Abogados de Éxito ficaram sem busca.
- **Conector Meta:** só devolve os 50 anúncios mais novos por página e não traz link de destino nem texto do anúncio.
