# Novos nichos profissionais nas Américas — v2 (30/10/2026)

**Escopo:** MX, CO, PE, CL, AR, EC, EUA hispânico e EUA em inglês. Fora só injetáveis/harmonização facial.
**Régua:** PROVADO = vendedor com anúncio ativo há 30+ dias no país/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. Espanhol neutro (PEN/USD multipaís) não prova país. O que não confirmei está como VERIFICAR.

## 0. Limites desta rodada (ler primeiro)
- **Créditos do SearchAPI acabaram durante a pesquisa** ("used all of the searches for the month"; renova em 08/11/2026). Foram ~100 buscas por termo (lote 1: MX, CO, PE, CL, AR, EC, EUA) + medições por page_id. A segunda leva (frases de vendedor como "formatos editables", "kit de documentos") **não rodou**. Depois disso usei só o conector `ads_library_search` (~30 consultas), que devolve poucos anúncios e **não dá texto nem preço**.
- Buscas por termo solto (ex.: "kinesiólogo", "consultorio") voltam cheias de clínicas anunciando paciente; só usei o que tinha cara de vendedor de documentos. Zero resultado no conector **não prova** que ninguém vende, só que não apareceu para aquela frase.
- **Não abri:** landing da Qualitiva (skywork.website, DNS falhou), landing do Recursos Legales PRO e da Archivos Digitales Express (só li o texto/preço dos anúncios), Dr. NOM (destino é Instagram/WhatsApp), Media Center, Kit-Vet (anúncio só diz "Consultanos"), Club del Droguista (WhatsApp). **Abri:** a página do Consultorio al Día Colombia (impultienda.ar).
- WebSearch não achou páginas dos vendedores, só normas; tamanhos de vários nichos continuam sem fonte oficial (listados no fim).
- O SearchAPI não informa moeda; moeda vem do conector ou do preço no texto.

## 1. O que mudou em relação à v1 (29/10)
1. **Preço e conteúdo reais** (a v1 não tinha nenhum): Consultorio al Día CO custa **COP 49.900** (57 documentos, só consultório médico, **sem app**, garantia 7 dias). Qualitiva: **COP 79.900** (lista 3100) e **COP 129.900**, com "Lista de Chequeo dinámica" (ferramenta, não só PDF). Recursos Legales PRO: **$499 MXN** para consultório médico, **dentista** e **psicologia** (ou seja, já concorre direto com o Maletín del Psicólogo e com o dentista MX). Archivos Digitales Express: packs **a partir de $100 MXN**.
2. **Dr. NOM não é kit**: é consultoria de regularização COFEPRIS (193 d, 13 anúncios), mas prova a dor. A v1 deixava como VERIFICAR.
3. **Club del Droguista** é **software de gestão da qualidade** ("Farmatízate Calidad"), não clube de documentos. Rebaixa droguerías CO.
4. **Normas com fonte**: Res. 465/2025 (CO) com DO 53.071; **Ley 21.719 CL em 01/12/2026** (anúncios de curso ainda usam essa data, mas há projeto de adiamento não confirmado); **Ley 27.802 AR** (publicada 06/03/2026, teletrabalho em jan/2027); **SENASA Res. 654/2026** (publicada 21/07/2026); **PTIN 31/12**; **Open Enrollment 2027 de 01/11/2026 a 15/01/2027** (fontes secundárias conflitam).
5. **Tamanho com fonte**: MX consultórios 85.908 (DENUE/DataMéxico), CL RNPI 946.294 profissionais (Superintendencia de Salud) com kinesiólogos ≈47,7 mil, psicólogos ≈99,6 mil, dentistas ≈29,2 mil (cálculo meu sobre % publicados), PTIN EUA 879.698 (IRS, da rodada anterior).
6. **Novo**: Chile (Ley 21.719 para pequenos prestadores) e Argentina (Ley 27.802) entraram; Kit "Prepárate para la Inspección del Ministerio de Trabajo 2026" (CO, 8 d) apareceu; Formatos digitales (+50 formatos veterinária, MXN, chega à CO) e NutriPack360 (CLP) medidos.
7. **Rebaixados**: MX STPS (não reconfirmei as 5 páginas de 0–13 d; Media Center $99 e Simple Nom035 59 d seguem), Home care EUA (Mountain Cane é isca grátis de funil, não kit), CO restaurantes (só 9 anúncios ativos para "Resolución 2674" e nenhum vendedor de kit).

## A. Evidências medidas hoje (vendedores)

### A1. Colômbia — consultório de profissional de saúde
| Vendedor | Dias | Anúncios | Moeda | Produto / preço | Observação |
|---|---|---|---|---|---|
| **Qualitiva Soluciones** (574842992375227) | **277 d** (início 26/01/2026) | 31 ativos (conector) | COP | "Lista 3100" (autoavaliação Res. 3100) em skywork.web; "Documentos listos para adaptar"; curso express de habilitação; "Agenda tu diagnóstico" | criativos novos até 28/10. Landing skywork não abriu (DNS) |
| **Consultorio al Día Colombia** (1458650307323982) | 0 d (lançado 29/10) | 5 | USD (conta) | **COP 49.900**, pagamento único, **57 documentos** editáveis (Word/Docs em Drive), 10 procedimentos com consentimento, REPS, autoevaluación, PGIRASA, bitácoras, 4 bônus, 7 dias de garantia, atualização grátis | **Só "consultório do médico"; sem app; sem simulado.** Página impultienda.ar aberta |
| M&B Calidad y Gestión (1105323405997653) | 94 d (SearchAPI, termo 3100) | 2 | COP | "Habilitación 360" pré-venda, WhatsApp | serviço/curso |
| Auditamerica (1879144762414368) | 75 d | 1 | — | habilitação e auditoria IPS "300 aperturas", landing documentos.auditamericasas.com | serviço |
| JIT Consultings (424265384099061) | 34 d | 3 | COP | "Cumple la normativa" | serviço |
| Nexalud PRO (989443230912220) | 23 d | 1 | — | "te pidieron papeles a última hora" (WhatsApp) | VERIFICAR |
| Dt.Dental Software Odontológico | 21 d | 1 | COP | "El plazo de la 1888 ya venció" (software dentista) | confirma que a 1888 (RIPS/ficha) é gancho dentista |

### A2. México — consultório / profissões de saúde (MXN)
| Vendedor | Dias | Anúncios | Produto / preço |
|---|---|---|---|
| **Recursos Legales PRO / Salud Mx** (880855681786807) | **99 d** (23/07/2026) | 5 (conector) | Catálogo: Kit Consultorio Médico **$499**, **Kit Cirujano Dentista $499**, **Kit Legal Psicología $499**, Kit Spas y Cosmetología $699, PNOs Farmacia Lite $249 / Std $699 / PRO $999. 28/10: "26 Formatos + 3 Guías $499" e "6 Áreas Clave en un Solo Kit $699 — Herramientas para tu Práctica / Atiende Clientes de Empresa" (nova linha para **advogados**). **Já vende dentista e psicólogo MX: concorrente direto do Maletín del Psicólogo.** |
| **Archivos Digitales Express** (103894282759676) | **≥199 d**, 18 ativos | 18 | Packs "DESDE $100" **MXN**: optometria, podologia, quiropraxia, fisioterapia ("77 programas de ejercicios ilustrados"), kits tatuaje & piercing **$199 cada (+55 formatos)**, outros $249–$499. Editáveis em Word. Sem app |
| **Dr. NOM** (553817761151337) | **193 d**, 13 anúncios (últ. 18 d) | 13 | **Consultoria** de regularização COFEPRIS (alta do consultório, consultório compartilhado, clausura). Destino: Instagram/WhatsApp. **Não é kit**: é serviço = prova de dor, não de kit |
| Mi Mundo Digital (728388967028092) / Archivos Enfermería (323649287507275) | 226 d / 145 d | 1 cada | **Pack de enfermagem MXN $100 pago único** ("biblioteca digital"). Preço-âncora baixíssimo |
| Media Center México (102603028861491) | 33 d | 1 | +300 formatos laborales + contratos **$99 MXN** (WhatsApp) |
| Simple Nom035 (104728217598723) | 59 d | 1 | NOM-035 por tamanho de empresa (webify.mx) |
| Contador Salud (106378421413768) / SL Clínica Jurídica | 175 d / 220 d | 4 / 6 | respondem a "aviso de funcionamiento"; serviço contábil/jurídico para saúde (VERIFICAR) |
| Mi Guardería (104976684876361) | 148 d | 1 | software de creche |

### A3. Outros vendedores medidos (conector + SearchAPI)
| País | Vendedor (page_id) | Dias | Anúncios | Moeda | O que vende / preço |
|---|---|---|---|---|---|
| CO | Formatos digitales (629381216925799) | ≥28 d | 4+ | MXN | "Formatos de consulta de veterinaria, +50 formatos premium"; aparece em buscas da CO e do MX. Preço não visto |
| CO | Mentoría Luz Bermudez (166487169881620) | 8 d | 1 | COP | "Kit Prepárate para la Inspección del Ministerio de Trabajo 2026" |
| CO | Nova Congesst SAS (1253185267886037) | 34 d | 2 | — | "Paquete Documental Profesional HSEQ" (SG-SST), WhatsApp |
| CO | Club del Droguista = Farmatízate Calidad (551005608728294) | 58 d | 2 | COP | **Software** "centraliza documentos, auditorías, indicadores" (WhatsApp) |
| CO | Software Psicología / Tu Psicólogo en línea | 53 d / 37 d | 1–3 | MXN | biblioteca de pruebas psicométricas digitalizadas |
| CL | NutriPack360.com (1439271562593537) | 9 d | 11 | CLP | pack de nutrição "4,9/5" (preço não visto). Entrou em 21/10 |
| CL | Vilboplanner (250580878147142) | 510 d | 1 | — | software de pautas alimentares |
| CL | EVOLUTIO.CL (101030988171053) | 89 d | 1 | CLP | "Pack Pyme" formalização **$99.990 CLP** |
| CL | Entre Aulas (109509918204364) | 73 d | 3 | — | reglamento interno / fiscalização para colegios (conteúdo VERIFICAR) |
| CL | Otec Pausa (1618584794895455) | 49 d | 1 | — | curso sobre a Ley 21.719 ("el 1 de diciembre de 2026 cambia...") |
| CL | Cer Solutions (106139672439939) | ativo | 1 | USD | "Plantillas editables para psicólogos" (neutro, não prova CL) |
| PE | Documentos – Seguridad y Salud Ocupacional (193948423812234) | 55 d (v1) | 9 | PEN | pack SSOMA; hoje também "Kit Completo de Evaluación Psicológica" (1 d) |
| PE | Aprendia: Guías profesionales (1319574141233447) | 49 d | 1 | — | guia ITSE (WhatsApp) |
| PE | Esencial VET (1440545885799329) | 1 d | 3+ | PEN | "+120 estudiantes ya tienen su kit" (parece kit de estudante; VERIFICAR) |
| AR | Kit-Vet (2787265894677038) | 88 d (v1) | 15 (v1) | ARS | anúncio só diz "Consultanos"; tipo VERIFICAR |
| AR | Veterinarias Asociadas (732275399966468) | 16 d | 1 | ARS | distribuidor de insumos para veterinários (não é kit) |
| US | Hugo Tax Pro (118994584626570) | ≥5 d (página grande) | 12+ | USD | curso de impostos (hugotaxproacademy.com) |
| US | TTS Academia y Software de Impuestos (361235360412536) | 94 d | 2 | USD | curso "cuota de $87" (WhatsApp) |
| US | Prestige Accounting US (104588331564998) | 75 d | 1 | USD | orientação para abrir negócio de impostos |
| US | Mountain Cane Media (105133994237307) | 9 d | 2 | USD | **checklist grátis** "25 policies" (isca de funil), mountaincanemedia.com |
| US | Allen Chaney Home Care Business Coaching (127104947881071) | 71 d | 4+ | USD | coaching para abrir agência |

## B. Tamanho e gancho com fonte
| Nicho | Tamanho | Fonte | Gancho / data / multa | Fonte |
|---|---|---|---|---|
| CO profissionais independentes | **VERIFICAR** (v1: 47.219 no REPS, via blog; não confirmei) | só secundárias: 58.723 prestadores no REPS (consultorsalud, sem data) | Res. 3100/2019 alterada pela **Res. 465/2025** (DO 53.071, 27/03/2025): art. 5 trata da autoavaliação | [Minsalud Res. 465](https://www.minsalud.gov.co/Normatividad_Nuevo/Resolucion%20No%20465%20de%202025.pdf), [Cancillería](https://cancilleria.gov.co/normograma/compilacion/docs/resolucion_minsaludps_0465_2025.htm). Prazo para independentes e multa: **VERIFICAR**. Projeto Minsalud (sep/2026) de ampliar prazos em 15 departamentos: [CER](https://www.cerlatam.com/normatividad/ministerio-de-salud-y-proteccion-social-proyecto-de-resolucion-1-sep-2026/) (adoção não confirmada) |
| CO PGIRASA (Res. 591/2024) | — | — | **Não achei fonte** nesta rodada | VERIFICAR |
| MX consultórios médicos | **85.908** unidades (DENUE mai/2026; Censo 2019: 62.965) | [DataMéxico/Economía](https://www.economia.gob.mx/datamexico/es/profile/industry/offices-of-physicians) (INEGI) | NOM-004-SSA3-2012 (expediente, guarda mínima 5 anos); NOM-024: planilha ou PDF sem assinatura/carimbo não cumpre a norma de sistemas (fonte de mercado, [Medesk](https://www.medesk.net/es/blog/expediente-clinico-gratis/)). **Sem data nova** | [AgendaPro](https://agendapro.com/blog/nom-004/) (secundária) |
| MX NOM-035/STPS | 1.011.239 registros patronais IMSS (v1, não reconfirmado) | v1 | **Programa de Inspección 2026** apresentado em 21/09 (modelo por risco); multa NOM-035 de **250 a 5.000 UMA** (LFT art. 994-V); UMA 2026 conflita entre fontes (117,31 vs 108,57) | [Veritas](https://www.veritas.org.mx/Impuestos/Seguridad-social/Inspecciones-STPS-2026-obligaciones-laborales-y-sanciones-en-Mexico), [IDC](https://idconline.mx/laboral/2026/10/13/programa-stps-2026-las-nuevas-alertas-de-inspeccion-laboral) (secundárias). Meta de 38.455 inspeções **não confirmada**. Jornada 48→46 h em 01/01/2027: só em anúncio (Staffbridge), **VERIFICAR no DOF** |
| CL Ley 21.719 (dados pessoais) | RNPI: **946.294** profissionais (30/06/2025); kinesiólogos ≈47,7 mil, psicólogos ≈99,6 mil, enfermeiros ≈93,8 mil, médicos ≈73,5 mil, dentistas ≈29,2 mil (cálculo meu sobre %) | [Superintendencia de Salud](https://www.superdesalud.gob.cl/noticias/2025/08/superintendencia-de-salud-reporta-mas-de-946-mil-profesionales-de-la-salud-en-su-rnpi-que-garantizan-su-certificacion/) (oficial) | Vigência plena **01/12/2026** (publicada 13/12/2024). Multa até 20.000 UTM por infração gravíssima. Pequenas empresas: 12 meses de advertência no lugar de multa (guia, secundária). **Há projeto no Senado (bol. 18.623-07) para adiar para 01/12/2027; não confirmei se passou** | [Diario Constitucional](https://www.diarioconstitucional.cl/2026/06/12/la-ley-21-719-entra-en-vigor-el-1-de-diciembre-y-expone-vacios-en-regulacion-de-pequenas-empresas/) (403 ao abrir; li pelo resumo da busca), [Ecosistema Startup](https://ecosistemastartup.com/?p=104145) |
| AR Ley 27.802 | **VERIFICAR** | — | Sancionada 27/02/2026, publicada 06/03/2026 (Dec. 137/2026); teletrabalho muda em jan/2027; Fondo de Asistencia Laboral previsto para 01/06/2026 (prorrogável 6 meses); RIFL por 1 ano | [Marval](https://www.marval.com/Publicacion/entra-en-vigencia-la-ley-de-modernizacion-laboral-17508), [Allende](https://allende.com/laboral/la-reforma-laboral-entro-en-vigencia-03-09-2026/) (escritórios) |
| AR veterinários | **VERIFICAR** (v1: ~23 mil, estimativa 2014) | — | **SENASA Res. 654/2026** (publicada 21/07/2026): SIGTRAZAVET + Receita Veterinária Eletrônica obrigatória para certos produtos; etapas e prazos no anexo, **não li** | [Aduanews](https://aduananews.com/?p=84848), [O'Farrell](https://www.estudio-ofarrell.com/el-senasa-crea-un-sistema-integral-de-trazabilidad-de-productos-veterinarios-y-reglamenta-la-receta-veterinaria-electronica/), [Cronista](https://www.cronista.com/economia-politica/chau-papel-y-nuevo-control-de-medicamentos-los-puntos-clave-de-la-medida-del-senasa-para-los-veterinarios/) |
| CO inspeção laboral | — | — | Ley 2466/2025 em fiscalização; MinTrabajo anunciou inspeções com fase pedagógica antes de sanção; escala de multas para pymes **não achei** | [Valora](https://www.valoraanalitik.com/?p=480573), [RTVC](https://www.rtvcnoticias.com/politica/gobierno/mintrabajo-inspeccionara-empresas-para-verificar-reforma-laboral) |
| CO droguerías | **VERIFICAR** (sem número oficial; Droxi projeta 3.300 afiliadas) | — | **Res. 820/2026 MSPS** fixa requisitos de abertura/traslado de estabelecimentos farmacêuticos varejistas (só o resumo da busca) | [Rama Judicial](https://sidn.ramajudicial.gov.co/SIDN//NORMATIVA/TEXTOS_COMPLETOS/8_RESOLUCIONES/RESOLUCIONES%202026/MSPS%20Resolucion%20000820%20de%202026.pdf) |
| EUA preparadores | **879.698** PTINs ativos (01/08/2026); parcela hispânica **não achada** | [IRS](https://www.irs.gov/tax-professionals/tax-professional-management-office-federal-tax-return-preparer-statistics) (rodada anterior) | PTIN renova até **31/12** ([Univision](https://www.univision.com/local/tampa-wvea/irs-preparadores-de-impuestos-deben-renovar-el-ptin-2025-es-obligatorio-fotos)). **W-12 linha 11:** fontes discordam se é "estou ciente do WISP" ou atestado de que tem WISP ([Verito](https://verito.com/blog/?p=8115)). **VERIFICAR no irs.gov** (form 2027) |
| EUA agentes ACA | **não achado** | — | Open Enrollment 2027: **01/11/2026 a 15/01/2027** na maioria das fontes; algumas dizem 15/12 (desatualizadas). 45 CFR 155.220(j) (consentimento, 10 anos; rodada anterior, oficial CMS) | [Healthcare Insider](https://healthcareinsider.com/when-is-open-enrollment-for-health-insurance-2027). **VERIFICAR no CMS** |
| EC SST | 1.228.415 empresas (INEC REEM 2022) | rodada anterior | MDT-2024-196 (em vigor 09/10/2024), formato V7 do Plan de Prevención | rodada anterior; **prazo no SUT: VERIFICAR** |

## C. Ranking 0–10 (país · nicho)
Critérios: evidência de vendedor no país (30%), tamanho com fonte (15%), gancho com data/multa (20%), reaproveitamento do app do Dentista/Consultora (20%), risco (15%, nota alta = risco baixo).

| # | País · nicho | Evid. | Tam. | Gancho | Reaprov. | Risco | **Nota** | Tipo |
|---|---|---|---|---|---|---|---|---|
| 1 | **CO · profissionais independentes de saúde (fisio, nutri, fono, TO, odonto, psico) — simulacro 3100 + app** | 9 | 5 (sem número oficial) | 7 (Res. 465/2025; prazo p/ independentes VERIFICAR) | 9 | 6 (clone MX entrou 29/10 a COP 49.900) | **8,0** | **PROVADO** |
| 2 | **MX · consultório médico + profissões de saúde (fisio, podologia, optometria, quiropraxia, nutri) — simulacro COFEPRIS + app** | 8 | 9 (85.908) | 4 (sem data) | 9 | 5 (RLPRO $499 já vende médico/dentista/psico; ADE a partir de $100) | **7,5** | **PROVADO** |
| 3 | **EUA hispânico · preparador de impostos — WISP + temporada 2027** | 6 (público provado, kit não achado) | 8 (879.698; fração hispânica não achada) | 8 (PTIN 31/12; W-12 linha 11 a confirmar) | 6 | 6 (checar W-12) | **7,5** | TESTE + PRAZO |
| 4 | **CL · Ley 21.719 para consultórios e pequenos prestadores (kine, psico, dentista, nutri)** | 5 (só curso Otec Pausa 49 d; nenhum kit) | 8 (RNPI) | 8 (01/12/2026) mas adiamento não confirmado | 7 | 5 | **7,0** | TESTE + PRAZO |
| 5 | **MX · SST/NOM-035/jornada 2027 como bump** | 6 (Media Center $99 33 d; Simple Nom035 59 d) | 8 | 7 (programa STPS 2026; 01/01/2027 a confirmar) | 7 | 6 | **7,0** | TESTE + PRAZO |
| 6 | **EUA hispânico · agente ACA (consentimento 10 anos)** | 4 (69 anúncios de agentes, nenhum kit) | 3 (não achado) | 8 (OE 01/11) | 8 | 6 | **6,5** | TESTE + PRAZO |
| 7 | **MX/CO/AR · veterinário (formatos + consentimentos + receita eletrônica AR)** | 6 (Formatos digitales ≥28 d MXN; Kit-Vet AR 88 d; Vetdigital 343 d) | 3 | 6 (SENASA 654/2026, prazos no anexo) | 7 | 5 | **6,0** | TESTE |
| 8 | **MX/CO · estética não invasiva** | 6 (RLPRO $699, ADE tatuagem $199) | 4 | 4 | 7 | 6 | **6,0** | TESTE |
| 9 | **CO · inspeção do Ministério do Trabalho (Ley 2466) para pymes** | 4 (kit de 8 d) | 5 | 6 | 6 | 5 | **5,5** | TESTE |
| 10 | **CL/AR/PE/CO/EC · kine, fono, TO (módulos de documentos)** | 2 (zero kit achado) | 6 (CL kine ≈47,7 mil) | 3 | 9 | 6 | **5,5** | TESTE (brecha) |
| 11 | EC · SST (MDT-2024-196) | 4 | 7 | 6 | 8 | 5 | 5,5 | TESTE |
| 12 | CL · nutricionista | 5 (NutriPack360 CLP 9 d; Vilboplanner software) | 4 | 2 | 6 | 5 | 5,0 | TESTE |
| 13 | AR · Ley 27.802 (contadores, RRHH, pymes) | 2 (não medi vendedores) | 3 | 7 | 5 | 4 | 4,5 | VERIFICAR |
| 14 | CO · droguerías | 3 (SaaS Farmatízate 58 d) | 3 | 4 (Res. 820/2026) | 7 | 4 | 4,5 | Hold |
| 15 | CO · restaurantes (Res. 2674) | 2 (9 anúncios ativos no total) | 5 | 3 | 8 | 5 | 4,5 | Hold |
| 16 | EUA (EN) · home care / care organizations | 3 (isca grátis 9 d; coaching 71 d) | 3 | 4 | 5 | 3 | 4,0 | Hold |
| 17 | MX · enfermagem (pack $100) | 5 (226 d e 145 d) | 5 | 2 | 5 | 3 | 4,0 | Não (ticket de $100) |

**Na mão, o que muda a decisão:** o #1 e o #2 têm concorrente barato (COP 49.900 e MXN 499), mas **nenhum tem app, simulado ou semáforo**; o diferencial é o mecanismo, não o documento.

## D. Brechas, uma a uma (país · profissão · quem vende · dias)
**Tipos:** NINGUÉM = nenhum vendedor de kit visto; POUCO = vendedor novo (<30 d); IDIOMA/MOEDA = só vende neutro ou em moeda de outro país; SÓ-DOC = vende PDF sem app/simulado.
| # | País | Profissão / tema | Brecha | Quem vende (dias) | Confiança |
|---|---|---|---|---|---|
| 1 | CO | Consultório de **fisioterapia, nutri, fono, TO, odonto** (3100) | SÓ-DOC + só médico | Consultorio al Día CO (0 d, só médico); Qualitiva 277 d (lista dinâmica, empresa de IPS) | Alta |
| 2 | CO | **App/simulado** de habilitação | NINGUÉM com app | Qualitiva tem "Lista de Chequeo dinámica" (ferramenta de empresa) | Média |
| 3 | CO | PGIRASA para independentes | POUCO | só dentro de kit do Consultorio al Día | Baixa (norma VERIFICAR) |
| 4 | MX | Consultório médico com **simulacro** | SÓ-DOC | RLPRO 99 d ($499), ADE ≥199 d, Dr. NOM 193 d (serviço) | Alta |
| 5 | MX | **Fisio, podologia, optometria, quiropraxia** | SÓ-DOC barato | ADE desde $100 (≥199 d), sem app | Alta |
| 6 | MX | **Nutriólogo** | IDIOMA/PREÇO | Media Center "+4.000 archivos $99" (pack de conteúdo, não compliance) | Média |
| 7 | MX | **Advogado** (kit) | POUCO | RLPRO "Herramientas para tu Práctica" lançado 28/10 | Média |
| 8 | MX | **Dentista/psicólogo** | JÁ TEM | RLPRO $499 (99 d) | Alta |
| 9 | MX | **Tatuador/piercing** | SÓ-DOC | ADE $199 (+55 formatos) | Alta |
| 10 | MX | **Veterinário** | MOEDA | Formatos digitales (MXN, ≥28 d) | Média |
| 11 | MX | **Contador** (kit de despacho) | NINGUÉM achado | zero no conector | Baixa (busca curta) |
| 12 | MX | **Estancia/guardería** | NINGUÉM | só creches e software (Mi Guardería 148 d) | Média |
| 13 | CO | **Veterinário** | IDIOMA/MOEDA | Formatos digitales (MXN) | Média |
| 14 | CO | **Inspeção MinTrabajo (Ley 2466)** | POUCO | Mentoría Luz Bermudez (8 d, COP) | Média |
| 15 | CO | **Droguería** | Só software | Farmatízate (58 d) | Média |
| 16 | CO | **Restaurantes (2674)** | NINGUÉM | só 9 anúncios ativos | Média |
| 17 | CO | **Kine/fono/TO "kit"** | NINGUÉM | zero no conector | Média |
| 18 | PE | **Obstetra, nutri, odonto, psico (kits)** | IDIOMA/MOEDA | pack PEN neutro (Documentos SSO 55 d; hoje "Kit Evaluación Psicológica" 1 d) | Média |
| 19 | PE | **Veterinário** | POUCO | Esencial VET (PEN, 1 d; tipo VERIFICAR) | Baixa |
| 20 | PE | **ITSE / defensa civil** | POUCO | Aprendia guía ITSE (49 d, 1 anúncio) | Baixa |
| 21 | PE | **Botica** | Só software | Sistema de Boticas (v1, 259 d) | Média |
| 22 | CL | **Kine/fono/TO/nutri** (kit) | NINGUÉM / POUCO | NutriPack360 CLP (9 d); kine e fono zero | Média |
| 23 | CL | **Psicólogo/dentista/kine — Ley 21.719** | NINGUÉM | só curso Otec Pausa (49 d) | Média |
| 24 | CL | **Formalização pyme** | POUCO | EVOLUTIO Pack Pyme CLP 99.990 (89 d) | Baixa |
| 25 | CL | **Colegios (reglamento interno)** | POUCO | Entre Aulas (73 d, conteúdo VERIFICAR) | Baixa |
| 26 | CL | **Psicólogo** | IDIOMA/MOEDA | Cer Solutions (USD) | Média |
| 27 | AR | **Kine/fono/TO/psicomotricista** | NINGUÉM | zero no conector | Média |
| 28 | AR | **Veterinário (SENASA 654/2026)** | Tipo VERIFICAR | Kit-Vet 88 d (v1); "Consultanos" | Baixa |
| 29 | AR | **Perito judicial** | NINGUÉM | 1 resultado irrelevante; BR "Guia do Perito Blindado" 103 d | Média |
| 30 | AR | **Contador/RRHH (Ley 27.802)** | Não medido | VERIFICAR | — |
| 31 | EC | **Consultório, odonto, nutri (ARCSA/MSP)** | NINGUÉM (kit) | só gestores/serviço (Permisos EC 111 d, fumilimpieza 135 d, v1) | Média |
| 32 | EC | **SST pyme (MDT)** | SÓ serviço | SITSO 44 d, Siproem 0 d (v1) | Média |
| 33 | US-ES | **Preparador: WISP/kit de documentos** | NINGUÉM (conector 0 em "tax preparers WISP") | só curso/software (TTS 94 d, Hugo Tax Pro) | Média |
| 34 | US-ES | **Agente ACA** | NINGUÉM | só app Next Level (v1, 1–2 d) | Baixa |
| 35 | US-ES | **Cuidado infantil em casa** | SÓ treinamento | BCCT 415 d (v1) | Baixa |
| 36 | US-EN | **HIPAA/políticas p/ consultório pequeno** | NINGUÉM (conector 0 em "HIPAA policies templates practice") | — | Baixa (busca curta) |
| 37 | US-EN | **Home care policies** | POUCO | Mountain Cane (9 d, grátis) | Média |
| 38 | BR→ES | **Psicomotricista, eletricista, barbeiro, cílios, instalador de segurança, perito** (ofertas BR com 100–118 d) | NINGUÉM em ES (conector 0 em perito, eletricista) | BR: Documentos de Psicomotricidade 118 d, Maleta Instalador 100 d, Guia do Perito 103 d | Média |

## E. Top 8 recomendado
1. **CO · Maleta do Profissional Independiente de Salud** (módulos fisio/nutri/fono/TO/odonto) com **simulacro de visita 3100 + app**. Preço sugerido COP 69.900–89.900 (acima do Consultorio al Día 49.900, abaixo da Qualitiva 129.900), por ter semáforo e app. 8,0.
2. **MX · Maletín del Consultorio** com simulacro COFEPRIS + módulos de fisio/podologia/optometria/quiropraxia/nutri. 7,5. Rebater RLPRO com app e semáforo.
3. **EUA hispânico · Maletín del Preparador de Impuestos (WISP + temporada 2027)**. 7,5. Só depois de ler o W-12 no irs.gov.
4. **CL · Kit Ley 21.719 para consultorios** (kine, psico, dentista, nutri) com contador de prazo. 7,0. Decidir depois de confirmar se o adiamento passou.
5. **MX · Bump SST/NOM-035/jornada 2027** na oferta de jornada. 7,0.
6. **EUA hispânico · Kit do Agente ACA**, bump do #3. 6,5.
7. **Veterinário MX/CO/AR** (consentimentos, prontuário, receita eletrônica AR). 6,0.
8. **Estética não invasiva MX/CO**. 6,0.

## F. Continuou VERIFICAR
- Prazo e multa da autoavaliação 3100/465 para independentes; texto do art. 5; REPS: nº de independentes; PGIRASA/Res. 591/2024.
- Se o adiamento da Ley 21.719 (bol. 18.623-07) foi aprovado.
- Texto da W-12 (linha 11) e datas do OE 2027 no CMS.
- Meta de 38.455 inspeções STPS; jornada 46 h em 01/01/2027 no DOF.
- Anexo de prazos da Res. SENASA 654/2026; nº de veterinários MX/CO/AR.
- Conteúdo e preço de Kit-Vet, Formatos digitales, Dr. NOM (landing), Media Center, Entre Aulas, Esencial VET, NutriPack360 (preço).
- Landing Qualitiva, RLPRO, ADE (preços só pelos anúncios).
- Segunda leva de buscas por frase de vendedor (MX/CO/PE/CL/AR/EC) e as 20 buscas dos EUA que caíram por cota: refazer após 08/11 (SearchAPI) ou com o conector.
- Peru, Equador e Argentina ficaram com menos cobertura que MX/CO/CL.
- Dados brutos em `novos-nichos-americas-v2-dados/` (`log.jsonl`, `sa.py`, `sp.py`).
