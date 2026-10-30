# Mapas mentais, esquemas, resumos, flashcards e simulados por país — v2 (30/10/2026)

> Status: CONCLUÍDO em 30/10/2026. Top 3: ES oposiciones em esquemas + app (7,5) · PL matura (7,0) · DE Einbürgerungstest em língua de imigrante (6,0) — empate com CO simulacros CNSC/DIAN (6,0).

## Avisos de método
- A v1 (`mapas-mentais-por-pais-2026-10-29.md`) NÃO estava acessível neste ambiente. Usei a lista de candidatos e os pontos a VERIFICAR escritos no próprio prompt e nas notas do usuário.
- SearchAPI indisponível (sem chave aqui e sem crédito até 08/11/2026). Medição feita com o conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por page_id). Nº de anúncios = `estimated_total_count` na busca por page_id.
- WebFetch bloqueado pela lista de rede da sessão (falhou em `portaloswiatowy.pl` e `ncsbn.org`; para abrir páginas de vendas e fontes oficiais, esses domínios precisam ser liberados nas configurações de rede). Por isso preços de página de vendas ficaram VERIFICAR e datas/números vêm de busca web com a fonte indicada.
- Limite do conector: mostra no máximo 50 anúncios por consulta; em páginas com mais de 50 anúncios a idade é "≥ X dias".
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.

## Contexto BR (referência do formato, base EscalaLow)
O formato "mapa mental / resumo esquematizado / simulado" está validado no Brasil (dados EscalaLow do repositório, dias = idade do anúncio mais antigo segundo o EscalaLow; não medi de novo):
- Validadas (213): Mapeei "Mapas Mentais" 89 d / 13 anúncios / R$ 67; Supermapas de Língua Portuguesa 88 d / 12 / R$ 57; "Resumo Esquematizado" (Abordagens da Psicologia) 70 d / 16 / R$ 37; "150 Mapas Mentais de Cinesiologia" 62 d / 23 / R$ 17,90.
- Coleta 24/10 (1.946): "Mapas Mentais" concursos 147 d / R$ 67; "+221 Simulados SAEB" 135 d / R$ 14,90; "Mapa Mental para Concurso" 121 d; "50 Mapas Mentais de RLM" 81 d / R$ 9,90; "SEDUC CE em Mapas Mentais" 66 d / R$ 67; "Apostila Visual" 51 d / 34 anúncios / R$ 37; "+500 resumos de Direito" 39 d / 41 anúncios / R$ 19,90; "+150 Mapas Mentais de Neurociência" 28 d / 43 anúncios / R$ 10; "Mapa da Aprovação" 26 d / R$ 47; "Mapas Mentais de Italiano" 519 d (0 ativos em 24/10).
- Padrão BR que está sendo exportado agora (ES, IT, MX neutro): "Mapa da Aprovação [cargo/órgão] 2026", "Constituição em X páginas", "+N mapas mentais de [disciplina]", R$ 10–67.

## Medição por candidato

### ES — oposiciones (esquemas, resúmenes, leyes visuales, test)
Busca `esquemas oposiciones` (ES, ativos): 82 anúncios. Em espanhol o termo que vende é "esquemas"/"resumen esquematizado"/"leyes ilustradas"; `mapas mentales oposiciones` só devolve 4 anúncios (academias policiais).

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| OpoEsquemas (319121182004656) | 149 | 3 | EUR | "Cuaderno Resúmenes MEGARESUMIDO" Administrativo del Estado + libros de tests + temario + curso FOCUS AGE | PROVADO (pouca escala) |
| OposTime (102294982452223) | 139 | 14 | EUR | "Temario resumen esquematizado en menos de 150 páginas" AGE e Local (OpoZip), leyes compiladas, cuadernos, planificadores | PROVADO |
| Opocaos (108681508359960) | 139 | 23 | EUR | "Opoleyes" (leis resumidas/visuais), "temario perfecto si te falta tiempo" | PROVADO |
| Editorial-esquematizate.es (106101570913247) | 83 | 18 | EUR | Temarios resumidos 2027 por especialidade (Educación Infantil, PT, FP: Estética, Peluquería, Cocina, Procesos Sanitarios, FOL…), com "muestra gratis" | PROVADO |
| Leyes.Bonitas (1127329127123304) | 83 | 10 | EUR | Leis ilustradas (Constitución, Función Pública AGE, Legislación Penitenciaria), Constitución em canções, agenda-planificador | PROVADO |
| Academia Prefortia – Guardia Civil (1470045239962805) | 62 | 36 | EUR | Academia GC: curso + "Guía Estrella" (isca) + "Libro Resumen" ascenso/ingresso + "guía visual para organizar tu estudio" | PROVADO (academia, não low ticket puro) |
| OpoFlow (1119118684610412) | 53 | 4 | EUR | "La Constitución Española, hecha visual", "El Código Penal más fácil de estudiar" | PROVADO (pouca escala) |
| Emma Schneider (1290103417523122) | 13 | 13 | **BRL** | "La Constitución entera en 42 páginas / 42 esquemas", "Un tema. Una página." | TESTE — operador BR clonando o formato BR para ES |
| Luiza Fontenelle (101871606032485) | 2 | 30 | **USD** | "El Mapa del Celador SERGAS 2026" (30 criativos lançados em 27/10) | TESTE — operador BR (nome BR), formato "Mapa da Aprovação" traduzido |
| Nuvora Digital Store (1288382994365212) | 1 | 26 | EUR | Multinicho: "La Constitución en esquemas + 300 test", guia de nacionalidad (CCSE/DELE, "Guía + 3 bonus por 14,90 €"), arraigo, NIE/TIE, air fryer | TESTE (loja multinicho nova) |

Leitura: ES tem 5+ vendedores nativos em EUR com 80–150 dias no formato "resumen esquematizado / ley visual" — o formato está PROVADO em ES. O sinal novo de outubro é a chegada de operadores BR (Emma Schneider em BRL desde 16/10; Luiza Fontenelle em USD desde 27/10 com 30 criativos; Nuvora em EUR desde 28/10), todos com o tema "Constitución en esquemas" ou "Mapa del [cargo] [órgão] 2026". Ou seja, a brecha ES está sendo ocupada AGORA.

### PL — matura (notatki, pewniaki, pytania jawne)
Busca `matura notatki` (PL, ativos): 183 anúncios. `mapy myśli` não funciona como termo (devolve ruído; a busca não é por frase exata). O formato que vende na Polônia é "notatki / opracowania / pewniaki / gotowe odpowiedzi do pytań jawnych" em PDF.

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| ZaufanyNauczyciel.pl (838665652654203) | ≥196 (o mais antigo achado é de 16/04/2026; a página tem 105 anúncios e o conector só mostra 50 por consulta — achei os antigos filtrando "2026") | 105 | PLN | "Kompletne notatki" biologia/química/matemática 2027, "Pewniaki maturalne" (questões que voltam, análise de 16 anos CKE), "76 gotowych odpowiedzi do pytań jawnych" (oral de polonês), E8 (egzamin ósmoklasisty), "1000 najważniejszych słówek" em vários idiomas | **PROVADO forte** |
| Matura 2027 – notatki i opracowania (794313660745548; marcas ArkuszeMaturalne / eNotatki.pl) | 175 | 29 | PLN | "Pytania jawne 2027–2028 — odpowiedzi PDF", "500+ pojęć z polskiego w jednym PDF-ie", motywy literackie PDF, geografia/WOS/angielski PDF | **PROVADO** |
| Na Maturkę (817139971479324) | 6 | 2 | PLN | "bohaterowie lektur bez wkuwania" | TESTE |
| Outros na busca (cursos/aulas, não PDF): Maturoliza, Lekarski w Rok, matematykagryzie/biologiagryzie, Anna Pajdak, Akademia Geografii, EduMatura (EUR) | — | — | PLN | cursos e mentorias | contexto |

Leitura: PL é o mercado mais PROVADO do formato fora do BR/ES — dois vendedores puros de PDF com 175–196+ dias e 29–105 anúncios em PLN, com gancho de calendário oficial ("pytania jawne 2027", "matura 2027"). Concorrência alta e nativa. Brecha possível só em subnicho (ex.: mapas visuais/flashcards de lektury, E8) — VERIFICAR.

### US — NCLEX (enfermagem) e real estate
Busca `NCLEX study guide` (US, ativos): 271 anúncios. Busca `real estate exam cheat sheet` (US): 55 anúncios, quase todos de lojas genéricas recém-lançadas.

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| My Nurse Notes (107734932379817) | ≥84 (mais antigo visível 06/08/2026; 56 anúncios, conector mostra 50) | 56 | USD | "NCLEX Review Cheat sheet 400 pages", flashcards de farmacologia e Med-Surg (270 cards), bundle impresso + digital; criativo "Nursing Textbooks are Scam!" | **PROVADO** |
| Nurse In The Making (102048951224762) | ≥10 visível (57 anúncios; os 7 mais antigos não aparecem) — VERIFICAR | 57 | USD | Flashcards (Mental Health, Med-Surg), Pharmacology Pocket Guide, Clinical Badge Card Pack, planner, "NCLEX Study Notebook", bundle completo | PROVADO provável (marca conhecida; idade VERIFICAR) |
| Bigdawgrn (824044447462407) | não medido | — | USD | "The Ultimate NCLEX Content Bundle — $49.99" | VERIFICAR |
| Nursing Nerds, The Nurse Sam, Stethoscope to Success, NurseNessa.com | não medidos | — | USD | iscas grátis ("FREE NCLEX guide") + upsell | contexto |
| Alexa Paige (1408123749050369) / Maya Bennett (1119367354591205) | ≤14 visível | vários | **CAD** | mesmo criativo "Read this if you're taking the NCLEX soon" em 2 perfis com nome de pessoa → operação de clonagem | TESTE |
| StarkLifestyle (1030020273527646) | ≥7 visível (52 anúncios) | 52 | USD | "32 páginas só com os tópicos mais cobrados", impresso com frete grátis, promo Black Friday; exame não identificado na lista (VERIFICAR se é real estate) | TESTE (físico) |

Leitura US: NCLEX é mercado grande e PROVADO, mas saturado de marcas nativas (cheat sheets 400 páginas, flashcards, bundles US$ 30–50) e já tem operação de clonagem chegando. Real estate: nenhum vendedor de "mapa/resumo" com 30+ dias achado pelo conector → só TESTE.

### IT — concorsi e "mappe mentali"
Buscas (IT, ativos): `mappe concettuali concorso` 15 anúncios; `concorso mappe schemi` 4; `mappe mentali` **547**. A página "Concorsi in Mappe" NÃO aparece com anúncio ativo no conector (nome não retornou nada em IT) → VERIFICAR se vende só orgânico.

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| Tilde Insegna (1186367151235833) | 24 | 19 | EUR | curso preparatório "Allievi Finanzieri 2026" + "Niente banca dati? Niente panico!" (curso, não mapa) | TESTE |
| concorsi_essentials (1352120907985299) | 3 | 3 | EUR | "ASMEL · Istruttore amministrativo" (página com erro "Pagina non trovata") | TESTE fraco |
| Quizly, Evolvelab, Peer4Med, AIMS (SSM27) | não medidos | — | EUR | quiz/cursos (medicina SSM, concursos públicos) | contexto |
| Lingua Chiara (1034177656443347) | 0–1 | ≥45 só na busca | **BRL/USD** | "520 mappe mentali · dall'A1 al C2" (idiomas) | TESTE — onda BR |
| Patricia Romero (1332152703318929) | 0–1 | ≥7 | USD | mesmo produto "520 mappe mentali A1–C2" | TESTE — clone do anterior |
| Laura Conti (1325287127343501) | 0 | ≥4 | USD | "50 mappe mentali" para preparar e expor discurso (oratória) | TESTE — onda BR |
| Living in Christ (581916825013915) | 0 | ≥2 | **BRL** | "Oltre 500 mappe mentali terapeutiche" (psicologia) | TESTE — onda BR |
| Studio Facile (1232011766670582) | 0 | ≥1 | USD | "Impara la Farmacologia Senza Giri di Parole" | TESTE — onda BR |

Leitura IT: não há vendedor nativo PROVADO de mapas/esquemas para concorsi achado pelo conector. Em 28–29/10 começou uma onda de operadores BR (moeda BRL/USD, nomes de pessoa italianos genéricos) traduzindo o catálogo BR de "mapas mentais" (idiomas, psicologia, farmacologia, oratória) para o italiano. Nenhum tem 30 dias → TESTE. O que provaria: algum deles ainda ativo em 28/11.

### MX — ENARM (residência médica)
Busca `ENARM` (MX, ativos): 180 anúncios. `mapas mentales ENARM`: 0. `mapas mentales medicina` (MX): 124, quase todos de operadores BR/LATAM em BRL/USD (espanhol neutro, não prova MX).

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| Nitidomed (1533871263132078) | 0–1 (anúncios de 29/10) | 4 | MXN | "48,000 tarjetas de Anki para el ENARM", um baralho ordenado por tema | TESTE |
| ENARM Digital 2.0 (107209685698321) | 7 | 8 | MXN | "Biblioteca ENARM 2027", "Nuevo Manual Dr Prieto 2027" (manuais em PDF — risco de material de terceiros/pirataria, VERIFICAR) | TESTE |
| Koplik (114467433795180) | 1–2 | 12 | MXN | "Deja de olvidar lo que estudias para el ENARM" (repetição espaçada) | TESTE |
| Enarm en tus manos 2027 / Enarm Entusmanos | não medidos | — | MXN | "Manuales para ENARM en digital 2027" | VERIFICAR (mesmo risco de manual de terceiros) |
| Reto MD, Praxis MD, PROEDUMED, ENARM CONSALUD, ENARMPass, Zailo | não medidos | — | MXN | casos clínicos diários, apps com trial grátis, cursos | contexto (concorrência de app/curso) |
| Semiología en Mapas (1386834697836743) | 7 | ≥7 | USD | mapas de semiologia (espanhol neutro) | TESTE neutro |
| Revisión Medicina (846281265228814), Sophie Laurent, Daniel Herrera, Bela IA Studio | 1–9 | vários | **BRL** | "Mapas mentales de medicina", "210 Trastornos Mentales", "Bioquímica en resúmenes visuales" | TESTE — operadores BR em espanhol neutro |

Leitura MX: o ciclo ENARM 2027 começou agora (anúncios de 7 dias para cá); nenhum vendedor de mapa/resumo/flashcard com 30+ dias achado pelo conector. Muita concorrência de apps e cursos em MXN. Nitidomed (Anki) acabou de entrar. → TESTE, com gancho de calendário (ENARM em setembro).

### Bíblia em mapas (espanhol)
Busca `mapas de la Biblia` (todos os países, ativos): **362** anúncios — quase todos de operadores BR (BRL/USD).

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | Alcance | O que vende | Régua |
|---|---|---|---|---|---|---|
| Mapa Didactico de la Biblia (958179187385380) | **257** (desde 14/02/2026) | 20 | **BRL** | os 20 anúncios entregam em MX **e** ES (filtro por país); 0 nos EUA | mapa didático da Bíblia, criativo "Calidad garantizada 4.9/5" | **PROVADO em espanhol neutro** (operador BR); não prova um país só |
| Código Divino Inmaculado (1272486079272719) | 110 | ≥1 | BRL | não medido | estudo bíblico visual ("Miles ya han transformado su manera de estudiar la Palabra") | PROVADO neutro |
| Helena Martins (167183929822437) | 0 | 1 | BRL | — | "¡Toda la Biblia en 66 Mapas Visuales!" | TESTE |
| Mundo Bíblico 3D (1011681425371712) | 0–1 | ≥15 | USD | — | "Entiende mejor la Biblia viendo el mundo donde ocurrió" | TESTE |
| La Biblia Revelada, Tiendova ("La Biblia en el orden en que pasó"), Renata Sampaio, Mateo López ("73 libros de la Biblia católica"), Fe y Devoción Católica ("El mapa de la Biblia en tu celular"), Mapas da Sabedoria | 0–2 | vários | BRL/USD | — | variações de Bíblia visual/cronológica/católica | TESTE — enxame BR |

Leitura: o formato está PROVADO (257 dias) mas é 100% operação BR em espanhol neutro e o nicho está lotado (362 anúncios, enxame de clones lançado em 28–29/10). Não é brecha; só entraria com ângulo novo (ex.: versão católica 73 livros, versão por país, PT-PT/IT/PL). → baixa prioridade.

### CO — DIAN / CNSC (concurso público e docente)
Busca `CNSC simulacro` (CO, ativos): 15 anúncios. Dois ganchos ativos agora: **DIAN 2676** (processo de seleção da DIAN) e **concurso docente "31.163 vacantes"** ("inscripciones: finales de noviembre").

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| Saber Más (1073930549136975) | **57** | 10 | COP | simulacros CNSC, concurso docente ("60/100 o quedas fuera", "31.163 vacantes: tu territorio ya tiene listón", "caso situacional", "prueba funcional elimina") | **PROVADO** (simulado/treino) |
| Entrenameapp (656468064224101) | 23 | ≥1 | COP | "micro estudio simulacro para concurso CNSC" (app) | TESTE |
| Reto DIAN 2676 (1286354121238457) | 9 | ≥1 | COP | DIAN 2676 | TESTE |
| Simulacro DIAN (1298056520068783) | 7 | ≥3 | COP | simulacro DIAN | TESTE |
| TuempleoPublico.co (775793672285354) | 1 | 5 | COP | "Simulacros Reales DIAN 2676" | TESTE |
| Educate (110455697748108) | 0 | ≥1 | COP | "Simulacro DIAN 2676" | TESTE |
| Centro de Estudios Socio Jurídicos Latinoamericanos | 3 | ≥1 | USD | talleres DIAN 2676, Procuraduría, Rama Judicial | contexto |

Leitura CO: o formato que vende é SIMULACRO (não mapa). Há 1 vendedor PROVADO (Saber Más, 57 d) e um enxame de entrantes no DIAN 2676 (1–9 dias). Gancho de PRAZO: inscrições do concurso docente no fim de novembro (VERIFICAR data oficial CNSC). Mapas/esquemas visuais para DIAN/CNSC: ninguém achado → BRECHA de formato, mas a demanda comprovada é por simulado.

### DE — Einbürgerungstest (teste de naturalização)
Busca `Einbürgerungstest` (DE, ativos): 25 anúncios — mercado pequeno no Meta e majoritariamente em idiomas de imigrantes.

| Vendedor (page_id) | Dias reais | Anúncios ativos | Moeda | O que vende | Régua |
|---|---|---|---|---|---|
| Know Germany (1156789017512611) | **171** | 5 | USD | em **árabe**: "baixe as perguntas do Einbürgerungstest e como se preparar" + teste de direção alemão | **PROVADO** (nicho por idioma, escala pequena) |
| Migrando (1855211144766647) | 23 | ≥1 | EUR | "Seit 2021 in Deutschland? Dann könntest du jetzt dran sein" (naturalização) | TESTE |
| Zestly (867437046460842) | 3 | ≥1 | EUR | "Einbürgerungstest с объяснениями по-русски" (em russo) | TESTE |
| Studovo (1317599128113052) | 1 | 6 | EUR | "Alles für B1 + Einbürgerungstest" | TESTE |
| sherbime_berlin (1044053968795102) | ≥196 (anúncio de 16/04) | ≥1 | EUR | serviços em albanês (link Instagram) | contexto |
| Quiz Box / SolvedLib / Nông Băng | — | — | USD | quizzes de cidadania dos EUA em alemão (iscas) | ruído |

Leitura DE: ninguém vende material nativo em alemão com escala; o único vendedor antigo (171 d) vende **em árabe**; entrantes de outubro em russo e B1+teste. Brecha real = Einbürgerungstest explicado na língua do imigrante (turco, árabe, ucraniano, russo, português?) em formato mapa/flashcard + app de simulado (o catálogo oficial de perguntas é público e gratuito no BAMF, então o valor tem de estar na explicação/tradução). → TESTE/BRECHA.

### Extra achado: ES — CCSE / nacionalidad española
Nuvora Digital Store (EUR, 1 dia, 26 anúncios) vende "Nacionalidad española paso a paso", "DELE y CCSE: quién está exento", "Guía + 3 bonus por 14,90 €". É o equivalente espanhol do Einbürgerungstest. Só 1 vendedor, recém-lançado → TESTE (VERIFICAR outros vendedores de CCSE em ES).

## Datas oficiais e tamanho de mercado
Bloqueio: o WebFetch deste ambiente não abre domínios fora da lista de rede liberada (falhou em `portaloswiatowy.pl` e `ncsbn.org`), então NÃO consegui abrir o texto oficial nem as páginas de vendas. Os dados abaixo vêm de busca web; marquei a natureza da fonte. "Oficial (via busca)" = a fonte é o órgão, mas li só o trecho do buscador.

| País / exame | Dado | Fonte | Status |
|---|---|---|---|
| ES – OEP 2026 | Real Decreto 387/2026, BOE nº 111 de 07/05/2026: **27.232 vagas na AGE** (20.541 acesso livre + 6.345 promoção interna + 346 extraordinárias); 37.017 no total com Justiça etc. | [La Moncloa – OEP 2026](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/transformacion-digital-y-funcion-publica/Paginas/2026/oep-oferta-empleo-publico.aspx); [INAP](https://laadministracionaldia.inap.es/noticia.asp?id=1520238) | Oficial (via busca) |
| ES – Guardia Civil | Resolución 160/38243/2026 (BOE nº 112, 08/05/2026): **3.240 vagas** Cabos y Guardias (1.704 livres + 1.296 militares de tropa + 240 Guardias Jóvenes); prova de conhecimentos 11/07/2026 (já ocorreu). Próxima convocatória (2027) sem data | [Interior – Escala de Cabos y Guardias](https://www.interior.gob.es/opencms/ca/servicios-al-ciudadano/empleo-publico/procesos-selectivos/escala-de-cabos-y-guardias-de-la-guardia-civil/index.html); [Redopositor](https://redopositor.com/blog/es-calendario-oposiciones-guardia-civil-2026-fechas/) | 2026 oficial (via busca); 2027 VERIFICAR |
| ES – oposiciones docentes 2027 | provas começam em **17/04/2027** (nota INAP); Extremadura convocou 805 vagas de Secundaria (Juntaex, 19/10/2026); demais CCAA são estimativas (Madrid ~3.000, Valência ~1.500, Murcia 1.500–2.000) | [INAP](https://laadministracionaldia.inap.es/noticia.asp?id=1520889); [Juntaex](https://www.juntaex.es/w/20261019-educacion-convoca-805-plazas-para-las-oposiciones); [CSIF](https://www.csif.es/es/articulo/aragon/educacion/96299) | parcial; números por CCAA VERIFICAR |
| PL – matura 2027 | CKE publicou o harmonograma em 26/08/2026; escrita principal de **04/05/2027** (polonês básico, 9h) até o fim de maio; polonês ampliado 20/05/2027; resultados **09/07/2027**; poprawka resultados 10/09/2027 | [Portal Oświatowy](https://www.portaloswiatowy.pl/komunikaty-men-i-cke/matura-2027-harmonogram-27906.html); [Interia](https://wydarzenia.interia.pl/matura/news-matura-2027-cke-podala-terminy-przyszlorocznych-egzaminow,nId,23531625); [otouczelnie](https://www.otouczelnie.pl/artykul/39741/Jezyk-polski-matura-2027-poziom-podstawowy) | secundária citando CKE → VERIFICAR em cke.gov.pl |
| PL – tamanho | matura 2026: **321.314 zdających** (CKE, dados preliminares de 08/07/2026); 81,1% aprovação | [Polsat News](https://www.polsatnews.pl/wiadomosc/2026-07-08/cke-podala-wyniki-matur-2026-wiadomo-ilu-uczniow-zdalo-egzamin/); [Interia](https://wydarzenia.interia.pl/matura/news-matury-2026-cke-podala-wyniki-egzaminow,nId,23511103) | secundária citando CKE |
| US – NCLEX-RN | 2025: **192.916** candidatos de primeira vez formados nos EUA, 86,7% aprovação (91,2% em 2024); todos os candidatos 69,1% | [NCSBN 2025 Exam Stats (PDF)](https://ncsbn.org/public-files/2025_NCLEXExamStats_Final.pdf) — não abriu; números via [GetOnCourse](https://getoncourse.ai/nclex/pass-rates/) e [Kaplan](https://www.kaptest.com/study/nclex/nclex-pass-rates-what-you-need-to-know/) | **ainda secundário** → VERIFICAR no PDF NCSBN |
| US – real estate | sem número nacional de candidatos | — | VERIFICAR |
| MX – ENARM | 50º ENARM aplicado 28–30/09/2026 (registro 15/04–15/06/2026); ciclo 2025: **66.278 inscritos e 18.515 vagas**; convocatória 2027 ainda não publicada (padrão: registro abr–jun, prova set) | [Excélsior](https://www.excelsior.com.mx/salud/enarm-2026-abre-registro-fechas-requisitos-y-sedes-examen-para-residencias-medicas); [Ruptura360](https://ruptura360.mx/el-pais/domina-el-enarm-2026-guia-completa-para-el-registro-y-sedes-oficiales/) | secundária; 2027 VERIFICAR em cifrhs.salud.gob.mx |
| CO – DIAN 2676 | inscrições modalidade aberta 28/01–06/02/2026 (só SIMO); 1.142 cargos de carreira (79 assistencial, 308 técnico, 755 profissional) ou 1.990 somando ascenso; Bogotá 475; data da prova escrita NÃO encontrada | [DIAN – nota de imprensa](https://www.dian.gov.co/Prensa/Paginas/NG-Inician-inscripciones-en-la-modalidad-abierta-del-concurso-de-meritos-DIAN-2676.aspx); [Bogotá.gov.co](https://bogota.gov.co/mi-ciudad/gestion-publica/trabajo-bogota-concurso-de-la-cnsc-en-la-dian-2026-con-475-vacantes) | oficial (via busca); data da prova VERIFICAR |
| CO – concurso docente | imprensa fala em ~26.000 (El País) ou ~28.000 (RTVC) vagas — o anúncio da Saber Más diz 31.163; inscrições: Geard diz 31/10–22/11/2026, RTVC/RCN dizem adiadas para jan–fev/2027 | [El País CO](https://www.elpais.com.co/economia/concurso-docente-2026-ministerio-de-educacion-y-cnsc-confirman-nuevo-paso-para-mas-de-26000-vacantes-1719.html); [RTVC](https://www.rtvcnoticias.com/actualidad/educacion/el-cronograma-del-concurso-docente-2026-se-movio-2027-aqui-le-contamos-las); [RCN](https://newsroom.rcnradio.com/colombia/concurso-docente-2026-cnsc-cambia-fechas-de-inscripcion-y-asi-queda-el-cronograma) | **conflitante** → VERIFICAR na CNSC/SIMO |
| DE – naturalização | 2025: **332.500 naturalizações** (+14%; 2024: 292.000) e **467.400 pedidos**; maiores grupos: sírios, turcos (34.100), russos (19.700) | [Destatis PM 186 de 03/06/2026](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/06/PD26_186_125.html) | Oficial (via busca) |
| DE – Einbürgerungstest | catálogo público de 310 perguntas (300 federais + 10 do estado); prova de 33 em 60 min; aprova com 17; taxa 25 € | [EinbTestV – gesetze-im-internet](https://www.gesetze-im-internet.de/einbtestv/BJNR164900008.html); [anwalt.org](https://www.anwalt.org/einbuergerungstest/) | Oficial (via busca) |

## Ranking 0–10
Critérios: prova no país/moeda (peso maior), tamanho do público, concorrência, encaixe com "kit + app" do usuário, gancho de prazo, barreira de idioma/pagamento.

| # | Nicho / país | Nota | Régua | Por quê | O que fazer |
|---|---|---|---|---|---|
| 1 | **ES – oposiciones em esquemas + app de test** (AGE C1/C2, Guardia Civil 2027, docentes 2027) | **7,5** | PROVADO | 5 nativos em EUR com 80–150 dias (OposTime 139 d/14, Opocaos 139 d/23, OpoEsquemas 149 d, esquematizate 83 d/18, Leyes.Bonitas 83 d/10); OEP 2026 com 27.232 vagas na AGE; docentes a partir de 17/04/2027. Contra: onda BR entrou em out/2026 (Emma Schneider BRL 13 d; Luiza Fontenelle USD 30 anúncios; Nuvora) | Entrar já, por cargo específico com prova marcada (ex.: Auxiliar/Administrativo del Estado, Celador, Guardia Civil 2027), "temario en esquemas + app de test" — o app é o diferencial que nenhum dos nativos mostra |
| 2 | **PL – matura 2027** (notatki/pewniaki/odpowiedzi em PDF) | **7,0** | PROVADO forte | ZaufanyNauczyciel 105 anúncios ≥196 d; Matura 2027 notatki 175 d/29; 321 mil candidatos/ano; data fixa 04/05/2027. Contra: polonês, concorrência nativa forte, checkout PLN/BLIK | Só com subnicho + app (ex.: lektury em mapas/flashcards, E8 egzamin ósmoklasisty); janela de compra jan–abr/2027; resolver pagamento antes |
| 3 | **DE – Einbürgerungstest na língua do imigrante** (árabe, turco, russo, ucraniano) + app de simulado | **6,0** | BRECHA/TESTE | 332.500 naturalizações e 467.400 pedidos em 2025; ninguém vende em alemão com escala; único antigo é Know Germany (árabe, 171 d, só 5 anúncios); russo e "B1 + Test" entraram em out/2026; nada em turco. Contra: catálogo de 310 perguntas é gratuito no BAMF → o valor tem de ser tradução + explicação + app | Teste barato em árabe e turco (maiores grupos: sírios e turcos), €9–19 |
| 4 | **CO – simulacros CNSC/DIAN e concurso docente** | **6,0** | PROVADO (simulado) + PRAZO | Saber Más 57 d em COP; enxame DIAN 2676 (1–9 d); concurso docente com ~26–31 mil vagas e inscrições nov/2026 ou jan–fev/2027 (conflito). Formato que vende é simulado, não mapa; encaixa com app | Simulacro + "esquemas" do Decreto 1278/temas pedagógicos; confirmar data CNSC antes |
| 5 | **ES – CCSE / nacionalidad española** | **5,5** | TESTE | Só Nuvora (EUR, 1 d, "Guía + 3 bonus por 14,90 €"); resto são advogados. Paralelo direto do Einbürgerungstest | Testar guia CCSE em esquemas + app de 300 perguntas; VERIFICAR volume de pedidos |
| 6 | **US – NCLEX** (cheat sheets/flashcards) | **5,5** | PROVADO, saturado | 192.916 candidatos 1ª vez/ano; My Nurse Notes ≥84 d/56; Nurse In The Making 57 anúncios; bundles US$ 9–50; clones (Alexa Paige/Maya Bennett em CAD) já chegaram | Só se for com ângulo próprio (ex.: enfermeiros estrangeiros/PT-BR que fazem NCLEX) |
| 7 | **MX – ENARM** (flashcards/mapas) | **5,0** | TESTE + PRAZO | 66.278 inscritos e 18.515 vagas (2025); ciclo 2027 recomeçou (todos ≤7 d); apps e cursos fortes; risco de PDF de manual de terceiros | Monitorar Nitidomed/Koplik até 30/11; lançar perto do registro (abr–jun/2027) |
| 8 | **IT – mappe mentali / concorsi** | **4,5** | TESTE | nenhum nativo PROVADO; onda BR começou 28–29/10 (Lingua Chiara, Patricia Romero, Laura Conti, Living in Christ, Studio Facile) | Esperar: re-checar em 28/11 se algum chegou a 30 dias |
| 9 | **Bíblia em mapas (espanhol neutro)** | **4,0** | PROVADO neutro, lotado | Mapa Didactico de la Biblia 257 d (BRL, entrega em MX e ES); 362 anúncios e enxame de clones de 0–2 d | Não entrar no ES neutro; só ângulo novo (católica 73 livros, PT-PT/IT/PL) |
| 10 | **US – real estate exam** | **3,0** | sem sinal | nenhum vendedor de resumo/mapa com 30+ d achado; só lojas novas (StarkLifestyle impresso, exame não confirmado) | Descartar por ora |

## Diferenças em relação à v1
A v1 não estava acessível, então não dá para comparar item a item. Pelo que o prompt diz da v1:
- **Datas 2027 agora com fonte**: matura 2027 em 04/05/2027 (harmonograma CKE de 26/08/2026, via imprensa); docentes ES a partir de 17/04/2027 (INAP); Guardia Civil 2026 com BOE (2027 ainda sem data); ENARM 2026 em 28–30/09/2026 (2027 sem convocatória).
- **NCLEX** continua com número de fonte secundária (o PDF da NCSBN não abriu aqui): 192.916 / 86,7%.
- **DIAN**: agora com nota da própria DIAN (inscrições 28/01–06/02/2026, 1.142 cargos), mas sem data de prova.
- **Fato novo de outubro**: operadores BR começaram a exportar o formato "mapas mentais" para ES (Constitución, Celador SERGAS), IT (idiomas, psicologia, farmacologia) e MX/LATAM neutro (medicina, Bíblia). A brecha que existia em ES/IT está sendo ocupada agora.
- **Achado novo**: Einbürgerungstest só tem vendedor antigo em árabe; CCSE (ES) só tem 1 vendedor de 1 dia.

## VERIFICAR
1. Preço, plataforma, bumps e garantia de TODAS as páginas de vendas (WebFetch bloqueado neste ambiente): OposTime, Opocaos, OpoEsquemas, Editorial-esquematizate, Leyes.Bonitas, OpoFlow, Emma Schneider, Luiza Fontenelle, ZaufanyNauczyciel, Matura 2027 notatki (ArkuszeMaturalne/eNotatki), My Nurse Notes, Nurse In The Making, Saber Más, Know Germany, Nitidomed, Mapa Didactico de la Biblia. Preços só vistos em anúncio: Nuvora "Guía + 3 bonus 14,90 €"; Bigdawgrn "NCLEX Content Bundle $49.99"; referência ES: Preparaoposiciones PDF AGE 45 € / Informática 29 €.
2. Idade real de Nurse In The Making (57 anúncios; conector só mostra 50) e de ZaufanyNauczyciel (≥196 d; pode ser mais).
3. Matura 2027 (04/05/2027) no comunicado oficial da CKE (cke.gov.pl).
4. NCLEX 2025 (192.916; 86,7%) no PDF oficial da NCSBN.
5. Concurso docente CO: número de vagas (26 mil / 28 mil / 31.163) e janela de inscrição (nov/2026 ou jan–fev/2027) na CNSC/SIMO; data da prova escrita DIAN 2676.
6. ENARM 2027: convocatória CIFRHS (datas de registro e prova).
7. Guardia Civil 2027: OEP 2027 e data de prova; vagas por CCAA das oposiciones docentes 2027 nos boletins oficiais.
8. "Concorsi in Mappe" (IT): sem anúncio ativo no conector — ver se vende só orgânico/Instagram.
9. StarkLifestyle (US): qual exame vende (real estate ou enfermagem?).
10. ES CCSE: volume de pedidos de nacionalidade (Ministerio de Justicia) e outros vendedores além da Nuvora.
11. DE: vendedores de Einbürgerungstest em turco e ucraniano (busca em turco devolveu só 2 anúncios de consultoria) e se há app gratuito dominante (o que derruba o preço).
12. PL: checkout em PLN/BLIK (Hotmart?) e fatura.
13. Re-checar em **28/11/2026** se a onda BR sobreviveu 30 dias: Emma Schneider (ES), Luiza Fontenelle (ES), Nuvora (ES), Lingua Chiara / Patricia Romero / Laura Conti / Living in Christ (IT), Nitidomed e Koplik (MX), Studovo e Zestly (DE).
14. ENARM Digital 2.0 / Enarm en tus manos: se os "manuais 2027" são material de terceiros (risco de pirataria) — não copiar o modelo.
