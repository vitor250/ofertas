# Fitness, nutrição e fisioterapia por país (v2, 30/10/2026)

> Status: EM ANDAMENTO (arquivo gravado aos poucos).

## Avisos de método
- A v1 de 29/10 (`pesquisas-nichos-2026-10-29/fitness-nutricao-fisio.md`) NÃO estava acessível neste ambiente (container na nuvem, sem o Desktop). Usei só a lista de VERIFICAR escrita no prompt e as notas do usuário.
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). Toda medição de anúncios foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
- Régua: PROVADO = anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.

## 1. Base Brasil (o que já vende aqui, EscalaLow)

Fonte: `dados/escalalow-ofertas-validadas.json` (V = índice na lista de 213) e `dados/escalalow-ofertas-24-10.json` (C = índice na coleta de 24/10). Dias e ativos como o EscalaLow registrou; não remedi no Brasil.

| Oferta BR | Nicho | Dias | Ativos | Preço | Fonte |
|---|---|---|---|---|---|
| Documentos Prontos para Consultoria em Alimentos (Domine a Nutrição) | nutricionista (UAN/consultoria) | 54 | 50 | R$ 8 | V30 / C248 |
| Combo Vitalício de Documentos para UAN, Consultoria, ILPIs, Creches (Domine a Nutrição) | nutricionista | 30 | 8 | R$ 79,90 | C899 |
| Kit de Estimulação Cognitiva (Neuromente) | idosos / estimulação | 165 | 22 | R$ 10 | C97 |
| +160 Atividades para Idosos (Cantinho das Atividades) | idosos | 61–65 | 9–11 | WhatsApp | V194 / C607 |
| +120 Fichas de Estimulação Cognitiva para Idosos (Professora Maria) | idosos | 21 | 1 | R$ 17,90 | C1918 (já anuncia em espanhol, ver 2.1) |
| Pilates Pro: 150+ Aulas Prontas (Ana Martins Pilates) | pilates | 47–58 | 22–35 | R$ 10 | V87 / C244 (já anuncia em Portugal a €5, ver 2.3) |
| Documentos de Psicomotricidade (Tia Su) | psicomotricidade | 118 | 20 | R$ 15,90 | V99 |
| 150 Mapas Mentais de Cinesiologia (Edufisicavisual) | estudante/profissional de ed. física | 58–62 | 23 | R$ 17,90 | V80 / C728 |
| +100 Planilhas de Fisioterapia Respiratória (Luisa Souza) | fisioterapeuta | 15 | 61 | R$ 10 | C243 |
| Super Kit (Natália Oliveira, fisioterapeuta) | fisioterapeuta | 19 | 31 | R$ 19,78 | C353 |
| Fichas de Musculação (ed_fisicadozero) | personal trainer | 187 | 4 | R$ 27 | C423 |
| +150 Atividades de Terapia Ocupacional (T.O. Na Prática) | terapeuta ocupacional | 82 | 6 | R$ 27 | C580 |
| Kit Profissional com 25 Fichas para Fisioterapeutas; +100 Documentos para Fisioterapeutas; Biblioteca do Fisio Domiciliar; Kit Quiropraxia; Kit Massoterapia; 60 Protocolos de Quiropraxia | fisio e afins | 3–29 | 0–10 | R$ 10–47 | C908, C1664, C760, C1867, C965, C1130 |

Leitura: no Brasil o que passa de 30 dias com volume é nutrição-consultoria (R$ 8), idosos/estimulação (R$ 10), pilates (R$ 10) e psicomotricidade. Fisioterapia tem muitos kits novos (≤30 d) e mais um entrando hoje (Acervo Digital, "+100 Documentos Prontos para Fisioterapeutas", page 1413431898512137, BRL, <1 d). O Brasil está saturado; a brecha está em levar idosos, pilates e nutrição para fora.

## 2. Medições por país (conector Meta)

Limites do conector percebidos nesta rodada (valem para toda a tabela):
- Ele devolve só os 50 anúncios mais recentes de cada página. Em página com mais de 50 ativos, os dias medidos são um PISO (o anúncio mais antigo pode estar fora da janela).
- A moeda é a da conta de anúncio, não a do país. O filtro `countries` mostra onde o anúncio é entregue.
- Não devolve o texto do anúncio nem a URL de destino, só o título do link. As páginas de vendas não puderam ser abertas: o proxy deste container bloqueia hotmart.com, kiwify.com.br, facebook.com, lovable.app e quase todos os domínios. Preço e conteúdo vêm do título do anúncio, do EscalaLow ou de busca web; o resto fica VERIFICAR.

### 2.1 Espanhol (LATAM + Espanha)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Geriactiva (1259324537268785) | geriatria / estimulação para profissionais | 143 (ES 71, MX 73, CO 71, US 56) | ≥ 8,8 (piso; 50 visíveis) | USD | "+3000 Profesionales lo recomiendan"; lotes de ~20 criativos em 20/10, 23/10 e 26/10 | ESCALANDO; dias VERIFICAR |
| Recursos Digitales (1209103695610757) | estimulação cognitiva idosos | 20 | 56,7 | USD | "+500 actividades para mantener la mente activa"; "Recibe y luego pagas" | PROVADO em espanhol neutro (país VERIFICAR) |
| Lectura Integral (1333329899870943) | material terapêutico / idosos | 39 | 28,4 | BRL (operador BR) | "ACTIVIDADES LISTAS PARA TUS SESIONES"; "Material terapéutico listo para usar hoy"; "70% de descuento"/WhatsApp | quase 30 d; TESTE forte |
| Edad Activa (1472176509293820) + 2ª página (1409411995586158) | atividades para idosos | 4 (+?) | 0,3 | USD | "Más de 420 páginas de actividades para mayores" | TESTE (novo) |
| Mah Souza (255170671023979) | sessões para idosos/terapeutas | 8 | 0,5 | USD | "Deja de armar la sesión desde cero" | TESTE (novo) |
| Productos digitales (104654868925408) | sessões montadas | 6 | 1,8 | USD | "Sesiones armadas, no ejercicios sueltos" | TESTE (novo) |
| Dra. Sofía Mendonza (1094102817110121) | atividades/exercícios | VERIFICAR | ~2 | BRL (operador BR) | "MÁS DE 1.000 ACTIVIDADES LISTAS PARA APLICAR"; "DEJA DE PERDER HORAS BUSCANDO EJERCICIOS" | TESTE |
| Clara Ríos · Pilates y Yoga (1325918880615223) | pilates/yoga (app) | 15 | 2,7 | USD | "50 clases listas para dar · +220 ejercicios con ficha · Modo clase · 5 regalos · en tu teléfono o tablet · pago único" | TESTE (novo) |
| Pilates con Método (827226377138589) | pilates reformer | 6 | 0,6 | USD | "Tu próxima clase de Reformer, sin improvisar"; "Que tus alumnas entiendan tus indicaciones" | TESTE (novo) |
| Mesa de Luz (1319912451210896) | pilates | 2 | 0,8 | USD | "100 clases listas + 500 ejercicios" | TESTE (novo) |
| Yoga Flow (1181284751742069) | yoga/pilates | VERIFICAR | 47,0 (anúncio mais velho achado na busca) | BRL (operador BR) | link "(4.9/5) ⭐" | provável PROVADO em espanhol; conferir página |
| DigitalShop (112053687360360) | fisioterapia esportiva | VERIFICAR | 2,5 | USD | "FISIOTERAPIA DEPORTIVA" | TESTE |

| Mi Colega T.O (1485100974676859) | terapia ocupacional (infantil) | 14 | 2,2 | CLP (operador no Chile) | "+1.500 actividades por edad · +180 sesiones listas en 1 minuto · tareas para la casa · US$17,99" | TESTE (novo) |
| Grulla psicología y nutrición (101855774607522) | nutricionista (plantillas) | 3 (todos entregues na ES) | 1.021 (anúncio de plantillas: 989) | EUR | "Oferta de lanzamiento - Plantillas profesionales para nutricionistas" | PROVADO na Espanha, mas escala mínima (1 anúncio) |
| Onmymeal (552447564625410) | nutrição (produto VERIFICAR) | 21 (20 na ES) | 183,4 | EUR | "Pasa de la teoría a la práctica"; "Accede ahora" | PROVADO na Espanha; produto VERIFICAR (pode ser app/curso, não kit) |
| Vilboplanner (250580878147142) | software de planos alimentares (Chile) | ≥1 | ~510 | CLP | (sem título) | SaaS, não kit; concorrente indireto no Chile |
| InnovaFiles Bolivia (884254744781430) | treino/musculação | 3 | ~1,6 | USD | "MUSCULAR" | TESTE |

Leitura rápida (espanhol): há uma ONDA NOVA (últimos 3 dias) de páginas em USD com o mesmo estilo de copy ("Pagas una vez. Es tuya para siempre", "lista para dar", "sin improvisar") em pilates, yoga e idosos. Parece um mesmo operador ou escola testando vários nichos (VERIFICAR). Quem já passou de 30 dias é geriatria/estimulação cognitiva (Recursos Digitales 57 d; Geriactiva com 143 anúncios), yoga em espanhol de operador BR (Yoga Flow, 73 anúncios, ≥58,8 d, BRL; parece produto para consumidor, VERIFICAR) e nutrição na Espanha em euro (Grulla 989 d com 1 anúncio; Onmymeal 183 d com 20 anúncios).

Yoga Flow (1181284751742069): 73 ativos, BRL, todos com o título "(4.9/5) ⭐⭐⭐⭐⭐"; o mais antigo entre os 50 visíveis começou há 58,8 dias (piso).

### 2.2 Italiano (IT)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Palestra Mentale (1389699987550571) | estimulação cognitiva / laboratórios para idosos (RSA, animadores) | 11 | 15,4 (piso; 10 visíveis) | USD | "Un anno di laboratori, pronto da stampare" | TESTE |
| Seduta Pronta (1447072035149109) | sessões prontas (estimulação/terapia) | ≥3 | ~1,7 | USD | "La seduta di domani, già pronta" | TESTE (novo) |
| The Mind Market (884241854764422) | sessões de estimulação | ≥1 | ~1,7 | USD | "96 sedute pronte da stampare" | TESTE (novo) |
| The Resource Lab (1123744187496255) | volumes de atividades | ≥4 | ~1,8 | USD | "6 volumi + 5 volumi speciali" | TESTE (novo) |
| Elena Costa (1482290864957903) | apareceu em "lezioni di pilates pronte"; produto VERIFICAR | 11 | ≥3,5 | USD | "ACCEDI ORA 🚨" | TESTE |
| Amelia Parker (1202102249654273) / Aulaprima italy (1385548604641382) | parecem kits para professores, não pilates (VERIFICAR) | — | ~1,8 | USD | "Mai più la pagina bianca: un anno già pronto"; "⭐ 4.8/5" | fora do nicho |
| busca "fisioterapisti modelli pronti" | fisio | 0 | — | — | nenhum anúncio ativo | BRECHA (fisio IT) |

| Beatriz Molina (1183938618138560) | exercícios ilustrados (parece consumidor) | ≥4 | ~2,8 | BRL (operador BR) | "Oltre 50 Esercizi Illustrati" | TESTE |
| buscas "personal trainer schede pronte" e "nutrizionisti modelli piano alimentare" | personal / nutricionista | 0 | — | — | nenhum anúncio ativo | BRECHA |

Leitura (Itália): a mesma onda em USD chegou à Itália em outubro, focada em estimulação cognitiva para idosos (4 páginas, a mais velha com 15 dias). Para fisioterapista, personal e nutricionista italianos não há kit anunciado.

### 2.3 Português de Portugal (PT)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Ana Martins Pilates (1107888629075356) | pilates (o mesmo vendedor BR do EscalaLow) | 15 | 45,8 (anúncios "por R$10", Brasil) / 8,3 (anúncio "por apenas 5 €") | USD | "150+ Aulas de Pilates por apenas 5 €" | BR PROVADO; PT TESTE (8 d) |
| Centerline Pilates Portugal (1381045968429098) | pilates | ≥10 | ~0,7 | USD | "100 aulas de 60 min prontas + 500 fichas de exercícios" | TESTE (novo) |
| GeriActive Portugal (1433767279817412) | atividades para idosos | 10 | ~0,8 | USD | "1.320 atividades prontas para idosos" | TESTE (novo) |
| DrFabiotrigo (105561912305385) | prescrição de exercício para profissionais de saúde (PT-PT) | ≥3 | ~0,2 | BRL | "Profissional da saúde, vais continuar a 'apagar incêndios' com prescrições curtas?" | TESTE |

### 2.4 Francês (FR/BE/CH/CA)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Cris Staruck - Flow Pilates Pro (1336633782860996) | pilates (kit para instrutoras) | 13 | ≥6,5 | EUR | "Flow Pilates Pro · Le Kit pour Enseignantes" | TESTE |
| The Resource Lab (1123744187496255) | programas/fichas de acompanhamento (idosos? VERIFICAR) | ≥3 | 12,7 | USD | "4 semaines de programme, prêtes à afficher"; "Vos fiches de suivi, déjà prêtes" | TESTE |
| NeuroXtrain (633138870474876) | software de treino cognitivo para kinés | ≥1 | ~211 | EUR | "Essai gratuit pendant 7 jours" | SaaS, não kit |
| busca "kinésithérapeutes fiches exercices" | kiné | só o SaaS acima | — | — | — | BRECHA de kit |

### 2.5 Alemão (DE/AT/CH)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Stundenfertig (1306841592522454) | pilates (aulas prontas) | ≥11 | ~1,9 | USD | "104 fertige Stunden + 410 Übungen" | TESTE (novo) |
| buscas "Senioren Beschäftigung…", "Aktivierung Senioren Vorlagen", "Pilates Stundenbilder fertig" | idosos / pilates | 0 | — | — | nenhum anúncio ativo | BRECHA (idosos DE) |

### 2.6 Polonês (PL)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Centerline Pilates PL (1395412080322675) | pilates (konspekty) | 40 | 14,2 | USD | "100 gotowych konspektów + 500 ćwiczeń"; lotes de criativos em 15/10, 20/10, 23/10 e 26/10 | TESTE escalando |
| GeriActive Polska (1384620951405497) | atividades para idosos | ≥6 | ~0,7 | USD | "1 320 gotowych zajęć dla seniorów" | TESTE (novo) |
| "100 wizualnych map bólu rzutowanego i punktów spustowych" (1210544588816989) | fisio/massagem (mapas de dor referida e trigger points) | 2 | 60,7 | USD | "⭐⭐⭐⭐⭐" | PROVADO na PL (escala mínima) |
| Marek Kowalczyk (1071799122688949) | treinador de futebol (exercícios) | ≥4 | ~0,5 | USD | "Ćwiczenia nagrane z drona – tylko 19 zł" | TESTE |

### 2.6b Espanhol: México, nutrição, yoga, personal (complemento)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| Recursos Digitales (1209103695610757), por país | idosos | PE 6 · MX 3 · outros LATAM 9 · ES 0 · CO 0 · US 0 | PE 56,7 · MX 20,8 | USD | "+500 actividades para mantener la mente activa" | PROVADO no PERU |
| Recursos Legales PRO Salud Mx (880855681786807) | kits legais de saúde MX | 5 | 98,8 | MXN | "Kit Consultorio Médico $499 · Kit Cirujano Dentista $499 · Kit Legal Psicología $499 · Spas y Cosmetología $699 · PNOs Farmacia $249–999" | PROVADO no MX; NÃO tem kit de fisio, nutriólogo nem pilates (brecha no catálogo dele) |
| Media Center México (102603028861491) | megapack (inclui nutrição) | 56 | 30,2 (anúncio de nutrição) | MXN | "+4,000 Archivos de nutrición por $99 pesos" | PROVADO no MX, mas é pacotão genérico |
| NutriKits (293707977159186) | nutriólogos | 1 | 6,0 | MXN | "70 kits para nutriólogos desde $50" | TESTE |
| LearnFit Institute (276123018926219) | guia profissional | ≥2 | ~0,2 | MXN | "Salud muscular y longevidad: guía profesional" | TESTE |
| Alma Yoga - Clases para Profes (1378014005397795) | instrutor de yoga | 1 | 0,9 | ARS (Argentina) | "100 clases completas para enseñar sin planificar de más" | TESTE |
| Yoga reset (1371307229398990) | instrutor de yoga | ≥3 | ~1 | USD | "Clases listas para dar"; "Precio lanzamiento" | TESTE |
| Professora Maria (1407583632419764) | idosos (vendedora BR em espanhol) | VERIFICAR | ~1,8 | BRL | "Fichas Visuales de Estimulación Cognitiva para Adultos Mayores" | TESTE |
| buscas "entrenadores personales plantillas rutinas clientes" | personal trainer | só apps (MoveUp Digital, Stenfit) | — | — | — | BRECHA de kit |

### 2.6c Inglês (US/GB/AU/CA)

| Página (page_id) | Nicho | Ativos | DIAS REAIS | Moeda | O que o anúncio diz | Régua |
|---|---|---|---|---|---|---|
| The Note Ninjas (120478321017238) | documentação para fisio (PT) e terapeuta ocupacional (OT) | 67 | ≥3,2 (piso; os 50 visíveis são de 26–29/10) | USD | "Stop Writing Notes From Scratch"; "Still Writing Notes at Home?"; "Write Notes With Confidence" | ESCALANDO; dias VERIFICAR (marca existe desde pelo menos mai/2025, segundo podcast achado na busca) |
| ClassReady Studio (1414757318380882) | pilates (versão em inglês da Clara Ríos) | ≥10 | 3,5 | USD | "50 classes ready to teach + 220 exercises" | TESTE |
| buscas "activity director seniors printable", "dementia activities printable caregivers", "dietitian handouts templates", "personal trainers client workout templates" | idosos / nutrição / personal | 0 (só um lead magnet da Trainer HQ, AUD) | — | — | — | BRECHA em inglês (ou demanda fora do Meta) |

### 2.7 O operador multipaís (achado principal da v2)

Os mesmos produtos aparecem com nome local e o mesmo número de itens em vários idiomas, todos em USD:
- Pilates "100 aulas + 500 exercícios": Centerline Pilates PL (14 d, 40 anúncios) → Centerline Pilates Portugal (0,7 d) → Mesa de Luz ES (0,8 d, "100 clases + 500 ejercicios") → Stundenfertig DE (1,9 d, "104 Stunden + 410 Übungen").
- Idosos "1.320 atividades": GeriActive Portugal e GeriActive Polska (ambos <1 d). Geriactiva em espanhol (143 anúncios, "+3000 profesionales") parece ser a matriz, mas os dias reais dela ficaram fora da janela do conector (VERIFICAR).
- O estilo de copy ("lista para dar", "en 1 minuto", "pagas una vez") se repete em Clara Ríos, Mi Colega T.O, Pilates con Método, Seduta Pronta, Palestra Mentale. Pode ser o mesmo grupo ou o mesmo "molde" de IA. Não dá para afirmar o dono (VERIFICAR).
Implicação: pilates e idosos estão sendo testados AGORA em ES/PT/PL/DE/IT/FR por um concorrente com escala de criativos. Ninguém além dele passou de 30 dias nesses países, exceto Recursos Digitales (espanhol, 57 d) e Geriactiva.

## 3. Concorrentes da v1 (VERIFICAR conteúdo/preço)

As páginas de vendas não abriram (proxy bloqueia o domínio delas, Hotmart e Kiwify). O que segue é o que o conector Meta e a busca mostraram; preço só onde aparece no título do anúncio.

| Concorrente | O que foi confirmado | Preço | Ainda VERIFICAR |
|---|---|---|---|
| Recursos Salud Pro | Nome exato não existe na Biblioteca. O mais próximo é "Recursos Legales PRO Salud Mx" (880855681786807, MXN): 5 ativos, 98,8 dias, catálogo de kits legais (consultório médico, dentista, psicologia, spas, PNOs de farmácia) | $249–999 MXN (no título) | se é o mesmo da v1; não vende kit de fisio nem de nutriólogo |
| Vilboplanner | SaaS chileno de planos alimentares para nutricionistas (page 250580878147142, CLP), anúncio ativo há ~510 dias. Imprensa chilena diz que a versão completa é gratuita para nutricionistas (diarioestrategia.cl) | grátis (segundo a imprensa) | planos pagos; não é kit, é concorrente indireto |
| The Note Ninjas | Documentação para PT/OT nos EUA, 67 anúncios ativos, USD, lotes de criativos em 26, 27 e 29/10 | não aparece | preço, conteúdo e dias reais (janela do conector só mostra 3 dias) |
| Clara Ríos · Pilates y Yoga | 15 ativos, 2,7 dias, USD. Produto é app: "50 clases listas para dar · +220 ejercicios con ficha · Modo clase · 5 regalos · en tu teléfono o tablet · pago único". Gêmeo em inglês: ClassReady Studio | não aparece | preço; se a v1 viu outra página mais velha (esta tem só 3 dias) |
| Nua Studio | Não encontrado pelo nome na Biblioteca (a busca por "Nua Studio" devolve só ruído) | — | page_id da v1 |
| Geriactiva | 143 ativos, USD, "+3000 Profesionales lo recomiendan", entrega em ES (71), MX (73), CO (71), US (56). Lotes de ~20 criativos a cada 3 dias. Clones "GeriActive Portugal" e "GeriActive Polska" ("1.320 atividades prontas") abertos em 29/10 | não aparece | dias reais (passa de 50 anúncios, o conector não mostra o mais antigo); preço |

## 4. Tamanho de mercado e normas (fontes oficiais)
(preenchendo)

## 5. Ranking 0–10
(preenchendo)

## 6. Lista final de VERIFICAR
(preenchendo)
