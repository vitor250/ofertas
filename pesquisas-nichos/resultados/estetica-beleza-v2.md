# Estética e beleza por país (sem injetáveis), v2

Data de referência: 30/10/2026. Relatório concluído com as limitações descritas em "Avisos de método".

## Resumo
- **Top 1: México, kit de consentimentos e fichas para estética, micropigmentação e tatuagem + app de assinatura (8,0, PROVADO).** Archivos Digitales Express vende consentimentos em MXN há 199 dias (estética 31 d, tatuagem 62 d). Kits Digitales vende em MXN há 139 dias. Nenhum dos dois tem app.
- **Top 2: Portugal, "Dossier da Esteticista" em PT-PT (7,5).** O Instituto Estética Portugal vende 30 cursos por 37 € há 128 dias, com 63 anúncios: é a única prova de low ticket de estética em euro. Um kit nativo (Estética em Regra, "um consentimento para cada procedimento") entrou há 4 dias, então a janela é curta.
- **Top 3: Colômbia, "Pasa la visita de la Secretaría de Salud" para salão, barbearia, manicure e estética (7,0, BRECHA).** Há 143 anúncios de cursos de bioseguridad e nenhum kit. A base legal citada como vigente é a Res. 2117/2010 e a Res. 2827/2006.
- **4: Espanha, kit do estúdio de tatuagem e micropigmentação (6,5).** A demanda pelo curso obrigatório está provada (El PUNTO, 253 dias), mas ninguém vende os documentos.
- **5: LATAM, termo e fichas para lash, sobrancelha e micropigmentação (6,0).** No Brasil o produto está provado ("Termo para lash", 319 d); em espanhol ninguém vende.
- Itália, França, Alemanha, Polônia, Romênia e inglês: zero kit e zero prova.
- Alerta: a onda BR em espanhol começou em outubro (Ultra Pack, Cabina PRO com fichas + app, Piel Lisa, E-books & Inspiração).
- Bloqueios: SearchAPI sem crédito; busca web esgotada após 3 consultas; WebFetch sem acesso a facebook.com e aos sites oficiais. Por isso preços dos concorrentes, vigência formal das normas e tamanhos de mercado ficaram VERIFICAR.

## Avisos de método
- A v1 (`pesquisas-nichos-2026-10-29/estetica-beleza.md`) NÃO estava acessível neste ambiente. Usei só a lista de candidatos e os itens VERIFICAR escritos no prompt e nas notas do usuário. Por isso a comparação com a v1 é parcial.
- SearchAPI indisponível (sem chave aqui e sem crédito até 08/11/2026). Toda medição de anúncio foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 menos o `ad_delivery_start_time` mais antigo entre os anúncios ativos da página, consultando por `page_ids`. Quando a página tem mais de 50 anúncios, o conector só devolve os 50 mais novos, então o número é um piso ("≥").
- Limite forte deste ambiente: o conector Meta devolve só nome da página, título do link e moeda. NÃO devolve o texto do anúncio nem a URL de destino, e `facebook.com` está bloqueado para WebFetch. Logo, preço e conteúdo dos vendedores achados só pela Biblioteca ficam VERIFICAR, salvo quando achei o site pela busca web.
- Busca web: só 3 consultas rodaram antes de a cota do turno acabar (limite de 200, compartilhado entre os agentes). WebFetch não resolve facebook.com, normograma.supersalud.gov.co nem colombiamove.com (bloqueio de rede). Nenhuma página de vendas foi aberta.
- Fora do escopo: harmonização facial e injetáveis (toxina, preenchimento, HOF, bioestimulador). Medicina estética com permiso COFEPRIS aparece só como sinal de norma.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias NO país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro (conta BRL/USD) não prova país.

## Achados na Biblioteca de Anúncios (por país)

### México (MXN)
| Vendedor (page_id) | O que vende (pelo título) | Anúncios ativos | DIAS REAIS | Moeda | Régua |
|---|---|---|---|---|---|
| Archivos Digitales Express (103894282759676) | Consentimientos informados: 11 dos 18 anúncios citam "consentimiento"; 3 citam "estética" (desde 30/09), 1 "tatuaje" (desde 29/08), 4 "médico" | 18 | 199 (página); estética 31; tatuagem 62 | MXN | **PROVADO MX** (consentimentos multiárea). Preço/conteúdo VERIFICAR |
| Guias profesionales - aprendia (1379772175208716) | Multinicho (456 anúncios). Estética: "Guía visual de maderoterapia y masaje reductor", "7 protocolos por zona para tu cabina", "50 fichas ilustradas: maniobra, presión y número de pases" | 456 (8 de estética) | estética ≥35 (desde 25/09) | MXN | **PROVADO MX** (guia visual, não kit de documentos) |
| mega cursos pro (871660932698024) | "Solo por hoy $50 pesos" (pack de cursos; apareceu na busca "barbería plantillas") | 7 | 270 | MXN | PROVADO MX, mas é pack de cursos genérico. Conteúdo VERIFICAR |
| Fer Torres - Marketing para Medicina Estética (987848967751572) | "Conoce el kit" (marketing para clínica) | 1+ | <5 | MXN | TESTE |
| Cabinas/estúdios de micropigmentação, lash, cejas | Serviço ao cliente final | muitos | – | MXN | ruído |

Sinal de norma no MX: a busca "COFEPRIS estética" devolve **2.797 anúncios ativos** de clínicas exibindo número de permiso de publicidad (ex.: SkinRx "Cofepris 2514132002A00003 (PUBLICIDAD)"). Isso mostra que a exigência é aplicada na prática, mas é mundo de medicina estética (fora do escopo). Para salão/estética não médica, "COFEPRIS salón de belleza" deu só 8 anúncios (serviço de licenças, "Licencia de Negocios CDMX: ¿Qué permisos necesita tu negocio?"). Ninguém vende kit "pasa la verificación sanitaria" para salão/estética: **BRECHA**.

### Colômbia (COP)
- "bioseguridad estética" CO: 143 anúncios, quase todos **cursos de bioseguridad** e academias (Cubrisalud, Cendecap, Certificación Estética, Nova Esthetic Academy, Lory D'Duque). Isso confirma que o tema bioseguridad é procurado, mas é vendido como curso presencial/certificado, não como kit.
- "formatos habilitación estética" CO: 0. "fichas técnicas cosmetología" LATAM: 13, nenhum kit colombiano.
- Gloss Boss Premium (266202273239273, COP), "El secreto de las Lashistas Top", desde 1789453020 (~45 dias): produto físico ou digital? VERIFICAR.
- Vetora Consultoria (1189422874260219, COP): consultoria (provável habilitação). VERIFICAR.
- Conclusão CO: **BRECHA** de kit de documentos de bioseguridad/visita sanitária para estética e barbearia, com demanda comprovada por cursos. Ver normas (Res. 2827/2006) na seção de normas.

### Espanhol neutro / LATAM (USD ou BRL)
| Vendedor (page_id) | O que vende | Anúncios | DIAS REAIS | Moeda | Régua |
|---|---|---|---|---|---|
| Ultra Pack (780532768486149) | "Más de 50 Fichas para Estética", "Ficha de Depilación Láser", "+200 Reels de estética", "Publicaciones listas para estética"; também PT ("O sistema que sua clínica precisa", "Gestão para Podólogas") | 16 | página 70; espanhol desde 09/10 (~21) | USD | ES = TESTE; operação BR (mesmo dono do Ultra Pack Canva R$37) |
| Estética Avanzada Academy (969643926228414) | Cursos de aparatologia "$10 USD" | 31 | 50 | BRL | PROVADO em espanhol neutro (BR operando) |
| Método Piel Lisa (1301326769726966) | "210 fichas ilustradas para aprender estética" | 1+ | ~2 | BRL | TESTE |
| Ana Beatriz (798620266658698) | "7 volúmenes sobre láser estético" | 1+ | ~2 | BRL | TESTE |
| E-books & Inspiração (433476344159696) | Multinicho BR: "Hair Stroke Profesional US$ 9,90", kinesiotaping | 19 | <4 | BRL | TESTE (onda BR nova) |
| Academia Lashista y Manicurista Pro (1366297433227139) | Cursos lash/unhas, "Black Friday" | 6+ | <7 | USD | TESTE |
| Camile Souza (1128638850323500), Camila Dias (1338511929341443) | "Haz clic para acceder" (infoproduto, tema VERIFICAR) | – | <15 | USD/BRL | TESTE |

Leitura: o espanhol de estética está recebendo agora a onda BR (Ultra Pack, Piel Lisa, Ana Beatriz, E-books & Inspiração, todos com conta BRL/USD e anúncios de outubro). Só Estética Avanzada Academy passa de 30 dias, e é curso, não kit.

### Espanha (EUR)
- "fichas estética" ES: 17 anúncios, todos de BR/LATAM (Ultra Pack USD, Piel Lisa BRL, Estética Avanzada BRL) ou software espanhol (DunaSoft, ViDay "desde 39€/mes"). Nenhum kit de documentos em euro.
- "plantillas esteticista" ES: 4 (Skin Tech Academy, curso HIFU).
- **Tatuagem/micropigmentação/piercing**: "curso higiénico sanitario tatuaje" ES = 24 anúncios. Centro de formación El PUNTO (1388793731378546, EUR) roda "Curso obligatorio para trabajar en estética", "¿Quieres tatuar legalmente?" e "Curso obligatorio para micropigmentación" **desde 19/02/2026 (253 dias)**. Aulas de Salud (1726010860992004) "Curso Higiénico Sanitario 189 €" (novo). CENTE com anúncio desde ~23/09/2025 (403 dias, curso de tatuagem). => demanda PROVADA pelo curso obrigatório (ticket médio, 189 €). **Ninguém vende o kit de documentos do estúdio** (registro de clientes, consentimento, controle de esterilização, ficha de pigmentos): BRECHA ES.

### Portugal (EUR)
| Vendedor (page_id) | O que vende | Anúncios | DIAS REAIS | Moeda | Régua |
|---|---|---|---|---|---|
| Instituto Estética Portugal (583463251514674) | "30 Cursos Certificados. 37€. Sem Truque.", "30 Cursos de Estética Online, Certificação CPD", "+3.000 alunas já formadas", "4,9/5 em 270 avaliações" | 63 | ≥128 (desde ~22/06) | EUR | **PROVADO PT** (low ticket 37 € de estética; curso, não kit) |
| Estética em Regra (1385184828015054) | "Um dossier para cada procedimento", "Um consentimento para cada procedimento" | 3 | ~4 (desde 26/10/2026) | EUR | **TESTE: concorrente PT-PT de kit de documentos acabou de entrar**. Site não indexado: preço VERIFICAR |
| Beauty Book App (776636645533944) | "A Agenda Feita Para a Esteticista" | 1 | ~270 | BRL | app BR vazando |

Leitura PT: é o único país europeu com prova de compra low ticket de estética em euro (Instituto Estética Portugal, 37 €, 128+ dias, 63 anúncios) e com um kit de documentos nativo entrando agora (Estética em Regra). Janela curta: entrar antes de Estética em Regra amadurecer.

### Itália (EUR)
- "estetista" IT: 1.940 anúncios ativos, mas é B2B pesado: software (Gestionale Madame, Beautycheck "schede tecniche personalizzate"), cosméticos, aparelhos, escolas, sites (My Beauty Site).
- "schede estetista" 6 (só software e Classmed); "consenso informato estetista" 0; "modulistica centro estetico" 0; "tatuatore consenso" 0; "kit estetista" 166 (produtos físicos e escolas).
- Sinal de norma: Classmed anuncia "Laser Diodo 808: nel tuo centro chi deve avere quale formazione?" (ver normas: laser/IPL para estetiste).
- Conclusão IT: **BRECHA** total de kit low ticket para estetista/tatuatore; mercado grande e acostumado a pagar software.

### França, Alemanha, Polônia, Romênia, inglês
- FR: "fiche client esthéticienne" 0; "esthéticienne modèles" 42 = CAP Esthétique à distance/CPF (Ascor), salões. Sem kit.
- DE/AT/CH: "Anamnesebogen Kosmetik" 1 (irrelevante); "Kosmetikerin Vorlagen" 0.
- PL: "karta zabiegowa" 0; "kosmetolog szablony" 1 (salão PMU).
- RO/MD: "cosmeticiana fișe" 0.
- EN (US/CA/GB/AU): "esthetician consent forms" 5 (coach de negócio, nada de kit); "lash tech templates" 7 (Zeely Ad Studio, gerador de anúncios por IA; AI Dream Team). Kits de formulários existem no Etsy/Canva, mas não anunciam no Meta (Etsy bloqueia, não verifiquei).
- Conclusão: **BRECHA** em todos, sem prova de compra. Só faz sentido com teste barato.

### Profissões específicas (LATAM/ES)
- Micropigmentação: "consentimiento informado micropigmentación" = 14, todos estúdios. **BRECHA** de kit.
- Tatuagem: "consentimiento tatuaje" = 6 (estúdios + Archivos Digitales Express). Só ADE vende.
- Lash: "lashista plantillas" = 30, cursos/academias. Sem kit de fichas/termo em espanhol (no BR, "Termo para lash" da Advocacia Mariane Salles tinha 319 dias e R$ 29,90 em 24/10, EscalaLow). **BRECHA** LATAM.
- Sobrancelha: "diseño de cejas plantillas" = 65, estúdios + E-books & Inspiração (BR, hairstroke US$ 9,90, novo).
- Manicure: "manicurista fichas" = 11, cursos (Digital Academy, Nail Studio Academy USD) e software (Esmalta EUR).
- Barbeiro: "barbería plantillas" = 19, software (AgendaYA CLP), e-commerce (Haciendola), mega cursos pro (MXN, 270 d). Sem kit de gestão/documentos de barbearia.
- Massoterapia: "masoterapia fichas" = 0 (no MX há o guia visual de maderoterapia da aprendia, ≥35 d).

### Achados extras (rodada 2 do conector)
- MX "consentimientos informados" (70 anúncios): **Kits Digitales (101231043033890, MXN)**, 3 anúncios, mais antigo de 16/06/2026 (**139 dias**), apareceu também em "consentimiento informado estética". Conteúdo e preço VERIFICAR. Fer Torres (MXN) "Tus formatos clínicos, sin complicaciones" (novo). OdontoDocs (BRL) e Dental PRO 360 (MXN) são de dentista.
- **Cabina PRO (1324482177420427, conta BRL, espanhol)**: "La esteticista que tiene todo bajo control", "Tu clienta completa y firma su ficha antes de la cita", "Comparte un QR y listo". É exatamente o nosso modelo (fichas + app com assinatura), 4 anúncios, desde 24/10/2026 (**6 dias**). TESTE, mas é o concorrente a vigiar.
- AR: **Criterio Clínico (1430330320154076, USD, voseo)** "Lo que tenés que tener antes de cada paciente", 2 anúncios, desde 29/10/2026 (1 dia). TESTE.
- PT "esteticista" (190 anúncios): salões, escolas (FormAlgarve, ÉpicaFormação) e de novo Estética em Regra. Nenhum outro kit.
- "30 cursos de estética certificados" em ES/IT/FR/MX/CO: só Instituto Estética Portugal (sem clone em espanhol). Mais antigo ativo dele: 16/06/2026 (128 dias).
- EUA hispânico: "examen de cosmetología en español" = 2 anúncios (escola em Chicago). Sem sinal.
- "catálogo nail designer" PT/ES/IT: 3 (loja de produtos). Sem sinal.

## Normas (verificação)
Aviso: a cota de busca web desta rodada acabou depois de 3 buscas (limite de 200 por turno, compartilhado entre os agentes) e o WebFetch não resolve os domínios oficiais (normograma.supersalud.gov.co, colombiamove.com, facebook.com bloqueados por DNS). O que está abaixo vem das 3 buscas feitas; o resto fica VERIFICAR.

### Colômbia (itens VERIFICAR da v1)
| Norma | O que diz | Status nesta rodada | Fonte |
|---|---|---|---|
| Res. 2117/2010 (MinProtección, DO 47741 de 15/06/2010) | Requisitos de apertura y funcionamiento de barberías, peluquerías, escuelas de formación de estilistas, salas de belleza e afins | Citada como vigente pela Prefeitura de Bogotá e pela SDS | saludcapital.gov.co/CTDLab/Publicaciones/2018/Resolucion_2117_2010_Salas_Belleza.pdf ; bogota.gov.co/mi-ciudad/salud/licencias-y-permisos-para-abrir-una-peluqueria-en-bogota-requisitos |
| Res. 2827/2006 | Adota o Manual de Bioseguridad para establecimientos de actividades cosméticas ou embelezamento facial, capilar, corporal e ornamental | Citada como vigente pela SDS Bogotá (guia de vigilância 2016) e compilada no normograma da Supersalud. **Nenhum ato de derrogação achado**, mas vigência formal não confirmada em fonte primária: VERIFICAR | saludcapital.gov.co/SectorBelleza/.../Resolución 2827 de 2006 - Manual Bioseguridad Actividades Cosméticas.pdf ; normograma.supersalud.gov.co/compilacion/docs/resolucion_minproteccion_2827_2006.htm |
| Res. 2263/2004 (+ Res. 3924/2005) | Apertura e funcionamento de centros de estética e cosmetologia (estética facial e corporal) | Fonte secundária diz que ainda se aplica a quem faz estética facial/corporal; a SDS Bogotá cita a 2263 como a que exige cumprir o manual de bioseguridad. **Vigência formal NÃO confirmada**: VERIFICAR. Res. 3924/2005 (guia de inspeção) não foi checada: VERIFICAR | saludcapital.gov.co (guia SDS); colombiamove.com/blog/requisitos-apertura-barberia-peluqueria-bioseguridad-colombia |
| Decreto 780/2016, arts. 2.8.10.1 e 2.8.10.2 (compila o Dec. 351/2014) | Gestão de resíduos; inclui barberías, peluquerías, estilistas, manicuristas e salas de belleza | Citado por fonte secundária. Documento exigido (plano de gestão de resíduos) é gancho de kit. Se houve manual novo de resíduos em 2024: VERIFICAR | idem |
| Autoavaliação SDS Bogotá | Existem formulários oficiais de autoavaliação para "Peluquerías, Barberías y Salones de Belleza" e "Estéticas aparatología" | Mostra o que o fiscal cobra: base perfeita para o checklist do kit | autorregulacion.saludcapital.gov.co/storage/Peluquerias, Barberias y Salones de Belleza.pdf ; .../Autoevaluación esteticas aparatologia 38.pdf |

Gancho CO: "Pasa la visita de la Secretaría de Salud" para salão, barbearia, manicure e estética (2117 + 2827 + resíduos + autoavaliação oficial), mais o app de registros diários (esterilização, limpeza, resíduos). Sem data de prazo (não é PRAZO), é fiscalização contínua.

### México (COFEPRIS)
- Observado na Biblioteca: 2.797 anúncios de estética no MX citam COFEPRIS, muitos com número de "permiso de publicidad". Isso é medicina estética (fora do escopo).
- Para salão/estética não médica, tatuagem e micropigmentação: exigência de aviso de funcionamiento/licencia sanitaria e base legal (Ley General de Salud, Reglamento de Control Sanitario de Productos y Servicios): **VERIFICAR** (não deu para buscar).

### Espanha e Itália (tatuagem, micropigmentação, piercing)
- ES: os anunciantes chamam o curso higiênico-sanitário de "obligatorio para trabajar en estética", "para tatuar legalmente" e "para micropigmentación" (El PUNTO, 253 dias; Aulas de Salud 189 €). A base legal é por comunidade autónoma (decretos regionais): **VERIFICAR** quais CCAA, quais registros e documentos o decreto exige.
- IT: zero anúncio de kit. Normas de tatuatore (linee guida do Ministero della Salute e leis regionais) e o tema laser/IPL para estetiste (anúncio da Classmed "Laser Diodo 808: chi deve avere quale formazione?"): **VERIFICAR** (inclusive se há prazo novo).

## Tamanho de mercado
Não consegui confirmar nenhum número oficial nesta rodada (busca web esgotada). Ficam **VERIFICAR**: número de esteticistas/salões em PT, FR, DE, PL, RO, PE, CL, AR (e CO/MX/ES/IT).
Sinal indireto da própria Biblioteca (anúncios ativos, não é tamanho de mercado):
- IT "estetista": 1.940 anúncios ativos (mercado B2B grande e que paga software).
- MX "COFEPRIS estética": 2.797 (medicina estética).
- PT "esteticista": 190. CO "bioseguridad estética": 143. ES "fichas estética": 17.

## Candidatos citados na v1 (verificação)
| Candidato | Achado em 30/10 | Régua |
|---|---|---|
| Archivos Digitales Express | Ativo, MXN, 18 anúncios, 199 dias. 11 anúncios falam de "consentimiento"; estética 31 d, tatuagem 62 d, médico 164 d. Preço, plataforma e conteúdo VERIFICAR (sem site indexado; título de link vazio) | PROVADO MX |
| Ultra Pack | Ativo, USD, 16 anúncios, página 70 d (anúncios em PT); espanhol só desde 09/10 (21 d): "Más de 50 Fichas para Estética", "Ficha de Depilación Láser", "+200 Reels". No BR, o mesmo operador vende "Ultra Pack Canva Fichas Estética" e "Posts Prontos para Estética" a R$ 37 (esteticapro.ultrapackcanva.com, EscalaLow 24/10). Preço em USD VERIFICAR | TESTE em espanhol |
| Digital Future | Nenhum anúncio ativo achado com "Digital Future estética" (2 resultados irrelevantes) | Parado ou nome diferente: VERIFICAR |
| Belleza Integral | "Belleza Integral fichas" só devolve anúncios da aprendia (Guias profesionales). Não achei página com esse nome | VERIFICAR (pode ter sido um produto da aprendia) |
| Tienda digital estética | "tienda digital estética" = 46 anúncios, nenhum vendedor de estética; aparece "Tienda Digital Perú" (PEN, 1 anúncio novo, tema não visível) | VERIFICAR |

## Ranking 0–10
Critérios: prova de compra no país (peso maior), brecha de kit com app, gancho de norma, encaixe com a estrutura do usuário (Hotmart MX/LATAM, euro IT/PT), risco de concorrente.

| # | Oferta (país, idioma, moeda) | Nota | Régua | Por quê |
|---|---|---|---|---|
| 1 | **México: "Kit de consentimientos y fichas para estética, micropigmentación y tatuaje" + app de firma** (MXN) | **8,0** | PROVADO | ADE vende consentimentos há 199 d (estética 31 d, tatuagem 62 d) e Kits Digitales há 139 d, ambos em MXN e sem app. Usuário já tem Hotmart/pixel MX do Psicólogo. Diferencial: app com assinatura na tela (como o Cabina PRO tenta) e modelos por procedimento (micropigmentação, lash, depilação, peeling, tatuagem) |
| 2 | **Portugal: "Dossier da Esteticista" (consentimento por procedimento, ficha, registos) + app** (EUR, PT-PT) | **7,5** | PROVADO de categoria (curso 37 €, 128 d) + TESTE de kit | Único país europeu com compra low ticket comprovada em estética. Estética em Regra entrou há 4 dias com a mesma ideia: janela curta. Casa com a Agenda Verde (mesmo público autônomo PT). Preço sugerido 19–27 € (VERIFICAR teto; notas apontam consumidor PT em 4,90–14,90 €) |
| 3 | **Colômbia: "Pasa la visita de la Secretaría de Salud" para salón, barbería, manicure y estética** (COP) | **7,0** | BRECHA com demanda (143 anúncios de curso de bioseguridad) | Normas citadas como vigentes (2117/2010, 2827/2006) e formulário oficial de autoavaliação da SDS. Mesmo ângulo "habilitación" do Dentista Colômbia que está na fila. Falta confirmar vigência da 2263/2004 e da 3924/2005 |
| 4 | **Espanha: kit documental do estúdio de tatuagem, micropigmentação e piercing** (EUR) | **6,5** | BRECHA com demanda (curso obrigatório 189 €, El PUNTO 253 d) | Ninguém vende o pacote de registros. Risco: norma muda por CCAA (fazer versão por comunidade ou genérica com tabela) |
| 5 | **LATAM: termo/consentimento + fichas para lash, cejas e micropigmentação** (USD/MXN) | **6,0** | BRECHA em espanhol; PROVADO no BR ("Termo para lash" 319 d, R$ 29,90) | Pode entrar como módulo do #1. Onda BR em espanhol começou em outubro (E-books & Inspiração, Piel Lisa) |
| 6 | **Espanhol neutro: fichas + app para esteticista** (USD) | **5,5** | TESTE | Ultra Pack (21 d) e Cabina PRO (6 d) acabaram de entrar; espanhol neutro não prova país. Melhor ir país a país (#1, #3) |
| 7 | **Itália: kit estetista (consenso informato, scheda cliente, registro laser/IPL)** (EUR) | **5,5** | BRECHA sem prova | Mercado grande (1.940 anúncios B2B), zero kit. Reaproveita checkout/euro do Dentista IT. Precisa confirmar norma laser e tatuatore |
| 8 | Barbearia LATAM (kit gestão/documentos + finanças) | 5,0 | BRECHA | Só software (AgendaYA) e pack de cursos (mega cursos pro, 270 d, genérico). No BR o "Assistente Financeiro para Barbearias" (R$ 10) tinha 76 d em 24/10 |
| 9 | Massoterapia/maderoterapia LATAM (fichas + protocolos) | 5,0 | PROVADO fraco (aprendia ≥35 d, guia visual, MXN) | "masoterapia fichas" = 0. No BR, "Kit Massoterapia Organizada 27 fichas" R$ 10 (18 d em 24/10) |
| 10 | Manicure/nail LATAM e EU | 4,0 | sem sinal de kit | Só cursos e software (Esmalta EUR) |
| 11 | França, Alemanha, Polônia, Romênia, inglês | 3,0–3,5 | BRECHA sem prova | Zero kit; FR vende CAP/CPF; Etsy domina formulários em inglês (não verificado) |

## Diferenças em relação à v1
A v1 não estava acessível, então só comparo com os itens que o prompt pedia para verificar:
- Archivos Digitales Express: confirmado e medido (199 d, consentimentos, MX). Sobe para PROVADO.
- Ultra Pack: em espanhol tem só 21 d. É TESTE, não PROVADO.
- Digital Future, Belleza Integral e Tienda digital estética: não achados como vendedores ativos de estética.
- Novos nesta v2: Instituto Estética Portugal (PT, 128 d, 37 €), Estética em Regra (PT, kit de documentos, 4 d), Kits Digitales (MX, 139 d), Cabina PRO (fichas + app em espanhol, 6 d), Criterio Clínico (AR, 1 d), Centro de formación El PUNTO (ES, curso obrigatório, 253 d).
- Normas CO: entra a Res. 2117/2010 (barbearia, salão) como base mais segura que a 2263/2004.

## Lista final de VERIFICAR
1. Preço, plataforma, conteúdo, bumps e garantia de: Archivos Digitales Express, Kits Digitales, Estética em Regra, Cabina PRO, Criterio Clínico, Ultra Pack (versão em espanhol), Instituto Estética Portugal (o que entra nos 30 cursos, plataforma). Não deu para abrir: facebook.com e os sites estão bloqueados no WebFetch e a busca web esgotou.
2. Vigência formal (fonte primária) da Res. 2263/2004, Res. 3924/2005 e Res. 2827/2006 (CO), e se houve manual novo de resíduos que mude o Dec. 780/2016.
3. COFEPRIS (MX): exigências para salão de beleza, estética não médica, tatuagem e micropigmentação (aviso de funcionamiento, licencia sanitaria, documentos de registro).
4. Espanha: quais comunidades autónomas exigem curso higiênico-sanitário e quais registros/documentos (decretos regionais) para tatuagem, micropigmentação e piercing.
5. Itália: normas de tatuatore por região e regra de formação para laser/IPL de estetiste (possível prazo).
6. Tamanho do setor (número de profissionais/estabelecimentos) em PT, FR, DE, PL, RO, PE, CL, AR, e também CO, MX, ES, IT.
7. Se "Digital Future", "Belleza Integral" e "Tienda digital estética" mudaram de nome ou pausaram (re-checar com SearchAPI após 08/11).
8. Gloss Boss Premium (CO, 45 d): é produto digital ou físico.
9. Re-checar em 12/11 e 27/11: Estética em Regra (PT), Cabina PRO e Ultra Pack (espanhol), Criterio Clínico (AR). Se algum passar de 30 dias, vira PROVADO e confirma a categoria.
