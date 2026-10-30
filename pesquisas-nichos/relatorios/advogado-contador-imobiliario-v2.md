# Advogado, contador, imobiliário, RH por país: V2 (30/10/2026)

Refeita do zero. Método: conector Meta (`ads_library_search`, só ATIVOS) + SearchAPI `meta_ad_library` (devolve texto do anúncio, link de destino e data de início, que o conector não devolve) + WebSearch/WebFetch em fontes oficiais. Dias = 30/10/2026 menos início do anúncio ativo mais antigo da página. Scripts e JSON bruto em scratchpad da sessão.
Definições: PROVADO = vendedor com anúncio ativo 30+ dias NO país/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma.

## 0. Correções em relação à V1 (29/10)
1. **Jornada de 40 h NÃO começa em 01/01/2027.** Reforma do art. 123 publicada no DOF em 03/03/2026 (edição vespertina). Redução gradual: 48 h em 2026, **46 h em 01/01/2027**, 44 h em 2028, 42 h em 2029, **40 h só em 2030**. Sem redução salarial. Congresso teve 90 dias para adaptar a LFT; aprovação/publicação da LFT secundária = VERIFICAR (imprensa contraditória). Fontes: DOF 03/03/2026 https://dof.gob.mx/2026/PRESREP/RCRJL_03032026_VES.pdf ; Câmara de Diputados https://comunicacionsocial.diputados.gob.mx/index.php/notas/publica-dof-reforma-al-articulo-123-de-la-constitucion-politica-en-materia-de-reduccion-de-la-jornada-laboral ; JD Supra https://www.jdsupra.com/legalnews/mexico-officially-enacts-constitutional-5543577/
2. **CNPCF: prazo duro oficial = 01/04/2027.** Decreto DOF 07/06/2023; cada estado e a federação fixam por declaratoria (máx. 120 dias entre declaratoria e vigência); se não emitirem, vigência automática, sem poder passar de 01/04/2027 (art. 2º transitório). Fonte: texto oficial https://www.ordenjuridico.gob.mx/Documentos/Federal/html/wo125098.html . Tabela estado por estado: NÃO ENCONTRADA em fonte oficial agregada (CDMX declaratoria ago/2024, etapas; BC e Guerrero citam 01/04/2027). VERIFICAR por estado.
3. **Manuales Jurídicos NÃO é novo**: 71 anúncios ativos, mais antigo **79 d** (V1 dizia 14 d, olhando só os 50 mais recentes). Vende por WhatsApp.
4. **Abogados de Éxito** confirmado: 274 d, 34-40 anúncios, MXN, WhatsApp, e o criativo atual vende "curso do juízo oral familiar conforme o CNPCF".
5. **Recursos Legales PRO** = 5 anúncios, 100 d (V1: 98), MXN, WhatsApp; catálogo ampliado (ver seção 2).
6. Ley 27.802 (AR) não é "prazo duro 01/01/2027": é a Ley de Modernización Laboral, publicada no Boletín Oficial em 06/03/2026 (decreto 137/2026), vigência imediata na maior parte; alguns artigos diferidos para jan/2027 e jan/2028 (Marval). Fonte: https://www.marval.com/Publicacion/entra-en-vigencia-la-ley-de-modernizacion-laboral-17508 . Artigos diferidos exatos = VERIFICAR no texto/InfoLEG.

## 1. Achado estrutural: o kit jurídico/contábil do México se vende por WhatsApp, não por página
Em 10 vendedores MX medidos, **todos** usam botão "Enviar mensagem de WhatsApp" (link api.whatsapp.com/send); o preço vem no texto do anúncio, entrega manual/Drive. Não existe página de vendas para abrir (exceção: Adriana Pilar, que tem checkout próprio). Implicação: o formato "página de vendas + app + checkout" do usuário é um degrau acima de todos eles; o que eles provam é demanda e faixa de preço, não conversão de página.

## 2. Prova no Meta, remedida por page_id (ATIVOS; dias reais até 30/10/2026)
Fonte: SearchAPI `meta_ad_library` por page_id (texto + data de início) e conector `ads_library_search`. "n" = nº de anúncios ativos da página.

### 2.1 Advogado
| País | Vendedor (page_id) | n | Mais antigo | Moeda | Canal | Preço / conteúdo (do anúncio) |
|---|---|---|---|---|---|---|
| MX | **Abogados de Éxito** (1255927857876624) | 34 (40 c/ colação) | **274 d** | MXN | WhatsApp | Curso de redação jurídica (anúncio de 273 d) e hoje "Curso do juízo oral familiar conforme o CNPCF" ("O novo código traz grandes mudanças"); "Garantizamos tu aprendizaje". Preço não aparece no anúncio |
| MX | **Manuales Jurídicos** (2171543346464337) | 71 | **79 d** (V1 errou: 14 d) | MXN | WhatsApp | "Manual paso a paso y desde cero", "Demanda paso a paso"; ex.: "Manual de demanda federal contra o IMSS por negativa de pensão". Preço não aparece |
| MX | **Recursos Legales PRO / Salud Mx** (880855681786807) | 5 | **100 d** | MXN | WhatsApp | Catálogo: Kit Consultório Médico $499, Kit Cirurgião Dentista $499, Kit Legal Psicologia $499, Kit Spas $699, PNOs Farmácia Padrão $699 / PRO $999 / Lite $249 (26 PNOs); para advogado: "26 Formatos + 3 Guías $499" e "Colección completa 6 áreas $699" (anúncios de 2 d, novos) |
| MX | Media Center México (102603028861491) | 50 multi-nicho | 34 d (laborais); novo anúncio jurídico 2 d | MXN | WhatsApp | "+11.000 formatos jurídicos por $99 MXN", "1.244 pessoas adquiriram"; "+300 formatos e contratos laborais $99" "com atualização a 2027" |
| MX | Memoria Viva (405824942622967) | 3 | 16 d | MXN | WhatsApp | "KIT JURÍDICO PROFISSIONAL +11.000 formatos, cursos em vídeo, $99 MXN" (mesmo pacote lixo de Media Center) |
| MX | Guias visuales Aprendia (1310990752096459) | 4 | 52 d | n/d | WhatsApp | "Guía visual del Juicio de Amparo": 70 páginas, 47 fichas, 7 unidades, 7 escritos modelo comentados, linhas do tempo de prazos. Mesma fábrica faz "Peritaje Contable" (39 d). Preço não aparece |
| MX | CASAN Editores (112095737234630) | 3 | 24 d | MXN | WhatsApp | Livro Código Civil Veracruz comentado, $1.190 MXN |
| AR | **Ratio Studio** (1227357643798350) | 216 | idade VERIFICAR (créditos SearchAPI zerados; conector só mostra os 50 mais novos) | USD | n/d | "Guía Práctica de ART / Amparos de Salud / Familia / Daños y Perjuicios / Marcas"; só o termo "ART" tem 80 anúncios |
| IT | **April Academy** (101357678427132) | 1 anúncio do produto (92 c/ cursos) | **155 d** | EUR | loja WooCommerce (shop.aprilacademy.it) | **"ATTI GIUDIZIARI – DIRITTO SCOLASTICO – Edizione 2026": 25 ricorsi ex art. 414/700 c.p.c. + 11 ricorsi TAR + 1 pignoramento, em Word editável, autor avv. cassazionista. PREÇO € 490,00** (página aberta 30/10) |
| IT | **Centro Anomalie Bancarie** (680556281980009) | 2 | **156 d** | EUR | fb.me | "ATTI GIUDIZIARI – EDIZIONE 2026", coletânea prática do avv. Francesco Roli (bancário/fideiussório/consumo). Preço VERIFICAR |
| US | Kim Buckner Realtor/Coach (233861516485778) | 8 (termo) | **1 d** | USD | n/d | "35 Agent Templates for $97" (imobiliário, ver 2.3) |
| ES / PT / FR / DE / PL / CO / PE / CL | **ninguém** | 0 | n/a | | | Frase exata "plantillas para abogados", "modelos de escritos", "modelos para advogados", "modèles pour avocats", "Vorlagen Rechtsanwälte", "wzory pism", "formatos para abogados" (CO, PE, CL): 0 anúncios de kit. Só IA: Anwalt GPT (DE, €19/mês), Dra. Catalina Leal (ES, agente de IA, 6 d), MF Legado I.A. (PT, 2 d) |

### 2.2 Contador
| País | Vendedor (page_id) | n | Mais antigo | Moeda | Canal | O que vende |
|---|---|---|---|---|---|---|
| MX | **Todo Digital** (916814288184704) | 34 | **89 d** (V1 dizia 73) | n/d | WhatsApp | Não é kit de contador: "Pack Definitivo Excel & Google Sheets, +15.000 plantillas e dashboards, 10 bônus, +4mil vendidos". Anúncio "Contador: balanços, conciliações, folha pronta" tem 15 d. Pago único, preço só no WhatsApp |
| MX | **Cer Solutions** (106139672439939) | 42 | **130 d** (confirmado) | USD | n/d | Fábrica multi-nicho "Plantillas editables / Más de 250 plantillas": contadores (130 d), psicólogos, agentes de seguros, ferreterías. Preço VERIFICAR |
| MX | ContaDigital (385630871559192) | 2 | 160 d | | site contadigital.mx | Software, "+10.000 contadores"; não é kit |
| MX | Guias profesionales Aprendia (1379772175208716) | 3 | 39 d | | WhatsApp | "Guía visual de Peritaje Contable e Financeiro Judicial": 70 págs, 48 fichas, 6 cálculos (lucro cessante etc.), 5 casos |
| CO | Aprende Rápido | 2 | 30 d (V1; não remedido) | | | 50 fichas formatos/prazos; "Exógena DIAN" |
| PE | Informática Contable (106010555534698) | n/d | 5 d | PEN | | Curso/software; sem kit |
| AR / CL / ES / PT / FR / IT / DE | **ninguém** | 0 | n/a | | | "plantillas contadores" (AR), "plantillas gestoría" (ES), "modelli commercialista" (IT), "expert-comptable modèles" (FR), "Steuerberater Vorlagen" (DE): 0 kits. PT "contabilistas certificados": só Rauva/Tally (software) e Revista Gerente |

### 2.3 Imobiliário / RH
| País | Vendedor | n | Mais antigo | Moeda | Canal | O que vende |
|---|---|---|---|---|---|---|
| MX | **Aprende Fácil** (500464209825230) | 1 | **226 d** | MXN | WhatsApp | **"Kit completo de +250 Contratos Inmobiliarios Actualizados (Norma 247)": arrendamento, compraventa, cessão de direitos, garantia hipotecária, remodelar e vender, roteiros de venda, guia Lei Antilavado, calculadora imobiliária. Por "tempo limitado" SÓ $99 MXN + bônus de cursos.** V1 não viu este vendedor |
| MX | OMYT Consultores (1161821683677652) | 3 | 67 d | MXN | WhatsApp | Serviço: contratos de arrendamento desde $3.000 MXN, convênios MASC (mostra o preço de referência do advogado) |
| US | Kim Buckner (233861516485778) | | 1 d | USD | | "35 Agent Templates for $97" |
| ES / IT / FR / DE / PT / CO / PL / AR | **ninguém** | 0 | n/a | | | "agente inmobiliario plantillas", "contratos de alquiler plantillas" (ES), "agent immobilier modèles" (FR), "modelli contratti agente immobiliare" (IT), "Immobilienmakler Vorlagen" (DE), "modelos de contratos arrendamento" (PT), "inmobiliaria formatos" (CO), "martillero contratos" (AR: só curso Cetec Neuquén, ARS, 3 anúncios) |
| MX RH | **Adriana Pilar** (1011832595356413) | 133 | 25 d | USD no anúncio | **página própria reglamentomx.ultimatedigital.lat (checkout próprio)** | "Reglamento Interior Inteligente": **US$ 19,99** no anúncio. Página aberta: preço em R$ 107,19 (!, preço geolocalizado em BRL; valor "total" R$ 182,31), Reglamento Interior completo em Word/Google Docs, vídeo passo a passo, kit de sanções (7 formatos), pack inspeção NOM-035, 2 guias, bônus "7 erros de despido injustificado", garantia 7 dias, atualização 1 ano. "+10 formatos". **Não menciona jornada de 40 h**; menciona prazo de 8 dias para depositar o regulamento no Tribunal Laboral |
| MX RH | Formato Empresarial (1024484890746364) | 1 | **231 d** | | página FB | "formatos atualizados, capacitação e serviços para empresas no México". Conteúdo/preço VERIFICAR |
| MX RH | Instituto de Capacitación Laboral (122098316954011864) | 1 | 17 d | | WhatsApp | "+280 plantillas editables; INCLUI ATUALIZAÇÃO 2026: jornada laboral de 40 horas, férias; calculadoras de finiquito/liquidação; Reglamento Interior; NOM-035/019" |
| MX RH | Media Center | | 34 d | MXN | WhatsApp | "+300 formatos e contratos laborais $99 MXN, atualização a 2027" (anúncio cita preço de $799 como valor cheio) |
| CO/PE/EC | Coach Augusto Jiménez (103857225566410) | 129 (termo) | 34 d (V1; não remedido) | USD | n/d | "Kit Reglamento Interno Inteligente". Jime Bauer (81 anúncios, 7 d) mesmo produto, V1; não remedido (SearchAPI sem créditos) |
| CO | Gestión Eficiente, TG Consultores | 1 cada | 142 d / 122 d | | | Só serviço de consultoria sobre Reglamento Interno e reforma laboral |
| CO | Nova Congesst (1253185267886037) | 1 | 35 d | | WhatsApp | Pacote HSEQ "+8.000 documentos" Word/Excel (SG-SST Res. 0312/2019, Reglamento Interno entre outros); preço n/d |

## 3. Tamanho com fonte (30/10/2026)
| País | Profissão | Nº | Fonte / qualidade |
|---|---|---|---|
| MX | advogados 445 mil; contadores/auditores 470 mil | DataMéxico 2026-T1 (OFICIAL, via `top10-por-pais-2026-10-27/mexico.md`, herdado, não reaberto). Alternativas: ENOE 1T/2025 541.956 "contadores, auditores, finanças e economia" (Expansión) ; IMCP só 22-23 mil sócios | oficial/herdado |
| IT | advogados | 211.464 ativos, 228.641 inscritos na Cassa Forense em 2025 (estudo apresentado 29/04/2026, via ntplusdiritto/Milano Finanza) | secundária |
| IT | commercialisti | **119.050** inscritos no Albo em 31/12/2025 (Rapporto 2026 Fondazione Nazionale Commercialisti, 16/07/2026) https://www.fondazionenazionalecommercialisti.it/filemanager/active/01901/2026_07_16_Rapporto_2026_Scheda_di_sintesi.pdf?fid=1901 | quase oficial |
| ES | abogados | 149.695 ejercientes + 88.692 não ejercientes = 237.239 colegiados (CGAE, dados de 2024, via Aranzadi LA LEY, 27/02/2025) | secundária |
| PT | advogados | **37.842** em 2025 (DGPJ, via ECO 01/06/2026) https://eco.sapo.pt/2026/06/01/numero-de-advogados-em-portugal-volta-a-descer-em-2025-agora-sao-37-842/ | oficial via imprensa |
| PT | contabilistas certificados | 70.563 em 2022 (plano de atividades OCC 2022); 2025 NÃO ENCONTRADO | desatualizada |
| DE | advogados | BRAK 01/01/2026: 173.504 membros das Kammern; 167.547 provável nº de advogados (leitura do PDF falhou) | VERIFICAR |
| FR | avocats | 77.598 em 2025 (site de terceiros, CNB não aberto) | VERIFICAR |
| CO | contadores | **334.685** ativos com tarjeta profesional em jun/2025 + 4.665 sociedades (JCC, rendição de contas, via INCP) https://incp.org.co/publicaciones/infoincp-publicaciones/2025/09/junta-central-de-contadores-presenta-informe-su-rendicion-de-cuentas-de-2024-y-2025/ | oficial |
| CO | abogados | NÃO ENCONTRADO (URNA/SIRNA não consultado) | |
| AR | abogados ~126 mil (FACA, sem data); contadores ~140 mil (nota sem fonte) | ESTIMATIVA |
| US | advogados | **1.374.720** (ABA Profile 2025, dez/2025); corretores NAR 1.439.163 (18/06/2026) | oficial/associação |
| PE, CL, PL, GB, imobiliário em MX/IT/ES/PT/FR/DE | | NÃO ENCONTRADO nesta rodada | |

## 4. Ganchos legais com data (fonte oficial, ou VERIFICAR)
| País | Gancho | Data | Status | Fonte |
|---|---|---|---|---|
| MX | **CNPCF** (processo civil e familiar nacional) | Decreto DOF 07/06/2023; **prazo-limite nacional 01/04/2027**; cada entidade fixa por declaratoria com até 120 dias | PRAZO real, estado a estado VERIFICAR (CDMX: declaratoria ago/2024 em etapas) | https://www.ordenjuridico.gob.mx/Documentos/Federal/html/wo125098.html |
| MX | **Jornada**: 48 h (2026), 46 h (01/01/2027), 44 h (2028), 42 h (2029), 40 h (2030) | DOF 03/03/2026; vigor 04/03/2026 | PRAZO gradual, não 01/01/2027 = 40 h. LFT secundária: VERIFICAR | https://dof.gob.mx/2026/PRESREP/RCRJL_03032026_VES.pdf |
| MX | **NOM-247-SE-2021** (contratos e publicidade de imóveis) + registro de contratos na Profeco (art. 73 LFPC) | DOF 22/03/2022; vigor 18/09/2022 | já em vigor (gancho permanente: "contrato válido segundo a Norma 247"); é o argumento do Aprende Fácil há 226 d | https://platiica.economia.gob.mx/normalizacion/nom-247-se-2021/ |
| ES | **LO 1/2025** eficiência da justiça: MASC como requisito de procedibilidad (civil e mercantil; fora trabalhista, penal, concursal) | BOE 03/01/2025; vigência 03/04/2025 | já em vigor; critérios judiciais ainda divergentes; "0 anúncios MASC" | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 ; ICAM https://web.icam.es/ley-organica-1-2025-de-2-de-enero-de-medidas-en-materia-de-eficiencia-del-servicio-publico-de-justicia/ |
| IT | **Riforma Cartabia** (d.lgs. 149/2022, processo civil) | GU n. 243 de 17/10/2022; aplicação 28/02/2023 (data de aplicação: conhecimento, não confirmada nesta rodada) | em vigor; sem prazo futuro | filodiritto/sistemapenale (secundárias) |
| GB | **Renters' Rights Act 2025**, fase 1 (fim do Section 21) | 01/05/2026 (roadmap gov.uk MHCLG); prazo 31/07/2026 p/ ações de S21 anteriores (fonte secundária) | em vigor; fases 2 e 3: VERIFICAR | https://assets.publishing.service.gov.uk/media/6915beb8bc34c86ce4e6e730/Implementing_Renters_Rights_Act_2025_-_roadmap.pdf |
| AR | Ley 27.802 Modernización Laboral | BO 06/03/2026 (decreto 137/2026); artigos diferidos jan/2027 e jan/2028 | parcialmente em vigor; artigos exatos VERIFICAR | https://www.marval.com/Publicacion/entra-en-vigencia-la-ley-de-modernizacion-laboral-17508 |
| CO | Reforma laboral Ley 2466/2025 | | VERIFICAR (não aberta) | |

## 5. BRECHAS encontradas, uma a uma (país × profissão × quem vende × dias)
Legenda: NINGUÉM = 0 anúncios ativos com a frase exata e com a busca difusa do conector; MOEDA/IDIOMA = existe vendedor, mas em moeda ou idioma que não serve ao comprador local.
| # | País | Profissão | Quem vende | Dias | Tipo de brecha | Tamanho | Observação |
|---|---|---|---|---|---|---|---|
| B1 | MX | Advogado (CNPCF por etapa, "qual escrito agora") | Abogados de Éxito (curso, 274 d), Manuales Jurídicos (79 d, 71 an.), Recursos Legales PRO (100 d) | 79-274 | Sem brecha de oferta, brecha de **formato**: ninguém tem app/checkout, todos WhatsApp | 445 mil | PROVADO + PRAZO 01/04/2027 |
| B2 | MX | Corretor/inmobiliario (contratos Norma 247, Profeco) | Aprende Fácil (226 d, $99) | 226 | Provado barato; ninguém com mecanismo nem app; ninguém com preço de nicho | N/E | Subnicho que a V1 não viu |
| B3 | MX | Amparo / peritaje contable (guias visuais) | Aprendia (52 d / 39 d) | 39-52 | Fábrica concorrente com mesmo mecanismo de "ficha visual" | | Sinal de que "guia visual" vende; nós podemos fazer com app |
| B4 | ES | Abogado (modelos de escritos + MASC) | **NINGUÉM** (só IA: Dra. Leal 6 d) | 0 | NINGUÉM | 149.695 ejercientes | TESTE; busca difusa "MASC" só trouxe ruído |
| B5 | PT | Advogado (peças processuais) | **NINGUÉM** (MF Legado I.A. 2 d) | 0 | NINGUÉM | 37.842 | Mercado pequeno |
| B6 | FR | Avocat / expert-comptable / agent immobilier | **NINGUÉM** | 0 | NINGUÉM | 77.598 (VERIFICAR) | francófono: concorrência forte em software, não medida |
| B7 | DE | Rechtsanwalt / Steuerberater / Makler / Hausverwaltung | **NINGUÉM** de kit (Anwalt GPT €19/mês IA) | 0 | NINGUÉM | ~167-173 mil | alemão busca "kostenlos" (lição de 28/10) |
| B8 | PL | Adwokat (wzory pism) | **NINGUÉM** (V1: e-book Gąsecka, 1 d) | 0-1 | NINGUÉM | N/E | |
| B9 | CO | Contador | NINGUÉM com a frase exata; Aprende Rápido 30 d (V1) | 0-30 | NINGUÉM/novo | **334.685** (JCC) | maior base de contadores da América Latina espanhola, medido |
| B10 | CO | Abogado | **NINGUÉM** (CO "formatos para abogados" 0, "minutas" só ruído) | 0 | NINGUÉM | N/E | V1 deu nota 3 por "formatos commodity"; não há nem vendedor |
| B11 | CL | Abogado (formatos legales) | **NINGUÉM** (0 resultados) | 0 | NINGUÉM | N/E | |
| B12 | PE | Abogado | **NINGUÉM**; contador: só software/cursos | 0 | NINGUÉM | N/E | Lex Tools (V1, USD, 16 d, sem kit) |
| B13 | AR | Contador | **NINGUÉM** (Eve Muriel = serviço, ARS) | 0 | NINGUÉM | ~140 mil (est.) | Ley 27.802 pesa na folha |
| B14 | AR | Abogado | Ratio Studio (216 an., USD) | VERIFICAR | **MOEDA**: cobra em USD num país com ARS | ~126 mil | idade não medida |
| B15 | AR | Martillero/corredor | só curso Cetec Neuquén (ARS) | <5 | NINGUÉM de kit | N/E | |
| B16 | MX/CO/PE | RH Reglamento Interior | Adriana Pilar (US$19,99 no anúncio, R$107 na página: **MOEDA errada**, 133 an., 25 d), Augusto Jiménez e Jime Bauer (USD), Media Center ($99 MXN), Formato Empresarial (231 d) | 7-231 | Saturado barato; MOEDA mista | N/E | Preço-âncora US$19,99 |
| B17 | IT | Avvocato (raccolte di atti) | April Academy 155 d **€490**, Centro Anomalie Bancarie 156 d | 155-156 | **Ticket alto provado**; só 2 coletâneas de nicho (scolastico, bancario); ninguém no generalista (família, locazioni, esecuzioni, Cartabia) | 211.464 | Cartabia sem kit |
| B18 | IT | Commercialista | **NINGUÉM** (V1: Eutekne AI software) | 0 | NINGUÉM | **119.050** | forfettario/Termometro já era top na rodada Europa |
| B19 | IT/ES/FR/DE/PT | Agente inmobiliario | **NINGUÉM** de kit | 0 | NINGUÉM | N/E | |
| B20 | GB | Landlord / agentes: pacote Renters' Rights Act | **NINGUÉM** em Meta (0 anúncios; V1: só guias grátis de imobiliárias) | 0 | NINGUÉM | N/E | RRA fase 1 em vigor 01/05/2026; venda de templates no Reino Unido ocorre também em Etsy/sites, não medido |
| B21 | US | Real estate agent templates | Kim Buckner ($97, 1 d) e outros | 0-1 | Teste novo, saturado em social | 1,44 mi NAR | |
| B22 | MX | Agente de seguros, psicólogo, ferretería (adjacentes) | Cer Solutions (USD, +250 plantillas) | 130+ | MOEDA (USD no MX) | | adjacentes; fora do escopo |

## 6. Ranking 0-10
Critérios: evidência (30%), tamanho (20%), gancho com data (15%), reaproveitamento do que já existe (20%), risco (15%, nota alta = risco baixo).
| # | País × nicho | Nota | Tipo | Evidência | Tamanho | Gancho | Reaproveit. | Risco |
|---|---|---|---|---|---|---|---|---|
| 1 | **MX advogado litigante: CNPCF por etapa + app "qual escrito agora"** | **8,0** | PROVADO + PRAZO | 3 vendedores 79-274 d, todos em WhatsApp, preço $99-$699 MXN | 445 mil | 01/04/2027 (oficial) | alto (pipeline MX do psicólogo/dentista, página/banner/Wiapy ou Hotmart) | médio: conteúdo jurídico, sem "revisado por"; CNPCF muda por estado |
| 2 | **IT avvocato: raccolta di atti (generalista: famiglia, locazioni, esecuzioni, Cartabia)** | **7,3** | PROVADO (ticket alto) | April Academy 155 d, €490; Centro Anomalie 156 d | 211 mil | Cartabia (em vigor) | médio (build IT dentista/psicólogo, logo própria) | alto: autoridade do autor-avvocato, qualidade dos atti, preço alvo €97-€197 não testado |
| 3 | **MX inmobiliario: kit contratos Norma 247 + registro Profeco + calculadora** | **7,0** | PROVADO barato | Aprende Fácil 226 d, $99 | N/E | NOM-247 (em vigor) + Profeco | alto | médio: tamanho não achado; ticket $99 MXN |
| 4 | **MX RH/Pymes: Reglamento Interior + simulador de jornada gradual (46 h em 2027)** | **6,8** | PROVADO saturado | Formato Empresarial 231 d, Media Center, Adriana Pilar (133 an.) | N/E | 01/01/2027 (46 h) | alto | alto: preço $99 MXN/US$19,99, 5+ vendedores |
| 5 | **ES abogado: modelos de escritos + MASC** | **6,5** | TESTE (NINGUÉM vende) | 0 anúncios de kit; vendedores só de IA | 149.695 | LO 1/2025 em vigor | médio (build ES psicólogo/dentista) | médio: "gratis"; não há prova de que compram kit |
| 6 | **MX contador despacho: papeles de trabajo, honorários, folha com jornada gradual** | **6,3** | PROVADO fraco | Todo Digital 89 d (Excel genérico), Cer Solutions 130 d (USD), ContaDigital (software) | 470 mil | 46 h/2027 afeta nómina | alto | médio: nenhum kit específico de contador com 30+ d |
| 7 | CO contador (formatos, exógena, nómina) | 6,0 | TESTE (NINGUÉM) | 0 kits na frase exata | **334.685** | Ley 2466/2025 VERIFICAR | alto (ES-LATAM) | médio |
| 8 | AR abogado/contador (guias por matéria, ARS) | 5,8 | PROVADO (moeda errada) | Ratio Studio 216 an. em USD | ~126 mil / ~140 mil | Ley 27.802 | médio | médio: idade do Ratio não medida |
| 9 | IT commercialista | 5,5 | TESTE | 0 kits | 119.050 | forfettario | alto (Termometro) | médio |
| 10 | GB landlord pack RRA | 5,0 | TESTE | 0 anúncios Meta | N/E | RRA 01/05/2026 | baixo | alto (Etsy domina; sem tamanho) |
| 11 | US corretor $97 | 4,5 | TESTE | Kim Buckner 1 d | 1,44 mi | | baixo | alto: saturado |
| 12 | PT/FR/DE advogado ou contador | 3,5-4,5 | TESTE | 0 kits | 37,8k / 77,6k / ~167k | | médio | mercados menores, FR/DE exigem idioma e ticket altos |
| 13 | CL / PE / PL abogado | 3,5 | TESTE | 0 kits | N/E | | alto | tamanho desconhecido |

## 7. TOP 6
1. MX advogado CNPCF (8,0, provado + prazo 01/04/2027) 2. IT avvocato raccolta atti (7,3, provado a €490) 3. MX inmobiliario Norma 247 (7,0, provado barato) 4. MX RH Reglamento + jornada 46 h (6,8, saturado) 5. ES abogado MASC (6,5, NINGUÉM) 6. MX contador despacho (6,3)
Observação para decisão: 4 e 6 compartilham o gancho da jornada gradual e podem sair do mesmo app MX (simulador de jornada/horas extras/finiquito); 1 e 3 compartilham o público "abogado que atende inmobiliarias" e a base de contratos.

## 8. O QUE CONTINUA VERIFICAR
1. CNPCF estado por estado (nenhum índice oficial agregado encontrado; só o prazo-limite 01/04/2027 e CDMX em etapas).
2. Publicação da LFT secundária da jornada de 40 h (90 dias após 03/03/2026 venceram em jun/2026; imprensa contraditória, "aprovada 01/05/2026" sem DOF).
3. Artigos diferidos da Ley 27.802 (AR) para jan/2027 e jan/2028; reforma trabalhista Ley 2466/2025 (CO).
4. Renters' Rights Act: fases 2 e 3 e datas; o PDF do roadmap não foi lido (só trecho do resultado de busca).
5. Cartabia: data de aplicação 28/02/2023 não confirmada nesta rodada (publicação GU 17/10/2022 confirmada).
6. Idade real (dias) de Ratio Studio, Destreza Digital, Coach Augusto Jiménez, Jime Bauer, Aprende Rápido: **créditos SearchAPI zerados em 30/10 (10.000/10.000, renova 08/11)** e o conector só mostra os 50 mais novos. Valores de V1 mantidos e marcados "não remedido".
7. Preços de Abogados de Éxito, Manuales Jurídicos, Todo Digital, Cer Solutions, Ratio Studio, Centro Anomalie Bancarie: não aparecem no anúncio e não existe página (WhatsApp) ou não foi possível chegar nela.
8. Tamanhos não encontrados: CO abogados, PE/CL/PL em todas, GB, e imobiliários de qualquer país exceto US; DE advogados (167.547 provável, PDF BRAK ilegível); FR 77.598 só em site de terceiros; PT contabilistas 2025; AR sem fonte oficial.
9. Termos NÃO rodados por falta de crédito (lista parcial): AR "guía práctica"/"monotributo"/"contratos de alquiler", CO "exógena"/"contratos de arrendamiento", PE/CL contador e corretor, RO, GB/US "templates" (só o conector difuso rodou), FR/DE imobiliário por frase exata, ES "administrador de fincas" (SearchAPI só devolveu cursos e seguros, sem kit).
10. Conteúdo da página de Formato Empresarial (231 d) e preço de Centro Anomalie Bancarie.
11. Ressalva de método: a SearchAPI por frase exata subestima (ex.: "formatos para abogados" deu 0 enquanto "formatos jurídicos" deu 7). "NINGUÉM" significa nenhum anúncio ativo nas frases testadas, não ausência de mercado (Etsy, Hotmart orgânico, sites sem Meta não medidos).
