# Catálogo EscalaLow, parte 2 (índices 53 a 105): brechas por país (30/10/2026)

> Data de referência: 30/10/2026. Fonte: `dados/escalalow-ofertas-validadas.json` (213 ofertas BR validadas; índices base 0, faixa 53–105 = 53 ofertas).

## Avisos de método (ler primeiro)
- A v1 desta pesquisa (29/10) e os arquivos do Desktop NÃO estavam acessíveis neste ambiente. Esta versão foi feita do zero, com as notas do usuário (`notas/*.md`) como contexto.
- **SearchAPI indisponível** (sem chave neste container e sem crédito até 08/11/2026). Toda a medição foi feita com o **conector Meta (`ads_library_search`)**, que só retorna anúncios ATIVOS.
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = estimativa da consulta por página.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias NO país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.
- Fora do escopo: harmonização facial e injetáveis.
- **Bloqueios desta rodada:** (a) a cota de busca web da sessão, compartilhada com os agentes irmãos, esgotou na primeira consulta; (b) WebFetch e curl são barrados pela lista de domínios deste ambiente (Eduzz, Lovable, Wikipedia, sites dos vendedores). Por isso nenhuma página de vendas foi aberta e nenhum número de mercado ou norma foi confirmado com fonte: tudo isso está marcado VERIFICAR.
- O conector Meta não devolve o texto nem o link do anúncio, só o título; o produto de cada vendedor foi deduzido do título.

## Status
Concluído em 30/10/2026. Cobertura: 53 ofertas agrupadas em 36 conceitos (7 profissionais) + 6 ofertas excluídas; cerca de 84 consultas ao conector Meta (busca por termo em ES, LATAM, PT, IT, FR/BE, DE/AT/CH, PL, RO, NL/BE, EN) e 19 vendedores medidos (14 por página). Uma pausa por limite de uso ("Too Many Requests") foi contornada reduzindo o ritmo.

**Top 5:** (1) documentos de psicomotricidade + app, IT/FR/AR/UY/PT/ES, BRECHA, 7,0; (2) kit do terapeuta/psicólogo infantil IT/FR, TESTE urgente, 6,5; (3) Pilates aulas prontas ES/PT/FR, TESTE, 6,0; (4) fono/logopedia ES/PT, BRECHA, 6,0; (5) grafismo fonético ES/IT/FR, TESTE (PROVADO MX), 6,0.

## 1. As 53 ofertas e o agrupamento por conceito

Dados do EscalaLow (Brasil). "Dias BR" e "Ativos" são os do arquivo, não remedidos. Os grupos: **P** = profissional (kit para a profissão, o que mais interessa), **C** = professor(a), **M** = pais, **A** = artesanato/papelaria para vender, **R** = receitas, **F** = religioso, **D** = design/marketing, **E** = estudante/autoconhecimento, **H** = hobby, **X** = excluído.

| # | Oferta (nome no EscalaLow) | Dias BR | Ativos | Preço R$ | Profissão/público | Termo do produto | Conceito (grupo) |
|---|---|---|---|---|---|---|---|
| 53 | +200 Dinâmicas para Alfabetização Infantil | 63 | 29 | 9,90 | Professora alfabetizadora / pais | dinâmicas de alfabetização | C1 Alfabetização (lectoescritura) |
| 54 | Manual Prático do Eletricista Residencial | 63 | 29 | — | Eletricista residencial | manual prático do eletricista | P6 Eletricista |
| 55 | Kit Baralho de Perguntas Terapêuticas | 51 | 29 | 37,00 | Psicólogo / terapeuta | baralho de perguntas terapêuticas | P4 Cartas terapêuticas |
| 56 | Kit Aula Pronta | 68 | 29 | — | Professora (ed. infantil/fundamental) | aula pronta / atividades com gabarito | C2 Aula pronta |
| 57 | A Sombra Certa | 56 | 29 | — | Hobby (desenho) | livro de sombras (The Pencil Method) | H2 Desenho (vendedor estrangeiro) |
| 58 | Guia de Cosméticos Naturais | 164 | 28 | 19,00 | Consumidor / empreendedora | receitas de cosméticos naturais | R3 Cosmético natural |
| 59 | Pack Elite STL | 107 | 28 | — | Maker impressão 3D | pack de arquivos STL | A6 STL 3D |
| 60 | 🍽️ Tem diabetes e fica em dúvida sobre o que pode comer? | 80 | 28 | — | Diabético (consumidor) | receitas para diabéticos (WhatsApp) | R1 Receitas diabéticos |
| 61 | Projetos Cartonadas | 105 | 28 | 10,00 | Artesã (cartonagem p/ vender) | projetos de cartonagem com medidas | A1 Cartonagem |
| 62 | Kit Consultório Lúdico | 91 | 28 | 17,00 | Psicólogo infantil | kit consultório lúdico (+80 recursos) | P5 Consultório lúdico |
| 63 | pack figurinhas 2 | 280 | 27 | 14,99 | Empreendedor (Instagram) | pack de figurinhas p/ stories | D1 Design/Canva/stories |
| 64 | Receba no Whatsapp | 51 | 27 | — | Consumidor religioso | Cartinhas da Esperança (imprimir) | F1 Cartões cristãos/devocional |
| 65 | 💛 Um presente que cuida de quem você ama, mesmo quando você  | 102 | 27 | — | (sem texto; WhatsApp) | presente afetivo (não identificado) | X Não identificado |
| 66 | 🧶Mais de 1000 modelos de macramê para você criar peças incrí | 60 | 26 | 67,00 | Artesã | +1000 modelos de macramê | A4 Macramê |
| 67 | +1000 Moldes de Kit Festa Prontos para Montar e Vender | 52 | 26 | 10,00 | Papelaria festa (p/ vender) | +1000 moldes kit festa | A2 Kit festa |
| 68 | Musicalização Infantil | 82 | 26 | 19,00 | Pais, musicoterapeutas, professores | musicalização infantil | C6 Musicalização |
| 69 | Combo NeuroTrilhas | 86 | 26 | 27,00 | Pais | atividades NeuroTrilhas (atenção/concentração) | M1 Estimulação infantil (pais) |
| 70 | Guia para Trabalhos Acadêmicos com Inteligência Artificial | 104 | 26 | 27,00 | Universitário | guia TCC com IA | E1 TCC com IA |
| 71 | Guia do Suco | 82 | 25 | 49,00 | (anabolizantes) | Guia do Suco | X Fora do escopo (substância controlada) |
| 72 | Teste de Superdotação | 77 | 25 | 47,00 | Adulto (autoconhecimento) | teste/rastreio de superdotação | E2 Altas habilidades |
| 73 | Kit de Grafismo Fonético | 461 | 25 | 37,00 | Pais / professoras | kit grafismo fonético | C3 Grafismo fonético |
| 74 | +800 Temas de Mini Livrinhos para Colorir | 61 | 25 | 12,90 | Professora / pais | +800 mini livrinhos para colorir | C4 Mini livrinhos |
| 75 | 80 Cafés da Manhã para Substituir o Pão | 143 | 24 | 17,90 | Consumidor | 80 cafés da manhã sem pão | R2 Receitas (café sem pão) |
| 76 | Livro físico ou e-book | 187 | 24 | 37,00 | Leitor | livro físico/e-book de autor | X Livro de autor (não replicável) |
| 77 | SOMENTE HOJE | 52 | 24 | — | Consumidor religioso | devocional Café com Jesus | F1 Cartões cristãos/devocional |
| 78 | +500 prompts prontos | 77 | 24 | 47,00 | Consumidor (fotos) | +500 prompts de fotos IA | D2 Prompts IA |
| 79 | 🐻💖 KIT DE URSINHOS PERSONALIZADOS 💖🐻 | 92 | 23 | — | Artesã (papel) | kit ursinhos personalizados de papel | A2 Kit festa |
| 80 | 🧠 150 Mapas Mentais de Cinesiologia para você dominar os fun | 62 | 23 | 17,90 | Estudante/prof. educação física | 150 mapas mentais de cinesiologia | E3 Mapas mentais saúde |
| 81 | Cabala dos Odùs Ilustrada | 49 | 23 | 19,90 | Religião afro-brasileira | Cabala dos Odùs ilustrada | F2 Odù/Ifá (BR-específico) |
| 82 | +300 modelos prontos para você imprimir, montar e vender | 82 | 22 | — | Papelaria (p/ vender) | +300 modelos imprimir/montar | A2 Kit festa |
| 83 | Kit de Estimulação Cognitiva | 169 | 22 | 10,00 | Professora / pais | kit estimulação cognitiva (Hexaconexão) | M1 Estimulação infantil (pais) |
| 84 | Leve uma palavra de Deus para cada pessoa que você encontrar | 91 | 22 | — | Consumidor religioso | cartõezinhos cristãos | F1 Cartões cristãos/devocional |
| 85 | Pack Renda3D | 103 | 22 | 9,90 | Maker impressão 3D | pack STL porta-latas | A6 STL 3D |
| 86 | 500 Receitas para Diabéticos | 70 | 22 | — | Diabético (consumidor) | 500 receitas para diabéticos | R1 Receitas diabéticos |
| 87 | Pilates Pro: 150+ Aulas Prontas para Aplicar | 58 | 22 | 10,00 | Instrutor(a) de Pilates | 150+ aulas de Pilates prontas | P3 Pilates aulas prontas |
| 88 | Canva Aesthetic Club® | 50 | 22 | 27,00 | Empreendedora (Instagram) | posts Canva aesthetic | D1 Design/Canva/stories |
| 89 | Clube Pequenos Criadores | 105 | 21 | 19,90 | Pais | clube projetos/robótica infantil | M2 Robótica/projetos infantis |
| 90 | Esse vídeo é pra você que tem uma empresa | 236 | 21 | — | Empresas (serviço local) | dedetização | X Serviço local (não é infoproduto) |
| 91 | Kit Sólidos Geométricos | 98 | 21 | 10,00 | Professor(a) matemática | kit sólidos geométricos | C5 Sólidos geométricos |
| 92 | Biblioteca RPG Master | 62 | 21 | 29,99 | Hobby | biblioteca de RPG de mesa | H1 RPG |
| 93 | Pack de Moldes para Prática de Mandala | 88 | 21 | 37,90 | Consumidor (arte/ansiedade) | pack de moldes de mandala | A5 Mandala/bordado |
| 94 | +150 Exercícios Prontos para Fala e Leitura Infantil | 101 | 20 | — | Fonoaudióloga / pais | +150 exercícios de fala e leitura | P2 Fono (exercícios de fala) |
| 95 | E-book: 15 Minutos por dia com sua Bíblia | 390 | 20 | 19,90 | Cristão | 15 min/dia com a Bíblia (autor) | F3 Estudo bíblico (autor) |
| 96 | KIT ESSENCIAL | 125 | 20 | 47,00 | (Prof Renato Porto) | KIT ESSENCIAL (não identificado) | X Não identificado |
| 97 | Livro físico ou em e-book | 209 | 20 | — | Leitor | livro físico/e-book de autor | X Livro de autor (não replicável) |
| 98 | Há um artesanato delicado que talvez você ainda não conheça | 217 | 20 | 27,00 | Consumidor (arte/calma) | bordado no papel | A5 Mandala/bordado |
| 99 | Documentos de Psicomotricidade | 118 | 20 | 15,90 | Psicomotricista | +60 documentos de psicomotricidade | P1 Psicomotricidade (documentos) |
| 100 | Minha Página | 83 | 20 | 10,00 | Papelaria festa (p/ vender) | kit festinha digital | A2 Kit festa |
| 101 | Protocolo Seguidores Orgânicos | 401 | 20 | 60,00 | Empreendedor | protocolo seguidores orgânicos | D3 Marketing Instagram |
| 102 | Kit Estimula Bebê, 131 Atividades para o 1º Ano de Vida | 66 | 20 | 19,90 | Pais (pediatra) | 131 atividades 1º ano do bebê | M3 Estimulação do bebê |
| 103 | [Planilha Inteligente] Método Comparativo Direto de Dados de | 72 | 20 | — | Avaliador/corretor de imóveis | planilha Método Comparativo Direto | P7 Avaliação de imóveis |
| 104 | +100 Moldes Prontos de Caixas Para Canecas | 57 | 20 | 37,00 | Artesã (sublimação) | +100 moldes caixas p/ canecas | A3 Caixas p/ caneca |
| 105 | Você não precisa ter deixado de amar a Bíblia para ter dific | 562 | 19 | — | Cristão | método de leitura bíblica (autor) | F3 Estudo bíblico (autor) |

**Conceitos agrupados (36 conceitos; 7 deles profissionais):**
- Profissionais (P): P1 psicomotricidade (99), P2 fono (94), P3 Pilates (87), P4 cartas terapêuticas (55), P5 consultório lúdico infantil (62), P6 eletricista (54), P7 avaliação de imóveis (103).
- Professor(a) (C): C1 alfabetização (53), C2 aula pronta (56), C3 grafismo fonético (73), C4 mini livrinhos (74), C5 sólidos geométricos (91), C6 musicalização (68).
- Pais (M): M1 estimulação infantil (69, 83), M2 robótica/projetos (89), M3 bebê 1º ano (102).
- Artesanato (A): A1 cartonagem (61), A2 kit festa/papel (67, 79, 82, 100), A3 caixas de caneca (104), A4 macramê (66), A5 mandala/bordado (93, 98), A6 STL 3D (59, 85).
- Receitas (R): R1 diabéticos (60, 86), R2 café sem pão (75), R3 cosmético natural (58).
- Religioso (F): F1 cartões/devocional (64, 77, 84), F2 Odù/Ifá (81), F3 estudo bíblico de autor (95, 105).
- Design/marketing (D): D1 Canva/stories (63, 88), D2 prompts IA (78), D3 seguidores (101).
- Estudante (E): E1 TCC com IA (70), E2 altas habilidades (72), E3 mapas mentais de cinesiologia (80).
- Hobby (H): H1 RPG (92), H2 desenho/sombras (57; já é de vendedor estrangeiro, The Pencil Method, vendendo no BR em USD).
- Excluídos (X): 65 e 96 (produto não identificado), 71 (anabolizantes, fora do escopo), 76 e 97 (livro de autor), 90 (serviço local de dedetização).

## 2. Resultado por país (tabela de TODAS as ofertas)

Legenda: **PROV** = vendedor com 30+ dias no país/idioma/moeda; **novo Xd** = vendedor com menos de 30 dias (dias reais medidos ou do anúncio mais antigo visto); **0** = busca sem nenhum vendedor de infoproduto (só serviços, escolas, lojas ou nada); **sat.** = muitos vendedores ativos; **n/p** = não pesquisado nesta rodada. Números entre parênteses = total estimado de anúncios ativos da busca. Moeda = moeda da conta do anunciante (BRL/USD em página de outro país = operador estrangeiro, quase sempre brasileiro).

### 2.1 Profissionais (o que mais interessa)

| Conceito (ofertas) | ES (Espanha) | LATAM (MX/CO/AR/CL/PE/UY) | PT | IT | FR/BE | DE/AT/CH | PL | outros | Leitura |
|---|---|---|---|---|---|---|---|---|---|
| P1 Documentos de psicomotricidade (99) | 0 kit de documentos (58 anúncios: escolas/serviços); PsicoMotion Kids, conta BRL, **atividades** (não documentos), 43d | 0 kit de documentos; AR/UY "psicomotricista" (22) só profissionais e cursos | 0 (39: clínicas, evento "Psicomotricidade Summit"; Sara Duarte "PlayMento" 8d, jogo) | 0 kit; "neuropsicomotricista" (4) só serviços; PsicoMotion Kids "200 attività di psicomotricità", USD, 2d | 0 ("psychomotricien" 5 anúncios, nenhum kit; "bilan psychomoteur" 0) | n/p | n/p | NL/BE "psychomotorische therapie" 0 | **BRECHA em todos os países pesquisados** |
| P2 Fono / exercícios de fala (94) | 0 ("logopedia actividades" 4 anúncios) | sem kit fono visível ("ejercicios de lenguaje" 583, ruído) | 0 ("terapia da fala exercícios" 5) | ABA Tools (USD, IT+EN, 133 anúncios, **90d**): atividades ABA para terapeutas | Audrey Monnet (EUR, ~38 anúncios, **≥35d**): produto p/ pais (respiração bucal, miofuncional); Annalisa Galli (USD) 3–4d | 0 ("Logopädie Übungen Material" 1, workshop) | sat. nativo (SAREO app, NeuroDots, centros PLN) | RO 0 kit; US/UK nativo (Speech Cube, box) | **BRECHA ES/PT/DE**; IT e FR provados em formatos vizinhos |
| P3 Pilates, aulas prontas (87) | Clara Ríos (USD, ~14 anúncios, 2,7d, "50 clases listas para dar" + "modo clase" no celular); Pilates con Método (USD, <1d, Reformer) | mesmos (busca ES+LATAM) | Centerline Pilates Portugal (USD, ~0,8d, "100 aulas de 60 min + 500 fichas") | busca trouxe só professores (Elena Costa, Amelia Parker, Aulaprima, USD, 1–2d) | Séancier (USD, 14 anúncios, <1d, "104 séances prêtes à donner") | 0 ("Pilates Stundenbilder") | n/p | EN 885, ruído de estúdios | **TESTE**: onda de clones começou 27–29/10, ninguém com 30d |
| P4 Cartas terapêuticas (55) | Terapeuta Creativo (USD, <1d, imprimível) | idem | n/p | Strumenti per Terapeuti (USD, 7,8d); Therapy Toolkit (USD, IT 20,7d, também EN e FR); Il Percorso del Terapeuta (USD, 1,8d); Bienestar Consciente (USD, 12,9d); Living in Christ (BRL, <1d) | Laura Martins (BRL, "1 257 outils", <1d); La Route du Thérapeute / Ruta Del Terapeuta (USD, <1d); Living in Christ (BRL) | n/p | sat. nativo (TherapyTools, Epedagogika.pl, Portal Oświatowy) | US: ThinkPsych (nativo) | **TESTE**, com onda BR entrando em IT/FR nesta semana |
| P5 Consultório lúdico infantil (62) | Universo Terapéutico Digital (BRL, 1–1,5d) | MenteCloud.com (conta CLP, 6,6d) | 0 | 0 ("psicologo infantile attività pronte") | ver P4 (kits de terapeuta) | n/p | n/p | — | **TESTE** (mesma onda de P4) |
| P6 Eletricista (54) | Maestro José Luis Hernández (BRL, ~1d, "+500 proyectos eléctricos residenciales"); Energy volts (BRL) | Maestro Eléctrico (USD, AR, 13,8d) | Miguel Ferreira (BRL, ~1,7d, **mesmo título** "Manual Prático do Eletricista Residencial" + "Comandos Elétricos") | Claude Ingegneria Elettrica PRO (BRL, <1d, "500+ Progetti Elettrici + 4 Bonus, 27 €"); Studio Quadri (USD, ~1d) | Commandes Électriques (USD, **24,0d**); Nodivra Studio (USD, 8,8d, "guide visuel de l'électricien") | n/p | n/p | — | **TESTE**; FR vira PROVADO se Commandes Électriques passar de 30d (≈05/11) |
| P7 Planilha de avaliação de imóveis (103) | 0 ("tasación inmobiliaria plantilla") | 0 | 0 ("avaliação imobiliária" 192 = só imobiliárias) | n/p | n/p | n/p | n/p | — | **BRECHA sem prova** (nicho regulado, ver §4) |

### 2.2 Professores, pais e estudantes

| Conceito (ofertas) | ES | LATAM | PT | IT | FR | outros | Leitura |
|---|---|---|---|---|---|---|---|
| C1 Alfabetização/dinâmicas (53) | ver LATAM | "lectoescritura dinámicas" (93): Megapack Online (PEN), Material psicología educativa (MXN), Aprende Y Crece (USD) | n/p | n/p | n/p | — | mercado hispano já ativo (sat.) |
| C2 Aula pronta (56) | n/p | MX "clases listas maestras" (33): Planeaciones para ti (MXN, nativo), El Rincón de las Maestras (USD, 1,4d) | n/p | "lezioni pronte insegnanti" (94): Lingello (conta PLN, ~1d), Aulaprima (USD, ~2d), Amelia Parker (USD, "un anno già pronto", 2d) | n/p | — | MX nativo; IT onda nova |
| C3 Grafismo fonético (73) | Planeta Mini Genios (EUR, 8,0d); Mi Peque Aprende (EUR, <1d) | **Eduki (MXN, 19 anúncios, 73,1d) = PROVADO MX** | busca vista em PT trouxe só espanhol | só anúncios em espanhol (FVA02 BRL **237d**, Maria Pereira BRL **245d**) | idem | — | **PROVADO MX**; ES nascendo; IT/FR/PT-PT sem vendedor no idioma local |
| C4 Mini livrinhos de colorir (74) | 0 do conceito | 0 do conceito ("mini libros para colorear" 28, kits genéricos) | n/p | n/p | n/p | — | **BRECHA (consumidor)** |
| C5 Sólidos geométricos (91) | — | Daniela Garcia (USD, 43,4d, espanhol neutro); Infinitum Digital (PEN, 4,6d, S/ 9); Profe Laura Gomes (COP, 1,5d) | n/p | n/p | n/p | — | espanhol neutro provado; PE/CO nascendo |
| C6 Musicalização (68) | — | só Kit Primera Infancia Listo (BRL, 2,5d) | n/p | Orbis Atlas (USD, música, 1,6d) | n/p | — | quase vazio |
| M1 Estimulação infantil/neuro (69, 83) | — | "estimulación cognitiva niños" (93): Espacio Crianza Integral (USD, <1d), El arte de Aprender (MXN) | n/p | rede nova de páginas USD (Growing Agile Minds etc., <2d) | n/p | **RO: Mom A-Z Romania (EUR, 21 anúncios, 100,1d, "Metoda Neuro Gym") = PROVADO** | provado na Romênia; IT inundando |
| M2 Robótica/projetos infantis (89) | n/p | n/p | n/p | n/p | n/p | — | não pesquisado (VERIFICAR) |
| M3 Bebê 1º ano (102) | — | "estimulación temprana bebé actividades" (248) = serviços | n/p | 0 ("attività neonato primo anno" 1, curso) | n/p | — | **BRECHA IT**; LATAM sem infoproduto visível |
| E1 TCC com IA (70) | — | "tesis con inteligencia artificial" (264): universidades, serviços | n/p | n/p | n/p | — | sem kit claro |
| E2 Altas habilidades (72) | **Cientoymucho (EUR, 55,5d, teste online, serviço)** | AR: clínicas (ARS 114–197d, serviços) | n/p | 0 | 0 ("test haut potentiel adulte") | — | ES provado como serviço; FR/IT brecha sensível |
| E3 Mapas mentais cinesiologia (80) | — | "mapas mentales anatomía" (142): Biblioteca Clínica (USD, <1d), Nube Digital Latam (USD) | n/p | n/p | n/p | — | ativo (há pesquisa irmã de mapas mentais) |

### 2.3 Consumidor (artesanato, receitas, religioso, design, hobby)

| Conceito (ofertas) | Espanhol (ES+LATAM) | IT | Leitura |
|---|---|---|---|
| A1 Cartonagem (61) | "moldes cartonaje" (4): só ART SHOP (USD, 11,3d) | n/p | quase vazio em espanhol |
| A2 Kit festa/papel (67, 79, 82, 100) | "kit imprimible fiesta" (12): Tienda Digital Perú (PEN), Florescer em Família (BRL), Hay un Plan (USD) | n/p | pouco disputado |
| A3 Caixas de caneca (104) | (9): Ediciones Vertice (USD, <1d, "moldes a tamaño real") | n/p | nascendo |
| A4 Macramê (66) | (222): Borda y emprende (ARS, nativo) | n/p | sat. |
| A5 Mandala/bordado (93, 98) | "bordado en papel" (174): El Bordado de Fe (USD, <1d) + lojas | n/p | ativo |
| A6 STL 3D (59, 85) | "archivos STL" (744): Marcos Santiny (USD) e muitos | n/p | sat. |
| R1 Diabéticos (60, 86) | (498): Luci Guadalupe (BRL), CocinaSalud 2026 (COP) | (68): L'Arte di Nutrirsi Bene (conta MXN, ~2d) | sat. em espanhol; IT nascendo |
| R2 Café sem pão (75) | "desayunos sin pan" (496): Valeria Méndez (USD) + ruído | n/p | sat. |
| R3 Cosmético natural (58) | (193): Mister Z (BRL), Affluo Beauty (BRL), Árvores (CLP) | n/p | BR já em espanhol |
| F1 Cartões/devocional (64, 77, 84) | devocional (32): Emprende con Alma (COP); tarjetas cristianas (91): Bendiciones creativas (USD) | n/p | ativo |
| F2 Odù/Ifá (81) | n/p | n/p | nicho afro-brasileiro, fora |
| F3 Estudo bíblico de autor (95, 105) | n/p | n/p | depende do autor, não replicável |
| D1 Canva/stories (63, 88) | (601): Chelly Lima (BRL), Flora Disegno (ARS) | n/p | sat. |
| D2 Prompts IA (78) | (49): Negócios Digitais (BRL, 0,8d), AI Master (USD, "29 €") | n/p | nascendo |
| D3 Seguidores orgânicos (101) | n/p | n/p | marketing genérico, fora |
| H1 RPG (92) | 0 | n/p | brecha sem prova |
| H2 Desenho/sombras (57) | n/p | n/p | o próprio vendedor é estrangeiro (The Pencil Method) |
| Excluídos (65, 71, 76, 90, 96, 97) | — | — | 96 = "Prof Renato Porto" (BRL, Black Friday 70% off), produto não identificado |

### 2.4 Termos traduzidos (para as próximas buscas)

Termos usados nesta rodada estão em **negrito**. Os demais são traduções propostas, ainda não buscadas.

| Conceito | ES (Espanha) | MX/CO/AR/CL/PE | PT-PT | IT | FR | DE | PL | RO | CZ/SK | HU | GR | NL | EN | TR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 documentos de psicomotricidade | **psicomotricidad**, **documentos psicomotricidad** | **psicomotricista** (AR/UY) | **psicomotricidade** | **psicomotricità**, **neuropsicomotricista** (TNPEE) | **psychomotricien**, **bilan psychomoteur** | Psychomotorik Befundbogen | psychomotoryka | psihomotricitate | psychomotorika | pszichomotoros terápia | ψυχοκινητική | **psychomotorische therapie** | psychomotor therapy forms | psikomotor terapi |
| P2 fono, exercícios de fala | **logopedia actividades** | **ejercicios de lenguaje**, terapia de lenguaje, fonoaudiología | **terapia da fala exercícios** | **logopedia schede** | **orthophonie exercices** | **Logopädie Übungen** | **logopeda ćwiczenia** | **logoped exerciții** | logopedická cvičení / cvičenia | logopédiai feladatok | ασκήσεις λογοθεραπείας | logopedie oefeningen | **speech therapy printable activities** | dil konuşma terapisi |
| P3 Pilates, aulas prontas | **clases de pilates listas** | idem | **aulas de pilates prontas** | **lezioni di pilates pronte** | **séances de pilates prêtes** | **Pilates Stundenbilder** | gotowe zajęcia pilates | lecții de pilates | lekce pilates | pilates óravázlat | μαθήματα pilates | pilates lesplannen | **pilates class plans** | pilates ders planı |
| P4 cartas terapêuticas | **cartas terapéuticas** | idem | cartas terapêuticas | **carte terapeutiche** | **cartes thérapeutiques** | Therapiekarten | **karty terapeutyczne** | cărți terapeutice | terapeutické karty | terápiás kártyák | θεραπευτικές κάρτες | therapiekaarten | **therapy cards for therapists** | terapi kartları |
| P6 manual do eletricista | **manual electricista** | idem | **eletricista manual** | **guida elettricista** | **électricien guide schémas** | Elektroinstallation Handbuch | poradnik elektryka | manualul electricianului | příručka elektrikáře | villanyszerelő kézikönyv | εγχειρίδιο ηλεκτρολόγου | handboek elektricien | electrician handbook | elektrik tesisatı kitabı |
| C3 grafismo fonético | **grafismo fonético** | idem | **grafismo fonetico** | grafismo fonetico | graphisme phonétique | — | — | — | — | — | — | — | phonetic graphism | — |
| M1 estimulação/neuro infantil | **estimulación cognitiva niños actividades** | idem | — | **giochi per il cervello bambini concentrazione** | jeux cerveau enfants | Gehirntraining Kinder | ćwiczenia koncentracji dla dzieci | **Metoda Neuro Gym** | — | — | — | — | brain games kids | — |

## 3. Vendedores medidos (dias reais, anúncios, moeda)

Medição por `page_ids` no conector Meta (só ativos). Quando a página tem mais anúncios do que a amostra, o valor é "≥" (o anúncio mais antigo pode estar fora da amostra). Página de vendas, preço, bumps e garantia: **não foi possível abrir nenhuma** (rede deste ambiente bloqueia os domínios; ver §6).

| Página (page_id) | País/idioma | Moeda da conta | Anúncios ativos | Dias reais | Produto (pelo título do anúncio) | Status |
|---|---|---|---|---|---|---|
| Mom A-Z Romania (102170736310283) | RO | EUR | 21 | **100,1** | "Metoda Neuro Gym", jogos para o cérebro e concentração infantil | PROVADO RO (M1) |
| ABA Tools (108617997275390) | IT + EN | USD | 133 | **≥90,6** | "+500 Attività ABA Naturalistiche", "Meno preparazione, sedute più leggere" | PROVADO IT (terapeutas, formato vizinho de P2/P5) |
| Eduki (988954757628041) | MX | MXN | 19 | **73,1** | grafismo fonético ("Del sonido a la letra", "Material listo para tu salón") | PROVADO MX (C3) |
| Cientoymucho (1001143956411927) | ES | EUR | n/m | **≥55,5** | "Test online de detección de altas capacidades. Servicio profesional." | PROVADO ES como serviço (E2) |
| Daniela Garcia (100796846213618) | espanhol neutro | USD | n/m | **≥43,4** | "Kit de Cuerpos Geométricos" | provado só em espanhol neutro (C5) |
| PsicoMotion Kids (1016893401512562) | ES (BRL) e IT (USD) | BRL/USD | 12 | 43 (ES); 2 (IT) | atividades de psicomotricidade (não documentos) | ES provado p/ atividades; IT novo |
| Audrey Monnet (1074362272427474) | FR | EUR | ~38 | **≥35** | produto para pais: respiração bucal, "jeux du petit nez" | PROVADO FR (consumidor, vizinho de P2) |
| Commandes Électriques (1368969016297770) | FR | USD | ~13 | 24,0 | guia de comandos elétricos | quase provado (re-checar ≈05/11) |
| Therapy Toolkit (102506312071455) | IT, FR, EN | USD | ≥200 (junto com Strumenti: 236) | ≥20,7 (IT) | "Kit di risorse terapeutiche per adolescenti" | TESTE (P4/P5) |
| Maestro Eléctrico (1027617017094389) | AR | USD | ~10 | 13,8 | eletricista ("Comentá Yo Quiero") | TESTE |
| ART SHOP (633754546495433) | espanhol | USD | 4 | 11,3 | moldes de cartonagem | TESTE |
| Nodivra Studio (986176944570114) | FR | USD | n/m | ≥8,8 | "Le guide visuel de l'électricien qui démarre" | TESTE |
| Planeta Mini Genios (1338863152636535) | ES | EUR | 4 | 8,0 | "Aprende a leer jugando, 10 min/día" | TESTE ES (C3) |
| Strumenti per Terapeuti (1390402674157680) | IT | USD | 2 | 7,8 | "Kit di Carte per Terapeuti" | TESTE |
| MenteCloud.com (1317896694749207) | CL | CLP | n/m | ≥6,6 | recursos para psicólogos infantis | TESTE |
| Clara Ríos · Pilates y Yoga (1325918880615223) | ES/LATAM | USD | ~14 | 2,7 | "50 clases listas para dar", "+220 ejercicios con ficha", "modo clase" no celular, pagamento único | TESTE (P3) |
| Pilates con Método (827226377138589) | ES/LATAM | USD | 6 | <1 | aulas de Reformer | TESTE |
| Séancier (1408265095703553) | FR | USD | 14 | <1 | "Vos 104 prochaines séances, prêtes à donner" | TESTE |
| Miguel Ferreira (1356560714196106) | PT | BRL | n/m | ~1,7 | mesmo "Manual Prático do Eletricista Residencial" do BR | TESTE |

n/m = não medido por página (dias do anúncio mais antigo visto na busca por termo).

**Padrão que aparece em quase todos os conceitos:** entre 20/10 e 29/10 operadores brasileiros (contas BRL ou USD, nomes estrangeiros inventados) começaram a clonar as ofertas desta faixa para IT, FR, PT e espanhol, muitas vezes com o mesmo título do Brasil (eletricista, Pilates, kits de terapeuta, psicomotricidade). Quase nenhum tem 30 dias ainda. A janela de "primeiro a chegar" nesses países está fechando agora.

## 4. Mercado e normas (fontes)

**Não foi possível confirmar nenhum número com fonte oficial nesta rodada:** a cota de busca web da sessão (compartilhada com os agentes irmãos) esgotou na primeira consulta, e o acesso direto a sites (WebFetch/curl) é bloqueado pela lista de domínios deste ambiente. Tudo abaixo é conhecimento prévio, a confirmar; nada disto deve ir para página de vendas antes da checagem.

| Conceito | País | O que sustenta a brecha (a confirmar) | Status |
|---|---|---|---|
| P1 Psicomotricidade | FR | psychomotricien é profissão de saúde regulamentada, com diploma de Estado (Code de la santé publique); o "bilan psychomoteur" costuma ser feito sob prescrição médica. Número de profissionais: ordem de 10–15 mil. | VERIFICAR (DREES / Légifrance) |
| P1 Psicomotricidade | IT | TNPEE (terapista della neuro e psicomotricità dell'età evolutiva) é profissão sanitária com albo (federação TSRM-PSTRP, após a Lei 3/2018). | VERIFICAR (número no albo, norma de documentação) |
| P1 Psicomotricidade | AR, UY | licenciatura em psicomotricidade com exercício regulamentado (UY: formação na UdelaR; AR: leis provinciais). | VERIFICAR |
| P1 Psicomotricidade | ES, PT | ES: profissão sem colégio próprio em todo o país (há associações). PT: psicomotricistas com associação profissional (APP). | VERIFICAR |
| P2 Fono | ES | logopeda é profissão sanitária com colégios autonômicos (Consejo General de Colegios de Logopedas). | VERIFICAR (número de colegiados) |
| P2 Fono | PT | terapeuta da fala é profissão de saúde regulamentada (ACSS, cédula profissional). | VERIFICAR |
| P3 Pilates | todos | não há regulamentação específica do instrutor de Pilates nos países pesquisados; o gancho é só operacional (aula pronta, ficha de aluno, anamnese, termo). | VERIFICAR |
| P6 Eletricista | FR | norma NF C 15-100 (revisão recente) e atestado de conformidade (Consuel). | VERIFICAR (datas de vigência) |
| P6 Eletricista | ES | REBT (RD 842/2002) + certificado de instalação (CIE) e inspeções por OCA. | VERIFICAR (há revisão do REBT em andamento?) |
| P6 Eletricista | IT | DM 37/2008 (dichiarazione di conformità) e norma CEI 64-8. | VERIFICAR |
| P6 Eletricista | PT | RTIEBT e certificação da instalação. | VERIFICAR |
| P7 Avaliação de imóveis | ES, PT | ES: avaliação "oficial" só por sociedades de tasación homologadas pelo Banco de España; PT: peritos avaliadores registrados na CMVM. Planilha de "método comparativo" serviria a corretores, não a avaliadores oficiais. | VERIFICAR |
| E2 Altas habilidades | FR, IT | teste psicológico é ato de psicólogo; vender "teste" ao consumidor pode ter restrição. Só como "questionário de autopercepção". | VERIFICAR |

## 5. Ranking das brechas (0–10) e reaproveitamento

Critérios: encaixe no modelo do usuário (kit de documentos + app por profissão), prova de compra (no BR e fora), concorrência no país, gancho legal (só conta se confirmado; aqui está tudo VERIFICAR) e velocidade da onda de clones. Nenhuma nota passa de 7 porque nenhum mercado e nenhuma norma foram confirmados com fonte nesta rodada.

| # | Brecha | Países | Régua | Nota | Por quê | Reaproveita |
|---|---|---|---|---|---|---|
| 1 | **Documentos de psicomotricidade + app** (99) | IT (TNPEE), FR, AR/UY, PT, ES | BRECHA | **7,0** | BR provado (118d, 20 ativos, R$15,90). Em nenhum dos países pesquisados há kit de documentos; o único estrangeiro (PsicoMotion Kids) vende *atividades*, e entrou em IT há 2 dias. Profissão regulamentada em FR, IT, UY/AR (VERIFICAR). | **Valigetta** quase inteira: anamnese, avaliação psicomotora, relatório para pais/neurologista, evolução, app de sessões. IT primeiro (usa o funil italiano), depois AR/UY em espanhol e FR. |
| 2 | **Kit do terapeuta / psicólogo infantil** (55, 62) | IT, FR | TESTE (urgente) | **6,5** | ABA Tools vende atividades para terapeutas em IT há ≥90d (133 anúncios). Desde ~20/10 uma onda BR (Therapy Toolkit ≥21d, Strumenti per Terapeuti, Il Percorso del Terapeuta, Laura Martins, La Route du Thérapeute) entrou em IT e FR. Confirma a demanda e mostra que a janela do **Psicólogo Itália** (já na fila) está se fechando. | **Valigetta** do psicólogo; diferencial = normas italianas (já levantadas) e app, que nenhum clone tem. |
| 3 | **Pilates: aulas prontas + ficha de aluno + app** (87) | ES, PT, FR (DE vazio) | TESTE | **6,0** | BR provado (58d, 22 ativos, R$10). Quatro clones nasceram entre 27 e 29/10 (Clara Ríos já com "modo clase" no celular, Séancier, Centerline Pilates Portugal, Pilates con Método); ninguém com 30d. Re-checar 12/11: se sobreviverem, vira PROVADO. | **Valigetta** (anamnese, PAR-Q, termo de responsabilidade, evolução) + aulas; app de "modo aula". |
| 4 | **Fono / logopedia: exercícios + documentos** (94) | ES, PT (DE vazio) | BRECHA | **6,0** | Zero vendedor em ES (4 anúncios), PT e DE. Formatos vizinhos provados: IT (ABA Tools ≥90d) e FR (Audrey Monnet ≥35d, produto para pais). PL e EUA têm mercado nativo forte (não ir). | **Valigetta** do fono (anamnese, avaliação, relatório, plano) + banco de exercícios. |
| 5 | **Grafismo fonético** (73) | ES, IT, FR, PT-PT | TESTE | **6,0** | PROVADO no México (Eduki, MXN, 73d) e em espanhol neutro por brasileiros há ~8 meses (FVA02 237d, Maria Pereira 245d). Na Espanha a onda está começando (Planeta Mini Genios 8d, Mi Peque Aprende <1d). Em italiano e francês ninguém vende o método. Produto de consumidor/professora, fora do modelo "profissão". | Nenhum dos três ativos; produto simples. |
| 6 | **Manual/kit do eletricista** (54) | FR, IT, PT, ES | TESTE | **5,5** | BR provado (63d). Clones em todos os países em 1–24 dias; FR é o mais perto de PROVADO (Commandes Électriques 24d → re-checar 05/11). Gancho de norma (NF C 15-100, REBT, DM 37/08) a confirmar. | **App de inspeção** (checklist de conformidade com fotos e relatório antes do Consuel/OCA/dichiarazione) e **Consultora** (simulador "passa na vistoria"), se a norma confirmar. |
| 7 | **Neuro Gym / estimulação infantil** (69, 83) | RO | PROVADO no RO | **5,0** | Mom A-Z Romania com 21 anúncios e 100 dias, em euro. Na Itália já há uma rede de páginas novas; em espanhol há muitos. Consumidor, fora do modelo. | — |
| 8 | Sólidos geométricos (91) | espanhol neutro, PE, CO | TESTE | 4,5 | Daniela Garcia 43d (USD); nativos PE/CO nascendo. IT/FR não pesquisados. | — |
| 9 | Bebê 1º ano (102) | IT | BRECHA | 4,0 | Zero em IT; LATAM só serviços. Sem prova fora do BR. | — |
| 10 | Teste de altas habilidades (72) | ES (FR/IT brecha) | PROVADO ES (serviço) | 4,0 | Cientoymucho 55d em euro, mas é serviço; teste psicológico é sensível (VERIFICAR). | — |
| 11 | Planilha de avaliação de imóveis (103) | PT, ES | BRECHA sem prova | 3,5 | Ninguém vende, mas a avaliação oficial é restrita a avaliadores registrados (VERIFICAR). | App de inspeção (vistoria com fotos) |
| 12 | Mini livrinhos de colorir (74) | ES/LATAM | BRECHA | 3,5 | Ninguém vende o conceito; consumidor, ticket baixo. | — |
| 13 | Cartonagem em espanhol (61) | ES/LATAM | TESTE | 3,5 | Só ART SHOP (11d). | — |
| — | Receitas (diabéticos, café sem pão, cosmético), Canva/stories, STL, macramê, bordado, devocional, prompts | espanhol | saturado | ≤3 | Muitos vendedores ativos; sem vantagem para o usuário. | — |
| — | Excluídos: 65, 71 (anabolizantes), 76/97 (livro de autor), 81 (Odù, nicho BR), 90 (serviço), 95/105 (autor), 96 (não identificado), 101 | — | — | — | — | — |

**Leitura geral:** desta faixa, o que encaixa no modelo do usuário e ainda está vazio lá fora é **psicomotricidade (1)** e **fono na Espanha/Portugal (4)**. Os kits de terapeuta (2), Pilates (3) e eletricista (6) já têm clones BR com menos de 30 dias: provam que outros operadores leram o mesmo sinal, mas ainda não provam venda. A única prova longa fora do BR nesta faixa está em formatos vizinhos: ABA Tools (IT, ≥90d), Mom A-Z (RO, 100d), Eduki (MX, 73d), Audrey Monnet (FR, ≥35d).

## 6. Lista final de VERIFICAR

1. **Páginas de vendas:** nenhuma pôde ser aberta (a rede deste ambiente bloqueia eduzz, lovable.app, avalliemais, renato.tv.br, wikipedia e outros). Faltam preço, plataforma, conteúdo, bumps e garantia das ofertas BR desta faixa e dos vendedores estrangeiros (ABA Tools, Therapy Toolkit, Eduki, Mom A-Z Romania, Clara Ríos, Séancier, Centerline Pilates Portugal, Commandes Électriques, Nodivra, Cientoymucho, Audrey Monnet).
2. **Tamanho de mercado e normas da §4:** nenhum confirmado (cota de busca web esgotada e sites oficiais bloqueados). Prioridade: número de psychomotriciens (FR), TNPEE no albo (IT), psicomotricistas (AR/UY/PT), logopedas colegiados (ES), terapeutas da fala (PT); vigência de NF C 15-100, REBT, DM 37/08, RTIEBT.
3. **Re-checagens com data:**
   - 05–06/11: Commandes Électriques (FR) passa de 30 dias? Se sim, eletricista FR vira PROVADO.
   - ≈09/11: Therapy Toolkit (IT) chega a 30 dias.
   - 12/11: os clones de Pilates (Clara Ríos, Séancier, Centerline Pilates Portugal, Pilates con Método) e de terapeuta (Strumenti per Terapeuti, Il Percorso del Terapeuta, Laura Martins, La Route du Thérapeute) continuam ativos?
   - 22/11: Planeta Mini Genios (grafismo fonético, ES) chega a 30 dias.
   - 28/11: PsicoMotion Kids em IT (psicomotricidade) chega a 30 dias.
4. **Países não pesquisados nesta rodada:** CZ, SK, HU, GR, TR, IE, NZ; DE, PL e RO só para alguns conceitos. Termos já traduzidos na §2.4.
5. **Conceitos não pesquisados:** M2 robótica infantil (89), F2 Odù (81), D3 seguidores (101), H2 desenho (57), e a maioria dos conceitos de consumidor fora do espanhol.
6. **Ofertas não identificadas:** 96 "KIT ESSENCIAL" (página "Prof Renato Porto", BRL, Black Friday até 70% off) e 65 (Prof.ª Selma, só WhatsApp).
7. **Moeda:** o campo `currency` do conector é a moeda da conta de anúncios, não a do checkout. Contas BRL/USD em páginas italianas, francesas ou portuguesas indicam operador estrangeiro (provavelmente BR), não prova de venda em euro.
8. **Amostras:** em páginas com mais anúncios do que a amostra (ABA Tools 133, Therapy Toolkit ~200), os dias reais podem ser maiores que o valor medido.
9. **Comparação com a v1:** a v1 (29/10) não estava acessível; não há como listar diferenças.
