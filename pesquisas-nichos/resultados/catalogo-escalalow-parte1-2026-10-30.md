# Catálogo EscalaLow, parte 1 (índices 0 a 52): brechas por país

Data de referência: 30/10/2026. Autor: agente de pesquisa (Claude). Status: CONCLUÍDO (com limitações listadas abaixo).

## Resumo (top 5)
1. **8,0 · Pasta HACCP + simulador de inspeção (FR, RO, CZ, SK; depois ES/PT/MX/CO)**: ninguém com 30 dias vendendo kit; um clonador (Andrei Kowalski, USD) testa a mesma tese da Consultora em 4 países há 12 dias. Reaproveita a Consultora.
2. **7,5 · Kit "facture électronique 2027" para micro/PME (FR)**: prazo oficial 01/09/2027; Amélie Boissieu vende kit contábil a 23,90 € com ~40 anúncios em 9 dias. Reaproveita o motor do Termometro/Agenda Verde.
3. **7,0 · Kit de documentos do dentista em inglês (EUA)**: Zulma Laguna com 29 dias; um BR vende kit de $27 para dentista americano há 146 dias. Reaproveita a Valigetta.
4. **6,5 · Kit Verifactu para autónomos (ES)**: mesmo operador do #2 entrou há 3 dias; prazo 01/07/2027 (VERIFICAR).
5. **6,0 · empate**: KSeF (PL, PDF anunciado há 269 dias), eletricista (IT zerada; BR testando no UK e FR) e psicopedagogo (AR, onda de 0–6 dias).

Diferença em relação à v1: a v1 não estava acessível aqui, então não dá para comparar item a item. O que mudou nesta semana é que operadores brasileiros/estrangeiros começaram a portar ofertas desta faixa (eletricista, HACCP, psicopedagogia, STL católico, Pet Comilão, planner TDAH, kit contábil) com 0 a 12 dias de anúncio.

## Avisos de ambiente (ler antes)
- A versão anterior (v1 de 29/10) e os arquivos do Desktop NÃO estavam acessíveis neste ambiente (container na nuvem). Não há comparação linha a linha com a v1; uso só as notas do usuário (`notas/*.md`).
- SearchAPI NÃO disponível (sem chave aqui e sem crédito até 08/11/2026). Toda medição de anúncios foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 menos o menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Quando não deu para consultar por página, marco "dias (busca)".
- Fonte das ofertas: `dados/escalalow-ofertas-validadas.json`, índices 0 a 52 (dias/ativos = números do EscalaLow no Brasil).
- WebFetch BLOQUEADO pela política de rede do container (todo host deu "ENOTFOUND", inclusive wikipedia.org; curl recebe 403 do proxy). Por isso NÃO consegui abrir páginas de vendas (nem as brasileiras do JSON, nem as dos concorrentes de fora). Preço/conteúdo/bumps/garantia dos concorrentes ficam VERIFICAR, salvo quando o título do anúncio ou a busca web trazem o preço. Para liberar: nas configurações do ambiente na nuvem (menu do ambiente na barra de título da sessão > Edit > Network access), ampliar o nível de acesso ou adicionar os domínios em Allowed domains (https://code.claude.com/docs/en/cloud-environments#network-access).
- Limite do conector: a consulta por `page_ids` devolve no máximo 50 anúncios, do MAIS NOVO para o mais antigo. Em página com mais de 50 anúncios ativos, o "dias" medido é um piso (marco "≥").
- O conector não devolve o texto do anúncio, só página, título do link, data de início e moeda. A moeda indica a conta do anunciante (BRL = operador brasileiro; USD = muitas vezes operador brasileiro/estrangeiro usando conta em dólar).

## 1. Ofertas da faixa, agrupadas por conceito

### 1.1 As 53 ofertas (dados do EscalaLow, Brasil)
| # | Oferta | Nicho EscalaLow | Dias BR | Anúncios BR | Preço | Domínio | Conceito |
|---|---|---|---|---|---|---|---|
| 0 | Copie e Cole na Sua Marca em Menos de 24h | Outros | 137 | 312 | R$47 | vortex-dynamiclean.lovable.app | C26 |
| 1 | Modelos STL para vender | Artesanato | 49 | 178 | – | acervodeartes.online | C11 |
| 2 | Pão de queijo lucrativo | Receitas | 131 | 167 | R$30 | receitas.revitamulher.online | C18 |
| 3 | +2000 projetos prontos (marcenaria) | Marcenaria | 79 | 165 | – | WhatsApp | C12 |
| 4 | Kit Completo de Inglês Visual (mapas mentais) | Idiomas | 109 | 117 | R$47 | mapa.fluentecomlegenda.com | C17 |
| 5 | +2000 Moldes de Costura | Artesanato | 93 | 116 | R$37 | moldecosturas.netlify.app | C13 |
| 6 | 365 Receitas sem açúcar/glúten/lactose | Receitas | 161 | 112 | R$10 | as365receitascheflu.lovable.app | C19 |
| 7 | Kit de aulas prontas de Ciências/Biologia | Educação | 56 | 110 | – | ciencias.kitaulasprontas.site | C09 |
| 8 | 10 jogos (Pegada) | Educação | 89 | 109 | R$27 | lovable.app | C10 |
| 9 | Guia Pet Comilão (comida natural p/ cães) | Pets | 58 | 94 | – | WhatsApp | C22 |
| 10 | 5.000 atividades infantis para imprimir | Educação | 91 | 85 | – | WhatsApp | C10 |
| 11 | Curso edição no CapCut | Foto e vídeo | 306 | 81 | 12x R$6,93 | edicaoviral.com.br | C15 |
| 12 | +500 Arquivos STL Católicos | Artesanato | 50 | 77 | R$10,90 | stlcatolico.vercel.app | C11 |
| 13 | Mapa Fácil da Reforma Tributária | Contábil | 91 | 77 | R$27 | materialseguro.site | C07 |
| 14 | Kit da Família Silábica | Educação | 82 | 74 | R$29,90 | lovable.app | C10 |
| 15 | Finger Foods Lucrativos | Receitas | 76 | 70 | R$10 | netlify.app | C18 |
| 16 | Receitas Saudáveis para Congelar | Receitas | 130 | 68 | R$67 | rc.patriciastenico.com.br | C19 |
| 17 | Time de naturais (consultoria fisiculturismo) | Outros | 197 | 64 | – | icarolermen.com.br | C26 |
| 18 | Treino mulher 30+ (personal) | Fitness | 49 | 63 | – | marianaeiraspersonal.com.br | C20 |
| 19 | Desafio Treino Trinca 28 dias | Fitness | 67 | 62 | – | inlead.digital | C20 |
| 20 | 150 Almoços Fitness | Receitas | 64 | 58 | R$18 | netlify.app | C19 |
| 21 | Caminho da Automação (Claude/IA) | (mal classificado) | 471 | 56 | R$10 | empresa1p.com.br | C25 |
| 22 | Baralho Vira Sílaba | Outros | 78 | 52 | R$17,90 | lovable.app | C10 |
| 23 | Kit Destrava Atendimento (psicopedagogia) | Psicopedagogia | 211 | 52 | R$37,90 | kitdestravaatendimento.com.br | C03 |
| 24 | Packs musicais (+100 mil músicas) | (mal classificado) | 482 | 51 | R$47 | packdemusicas.com.br | C16 |
| 25 | Guia Coxa e Bumbum sem agachamento | Fitness | 230 | 51 | R$39,90 | quiz.elisacandido.fit | C20 |
| 26 | Planner financeiro no WhatsApp | Finanças | 126 | 50 | R$69 | meuplannerfinanceiro.com.br | C24 |
| 27 | Receitas Sem Pensar (nutri) | Receitas | 187 | 50 | R$47 | pv.rebrugnera.com.br | C19 |
| 28 | Moldes digitais de costura em PDF | Artesanato | 364 | 50 | R$25 | moldeparacostura.com.br | C13 |
| 29 | Chutes mais altos em 14 dias (flexibilidade) | (luta) | 55 | 50 | R$47 | flexibilidade2bt.com.br | C21 |
| 30 | NutriPack: documentos para consultoria em alimentos | Nutrição | 54 | 50 | R$8 | consultoriaperfeita.com.br | C02 |
| 31 | Planner Sem Caos (TDAH) | TDAH | 176 | 45 | R$37 | semcaosplanner.online | C23 |
| 32 | Apostila de Comandos Elétricos | Elétrica | 53 | 44 | – | WhatsApp | C04 |
| 33 | +300 Dinâmicas de Arte Infantil | Educação | 75 | 43 | – | kitgramoficidad.site | C09 |
| 34 | Checklist Mentora 100K | Negócios | 66 | 43 | R$67 | talitaamarques.com.br | C08 |
| 35 | Tabela Digital do Eletricista (preço por voz) | Engenharia | 61 | 42 | – | inlead.digital | C04 |
| 36 | Planta-turbo (QGIS: planta + memorial) | Imobiliário | 159 | 42 | R$67 | universogis.com.br | C05 |
| 37 | Kit Radiestesia Completa | Terapias | 168 | 41 | R$27 | caixadoterapeuta.com | C06 |
| 38 | 300 STL nicho pet | Pets | 56 | 41 | R$29,90 | 3dpetpro.site | C11 |
| 39 | 101 Pães sem glúten / 101 receitas mexicanas | Receitas | 91 | 40 | R$10 | lovable.app | C19 |
| 40 | Biblioteca 250+ Presets (Lightroom) | Foto e vídeo | 138 | 38 | R$59,70 | hotmart.host | C15 |
| 41 | +300 Moldes Caixinha Cenário (Canva) | Artesanato | 53 | 37 | R$37 | vercel.app | C14 |
| 42 | Do Manual ao Mecanizado (endodontia) | Educação (dentista) | 119 | 36 | R$47 | endocomcafe.com | C01 |
| 43 | App com +150 receitas (nutri) | Receitas | 194 | 35 | – | pv.rebrugnera.com.br | C19 |
| 44 | Biblioteca digital (3.500 ebooks) | Outros | 88 | 35 | R$10 | lpbooks.com.br | C16 |
| 45 | 2effe Sport (simulador de uniformes) | Outros | 124 | 34 | – | 2effesportdf.com.br | C26 |
| 46 | Kit Completo de Documentos para Odontologia | Odontologia | 238 | 32 | R$67 | kit-docs-odonto.lovable.app | C01 |
| 47 | Wrestling para Jiu-Jitsu | Fitness | 99 | 32 | R$47 | wilgnersilva.com.br | C21 |
| 48 | Kit Recuperação Final / Fichas de leitura | Educação | 92 | 31 | – | WhatsApp | C10 |
| 49 | +150 Dinâmicas prontas (funcional kids) | Educação | 49 | 31 | R$17 | lovable.app | C09 |
| 50 | +600 Atividades e Experimentos de Física | Educação | 57 | 31 | R$67 | netlify.app | C09 |
| 51 | 150 receitas de drinks gourmet (copão) | Receitas | 131 | 29 | R$10 | netlify.app | C18 |
| 52 | Pack Tesouro do Serralheiro (+3.000 projetos) | Marcenaria | 130 | 29 | R$10 | lovable.app | C12 |

### 1.2 Conceitos (profissão/público, termo, termos locais pesquisados)
| Conceito | Ofertas | Profissão / público | Termo BR | Termos locais usados na Biblioteca |
|---|---|---|---|---|
| C01 Kit de documentos do dentista (+ curso de endodontia) | 46, 42 | Dentista | kit documentos odontologia | IT kit studio dentistico; ES documentos clínica dental; EN dental forms templates; DE Zahnarztpraxis Vorlagen; PT-PT documentos clínica dentária |
| C02 Documentos para consultoria em alimentos (BPF/HACCP) | 30 | Nutricionista, consultor de segurança alimentar, dono de restaurante | documentos prontos consultoria em alimentos | IT manuale HACCP; ES plan APPCC; MX NOM-251; CO/PE plan de saneamiento; PT plano HACCP; FR plan de maîtrise sanitaire; DE/PL/GR/HU/NL/TR HACCP; EN HACCP plan template |
| C03 Kit de atendimento psicopedagógico | 23 | Psicopedagogo | kit atendimento psicopedagogia | ES/AR psicopedagogía; PT-PT psicopedagogia; IT pedagogista; FR psychopédagogie |
| C04 Eletricista: tabela de preços + apostila de comandos | 35, 32 | Eletricista | tabela do eletricista; comandos elétricos | ES tabulador/precios electricista, comandos eléctricos; IT elettricista preventivo, dichiarazione di conformità; FR devis électricien; EN electrician price guide/EICR; PL elektryk cennik; DE Elektriker |
| C05 Planta e memorial no QGIS | 36 | Topógrafo/agrimensor, regularização de imóveis | QGIS planta memorial | QGIS (todos); ES GML catastro; IT geometra catasto |
| C06 Gráficos de radiestesia | 37 | Terapeuta holístico | radiestesia | ES radiestesia gráficos; IT radiestesia; FR radiesthésie; DE Pendeltafeln; PL radiestezja |
| C07 Mapa da reforma tributária | 13 | Contador, empresário | reforma tributária | FR facturation électronique; PL KSeF; ES Verifactu; DE E-Rechnung; BE e-facturation |
| C08 Kit/checklist para mentoras | 34 | Mentores, infoprodutores | checklist mentoria | ES plantillas mentoría |
| C09 Aulas prontas por disciplina (ciências, física, arte, ed. física) | 7, 50, 33, 49 | Professores especialistas | aulas prontas, experimentos, dinâmicas | ES situaciones de aprendizaje, planeaciones, experimentos de física; IT esperimenti fisica; FR fiches; PL scenariusze |
| C10 Alfabetização e atividades infantis | 8, 10, 14, 22, 48 | Pais, professores de ed. infantil/anos iniciais | família silábica, atividades para imprimir | ES familias silábicas, actividades para imprimir; IT sillabe; FR syllabes; PT-PT famílias silábicas; PL sylaby; EN phonics |
| C11 Arquivos STL para impressão 3D | 1, 12, 38 | Maker 3D que revende peças | arquivos STL | ES archivos STL; IT file STL; FR fichiers STL; DE STL Dateien; EN STL files |
| C12 Projetos de marcenaria/serralheria | 3, 52 | Marceneiro, serralheiro | projetos prontos | ES planos carpintería, proyectos herrería; IT progetti falegnameria; FR plans menuiserie; EN woodworking plans |
| C13 Moldes de costura PDF | 5, 28 | Costureira | moldes de costura | ES moldes de costura; IT cartamodelli; FR patrons de couture; DE Schnittmuster; PL wykroje |
| C14 Moldes de caixinha cenário (festa) | 41 | Artesã de festa | caixinha cenário | ES cajitas personalizadas moldes |
| C15 Presets e edição de vídeo | 40, 11 | Fotógrafos, criadores | presets, CapCut | presets lightroom; curso capcut |
| C16 Acervos (músicas, ebooks) | 24, 44 | Consumidor/DJ | packs, biblioteca digital | ES biblioteca digital ebooks; packs de música |
| C17 Inglês visual com mapas mentais | 4 | Estudante de inglês | mapas mentais inglês | ES inglés mapas mentales; IT inglese mappe |
| C18 Receitas para vender (renda extra) | 2, 15, 51 | Renda extra / confeitaria | receitas lucrativas | ES recetas para vender, micheladas para vender |
| C19 Receitas saudáveis/restritivas | 6, 16, 20, 27, 39, 43 | Consumidor | receitas sem glúten/lactose/açúcar | ES recetas sin gluten; IT ricette senza glutine; FR recettes sans gluten |
| C20 Treino feminino | 18, 19, 25 | Mulheres | treino glúteos, desafio | ES rutina glúteos, reto 28 días |
| C21 Artes marciais (flexibilidade, wrestling) | 29, 47 | Praticantes de luta | chutes, wrestling jiu-jitsu | ES flexibilidad patadas; lucha jiu jitsu |
| C22 Comida natural para cães | 9 | Tutor de cão | comida natural | ES comida natural perros; IT dieta casalinga cane; FR ration ménagère; DE BARF |
| C23 Planner TDAH adulto | 31 | Adulto com TDAH | planner TDAH | ES planner TDAH; FR planner TDAH; EN ADHD planner |
| C24 Planner financeiro via WhatsApp | 26 | Consumidor | controle financeiro | (SaaS, fora do modelo) |
| C25 Curso de IA (Claude) | 21 | Profissionais | automação com Claude | (fora do modelo) |
| C26 Fora do modelo ou indefinido | 0, 17, 45 | – | – | 0 = VERIFICAR (página fora do ar para mim); 17 = consultoria de fisiculturismo; 45 = e-commerce de uniformes |

## 2. Resultado por país, por conceito
Legenda: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; BRECHA = ninguém vende; PRAZO = gancho com data de norma. "d" = dias reais medidos por page_id (30/10/2026 menos o anúncio ativo mais antigo).

### C02 Documentos para consultoria em alimentos / HACCP (oferta 30, NutriPack R$8)
| País / idioma | Termo | Quem vende (página, moeda, dias, anúncios) | Leitura |
|---|---|---|---|
| IT | manuale HACCP | Só serviço/SaaS: HACCP Smart - JPvision (EUR, ≥164d), NORMA HACCP (EUR, ≥125d, "chi controlla i tuoi registri HACCP?"), Facile Sicurezza (servizio), Biorsaf, Chemichal (gestionale HaccpOK). Info-produto: Sb food consulting "Il manuale per chi guida un locale" (EUR, ~16d); Studio Facile "La cucina professionale, spiegata con i disegni" (USD, 1d) | BRECHA de kit de documentos (só consultoria cara e app). Concorrência de ebook chegando agora |
| ES | plan APPCC | Trazabilidad Express "Obrador listo para Sanidad" (EUR, 3 anúncios, ~2d); resto é curso grátis (Foro de Formación, talentodigital) | TESTE (1 vendedor novo) |
| PT | plano HACCP / HACCP | Novelty Nook "Guia de Formação HACCP para Cantinas Escolares" (USD, 4 anúncios, ~1–2d); Studio Facile "O HACCP explicado com desenhos" (USD, 1d); thequalitycollege (BRL) | TESTE (só operadores estrangeiros novos) |
| FR / BE | plan de maîtrise sanitaire | Andrei Kowalski "L'inspecteur de la DDPP est à la porte" (USD, 1d no FR); ePackPro (SaaS HACCP, EUR); JDC "Plan d'Hygiène Digitalisé" (EUR) | TESTE |
| RO / CZ / SK | (página Andrei Kowalski) | Andrei Kowalski (USD, ~17 anúncios, anúncio mais antigo ~12d em 18/10): "Dosar de igienă pentru cafenea și bistro", "Mâine vine controlul DSVSA", "Kde máte zložku HACCP?", "Co přesně chce hygiena vidět?" | TESTE com operador multi-país: mesma tese da Consultora (pasta para a inspeção) em RO, CZ, SK e FR |
| PL / GR / TR | HACCP | Studio Facile "HACCP w obrazkach", "Το HACCP, με εικόνες", "Gıda hijyeni, resimlerle" (USD, 1d) | TESTE (ebook ilustrado, não kit) |
| HU | HACCP | AHACCP.ai "Rendelj professzionális HACCP-t" e Sattva Guidance "HACCP készítés egyszerűen" (HUF, ~0–1d) | TESTE local (serviço/IA) |
| DE / AT / NL | HACCP | Só escolas (§4 LMHV Schulung), SaaS (Apprendo Horeca NL) | BRECHA (sem kit) |
| MX | NOM-251 | Instituto Enso "Curso Anti Clausura NOM-251" (MXN, curso), consultorias, fumigação | BRECHA de kit (há curso "anti clausura" = mesmo gancho de medo da inspeção) |
| CO / PE / CL / AR / EC | plan de saneamiento | C & A. I "PLAN DE SANEAMIENTO A TU ALCANCE" (COP, ~5d); Valéria Moura Gestión de Procesos y Calidad (BRL, operador BR em espanhol: "Los 68 documentos del combo", "El HACCP no es solo para el auditor", "¿Dónde está el registro de cloro?", kits de 39/90/118 arquivos, todos de 29/10); FoodConsulting (PEN, serviço) | TESTE: um operador BR acabou de portar o kit de qualidade/HACCP para o espanhol |
| EN (GB/IE/AU/US) | HACCP plan template; food safety folder | Nada relevante (a busca em inglês devolve ruído) | VERIFICAR com termo melhor (ex.: "SFBB pack", "food safety management system template") |

Resumo C02: ninguém com 30+ dias vendendo KIT de documentos HACCP/BPF de baixo valor em nenhum país pesquisado; o que dura é serviço/SaaS. Mas há uma onda de testes de 1 a 12 dias (Andrei Kowalski em RO/CZ/SK/FR; Studio Facile em 6 idiomas; Valéria Moura em ES-LATAM; Novelty Nook em PT). Conclusão: BRECHA que está sendo descoberta AGORA; a Consultora traduzida precisa entrar em semanas, não meses. Re-checar a página de Andrei Kowalski em 15/11 (se passar de 30d, vira prova).

### C03 Kit de atendimento psicopedagógico (oferta 23, R$37,90, 211d no BR)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| AR (voseo) | psicopedagogas; evaluación psicopedagógica | Evaluá Psicope (USD, 5 anúncios, ~3,5d): "100 pruebas listas para aplicar", "El informe para la escuela, ya redactado"; Formacionpsicopeok (ARS, ~5,6d, curso "Comprender matemática"); Consultorio en Orden (USD, 9 anúncios, ~0,8d: "21 plantillas en 8 módulos", "7 días de garantía"); Camila Rodriguez (BRL, "Kit Psicopedagógico Editable", ~0,8d); resto = consultórios | TESTE (onda de 0–6 dias; nenhum com 30d) |
| CL / PE / MX / CO / EC / BO | idem | Só centros de atendimento (serviço) e mestrado (TECH, EUR) | BRECHA |
| ES | idem | TECH "Máster en Psicopedagogía" (EUR) | BRECHA (profissão = orientador/psicopedagogo escolar; VERIFICAR demanda) |
| IT | pedagogista | ~225 anúncios, todos de pedagogistas vendendo serviço a pais (consulenze, masterclass); nenhum kit para o profissional | BRECHA (profissão ganhou Ordem própria: Lei 55/2024, VERIFICAR prazos de inscrição) |
| PT / FR | – | Psicopedagogia não é profissão estruturada nesses países | Não se aplica |

Resumo C03: Argentina é o lugar (psicopedagogia é carreira universitária forte lá), e 3–4 vendedores começaram nesta semana. TESTE rápido em AR (ARS, voseo) ou esperar 15/11 para ver quem sobrevive.

### C04 Eletricista: tabela de preços digital (35) + apostila de comandos elétricos (32)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| ES-LATAM (neutro) | precios electricista; comandos eléctricos | Tu Rincon Digital (USD, ~20 anúncios, ~0,8d): "Saber qué hacer y cuánto cobrar", "¿Cuánto se cobra un ventilador?", "Aprende electricidad desde cero", também albañil/plomero; Recursos digitales (USD, "+1300 descargas", ~2,6d). "comandos eléctricos" devolve ruído | TESTE (espanhol neutro, não prova país) |
| FR | électriciens devis | Acelera Negócios (BRL, 4 anúncios, ~0,5–1d): "Vos devis professionnels par la voix", "Signez le chantier avant de repartir", "Sécurisez l'acompte" = PORTE DIRETO da Tabela Digital do Eletricista (orçamento por voz) para artesãos franceses; SaaS (One Flow, izi Touch) | TESTE (operador BR acabou de entrar) |
| UK | EICR certificate electricians | Markus Schneider (BRL, 4 anúncios, ~8d desde 22/10): "+200 Visual Cards for UK Electricians" = porte da apostila/cards; Tradecert (GBP, app de certificados, ~34d) | TESTE (BR) + SaaS provado |
| IT | prezzario elettricista | 0 anúncios | BRECHA (VERIFICAR com "dichiarazione di conformità", "DiCo") |
| PT / DE / PL | – | não pesquisado por falta de cota; VERIFICAR | – |

Resumo C04: operadores brasileiros estão portando AGORA os dois produtos de eletricista (cards visuais no Reino Unido, orçamento por voz na França, tabela de preços em espanhol). Ninguém com 30 dias. Itália zerada.

### C05 Planta e memorial no QGIS (36, R$67, 159d no BR)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| ES/LATAM/PT/IT/FR | QGIS | Só escolas e cursos (Ingenium PE, Resolución de Exámenes, Ing. Luis Achamizo); nenhuma automação/plugin de planta+memorial à venda | BRECHA, mas o produto BR depende de regra brasileira (REURB, memorial descritivo INCRA/cartório). Porte exige estudo de cadastro de cada país (ES: GML do Catastro, Lei 13/2015; IT: geometri e DOCFA/PREGEO) = VERIFICAR |
| PE | (achado lateral) | Ing. Jorge Hurtado (PEN, ~120 anúncios, ~3–5d nos 50 mais novos): packs de S/18 para engenheiros (Formatos SST para obras, Pack ITSE, Puesta a tierra SPAT, Diagnóstico eléctrico, Expedientes de verificación catastral Perú 2026, Norma E.030) | TESTE: "pack de documentos por S/18" para engenharia no Peru, com muitos criativos |

### C06 Gráficos de radiestesia (37, R$27, 168d no BR)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| ES-LATAM / ES | radiestesia | ~626 anúncios ativos (muitos consultórios e cursos). Info-produtos: Radiestesia Terapéutica (BRL, 5 anúncios, ~0,4d, "Desafío Terapeuta de ti misma"); Regarte (USD, voseo AR, "Aprendé a usar tu péndulo en 7 días", ~1,6d); Terapias de Luz (USD, operador BR multi-curso) | TESTE (todos novos; BR entrando em espanhol) |
| PT | radiestesia | Espaço Mannah (BRL, PT-BR) | sem prova PT-PT |
| IT / FR / DE / PL | – | não pesquisado (cota); FR "radiesthésie" e DE "Pendeltafeln" ficam VERIFICAR | – |

### C07 Mapa da reforma tributária (13, R$27) → kits de obrigação fiscal com prazo lá fora
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| FR | facturation électronique 2027 | Amélie Boissieu (USD, ~40 anúncios, mais antigo ~9d em 21/10): "Kit Comptable Pratique 2027 · 7 cahiers + 6 bonus à 23,90 €"; Isula Solutions "Factures PDF interdites en 2027 : êtes-vous prêt ?" (EUR, ~10d, serviço); CMAs (câmaras de ofícios) fazendo campanha "Préparez votre entreprise à 2027"; SaaS (Abby, OmniFacture) | TESTE forte + PRAZO (01/09/2027) |
| ES | Verifactu autónomos | Kit Contable Práctico (USD, mesmo operador da Amélie, ~12 anúncios, ~3d): "7 cuadernos + 6 bonos por 23,90 €"; SaaS de faturação Verifactu (Quantax, ZIOBE 9,95 €/mês, VoFactu "facturas por voz") | TESTE + PRAZO (Verifactu 2027, VERIFICAR datas) |
| PL | KSeF poradnik | Porady dla JDG "Poradnik (PDF): KSeF" (PLN, anúncio ativo há ~269 dias); Scanye (PLN, SaaS, e-book grátis) | PROVADO de demanda por guia PDF de KSeF para JDG (VERIFICAR se é pago ou isca) |
| BR → fora | – | O operador "Amélie Boissieu / Kit Contable Práctico" (conta em USD) replica em FR e ES o modelo "kit contábil" a €23,90 | Concorrente a monitorar |

Resumo C07: o "mapa da reforma" brasileiro não se traduz, mas o MODELO (kit/mapa de obrigação fiscal com data) tem prazo real em FR (emissão de e-fatura para PME/micro em 01/09/2027) e ES (Verifactu), e um vendedor estrangeiro escalando rápido na França.

### C01 Kit de documentos do dentista (46, R$67, 238d) + curso de endodontia (42)
Dentista já foi pesquisado a fundo em 28–29/10 (ver `notas/fila-ofertas.md` e `notas/pesquisa-europa.md`): IT provado (Kit Studio Blindato, BR, €19,99, 30+ dias), Colômbia GO, México #2, Romênia/Sérvia/Moldávia com operador BR clonando, Europa sem prova. Aqui só re-chequei o mercado em inglês.
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| US/UK/AU/CA | dental kit Canva | Lic. Zulma Laguna (USD): "Get Your Dental Clinic Inspection-Ready in 1 Hour" ativo desde 01/10 (~29d hoje; vira 30d em 31/10) + 4 criativos novos de 26/10 ("Dental Docs, Done for You", "Dental Protocols, Already Written", "Not a Blank Template"); Dental Master Pro Max (BRL, operador BR) "Get More Dental Patients For Just $27" ativo há ~146d; Karbonna (BRL, sem título, anúncios de ~95d, produto VERIFICAR); Dental Marketing Vault "Halloween Dental Kit — $1" | EUA: kit de MARKETING para dentista PROVADO (146d, $27, BR); kit de DOCUMENTOS a 1 dia de virar provado (Zulma). Re-checar Zulma em 31/10–05/11 como já previsto |
| Endodontia (42) | – | Curso BR de técnica; não é kit de documentos. Não portado por falta de cota | VERIFICAR (baixa prioridade) |

### C09 Aulas prontas por disciplina (7 ciências, 50 física, 33 arte, 49 dinâmicas)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| IT | schede didattiche da stampare | Prof di Scienze (USD) "120 Schede di Scienze Pronte all'Uso" (~0,8d, porte do kit de Ciências 7); Attivita Premium (USD) "2.500 schede così, a 7,90 €" (~3d); Mondo Infanzia Didattica (USD) "Oltre 1.000 Attività per la Scuola dell'Infanzia" (~8,6d); Edudoro.eu (PLN, ~58d); L'angolo del Docente (EUR, loja local, anúncio de ~208d) | TESTE de BR + loja local PROVADA (L'angolo del Docente). Preço de referência IT: €7,90 |
| FR / BE / CA | fiches à imprimer maternelle | Tiny Inventors (USD) "275 activités de maths à imprimer" (~0,7d); Alejandra Casas (USD) "+500 activités pour la maternelle — 5 € aujourd'hui" (~0,7d) | TESTE (BR/LATAM entrando; preço €5) |
| ES-LATAM | psicopedagogas (achado lateral) | Valentina Morales (BRL) "+500 páginas de dinámicas… clases de música" (porte das dinâmicas 33/49 para professor de música) | TESTE |
| ES / MX / PL | situaciones de aprendizaje, planeaciones, scenariusze | não pesquisado (cota); MX planeaciones é sabidamente saturado; VERIFICAR | – |

### C10 Alfabetização e atividades infantis (8, 10, 14, 22, 48)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| ES-LATAM | familias silábicas | ~106 anúncios; Aula pedagogicaa (BRL) com 30+ anúncios novos "¡50 Actividades de Alfabetización con Sílabas Simples listas para imprimir!" (~0,4d). A busca devolve só os mais novos; não achei vendedor com 30+ dias nesta amostra (VERIFICAR) | SATURANDO de operadores BR (espanhol neutro não prova país) |
| IT | sillabe / schede | Attivita Premium "Dalle sillabe semplici alle complesse", "Dalla lettera alla parola" (USD, ~3d) | TESTE |
| FR | maternelle | ver C09 (Alejandra Casas €5) | TESTE |
| PT-PT / PL / RO / EN | – | não pesquisado (cota) | VERIFICAR |

### C11 Arquivos STL (1, 12, 38)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| ES-LATAM | archivos STL | ~744 anúncios; Marcos Santiny (USD) "Gana Dinero con la Impresión 3D en el Nicho Católico" (15+ anúncios de hoje = porte direto do 12 "STL Católicos") | TESTE com muita concorrência; nicho de consumidor/maker, fora do modelo profissão+documento |
| IT/FR/DE/EN | – | não pesquisado (cota) | VERIFICAR |

### C12 Projetos de marcenaria e serralheria (3, 52)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| MX | proyectos de herrería | Planos y Diseños de Herrería (MXN, vendedor local, 7 anúncios, mais antigo ~13d): "MEGA PACK DE PLANOS HERRERIA Y CARPINTERIA"; muito e-commerce de ferramenta no meio | TESTE local (moeda local = demanda real) |
| PE / BO / AR / CO | planos de carpintería | CursoNet (USD) "15.000 planos de muebles por solo S/3" (~16d); Melamina Desing 2026 (BOB) "Dos oficios por 49 Bs"; Plano cerrado (USD) "100+ planos de carpintería"; Elias Joel (ARS) "Curso Melamina Pro 360 PDF"; Carlos Mendoza (COP) | Mercado ativo e barato (S/3 a 49 Bs); ninguém com 30d na amostra |
| EN US | woodworking plans | não pesquisado (cota); o "Ted's Woodworking" é clássico antigo dos EUA (VERIFICAR) | – |

### C13 Moldes de costura (5, 28)
| País / idioma | Termo | Quem vende | Leitura |
|---|---|---|---|
| IT | cartamodelli PDF | Tu Evolución Activa (USD, ~8,5d, 8+ anúncios); NOVA HOUSE (USD) "Cartamodelli precisi al millimetro" (~7,6d); Sartoria a 4 Zampe (USD, moldes de roupa para pet, ~4,9d); Il Mio Quaderno di Cucito (USD, ~2,7d); Studio Facile | TESTE (só operadores em USD, todos <9d) |
| ES-LATAM | moldes de costura PDF | consulta barrada por limite do conector (Too Many Requests) | VERIFICAR |
| FR / DE / PL | patrons de couture, Schnittmuster, wykroje | não pesquisado (cota) | VERIFICAR |

### C14 a C26 (consumidor final, cursos, SaaS e fora do modelo): leitura rápida
| Conceito | Ofertas | O que achei lá fora | Leitura |
|---|---|---|---|
| C14 Caixinha cenário | 41 | não pesquisado (cota). Parecido: agente irmão (parte 3) achou "Bordados en Papel" (USD) com a MESMA copy do BR em espanhol, ~1d | VERIFICAR |
| C15 Presets / CapCut | 40, 11 | não pesquisado; mercado global saturado (Lightroom presets) | Fora do modelo |
| C16 Acervos (músicas, ebooks) | 24, 44 | não pesquisado; risco de direito autoral (100 mil músicas, 3.500 ebooks por R$10) | Não portar |
| C17 Inglês com mapas mentais | 4 | ver relatório irmão `mapas-mentais-por-pais-v2-2026-10-30.md` (Polônia: "Matura 2027 notatki PDF" PROVADO, PLN, 175 anúncios) | Ver irmão |
| C18 Receitas para vender | 2, 15, 51 | Relatório irmão (parte 3): "recetas de bolis gourmet para vender" PROVADO em espanhol (Máster Class Online, COP, ~79d; Rincón Artesanal, USD, ~61d) | PROVADO em ES-LATAM (renda extra), fora do modelo profissão |
| C19 Receitas saudáveis/restritivas | 6, 16, 20, 27, 39, 43 | IT "ricette senza glutine senza lattosio": AirChef (USD) "Keto 365 — ricettario Bimby" (~1,7d, 10+ anúncios), Alessia Romano (USD, ~1,7d), La Mia Cocina Sana (BRL) | TESTE de operadores BR em massa; consumidor |
| C20 Treino feminino | 18, 19, 25 | não pesquisado (cota); ver `fitness-nutricao-fisio-v2.md` | VERIFICAR |
| C21 Artes marciais | 29, 47 | não pesquisado (cota) | VERIFICAR |
| C22 Comida natural para cães | 9 | ES-LATAM: Pet Comilón (BRL, ~2,8d) = porte direto do "Guia Pet Comilão" (9); Impulso E-books (ARS) "¿Sabés qué come realmente tu perro?" (~0,4d); Alimentacion BARF (USD) | TESTE (BR clonando em espanhol) |
| C23 Planner TDAH | 31 | ES: Mente Inquieta (EUR, "La agenda hecha para tu cerebro", ~0,4d); Semana em Vista (BRL, "El planner para la mente TDAH", ~1d); Agenda sin Caos TDAH (USD, ~7,6d, clone do 31); FR: Lumi Editions (USD) "Le planner pour les cerveaux qui s'éparpillent" (~8,8d); o próprio Planner Sem Caos (BRL) com anúncios de ~14d nessa busca | TESTE (o vendedor BR e clones já saíram para ES/FR) |
| C24 Planner financeiro via WhatsApp | 26 | SaaS | Fora do modelo |
| C25 Curso de IA (Claude) | 21 | ES: "Academia Claude AI ES" (USD) apareceu na busca de QGIS | Fora do modelo |
| C26 Fora do modelo | 0, 17, 45 | 0 = produto não identificado (WebFetch bloqueado); 17 = consultoria; 45 = e-commerce | VERIFICAR o 0 |

### Achados laterais que reforçam o quadro
- Caixa do Terapeuta (vendedor da oferta 37, radiestesia) já roda em Portugal: 141 anúncios no PT, ≥23 dias (relatório irmão `novos-nichos-europa-v2-2026-10-30.md`). Vira PROVADO PT-PT por volta de 07/11 se continuar.
- Jogos Terapêuticos (BRL) vende "Plus de 50 activités psychopédagogiques · dès 5 €" na França há ~19 dias, 123 anúncios na página (relatório irmão `educacao-inclusao-v2.md`): psicopedagogia em francês é TESTE com operador BR.
- Marcenaria em inglês está saturada, inclusive por brasileiros (Weekend Woodshop, BRL, "16,000+ plans") (relatório irmão `catalogo-escalalow-parte3`).

## 3. Aprofundamento das brechas fortes (página de vendas, tamanho da profissão, gancho legal)
Limitação: com o WebFetch bloqueado e a cota de busca web esgotada (limite de 200 buscas por turno, compartilhado entre agentes, atingido no meio desta pesquisa), não abri nenhuma página de vendas e confirmei por fonte oficial só a data francesa. O resto vai como VERIFICAR, com a norma citada para conferência.

### 3.1 C02 → "Consultora" (simulador de inspeção sanitária + pasta HACCP) em FR, RO, CZ, SK, ES, PT, MX, CO
- O que vende lá fora: Andrei Kowalski (page 1340912605769671, conta USD, 17 anúncios, mais antigo 18/10 = ~12 dias) vende exatamente a tese da Consultora: "pasta pronta para a inspeção" de café/bistrô, com ganchos de medo ("L'inspecteur de la DDPP est à la porte", "Mâine vine controlul DSVSA", "Kde máte zložku HACCP?"). Preço, plataforma, bumps e garantia: VERIFICAR (página não abriu).
- Concorrentes que acabaram de entrar: Valéria Moura (BRL, ES-LATAM, combo HACCP 68 documentos, 29/10); Studio Facile (USD, e-book "HACCP com desenhos" em 6 idiomas, 29/10); Novelty Nook (PT, cantinas escolares); Trazabilidad Express (ES, obradores); AHACCP.ai/Sattva (HU).
- O que dura há meses é serviço/software (HACCP Smart IT ≥164d; NORMA HACCP IT ≥125d; Facile Sicurezza IT 644d segundo o irmão `novos-nichos-europa-v2`), ou seja, o dono de restaurante PAGA para resolver isso; falta a versão barata.
- Gancho legal (VERIFICAR texto e URL oficial): na UE, o Regulamento (CE) 852/2004, art. 5, obriga todo operador do setor alimentar a manter procedimentos baseados nos princípios HACCP; fiscalização nacional (FR DDPP; RO DSVSA/ANSVSA; CZ KHS; SK RÚVZ; ES Sanidad autonómica; PT ASAE). México: NOM-251-SSA1-2009 (práticas de higiene) e o medo da "clausura" (há curso "Anti Clausura NOM-251" anunciando). Colômbia: Res. 2674/2013 (BPM, plano de saneamento).
- Tamanho de mercado: VERIFICAR (número de restaurantes/cafés por país).
- Leitura: BRECHA real (sem vendedor de kit com 30 dias), mas em corrida: um clonador já testa 4 países há 12 dias. Se Kowalski chegar a 30 dias (≈17/11), vira prova de compra em RO/CZ/SK/FR.

### 3.2 C07 → kit/app "faturação eletrônica 2027" para micro e pequenas (FR, ES, PL, DE)
- FR (PRAZO confirmado em fonte oficial): emissão de fatura eletrônica obrigatória para PME, TPE e microempresas a partir de 01/09/2027; recepção obrigatória para todas desde 01/09/2026 (impots.gouv.fr, página "À partir de quand suis-je concerné par la réforme de la facturation électronique ?": https://impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation ; base: LF 2024 art. 91 e LF 2026 art. 123, segundo La Poste: https://www.laposte.fr/entreprise-collectivites/actualites/calendrier-dematerialisation-factures-en-est-votre-entreprise). Multa de €50 por fatura (art. 1737 CGI) segundo o irmão `prazos-de-norma`: VERIFICAR. Se micro-empresário em "franchise en base de TVA" também emite: VERIFICAR.
- Quem vende: Amélie Boissieu (page 1363004406903385, USD, ~40 anúncios em 9 dias) "Kit Comptable Pratique 2027 · 7 cahiers + 6 bonus à 23,90 €"; o mesmo operador abriu "Kit Contable Práctico" na Espanha há ~3 dias (12 anúncios, 23,90 €). Câmaras de ofícios (CMA) e consultorias fazem campanha "Factures PDF interdites en 2027". Ritmo de criativos = teste que está dando certo (VERIFICAR conteúdo e funil).
- ES: Verifactu (RDL 15/2025: sociedades 01/01/2027; autónomos 01/07/2027, segundo o irmão `prazos-de-norma`; VERIFICAR no BOE). Concorrência = SaaS barato (ZIOBE 9,95 €/mês, Quantax grátis) + o kit de 23,90 €.
- PL: KSeF para micro (≤10 mil zł/mês) a partir de 01/01/2027 (irmão `prazos-de-norma`; VERIFICAR). "Porady dla JDG" anuncia "Poradnik (PDF): KSeF" há ~269 dias (PLN) = demanda contínua por guia em PDF (VERIFICAR se é pago).
- DE: E-Rechnung, emissão obrigatória 01/01/2027 para faturamento > €800 mil e para todos em 01/01/2028 (irmão `prazos-de-norma`); não pesquisei vendedor.
- Reaproveitamento: o motor do Termometro 85k / Agenda Verde (calculadora + calendário + checklist) vira "Kit Facture Électronique 2027" (FR) e "Kit Verifactu autónomos" (ES) com app de checklist e modelos.

### 3.3 C01 → dentista em inglês (EUA)
- Lic. Zulma Laguna (page 778739435326228, USD): "Get Your Dental Clinic Inspection-Ready in 1 Hour" ativo desde 01/10 (~29 dias; vira PROVADO em 31/10 se continuar), mais 4 criativos de 26–27/10 ("Dental Docs, Done for You", "Dental Protocols, Already Written"). Nota anterior do usuário: "Dental Kit in Free Canva $27".
- Dental Master Pro Max (page 1170940042761217, conta BRL) "Get More Dental Patients For Just $27": anúncio ativo há ~146 dias = PROVADO de que dentista americano compra kit de $27 de operador brasileiro (é kit de marketing, não de documentos; conteúdo VERIFICAR).
- Reaproveitamento: Valigetta (kit + app) em inglês, com gancho de inspeção (OSHA/estado; VERIFICAR norma).

### 3.4 C04 → eletricista (UK, FR, IT, ES)
- UK: Markus Schneider (BRL) "+200 Visual Cards for UK Electricians" (~8 dias); Tradecert (app, ~34 dias). Gancho (VERIFICAR): Electrical Safety Standards in the Private Rented Sector (England) Regulations 2020 = EICR a cada 5 anos em imóvel alugado.
- FR: Acelera Negócios (BRL) "Vos devis professionnels par la voix" = porte da Tabela Digital do Eletricista (35), ~1 dia.
- IT: zero anúncio para "prezzario elettricista". Gancho (VERIFICAR): DM 37/2008, dichiarazione di conformità obrigatória ao fim de cada instalação.
- ES-LATAM: Tu Rincon Digital (USD) "¿Cuánto se cobra…?" multi-ofício, ~1 dia.
- Leitura: TESTE em 3 países com operadores BR; Itália é a brecha limpa.

### 3.5 C03 → psicopedagogia na Argentina (e França)
- AR: Evaluá Psicope (USD, voseo, "100 pruebas listas para aplicar", "El informe para la escuela, ya redactado", ~3,5d), Consultorio en Orden (USD, "21 plantillas en 8 módulos", "7 días de garantía", ~0,8d), Camila Rodriguez (BRL, "Kit Psicopedagógico Editable"), Formacionpsicopeok (ARS, curso).
- FR: Jogos Terapêuticos (BRL) "activités psychopédagogiques dès 5 €" (~19d, irmão).
- Tamanho da profissão na Argentina: VERIFICAR (cota de busca esgotada).
- Reaproveitamento: estrutura do Maletín del Psicólogo (MX) para "Maletín del Psicopedagogo" AR (informe escolar, anamnese, consentimentos, app de sessões).

## 4. Ranking das brechas (0 a 10) e reaproveitamento
Critério: régua do usuário (PROVADO / TESTE / PRAZO / BRECHA), aderência ao modelo "kit de documentos + app por profissão", reaproveitamento do que já existe e velocidade da concorrência.

| # | Brecha (país) | Conceito / ofertas | Status | Nota | Reaproveita | Por quê |
|---|---|---|---|---|---|---|
| 1 | Pasta HACCP + simulador de inspeção (FR, RO, CZ, SK; depois ES, PT, MX, CO) | C02 / 30 | BRECHA virando TESTE (Kowalski 12d) | 8,0 | Consultora + app de inspeção | Obrigação legal em toda a UE, medo de fiscalização, só serviço caro dura; clonador já testando = entrar já |
| 2 | Kit "facture électronique 2027" para micro e PME (FR) | C07 / 13 | PRAZO 01/09/2027 + TESTE (Amélie Boissieu, 23,90 €, ~40 anúncios em 9d) | 7,5 | Motor Termometro 85k / Agenda Verde | Data oficial, público enorme, concorrente estrangeiro escalando rápido |
| 3 | Kit de documentos do dentista em inglês (EUA) | C01 / 46 | Quase PROVADO (Zulma 29d) + PROVADO de kit $27 de marketing (146d) | 7,0 | Valigetta | Já estava na fila; confirmar 31/10–05/11 |
| 4 | Kit Verifactu para autónomos (ES) | C07 / 13 | PRAZO 01/07/2027 (VERIFICAR) + TESTE (Kit Contable Práctico ~3d) | 6,5 | Motor Termometro / Agenda Verde | Mesmo produto do #2, segundo idioma |
| 5 | Guia/kit KSeF para JDG (PL) | C07 / 13 | PROVADO de demanda (PDF há ~269d) + PRAZO 01/01/2027 | 6,0 | Motor Termometro | Polonês, PLN/BLIK e fatura são barreira (mesmo bloqueio já anotado para a Polônia) |
| 6 | Kit do eletricista (IT; depois UK e FR) | C04 / 35, 32 | BRECHA na IT; TESTE BR no UK (8d) e FR (1d) | 6,0 | App de checklist/inspeção (Consultora) + tabela de preço por voz | DiCo (DM 37/08) e EICR são documentos obrigatórios (VERIFICAR) |
| 7 | Maletín del Psicopedagogo (AR) | C03 / 23 | TESTE (3–4 vendedores de 0–6 dias) | 6,0 | Maletín del Psicólogo | Carreira forte na AR; risco de câmbio/checkout ARS |
| 8 | Schede/aulas prontas para professor (IT: scienze, sostegno, infanzia) | C09 / 7, 50, 33, 49 | Loja local PROVADA (L'angolo del Docente ~208d) + TESTE BR a €7,90 | 5,5 | – | Professor italiano compra; preço baixo; concorrência BR chegando |
| 9 | Catálogo de projetos para herrero/serralheiro cotar (MX) | C12 / 52, 3 | TESTE local (13d, MXN) | 5,0 | – | Ângulo profissional (cotar no WhatsApp); hobby já saturado |
| 10 | Radiestesia para terapeuta (PT-PT, ES) | C06 / 37 | Quase PROVADO no PT (Caixa do Terapeuta ≥23d, 141 anúncios) | 5,0 | – | O próprio vendedor BR já está lá; nicho místico |
| 11 | Planner TDAH (ES, FR) | C23 / 31 | TESTE (vários clones, inclusive EUR nativo) | 4,0 | – | Consumidor, muitos clones |
| 12 | Comida natural para cães (ES-LATAM) | C22 / 9 | TESTE (clone BR 3d) | 4,0 | – | Consumidor |
| 13 | Receitas para vender (ES-LATAM) | C18 / 2, 15, 51 | PROVADO (irmão: bolis 79d) | 4,0 | – | Funciona, mas fora do modelo profissão |
| 14 | Moldes de costura (IT) | C13 / 5, 28 | TESTE (só USD, <9d) | 3,5 | – | Consumidor |
| 15 | Alfabetização / atividades infantis (ES, IT, FR) | C10 / 8, 10, 14, 22, 48 | SATURANDO de BR | 3,0 | – | Oceano vermelho em espanhol |
| 16 | STL 3D (ES) | C11 / 1, 12, 38 | TESTE com 744 anúncios no termo | 3,0 | – | Consumidor/maker |
| 17 | Receitas restritivas (IT) | C19 | TESTE em massa BR | 3,0 | – | Consumidor |
| 18 | QGIS planta + memorial (ES/IT) | C05 / 36 | BRECHA, mas produto depende de regra BR | 3,0 | – | Exige refazer para cadastro de cada país |
| – | C14, C15, C16, C17, C20, C21, C24, C25, C26 | – | não pesquisado ou fora do modelo | ≤3 | – | ver seção 2 |

### Reaproveitamento em uma linha
- App de inspeção / Consultora → #1 (HACCP em 8 países) e #6 (checklist do eletricista: DiCo/EICR).
- Valigetta → #3 (EUA, inglês) e já na fila para CO/ES/RO.
- Motor Termometro 85k / Agenda Verde → #2, #4, #5 (calendário de obrigação + calculadora + checklist de faturação eletrônica).
- Maletín del Psicólogo → #7 (psicopedagogo AR).

## 5. Lista final de VERIFICAR
1. Andrei Kowalski (page 1340912605769671): re-checar 15–17/11 se passou de 30 dias; abrir a página para preço, plataforma, conteúdo, bumps e garantia.
2. Amélie Boissieu (1363004406903385) e Kit Contable Práctico (1411204478738237): conteúdo dos "7 cahiers + 6 bonus", checkout e se segue escalando (re-checar 20/11).
3. FR: micro-empresário em franquia de IVA é obrigado a EMITIR em 01/09/2027? Multa €50 por fatura (art. 1737 CGI)?
4. ES Verifactu: datas do RDL 15/2025 (01/01/2027 e 01/07/2027) e convalidação no BOE.
5. PL KSeF: data para micro (01/01/2027) e adiamento das multas; "Porady dla JDG" (983981824797132) cobra pelo PDF?
6. Zulma Laguna (778739435326228): ativo em 31/10 (30 dias)? preço $27 confirmado?
7. Dental Master Pro Max (1170940042761217): o que tem no kit de $27; Karbonna (117666710068820): qual produto.
8. Valéria Moura (828042450397666): preço, países e se o combo HACCP em espanhol sobrevive.
9. Psicopedagogia AR: Evaluá Psicope (1384325881424603) e Consultorio en Orden (1514939898362514) em 15/11; número de psicopedagogos na Argentina (fonte oficial).
10. Eletricista: IT DM 37/2008 (DiCo) e UK EICR 2020 (texto oficial); Markus Schneider (1401781706350470) e Acelera Negócios (837418056131966) em 15/11; IT "dichiarazione di conformità" na Biblioteca.
11. HACCP: Regulamento (CE) 852/2004 art. 5 (URL EUR-Lex), NOM-251-SSA1-2009, Res. 2674/2013; nº de restaurantes/cafés por país.
12. Caixa do Terapeuta no PT: passa de 30 dias por volta de 07/11?
13. L'angolo del Docente (IT, ~208d): é loja de material digital ou físico?
14. Itália, pedagogisti: prazos da Lei 55/2024 (Ordine) que possam virar gancho.
15. Oferta 0 ("Copie e Cole na Sua Marca", 312 anúncios no BR): qual é o produto (página não abriu).
16. Não pesquisado por limite (cota de busca web esgotada e "Too Many Requests" no conector): PT/DE/PL para eletricista; ES moldes de costura; FR/DE radiestesia; C14, C15, C16, C20, C21; EN HACCP com termos melhores (ex.: "SFBB", "food safety management system template").
17. Páginas de vendas das 53 ofertas brasileiras (WebFetch bloqueado): conteúdo, preço final, bumps e garantia, principalmente 23, 30, 35 e 46 (as que viram produto lá fora).
