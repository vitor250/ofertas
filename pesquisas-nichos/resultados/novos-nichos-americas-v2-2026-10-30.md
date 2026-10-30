# Novos nichos profissionais nas Américas (MX, CO, PE, CL, AR, EC, US) — v2

Data de referência: 30/10/2026. Pesquisa refeita (v2).

## Avisos de método (ler primeiro)
- A v1 de 29/10 (`novos-nichos-americas-2026-10-29.md` e `novos-nichos-latam-menores-2026-10-29.md`) NÃO estava acessível neste ambiente. Usei só a lista de candidatos escrita no prompt e as notas do usuário (`notas/fila-ofertas.md`: top da v1 LATAM menores = EUA hispânico preparador de impostos 8,0 / Obamacare 7,0 / Equador SST 7,0).
- SearchAPI NÃO disponível (sem chave aqui e créditos zerados até 08/11). Todas as medições de anúncios foram feitas pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` da consulta por página.
- Régua: PROVADO = vendedor ativo há 30+ dias NO país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.

## Status
(em andamento — preenchido aos poucos)

## 1. Varredura por nicho e país

Limitação do conector: ele devolve página, título do link, data de início e moeda, mas NÃO o texto do anúncio, e a busca por palavra lista os mais novos primeiro (50 por consulta). Páginas com mais de 50 anúncios ficam com "dias reais" como mínimo (≥). O link do anúncio (facebook.com) está bloqueado neste ambiente, então o produto foi deduzido pelo título do link e pela página de vendas quando achei o domínio.

### 1.1 México (MXN)
| Vendedor (page_id) | Anúncios ativos | Dias reais | O que vende (título do link) | Régua |
|---|---|---|---|---|
| Recursos Legales PRO / "Salud Mx" (880855681786807) | 5 | 98,8 | Catálogo: Kit Consultorio Médico $499, Kit Cirujano Dentista $499, Kit Legal Psicología $499, Kit Spas y Cosmetología $699, PNOs Farmacia Lite $249 / Estándar $699 / PRO $999; desde 27/10 linha para advogados ("26 Formatos + 3 Guías $499", "Colección Completa 6 áreas $699") | PROVADO (MX, 99d, poucos anúncios) |
| Dr. NOM (553817761151337) | 13 | 192,9 | CTA WhatsApp/Instagram; nome sugere adequação NOM/COFEPRIS de consultório (serviço ou kit: VERIFICAR) | PROVADO como anunciante; produto VERIFICAR |
| Mi Mundo Digital (728388967028092) | 7 | 364,4 | bateu na busca "formatos expediente clínico"; CTA "Chatea con nosotros" (venda por WhatsApp) | PROVADO (produto exato VERIFICAR) |
| Archivos Digitales Express (103894282759676) | 18 | 198,9 | bateu "formatos expediente clínico"; sem título | PROVADO (produto VERIFICAR) |
| Formatos Profesionales (860792607114068) | 1 | 149,7 | bateu "PNOs farmacia"; "¡Comprar ahora!" | PROVADO fraco (1 anúncio) |
| Archivos Digitales (1269640679555632) | 1 | 106,3 | bateu "Dr. NOM"/formatos | fraco |
| Psique y Ciencia (382519355660997) | 13 | 33,3 | "Kit de Plantillas para Psicólogos, +10 documentos esenciales" + curso de expediente | PROVADO (concorrente direto do Maletín del Psicólogo MX) |
| Formatos digitales (629381216925799) | 7 | 27,2 | formatos (bateu NOM-035/expediente) | TESTE (quase 30d) |
| Kits Profesionales (692615883936217) | 7 | 22,1 | "Kit profesional de farmacovigilancia hospitalaria 2026", "Kit manuales laboratorio clínico 2026", "Kit protocolos de ambulancias 2026" | TESTE |
| Dental PRO 360 (768039019732604) | 8 | 3,7 | bateu "formatos expediente clínico" (dentista) | TESTE (novo) |
| Papeles Laborales MX (1394677820397174) | 4 | 0 | "Blíndate por menos de 160 pesos" (documentos trabalhistas p/ patrão); **moeda BRL = vendedor brasileiro** | TESTE (clonador BR entrando hoje) |
| Formatos digitales pro (1301518069721501) / Seguridad e higiene y más (1101519659721154) | 3 / 2 | 0 | formatos NOM-035/STPS | TESTE |

Buscas de contexto MX: "NOM-035" = 211 anúncios ativos, quase todos SaaS/consultoria (Orienta "NOM-035 desde $2.999/mês", DOC24, PeopleCloud guia grátis, iodaanalytics); "registro de jornada" = 471 ativos, dominados por SaaS de ponto (Humand "Enero 2027: el registro de jornada ya es obligatorio", Chekko "Prepárate antes de 2027", Aurora Inbox "Hazlo gratis", Sesame HR) — **nenhum kit low ticket de jornada entre os 40 mais novos** (BRECHA de formato, mas briga com "grátis"); "formatos STPS" = 63 (cursos e consultorias); "formatos COFEPRIS" = 12 (Instituto Enso curso "Anti Clausura NOM-251", FRAGI, Soluciones Regulatorias).

### 1.2 Colômbia (COP)
| Vendedor (page_id) | Anúncios | Dias reais | O que vende | Régua |
|---|---|---|---|---|
| Qualitiva Soluciones (574842992375227) | 31 | 276,0 | "Documentos listos para adaptar", "Evalúa tu cumplimiento de la Resolución 3100", "Curso Express de Habilitación IPS", "Audita HC y mide adherencia a GPC", "Agenda tu diagnóstico" | PROVADO (o mais longo da CO) |
| Club del Droguista Independiente (551005608728294) | 2 | 58,1 | "Tu gestión de calidad, más fácil" (droguerías) | PROVADO fraco (2 anúncios) |
| Solunetpro (1118702291315648) | 15 | 13,4 | "Formatos SG-SST con normas 2025-2026", "Deja de bajar formatos sueltos", "Para asesores con varias empresas", "Primero recibes y luego pagas!" | TESTE forte (15 criativos em 2 semanas) |
| Consultorio al Día Colombia (1458650307323982) | 5 | 0,3 | "+55 documentos para tu consultorio"; **moeda USD** (operador estrangeiro; mesmo nome do "Consultório em Dia" visto em PT) | TESTE (clonador entrando hoje) |
| Auditamerica / Salud & Calidad Consulting / Habilisalud / JIT Consultings | 1–2 cada | 189 / 136 / 2 / — | consultoria de habilitação IPS | serviço, não kit |

### 1.3 Peru (PEN), Chile (CLP)
| Vendedor (page_id) | País | Anúncios | Dias reais | O que vende | Régua |
|---|---|---|---|---|---|
| Ing. Jorge Hurtado (1238361622683411) | PE | 153 | ≥2,7 (só vejo os 50 mais novos) | catálogo de packs a S/18: formatos SST para obras, residente de obra, Pack ITSE, norma E.030, calidad minera, SPAT etc. | TESTE forte/escala (153 anúncios) — VERIFICAR idade |
| BosQa (1319131567955572) | PE | — | 28,5 (1 anúncio visto) | "Tu primera implementación de SST S/19.90" | TESTE |
| Seguridad y Salud Ocupacional y Medio Ambiente (108273737689362) | PE | 4 | 6,4 | "Pack documental SG-SST + dashboard y señalética", "Pack completo ISO + dashboards" | TESTE |
| Esencial VET (1440545885799329) | PE | 3 | 0,5 | "+120 estudiantes ya tienen su kit" (kit p/ estudante de veterinária) | TESTE |
| Chileprevencion.cl (973357796093629) | CL | 10 | 0 (todos de hoje) | "Formatos 2026 Protocolo Ley Karin V3", "Documentos 2026 nuevo DS 44", "Comité Paritario DS 44", "Matrices IPER 2026", "Protocolo TMERT V3", "Reglamento Interno 2026 v6 DS 44" | TESTE (portal antigo começando a anunciar) |
| Arévalo y Paz Abogados (1559018394351595) | CL | ~6 | ~1–3 | "Dossier" Ley Karin, "¿Qué le muestra al fiscalizador?" | TESTE |
| Sonia Leonor Abarca Nuñez (222684954261410) | CL | — | ~2 | "Reglamento Interno PYME listo para Dirección del Trabajo y SEREMI" | TESTE |
| Vilboplanner (250580878147142) | CL | 2 | 510,4 | "Planificador profesional de nutrición" | PROVADO (nutri CL, ferramenta) |

### 1.4 Argentina (ARS)
| Vendedor | Anúncios | Dias | O que vende | Régua |
|---|---|---|---|---|
| Kit-Vet (2787265894677038) | 12 | 88,5 | CTA "Consultanos" (mensagem); produto VERIFICAR (kit físico ou digital) | PROVADO como anunciante |

### 1.5 EUA (USD)
| Vendedor | Anúncios | Dias | O que vende | Régua |
|---|---|---|---|---|
| Lic. Zulma Laguna (778739435326228) | 8 | 28,8 (faz 30d em 01/11) | kit dentista em inglês: "Inspection-Ready in 1 Hour", "Ready Dental SOPs", "Lawyer-Reviewed Dental Consents & Forms"; 4 criativos novos em 27/10 ("Dental Docs, Done for You", "Not a Blank Template"…) | TESTE→PROVADO em 01/11 se seguir ativo (está escalando criativos) |
| Certified Homecare Consulting (447937825234424) | 2 | 295,0 | anúncios de catálogo; consultoria de licença + manual de políticas p/ agência de home care (sem preço público) | PROVADO como anunciante, mas ticket alto (manuais parecidos: US$299 em payhip; Fiverr US$200–400; associação CAHSAH US$864) |
| Dental Master Pro Max (BRL, em inglês) | — | anúncio de ~146d | "Get More Dental Patients For Just $27" (marketing p/ dentista, operador BR) | sinal de BR vendendo em inglês |

Busca "preparador de impuestos" (US): 216 anúncios ativos, quase só CURSOS (TAX Cursos USA, Alpenn Institute, Clases de Taxes USA "curso gratis", MultiGla). "plantillas preparadores de impuestos" = 2 anúncios (aula grátis). → **BRECHA de kit/ferramenta para o preparador hispano já formado** (contrato de serviço, checklist de documentos do cliente, cartas, planilhas de temporada). Público = alunos desses cursos. Temporada abre em jan/2027.
Busca "home care agency forms": só ruído (suplementos). Home care em inglês é mercado de manual caro, não low ticket.

### 1.6 Varreduras por profissão (LATAM, 6 países)
- **Fisioterapia** ("formatos fisioterapia"): 6 anúncios ativos no total (Recursos Salud Pro MX: 1 anúncio de catálogo há 373d; DigitalShop USD "Fisioterapia deportiva"). → BRECHA.
- **Fonoaudiologia** ("fonoaudiología material terapia" CO/CL/AR/PE/EC): 16 ativos, só clínicas e Nexora (USD, lançamento). Nenhum kit documental. → BRECHA.
- **Terapia ocupacional**: "Bien Ocupados Pro" (1207970605743920, CL, CLP): 1 anúncio, 55,9d, "Tienda en línea de Bien Ocupados" (loja; produto VERIFICAR).
- **Nutrição** MX ("formatos para nutriólogos"): 5 ativos — NutriKits (293707977159186, MX) 1 anúncio, 6,0d, "70 kits para nutriólogos desde $50"; Media Center México "+4,000 archivos de nutrición $99". Chile: Vilboplanner 510d.
- **Equador SST** ("reglamento de higiene y seguridad", EC): 10 ativos, todos consultorias (Nova Green, SYSO Consulting via WhatsApp, SITSO EC 45,3d, admindu 49,4d, J&K Capacitaciones). Nenhum kit. Moeda USD (país dolarizado, então USD não separa neutro de local).
- **Veterinária** ("historia clínica veterinaria", 6 países): 126 ativos, todos clínicas/consumidor; vendedor para o veterinário só Kit-Vet (AR, 88d) e Esencial VET (PE, estudante, novo). → BRECHA (MX/CO/CL sem ninguém).
- **Estética sem injetáveis** ("consentimiento informado estética"): 58 ativos; kits: Ultra Pack (operador BR, USD, espanhol neutro: "Más de 50 Fichas para Estética" 20,7d, "Ficha de Depilación Láser", "+200 Reels"), Fer Torres (MX, "Conoce el kit", 1,4d), Recursos Legales PRO "Kit Spas y Cosmetología $699" (MX, 99d na página). → TESTE; neutro não prova país.
- **Advogado** ("formatos para abogados"): 45 ativos (editoras jurídicas CASAN, Notarial Ediciones, cursos). Kit low ticket: só Recursos Legales PRO (linha nova de 27/10, $499/$699 MXN) e Media Center México (mega-pack $99 MXN). Colômbia: Mentoría Luz Bermudez "Kit Inspección del Ministerio de Trabajo 2026" (COP, 7,1d).
- **Contador** ("plantillas para contadores"): 76 ativos genéricos (lojas de planilhas PE, cursos MX, Go Prompts AI). Nenhum kit de contador provado. Digitara MX vende "200 Prompts para Contadores" (novo).
- **Restaurante** ("manual de buenas prácticas restaurante" 6 países = 2 anúncios; "NOM-251 restaurante" MX = 4: Instituto Enso "Curso Anti Clausura NOM-251", consultorias). → BRECHA de kit/simulador de inspeção sanitária.
- **RH/patrão MX**: Media Center México "+300 Formatos Laborales + Contratos $99" (≥37d na página), Papeles Laborales MX (BR, $160, novo). Registro de jornada: só SaaS.
- **Mega-pack âncora**: Media Center México (102603028861491) tem 56 anúncios, ≥37d, tudo a $99 MXN (11.000 formatos, guías clínicas, tests Excel, nutrição). Puxa o preço percebido para baixo em MX.

## 2. Páginas de vendas abertas
**Bloqueado.** WebFetch não resolve domínios fora da lista liberada desta sessão (falharam chileprevencion.cl, solunetpro.com, recursoslegalespro.com, minsalud.gov.co e facebook.com). A busca web não achou o domínio de Recursos Legales PRO, Psique y Ciencia, Solunetpro, Dr. NOM, Qualitiva nem Kit-Vet. Preços abaixo vêm só do TÍTULO do anúncio:
- Recursos Legales PRO (MX): Kit Consultorio Médico $499 MXN; Kit Cirujano Dentista $499; Kit Legal Psicología $499; Kit Spas y Cosmetología $699; PNOs Farmacia Lite $249 / Estándar $699 / PRO $999; Abogados "26 formatos + 3 guías" $499; "Colección completa 6 áreas" $699. Plataforma, bumps e garantia: VERIFICAR.
- Media Center México: tudo $99 MXN (mega-packs).
- Ing. Jorge Hurtado (PE): cada pack S/18.
- BosQa (PE): "primera implementación de SST" S/19,90.
- Papeles Laborales MX (BR): "menos de 160 pesos".
- NutriKits (MX): "70 kits para nutriólogos desde $50".
- Solunetpro (CO): modelo "Primero recibes y luego pagas" (pós-pago/contra-entrega digital) — preço VERIFICAR.
Para fechar preço, plataforma, bumps e garantia é preciso abrir as páginas no navegador do Mac (lista no fim, em VERIFICAR).

## 3. Normas e tamanho de mercado (fontes oficiais)

### Colômbia — habilitação (Res. 3100)
- A **Res. 1732 de 2026** (Minsalud) foi anunciada como a nova norma de habilitação: 35 artigos, derrogando a Res. 3100/2019, a 544/2023 e a 465/2025, com transição de 12 meses (Accounter: expedida em 05/08/2026; Asuntos Legales 20–25/08/2026; Consultorsalud).
- **Ela foi revogada** pela **Res. 2080 de 2026 (08/09/2026)**, porque nunca foi publicada no Diario Oficial. Com isso, **a Res. 3100/2019 e suas modificações seguem vigentes sem interrupção** (Cerlatam). Separadamente, a **Res. 002313/2026** ampliou em até 6 meses os prazos de autoavaliação e de visitas em 16 departamentos (emergência).
- Consequência para a oferta: o gancho "pasa la visita de habilitación (Res. 3100)" continua válido. "Nueva habilitación 2026/2027" NÃO pode ser prometido. Pode-se usar "listo para la norma actual y preparado para la que viene", sem citar data. Isso bate com a regra da fila: nunca prometer data da Res. 914.
- Fontes: https://www.cerlatam.com/normatividad/minsalud-resolucion-2080-de-2026-08-sep-26/ · https://consultorsalud.com/habilitacion-servicios-de-salud-cambia-colombia/ · https://www.minsalud.gov.co/Normativa/proyactadm/PROYECTO%20DE%20RESOLUCION%20ACTUALIZACION%20HABILITACION%2009072026_20260709121104.pdf · https://consultorsalud.com/wp-content/uploads/2026/10/Resolucion_002313_2026_Diario_Oficial_OCR.pdf · https://www.cancilleria.gov.co/sites/default/files/Normograma/docs/pdf/resolucion_minsaludps_3100_2019.pdf
- VERIFICAR: o texto da Res. 2080/2026 no Diario Oficial e se o Minsalud reexpediu uma nova norma depois de 08/09.

### México — COFEPRIS / NOM-004
- **NOM-004-SSA3-2012** (expediente clínico) está vigente: DOF 15/10/2012, em vigor desde 13/12/2012 (registro oficial da Secretaría de Economía: https://platiica.economia.gob.mx/normalizacion/NOM-004-SSA3-2012/ ; texto: https://www.gob.mx/cms/uploads/attachment/file/512094/NOM-004-SSA3-2012.pdf). A NOM-024-SSA3-2012 cobre o expediente eletrônico.
- Aviso de funcionamiento e aviso de responsable sanitario perante COFEPRIS: citados por guias comerciais (Medesk, AgendaPro), sem fonte oficial nova. **Nenhuma obrigação nova de 2026 para consultório foi achada** → não há PRAZO, é gancho evergreen ("que no te clausuren / pasa la verificación").

### México — STPS 2026 (registro de jornada)
- Reforma constitucional publicada no DOF em 03/03/2026; reforma da LFT publicada no DOF em 01/05/2026. **Registro electrónico de jornada exigível a partir de 01/01/2027** (art. 132, fr. XXXIV LFT), com entrada, saída, horas extras e descansos. A jornada cai para 46h em 2027, 44h em 2028, 42h em 2029 e 40h em 2030. Multa de **250 a 5.000 UMA** (KPMG). As disposições operativas da STPS ainda estão pendentes (Littler).
- Fontes: https://www.perezllorca.com/wp-content/uploads/2026/04/Nota-Juridica-Reforma-Laboral-2026.pdf · https://kpmg.com/mx/es/tendencias/2026/04/flash-lft-avance-legislativo-de-la-reforma-en-materia-de-reduccion-de-jornada-laboral.html · https://www.littler.com/news-analysis/asap/mexico-reduce-la-jornada-laboral · https://www.elcontribuyente.mx/2026/10/registro-electronico-de-asistencia-que-exige-la-reforma-laboral/
- VERIFICAR: os números do DOF (link direto do dof.gob.mx não saiu na busca).
- NOM-035: segue sendo o maior volume de anúncios (211), mas é dominada por SaaS/consultoria; não achei prazo novo.

### Argentina — SENASA
- **Res. SENASA 43/2026** (BO 15/01/2026) cria o **Sistema Único de Registro (SUR)** de acreditação para veterinários privados, técnicos, vacunadores e inspectores que atuam em **planos sanitários oficiais**. Acreditação válida por 4 anos; sanções vão de suspensão a inabilitação de 5+ anos. Alcance restrito ao veterinário rural/de planos oficiais, não à clínica de pequenos animais. Há também protesto contra a "Res. 201/26 SENASA" (Bichos de Campo; conteúdo VERIFICAR).
- Fontes: https://www.boletinoficial.gob.ar/detalleAviso/primera/337639/20260122 · https://www.ambito.com/informacion-general/el-senasa-unifico-el-sistema-acreditacion-veterinarios-y-tecnicos-privados-n6234478 · https://siap.blogdelcontador.com.ar/normativa/resolucion-senasa-43-2026/
- Leitura: **não é gancho de massa** para kit veterinário AR. Serve, no máximo, de bônus para vet rural.

### Chile — Ley Karin / DS 44
- Ley 21.643 (Ley Karin): protocolo de prevenção de assédio obrigatório para toda empresa desde 01/08/2024. **DS 44** (novo regulamento SST, revoga DS 40 e DS 54) em vigor desde fev/2025. A DT tem novo procedimento de fiscalização (Decreto 21) desde 19/01/2026 e usa o Formulário Único de Fiscalização (FUF).
- **Sem prazo novo em 2026** → gancho de fiscalização ("¿qué le muestras al fiscalizador?"), não de data.
- Fontes: https://previsionsocial.gob.cl/wp-content/uploads/2026/03/SEGUNDO-INFORME-DS44-18032026.pdf · https://www.diariooficial.interior.gob.cl/publicaciones/2026/04/17/44427/01/2796568.pdf · https://dt.gob.cl/portal/1626/w3-article-127643.html

### Equador — SST
- **Acuerdo MDT-2024-196 (09/10/2024)**, que regulamenta o Decreto Executivo 255. Empresas de 1–10 trabalhadores tinham 12 meses para responsável SST, plano de prevenção, organismo paritário e vigilância da saúde. Empresas com +10 tinham **24 meses** para o regulamento de higiene e segurança e os paritários; os programas de riscos psicossociais e de álcool/drogas tinham 12 meses (EY, NMS).
- Pelo meu cálculo, o prazo de 24 meses venceu ou está vencendo **agora (out/2026)**: VERIFICAR. Fiscalização via plataforma SUT do MDT.
- Fontes: https://ey.com/content/dam/ey-unified-site/ey-com/es-ec/technical/tax/documents/ey-labor-alert-oct15-normas-de-seguridad-salud.pdf · https://nmslaw.com.ec/?p=14427 · https://www.trabajo.gob.ec/wp-content/uploads/2025/09/Acuerdo-Ministerial-Nro.-MDT-2025-122-signed.pdf

### Peru — SST
- Nenhuma mudança de 2026 no regulamento da Ley 29783 foi achada; só a campanha MTPE "Yo construyo sano y seguro" (RM de 13/10/2026). Gancho = SUNAFIL (evergreen).

### Tamanho de mercado (o que deu para confirmar)
- MX: cerca de **65.105 farmácias** (estudo não nomeado, via Milenio/Cronista). **55 mil farmácias independentes, 33% com consultório** (Milenio: https://www.milenio.com/negocios/una-de-cada-tres-farmacias-independientes-en-mexico-tiene-consultorios). Consultórios anexos a farmácia passaram de 239 (2001) para 6.518 (2018). VERIFICAR no DENUE.
- CO: **334.685 contadores ativos** e 4.665 sociedades contábeis (Junta Central de Contadores, jun/2025: https://incp.org.co/publicaciones/2025/09/junta-central-de-contadores-presenta-informe-su-rendicion-de-cuentas-de-2024-y-2025/).
- CO, número de profissionais independentes no REPS e de droguerías: NÃO achado (VERIFICAR no REPS/Supersalud).

## 4. Ranking 0–10
(pendente)

## 5. VERIFICAR
(pendente)
