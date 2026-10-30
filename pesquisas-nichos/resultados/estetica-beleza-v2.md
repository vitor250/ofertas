# Estética e beleza por país (sem injetáveis), v2

Data de referência: 30/10/2026. Gravado aos poucos (em andamento).

## Avisos de método
- A v1 (`pesquisas-nichos-2026-10-29/estetica-beleza.md`) NÃO estava acessível neste ambiente. Usei só a lista de candidatos e os itens VERIFICAR escritos no prompt e nas notas do usuário. Por isso a comparação com a v1 é parcial.
- SearchAPI indisponível (sem chave aqui e sem crédito até 08/11/2026). Toda medição de anúncio foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 menos o `ad_delivery_start_time` mais antigo entre os anúncios ativos da página, consultando por `page_ids`. Quando a página tem mais de 50 anúncios, o conector só devolve os 50 mais novos, então o número é um piso ("≥").
- Limite forte deste ambiente: o conector Meta devolve só nome da página, título do link e moeda. NÃO devolve o texto do anúncio nem a URL de destino, e `facebook.com` está bloqueado para WebFetch. Logo, preço e conteúdo dos vendedores achados só pela Biblioteca ficam VERIFICAR, salvo quando achei o site pela busca web.
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

(continua: normas, tamanho de mercado, candidatos da v1, ranking)
