# Brechas internacionais a partir do catálogo EscalaLow, parte 1 (índices 0 a 52, 53 ofertas)

Data: 30/10/2026. Fonte das ofertas: `3 - EU/pesquisas/brechas-europa-2026-10-28/escalalow-ofertas-validadas.json`.
Dados brutos: `pesquisas-nichos-2026-10-29/catalogo-p1-dados/` (resultado*.json, saida*.txt, out_chunk_*.txt).

## Como ler (método e limites, importante)

- **SS** = SearchAPI, frase exata, só anúncios ativos, 2 páginas por busca, dias reais por page_id em 30/10. **PROVADO** = vendedor com 30+ dias e 3+ criativos no país.
- **CN** = conector ads_library_search. Ele devolve os anúncios MAIS RECENTES primeiro e não dá a data real do anúncio mais antigo. Por isso o CN só serve para contagem, nomes de quem anuncia e moeda; "dias" do CN são do anúncio mostrado (≈1d = começou em 28/10 a 30/10). Nunca usei CN para afirmar PROVADO.
- **O crédito do SearchAPI acabou hoje** (`current_month_usage` 10000 de 10000; ciclo renova 08/11). Das 95 buscas planejadas, 37 saíram completas via SS (a rodada paralela levou 429 e depois "used all searches"). O resto foi completado só com contagem via CN ou ficou **n/m (não medido) = VERIFICAR**.
- "ninguém" = zero anúncios ativos para a frase exata (SS) ou nenhum anunciante vendendo o produto na amostra do CN. Não é prova de que ninguém venda fora do Meta.
- Moeda: o campo currency do conector é a moeda de COBRANÇA do anunciante, não do preço da página. USD/BRL em anúncio na Itália indica anunciante brasileiro/estrangeiro rodando para lá. EUR indica anunciante local.
- Espanhol neutro não prova país: só considerei ES (Espanha) e MX quando a busca foi com esse país.
- Memória do usuário: foco desde 07/10 em kits de documentos de PROFISSIONAIS; o ranking pondera isso, mas mostro também as brechas de consumidor.

## Descoberta mais importante da rodada

Um anunciante brasileiro do próprio catálogo (**Caixa do Terapeuta**, oferta 37, Kit Radiestesia, 168d no Brasil) tem 169d / 8 criativos na Espanha (SS, ES) e em **29/10/2026 abriu a França ("Boîte du Thérapeute", ~20 criativos, 1 dia) e a Itália ("Cassetta del terapeuta", 3 criativos, 1 dia)** (CN). Ou seja: quem já provou na Espanha está testando FR e IT agora. A Alemanha está vazia (0 anúncios em "Radiästhesie Pendel").
Também na Itália, de 27 a 29/10, apareceu uma onda de clones brasileiros (cobrança USD, 1 a 2 dias): Attivita Premium (2.500 schede a €7,90), Prof di Scienze (120 schede de ciências), Pronti via (25.000 materiais a €9,99), Studio Facile (falegnameria, cartamodelli), Sartoria a 4 Zampe, Il Mio Quaderno di Cucito, ZampaLife (cães). A janela de Itália para educação/costura/marcenaria está sendo ocupada agora, mas sem nenhum com 30 dias.

---

## 1. Conceitos (ofertas agrupadas)

| ID | Conceito | Ofertas (índice) | Profissão / público |
|---|---|---|---|
| C1 | Modelos 3D / arquivos STL prontos | 1, 12, 38 | Dono de impressora 3D (renda extra), nicho católico, nicho pet |
| C2 | Receitas por tema (pão de queijo, sem glúten/lactose, finger food, congelar, almoço fitness, drinks) | 2, 6, 15, 16, 20, 27, 39, 43, 51 | Consumidor / quem vende comida |
| C3 | Projetos prontos de marcenaria / serralheria | 3, 52 | Marceneiro, serralheiro, hobby DIY |
| C4 | Moldes de costura / caixinhas cenário (papel) | 5, 28, 41 | Costureira, artesã de papelaria |
| C5 | Mapas mentais para estudar (inglês visual) | 4 | Estudante / quem aprende idioma |
| C6 | Aulas e atividades prontas para professor (ciências, física, arte, jogos, dinâmicas, leitura, recuperação) | 7, 8, 10, 33, 48, 49, 50 | Professor infantil/fundamental |
| C7 | Alfabetização silábica | 14, 22 | Pais e professores de alfabetização |
| C8 | Guia de alimentação caseira para cães | 9 | Tutor de cachorro |
| C9 | Curso/edição de vídeo no celular (CapCut) | 11 | Criador de conteúdo |
| C10 | Treino em casa / fitness (mulher 30+, glúteo, desafio, jiu-jitsu, chutes) | 18, 19, 25, 29, 47 | Mulheres 30+, praticantes de artes marciais |
| C11 | Reforma Tributária explicada | 13 | Contador / empresário (Brasil) |
| C12 | IA (Claude) para trabalho / automação | 21 | Profissionais que querem usar IA |
| C13 | Packs digitais genéricos (músicas, biblioteca de ebooks, "copie e cole marca", simulador de uniforme) | 0, 24, 44, 45 | Consumidor genérico / DJ / revendedor |
| C14 | Planner para TDAH e kit de atendimento psicopedagógico | 31, 23 | Adulto com TDAH; psicopedagogo |
| C15 | Planner financeiro por WhatsApp; checklist de mentoria | 26, 34 | Autônomo, mentora/coach |
| C16 | Documentos prontos de consultoria em alimentos (HACCP/RDC) | 30 | Consultor/nutricionista de alimentos |
| C17 | Eletricista: apostila de comandos elétricos e tabela de preços | 32, 35 | Eletricista, técnico elétrico |
| C18 | Planta/memorial automatizado QGIS | 36 | Topógrafo/engenheiro de georreferenciamento |
| C19 | Radiestesia (gráficos de pêndulo, relógio radiestésico) | 37 | Terapeuta holístico |
| C20 | Presets de Lightroom | 40 | Fotógrafo |
| C21 | Curso de endodontia mecanizada | 42 | Dentista |
| C22 | Kit de documentos para clínica odontológica | 46 | Dentista |

## 2. Resultado por conceito e país

Legenda de status: PROVADO / TESTE / BRECHA / VERIFICAR (n/m).

### C1 STL (1, 12, 38)
| País | Termo | Quem vende (dias, criativos, moeda) | Status |
|---|---|---|---|
| ES | "archivos STL" | SS: Marcos Vinicius (BR) coleccionmaestrastl.lovable.app 125d/1cr; Mundo catolico 3d 80d/4cr; Sebastián Torrez garaje3d 35d/6cr; Roberto (BR) packstlanimalitos 27d/37cr, "US$3.99". 234 anúncios | PROVADO (vendedores a 80d e 125d) |
| ES | "nicho católico" | SS: 6 anúncios, só Marcos Santiny (BR) 0d/6cr; CN: "Gana Dinero con la Impresión 3D en el Nicho Católico", USD, ~3d | TESTE (católico 3D), BR já entrou |
| US | "STL files" | SS: Nico's Printed Antiques 374d, Terror Prints 209d (700+ horror STL), Model Craft 3d 178d, The Workspace Hero 141d/5cr. 739 anúncios | PROVADO (EN) |
| IT | "file STL" | SS: 41 anúncios, quase tudo B2B dental/moldes; Maestro 3D PRO (stampa3d.pro, "oltre 300.000 progetti STL") 14d/1cr | TESTE |
| FR | "fichiers STL" | SS: 4 anúncios (SUNLU filamento, Farmtuile). Nenhum pack | BRECHA |
| DE | "STL Dateien" | SS: 0; CN (busca ampla): 4 anúncios, nenhum vende pack de STL (Fehn-Factory xadrez, 3D Letter Studio) | BRECHA |
| PT | n/m | VERIFICAR | |
Preço observado: US$3,99 (ES, Roberto). Risco: direitos autorais dos modelos (packs "150 mil modelos" costumam ser material pirateado). Produto próprio exige modelos próprios ou licenciados.

### C2 Receitas (2, 6, 15, 16, 20, 27, 39, 43, 51)
| País | Termo | Resultado | Status |
|---|---|---|---|
| ES | "recetas para congelar" | SS: 1 anúncio (Lo Que Nadie Te Explicó, 0d) | BRECHA |
| FR | "recettes à congeler" | CN: 12 anúncios, nada específico de congelar; Tuto Airfryer, Cookimag (GBP), **Mon Airfryer "300 recettes pour AirFryer" EUR, anúncio de 24/09 = 36d (1 criativo visto)**, Priscila Vermont (BR, BRL) | TESTE (airfryer FR); congelar = BRECHA |
| DE | "Meal Prep Rezepte" | CN: 69 anúncios, coaches fitness; nenhum caderno de congelar | BRECHA (congelar) |
| IT / PT | congelar | CN: 11 e 11 anúncios, nenhum de receitas | BRECHA |
| US/GB | "freezer meals" | n/m (SS sem crédito) | VERIFICAR |
Demais temas (sem glúten, anti-inflamatória, Bimby/Thermomix, air fryer) já medidos em 28/10: ver `CONSOLIDADO-V2.md`, item 2 (ES 30, PT 31, IT 29, DE 29). Não refiz.
Preço consumidor Europa: €9,90 a €19 (CONSOLIDADO-V2).

### C3 Marcenaria / serralheria (3, 52)
| País | Termo | Resultado | Status |
|---|---|---|---|
| US | "woodworking plans" | SS: Crafted Wood DIY 194d/2cr, WoodCrafts DIY 141d/3cr, Wood Blueprints 137d/7cr, Craft Blueprints 126d/2cr. 268 anúncios | PROVADO |
| GB | idem | SS: os mesmos 4, 162 anúncios | PROVADO |
| FR | "plans de menuiserie" | SS: **WoodCrafts DIY página em francês 104d/12cr**; WoodSense 38d/5cr; Master Crafts DIY 16d. 20 anúncios | PROVADO (104d) |
| ES | "planos de carpintería" | CN: 102 anúncios; WoodSense (USD, ~3d), CutOnce "Conviértete en experto en carpintería" (USD, ~3d), oficiosrentables.ok | TESTE |
| IT | "progetti falegnameria" | CN: 147 anúncios; Studio Facile (cobrança USD, "La falegnameria spiegata con i disegni", ~2d), MrGeppetto (EUR), WEB PRO ITALIA curso fai da te | TESTE |
| DE | "Holzbau Pläne" | SS: 0 (CN traz só vaga de emprego da Grübbel Holzbau) | BRECHA |
| ES | "planos de herrería" (serralheria) | n/m | VERIFICAR |
Preço: não confirmado (páginas de dropship "{{product.brand}}").

### C4 Moldes de costura / caixinhas cenário (5, 28, 41)
| País | Termo | Resultado | Status |
|---|---|---|---|
| ES | "patrones de costura" | CN: 172 anúncios; Entre Mujeres "200+ patrones digitales en PDF" (USD, ~1d, 5cr), Vanessa Agudelo (COP), Arte en Tus Manos (BR, BRL), GalianaSpain | TESTE |
| DE | "Schnittmuster PDF" | CN: 29 anúncios; Lybstes "Schnittmuster downloaden & loslegen" EUR (~1d visto), Schleiferlwerk | TESTE/mercado nativo existente (dias VERIFICAR) |
| IT | "cartamodelli PDF" | CN: 15; Studio Facile (USD, 1d), Sartoria a 4 Zampe (USD, 2d), Il Mio Quaderno di Cucito (USD, 3d) | TESTE (clones BR) |
| PT | "moldes de costura" | CN: 142 anúncios, quase todos de brasileiros (BR/USD); sem nativo | VERIFICAR |
| US | "shadow box" (caixinha cenário) | SS: 410 anúncios, só produto físico (Great Golf Memories 1010d etc.) | sem kit de molde digital na amostra |
| FR / US sewing | n/m | VERIFICAR | |

### C5 Mapas mentais / Inglês visual (4)
| País | Termo | Resultado | Status |
|---|---|---|---|
| MX | "mapas mentales" | CN: 1.114 anúncios (termo amplo); **Mapasyresumenes "Tu kit de inglés visual · Solo US$ 7", "Entiende el inglés con mapas · US$ 7", literatura US$5 (BRL de cobrança, ~1d)**; Mente Bilingüe (438 reseñas) | TESTE (clone BR de 1 dia) |
| IT | "mappe mentali" | SS: 546 anúncios; Nicoletta Todesco 517d/2cr (leitura veloz), Centro Studi Lambda 451d/4cr (método de estudo, guia grátis), MyEdu 120d/3cr. São métodos/cursos para pais de crianças, não kit imprimível | PROVADO (método de estudo IT), kit imprimível = BRECHA |
| ES, US, DE, FR | "mapas mentales"/"mind maps"/"Mindmaps"/"cartes mentales" | n/m (429/sem crédito) | VERIFICAR |

### C6 Educação professor (7, 8, 10, 33, 48, 49, 50)
| País | Termo | Resultado | Status |
|---|---|---|---|
| IT | "schede didattiche" | CN: 79; **Attivita Premium "2.500 schede a 7,90 €" (USD, 8 quaderni, ~1-2d, 10 criativos)**, Prof di Scienze "120 Schede di Scienze Pronte all'Uso" (USD, ~1d), Pronti via "25.000 materiali a 9,99 €" (USD, ~2d), Chiaramente | TESTE quente (ninguém com 30d) |
| ES | "actividades para imprimir" | SS: 35; Gana con Conocimiento 39d/1cr, Geriactiva 27d (adultos mayores, .ar), NeuroKids 27d/3cr, Play and Learn Lab 17d/5cr | TESTE |
| ES | "planeaciones" | SS: 4; Arya Cheeze fichasmontessori 66d/1cr; Dra. Catalina Leal "Claude para docentes" 6d | TESTE |
| MX | "material didáctico" | SS: 496, quase tudo loja física/escola; sem kit digital relevante | BRECHA |
| ES | "actividades de arte para niños", "experimentos de física" | SS: 0 e 0 | BRECHA |
| US | "physics experiments" | SS: 30 (ACT prep, Kickstarter, kit físico) | BRECHA (kit digital) |
| ES / IT / FR | "fichas de lectura" / "schede di lettura" / "fiches de lecture" | SS: 3, 2, 4 anúncios sem kit (só Scala delle Sillabe IT 0d) | BRECHA |
| DE, FR, PT, US | "Arbeitsblätter", "fiches à imprimer", "fichas para imprimir", "printable activities" | n/m | VERIFICAR |

### C7 Alfabetização silábica (14, 22)
| País | Termo | Resultado | Status |
|---|---|---|---|
| ES (CN, sem país fixo) / MX | "método silábico" | CN (MX): 115 anúncios, dominado por **Lectoescritura ya** (USD, lead grátis "Recíbelo gratis hoy", 15+ criativos, ~1d) | TESTE |
| IT | "schede di lettura"/pregrafismo | Attivita Premium cobre ("dalla lettera alla parola") 1-2d; "Scala delle Sillabe" 0d | TESTE |
| ES, IT "sillabe" | SS | n/m | VERIFICAR |

### C8 Comida caseira para cães (9)
| País | Resultado | Status |
|---|---|---|
| ES | CN "comida casera para perros": 9 anúncios, nenhum guia (TrendFold Daily conteúdo, Puromenu BARF loja, Mi amiga la veterinaria ração) | BRECHA de guia digital |
| DE | CN "Hundefutter selber kochen": 9; HelloBello, Fidelis.dog (marcas de comida fresca) | BRECHA de guia |
| IT | CN "cibo casalingo per cani": 11; ZampaLife (USD, "Finalmente — un metodo che funziona", ~2d), DogUp | TESTE |
| FR, US | n/m | VERIFICAR |
Tamanho: cães DE 10,5M, ES 9,46M, IT 8,77M (fonte secundária resumindo FEDIAF 2025, não conferi o PDF: https://petproducts.com.cn/european-pet-ownership-statistics-2025/ ; FEDIAF Facts & Figures https://www.zzf.de/fileadmin/ZZF/Dokumente/Heimtiermarkt/FEDIAF_Facts_Figures_2026.pdf). Cuidado: nutrição animal, texto sem promessa clínica.

### C9 CapCut (11)
| País | Resultado | Status |
|---|---|---|
| FR | SS "formation CapCut": **MelleDigital 214d/7cr**, Haude Georgelin 108d/3cr. 10 anúncios | PROVADO |
| ES | CN "curso de CapCut": 57 anúncios amplos (Setcero.ai UGC com IA EUR; Método S6F, BR, BRL, ~2d). Sem vendedor dedicado visível | TESTE |
| IT | SS "corso CapCut": 0; CN 34 anúncios amplos (SD Formazione social media) | BRECHA (dedicado) |
| DE | SS "CapCut Kurs": 0 | BRECHA |
| US | SS "CapCut course": 0 | sem anúncio dedicado (VERIFICAR com outro termo) |
Observação: é curso em vídeo, não kit de documentos; fraco para o modelo do usuário.

### C10 Fitness (18, 19, 25, 29, 47)
| País | Resultado | Status |
|---|---|---|
| ES | SS "ejercicios para glúteos": 4; Lucía Pérez quiz "bumbumturbinado.online" 24d/1cr (clone BR), Rachel Clark 2d/2cr | TESTE |
| US | SS "bjj wrestling": 62 anúncios, vestuário e academias (Ronin 328d, Anaconda 324d, ATT Palm Beach 120d); sem curso de wrestling para BJJ | BRECHA (curso) |
| Demais (mulher 30+, desafio 28 dias, chutes) | n/m | VERIFICAR |
Nichos de treino de emagrecimento: risco de regras de saúde/promessa; prioridade baixa.

### C11 Reforma Tributária (13)
BR-específico, sem análogo direto no catálogo. Os análogos europeus já foram medidos em 28/10: Termometro 85k (IT forfettario, 34) e Agenda Verde (PT recibos verdes, 36), `CONSOLIDADO-V2.md`. Não pesquisei de novo.

### C12 Claude / IA (21)
| País | Resultado | Status |
|---|---|---|
| ES | SS "curso de Claude": 112 anúncios; Copolo Inmobiliaria (inmobiliariaclaude.online, "Si sos agente inmobiliario…") 22d/12cr, Valeria.ia 16d/3cr, Red Sanitaria 70d/1cr, "Claude para docentes" 6d | TESTE (Claude por profissão já em 22d) |
| US | SS "Claude AI course": 0 | BRECHA/VERIFICAR (termo) |
| IT, FR, DE, PT | n/m | VERIFICAR |
Tendência: "Claude para [profissão]" (imobiliário, docentes, controladoria) já aparece em ES e PT-BR. Alto risco de saturação rápida.

### C13 Packs genéricos (0, 24, 44, 45)
Não são profissão nem kit documental; não pesquisei (0 "Copie e cole na sua marca", 24 packs musicais DJ com problema de direitos, 44 biblioteca de ebooks com problema de direitos, 45 simulador de uniforme de uma loja local). n/m.

### C14 TDAH e psicopedagogia (31, 23)
| País | Termo | Resultado | Status |
|---|---|---|---|
| US | "ADHD planner" | CN: 546 anúncios (ProsperSheet, Untangle ADHD, Kristen Newsome "Doodle My Chaos", pad de planner dropship) | mercado maduro/saturado |
| ES | "planner TDAH" | SS exato: 0; CN amplo: 37 anúncios; **Mente Inquieta "La agenda hecha para tu cerebro" (EUR, ~1-2d)** | TESTE |
| FR | "planner TDAH" | CN: 30; **Lumi Editions "Le planner pour les cerveaux qui s'éparpillent" (USD, anúncio de 16/10 = ~14d, 3 criativos vistos)** | TESTE |
| DE | "ADHS Planer" | CN: 9; Lisa Klein (EUR, texto longo/ficção, ~1d) | TESTE fraco |
| IT | "agenda ADHD" | CN: 3; Therapy Toolkit e ABA Tools (USD, "Kit di risorse terapeutiche per bambini", ~19d e ~33d, 1 criativo cada), Centro Nova Mentis (clínica) | BRECHA de planner; kit terapeuta infantil TESTE |
| PT | "planner TDAH" | CN: 42; **Planner Sem Caos TDAH (o próprio BR, BRL)** | só o BR |
Tamanho: ES adultos 3-4% (https://psiquiatria.com/tdah-hiperactividad/entre-el-3-y-el-4-por-ciento-de-adultos-espanoles-padecen-trastorno-de-deficit-de-atencion-e-hiperactividad/); DE 2,58% = 1,8 a 4,8 milhões (UKE https://www.uke.de/landingpage/hoou/erkrankungen/adhs/index.html). Kit psicopedagogia (23) em ES ("psicopedagogía"): n/m.

### C15 Planner financeiro WhatsApp / checklist mentoria (26, 34)
n/m (sem crédito). VERIFICAR. Mentoria: termo "plantillas para mentoría"/"mentoring templates" não medidos.

### C16 Consultoria de alimentos (30)
Já é a Consultora: simulado/documentos HACCP. Medido em 28/10 (não refiz): IT 31, PT 30, ES 29, FR 23; no Meta só aparece software (`CONSOLIDADO-V2.md`, item 1). Preço BR da oferta: R$8.

### C17 Eletricista (32, 35)
| País | Termo | Resultado | Status |
|---|---|---|---|
| US | "motor control wiring" | SS: 3; **Vifalio App Tec (BR) "Download 27 c..." em inglês, 9d/3cr** | TESTE (BR clonando) |
| US | "electrician pricing" | SS: 3; Vifalio App Tec "Not sure what to charge for an outlet…" 3d/3cr | TESTE |
| ES | "precios de electricista" | SS: 0 | BRECHA |
| DE | "Schützschaltung" | SS: 0 | BRECHA |
| ES | "comandos eléctricos" | n/m | VERIFICAR |
Tamanho ES: InfoJobs registrou 29.847 vagas de eletricista em 2025; patronais falam em déficit de ~70.000 (sem data; cautela) https://www.merca2.es/2026/06/15/falta-electricistas-ia-espana-2397340/ ; autónomos totais 3,44 milhões (RETA, abr) https://emprendedores.es/ideas-de-negocio/oportunidades-de-negocio/oficios-tradicionales-refugio-auge-ia/. Contagem de eletricistas autônomos: não encontrei (VERIFICAR no INE/CNAE 432). Gancho legal com data: não confirmei (VERIFICAR).

### C18 Planta QGIS (36)
Nicho técnico local, n/m. VERIFICAR.

### C19 Radiestesia (37) (ver destaque acima)
| País | Termo | Resultado | Status |
|---|---|---|---|
| ES | SS "radiestesia" | 202 anúncios; **Caixa do Terapeuta (BR) 169d/8cr**, Centro de Radiestesia Cabalística 170d/1cr, ines_terapeuta 180d/2cr (PT-BR), Yo Soy Holística (.ar) 93d | PROVADO |
| FR | CN "radiesthésie" | 57; **Boîte du Thérapeute (BR, BRL) ~1d, ~20 criativos, "Accédez maintenant à votre kit complet"**; nativos: instrutores/magnetiseurs locais (formação, sem kit) | TESTE (líder BR entrando) |
| IT | CN "radioestesia pendolo" | 4 (cartomante, sem kit); mais CN "radiestesia": **Cassetta del terapeuta (BR) ~1d, 3 criativos** | TESTE |
| DE | CN "Radiästhesie Pendel" | 0 | BRECHA |
| PT | CN "radiestesia" | 316 (mistura PT-BR; Terapias de Luz, Espaço Mannah, Radiestesia-Práctica) | VERIFICAR (BR domina) |
| BE | CN "radiesthésie" | 24 (magnétisme, formação) | sem kit |
Concorrentes de produto: Hotmart FR "Kit Complet de Radiesthésie" (4 gráficos + protocolos, preço não exibido) https://hotmart.com/fr/marketplace/des-produits/kit-complet-de-radiesthesie-diagnostic-cause-et-correction-energetique/P105370292F ; "Radiesthésie Totale: 90 planches" na Hotmart FR; livro "Les 333 planches du pendule" €35 (Leduc); gráficos digitais na Etsy a partir de €1,45. ES: cursos de €45 a €299 (Educaweb/Emagister). Atenção: sem eficácia científica; vender como prática tradicional, sem diagnóstico ou promessa de cura. Cabe na regra de sem saúde sensível (não é HOF/injetáveis), mas evite alegação médica.

### C20 Presets Lightroom (40)
| País | Resultado | Status |
|---|---|---|
| DE | SS "Lightroom Presets": 285; Moses Aurelius 883d/5cr, 123presets 696d, Carrot Presets 588d/6cr (lojas globais em inglês) | PROVADO, mas por lojas em EN |
| FR | SS: 41; Moses Aurelius 141d/5cr; **Nati Debortoli (BR) fr.natidebortoli.com 12d/9cr, em francês** | PROVADO (EN) / TESTE (FR nativo, BR entrando) |
| IT | SS: 1 (preset grátis) | BRECHA IT |
| ES, US | n/m | VERIFICAR |

### C21 Endodontia (42)
ES SS "endodoncia": 180 anúncios, quase tudo clínica/universidade (sem curso/kit de endodontia mecanizada na amostra). IT e US n/m. VERIFICAR.

### C22 Kit de documentos odontologia (46)
Já medido em 28-29/10 (não refiz): Itália tem BR vendendo a €19,99 há 30+ dias (PROVADO); ES dentista 43,7k sem vendedor (nota 6,5); PT Consultório em Dia ~2,5d (4,5, monitorar); FR e DE em espera. Fonte: memória pesquisa-europa, `3 - EU/pesquisas/psicologo-dentista-4-paises-2026-10-29.md`. La Valigetta del Dentista (IT, €27/€19) já em construção.

---

## 3. Tabela das 53 ofertas

Formato: índice | oferta (dias BR / ativos / preço BR) | profissão-público | conceito | resultado internacional resumido.

| # | Oferta | Público | C | Resultado |
|---|---|---|---|---|
| 0 | Copie e Cole na Sua Marca (137d, 312 ativos, R$47) | empreendedor | C13 | n/m, genérico |
| 1 | Modelos STL para vender (49d, 178, preço n/c) | dono de impressora 3D | C1 | ES e US PROVADO; IT TESTE; FR/DE BRECHA |
| 2 | Pão de queijo lucrativo (131d, 167, R$30) | quem vende comida | C2 | BR-específico; sem busca |
| 3 | +2000 projetos prontos (marcenaria) (79d, 165) | marceneiro/DIY | C3 | US/GB/FR PROVADO; ES/IT TESTE; DE BRECHA |
| 4 | Kit Inglês Visual (109d, 117, R$47) | estudante de inglês | C5 | MX TESTE (US$7, 1d); IT método PROVADO |
| 5 | +2000 moldes de costura (93d, 116, R$37) | costureira | C4 | ES/IT TESTE; DE nativo existe; PT BR domina |
| 6 | 365 receitas sem açúcar/glúten/lactose (161d, 112, R$10) | consumidor | C2 | ver CONSOLIDADO-V2 (28/10) |
| 7 | Kit aulas prontas Ciências (56d, 110) | professor | C6 | IT TESTE (Prof di Scienze, 1d); ES planeaciones TESTE |
| 8 | 10 jogos (89d, 109, R$27) | professor | C6 | ver C6; n/m específico |
| 9 | Guia Pet Comilão (58d, 94) | tutor de cão | C8 | ES/DE BRECHA de guia; IT TESTE |
| 10 | 5.000 atividades infantis (91d, 85) | pais/professores | C6 | IT TESTE (2.500 schede €7,90); ES TESTE |
| 11 | Curso CapCut (306d, 81, 12x 6,93) | criador | C9 | FR PROVADO 214d; IT/DE BRECHA |
| 12 | +500 STL católicos (50d, 77, R$10,90) | nicho católico 3D | C1 | ES católico PROVADO 80d/4cr |
| 13 | Mapa Fácil da Reforma Tributária (91d, 77, R$27) | contador/empresário | C11 | BR-específico; ver Termometro 85k / Agenda Verde |
| 14 | Kit Família Silábica (82d, 74, R$29,90) | alfabetização | C7 | MX TESTE (Lectoescritura ya, 1d) |
| 15 | Finger Foods Lucrativos (76d, 70, R$10) | quem vende comida | C2 | n/m |
| 16 | Receitas saudáveis para congelar (130d, 68, R$67) | consumidor | C2 | ES, IT, PT, DE BRECHA; FR airfryer TESTE |
| 17 | Maior time de naturais (197d, 64) | fitness/treinador | n/a | fora do escopo (infoproduto de coach); não pesquisado |
| 18 | Mulher 30+ que cansou de treinar (49d, 63) | personal trainer | C10 | n/m |
| 19 | Desafio Treino Trinca (67d, 62) | fitness | C10 | n/m |
| 20 | 150 almoços fitness (64d, 58, R$18) | consumidor | C2 | DE meal prep: coaches, nenhum caderno |
| 21 | Caminho da Automação (Claude) (471d, 56, R$10) | profissionais com IA | C12 | ES TESTE (22d máx.) |
| 22 | Baralho Vira Sílaba (78d, 52, R$17,90) | alfabetização | C7 | ver C7 |
| 23 | Kit Destrava Atendimento (211d, 52, R$37,90) | psicopedagogo | C14 | IT kit terapeuta infantil TESTE; ES n/m |
| 24 | Packs musicais (482d, 51, R$47) | DJ/bares | C13 | não pesquisado (direitos autorais) |
| 25 | Guia Coxa e Bumbum sem agachamento (230d, 51, R$39,90) | mulheres | C10 | ES TESTE (24d, clone) |
| 26 | Plano Premium WhatsApp finanças (126d, 50, R$69) | autônomo | C15 | n/m |
| 27 | Receitas Sem Pensar (187d, 50, R$47) | consumidor | C2 | n/m |
| 28 | Moldes digitais PDF (364d, 50, R$25) | costureira | C4 | idem 5 |
| 29 | Chutes mais altos em 14 dias (55d, 50, R$47) | taekwondo/artes marciais | C10 | n/m |
| 30 | Documentos prontos Consultoria em Alimentos (54d, 50, R$8) | consultor de alimentos | C16 | já coberto: IT 31, PT 30, ES 29 |
| 31 | Planner Sem Caos TDAH (176d, 45, R$37) | adulto TDAH | C14 | ES/FR TESTE; IT BRECHA; DE fraco |
| 32 | Apostila de Comandos Elétricos (53d, 44) | eletricista | C17 | US TESTE (BR clonando); ES/DE BRECHA |
| 33 | +300 dinâmicas de arte infantil (75d, 43) | professor | C6 | ES arte: 0 |
| 34 | Checklist Mentora 100K (66d, 43, R$67) | mentora | C15 | n/m |
| 35 | Tabela Digital do Eletricista (61d, 42) | eletricista | C17 | US TESTE (Vifalio 3d); ES "precios de electricista" 0 |
| 36 | Planta Turbo (QGIS) (159d, 42, R$67) | geoprocessamento | C18 | n/m |
| 37 | Kit Radiestesia Completa (168d, 41, R$27) | terapeuta holístico | C19 | ES PROVADO 169d; FR/IT TESTE (1d); DE BRECHA |
| 38 | 300 STL nicho pet (56d, 41, R$29,90) | impressão 3D pet | C1 | ver C1 (ES animalitos 27d/37cr) |
| 39 | 101 pães sem glúten (91d, 40, R$10) | consumidor | C2 | ver CONSOLIDADO-V2 |
| 40 | Biblioteca 250+ presets (138d, 38, R$59,70) | fotógrafo | C20 | DE/FR PROVADO por lojas EN; FR nativo TESTE |
| 41 | +300 moldes caixinha cenário (53d, 37, R$37) | artesã | C4 | US shadow box só físico; kit digital n/m |
| 42 | Do Manual ao Mecanizado (119d, 36, R$47) | dentista (endo) | C21 | ES só clínicas; n/m |
| 43 | App com +150 receitas (194d, 35) | consumidor | C2 | n/m |
| 44 | Biblioteca Digital 3.500 ebooks (88d, 35, R$10) | consumidor | C13 | não pesquisado (direitos) |
| 45 | 2effe Sport simulador uniformes (124d, 34) | loja local | C13 | fora de escopo |
| 46 | Kit Completo Documentos Odontologia (238d, 32, R$67) | dentista | C22 | IT PROVADO (BR, €19,99); ES BRECHA 43,7k |
| 47 | Wrestling para Jiu-Jitsu (99d, 32, R$47) | lutador BJJ | C10 | US: sem curso concorrente na amostra |
| 48 | Kit Recuperação Final (fichas de leitura) (92d, 31) | professor | C6 | fichas de lectura/lettura: BRECHA |
| 49 | +150 dinâmicas prontas (49d, 31, R$17) | professor educação física | C6 | n/m |
| 50 | +600 atividades e experimentos física (57d, 31, R$67) | professor de física | C6 | ES 0; US sem kit digital |
| 51 | 150 drinks gourmet (131d, 29, R$10) | quem vende drinks | C2 | n/m |
| 52 | Pack Tesouro do Serralheiro (130d, 29, R$10) | serralheiro | C3 | ES n/m (VERIFICAR) |

---

## 4. Ranking 0 a 10 das brechas mais fortes (parte 1)

Nota = demanda provada (prova no Brasil + sinal lá fora) + espaço livre + tamanho + gancho + reaproveitamento. Onde a nota vem de pesquisa anterior, digo.

1. **Consultoria em alimentos / simulado de inspeção (C16, #30): 8,0.** Prova BR (54d, 50 ativos, R$8). No exterior só software no Meta; notas V2: IT 31, PT 30, ES 29, FR 23 (de 45). Tamanho e gancho (HACCP/inspeção sanitária, normas locais) já levantados em 28/10, não refiz hoje. Reaproveitamento total: app de inspeção + Consultora, trocar norma e idioma. Fonte: `brechas-europa-2026-10-28/CONSOLIDADO-V2.md`.
2. **Kit de radiestesia FR/IT/DE (C19, #37): 7,5.** Evidência: o próprio anunciante BR tem 169d/8cr na Espanha e abriu FR e IT em 29/10; Hotmart FR já tem kits de 4 a 90 gráficos; DE tem 0 anúncios. Risco: o líder está entrando e a página dele é em português traduzido; entrar com marca local, nativo em alemão (brecha limpa) e sem promessa de saúde. Tamanho: não confirmei (VERIFICAR). Gancho legal: nenhum (nicho esotérico, atenção a alegações de saúde). Reaproveitamento: kit gráfico imprimível, mesmo motor da Valigetta (marca própria por oferta).
3. **Kit de documentos odontológicos, Espanha (C22, #46): 7,0.** Já medido: ES 43,7k dentistas sem vendedor (6,5 na rodada anterior), Itália PROVADO por BR a €19,99. Sem busca nova. Reaproveita La Valigetta del Dentista. Subo para 7 porque a oferta BR continua a 238d / 32 ativos.
4. **Planner TDAH, ES/FR (C14, #31): 6,5.** BR: 176d, 45 ativos, R$37. ES: Mente Inquieta (EUR) começou há ~1-2 dias; FR: Lumi Editions (~14d); IT sem planner (brecha), DE fraco. Tamanho: TDAH adulto 3 a 4% na Espanha (psiquiatria.com), DE 1,8 a 4,8 milhões (UKE). Gancho legal: nenhum; é consumidor, não profissional. Risco: EUA saturado (546 anúncios), a Europa só tem testes.
5. **Mapas mentais / inglês visual, ES-LATAM (C5, #4): 6,5.** BR: 109d, 117 ativos. MX: Mapasyresumenes (US$5 a 7, 1 dia, cobrança BRL). Para EUR: IT tem 451 a 517 dias de vendedores de método de estudo, mas nenhum kit imprimível. Ticket baixo. Sem gancho legal.
6. **STL pack para Alemanha/França (C1, #1/#12/#38): 6,0.** DE e FR sem nenhum vendedor de pack (0 e 4 anúncios); ES provado (125d, 80d), US provado (209d a 374d). Ticket €4,90 a 9,90. Risco alto de direitos autorais dos modelos e de concorrência gratuita (repositórios); precisaria de modelos próprios. Católico: ES já com Mundo Católico 80d/4cr.
7. **Eletricista (tabela de preços + comandos), ES/DE (C17, #32/#35): 6,0.** BR clonando para EUA em inglês (3 a 9 dias, Vifalio); ES "precios de electricista" e DE "Schützschaltung" com 0 anúncios. Tamanho: ES 29.847 vagas de eletricista em 2025 (InfoJobs, via merca2) e déficit citado de ~70.000. Falta o gancho legal com data (VERIFICAR) e a contagem de autônomos. É profissional, cabe no foco; reaproveita o app (tabela por serviço).
8. **Educação em Itália: schede didattiche (C6, #7/#10/#14/#49): 6,0.** BR com 80 a 90 dias e 85 a 110 ativos. Itália: onda de clones de 1 a 2 dias a €7,90 / €9,99. Janela aberta mas já disputada; entrar com mecanismo próprio (PEI/BES, materiais por faixa) em vez de "2.500 schede". Prévia: IT 30 e 33 em V2.
9. **Marcenaria: planos DIY, Alemanha/Itália/Espanha (C3, #3/#52): 5,5.** FR provado (WoodCrafts DIY 104d/12cr), US/GB 126 a 194d. DE 0 anúncios; IT/ES com testes de 2 a 3 dias. Preço e conteúdo das páginas não confirmados (dropship). Sem gancho legal.
10. **Guia de comida caseira para cães, ES/DE/IT (C8, #9): 5,5.** Nenhum guia anunciando em ES e DE (marcas de ração fresca só); IT teste de 2 dias. Tamanho: cães DE 10,5M, ES 9,46M, IT 8,77M (fonte secundária da FEDIAF). Sem gancho legal; cuidado com promessa veterinária.

Fora do top 10 mas notáveis: Claude por profissão em ES (já 22d/12cr, saturando rápido), CapCut FR (214d, mas é curso), moldes de costura DE/IT/ES (mercado nativo existe), presets (lojas em EN dominam).

## 5. O que continuou VERIFICAR

1. SearchAPI zerou em 30/10 (10000/10000). Buscas não feitas ou falhas por 429/crédito: freezer meals (US/GB/DE/FR/IT/PT via SS), plans de herrería ES, patrones/sewing US/FR/DE (só CN), schede/fiches/Arbeitsblätter/fichas/printable, sílabas ES/MX/IT, perros/dog food (SS), CapCut ES, mapas mentales ES/US/DE/FR, ADHD planner SS, psicopedagogía ES, mentoría, comandos eléctricos ES, radiesthésie FR/IT/DE/PT e dowsing US (SS, só CN), presets ES/US, endodoncia IT/US, ebooks, packs de música. Reabrir depois de 08/11 ou comprar o plano de US$40.
2. **Dias reais** de: Mente Inquieta (ES), Lumi Editions (FR), Lybstes (DE), Studio Facile/Attivita Premium/Pronti via (IT), Boîte du Thérapeute (FR). O conector não dá a data do mais antigo. Reconferir em SS em 7 a 14 dias para ver se algum passa de 30.
3. **Preços das páginas de venda** (só vi preço em anúncio: US$5 a 7 Mapasyresumenes, €7,90 Attivita Premium, €9,99 Pronti via, US$3,99 Roberto). Páginas de radiestesia FR/IT/ES e WoodCrafts DIY não foram abertas.
4. Tamanho e **gancho legal com data** para: eletricistas (autônomos e instaladores ES/DE), radiestesia (nenhum dado), cães (só fonte secundária), TDAH (sem gancho).
5. Ofertas não pesquisadas: 0, 17, 24, 44, 45 (genéricas/direitos/fora de escopo), 18, 19, 29 (fitness), 26, 34, 36 (profissionais de nicho BR), 2, 15, 27, 43, 51 (receitas BR-específicas).
6. Direitos autorais de STL e packs de ebooks/músicas: não são produtos replicáveis como estão.
