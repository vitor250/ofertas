# Fitness, nutrição, fisio e movimento: brechas por país × profissão (v2, 30/10/2026)

Reescrita da versão de 29/10 (`fitness-nutricao-fisio.md`). Arquivo gravado aos poucos; no fim há o ranking e a lista do que continuou VERIFICAR.

**Método e limites**
- Biblioteca de Anúncios pelo conector `ads_library_search`, só ATIVOS, 30/10/2026. **Dias = 30/10 menos `ad_delivery_start_time` do anúncio ativo mais antigo que o conector devolveu.** O conector devolve os mais novos primeiro e corta em 50, então em páginas grandes o número é **piso** (marcado "≥").
- **SearchAPI esgotado:** `/me` em 30/10 mostra 10.000 de 10.000 usados (outros agentes consumiram os ~1.100 créditos restantes no mesmo dia). Não houve varredura por SearchAPI; tudo abaixo é conector + web. O ciclo renova em 08/11.
- A coluna "moeda" é a moeda da conta de anúncios, não prova de mercado-alvo (um anúncio em inglês com CLP é conta chilena).
- Prova: PROVADO = vendedor ≥30 dias ativo no país/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma.

---

## 1. Medição real dos vendedores da v1 (page_id, dias, nº, moeda)

| Vendedor (page_id) | Moeda | Mais antigo ativo | Dias | Anúncios (estimado pelo conector) | Mudou vs v1 |
|---|---|---|---|---|---|
| **Nua Studio** (1192493037272507), pilates instrutor | CLP | **07/09/2026** | **53** | 18 | **v1 dizia 29 d.** Passa de 30: é PROVADO. Criativos: "+100 clases listas para usar o adaptar", "The Pilates Sculpt Instructor Kit", "POV: mañana tienes que dar Pilates y todavía no sabes qué enseñar", "¿Siempre terminas usando los mismos ejercicios?". Roda em espanhol e em inglês |
| **Clara Ríos · Pilates y Yoga** (1325918880615223) | USD | 27/10/2026 | 3 | 15 (v1: 20+) | Sem mudança de leitura. Todos os criativos entraram em 27–28/10 |
| **Geriactiva** (1259324537268785) | USD | **25/09/2026** | **≥35** | 143 | v1 dizia ≥30. Confirmado com o anúncio "Deja de armar la sesion desde cero" de 25/09 e 01/10. Piso: a página tem 143 ativos |
| Mah Souza (255170671023979) | USD | 29/10 | 1 | 8+ | clone do Geriactiva |
| Comprafacil.net (368910322962264) | USD | 11/10 | 19 | 8+ | clone do Geriactiva, 19 d |
| Sector Digital (1122535934265327) | USD | 11/10 (esta frase) | 19 | 37 | Voseo argentino ("Dejá de armar cada sesión desde cero"); página multi-nicho (psicologia do esporte, etc.) |
| **Compra Digital Yaa** (1130935583430737) | USD | **18/09/2026** | **42** | 3 | **Novo.** "Dejá de improvisar tu rehabilitación", "Rehabilitá paso a paso", "Volvé a moverte sin dolor" (voseo AR). Pouco gasto (3 anúncios), mas 42 d. Conteúdo: VERIFICAR |
| **Kit de Documentos para Fisioterapeutas** (1288195784387072) | USD | — | **0 ativos hoje** | 0 | v1 tinha 10 anúncios em 28/10. Hoje a busca por page_id e por "126 documentos fisioterapeuta" volta vazia: **pausaram ou trocaram de página em 2 dias**. Não conta como prova |
| **FizjoTeczka** (716677868202484), fisio PL | USD | 28/10/2026 | 2 | 16 | v1: 20+ |
| **Zgodny Gabinet** (1228451337028686), PL | **PLN** | 26/10/2026 | 4 | 6 | v1: 4 anúncios. Hoje vende também "massagem seca" (suchy masaż), 42 seções, pacote de 5 documentos "199 zł, pierwsze 5 pakietów", entrega Word e PDF |
| **Sophie Collins** (1423844567472797), multi-nicho PL | USD | ≥27/10 (piso, 57 ativos) | ≥3 | 57 | Cobre fisio, estética, advogado ("adwokatka", sprawa o dziecko), esterilização, RODO, "Terminy na cały rok". v1 vira 23/10 = 7 d |
| **NutriPack360.com** (1439271562593537), nutri | CLP | 21/10/2026 | 9 | 11 | Todos os 11 anúncios têm o mesmo título "¡Accede ahora! (4.9/5)" |
| **The Note Ninjas** (120478321017238), PT/OT/SLP EUA | USD | ≥26/10 (piso, 67 ativos) | ≥4 | 67 | v1: 40+. **Preço resolvido (Kajabi): US$34/mês ou US$306/ano; Pediátrico idem; "Both" US$44/mês ou US$396/ano; garantia 14 dias.** Ver §2 |
| **Recursos Salud Pro** (647860388411738) | MXN | 21/10/2025 | **374** | 1 | **Continua VERIFICAR.** Anúncio de catálogo dinâmico (`{{product.name}}`), 1 só anúncio ativo, a Biblioteca diz "o anúncio não está na biblioteca" na visualização individual. Página do Facebook sem texto. Busca web: zero resultado. Não dá para afirmar que é kit de fisio |
| **Vilboplanner** (250580878147142), nutri CL | CLP | 06/06/2025 | **511** | 2 | **Resolvido: é SaaS.** Planejador alimentar online, fundado no início de 2023 pelo médico Bruno Villalobos e a nutricionista Ana Paula Guerrero; imprensa chilena diz que a versão completa é grátis para testar em vilboplanner.com; "mais de 2.000 nutricionistas" no Instagram. 2 anúncios velhos de baixo gasto. **Não é prova de kit** |

Fontes da tabela: Meta Ads Library (conector), 30/10; Vilboplanner: [Diario Estrategia](https://www.diarioestrategia.cl/texto-diario/mostrar/5034441/vilbo-planner-revolucion-planificaciones-alimentarias-nutricionistas), [Portal Innova](https://portalinnova.cl/?p=69228); Note Ninjas: [Kajabi membership](https://thenoteninjas.mykajabi.com/membership).

## 2. Páginas de vendas abertas (preço, plataforma, conteúdo)

**Clara Ríos Pilates y Yoga** ([clarariospilates.shop](https://clarariospilates.shop))
- **US$27 pago único** (de US$117 tachado; "valor total US$180"). Moeda USD. Plataforma de pagamento não identificada (botões vão a `/checkout` interno).
- 220 exercícios de yoga e pilates mat com ficha, **50 clases** (20 yoga, 20 pilates mat, 10 fusão; 30/45/60 min), "Modo clase" com cronômetro, busca, filtros, impressão e PDF. Roda em celular, tablet e PC. **É app, não PDF.**
- 5 bônus: 52 temas semanais, banco de frases, guia de adaptações e segurança, 30 clases de emergencia, buscador de clases.
- **Upsells opcionais:** ampliação Pro (aparelhos de estúdio, +10 clases), packs prenatal e mayores (preço não indicado).
- Garantia técnica de 7 dias (só falha técnica, sem arrependimento).
- Lição: o concorrente já usa o formato que decidimos para Pilates (app + modo aula + upsell de aparelho/prenatal/idosos), a US$27.

**The Note Ninjas** (fundadores PT e OT, Kajabi): assinatura recorrente de bancos de documentação, biblioteca de vídeo, ferramenta "Planwise" de IA, comunidade. US$34/mês (US$25,50/mês no anual), "Both" US$44/mês. É **recorrência com ticket de US$300–400/ano**, o oposto do low ticket.

**Geriactiva:** a página do Facebook e a web não deram preço. Preço e conteúdo: VERIFICAR (o navegador embutido estava sendo usado por outro agente e perdeu o foco).

**Vilboplanner:** SaaS, ver §1.


### 1b. Vendedores da v1 remedidos hoje (nutri e SaaS)

| Vendedor | Moeda | Mais antigo ativo | Dias | Anúncios | Leitura |
|---|---|---|---|---|---|
| Grulla psicología y nutrición (101855774607522) | EUR | 14/02/2024 | **989** | 3 | "Plantillas profesionales para nutricionistas" (oferta de lançamento) ainda ativa, mais um anúncio de prompts para psicólogos. Baixo gasto: 3 anúncios em 2,7 anos. Prova fraca de volume |
| Silvia Menéndez (111642171338135) | EUR | 12/09/2026 | ≥48 | 63 | "Descarga tu Kit de Plantillas (Bestseller)". Escala real (63 ativos, EUR, ES). **Nicho continua VERIFICAR**: o título nunca cita profissão; busca "plantillas nutricionista" a trazia, mas pode ser kit genérico de negócio |
| Fisioterapista Facile (106802867939802), fisio IT | EUR | 11/09/2026 | 49 | 9 | SaaS (agenda, fatura, lembretes WhatsApp, "oltre 2.000 fisioterapisti"). Prova que fisio IT **compra software de gestão**, mas não é kit |
| thevea (110904617498229), DE | EUR | 01/10/2025 | **394** | 6+ | **Novo.** Lead magnet "Kostenlose Therapiebericht-Vorlagen für Heilmittelerbringer" (modelos grátis de relatório de terapia para fisio/ergo/logo). Mostra demanda alemã por modelo, mas o âncora é **grátis** |
| Archivos Digitales Express (103894282759676), MX | MXN | 25/08/2026 | **66** | 18 | **Novo.** Apareceu em "formatos fisioterapia" no México; criativos sem título. Conteúdo VERIFICAR |
| Formatos digitales (629381216925799), MX | MXN | 02/10/2026 | 28 | 7 | **Novo.** Mesmo caso, conteúdo VERIFICAR |
| Avena Salud (186593081693927), nutri MX | MXN | 30/10 | 0 | 2 | SaaS ("prueba GRATIS por 1 mes") |

Não remedidos nesta rodada (sem créditos e fora do conector): Onmymeal (ES, software), Alimetrics Studio, Mesa de Luz, Pilates con Método (vista hoje com anúncios de 28/10 = 2 d), ClassReady Studio, Your Pilates Class, Kit "Studio Blindato" etc. Valem os números da v1.

---

## 3. Tamanho (fonte oficial ou melhor disponível, 30/10)

| País × profissão | Número | Fonte | Qualidade |
|---|---|---|---|
| Espanha fisio | **74.990** colegiados (2025) | [INE EPSC 2025](https://ine.es/dyngs/Prensa/EPSC2025.htm) | Oficial |
| Espanha dietista-nutricionista | **8.683** colegiados (2025) | mesma fonte | Oficial |
| **EUA** physical therapists | **283.700** empregos em 2025 (267.200 em 2024) | [BLS OOH, Physical Therapists](https://www.bls.gov/ooh/healthcare/physical-therapists.htm), [BLS MLR 2024–34](https://www.bls.gov/opub/mlr/2026/article/industry-and-occupational-employment-projections-overview.htm) | Oficial. Resolve o VERIFICAR (v1 dizia ~245 mil) |
| **Polônia** fizjoterapeuci | **64,6 mil** exercendo em 31/12/2025 (+4,0% vs 2024); a KIF informava 75.243 ativos em 2022 | [Bankier citando GUS](https://www.bankier.pl/wiadomosc/W-Polsce-przybywa-medykow-Najnowsze-dane-GUS-9187857.html); [KIF](https://kif.info.pl) | GUS via imprensa (secundária); as duas bases têm metodologias diferentes. Resolve a lacuna: **faixa 65 a 75 mil** |
| **Itália** fisioterapisti | ~70 mil (70.388, 2023) a mais de 73 mil (sem data) iscritti | [Quotidiano.net](https://www.quotidiano.net/news/fisioterapia-la-riabilitazione-in-italia-i-numeri-dei-fisioterapisti-l6rhr1lk), [Quotidiano Sanità](https://www.quotidianosanita.it/?p=143420) | Secundária. Total atual vive no albo FNOFI (albo.alboweb-fnofi.net): **VERIFICAR** o número exato |
| **México** | **53,5 mil** ocupados na categoria "Técnicos em aparelhos de diagnóstico e tratamento médico, podólogos e fisioterapeutas" (1º tri 2026) | [DataMéxico, Economía/INEGI](https://www.economia.gob.mx/datamexico/es/profile/occupation/tecnicos-en-aparatos-de-diagnostico-tratamiento-medico-podologos-y-fisioterapeutas) | Proxy **sobreestimado** (mistura técnicos e podólogos); fisioterapeuta puro: VERIFICAR (cédulas SEP) |
| **Chile** kinesiólogos | **22.080** (inscritos no RNPI até set/2016) | [Superintendencia de Salud](https://www.superdesalud.gob.cl/664/articles-14280_recurso_1.pdf) | **Antigo (2016)**. Número atual: VERIFICAR (buscador do RNPI) |
| **Colômbia** fisioterapeutas | não achei total | ReTHUS/SISPRO tem o cubo; Ley 528/1999 exige tarjeta profesional | **VERIFICAR** |
| Pilates, yoga, personal trainer | sem registro oficial em nenhum país | — | só estimativa de mercado |

## 4. Normas com data (fonte oficial e URL)

| País | Norma | Status em 30/10/2026 | Gancho |
|---|---|---|---|
| **Itália** (fisio, nutri, todos os sanitários) | **DM 15/12/2023 n. 232** (MIMIT), requisitos mínimos das apólices de responsabilidade civil sanitária (L. 24/2017, Gelli) | Confirmado na [Gazzetta Ufficiale n. 51 de 01/03/2024](https://www.gazzettaufficiale.it/eli/id/2024/03/01/24G00032/sg): decreto de 15/12/2023, **em vigor desde 16/03/2024**. O período de adaptação das seguradoras é de **24 meses**, ou seja até ~16/03/2026 (fonte secundária [partitaiva.it](https://www.partitaiva.it/responsabilita-professionale-sanita), texto do artigo na GU: VERIFICAR). Mínimos de € 1 a 2 milhões por sinistro conforme a área (secundária). Ligação com ECM: quem não completou 70% da ECM 2023–25 pode ter cobertura negada ([OPI Palermo](https://www.opipalermo.it/images/pdf/2026/nuovo_triennio_ECM_26-28.pdf)); novo triênio ECM 2026–28 começou | **Já vigente** (VERIFICAR resolvido): é gancho de "sua apólice está em regra? seu consenso informato (L. 219/2017) está em regra?", **sem contagem regressiva**. PRAZO fraco |
| **Polônia** (fisio) | **Ustawa Kamilka** (lei de 28/07/2023, em vigor 15/02/2024), art. 10 dá 6 meses: **até 15/08/2024** para os *standardy ochrony małoletnich* | [gov.pl](https://www.gov.pl/web/sprawiedliwosc/ustawa-kamilka--standardy-ochrony-maloletnich) (oficial) lista "outra unidade médica" e organizadores de atividade médica para menores. Comentário jurídico (NIL/Prawo.pl): vale para **todo prestador de atividade médica onde menores estejam ou frequentem**, sem exigir forma separada para prática pequena. **Aplicação ao gabinete de fisio: provável, só quando atende crianças; a página oficial não cita fisioterapia nominalmente** | **Prazo vencido há 14 meses**: gancho de "documento pronto", não de urgência |
| **Chile** | **Ley 21.719** (dados pessoais) | Data legal **01/12/2026**, mas o Executivo ingressou em 01/09/2026 o Boletín 18.623-07 para postergar a **dez/2027**; comissão do Senado propôs até **out/2027** (coluna de 27/10). Fontes: [Carey](https://www.carey.cl/gobierno-ingresa-proyecto-de-ley-que-posterga-en-un-ano-entrada-en-vigor-de-la-ley-sobre-proteccion-de-datos-personales), [Pauta, 02/10/2026](https://www.pauta.cl/actualidad/2026/10/02/ley-de-datos-personales-senadores-proponen-prorroga-de-seis-meses-frente-al-ano-que-pide-el-gobierno.html) | **Prazo incerto**. Não usar "01/12/2026" como contagem regressiva até o Senado fechar |
| **Colômbia** | **Res. 1888/2025** (Minsalud, 15/09/2025): Resumen Digital de Atención (RDA) na Interoperabilidad de la HCE; modificada pela Res. 1799/2026. Mais Res. 839/2017 (guarda 15 anos), Ley 528/1999 (fisio) | [Minsalud, Res. 1888](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/resolucion-1888-de-2025.pdf). **Prazo: as fontes divergem** (6 meses a partir de 15/10/2025 = ~15/04/2026, ou vigência imediata). **Data para profissional independente: VERIFICAR** | Gancho real de HCE, sem data confirmada para independentes |
| **México** | NOM-004-SSA3-2012 (expediente clínico), vigente, **sem proposta de modificação publicada** (portal Economía). Reforma da Ley General de Salud com capítulo de Salud Digital publicada no DOF em **15/01/2026** (fonte secundária) | [Economía, NOM-004](https://platiica.economia.gob.mx/normalizacion/nom-004-ssa3-2012/), [texto no gob.mx](https://www.gob.mx/cms/uploads/attachment/file/512094/NOM-004-SSA3-2012.pdf). DOF da reforma: VERIFICAR | Sem prazo para fisio/nutri |
| **Espanha** | Ley 41/2002, LOPDGDD 3/2018 | Sem data de fiscalização | Sem gancho |
| Pilates, yoga, personal trainer | — | Nenhuma norma com data | Sem gancho |

**Efeito:** nenhum país × profissão deste agente tem contagem regressiva firme. O peso da nota vem da prova no Meta.

---

## 5. Brechas encontradas, uma a uma (país × profissão: quem vende e há quantos dias)

Legenda: **NINGUÉM** = zero vendedor de kit/aula pronta nos ativos de 30/10; **POUCO** = vendedores com menos de 30 dias; **ERRADO** = vende, mas em outro idioma, moeda ou formato.

| # | País | Profissão | Quem vende / dias | Tipo | Observação |
|---|---|---|---|---|---|
| 1 | Itália | Fisioterapista | Ninguém de kit. SaaS: Fisioterapista Facile 49 d (EUR), Scriva (IA). Buscas "modelli per fisioterapisti", "consenso informato fisioterapia": só vagas e consumo | **NINGUÉM** | Formato kit+app já roda >30 d na IT com dentista e psicólogo (v1) |
| 2 | Itália | Instrutor de pilates | Ninguém ("lezioni di pilates pronte istruttore" = 0) | **NINGUÉM** | |
| 3 | Itália | Dietista/nutrizionista | Ninguém de kit; "Nutrition App" SaaS | **NINGUÉM** | |
| 4 | Itália | Personal trainer | Ninguém de kit (Allenio é SaaS) | **NINGUÉM** | |
| 5 | Espanha | Fisioterapeuta | Ninguém de kit (Docfav, ZeeClip são software). Busca "plantillas para fisioterapeutas consentimiento historia" ES = 0 | **NINGUÉM** | Maior mercado oficial da lista: 74.990 |
| 6 | Espanha | Instrutor de pilates | Só estúdios de aula. Kit ES: ninguém | **NINGUÉM** | Clara Ríos roda em espanhol neutro, "não roda na CO" na v1; ES-Espanha em EUR sem vendedor |
| 7 | Portugal | Fisio, nutri, personal | Ninguém ("fisioterapeuta modelos documentos clínica" = 0). GeriActive Portugal abriu 29/10 (0 d, v1) | **NINGUÉM** | |
| 8 | França/Bélgica | Kiné, diététicien | Ninguém ("kinésithérapeute modèles documents cabinet" = 0) | **NINGUÉM** | |
| 9 | Alemanha/Áustria/Suíça | Physio, Ergo, Logo (Heilmittelerbringer) | Só **thevea**, EUR, **394 d**, com modelos **grátis** + software | **ERRADO** (preço zero) | Demanda existe há >1 ano; falta kit pago |
| 10 | Polônia | Fizjoterapeuta | 5 vendedores, todos <30 d: Zgodny Gabinet (PLN, 4 d, 6 anúncios), FizjoTeczka (USD, 2 d, 16), Gabinet w Porządku (USD, 5 d), Sophie Collins (USD, ≥3 d, 57 multi-nicho), Gabinet na Prawo (PLN, 14 d) | **POUCO** | Zgodny Gabinet vende massagem seca e "fizjoterapeuta mobilny" a 199 zł |
| 11 | Polônia | Dietetyk, trener personalny | Ninguém ("dokumentacja dietetyk wzory" = 0, "trener personalny dokumenty umowa wzór" = 0) | **NINGUÉM** | |
| 12 | México | Fisioterapeuta | Recursos Salud Pro (MXN, 374 d, 1 anúncio), Archivos Digitales Express (MXN, 66 d, 18), Formatos digitales (MXN, 28 d, 7). Conteúdo dos três: VERIFICAR | **POUCO/VERIFICAR** | São "formatos" em MXN; pode ser kit multi-profissão. Abrir a loja antes de decidir |
| 13 | México | Nutriólogo | Ninguém de kit (Avena Salud é SaaS grátis 1 mês) | **NINGUÉM** | |
| 14 | Colômbia | Fisio | Em COP, ninguém. Em USD neutro: Kit Docs Fisio (0 anúncios hoje, v1 10 anúncios em 28/10), Geriactiva ≥35 d | **ERRADO** | O concorrente que justificava a nota sumiu |
| 15 | Colômbia, Peru | Nutri | NutriPack360 (CLP, neutro, 9 d). Peru: cursos (ENVI, ProFormación), sem kit | **POUCO** | |
| 16 | Chile | Kinesiólogo | Ninguém ("fichas kinesiólogo planillas kinesiología" CL+AR = 0) | **NINGUÉM** | 22.080 em 2016 |
| 17 | Chile | Nutricionista | NutriPack360 CLP 9 d; Vilboplanner é SaaS grátis (511 d) | **POUCO/ERRADO** | |
| 18 | Chile | Instrutor de pilates | **Nua Studio, CLP, 53 d, 18 anúncios**; "Yobu" CLP novo (30/10) | **PROVADO** | Única prova ≥30 d do kit de aula pronta em espanhol |
| 19 | Argentina | Reabilitação/kinesiologia | Compra Digital Yaa (USD, 42 d, 3 anúncios, voseo, "Dejá de improvisar tu rehabilitación"); Sector Digital (USD, 19 d, voseo, multi-nicho) | **POUCO** | Moeda ARS: ninguém; Argentina com voseo é nicho de linguagem |
| 20 | Argentina | Instrutor de pilates | Pilates con Método (USD, 2 d) | **POUCO** | |
| 21 | EUA | Physical therapist/OT/SLP | The Note Ninjas (USD, ≥4 d, 67 anúncios, Kajabi, **US$34/mês, US$306/ano, "Both" US$44/mês**, 14 dias de garantia) | **ERRADO** (assinatura, não kit low ticket) | Brecha: kit de pagamento único de modelos de nota |
| 22 | EUA/UK/AU | Dietitian templates | Ninguém ("dietitian templates" = 2 resultados, sem relação) | **NINGUÉM** | |
| 23 | EUA/UK/AU | Personal trainer templates | Ninguém de kit (só software e marketing) | **NINGUÉM** | |
| 24 | EUA/UK/AU/CA | Pilates class plans | Estúdios; ninguém de kit além de Your Pilates Class (AUD, 1 d) e ClassReady (2 d) da v1 | **POUCO** | |
| 25 | EUA/UK/AU | Yoga teacher templates | The Well (AUD, curso "Nervous System Foundations"), Susanne Rieker (EUR, "Yoga Mini Course", marketing). Ninguém de sequências prontas | **NINGUÉM** | |
| 26 | Espanhol neutro (+PT) | Fisio geriátrica/TO/cuidador | **Geriactiva USD ≥35 d, 143 anúncios**; clones Comprafacil.net 19 d, Mah Souza 1 d, Sector Digital 19 d | **PROVADO** (saturado) | Sessão pronta, não papelada |
| 27 | Espanhol neutro | Instrutor de yoga | Só Clara Ríos (3 d, fusão yoga+pilates) | **POUCO** | |
| 28 | Espanha | Nutricionista | Grulla (EUR, 989 d, 3 anúncios, "plantillas profesionales para nutricionistas"), Silvia Menéndez (EUR, ≥48 d, 63 anúncios, nicho VERIFICAR) | **PROVADO fraco** | Só 8.683 colegiados |
| 29 | Qualquer | Terapeuta ocupacional (kit de documentos) | "terapia ocupacional plantillas evaluación" = 0 | **NINGUÉM** | TO nunca foi testada com kit neste mapa |
| 30 | Qualquer | Osteopata, quiropraxista, podólogo | Não varridos nesta rodada (conector sem termo estável, SearchAPI zerado) | **VERIFICAR** | Fica para 08/11 |

---

## 6. Ticket e LTV observados (resolvidos)
- **Clara Ríos: US$27 (de US$117), pagamento único, app**, upsell Pro (aparelhos), prenatal, mayores. É o ticket de referência do Pilates em espanhol. Garantia só técnica (7 dias).
- **Note Ninjas: US$34/mês, US$306/ano; Both US$44/mês.** Recorrência, 14 dias de garantia. Alto LTV, não é nosso modelo, mas prova que o PT/OT dos EUA paga ~US$300 a US$400 por ano por modelos de nota.
- **Zgodny Gabinet: 199 zł** por pacote (primeiros 5); polonês paga ticket alto por pacote de gabinete.
- **Vilboplanner:** SaaS com versão grátis. Preço: não encontrado.
- **Geriactiva, NutriPack360, Archivos Digitales Express, Recursos Salud Pro:** preço VERIFICAR (anúncios sem link legível; o navegador embutido foi disputado por outro agente).
- **IT:** referência €27/€19 da valigetta do dentista.

---

## 7. Ranking país × profissão (nota 0 a 10)

| # | País × profissão | Evidência (dias, moeda) | Tamanho (fonte) | Gancho | Reaproveitamento | Risco | Nota | Tipo |
|---|---|---|---|---|---|---|---|---|
| 1 | **Instrutor de pilates e yoga × espanhol (LATAM + ES)** | BR Pilates Pro 58 d; **Nua Studio 53 d CLP**; Clara Ríos US$27 com app em 3 d; Pilates con Método, Mesa de Luz, Yobu (CLP) novos | sem registro | nenhum | **Alto**: já temos o app+modo aula do formato; espanhol e BR | **Enxame**: 5+ vendedores em 7 dias, Clara Ríos já tem upsell Pro/prenatal/mayores | **7,5** | **PROVADO** (CLP 53 d) |
| 2 | **Fisioterapista × Itália** | NINGUÉM de kit; formato kit+app roda >30 d na IT (dentista 42 d, psicólogo 35 d, v1); fisio IT compra SaaS (Fisioterapista Facile 49 d) | ~70 a 73 mil (secundária) | DM 232/2023 vigente desde 16/03/2024 (GU); consenso L. 219/2017 | **Alto**: pipeline valigetta | Gancho fraco, sem sinal de que fisio compra papelada | **6,5** | **TESTE** |
| 3 | **Geriátrica/idosos (sessão pronta) × espanhol neutro e PT** | Geriactiva ≥35 d, 143 anúncios, USD; GeriActive PT 0 d; 3 clones | grande | nenhum | Médio: é conteúdo de sessão | Saturação com clones em 3 semanas | **6,5** | **PROVADO** (neutro) |
| 4 | **Fizjoterapeuta × Polônia** | 5 vendedores novos (2 a 14 d), PLN 199 zł local; nenhum ≥30 d | **64,6 mil GUS 2025 (75 mil KIF 2022)** | Kamilka: prazo vencido 15/08/2024, vale se atende menores | Médio: traduzir o kit; PL mais difícil | Sem prova de 30 d | **6,0** | **TESTE** (reavaliar 15/11) |
| 5 | **Fisioterapeuta × Espanha** | NINGUÉM de kit | **74.990 (INE 2025)** | Ley 41/2002, sem data | Alto (espanhol, EUR) | Sem vendedor ≥30 d no mundo para fisio kit; teria de ser primeiro | **5,5** | **TESTE** |
| 6 | **Fisioterapeuta × Colômbia** | Kit Docs Fisio USD: **0 ativos hoje**; Geriactiva ≥35 d | total VERIFICAR | Res. 1888/2025 (prazo divergente), Res. 839/2017 | Alto (CO do psicólogo) | A prova de v1 sumiu | **5,5** | **TESTE** |
| 7 | PT/OT × EUA (kit de nota pago único) | Note Ninjas ≥4 d, 67 anúncios, assinatura US$34 | **283,7 mil PT (BLS 2025)** | Medicare: VERIFICAR | Médio (inglês) | CPM alto; concorrente é marca com podcast e comunidade | **5,0** | **TESTE** |
| 8 | Fisio × México | Recursos Salud Pro 374 d, Archivos Digitales Express 66 d, Formatos digitales 28 d (MXN, conteúdo VERIFICAR) | 53,5 mil (proxy superestimado) | NOM-004, sem prazo | Alto (MX do psicólogo) | Três vendedores MXN **sem conteúdo verificado** | **5,0** | **VERIFICAR antes de testar** |
| 9 | Heilmittelerbringer × DE/AT/CH | thevea EUR 394 d com modelos grátis | VERIFICAR | nenhum | Baixo (alemão) | Âncora grátis | **4,0** | Hold |
| 10 | Nutri × Espanha / Chile / Colômbia | Grulla 989 d (3 anúncios), Silvia Menéndez ≥48 d (nicho ?), NutriPack360 9 d; Vilboplanner é SaaS | **8.683 (ES)**; CL, CO: VERIFICAR | Ley 21.719 (data incerta) | Médio | Mercado pequeno e SaaS grátis | **4,0** | Hold |
| 11 | Kinesiólogo × Chile/Argentina | Ninguém de kit; Compra Digital Yaa 42 d (rehab, voseo) | CL 22.080 (2016) | Ley 21.719 incerta | Médio | Sem sinal claro | **4,0** | Hold |
| 12 | Personal trainer, TO, nutri IT/FR/DE/UK/US | só SaaS ou nada | grande | nenhum | — | Sem prova | **≤3,0** | Não |

---

## 8. TOP 6
1. **Pilates + yoga instrutor × espanhol (7,5, PROVADO).** O que mudou: Nua Studio estava em 29 d na v1 e **mede 53 d** (07/09), em CLP, 18 anúncios, com criativos "+100 clases listas para usar o adaptar". Isso fecha a prova que faltava no espanhol. O Clara Ríos (US$27, app, modo aula, upsells) é o benchmark de preço e de produto. Risco: 5 vendedores entraram em 7 dias.
2. **Fisioterapista × Itália (6,5, TESTE).** Nenhum kit; o formato kit+app já passou de 35 a 42 dias na IT com outras profissões. O DM 232/2023 está em vigor desde 16/03/2024: não é contagem regressiva.
3. **Geriátrica × espanhol neutro (6,5, PROVADO).** Geriactiva confirmado ≥35 d, 143 anúncios. Já tem 3 clones; sessão pronta, não papelada.
4. **Fizjoterapeuta × Polônia (6,0, TESTE).** Tamanho agora fechado: 64,6 mil (GUS 2025) a 75 mil (KIF 2022). 5 vendedores, nenhum com 30 d; Kamilka vence em tese só quando o gabinete atende crianças. Reavaliar em 15/11.
5. **Fisioterapeuta × Espanha (5,5, TESTE).** 74.990 colegiados, zero kit. Oceano azul, mas ninguém prova que fisio compra kit.
6. **Fisioterapeuta × Colômbia (5,5, TESTE).** Caiu de 6,5: o Kit de Documentos para Fisioterapeutas (nossa prova direta) está com 0 anúncios hoje.

## 9. Diferenças em relação à v1 (29/10)
- **Nua Studio: 29 d vira 53 d.** O pilates em espanhol agora é PROVADO e sobe de 7,0 para 7,5.
- **Kit de Documentos para Fisioterapeutas (CO): 10 anúncios vira 0 ativos.** Fisio CO cai de 6,5 para 5,5.
- **Vilboplanner resolvido:** é SaaS grátis (fundado 2023), os 511 d não provam kit.
- **The Note Ninjas resolvido:** assinatura Kajabi, US$34/mês, US$306/ano, não é kit.
- **Clara Ríos resolvido:** US$27 (de US$117), app, upsell Pro/prenatal/mayores.
- **Tamanho fechado:** EUA 283,7 mil (BLS), Polônia 64,6 mil (GUS)/75 mil (KIF), MX proxy 53,5 mil, Itália ~70 a 73 mil. Chile só 2016 (22.080).
- **Normas:** DM 232/2023 confirmado na GU (em vigor 16/03/2024, adaptação de 24 meses, secundária); Kamilka confirmada como aplicável a prestador de saúde com menores (comentário jurídico), prazo vencido 15/08/2024; Ley 21.719 do Chile passou a ter **postergação em tramitação** (dez/2027 pelo Executivo, out/2027 na comissão).
- **Novos vendedores/pistas:** Compra Digital Yaa (AR, 42 d), thevea (DE, 394 d, grátis), Archivos Digitales Express (MX, 66 d), Formatos digitales (MX, 28 d), Silvia Menéndez remedida (≥48 d, 63 anúncios), Fisioterapista Facile 49 d.
- **Geriactiva** subiu de ≥30 para ≥35 d e a nota 6,0 para 6,5 (3 clones, mas prova firme).

## 10. O que continuou VERIFICAR
1. **Recursos Salud Pro** (MXN, 374 d): anúncio de catálogo dinâmico sem conteúdo; página sem texto; web sem resultado.
2. **Archivos Digitales Express** e **Formatos digitales** (MXN): conteúdo e preço.
3. **Preço e conteúdo do Geriactiva**, NutriPack360, Zgodny Gabinet (além de 199 zł), Nua Studio, FizjoTeczka, Compra Digital Yaa: o navegador embutido foi usado por outro agente em paralelo e os anúncios com filtro de país BR escondem os que não rodam no Brasil.
4. **Idade real do Note Ninjas** (67 anúncios, só vi os 50 mais novos, o mais antigo visto 26/10) e do Sophie Collins (57 anúncios).
5. **Nicho da Silvia Menéndez** (63 anúncios, "Kit de Plantillas").
6. **Totais:** fisio na Colômbia (ReTHUS/SISPRO), fisioterapeutas puros no México (cédulas SEP), kinesiólogos atuais no Chile (RNPI), total atual na Itália (albo FNOFI) e número oficial KIF da Polônia 2025.
7. **DM 232/2023:** texto do artigo transitório e mínimos por profissão (só fonte secundária); se fisioterapista e dietista estão no escopo nominal.
8. **Res. 1888/2025 (CO):** data de obrigatoriedade para profissional independente.
9. **Reforma da Ley General de Salud (MX)** de 15/01/2026: número do DOF.
10. **Medicare/Medicaid documentation** (EUA) como gancho: não pesquisado.
11. **Osteopata, quiropraxista, podólogo, massoterapeuta** e outros países (RO, NL, TR, CZ): não varridos. **SearchAPI está em 10.000 de 10.000 e só renova em 08/11;** as buscas em RO, NL, UK/AU além do que consta na §5 ficaram sem fazer.
12. **Aplicação da Kamilka a gabinete de fisio** sem pediatria: a fonte oficial não cita fisioterapia nominalmente.

## Fontes
- Meta Ads Library (conector `ads_library_search`), consultas de 30/10/2026, client_conversation_id `Ft7Nq2Wx9Lk4Rb8Zc3Vy`; ad de Clara Ríos aberto na Biblioteca (id 893002270473872, início 27/10/2026)
- Sites: [clarariospilates.shop](https://clarariospilates.shop), [thenoteninjas.com](https://www.thenoteninjas.com), [Kajabi membership](https://thenoteninjas.mykajabi.com/membership)
- Tamanho: [INE EPSC 2025](https://ine.es/dyngs/Prensa/EPSC2025.htm), [BLS](https://www.bls.gov/ooh/healthcare/physical-therapists.htm), [Bankier/GUS](https://www.bankier.pl/wiadomosc/W-Polsce-przybywa-medykow-Najnowsze-dane-GUS-9187857.html), [DataMéxico](https://www.economia.gob.mx/datamexico/es/profile/occupation/tecnicos-en-aparatos-de-diagnostico-tratamiento-medico-podologos-y-fisioterapeutas), [Superintendencia de Salud CL](https://www.superdesalud.gob.cl/664/articles-14280_recurso_1.pdf), [Quotidiano.net](https://www.quotidiano.net/news/fisioterapia-la-riabilitazione-in-italia-i-numeri-dei-fisioterapisti-l6rhr1lk)
- Normas: [GU DM 232/2023](https://www.gazzettaufficiale.it/eli/id/2024/03/01/24G00032/sg), [partitaiva.it](https://www.partitaiva.it/responsabilita-professionale-sanita), [OPI Palermo](https://www.opipalermo.it/images/pdf/2026/nuovo_triennio_ECM_26-28.pdf), [gov.pl Kamilka](https://www.gov.pl/web/sprawiedliwosc/ustawa-kamilka--standardy-ochrony-maloletnich), [Minsalud Res. 1888/2025](https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/resolucion-1888-de-2025.pdf), [Economía NOM-004](https://platiica.economia.gob.mx/normalizacion/nom-004-ssa3-2012/), [Carey](https://www.carey.cl/gobierno-ingresa-proyecto-de-ley-que-posterga-en-un-ano-entrada-en-vigor-de-la-ley-sobre-proteccion-de-datos-personales), [Pauta](https://www.pauta.cl/actualidad/2026/10/02/ley-de-datos-personales-senadores-proponen-prorroga-de-seis-meses-frente-al-ano-que-pide-el-gobierno.html)
- Vilboplanner: [Diario Estrategia](https://www.diarioestrategia.cl/texto-diario/mostrar/5034441/vilbo-planner-revolucion-planificaciones-alimentarias-nutricionistas)
