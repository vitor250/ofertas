# Catálogo EscalaLow, parte 3 (índices 106 a 158, 53 ofertas): brechas internacionais (30/10/2026)

Fonte: `3 - EU/pesquisas/brechas-europa-2026-10-28/escalalow-ofertas-validadas.json`, itens 106 a 158. Harmonização/injetáveis fora.

## Método e limites (leia antes)
- Regra: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. BRECHA = ninguém vende. Espanhol neutro não prova país.
- SearchAPI (frase exata, só ativos, dias por page_id): 271 buscas disparadas, 196 válidas. **O crédito do SearchAPI acabou em 30/10 (10.000/10.000, os outros agentes consumiram o mesmo plano)** e 75 buscas voltaram 429/sem crédito. Dados brutos: `pesquisas-nichos-2026-10-29/dados-parte3/r1..r8.json` (script `medir3.py`).
- Conector `ads_library_search` (usado de apoio): devolve só os anúncios mais novos, sem ordenar por idade, então dá contagem e vendedor, mas os dias só quando o anúncio é de uma página que já medi. Dias do conector = hoje menos `ad_delivery_start_time`, só da amostra lida (3 a 10 anúncios). Onde marquei "amostra", o vendedor pode ser mais antigo.
- Frase exata zera fácil: "0 anúncios" significa "nenhum anúncio com essa frase", não "ninguém vende". Vendedores no Etsy/Amazon não aparecem (Etsy bloqueia com 403).
- Não abri páginas de vendas além das listadas na seção de preços. Tamanho de profissão com fonte só onde achei dado; o resto está em VERIFICAR.

## Conceitos (grupos)
| ID | Conceito | Ofertas |
|---|---|---|
| C1 | Papelaria/moldes de caixas, agendas e calendários 2027 para imprimir e vender | 106, 107, 122, 128 |
| C2 | Papelaria de casamento editável | 111 |
| C3 | Elétrica residencial / segurança eletrônica | 108, 153 |
| C4 | Receitas (geladinho, doces para vender, ervas medicinais) | 110, 147, 148 |
| C5 | Projetos/planos de marcenaria, pergolados, galinheiros, casinhas de pássaros | 112, 113, 125, 129, 138, 146 |
| C6 | Moldes de costura infantil | 114 |
| C7 | Pré-escrita/grafomotricidade/alfabetização/jogos impressos | 115, 136, 142, 143, 158 |
| C8 | Livro de lápis de cor | 116 (109 é livro de autor, fora) |
| C9 | Documentos clínicos para psicólogo / plataforma neuropsicopedagoga | 117, 120 |
| C10 | Mapas mentais/resumos por carreira + gerador de apostilas com IA | 118, 119, 133, 154 |
| C11 | Cifras de igreja | 121 |
| C12 | Artes para sublimação/estamparia | 123, 137, 139 |
| C13 | Estimulação cognitiva para idosos (kit para familiar) | 124 |
| C14 | Religioso (Odus, São Bento) | 126, 150 |
| C15 | Templates de consultoria | 127 |
| C16 | Perito judicial | 155 |
| C17 | Kit ABA / VB-MAPP | 130 |
| C18 | Curso de cílios | 131 |
| C19 | Cabelo/fitness (protocolo capilar, TransformaFit) | 132, 156 |
| C20 | Projetos ambientais | 134 |
| C21 | Posts prontos Canva para profissionais (lash, dra., personal) | 135, 144, 151 |
| C22 | Bordado em papel | 145 |
| C23 | Projetos de papelão para crianças | 149 |
| C24 | Contador (reforma tributária) | 152 |
| C25 | Planilha financeira | 157 |
| C26 | Fora de escopo/ruído | 109, 140, 141 |

## Tabela das 53 ofertas
Preço = preço BR na página (R$) quando o JSON tem; "?" = vende por WhatsApp. Dias/anúncios = BR no catálogo.

| # | Oferta (BR) | Preço BR | Conceito / profissão | Resultado por país (quem vende, dias, moeda, preço, ou "ninguém") | Veredito |
|---|---|---|---|---|---|
| 106 | Biblioteca de Moldes de Caixas 2026 (68d/19) | 27,90 | C1 papeleira/personalizados | PT "moldes de caixas" 3 anúncios, ninguém ≥30d; MX 7, ES 5, ninguém ≥30d; US/DE/FR 0 | BRECHA (todos) |
| 107 | Calendários 2027 pets (50d/18) | ? | C1 | PT "calendário 2027" 6 anúncios sem vendedor ≥30d; IT/FR/DE/US kit imprimível 0. DE: só editoras de calendário em livro (Elizalde, Gallo, 56 a 78d, 3-5 criativos, não é kit). ES: ver 122 | BRECHA PT/IT/FR; DE só livro |
| 108 | 18 instalações elétricas residenciais (76d/18) | ? | C3 eletricista/leigo | ES Faradayos "Guía ilustrada de instalaciones eléctricas" ~56d, USD, 2 criativos lidos (amostra); PT 104 anúncios só lojas/eletricistas; DE "Elektroinstallation selber machen" 0; MX, IT, FR, US não medi (429) | TESTE ES; DE/IT têm lei que restringe obra elétrica de leigo (risco) |
| 109 | Livro físico/e-book do autor (209d) | 37 | livro de autor | fora de escopo | N/A |
| 110 | Guia caseirinhos (71d/18) | ? | C4 renda extra | não medi; "para vender" já classificado lotado em 28/10 | descartado |
| 111 | Kit Papelaria de Casamento Canva (114d/18) | 37 | C2 noivas/cerimonialista | PT, MX, IT, FR, DE, GB, US ("convites de casamento editáveis" e equivalentes): 0 anúncios com a frase; Etsy domina e não aparece | VERIFICAR |
| 112 | Pack Oficina Lucrativa +5.000 moldes (172d/18) | 9,90 | C5 marceneiro/serralheiro | ver C5 abaixo | ver C5 |
| 113 | Projetoteca Pergolados/Toldos (105d/18) | 17 | C5 | "planos de pérgola" ES 0; "Pergola Bauplan" DE 0; "pergola plans" US 0; "plans pergola" FR 0; "progetto pergola" IT 0 | BRECHA (5 países) |
| 114 | +100 moldes de vestidos infantis (82d/18) | ? | C6 costureira | ES "patrones de ropa infantil" 0; IT "cartamodelli bambina" 0; FR "patrons couture enfant" 0; DE "Schnittmuster Kinderkleid" 0; GB 1 anúncio; US "sewing patterns pdf" 6 (Florence + The Makers 104d, 4 cr, loja); MX só app SewPal 79 a 84d (app, não kit) | BRECHA kit; cuidado direitos de molde |
| 115 | Caligrafia cursiva com Salmos (92d/18) | 49,99 | C7 pais/catequese | FR "écriture cursive": Caaly 377d (caderno físico), Petitecrivain 49d 8 cr (físico); ES/MX "caligrafía cursiva" 2; DE "Schreibschrift Übungsheft" 0; US 4; versão com versículos: ninguém | TESTE (nicho cristão sem vendedor) |
| 116 | A Cor Certa, lápis de cor (57d/18) | US$17 (era 47) | C8 desenhista amador; vendedor é operador internacional (The Pencil Method, URL /br/usd) | GB "colored pencil" 43 anúncios: Kirsty Partridge 358d (workshop grátis), Art Storefronts; DE "Buntstifte Zeichnen lernen" 0; US "colored pencil guide" 0; ES/MX/FR/IT não conclusivo | VERIFICAR (vendedor já é cross-border) |
| 117 | Combo PSI Prático (72d/18) | 37,90 | C9 psicólogo | Não refiz (429). Ver `3 - EU/pesquisas/psicologo-dentista-4-paises-2026-10-29.md`: IT tem BR a €19,99 há 30+d; ES psicólogo 6/10; PT 5/10. Reaproveita a Valigetta dello Psicologo | já coberto |
| 118 | Apostila Visual (55d/18) | 37 | C10 professor | ver 119 | ver 119 |
| 119 | Gerador de Apostilas (70d/18) | 37 | C10 professor (app com IA) | ES "generador de fichas con IA", "crear material didáctico con IA" 0; DE "Arbeitsblätter mit KI" 0; FR "créer des fiches avec l'IA" 0; IT 0; PT 0; US "worksheet generator" 13 anúncios, education.com 78d (plataforma grande, não kit) | BRECHA (5 idiomas, frase exata) |
| 120 | Neurolyn, plataforma clínica (80d/17) | 49 | C9 neuropsicopedagogo | "informes psicopedagógicos" ES/MX, "plantillas psicólogos": 429, não medido | VERIFICAR |
| 121 | K34 cifras simplificadas de igreja (186d/17) | ? | C11 músico de igreja | MX "cifrados de alabanza" 0, "cifrados guitarra" 0 (conector "cifrados de alabanza guitarra" MX 0); ES "acordes iglesia" 0; US "worship chord charts" 0; PT "cifras igreja" 0; CO "cifrados" 44 sem vendedor do tipo | BRECHA aparente (termo pode estar errado) |
| 122 | Kit Encadernação 2027 (112d/17) | 10 | C1 papeleira | ES "agenda 2027": Papelia Digital 65d 2 cr (superpack de agendas para vender), Papelería Creativa (WhatsApp) 52d 4 cr "aprende a crear agendas personalizadas"; PT/IT/FR/DE: só fotógrafos de casamento e calendários impressos; MX "calendario 2027" Edukopolis 57d é calendário de vestibular UDG (outra coisa) | PROVADO ES (clones BR); BRECHA PT/IT/FR/DE |
| 123 | Macros Corel para sublimação (181d/17) | 37 | C12 sublimador | MX "diseños para sublimar" Pixelpack 96d 14 cr (pixelmedia.store, "atención sublimadores"); MX "plantillas sublimación" 2; ES/US/DE "sublimation templates/Sublimation Vorlagen" 0; GB "sublimation designs" 9 anúncios, ninguém ≥30d com 2+ cr; US bundle 1 | PROVADO MX (LatAm); BRECHA EU/EN |
| 124 | Kit para cuidar de idoso com esquecimento, Projeto Vida Plena (85d/17) | ? | C13 familiar/cuidador | ES (conector) "estimulación cognitiva adultos mayores" 64 anúncios: Professora Maria (moeda BRL, novo, ~5d) e Geriactiva (AR, 32d+ em 28/10); IT "stimolazione cognitiva anziani" 17 anúncios, só assistência domiciliar e cadeira, nenhum kit. Ver pesquisa 28/10: DE CareTable 127d/9 cr, DE Gedächtnistraining 140 anúncios, nenhum nativo imprimível | BRECHA IT; ES já com BR novo (TESTE); DE nicho de profissional (§43b SGB XI) |
| 125 | +60 Projetos de Galinheiros (48d/17) | 19,90 | C5 | ES "planos de gallinero" 0; FR "plans poulailler" 0; DE "Hühnerstall Bauplan" 0; IT "pollaio fai da te" 0; PT "galinheiro" só WoodSense (app) 84d 4 cr; US "chicken coop plans" 12 anúncios, Tri City Shed Plans 60d 2 cr (Etsy); GB 10 | BRECHA EU; US com um vendedor pequeno |
| 126 | Os 16 Odus Meji ilustrado (75d/17) | 17,90 | C14 praticante de religião afro | ES "odus de Ifá" 0; US "Ifá odu" 0; MX "oráculo de Ifá" 1; PT "odus" 1; ES "santería" 19 anúncios (consulentes, não curso); US "orisha" 77 (Instagram/pessoas) | BRECHA aparente; nicho espiritual, mercado US/Cuba/ES a validar |
| 127 | Sistema Consultoria Única (83d/17) | 27 | C15 consultor | ES "plantillas consultoría" 0, "plantillas para abogados" ES/MX 0; IT 0; US "consulting templates" 1; GB 0 | BRECHA aparente, sem prova de demanda |
| 128 | +300 moldes de mesa posta (72d/17) | 10 | C1 | PT "mesa posta" 52 anúncios, só restaurantes/lojas; Agatha Moraes (BR, kit digital festa) 60d; US "tablescape" influencers/Amazon; MX "mesa de postres" salões | BRECHA |
| 129 | Vai construir? Casa de Campo, VG Projetos (195d/16) | ? | C5 arquiteto/projetista | classificado "plantas de casa" lotado em 28/10; não refiz | descartado |
| 130 | Kit de Programas Transformação, VB-MAPP (183d/16) | 47 | C17 ABA/terapeuta/pais | **EN: ABA Tools (en.abatools.pro) 133d, 9-10 cr, US/GB e também aparece em ES; "Practical Autism Transformation Toolkit": Basic US$9 (de 49), Completo US$17 (de 230), 5 áreas x 15 programas, 7 bônus, certificado, garantia 30d (WebFetch).** US "The Autism Helper" loja 101d. ES: ABA Tools 133d, ES "terapia ABA autismo" 0 nativo; MX "terapia ABA" 14 anúncios, 5 anunciantes, nenhum ≥30d com 2+ cr; IT/DE "terapia ABA autismo"/"ABA Therapie Autismus" 0; FR/PT não medi | PROVADO EN (BR já exportado a US$9-17); BRECHA IT/DE; TESTE ES |
| 131 | Curso de extensão de cílios (198d/16) | ? | C18 lash designer | IT ONYX Academy 90d 12 cr (curso presencial); FR Maya Academy 30d 4 cr, Nalhya 44d 2 cr; MX curso 31d 2 cr; US 48 anúncios, 3 anunciantes; DE 1 | saturado de cursos, descartar |
| 132 | Protocolo Capilar Natural (72d/16) | ? | C19 | ES/MX "cronograma capilar", US/FR/IT/DE "curly girl": 429, não medido | VERIFICAR |
| 133 | Resumo Esquematizado, psicologia (70d/16) | 37 | C10 estudante de psicologia | US "study guide psychology" 1; ES "mapas mentales" 823 anúncios (ver 154) | ver 154 |
| 134 | Biblioteca Profissional Ambiental (48d/16) | 19,90 | C20 engenheiro ambiental/consultor | MX "estudio de impacto ambiental" 6 anúncios, CO 3; ES "proyectos ambientales modelos" 0; IT/DE "valutazione impatto ambientale modelli"/"Umweltgutachten Vorlage" 0 | BRECHA aparente |
| 135 | Pack MasterLash Canva (48d/16) | 27,90 | C21 lash designer | ES "posts para pestañistas" 0; US "instagram templates lash" 0; IT/FR/DE/MX "template Canva estetista/esthéticienne/Kosmetik": 429 | VERIFICAR |
| 136 | 50 pranchas de massinha (61d/16) | 10 | C7 pais/professor infantil | US "playdough mats" 20 anúncios: Planning Playtime 234d 13 cr (sight words); MX "plastilina fichas" 0; ES "tapetes de plastilina" 0; IT "schede pongo" 0; FR "tapis pâte à modeler" 0; DE "Knetkarten" 0 | PROVADO US; BRECHA ES/IT/FR/DE (termo pode variar) |
| 137 | 2.500 artes cristãs para camisetas (134d/15) | 10 | C12 | MX "diseños cristianos para camisetas" 0; US "christian svg bundle" 0 e "christian shirt designs" 0 (vende em Etsy) | VERIFICAR |
| 138 | Móveis profissionais, 2.000 projetos (73d/15) | ? | C5 | ver C5 | ver C5 |
| 139 | +1.000 estampas de pano de prato (83d/15) | ? | C12 | ES "estampados paños de cocina" 0; US "tea towel designs" 0 | BRECHA aparente |
| 140 | Pack otimização de PC (48d/15) | ? | tecnologia | ES "PC lento" 1; MX "optimizar PC" 0; DE "PC langsam" 0; zona cinza (suporte técnico) | descartado |
| 141 | Top Toner (55d/15) | ? | loja física | fora de escopo | N/A |
| 142 | Kit Alfabetização Alfa Kids (165d/14) | 57 | C7 pais/professor | MX "kit de alfabetización" 64 anúncios, 3 anunciantes (WhatsApp, clones BR); ES "lectoescritura fichas" 1; IT "pregrafismo": Mente Gentile 40d 5 cr (pedagogista nativa, curso/pack); DE/FR graphisme/Schwungübungen: cadernos mágicos físicos | PROVADO MX/CO; TESTE IT |
| 143 | Lúdica Pedagógica, jogos de leitura (148d/14) | 15 | C7 professor | "juegos didácticos para imprimir" MX, "giochi didattici da stampare" IT, "Lernspiele zum Ausdrucken" DE, "jeux éducatifs à imprimer" FR: 429 | VERIFICAR |
| 144 | 50 Viral Kids, posts para personal (59d/14) | 47 | C21 personal trainer | ES/US/IT/FR/DE "plantillas canva entrenador": não rodei | VERIFICAR |
| 145 | Bordado Criativo, bordado em papel (66d/14) | 37 | C22 hobby/artesanato | **US: The Paper Atelier 144d 3 cr; The Evening Stitch 61d 24 cr, US$27 (sobe para 47), 500 padrões imprimíveis, 4 bônus, reembolso 7d, é clone do copy BR ("There's a quieter craft you may not have heard of yet").** IT: "Ricamo su Carta da Zero" (Sofia Bennett, USD) ~8d, 3+ anúncios, TESTE novo; DE "Papierstickerei" 1 anúncio; FR "broderie sur papier" 6 anúncios, ninguém ≥30d; MX "bordado en papel" 11 anúncios, ninguém ≥30d; ES (conector) sem vendedor claro | PROVADO US; TESTE IT (8d); BRECHA DE/FR/ES |
| 146 | +100 moldes de casinhas e comedouros (96d/14) | ? | C5 | DE "Vogelhaus Bauplan" 0; FR "plans nichoir" 0; ES "casitas para pájaros" 0; US "birdhouse plans" 1 | BRECHA |
| 147 | Geladinho gourmet (113d/14) | ? | C4 renda extra | MX "paletas heladas" 44 anúncios: Lula Love 477d 2 cr (serviço de eventos), Helados Finos Juvi 136d 2 cr (franquia); ES "helados caseros para vender" 0; IT "ghiaccioli fatti in casa" 0; US "ice pop recipes" 0 | BRECHA kit de receitas; MX tem vendedores de produto, não de receita |
| 148 | +2.000 receitas com ervas medicinais (111d/14) | ? | C4 | PT "plantas medicinais": "Os remédios caseiros de antigamente" 174d 20 cr (copy BR, em PT-PT); FR Anne Vastel (CA) ebook 693d; DE "Die Ernährungslüge" 654d (livro); US The Lost Book of Herbal Remedies 93d (3 cr, saturado); IT "erbe medicinali" 19 anúncios, só cosmético; ES "plantas medicinales recetas" 0; MX 420 anúncios (produtos) | PROVADO PT/FR/DE/US; BRECHA IT/ES (claims de saúde: cuidado) |
| 149 | 120 projetos de papelão para crianças (75d/14) | ? | C23 pais | **ES (conector): Rincón de Aprendizaje ~119d, USD, 2 anúncios lidos "Tu hijo no necesita más pantalla. Necesita crear"; Pequeños Inventores "+120 proyectos" (novo, <1d).** DE: Mundo Inventor "+350 Projekte statt Bildschirmzeit" (USD, ~3d, 3+ anúncios) TESTE; US "cardboard crafts for kids" 863 anúncios (genérico); IT, FR: 429 | PROVADO ES; TESTE DE; VERIFICAR IT/FR |
| 150 | Kit de São Bento (71d/14) | ? | C14 devoto católico | MX "medalla de San Benito" 61 anúncios, só lojas (Sanborns, Cordero Sagrado); IT/PL/US/ES: 429 | VERIFICAR (e é produto devocional, não kit de documento) |
| 151 | Glow Season, 70 posts para "Dra." (49d/14) | 47 | C21 | não rodei no exterior | VERIFICAR |
| 152 | Axxen, modelos de monetização para contadores (49d/14) | ? | C24 contador (reforma tributária BR) | ES "contadores servicios" 0, MX "plantillas contador" 0, IT "modelli commercialista" 0, US "bookkeeping templates" 1 | BRECHA; ver pesquisa do Contador (Raio-X dos Honorários) |
| 153 | Maleta Digital Instalador de Segurança Eletrônica (100d/14) | 17 | C3 instalador CFTV/alarme | MX "cámaras de seguridad instalación", ES "instalador de alarmas", IT, US, DE: 429, não medido | VERIFICAR |
| 154 | Mapas Mentais, Método Mapeei (89d/13) | 67 | C10 concurseiro/estudante | **ES: Mapas Visuales PRO (mapasvisuales.pro, "+250 mapas mentales de ingeniería civil") 39d 7 cr; Estudia Sencillo (MX, farmacología) 97d 8 cr; Digital Nova 69d 3 cr; ES "mapas mentales" 823 anúncios totais. MX "mapas mentales" 1.085 (Tus Clases Online 64d 11 cr etc.). PT: Fluente com Legenda 55d 28 cr ("+300 mapas mentais" de inglês, copy BR em PT-PT). DE: Frau Anna Müller Mathematik (mindmapsmathe.vercel.app) 30d 2 cr. IT "mappe mentali" 546 (Centro Studi Lambda 451d, MyEdu 120d: método de estudo, não kit por carreira); IT "mappe concettuali concorso" 0; ES "mapas mentales oposiciones" 0; FR "cartes mentales" 285 (Kontre Kourant 198d, Objectif CRPE 183d)** | PROVADO ES/MX/PT (clones BR); TESTE DE; BRECHA IT concorsi |
| 155 | Guia do Perito Blindado (103d/13) | 67 | C16 perito judicial | ES "peritos judiciales" 9 anúncios, "informe pericial" 42: Escuela Nacional de Peritos 281d 16 cr (cursos, perícia de veículos); MX "perito judicial" 3: "Guías profesionales" (clone BR, peritaje contable) 38d 2 cr; IT "consulente tecnico d'ufficio": April Academy 86d 4 cr (curso universitário); FR/DE/PT 0; US/GB "expert witness" outros | PROVADO ES (curso, não kit); TESTE MX; BRECHA kit/guia |
| 156 | TransformaFit, treino com peso do corpo (330d/13) | ? | C19 | "rutina sin equipo", "bodyweight workout plan", "allenamento a corpo libero": 429 | VERIFICAR (categoria saturada) |
| 157 | Planilha Gestão Financeira Empresarial (166d/13) | 10 | C25 pequeno empresário | 9 buscas (MX/ES/IT/FR/DE/US/GB/PT) com "plantilla excel…", "Excel Vorlage Buchhaltung" etc.: 0 anúncios com a frase | VERIFICAR (inconclusivo) |
| 158 | Desenvolva a escrita do seu filho, grafomotricidade (97d/13) | 37 | C7 pais | **MX "grafomotricidad" 91 anúncios: Edukidz (WhatsApp) 175d 11 cr, Impulso Educativo 94d 3 cr, Creciendo Juntos 91d 6 cr; CO: Descargables educativos 65d 10 cr; ES/CO/PT: FVA02 (grafomotor-kit-builder.lovable.app, clone BR) 238d 3-5 cr.** PT-PT: Tienda E-Home 175d 17 cr (kit físico), Ana Ferreira/atividadespremium.pt 95d 2 cr (kit digital de atividades). IT "pregrafismo": Mente Gentile 40d 5 cr. DE "Schwungübungen": Laura's Kinderwelt/Edubini 133d (caderno mágico físico); FR "graphisme maternelle" 0 | PROVADO MX/CO/PT; TESTE IT; BRECHA DE/FR digital |

## C5, marcenaria/planos de projeto (112, 113, 125, 129, 138, 146): detalhamento
- **EN provado e crescendo:** US "woodworking plans" 268 anúncios: Crafted Wood DIY 194d, Wood Blueprints 137d (4 cr), Craft Blueprints 126d. GB mesmos três. AU (conector, 200 anúncios): Wood Atlas Plans (EUR), Creativo Digital (nome espanhol vendendo "60 furniture plans" em inglês, USD), Woodplans (SEK, copy "Become a woodworking expert", igual ao WoodSense), "TedsWoodworking Review" (afiliado). Ou seja, os clones de ES/BR já estão arbitrando em inglês.
- **Preço de referência:** Crafted Wood DIY, €27 (riscado €97), 150+ projetos, medidas em polegada e cm, bônus de assistente de IA, página mostra "out of stock" (WebFetch).
- **ES-LATAM:** MX (conector, 186 anúncios): Planos y Diseños de Herrería, Plano Cerrado ("100+ planos de carpintería", USD), Creación Digital; ES (Argentina): Planoteca, Metal & Madera, oficiosrentables. Todos com anúncios novos na amostra; **idade não medida (VERIFICAR)**.
- **Idiomas europeus nativos:** DE "Möbel selber bauen Bauplan" 0 (conector), "Holzprojekte Bauplan", "Hühnerstall Bauplan", "Vogelhaus Bauplan", "Pergola Bauplan" 0; FR "plans poulailler/pergola/nichoir/de meubles" 0; IT "pollaio fai da te", "progetto pergola" 0, "progetti falegnameria" 46 anúncios sem vendedor ≥30d; ES-ES "planos de gallinero/pérgola/muebles" 0; PT-PT só WoodSense (app, USD, 84d, 4 cr). Nota: a frase exata pode subestimar.
- **Tamanho:** Alemanha, 37% dos respondentes fazem reparo ou obra por conta própria (49% dos homens), segundo YouGov (https://yougov.com/de-de/artikel/14544-ob-do-it-yourself-oder-upcycling-drei-von-funf-deu) e a pesquisa de interesse em DIY da Statista (https://de.statista.com/statistik/daten/studie/170918/umfrage/interesse-an-heimwerken-und-do-it-yourself/). Faturamento do mercado de baumarkt não achei (VERIFICAR).
- **Gancho legal com data:** não há. Gancho sazonal: inverno/Natal (presentes de madeira, casinhas de pássaros).

## Ranking das brechas (0 a 10)
| Nota | Brecha | Evidência | Tamanho (fonte) | Gancho | Reaproveitamento |
|---|---|---|---|---|---|
| 7,5 | **C5 planos de marcenaria/pergola/galinheiro/casinha em DE, FR, IT, ES-ES, PT-PT** (112, 113, 125, 138, 146) | EN provado 126 a 194d (US/GB), EUR já aparece em AU; DE/FR/IT/ES/PT nativo: zero vendedores nas frases testadas | DE: 37% fazem obra própria (YouGov, link acima) | sem data; sazonal inverno/Natal | Pack de projetos + app tipo WoodSense; mesmo funil das "Projetotecas". Não usa a Consultora |
| 7 | **C13 estimulação cognitiva para familiar/cuidador (IT)** (124) | IT: 17 anúncios, nenhum kit; ES já com BR novo (Professora Maria, ~5d, BRL) e Geriactiva (AR); pesquisa 28/10: DE CareTable 127d, ninguém nativo imprimível | IT: 78.826 pessoas com diagnóstico de autismo nos 1.214 centros, mas para idosos não achei contagem (VERIFICAR) | DE §43b SGB XI (profissionais de cuidado, regulado) | Mesmo kit adaptado; entra junto com Consultora/Valigetta como "kit para profissional do cuidado" |
| 7 | **C17 kit ABA/VB-MAPP em IT e DE** (130) | EN provado: ABA Tools 133d, 9 a 10 criativos, US$9/US$17 (BR faz R$47); ES 133d; IT/DE 0 anúncios | IT: prevalência 1 em 77 crianças de 7 a 9 anos (ISS), 1.214 centros de diagnóstico (https://www.quotidianosanita.it/?p=133644; https://www.orizzontescuola.it/disturbo-dello-spettro-autistico-in-italia-la-prevalenza-raggiunge-1-bambino-su-77-leta-della-diagnosi-scende-a-3-anni-ma-restano-forti-disomogeneita-territoriali-nellaccesso-ai-servizi/). Número de analistas do comportamento em IT/DE: não achei (VERIFICAR) | sem data; EN já dá prova de preço | Reaproveita o kit BR traduzido; mesma arquitetura da Valigetta (documentos clínicos) |
| 7 | **C10 mapas mentais por concurso/carreira em IT (e DE)** (154, 133, 118) | ES/MX/PT provado por clones BR (39 a 97d); IT: "mappe concettuali concorso" 0, só métodos genéricos; DE só um teste vercel de 30d | IT: concurso PNRR3 teve 225 mil candidatos para 58 mil vagas (https://catania.liveuniversity.it/2025/11/12/concorso-pnrr3-docenti/amp/); novo concurso ordinário esperado entre fim de 2026 e início de 2027, data não oficial (https://www.docenti.it/blog/concorsi-scuola-2026-quante-sono-le-assunzioni-previste/) | Concurso docente IT (data a confirmar) | Irmão do simulador de opositores ES (nº 1 ES em 28/10); app + mapas |
| 6,5 | **C22 bordado em papel em DE, FR, ES, PT** (145) | US provado (144d e 61d, 24 criativos, US$27); IT só 8 dias (TESTE); DE 1 anúncio, FR 6 sem ≥30d, MX 11 sem ≥30d | hobby/artesanato, tamanho não medido (VERIFICAR) | sem data; presente de Natal | Padrões imprimíveis + vídeo; ticket €19 a €27; pouca concorrência local |
| 5,5 | **C10b gerador de fichas/apostilas com IA para docentes** (118, 119) | 0 anúncios em ES, DE, FR, IT, PT; US só education.com; todos com frase exata | mercado docente já levantado (opositores ES, Kita DE); ver pesquisa 28/10 | início de ano letivo (set) | App lovable reaproveita o gerador BR; tradução simples |
| 5,5 | **C7 pré-escrita/grafomotricidade digital em DE e FR (e IT mais fraco)** (158, 136, 142, 115) | provado MX/CO/PT (clones BR 65 a 238d); IT Mente Gentile 40d; DE/FR só caderno físico "mágico" | Kita DE / maternelle FR (já em pesquisa 28/10) | Einschulung (DE, set) | Atividades infantis já são repetição entre países |
| 5 | **C23 projetos de papelão** (149) | ES provado ~119d (Rincón de Aprendizaje, USD); DE Mundo Inventor ~3d (BR ou LatAm); IT/FR não medi | pais com "menos tela" | Natal/férias | Kit infantil Léo & Bia; um agente já está em DE |
| 5 | **C16 guia do perito judicial** (155) | ES: só cursos (Escuela Nacional de Peritos 281d, 16 cr); MX clone BR 38d; IT curso universitário 86d; nenhum kit/guia low ticket | listas de peritos judiciais por comunidade (Madrid: Agencia para la Administración Digital; designações em https://www.aparejadoresmadrid.es/documents/d/aparejadores/listas-de-peritos-judiciales-2026-y-presentacion-de-informes-via-telematica-pdf); contagem nacional: não achei (VERIFICAR) | listas anuais; sem data nova | Formato Consultora (checklist + modelos de informe) |
| 4,5 | **C4 receitas de ervas (IT, ES) e paletas (MX)** (147, 148) | ervas: PT provado (BR 174d, 20 cr), IT/ES zero; paletas: MX 44 anúncios sem vendedor de receita | — | claims de saúde: cuidado | Receitas já recorrentes |
| 4,5 | **C1 agendas/papelaria 2027 em PT, IT, FR, DE** (107, 122, 106, 128) | ES provado (Papelia 65d, Papelería Creativa 52d); resto zero | sazonal curto (2027 já em vendas) | virada de ano | Planners; baixo ticket |
| 4 | C12 sublimação (123, 137, 139), C6 moldes infantis (114), C3 elétrica (108) | sublimação MX provado (Pixelpack 96d); moldes zero em 5 países; elétrica ES 56d | — | elétrica: restrição legal de leigo em DE/IT | — |

## O que continuou VERIFICAR
1. 75 buscas que deram 429 após o SearchAPI zerar (lista em `dados-parte3/qf.json`): instalações elétricas ES/MX/IT/FR/US, segurança eletrônica (CFTV/alarme) MX/ES/IT/US/DE, cardboard IT/FR, bordado ES/IT (parcial pelo conector), ABA FR/PT/US-templates, informes psicopedagógicos, plantillas para psicólogos, therapy notes US/GB, jogos impressos (143) em 6 idiomas, estimulação cognitiva em DE/FR/PT/US/GB (pelo conector só IT e ES), São Bento IT/PL/US/ES, cabelo/curly e treino sem equipamento (132, 156), posts Canva para estética em IT/FR/DE/MX (135).
2. Idade (dias) dos vendedores de planos de marcenaria em ES-LATAM e AU (Plano Cerrado, Planos y Diseños de Herrería, Creativo Digital, Wood Atlas Plans, Woodplans): só vi anúncios recentes na amostra.
3. "ABA Tools" aparecendo em ES: confirmar se o país do anúncio é Espanha ou só LatAm.
4. Tamanho: nº de analistas do comportamento em IT/DE (ABA), nº de peritos em ES, faturamento DIY da Alemanha, população 65+ com demência em IT/DE (para C13).
5. Papelaria de casamento (111), planilha financeira (157), cifras (121), artes cristãs (137): frases exatas sem resultado; refazer com termos de vendedores reais (inspecionar páginas no Etsy/Hotmart, que o Etsy bloqueia).
6. Livro de lápis de cor (116): confirmar se o vendedor opera versões em outros idiomas/países além do BR em USD.
7. Padrão de frase exata: todos os "0 anúncios" dependem do termo escolhido; priorizar C5, C17 e C10-IT para uma segunda passada com 3 a 4 variações de termo por idioma assim que o SearchAPI renovar (08/11).

## Preços de referência (páginas abertas)
- ABA Tools PAT: US$9 básico, US$17 completo (WebFetch https://en.abatools.pro/pat).
- The Evening Stitch: US$27 (sobe para 47) (https://theeveningstitch.com/).
- Crafted Wood DIY: €27, riscado €97, 150+ projetos (https://craftedwooddiy.shop/).
- A Cor Certa (The Pencil Method): US$17, de US$47, 38 aulas, 71 pranchas (https://thepencilmethod.com/br/usd/livro-cor).
- Mapas Visuales PRO (ES): preço não aparece no HTML.
