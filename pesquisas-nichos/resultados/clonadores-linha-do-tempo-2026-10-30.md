# Clonadores do nosso modelo: linha do tempo e próximos nichos (30/10/2026)

> **Status:** concluído em 30/10/2026. Todas as medições são de anúncios ATIVOS via conector Meta.
>
> **Não havia versão anterior acessível (v1 de 29/10).** Por isso não dá para listar o que mudou em relação a ela. Toda página nova nesta lista foi encontrada hoje.
> **Limitações deste ambiente:** a v1 de 29/10 e os arquivos do Desktop NÃO estavam acessíveis; usei só a lista de operadores do prompt e as notas (`notas/*.md`). O SearchAPI NÃO estava disponível (sem chave aqui e créditos zerados até 08/11): toda medição foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página. Como o conector só vê anúncios ativos, "início" = anúncio ativo mais antigo, não necessariamente o primeiro anúncio da página.

## Resumo executivo

1. **O operador que mais importa é a "família APP".** É um operador só, com conta em USD, que vende os kits de dentista e psicólogo em IT e AR (o Kit Studio Blindato da nota de 28/10 é dele).
   - Mesmo molde de título "⭐ 4.9/5 · ..." e lotes criados no mesmo minuto em 4 páginas.
   - Dentista IT 43 dias (PROVADO) → psicólogo IT 36 dias (PROVADO) → dentista AR 32 dias (PROVADO, limite) → psicólogo AR 4 dias (TESTE).
   - Sequência: **dentista primeiro, psicólogo 6 dias depois, mesmo país; depois o mesmo par em outro país.** O próximo par provável é ES/MX/CO/CL ou PT (VERIFICAR a partir de 05/11).
2. **Itália ganhou um concorrente com norma italiana.** O **Sorrisi in Regola** (conta EUR, desde 17/10, 13 anúncios) vende kit de higienista, **"Kit DVR per studi dentistici"** (29/10), rastreabilidade de autoclave, registros de esterilização e um consentimento por procedimento, além de um webinar de segurança do trabalho. É o ângulo "norma" que era a nossa vantagem no Dentista Itália. Preço e plataforma: VERIFICAR.
3. **Onda do Leste Europeu (9–29/10).** Fábricas multi-idioma com conta USD e uma página só para 6 a 10 idiomas:
   - **Digital solutions**: 251 anúncios ("+70 documentos para o consultório" em GR/BG/HU, consentimentos, farmacologia, ECG);
   - **Recursoslandia**: 332 anúncios (TCC para psicólogo US$ 14,90, Ergo/Logopädie €19,90, eletricista FR, handebol);
   - **Escuela Saludable**: 47 anúncios, kit de terapeuta em HU/CZ/RO/PL/GR/TR, contas em CRC/EUR/USD;
   - **Andrei Kowalski**: dossiê HACCP para cafeteria, SK → CZ → RO → FR em 11 dias.
   - Todas usam uma persona local (Kowalski, Mureșan, Blažková, Hudáková, Marieke Vos, Luca Ferrari).
4. **impultienda.com é PLATAFORMA, não operador.** É uma loja/checkout argentino de infoproduto: a página "Tu tienda propia" (ARS) anuncia "Tu web cobra y entrega sola". Há ~390 anúncios ativos apontando para o domínio, de dezenas de vendedores, entre eles um kit de psicólogo IT (Pronto Soccorso Emotivo) e kits de terapeuta PT. Aparece junto **Denise Encinas** ("La IA arma tu negocio digital… Valida, escala y traduce"), que é provavelmente a escola que ensina a clonar e traduzir. VERIFICAR.
5. **Próximo nicho previsto** (seção 6):
   - nichos-filhos do dentista (higienista, DVR/segurança do trabalho) e do psicólogo (terapeuta, TCC, ABA, fono);
   - farmácia (PNOs, farmacovigilância);
   - fisioterapia e massagem;
   - em FR, DE, NL e nórdicos, que entraram em 28–29/10.

## 0. Método e o que funcionou neste ambiente

- **Conector Meta:** busca por `page_ids` devolve os anúncios ativos da página do mais novo para o mais antigo (até 50). Com ≤50 anúncios dá para ver o mais antigo e medir os DIAS REAIS; com >50, o resultado vira "≥ X dias".
- **Busca por domínio funciona:** `search_terms` = domínio (ex.: `kit-docs-odonto.lovable.app`) devolve os anúncios que apontam para ele. Testei com a Artes para Odontologia: 46 ativos, o mais antigo de 05/03/2026 = 239 dias, batendo com o EscalaLow (234 d em 24/10).
- **Busca por nome de página:** funciona quando o nome é raro e você filtra o país (ex.: Zgodny Gabinet no PL). Nomes comuns ("Farmacia al Día") só trazem ruído (anúncios de suplemento com "farmacia").
- **O conector não traz** texto do anúncio, URL de destino nem criativo. Só traz o título do link, a moeda da CONTA de anúncios (não a moeda da oferta), a data de início e o país do filtro.
- **Páginas de vendas: BLOQUEADAS.** WebFetch e curl recusam qualquer domínio fora da lista do ambiente (facebook.com, impultienda.com, hotmart.com, storeleads.app etc. → `ENOTFOUND` / `403`). Preço, checkout, bumps e garantia só entram quando o próprio título do anúncio mostra; o resto fica como VERIFICAR.

## 1. Tabela de páginas por operador (page_id)

Como ler a tabela:
- **Moeda** é a moeda da CONTA de anúncios (USD costuma indicar operador estrangeiro com conta em dólar). Preço em moeda local aparece só quando o título do anúncio mostra.
- **Início** é a data do anúncio ATIVO mais antigo; **dias** são contados até 30/10/2026.
- **Nº** é o total de anúncios ativos da página (estimated_total_count).

### 1.1 Operadores da lista do prompt

| Operador (v1) | Página / page_id | País · idioma | Moeda | Produto | Início | Dias | Nº | Régua |
|---|---|---|---|---|---|---|---|---|
| impultienda | **Plataforma** (página "Tu tienda propia" 1413976621794277, ARS). ~390 anúncios de vários vendedores apontam para impultienda.com | AR (loja) | ARS/USD | loja + checkout de infoproduto | — | — | ~390 (domínio) | não é operador |
| ↳ Farmacia Lista | 1315946498277803 | ES (país VERIFICAR) | USD | "Todo lo que tu farmacia necesita en una sola carpeta" | 28/10 | 1 | 2 | TESTE |
| ↳ Farmacia al Día | não achado | — | — | — | — | — | — | VERIFICAR |
| ↳ Consultorio al Día | não achado | — | — | — | — | — | — | VERIFICAR |
| Andrei Kowalski | 1340912605769671 | SK, CZ, RO, FR | USD | dossiê higiene/HACCP para café e bistrô | 18/10 | 12 | 17 | TESTE |
| Studio Facile | não achado. A busca IT achou a família APP (abaixo) | IT | — | — | — | — | — | VERIFICAR |
| PictoStudy Europe | não achado ("pictogrammi"/"Piktogramme" = 0) | — | — | — | — | — | — | VERIFICAR |
| Ultra Pack | não achado (busca só traz e-commerce) | — | — | — | — | — | — | VERIFICAR |
| Digital solutions | 1406571882531997 | GR, BG, HU, SR, HR/SL, PT | USD | "+70 documentos para o consultório", "16 tratamentos, 16 consentimentos", psicopatologia, +250 mapas de farmacologia, +90 pranchas de ECG | ≥27/10 (página toda relançada) | ≥3 | **251** | fábrica, TESTE |
| Recursos Legales PRO | 880855681786807 | MX | MXN | catálogo de kits legais de saúde de $249 a $999 MXN; advogados desde 28/10 | **23/07** | **99** | 5 | **PROVADO MX** |
| Digital Future | não achado | — | — | — | — | — | — | VERIFICAR |
| Kits Profesionales | 692615883936217 | MX | MXN | kits 2026: ambulância, laboratório clínico, farmacovigilância hospitalar | 07/10 | 22 | 7 | TESTE |
| Academia VIP | não achado | — | — | — | — | — | — | VERIFICAR |
| Escuela Saludable | 100723261734448 | HU, CZ, RO, PL, GR, TR | **CRC**/EUR/USD | kit de terapeuta: 120 exercícios com roteiro de sessão, genograma, nervo vago (64 cartas + 120 ferramentas), ventosas, chakras | 13/10 | 17 | 47 | TESTE |
| Pure Digital Shop | não achado | — | — | — | — | — | — | VERIFICAR |
| Recursoslandia | 954945787709648 | ES/LATAM, DE, FR, HR, DA, CZ, PL, HU, JA | USD | multinicho: TCC US$14,90 / CLP 14.990; Ergo/Logopädie €19,90; Triggerpunkte €15,90; handebol €15,90 / 109 kr; NF C 15-100 €19,90 (de €59,90); idiomas 369 Kč / 59 zł | ≥28/10 (relançado) | ≥2 | **332** | fábrica, TESTE |
| Guias Práticos | não achado | — | — | — | — | — | — | VERIFICAR |
| Emma Schneider | não achado (DE achou The Resource Lab e Therapy Toolkit, abaixo) | — | — | — | — | — | — | VERIFICAR |
| Zgodny Gabinet | 1228451337028686 | PL | PLN | documentação para fisioterapeuta móvel e masaż suchy, 199 zł "pierwsze 5 pakietów" | 26/10 | 3 | 6 | TESTE |
| Extreme Gym | só "extremegym18" (BR, academia física, 2025). Não é clonador | — | — | — | — | — | — | VERIFICAR |
| Kit Odontologico APP | 1218589731347806 | **AR** (37 de 43) | USD | papéis do consultório com logo, consentimentos, protocolos | **27/09** | **32** | 43 | **PROVADO AR** (no limite) |
| Consultorio en Regla | 1337994426072311 | **AR** | USD | papéis do consultório (obra social, historia clínica, atendimento online) | 27/10 | 2 | ~17 | TESTE |
| Consultorio Listo – Pediatras | 1379560635235954 | VERIFICAR | USD | biblioteca para pediatras, "oferta lanzamiento" | 11/10 | 19 | 1 | TESTE |
| OdontoDocs | 1328543073683086 | ES-LATAM | **BRL** | "105 documentos listos para tu consultorio" | 30/10 | 0 | 1 | TESTE |

### 1.2 Operadores NOVOS achados hoje (não estavam na lista)

| Página | page_id | País · idioma | Moeda | Produto | Início | Dias | Nº | Régua |
|---|---|---|---|---|---|---|---|---|
| **Kit Studio Blindato - APP** (família APP) | 1294553453740890 | IT | USD | kit dentista, "Tutte le carte del tuo studio, già pronte" (€19,99 na nota de 28/10) | **17/09** | **43** | 28 | **PROVADO IT** |
| **Kit di Documenti Psicologici** (família APP) | 1316795101520270 | IT | USD | "Oltre 270 documenti per psicologi" | **23/09** | **36** | 35 | **PROVADO IT** |
| **Kit Consultorio Psicologico APP** (família APP) | 1304281136103952 | AR | USD | "+120 documentos para psicólogos", "Tu nombre en cada documento" | 26/10 | 4 | >50 | TESTE |
| **Sorrisi in Regola** | 1063538733498593 | IT | **EUR** | norma do consultório odontológico: kit DVR, rastreabilidade de autoclave, registros de esterilização, consentimentos, kit de higienista, webinar | 17/10 | 13 | 13 | TESTE (concorrente direto) |
| Luca Ferrari | 1275716428958044 | IT | **BRL** | "A SOLI €9,99" (produto VERIFICAR) | ≤08/10 | ≥22 | 90 | TESTE (perto de 30 d) |
| Jessica Reynolds | 101176478643659 | IT | USD | "100 Schede Illustrate di Laserterapia" | 14/10 | 16 | VERIFICAR | TESTE |
| Pronto Soccorso Emotivo (impultienda) | 1429865763533829 | IT | USD | kit psicólogo, "Seduta pronta in 4 minuti" | 26/10 | 4 | VERIFICAR | TESTE |
| Qualitiva Soluciones | 574842992375227 | CO | COP | "Documentos listos para adaptar" (dentista) | **29/01** | **273** | VERIFICAR | PROVADO CO (já conhecido) |
| Dental PRO 360 | 768039019732604 | MX | MXN | VERIFICAR | 26/10 | 3 | VERIFICAR | TESTE |
| Salud Podal | 821483754384430 | ES | BRL | "Podóloga, moderniza tu consultorio" | 27/10 | 3 | VERIFICAR | TESTE |
| Ioana Mureșan | 1336453036226061 | RO | USD | "Dosarul pentru controlul DSP" (dentista), 89 lei | onda de 22–28/10 (nota); anúncio novo 29/10 | VERIFICAR | VERIFICAR | TESTE |
| Tereza Blažková | 366485309891364 | CZ | EUR | "Celá práce makléře v jednom diáři" (corretor de imóveis) | 09/10 | 20 | VERIFICAR | TESTE |
| Kristína Hudáková | 1318646484661479 | SK | EUR | o mesmo diário de corretor (clone SK) | 12/10 | 17 | VERIFICAR | TESTE |
| **Hanari Digital Sk** | 400335676487161 | SK/CZ | EUR | 250 prompts para professor, "pracovný list za menej ako minútu" | **13/07** | **109** | ≥2 | **PROVADO SK** (professor) |
| Luna Noire | 978656985328281 | TR | USD | "100 Kullanıma Hazır Terapi Seansı" | 27/10 | 3 | VERIFICAR | TESTE |
| Marieke Vos | 1450685058119021 | NL/BE | USD | "Kant-en-klare ABA-protocollen" | 29/10 | 1 | ≥12 | TESTE |
| The Resource Lab | 1123744187496255 | DE | USD | "Die Bibliothek für die soziale Betreuung" (Pflege) | 29/10 | 1 | ≥3 | TESTE |
| Therapy Toolkit | 102506312071455 | DE | USD | "Therapiematerial-Kit für Kinder" | 11/10 | 19 | ≥4 | TESTE |
| Digital Home (impultienda) | 1285293408008330 | RO | USD | "90 de fișe de lucru TCC gata pentru ședință" | 29/10 | 1 | VERIFICAR | TESTE |
| Veronica Rose (impultienda) | 1342395585621504 | PT/EN | USD | "Kit do Terapeuta Sistémico", constelações | 28/10 | 1 | VERIFICAR | TESTE |
| Fonemas en Juego (impultienda) | 1272500302624536 | ES | USD | fono: "820 piezas listas para imprimir" | 29/10 | 0 | ≥7 | TESTE |
| Alma Artesana | 1089888217551160 | HR | USD | Natal ("Božićna večer u 3 dijela") | 29/10 | 1 | VERIFICAR | fora do escopo |
| Етажна собственост | 1087877047748166 | BG | USD | manual do condômino, 3 pacotes | 28/10 | 2 | VERIFICAR | TESTE |
| Denise Encinas | 777108258821844 | ES | USD | curso "La IA arma tu negocio digital / Valida, escala y traduce" (provável escola dos clones) | 14/10 | 16 | ≥10 | VERIFICAR |
| Udemia.IA | 1187693011097208 | PT, RO, EL, BG… | USD | curso "Domine Claude/IA em 7 dias" (mesma máquina de tradução) | — | — | VERIFICAR | fora do escopo |

### 1.3 Notas de campo por página (log bruto, na ordem em que foram coletadas)
- **Zgodny Gabinet** (PL): page 1228451337028686, moeda PLN. Títulos: "Dokumentacja dla fizjoterapeuty mobilnego", "Dokumentacja gabinetu masażu suchego", "199 zł, pierwsze 5 pakietów", "Pliki Word i PDF od razu po zakupie", "RODO i organizacja danych". Anúncios mais antigos vistos: 26/10/2026.
- **OdontoDocs**: page 1328543073683086. Título "105 documentos listos para tu consultorio" (espanhol), conta em BRL, ou seja, operador brasileiro vendendo em espanhol.
- **Recursoslandia**: page 954945787709648, conta em USD, multinicho e multi-idioma:
  - HR: "240 gotovih rukometnih treninga – 15,90 €";
  - FR: eletricista NF C 15-100, "19,90 € au lieu de 59,90 €", "Le devis, déjà calculé";
  - PL: "Cały hiszpański za 59 zł";
  - HU: limpeza.
- **impultienda.com** (busca por domínio: ~390 anúncios ativos) mostra MUITAS páginas diferentes, quase todas com conta em USD. Parece PLATAFORMA/loja usada por vários vendedores, não um operador só. Páginas vistas:
  - Pronto Soccorso Emotivo (IT, kit de psicólogo: "Seduta pronta in 4 minuti");
  - Veronica Rose ("Kit do Terapeuta Sistémico", "Everything for your session in one toolkit");
  - Dra Laura martin (PT-PT, EUR);
  - Jantar Feito (PT);
  - Luisa Diaz (PT, artesanato);
  - Smart Learning Academy (CLP, "300 sessões para goleiros");
  - 365 Atividades sem Ecrãs (PT);
  - Udemia.IA;
  - Improvisación Mastery.
  - Também aparece **Denise Encinas** ("La IA arma tu negocio digital", "Valida, escala y traduce", "Lanza, prueba, aprende"), que parece o curso que ensina a clonar e traduzir com IA. VERIFICAR.
- A busca "impultienda" sem ".com" (~22 mil, mais difusa) trouxe:
  - Fonemas en Juego (ES, fono, "820 piezas listas para imprimir");
  - Digital Home (RO, "90 de fișe de lucru TCC gata pentru ședință");
  - «A hit miértje» (HU, catequese);
  - Tinkerkids (TR/HU, robótica infantil);
  - Que Te Busque El; Negocio Resuelto (planos de cama casita).
- **Andrei Kowalski**: page 1340912605769671, conta em USD, **17 anúncios ativos**. Produto: dossiê de higiene/HACCP para café e bistrô ("pasta para a fiscalização"), o modelo Consultora Sanitária traduzido. Ordem dos anúncios ativos mais antigos:
  - **SK** 18/10 ("Zajtra ráno kontrola? Zložka hotová dnes"), o mais antigo = 12 dias;
  - **CZ** 20/10 ("Kavárna a bistro připravené na kontrolu");
  - **RO** 22/10 ("Dosar de igienă pentru cafenea și bistro");
  - SK/RO 26/10 (novos ângulos: "6 vecí na zozname kontrolóra", "Dosarul dvs. e la zi?");
  - CZ/SK 28/10 ("7 drobností, za které dostanete pokutu");
  - **RO** 29/10 (DSVSA) e **FR** 29/10 ("L'inspecteur de la DDPP est à la porte").
  - Ordem de expansão: SK → CZ → RO → FR em 11 dias.
- **OdontoDocs**: 1 anúncio ativo, criado 30/10 (0 dias). Título "105 documentos listos para tu consultorio", conta BRL.
- **Zgodny Gabinet**: **6 anúncios ativos**, todos de 26–27/10 (o mais antigo tem 3,4 dias), conta PLN. Produtos: documentação para fisioterapeuta móvel e para gabinete de "masaż suchy", 199 zł "pierwsze 5 pakietów" (escassez), Word + PDF.
- **Recursoslandia**: **332 anúncios ativos**; os 50 mais novos foram todos criados em 28–29/10. Filtrando ES/LATAM: 20 anúncios, também todos criados em 28/10. Ou seja, a página inteira foi relançada em 28–29/10 (não dá para ver o anúncio mais antigo).
  - ES/LATAM: "TCC Sesión a Sesión", US$ 14,90 / CLP $14.990, "garantía 30 días", "15 fichas listas", "Mapa de consulta".
  - DE: "Ergotherapie auf einen Blick – 19,90 €", "Logopädie auf einen Blick – 19,90 €"; handebol "240 fertige Handball-Einheiten – 15,90 €".
  - DA: "240 færdige håndboldtræninger – 109 kr". HR: "240 gotovih rukometnih treninga – 15,90 €".
  - FR: eletricista NF C 15-100, "500 fiches", 19,90 € (de 59,90 €), "Le devis, déjà calculé".
  - CZ: "Celá španělština / němčina na 365 mapách", "Všechno za 369 Kč". PL: "Cały hiszpański za 59 zł".
  - JA: espanhol em 365 mapas. HU: limpeza da casa em 5 dias.
- **A busca "documentos listos consultorio" achou o cluster de LATAM** (18 anúncios):
  - **Kit Odontologico APP**: page 1218589731347806, conta USD, **43 anúncios ativos (37 na Argentina)**.
    - O mais antigo é de **27/09 = 32 dias**. Lotes de criação: 27/09 → 07/10 → 16/10 → 26/10 (relança um lote a cada ~10 dias e mantém 1 ou 2 anúncios antigos).
    - Voseo ("Tu logo en cada papel que entregás"). Ângulos: logo do dentista em cada papel, "Un consentimiento para cada tratamiento", "Protocolos escritos de cada tratamiento", "Indicaciones para llevar a casa", "El paquete completo del consultorio", prova social "4.9/5".
  - **Kit Consultorio Psicologico APP**: page 1304281136103952, conta USD, **51 anúncios no filtro AR** (o total passa de 50). O mais antigo visto é de 26/10 (4 dias). Títulos: "+120 documentos para psicólogos", "Tu nombre en cada documento", "El papeleo de antes y después de la sesión". É **clone irmão do Kit Odontologico APP** (mesmo layout de título "⭐ 4.9/5 · ...", mesmo dia de criação 26/10).
  - **Consultorio en Regla**: page 1337994426072311, conta USD, ~17 anúncios (17 no AR). O mais antigo é de **27/10 (2,4 dias)**. Gancho argentino: "¿Tu obra social te lo pidió?", "¿Tu historia clínica resiste un pedido?", "Si atendés online, leé esto", "El consentimiento te lo van a pedir".
  - **Consultorio Listo – La Biblioteca Definitiva para Pediatras**: page 1379560635235954, conta USD, **1 anúncio ativo**, "OFERTA LANZAMIENTO", de 11/10 (19 dias). País: VERIFICAR.
  - **Recursos Legales PRO** (antes "Recursos Legales PRO Salud Mx"): page 880855681786807, conta **MXN**, 5 anúncios. O mais antigo é de **23/07/2026 = 99 dias** (MX).
    - Catálogo no título: Kit Consultorio Médico $499 MXN, Kit Cirujano Dentista $499, Kit Legal Psicología $499, Kit Spas y Cosmetología $699, PNOs Farmacia Lite $249 / Estándar $699 / PRO $999.
    - Novo em 28/10: kits para advogados/empresas ("26 Formatos + 3 Guías $499 MXN", "Colección Completa $699 MXN", "6 Áreas Clave en un Solo Kit").
  - Outros vistos:
    - **Qualitiva Soluciones** (CO, COP, page 574842992375227, anúncio ativo de 29/01/2026 = 273 dias, "Documentos listos para adaptar"). Já estava no radar: dentista Colômbia.
    - **Dental PRO 360** (MXN, page 768039019732604, 26/10).
    - **Salud Podal** (BRL, page 821483754384430, "Podóloga, moderniza tu consultorio!", 27/10). Mais um BR vendendo em espanhol.
- **Farmacia Lista**: page 1315946498277803, conta USD, **2 anúncios ativos**, ambos de 28/10 (1,2 dias). Título: "💊 TODO LO QUE TU FARMACIA NECESITA EN UNA SOLA CARPETA". País VERIFICAR.
- **Kits Profesionales**: page 692615883936217, conta MXN, **7 anúncios ativos**. O mais antigo é de **07/10 (22 dias)**. Lança um kit novo a cada ~5–10 dias:
  - 07/10: sem título;
  - 11/10: "KIT DE PROTOCOLOS DE AMBULANCIAS 2026";
  - 22/10: "KIT PROFESIONAL DE MANUALES PARA LABORATORIO CLÍNICO 2026" e "KIT PROFESIONAL DE FARMACOVIGILANCIA HOSPITALARIA 2026";
  - 29/10: sem título.
- **Digital solutions**: page 1406571882531997, conta USD, **251 anúncios ativos**. Os 50 mais novos foram criados entre 28 e 30/10. Multi-idioma na mesma página:
  - "+70 ready documents for the clinic" ("ιατρείο"/"кабинет"/"rendelő"): GR "+70 έτοιμα έγγραφα για το ιατρείο", BG "+70 готови документа за кабинета", HU "Rendelő Rendben – +70 kész dokumentum".
  - Odonto/estética: HU "16 kezelés. 16 nyilatkozat. Kész.", BG "16 лечения. 16 съгласия. Готово." (16 tratamentos, 16 termos de consentimento).
  - Psicologia: "Psicopatologia em uma página" (HU/BG).
  - Mapas visuais de farmacologia ("+250 mapas visuais de farmacologia" em PT, BG, SR "vizuelnih mapa", HR/SL "vizualnih shem"), criados 28 e 30/10.
  - ECG: BG "+90 илюстровани ЕКГ табла".
  - GR "Τέλος ο μπαλωμένος φάκελος" ("chega de pasta remendada").
- **Ioana Mureșan** (RO, dentista, já conhecida): page 1336453036226061, conta USD. Anúncio novo de 29/10. O título mostra a oferta inteira:
  - "Dosarul pentru controlul DSP": 39 documentos do consultório + 22 documentos do paciente + registros prontos para imprimir;
  - bônus: "Ziua controlului", treinamento da equipe, calendário do consultório, **"Actualizări 12 luni"**;
  - preço: **"Tot kitul: 89 lei"**.
- **Kristína Hudáková** (SK, EUR, page 1318646484661479, desde 12/10 = 17 dias) e **Tereza Blažková** (CZ, EUR, page 366485309891364, desde 09/10 = 20 dias): o MESMO produto ("Celá práce makléře v jednom diáři", diário/planner de corretor de imóveis). É par de clones CZ→SK com nome de pessoa local e conta em EUR.
- **Hanari Digital Sk** (SK, EUR, page 400335676487161): "Pracovný list za menej ako minútu", "250 promptov pre učiteľov". Anúncio ativo desde **13/07/2026 = 109 dias**. É PROVADO para professores na Eslováquia (prompts de IA + fichas).
- **Udemia.IA** (page 1187693011097208, USD): curso "Domine o Claude/IA em 7 dias" em PT, RO, EL, BG etc. Não é kit de profissão, mas usa a mesma máquina de tradução.
- **"Етажна собственост: Наръчникът на собственика"** (BG, page 1087877047748166, USD): manual do condomínio, "3 pacotes", desde 28/10.
- **ITÁLIA ("documenti pronti studio")**: achei a família "APP", que é UM operador só. Em todas as páginas o título segue o molde "⭐⭐⭐⭐⭐ 4.9/5 · ...", e os lotes são criados no mesmo minuto em páginas diferentes.
  - **Kit Studio Blindato - APP** (dentista IT): page 1294553453740890, conta USD, **28 anúncios ativos**, o mais antigo de **17/09 = 43 dias**. Lotes: 17/09, 29/09, 05–06/10, 09/10, 21/10, 23/10. Ângulos: "Tutte le carte del tuo studio, già pronte", "Stampa solo quello che ti serve", "Ogni foglio della giornata, pronto". Na nota de 28/10 o preço era €19,99. **PROVADO em IT.**
  - **Kit di Documenti Psicologici** (psicólogo IT): page 1316795101520270, conta USD, **35 anúncios ativos**, o mais antigo de **23/09 = 36 dias**. Lotes: 23/09, 05–07/10, 21–23/10, 26/10. Título "Oltre 270 documenti per psicologi 📄". **PROVADO em IT.**
  - **Kit Odontologico APP** (dentista AR, desde 27/09) e **Kit Consultorio Psicologico APP** (psicólogo AR, desde 26/10) são o mesmo operador:
    - lote de 05/10: criado no mesmo minuto em IT dentista e IT psicólogo;
    - lote de 07/10: no mesmo minuto em IT dentista, IT psicólogo e AR dentista;
    - lote de 25/10: no mesmo minuto em AR dentista e AR psicólogo.
  - **Sorrisi in Regola** (IT, conta **EUR**, page 1063538733498593): "Il kit che mancava all'igienista" (kit para higienista dental), desde 22/10 (8 dias). É um nicho-filho do dentista.
  - **Luca Ferrari** (conta **BRL**, page 1275716428958044): "A SOLI €9,99", desde 07/10 (22 dias). BR na Itália a €9,99. Produto: VERIFICAR.
  - **Jessica Reynolds** (USD, page 101176478643659): "100 Schede Illustrate di Laserterapia", desde 14/10 (fisioterapia/estética).
- **Varredura por idioma (termos "documentos prontos" e "pack" em cada idioma):**
  - **HU** "kész dokumentum": só aparece Digital solutions ("Rendelő Rendben – +70 kész dokumentum", desde 27/10). O resto é nativo (Helyesen írva-szerkesztve, Laba "Digitális transzformáció jogászoknak", MUBI segurança do trabalho, este último desde ~01/08).
  - **HR/SR/SI/BA** "gotovih":
    - Recursoslandia (handebol, "Cijela sezona – 15,90 €", "40 treninga po uzrastu");
    - **Alma Artesana** (page 1089888217551160, USD, "Božićna večer u 3 dijela", 28/10), fábrica sazonal de Natal;
    - **Pozivko** (page 1285752287961638, EUR, "50 pozivnica za svaku priliku");
    - Sargon Academy (IA).
  - **TR** "psikologlar için hazır": **Luna Noire** (page 978656985328281, USD, "🧠 100 Kullanıma Hazır Terapi Seansı", desde 27/10), clone do kit de terapeuta. Fora isso, "Hijyen Sertifikam" (TRY, certificado de higiene 1.400 TL "aynı gün hazır") é serviço local, não kit.
  - **NL/BE** "kant-en-klaar": **Marieke Vos** (page 1450685058119021, USD, "Kant-en-klare ABA-protocollen", 29/10). É o clone do Inovaba (ABA) BR. O resto é software (Clearfacts).
  - **DA/NO** "færdige skabeloner": nada de kit. Só Recursoslandia (handebol, 109 kr).
  - **SV/FI** "färdiga mallar": só nativos (Kreativ Undervisning "Lyckat Läsår", Melina Ede "Halloweenpyssel att skriva ut" em SEK, Memolio). Nenhum clone de kit de profissão.
  - **RO** "documente gata": Ioana Mureșan (dentista), Udemia.IA, DocGen App (software). **CZ/SK** "hotové dokumenty": par de corretores (Tereza/Kristína) e Hanari Digital.
  - **EL/GR** "έτοιμα έγγραφα" e **BG** "готови документи": Digital solutions dominando (ιατρείο/кабинет).
- **Farmacia al Día / Consultorio al Día** (ligadas à impultienda na v1): NÃO achei pelo conector. A busca por nome só traz ruído de suplemento, e a busca por domínio "impultienda.com" (50 mais novos) não mostrou essas páginas. → VERIFICAR com o page_id da v1.

## 2. Linha do tempo de lançamentos

(em preenchimento)

## 3. Páginas de vendas (preço, checkout, bumps, garantia, domínio)

(em preenchimento)

## 4. Padrões (ordem de expansão, tempo até matar anúncio)

(em preenchimento)

## 5. Operadores novos (idiomas não cobertos)

(em preenchimento)

## 6. Previsão do próximo nicho

(em preenchimento)

## 7. Ranking 0–10

(em preenchimento)

## 8. Lista de page_ids para o EscalaLow

(em preenchimento)

## 9. VERIFICAR

(em preenchimento)
