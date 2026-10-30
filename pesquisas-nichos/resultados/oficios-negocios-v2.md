# Ofícios e negócios por país — v2 (30/10/2026)

> **Avisos de ambiente (ler antes)**
> - A v1 (`pesquisas-nichos-2026-10-29/oficios-negocios.md`) **não estava acessível** (container na nuvem, sem Desktop). Usei só o que o prompt cita dela (Andrei Kowalski; Studio Facile/PictoStudy; títulos vazios Más seguridad, Beatriz Guerra, Solunetpro) e as notas do usuário (`notas/*.md`).
> - **SearchAPI indisponível** (sem chave aqui e créditos zerados até 08/11/2026). Toda a medição foi feita com o conector Meta (`ads_library_search`, só anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
> - **WebFetch bloqueado pela rede do container** (proxy recusa facebook.com, wikipedia, salute.gov.it, pictostudy.com e outros). Não consegui abrir nenhuma página de vendas nem texto oficial de norma.
> - **WebSearch esgotou** (limite de 200 buscas por turno, compartilhado com os agentes irmãos) depois de poucas buscas minhas, e as poucas que rodei não acharam os sites dos concorrentes. Por isso **nenhuma norma, data ou tamanho de mercado deste relatório foi confirmado em fonte oficial**: tudo isso está marcado VERIFICAR.
> - O conector Meta não devolve o link de destino nem o texto do anúncio. Devolve só a página, o título do link, a data de início e a moeda da CONTA de anúncios (que não é a moeda do preço; conta em USD ou BRL costuma ser operador brasileiro). A busca por palavra é ampla (não é frase exata) e mostra no máximo 50 anúncios, os mais novos primeiro. Em páginas com centenas de anúncios não dá para achar o mais antigo.
> - Régua: PROVADO = anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.

---

## 0. Resumo

**Top 5 (nota 0–10):**
1. **México: formatos de seguridad e higiene / STPS para o pequeno patrão (7,5).** PROVADO: "Más seguridad" tem anúncio ativo há **361 dias** (conta em MXN), e a rede de páginas irmãs abriu páginas novas em outubro (está escalando). Casa com a "Jornada México" que já está na fila (mesmo comprador, o patrão PyME).
2. **Simulado de inspeção sanitária (a Consultora traduzida) em FR/RO/CZ/SK/IT/PT/ES (6,5).** É um TESTE em corrida: Andrei Kowalski tem 17 anúncios em 4 países, mas só 11,8 dias. Studio Facile faz HACCP ilustrado em IT/PT. Ninguém provou ainda, então a janela está aberta. Re-checar Kowalski entre 17 e 20/11.
3. **Chile: SST da PyME (DS 44 + protocolo Ley Karin + reglamento interno) (6,0).** TESTE/PRAZO. Vendedores locais em CLP começaram agora (Chileprevencion.cl, Arévalo y Paz, Sonia Abarca), todos com ≤2 dias. O gancho de norma existe (aparece nos títulos), mas as datas ficam VERIFICAR.
4. **Kit do anfitrião de aluguel curto (6,0).** Em inglês está PROVADO: BNB Tracker Pro vende o kit a US$9, com anúncio ativo há **82,9 dias**. Na Itália é TESTE com gancho de norma: "Protocollo Zero Sanzioni" (EUR, 6 d) e o gancho "Dal 2028 serve l'autorizzazione" (VERIFICAR).
5. **Colômbia SG-SST (5,5) e Itália DVR (5,5), empatados.**
   - Colômbia: Solunetpro vende em COP há 13,4 d. Aproveita a infraestrutura CO da fila (dentista e psicólogo).
   - Itália: Beatriz Guerra (operador BR) tem 1 criativo com 34,8 d. O resto do mercado é consultoria que faz o "DVR em 48–72 h".

**Diferenças em relação à v1** (pelo que o prompt cita dela, porque o arquivo não abriu):
- **Más seguridad** deixou de ser "título vazio": é seguridad e higiene no MÉXICO, com 361 d. É o achado mais forte da área.
- **Beatriz Guerra** = sicurezza/DVR na ITÁLIA, conta em BRL, 34,8 d com 1 anúncio só (prova fraca).
- **Solunetpro** = formatos SG-SST na COLÔMBIA, em COP, 13,4 d (TESTE).
- **Andrei Kowalski** medido: 17 anúncios em FR/RO/CZ/SK, o mais antigo de 18/10, ou seja, 11,8 d. **Ainda não provou.**
- **Studio Facile** não é um concorrente de HACCP: é uma fábrica de e-books ilustrados com **920 anúncios** em uns 10 idiomas e ~20 ofícios, todos criados em 29/10. "PictoStudy" não aparece em nenhum anúncio nem na busca web.
- Novidades desta rodada:
  - construção na América Latina começando: herrería MX 13 d, kit de obra CLP 0 d;
  - kits de limpeza em inglês nascendo nesta semana;
  - pastor em espanhol lotado: 166 anúncios, todos com <30 d.

---

## 1. Concorrentes da v1 a checar

| Página (page_id) | O que vende | Países/idiomas vistos | Nº anúncios ativos | Anúncio ativo mais antigo | Dias reais | Moeda da conta | Veredito |
|---|---|---|---|---|---|---|---|
| **Andrei Kowalski** (1340912605769671) | "Pasta de higiene" para café e bistrô, um simulado de inspeção sanitária. Títulos: "L'inspecteur de la DDPP est à la porte. Qu'est-ce que vous lui montrez ?", "Mâine vine controlul DSVSA. Aveți dosarul pregătit?", "Dnes ráno kontrola. Kde máte zložku HACCP?", "Planul HACCP pe perete, nu în sertar", "7 drobností, za ktoré dostanete pokutu aj v čistej kaviarni" | FR, RO, CZ, SK | 17 | 18/10/2026 | **11,8 d** | USD (típico de operador BR) | **TESTE.** É a Consultora traduzida em 4 países ao mesmo tempo. Preço, checkout e bumps: VERIFICAR |
| **Studio Facile** (1232011766670582) | Fábrica de e-books **ilustrados** ("X spiegato con i disegni", "Veja as páginas antes de descarregar"). Temas:<br>• ofícios: cozinha profissional e higiene na cozinha (HACCP), toelettatura, idraulico, elettricista, falegnameria, macellaio, soldadura, bombas de calor, fotovoltaico, segurança do trabalho<br>• outros: contabilidade, primeiros socorros, consultório dentário, unhas, nutrição, LIS, física, matemática, vinho, cogumelos | IT (345 anúncios), DK (98), PT, PL, CZ, GR e outros | **920** | todos os 150 vistos foram criados em 29/10/2026 | **≈1 d** (o conector só mostra os 50 mais novos, então pode haver anúncio antigo escondido) | USD | **TESTE em massa** (1 livro ilustrado × ~20 ofícios × ~10 idiomas). "PictoStudy" provavelmente é o nome do site ou do checkout: VERIFICAR |
| **Más seguridad** (291789807354053) | Anúncios sem link title (imagem ou vídeo). A busca "NOM-035 formatos" (MX) puxou a rede. Páginas irmãs:<br>• "Seguridad e higiene y más" (345679278628269): 3 anúncios, 361 d<br>• "Seguridad e higiene y mas.9" (101919158005402): ≥4 anúncios, 13,9 d<br>• "Seguridad e higiene y más" (1101519659721154): novos de 29/10<br>• "Formatos digitales pro" (1301518069721501): novos de 29/10<br>• outra "Más seguridad" (1308025092398670): 3 anúncios de 29/10, que também aparece na busca "presupuestos de obra" | MX | 5 | **02/11/2025** | **361 d** | MXN | **PROVADO no MX.** Dois anúncios de 361 d, e a rede abrindo páginas novas em outubro = escalando. Produto e preço: VERIFICAR (provável pacote de formatos de seguridad e higiene / NOMs STPS) |
| **Beatriz Guerra** (907895875729587) | Em italiano: "Capisci il rischio, non andare a memoria". Aparece na busca "DVR valutazione dei rischi" | IT | 8 | 25/09/2026 | **34,8 d** (só 1 anúncio tão antigo; os outros 7 têm ≤12 d) | BRL (operador BR) | **PROVADO fraco no IT** (1 criativo com 30+ d). Produto exato: VERIFICAR |
| **Solunetpro** (1118702291315648) | "Formatos SG-SST con normas 2025-2026", "¿No sabes por dónde empezar el SG-SST?", "Primero recibes y luego pagas!", "Para asesores con varias empresas", "Deja de bajar formatos sueltos" | CO | 15 | 16/10/2026 | **13,4 d** | COP | **TESTE.** Vendedor local, "recebe primeiro e paga depois" |

Outros vendedores do mesmo tipo:
- **Marina cardozo** (1019209551268731): conta USD, 67 anúncios, fábrica de vários produtos. Tudo com ≤2 d: TESTE.
  - FR: "Ton entreprise en règle en un après-midi", que aparece na busca **DUERP** (6 anúncios, todos de 29/10, 0,7 d).
  - ES: "Las 45 actas, ya redactadas" e "Dueño de negocio: tus reglas, por escrito y firmadas" (reglamento interno).
  - PT: manual de habilidades.
- **Seguridad y Salud Ocupacional y Medio Ambiente** (108273737689362): conta PEN, mira a Colômbia. Vende "PACK DOCUMENTAL SG-SST + DASHBOARD Y SEÑALETICA" e "Pack Completo ISO + Dashboards". 4 anúncios, o mais antigo de 23/10 (6,4 d). Há uma página irmã, "Documentos - SSO y Medio Ambiente" (193948423812234), com "Pack Ingeniería Civil".
- **Studio in Ordine** (1441969015658409): EUR, Itália, "Il faldone dello studio, già scritto". 3 anúncios de 29/10. TESTE nativo.
- **Annie Portinari** (102222484836247): EUR, Itália. "Se domani arrivasse un controllo ASL?", "Legionella in condominio: chi ne risponde?", "Proteggi la reputazione del tuo hotel". 4 anúncios de 27/10. Parece consultoria. VERIFICAR.

---

## 2. Nichos por país (o que o conector mostrou em 30/10)

### 2.1 HACCP / inspeção sanitária (simulado tipo Consultora)

| País | Quem anuncia | Dias reais | Leitura |
|---|---|---|---|
| FR / RO / CZ / SK | Andrei Kowalski (USD) | 11,8 d | TESTE de operador BR. O resto da busca FR "contrôle sanitaire restaurant" é software ou consultoria: ePackPro, HACCP Simple, EFAA "Diagnostic gratuit", Quality Food Industry, Resto Propre (luvas). Nenhum kit nativo barato |
| IT | Studio Facile (USD, ~1 d, "L'igiene in cucina, con i disegni", "La cucina professionale, spiegata con i disegni"); Annie Portinari (EUR, consultoria) | ~1–3 d | O resto é software ou consultoria antiga: HACCP Smart–JPvision (EUR, ativo há 164 d), NORMA HACCP, EPC Editore (módulo HACCP), Biorsaf, Gaesco "Conformi ASL", Facile Sicurezza (serviço, desde jan/2025). Kit barato nativo: **BRECHA** |
| PT | Cristiano Monteiro (EUR, 3 anúncios sem título, o mais antigo de 21/09 = **38,2 d**); Novelty Nook (USD) "Guia de Formação HACCP para Cantinas Escolares" (≈0,5 d); Studio Facile "O HACCP explicado com desenhos" | 38 d / 0–1 d | Cristiano Monteiro pode ser a primeira prova em PT, mas o produto é desconhecido (VERIFICAR). Os demais estão em TESTE |
| ES | Trazabilidad Express (EUR, "Obrador listo para Sanidad", 3 anúncios de 27/10, ~2,2 d) | ~2 d | TESTE nativo, só para obrador/padaria |
| CO | Aprende y Emprende (USD) "Paquete BPM" (~2,5 d); consultorias (Alka Gestión Sanitaria, Sklafood, Ingenio Alimentario, Fumycontrol "Evita multas y sellamientos") | ≤3 d no kit | Kit BPM só em TESTE. Há demanda por "visita sanitaria" (consultorias anunciando) |
| MX | KINSO ("Consigue Distintivo H", serviço); SAR Solutions (curso de inocuidad a $1.890 MXN) | — | Kit de inspeção COFEPRIS/Distintivo H: **BRECHA** (só serviço e curso) |

### 2.2 SST do pequeno empregador

| País | Quem anuncia | Dias reais | Leitura |
|---|---|---|---|
| **MX** | **Más seguridad** e "Seguridad e higiene y más" (MXN, **361 d**) e as páginas irmãs novas; Formato Empresarial (MXN, 1 anúncio, **229,8 d**); Media Center México (MXN, mega-pack a $99 MXN: "+300 Formatos Laborales + Contratos por $99 pesos", **33,1 d**; 56 anúncios, o mais antigo visto com 37,1 d); Coaserta ("NOM-035 sin complicaciones", 10,4 d) | **361 d** | **PROVADO.** Preço de referência do mercado: **$99 MXN** no pacotão genérico |
| **CL** | Chileprevencion.cl (CLP, 10 anúncios, todos de 30/10). Títulos: "FORMATOS 2026 PROTOCOLO LEY KARIN V3", "DOCUMENTOS 2026 NUEVO DS 44 PARA EMPRESAS Y COMERCIO", "MATRICES IPER 2026 DS 44", "REGLAMENTO INTERNO 2026 v6 DS 44 (RIOHS y RIHS)", "Capacitaciones mínimas obligatorias Resolución 1117 Ds 44", "PROTOCOLO TMERT V3 2026", "PLAN DE RESPUESTA A EMERGENCIAS 2026". Também: Arévalo y Paz Abogados (CLP, "¿Qué le muestra al fiscalizador?", "Qué incluye el Dossier", ~1 d); Sonia Leonor Abarca (CLP, "Reglamento Interno PYME listo para Dirección del Trabajo y SEREMI", 2,2 d) | 0–2 d nos anúncios | **TESTE + PRAZO.** O gancho de norma (DS 44, Ley Karin) aparece nos próprios anúncios. Chileprevencion parece um portal antigo que trocou os criativos hoje (a idade real do vendedor: VERIFICAR) |
| CO | Solunetpro (COP, 13,4 d); SSO y Medio Ambiente (PEN, 6,4 d); e-Misión (COP, serviço) | 13 d | TESTE |
| IT (DVR) | Beatriz Guerra (BRL, 34,8 d); consultorias: Fo Click ("Evita sanzioni inutili: DVR in 72 ore", EUR, **128,2 d**), TCertifico ("Sai com'è strutturato il DVR?", EUR, **68 d**), Sanzione Zero ("Nuova Apertura? DVR in 48 ore con Garanzia", EUR, 16,4 d), Nicola Nocera, Emmess ("Il tuo DVR prende polvere?"), software EPC/Blumatica | 35 d (kit) / 68–128 d (serviço) | Há demanda paga e antiga, mas do lado do SERVIÇO. Kit barato: prova fraca (1 criativo BR) |
| FR (DUERP) | Marina cardozo (USD, 0,7 d); Preventionbtp (organismo setorial); People Vox (software RPS) | <1 d | **TESTE / quase BRECHA** no kit barato |
| PE | Página SSO (PEN) vende para a Colômbia; sem vendedor PE próprio visto | — | não medido a fundo |

### 2.3 Pastor / igreja (espanhol)
- Busca "bosquejos para predicar" (MX/CO/PE/AR/CL/US/GT/DO/EC/BO): **166 anúncios**.
- **Luz y Palabra** (115620948182714, conta USD): 40 anúncios só nos EUA. O mais antigo tem **20,8 d** ("110 bosquejos listos para predicar", "Que el próximo sábado termine temprano").
- **Juliana Vargas** (COP): "52 bosquejos listos para predicar", "Prepara tu ceremonia sin improvisar", "Recíbelo primero, aporta después".
- Outros: Unidos en la Fe (USD, entrega por WhatsApp), Predica con Propósito, JSN, Pastor Pablo Ramírez (BRL), Daniela Hernandez (BRL).
- Leitura: **lotado e jovem**. Muita gente (inclusive BR) entrou nas últimas 3 semanas, ninguém medido passa de 30 d, e o espanhol neutro não prova país.
- A fonte BR é antiga (Biblioteca Teológica Atualizada 125–129 d e Augustus Nicodemus 390–562 d no EscalaLow).
- Não recomendo entrar agora.

### 2.4 Gastronomia LATAM (ficha técnica e custo do prato)
- Aprende Profesional (MXN): "50 FICHAS DE COSTEO PASO A PASO", "CALCULA EL COSTO REAL DE CADA PLATO", ~3 d.
- **Aprendia: Guías Oficiales** (1453826204471738, MXN, **414 anúncios**): fábrica de "50 fichas" de vários temas, incluindo receita padrão, "arroz chaufa… para vender", reumatologia, segurança penitenciária e segurança viária. Mais antigo visto: 12,2 d.
- Página irmã "Guías visuales - Aprendia" (MXN): "Ficha de recepción, tarifas por servicio y plan de arranque en 30 días" (limpeza de tênis).
- A fonte BR é provada (Minhas Finanças Organizadas: precificação 370 d, versões pizzaria/hamburgueria/açaiteria).
- Leitura: **TESTE.** Ninguém na América Latina com 30 d.

### 2.5 Limpeza
- Espanhol: Ideas Lab (PEN) "+400 FORMULAS ASEO" (fórmulas de produtos), Aprende y Emprende MX "Pack Profesional de Limpieza de Tapicerías" (~52 d, mas é ofício de estofado, VERIFICAR), Aprendia (limpeza de tênis). Kit de gestão para empresa de limpeza (contratos, orçamentos, checklists): **BRECHA**.
- Inglês: três páginas novas nesta semana, ainda **TESTE**:
  - **Pro Trade Kits** (USD): "16 editable templates for your cleaning business" e "Price your cleaning jobs with a calculator", 2 anúncios, 0 d;
  - **BizReady Kits** (USD): "50% OFF Business Starter Kits", 1 anúncio, 0 d;
  - **Business Profit Tools & Resources** (EUR): "Stop Guessing Your Cleaning Prices", 1 anúncio, 0,5 d.
- É a onda do "kit por ofício" chegando ao inglês.

### 2.6 Empreiteiro / arquiteto / construção
- **Planos y Diseños de Herrería** (1197011490158539, MXN): "MEGA PACK DE PLANOS HERRERIA Y CARPINTERIA", "PLANOS DETALLADOS CON MEDIDAS REALES". 7 anúncios, o mais antigo de 16/10 (**13,1 d**). É o "Pack Tesouro do Serralheiro" (BR, 130 d) chegando ao MX.
- **Obra en Orden** (1476846485501338, conta USD): "**Kit ObraEnOrden · $14.990 CLP**", "Presupuestos exactos, sin adivinar", "Flujo de caja de obra, semana a semana". 3 anúncios de hoje (0,2 d). Mira o Chile.
- Outros: "Documentos - SSO y Medio Ambiente" (PEN) com "Pack Ingeniería Civil"; MasterCursos (PEN) "Pack BIM por S/39"; Tutti (assistente de orçamento por WhatsApp, SaaS); a segunda página "Más seguridad" (MXN) também aparece em "presupuestos de obra".
- Inglês: "contractor templates" só trouxe coatandquote (USD, 23,9 d, produto desconhecido).
- Leitura: **TESTE na América Latina.** Fonte BR provada: Maleta do Vidraceiro 117 d, Pack Serralheiro 130 d, Marmorista 61–85 d, Fichas Visuais de Obra 20 d, Orça Obra Pro 57 d.

### 2.7 Aluguel de curta temporada (anfitrião)
- Inglês:
  - **BNB Tracker Pro** (258977330641466, USD; a página hoje se chama "Ultimate Life OS"): "Everything Your Airbnb Needs, $9" e "What $9 Gets Airbnb Hosts | 20-Page Welcome Book | 62 House Signs | 25+ Cleaning Checklists | 500+ Templates". O anúncio do kit de anfitrião está ativo desde 08/08/2026, **82,9 d**: **PROVADO em inglês/USD**.
  - Superhost Kit (EUR, "5-Star Guest Guide | All-In-One Host Kit"): 10 d.
- Itália: **Protocollo Zero Sanzioni** (EUR, "Affitti brevi in regola in 3 fasi", 1 anúncio, 6,2 d). Também GoHomes ("**Dal 2028 serve l'autorizzazione**" e "La burocrazia la gestiamo noi", gestão de imóveis), TheOwner.Club ("Affitti brevi, tutto in regola"), AmazHome e Studio TOP Lease (serviço). Leitura: **TESTE + PRAZO** (o gancho de norma existe nos anúncios; datas: VERIFICAR).
- Espanha e Portugal: não medi (o orçamento de busca acabou). VERIFICAR "registro único alquiler" (ES) e "alojamento local" (PT).

### 2.8 Pet (banho e tosa)
- Espanhol: só produto físico (tesouras, secadores, kit de máquina "$25.900, pagas al recibir" no Chile).
- Itália: só Studio Facile ("La toelettatura passo passo, con i disegni", ~1 d).
- Fonte BR: Kit Pet Shop com Agenda Recorrente (MktBoost, 6 d) e Combo Veterinária (19 d), nada provado.
- Leitura: **BRECHA sem prova de demanda.**

### 2.9 Cerimonialista / wedding planner
- Espanhol: Boucle Weddings (curso, EUR); BodaLab (SaaS para profissionais de casamento, EUR, **169,5 d**: há demanda B2B, mas é software); Archivos Digitales Express (MXN, sem título, **65,1 d**, produto desconhecido: VERIFICAR).
- Leitura: kit nativo de cerimonialista é **BRECHA**. O mais perto disso é "Prepara tu ceremonia sin improvisar" (Juliana Vargas), que é para pastor.

### 2.10 Fotógrafo
- Espanhol: só cursos e software (Arcadina EUR, Canon Academy, Entre Camaradas).
- Fonte BR provada: Kit Fotógrafo Blindado (Alex Bernardo, 134 d) e Biblioteca 250+ Presets (138 d).
- Leitura: **BRECHA no exterior** (sem vendedor de kit de contratos e precificação).

### 2.11 Transporte
- México ("Carta Porte transportistas"): só SaaS (Fletix com código FUNDADOR, Kordata com demo, Neuro Crow "Tu Carta Porte desde el pedimento"). Também Aprendia: "Seguridad vial con criterio técnico" (~0,5 d).
- Leitura: kit barato é **BRECHA**, mas o mercado é dominado por software. Baixa prioridade.

---

## 3. Ranking 0–10

Critérios (peso aproximado):
- prova no país, na moeda local, com 30+ d (40%);
- gancho de norma ou prazo (20%);
- encaixe com o modelo "kit de documentos + app por profissão" (20%);
- concorrência e espaço para entrar (20%).

| # | Nicho × país | Nota | Régua | Por quê | Próximo passo |
|---|---|---|---|---|---|
| 1 | **MX: seguridad e higiene / formatos STPS para o pequeno patrão** | **7,5** | PROVADO | Más seguridad e Seguridad e higiene y más com 361 d em MXN, rede abrindo páginas novas. Mesmo comprador da "Jornada México" (fila #5) | Abrir as páginas da rede no Mac (produto, preço, bumps). Desenhar "Maletín del Patrón": NOM-035 + registro de jornada + bitácoras + app de checklist STPS |
| 2 | **Simulado de inspeção sanitária: FR, RO, CZ, SK (+ IT, PT, ES)** | **6,5** | TESTE (corrida) | Kowalski aposta em 4 países (17 anúncios, 11,8 d). IT e ES sem kit nativo barato; PT com 1 sinal de 38 d (produto desconhecido). Reaproveita a Consultora | Re-checar Kowalski em 17–20/11 (marca de 30 d). Se passar, entrar em IT/PT primeiro (idiomas já no portfólio) |
| 3 | **CL: SST da PyME (DS 44 + Ley Karin + reglamento interno)** | **6,0** | TESTE + PRAZO | Vendedores locais em CLP começando hoje. Norma nova citada nos anúncios. Preço de referência de kit chileno: CLP 14.990 (Obra en Orden) | VERIFICAR a vigência do DS 44, as obrigações por porte e a multa. Re-checar Chileprevencion em 29/11 |
| 4 | **Kit do anfitrião de aluguel curto: EN (provado) / IT (prazo)** | **6,0** | PROVADO EN / TESTE IT | US$9 com 82,9 d em inglês. IT com gancho "autorização 2028" e CIN (VERIFICAR) e só 1 kit nativo (6 d) | Passar o EN para o agente "países de inglês". IT: confirmar a norma e testar "Valigetta dell'Host" a €19–27 |
| 5 | **CO: formatos SG-SST** | **5,5** | TESTE | Solunetpro 13,4 d em COP + página peruana mirando a CO. A Colômbia já está na fila (dentista e psicólogo): mesmo checkout em COP | Re-checar Solunetpro em 15/11 |
| 6 | **IT: kit DVR / sicurezza para pequeno negócio** | **5,5** | PROVADO fraco | Beatriz Guerra com 34,8 d (1 criativo, BRL). Demanda forte do lado do serviço (Fo Click 128 d, TCertifico 68 d). A Itália já é o país principal do usuário | Abrir a página da Beatriz Guerra. Avaliar o DVR como bump da Valigetta del Dentista |
| 7 | **LATAM: construção (planos de herrería, orçamento de obra)** | **5,0** | TESTE | Herrería MX 13 d, ObraEnOrden CL 0 d. Fonte BR provada (Serralheiro 130 d, Vidraceiro 117 d) | Re-checar a herrería MX em 15/11 |
| 8 | **FR: kit DUERP** | **5,0** | TESTE / quase BRECHA | Só a Marina cardozo (0,7 d). Mercado grande (todo empregador, VERIFICAR), sem kit nativo barato. Francês é idioma novo para o usuário | VERIFICAR a obrigação e a multa. Esperar 30 d de algum vendedor |
| 9 | **LATAM: ficha técnica e custo para restaurante** | **4,5** | TESTE | MX com 3–12 d. Fonte BR com 370 d | Re-checar em 15/11 |
| 10 | **EN: kit para empresa de limpeza** | **4,5** | TESTE | 3 páginas nasceram nesta semana | Re-checar em 29/11 |
| 11 | **ES (neutro): pastor / bosquejos** | **4,0** | TESTE lotado | 166 anúncios, nenhum vendedor medido com 30+ d, muito operador BR. Ticket baixo | Não entrar agora |
| 12 | **Multi-ofício ilustrado (modelo Studio Facile)** | **4,0** | TESTE spray | 920 anúncios de 1 dia. Se algum tema sobreviver, revela qual ofício vende | Re-checar em 28/11 quais temas seguem ativos |
| 13 | **IT/ES/LATAM: kit para banho e tosa** | **3,5** | BRECHA | Ninguém vende kit, mas não há prova de demanda | Só se sobrar fôlego |
| 14 | **ES/LATAM: kit de fotógrafo (contratos e precificação)** | **3,0** | BRECHA | Provado no BR (134–138 d), zero no exterior | Teste barato possível, sem prova |
| 15 | **ES/LATAM: kit de cerimonialista** | **3,0** | BRECHA | Só SaaS (BodaLab 169 d) e cursos. O produto do sinal MXN de 65 d é desconhecido | VERIFICAR Archivos Digitales Express |
| 16 | **MX: transporte / Carta Porte** | **2,5** | BRECHA dominada por SaaS | Só software | Descartar por ora |

---

## 4. Lista final de VERIFICAR

**Páginas de vendas** (abrir no navegador do Mac; aqui o WebFetch é bloqueado e o conector não dá link). Levantar preço, plataforma, conteúdo, bumps e garantia de:
1. **Más seguridad** (291789807354053 e 1308025092398670) e **Seguridad e higiene y más** (345679278628269, 101919158005402, 1101519659721154), além de **Formatos digitales pro** (1301518069721501). Confirmar se é tudo um operador só, qual é o produto e se vende só no MX.
2. **Andrei Kowalski** (1340912605769671): preço por país, moeda do checkout (EUR/RON/CZK?), plataforma, se é a Consultora clonada e quem é o operador.
3. **Studio Facile** (1232011766670582): confirmar se o site/checkout é "PictoStudy", o preço por livro e a plataforma.
4. **Beatriz Guerra** (907895875729587): produto exato do "Capisci il rischio" (DVR? formação de trabalhadores?) e preço.
5. **Solunetpro** (1118702291315648): preço em COP e o modelo "primero recibes, luego pagas".
6. **Cristiano Monteiro** (1187979577739554, PT, 38 d, sem título): o que vende.
7. **Archivos Digitales Express** (103894282759676, MXN, 65 d, sem título): o que vende.
8. **Chileprevencion.cl** (973357796093629): desde quando anuncia e preço de cada pacote em CLP.
9. **Obra en Orden** (1476846485501338): o título diz CLP 14.990; confirmar.
10. **BNB Tracker Pro / Ultimate Life OS** (258977330641466): o título diz US$9; confirmar e ver bumps.
11. **Planos y Diseños de Herrería** (1197011490158539), **Trazabilidad Express** (937213949485425), **Protocollo Zero Sanzioni** (1067984506407525), **Pro Trade Kits** (1384159991448444).

**Normas e mercado** (nada foi confirmado em fonte oficial nesta sessão):
12. MX: obrigações da NOM-035-STPS-2018 e das NOMs de seguridad e higiene para empresas de 1 a 15 trabalhadores; multas da STPS; número de patrões PyME (IMSS/INEGI).
13. CL: data de vigência e escopo do **DS 44** (substitui DS 40/DS 54?), a **Resolución 1117**, a Ley 21.643 (Ley Karin: protocolo obrigatório para todo empregador?), o reglamento interno obrigatório a partir de quantos trabalhadores, e as multas da Dirección del Trabajo.
14. CO: Decreto 1072/2015 + Res. 0312/2019 e o que mudou em 2025–2026 (os anúncios dizem "normas 2025-2026").
15. IT: D.Lgs. 81/2008 (DVR obrigatório desde o 1º trabalhador; sanções atualizadas); CIN para affitti brevi (vigência e multa); **"dal 2028 serve l'autorizzazione"** (qual lei? regional ou nacional?).
16. FR: obrigação do DUERP desde o 1º empregado, multa e atualização anual (Code du travail; service-public.fr).
17. RO/CZ/SK/FR: o que a fiscalização sanitária pede de um café/bistrô (DSVSA, KHS, RÚVZ, DDPP) e o número de estabelecimentos de restauração em cada país.
18. ES: Registro Único de Arrendamientos de curta duração e obrigações do anfitrião; ES/PT: kit de alojamento local (não medido).

**Re-checagens de data** (marca de 30 dias):
19. Andrei Kowalski: **17–20/11**.
20. Solunetpro e Planos y Diseños de Herrería: **15/11**.
21. Luz y Palabra (pastor US): **08/11**.
22. Chileprevencion, Pro Trade Kits/BizReady (limpeza EN), Studio Facile e Marina cardozo (DUERP): **28–29/11**.
23. Más seguridad: conferir se os anúncios de 361 d seguem ativos. Se caírem, a prova enfraquece.

---

## 5. Fontes

- **Biblioteca de Anúncios da Meta** via conector (`ads_library_search`, ACTIVE, 30/10/2026). Os page_ids estão nas tabelas acima; anúncio: `https://www.facebook.com/ads/library/?id=<id>`. Exemplos:
  - Andrei Kowalski [1115858381031924](https://www.facebook.com/ads/library/?id=1115858381031924) e o mais antigo, [1669387811372699](https://www.facebook.com/ads/library/?id=1669387811372699);
  - Más seguridad [1396762502069360](https://www.facebook.com/ads/library/?id=1396762502069360);
  - Beatriz Guerra [1627049982141608](https://www.facebook.com/ads/library/?id=1627049982141608);
  - Solunetpro [1724834118581193](https://www.facebook.com/ads/library/?id=1724834118581193);
  - BNB Tracker Pro [1780948740010543](https://www.facebook.com/ads/library/?id=1780948740010543);
  - Obra en Orden [1479743200886563](https://www.facebook.com/ads/library/?id=1479743200886563);
  - Chileprevencion [1647234700526883](https://www.facebook.com/ads/library/?id=1647234700526883);
  - Planos y Diseños de Herrería [2328758811226842](https://www.facebook.com/ads/library/?id=2328758811226842);
  - Fo Click DVR [2367718740689462](https://www.facebook.com/ads/library/?id=2367718740689462).
- **EscalaLow** (`dados/escalalow-ofertas-validadas.json` e `escalalow-ofertas-24-10.json`): fontes BR citadas (Maleta do Vidraceiro, Pack Tesouro do Serralheiro, Maleta do Marmorista, Kit Fotógrafo Blindado, Biblioteca Teológica, Planilha de Precificação).
- **Busca web:** as poucas buscas feitas não acharam o site de nenhum concorrente ("Andrei Kowalski", "PictoStudy", "Seguridad e higiene y más"). Depois o limite de buscas acabou. Nenhuma norma foi confirmada; ver a seção 4.
