# Novos nichos profissionais na Europa principal — v2 (30/10/2026)

Países: PL, IT, FR, ES, PT, DE, RO, NL. Profissões: salões/estética (sem injetáveis), HACCP/gastronomia, fisioterapia, fono/ABA, veterinária, educação, aluguel de temporada, contabilidade.

## Resumo em 6 linhas
1. **Só a educação tem vendedor nativo provado (30+ dias) nos países varridos:** Romênia (educadoras de jardim de infância: "Pentru Educatoare" e "Gradul didactic II Educatoare", 556 dias, RON) e Polônia (professores: "Sklep Kreatywny Nauczyciel", 39 dias, PLN).
2. **Fisio, estética, HACCP, fono, contabilidade e aluguel de temporada estão recebendo AGORA uma onda de clones estrangeiros** (contas USD/BRL), quase toda iniciada entre 09/10 e 29/10: FizjoTeczka (PL fisio, 2 d), Andrei Kowalski (FR/RO simulador de inspeção, ~12 d), Studio Facile (920 anúncios, manuais "com desenhos" em 10 idiomas, 0–1 d), Ultra Pack (fichas de estética no ES, 21 d), Jogos Terapêuticos (fono/psicopedagogia no FR, ≥20 d), Mia Parker (fichas de cosmetologia FR/DE/UK, ≥9 d), Kit Contable Práctico (ES, €23,90, 3 d), Chameleon Edge (Airbnb IT, €9, 3 d).
3. **Ninguém com 30+ dias** em fisio, estética, HACCP, fono, contabilidade ou aluguel de temporada, em nenhum dos 8 países. Os primeiros a fazer 30 dias: Ultra Pack ES (08/11), Jogos Terapêuticos FR (09/11), Andrei Kowalski (17/11).
4. **Veterinária = BRECHA total** (IT, ES, FR: só produto pet para consumidor; ninguém vende kit para o veterinário). Sem prova de demanda.
5. **Holanda e Alemanha** quase vazias de kit (DE: só "Portfolio-Vorlagen" Kita com 1 anúncio de 20 d; NL: só SaaS).
6. Bloqueios desta sessão: SearchAPI indisponível; **busca web esgotada** (limite de 200 buscas compartilhado pelos agentes) e **WebFetch sem rede** (eur-lex, boe.es e sites de vendedores dão ENOTFOUND). Por isso **nenhuma página de vendas foi aberta** e tamanhos/normas sem fonte ficaram **VERIFICAR** (uso fontes já confirmadas por relatórios irmãos quando existem, com a URL deles).

## Avisos de método (leia antes)
- A v1 de 29/10 (`3 - EU/pesquisas/novos-nichos-europa-2026-10-29.md`) **NÃO estava acessível** neste ambiente. Esta v2 foi feita do zero. Como lista de candidatos usei só o que está no prompt e nas notas do usuário (`notas/pesquisa-europa.md`, `notas/fila-ofertas.md`).
- **SearchAPI NÃO disponível** (sem chave aqui e créditos zerados até 08/11). Tudo medido com o conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 (epoch 1793318400) − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` da busca por page_id.
- **`page_ids` + `countries` funciona**: dá os dias reais do vendedor DENTRO do país (ex.: Ultra Pack tem 70 dias no geral, em PT-BR, mas só 20,8 dias no ES). Usei isso para separar "prova no país" de "prova em outro mercado".
- A busca devolve os anúncios mais novos primeiro (máx. 50). Em páginas com mais de 50 ativos (ou quando pedi amostra menor), o mais antigo pode não aparecer: escrevo "≥ X dias (amostra)".
- A busca por palavra do conector funciona como "OU" (palavras soltas trazem clínicas, fornecedores, Alibaba). Aspas melhoram a relevância, mas não viram frase exata.
- O conector não traz texto do anúncio nem URL de destino; só título do link, moeda da conta e datas. Moeda USD/BRL em página de idioma europeu = quase sempre operador brasileiro/estrangeiro. Preço só aparece quando está no título do anúncio.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.
- Fora do escopo: harmonização facial e injetáveis.

## 1. Varredura país × profissão (Biblioteca de Anúncios, só ativos, 30/10/2026)

Legenda: "kit" = produto digital low ticket de documentos/modelos/material para o profissional. "não varrido" = célula sem busca específica nesta sessão (falta de orçamento de chamadas); conta como VERIFICAR.

| País | Salões/estética | HACCP/gastronomia | Fisioterapia | Fono/ABA | Veterinária | Educação | Aluguel de temporada | Contabilidade |
|---|---|---|---|---|---|---|---|---|
| **IT** | só clínicas/fornecedores ("estetista" 1.940) | serviços/softwares (HACCP Smart 86 d, Norma HACCP, Facile Sicurezza 644 d = consultoria); infoproduto só Studio Facile "La cucina professionale spiegata con i disegni" (USD, 0 d) e Sb food consulting "Il manuale per chi guida un locale" (EUR, 16 d) | só clínicas ("fisioterapista" 2.410) | Sofia G (BRL, 6 anúncios, 0 d); Studio Facile "La logopedia con i disegni" (0 d) | BRECHA (só 1 anúncio de consumidor) | "PEI modelli" e "maestra materiale didattico" = 0 anúncios (ver relatório irmão de educação para PEI) | **Chameleon Edge "500+ modelli per il tuo Airbnb a 9 €" (USD, 12 anúncios, 3 d)**; GoHomes "Dal 2028 serve l'autorizzazione" (gestora) | não varrido (é a frente Termometro 85k já na fila do usuário) |
| **ES** | **Ultra Pack "Más de 50 Fichas para Estética" (USD, 5 anúncios no ES, 20,8 d)**; Método Piel Lisa (BRL, 2 d, relatório irmão) | Appticc (app "¿Pasarías una inspección hoy?"), Trazabilidad Express ("Obrador listo para Sanidad"), cursos grátis de manipulador | E-books & Inspiração "Domina las bases del Kinesiotaping" (BRL, 2 d) | Wumbox masterclasses (USD, LATAM); Udima (grado) | BRECHA ("veterinarios" 1.613 = produtos pet) | mercado maduro de oposiciones (Polaris, Sara Cabo, Diego Fuentes, OposicionesEduca); Tu Programación Didáctica (serviço "la hacemos por ti"); Landris.ai (IA) | só software/gestoras (Regi "parte de viajeros", Interhome, The Home Cake); nenhum kit | **Kit Contable Práctico "7 cuadernos + 6 bonos por 23,90 €" (USD, 13 anúncios, 2,8 d)**; resto = software Verifactu/gestorias |
| **PT** | **Susanarvilhena "Domina o Laser Díodo · de 47€ por 20€" (EUR nativa, 9 anúncios, 11,6 d)**; Nail Designer (escola) | Studio Facile "O HACCP com desenhos" (0 d); Novelty Nook "Guia HACCP Cantinas Escolares" (USD, 0 d) | não varrido | Caixa do Terapeuta (BRL, 141 anúncios no PT, ≥22,7 d) = terapeuta geral, fora das 8 | não varrido | não varrido | **Manual do Gestor de Alojamento Local (EUR nativo, 1 anúncio, 0 d)** | Studio Facile "A Contabilidade Ilustrada" (0 d) |
| **FR** | **Mia Parker "138 fiches de cosmétologie" (USD, ≥8,8 d)**; resto = software de agenda | **Andrei Kowalski "L'inspecteur de la DDPP est à la porte" (USD, 17 anúncios FR/RO/CZ/SK, 11,8 d segundo relatório irmão)** = Consultora traduzida; HACCP Simple (app); JDC SA plan d'hygiène | não varrido | **Jogos Terapêuticos (BRL, 35 anúncios no FR, ≥19,7 d)** "+50 activités psychopédagogiques dès 5 €" / "+30 exercices pour les troubles des sons" | BRECHA ("vétérinaire" 3.291 = produtos pet) | CRPE: academias com funil de live/RDV (Objectif CRPE 202 anúncios, Demain CRPE, Accès CRPE USD 0 d) | só conciergeries (Meilleur concierge) | não varrido (relatório irmão: faturação eletrônica 2026/2027) |
| **DE** | Mia Parker "Kosmetik-Atlas: 138 Wirkstoffe erklärt" (USD, ~1 d); Irina Kunkel Academy (curso) | "HACCP Vorlagen" = 0 | "Physiotherapeuten Praxis Vorlagen" = 0 → BRECHA | Tebeeo (plataforma), K2-Verlag (material físico, 139 d) | não varrido | **Miluja "480 Portfolio-Vorlagen (Waldtiere XL)" (EUR, 1 anúncio, 19,7 d)**; Verlag PRO Kita (e-book grátis, 184 d = editora); ErzieherIn (revista) | FeWo-Butler, Hendrik Kuhlmann (cursos), gestoras | não varrido (relatório irmão: E-Rechnung 2027/2028) |
| **PL** | "kosmetolog karta zabiegowa" = 0 → BRECHA | Studio Facile "HACCP w obrazkach" (0 d); Szkoła Jakości curso HACCP 597 zł | **FizjoTeczka "Wzory dokumentów dla gabinetu fizjoterapii" (USD, 16 anúncios, 1,8 d)** | SAREO (jogos logopédicos), gabinetes | não varrido | **Sklep Kreatywny Nauczyciel (PLN, 7 anúncios, 39,4 d) PROVADO**; EduPaczka, Rozwojowe Karty, Dar Dysleksji ("Wzór pisma… 200 stron PDF za 49 zł"), Marta Wójcik-Wiśniewska (curso Canva) | não varrido | KSeF: 1.010 anúncios, só software/cursos (mojaKsiegowa.ai, KSEFtoDrive 400 zł/ano) |
| **RO** | não varrido | Andrei Kowalski "Mâine vine controlul DSVSA" e Studio Digitale (relatório irmão resto-Europa: nenhum nativo 30+ d) | "kinetoterapeut" 65 = só clínicas → BRECHA | **Cupa Emotiilor "4 jocuri terapeutice la prețul unuia" (USD, 12+ anúncios, 3,0 d)** | não varrido | **Pentru Educatoare (RON, 3 anúncios, 556 d) e Gradul didactic II Educatoare (RON, 556 d) PROVADO**; Aricel Învățăcel (RON, 33,5 d) | não varrido | não varrido |
| **NL** | não varrido | só SaaS (Apprendo Horeca; relatório irmão: Quality Guard etc.) | "fysiotherapeut praktijk" 233 = anúncios de consumidor → BRECHA | não varrido | não varrido | Kleuterflits, Uitgeverij Eduforce (poucos anúncios) | não varrido | não varrido (relatório irmão: ZZP/DBA) |

## 2. Vendedores medidos por page_id (dias reais = 30/10/2026 − anúncio ativo mais antigo)

| Página (page_id) | País medido | Anúncios ativos | Moeda | Dias reais | Produto (título do anúncio) | Régua | 30 dias em |
|---|---|---|---|---|---|---|---|
| **Pentru Educatoare** (105297442237606) | todos (RO) | 3 | RON | **556** (desde 21/04/2025) | material para educadoras (títulos vazios) | **PROVADO** | — |
| **Gradul didactic II Educatoare** (109434637495032) | todos (RO) | ≥1 | RON | **556** | preparação para o grau didático II de educadoras (provável mesmo operador) | **PROVADO** | — |
| Aricel Învățăcel (1311784828686389) | RO | ≥1 | RON | 33,5 | material educadoras | PROVADO (fraco) | — |
| **Sklep Kreatywny Nauczyciel** (259563790572645) | todos (PL) | 7 | PLN | **39,4** (desde 20/09) | loja de materiais para professores | **PROVADO** | — |
| Verlag PRO Kita (338558226784) | DE | ≥1 | EUR | 184 | e-book grátis para Erzieher (isca de editora) | PROVADO como editora, não low ticket | — |
| Ultra Pack (780532768486149) | geral / **ES** | 16 / 5 no ES | USD | 70 geral (PT-BR) / **20,8 no ES** (desde 09/10) | "Más de 50 Fichas para Estética", "Tu Clínica Más Profesional", "Ficha de Depilación Láser", "+200 Reels de estética" | TESTE no ES (espanhol neutro) | 08/11 |
| Jogos Terapêuticos (764728496715153) | **FR** | 35 no FR | BRL | **≥19,7** (amostra 30/35, desde 10/10) | "Plus de 50 activités psychopédagogiques · dès 5 €", "+30 exercices pour les troubles des sons" | TESTE | 09/11 |
| Miluja (114220420764413) | todos (DE) | 1 | EUR | 19,7 | "480 Portfolio-Vorlagen (Waldtiere XL)" | TESTE (nativo) | 09/11 |
| Infolabs Digital (786768801191850) | todos | 35 | USD | 19,3 | perito avaliador (IT/LATAM/JP), fora do escopo | TESTE | 09/11 |
| Caixa do Terapeuta (469875186209972) | **PT** | 141 no PT | BRL | ≥22,7 (amostra) | "+200 Ferramentas Práticas", "Kit Completo" (terapeuta) | TESTE forte (fora das 8 profissões) | 06/11 |
| Andrei Kowalski (1340912605769671) | FR/RO/CZ/SK | 17 | USD | 11,8 (medição do relatório irmão `oficios-negocios-v2.md`) | "L'inspecteur de la DDPP est à la porte", "Mâine vine controlul DSVSA" | TESTE (Consultora traduzida) | 17/11 |
| Susanarvilhena (571358532735278) | todos (PT) | 9 | EUR | 11,6 | "Domina o Laser Díodo · de 47€ por 20€" | TESTE (nativa PT) | 17/11 |
| Mia Parker (1108957155642392) | todos | 25 | USD | ≥8,8 (amostra 15/25) | "138 fiches de cosmétologie" (FR), "Kosmetik-Atlas" (DE), "The Skincare Atlas — £29" (UK) | TESTE multi-país | 20/11 |
| Chameleon Edge (1184706708060086) | todos (IT) | 12 | USD | 3,2 | "500+ modelli per il tuo Airbnb a 9 €" | TESTE | 25/11 |
| Kit Contable Práctico (1411204478738237) | todos (ES) | 13 | USD | 2,8 | "7 cuadernos + 6 bonos por 23,90 €" | TESTE | 26/11 |
| Cupa Emotiilor (1397039396826105) | todos (RO) | 12+ | USD | 3,0 | "4 jocuri terapeutice la prețul unuia" | TESTE | 26/11 |
| E-books & Inspiração (433476344159696) | **ES** | 10 no ES | BRL | 2,3 | "Domina las bases del Kinesiotaping", "Hair Stroke Profesional – US$ 9,90" | TESTE | 26/11 |
| **FizjoTeczka** (716677868202484) | todos (PL) | 16 | USD | **1,8** (desde 28/10) | "Wzory dokumentów dla gabinetu fizjoterapii" | TESTE (clone do modelo kit-por-profissão em PL) | 27/11 |
| Studio Facile (1232011766670582) | todos | 920 | USD | 0–1 nos 50 mais novos; mais antigo não alcançado | manuais "X com desenhos" em IT/PT/PL/CZ/DA/EL: HACCP, logopedia, contabilidade, nutrição, unhas, primeiros socorros, solda, bomba de calor, fotovoltaica, tosa | TESTE em massa | — |
| Sofia G (1215203431679518) | todos (IT) | 6 | BRL | 0 | "Valutazione dell'utente (4,89 ⭐)" (apareceu na busca "logopedista") | TESTE | — |
| Manual do Gestor de Alojamento Local (1234895269709062) | todos (PT) | 1 | EUR | 0 | "Manual do Gestor de AL" | TESTE (nativo) | — |
| Accès CRPE (1154800614394241) | todos (FR) | 1 | USD | 0 | sem título | TESTE | — |
| K2-Verlag (139567646066162) | todos | 33 | EUR | 139 | material físico (Lernkarten, CHF) | fora (produto físico) | — |

Leitura: a moeda USD/BRL em quase todos os TESTE confirma que é o mesmo movimento de operadores brasileiros que o usuário já viu em dentista/psicólogo, agora espalhado para fisio (PL), estética (ES/FR/DE), HACCP (FR/RO/IT/PT/PL), fono (FR/IT/RO), contabilidade (ES) e Airbnb (IT). Quase tudo nasceu entre 09/10 e 29/10.

## 3. Páginas de vendas

**Nenhuma página de vendas pôde ser aberta nesta sessão.** O conector Meta não devolve a URL de destino; a busca web esgotou o limite do turno (200 buscas compartilhadas entre agentes); e o WebFetch não tem rede (`eur-lex.europa.eu`, `www.boe.es` e `kreatywnynauczyciel.pl` deram ENOTFOUND; os relatórios irmãos relatam o mesmo para hotmart, kiwify, facebook etc.).

O que se sabe de preço vem só do título do anúncio:
- Chameleon Edge (IT): **€9** por "500+ modelli per il tuo Airbnb".
- Kit Contable Práctico (ES): **€23,90** por "7 cuadernos + 6 bonos".
- Susanarvilhena (PT): **€20** (de €47) por curso/guia de laser díodo.
- Jogos Terapêuticos (FR): **a partir de €5** por "+50 activités psychopédagogiques".
- E-books & Inspiração (ES): **US$ 9,90** (Hair Stroke).
- Mia Parker (UK): **£29** ("The Skincare Atlas").
- Dar Dysleksji (PL): **49 zł** por PDF de 200 páginas.
- KSEFtoDrive (PL, software): 400 zł/ano.
- Szkoła Jakości (PL, curso HACCP): 597 zł.

Plataforma, conteúdo, order bumps e garantia de todos: **VERIFICAR** (abrir pelo navegador do Mac, a partir dos `ad_snapshot_url` / page_id acima).

## 4. Tamanho de mercado e gancho legal

Não consegui confirmar nada novo com fonte oficial nesta sessão (busca e rede bloqueadas). A tabela separa:
- **(a)** fatos já confirmados por relatório irmão, com a URL que ele citou (não reabri);
- **(b)** o que sei de antes, que é só pista e está marcado **VERIFICAR**.

| Nicho / país | Tamanho | Gancho legal / PRAZO | Status |
|---|---|---|---|
| Educação PL (professores) | VERIFICAR (nº de nauczyciele) | **(a)** Reforma "Kompas Jutra": nova podstawa programowa desde 01/09/2026 na pré-escola e nas classes I e IV; desde 01/09/2027 na classe I das ponadpodstawowe. Fonte via `educacao-inclusao-v2.md`: https://www.gov.pl/web/edukacja/rada-ministrow-przyjela-projekt-ustawy-o-zmianie-ustawy---prawo-oswiatowe-oraz-niektorych-innych-ustaw . **(a)** Ocena funkcjonalna obrigatória desde 01/09/2026 (Dz.U. 2026 poz. 428), mesma fonte do irmão. | PRAZO confirmado (via irmão) |
| Educação RO (educatoare) | VERIFICAR (nº de educadoras no pré-escolar, INS) | **(b)** "Gradul didactic II" é etapa de carreira com inspeção e portfólio; existe "Curriculum pentru educație timpurie" (2019). Prazos de 2027: VERIFICAR | sem fonte |
| Educação DE (Kita) | VERIFICAR (pessoal pedagógico em Kitas, Destatis) | **(b)** Bildungspläne dos Länder pedem observação e documentação (Portfolio/Beobachtungsbogen); sem prazo novo conhecido. VERIFICAR | sem fonte |
| Educação ES (oposiciones) | VERIFICAR | **(a)** Calendário 2027 por comunidade (Baleares 17/04/2027 etc.), janela de compra nov/2026–mar/2027 (via `educacao-inclusao-v2.md`) | PRAZO (via irmão) |
| Educação FR (CRPE) | VERIFICAR | **(a)** Inscrições CRPE 2027 até 25/11/2026; escritas 30–31/03/2027 (digiSchool, conferir em devenirenseignant.gouv.fr; via `educacao-inclusao-v2.md`) | PRAZO parcial |
| Educação IT (sostegno) | **(a)** >261 mil insegnanti di sostegno, ~57 mil sem especialização (ISTAT a.s. 2024/25, via irmão: https://www.istat.it/comunicato-stampa/linclusione-scolastica-degli-alunni-con-disabilita-anno-scolastico-2024-2025/) | **(a)** Novo calendário de PEI (definitivo até 15/10 para novos casos), via irmão | PRAZO (via irmão) |
| Fisio PL | VERIFICAR (nº de fisioterapeutas com direito de exercício, KIF) | **(b)** Dokumentacja medyczna obrigatória também para fisioterapeutas (ustawa o zawodzie fizjoterapeuty + rozporządzenie MZ sobre documentação). Data nova: nenhuma conhecida. VERIFICAR | sem fonte |
| Estética ES | VERIFICAR (nº de centros de estética/peluquerías) | **(b)** Consentimento informado + RGPD/LOPDGDD para fichas de clientes; sem prazo novo conhecido. VERIFICAR | sem fonte |
| HACCP FR (restauração) | VERIFICAR (nº de restaurantes) | **(b)** Formação em higiene alimentar obrigatória para restauração comercial (14 h) desde 2012, controle pela DDPP. VERIFICAR | sem fonte |
| HACCP ES | VERIFICAR | **(a)** Lei 1/2025 desperdício alimentar: obrigações desde abr/2026, plano de prevenção obrigatório (exceto micro); multas VERIFICAR (via `prazos-de-norma-2026-10-30.md`) | PRAZO (via irmão, VERIFICAR) |
| HACCP + estética + fisio IT (todo empregador) | — | **(a)** Accordo Stato-Regioni 59/CSR (GU 24/05/2025): curso base de 16 h para todo datore di lavoro até ~23–24/05/2027 (via `prazos-de-norma-2026-10-30.md`) | PRAZO (via irmão) |
| Fono FR | VERIFICAR (nº de orthophonistes, DREES) | sem gancho de data conhecido | sem fonte |
| Fono ES / IT | **(a)** ES ~10.900 logopedas colegiados (INE 2021; https://ine.es/dyngs/Prensa/EPSC2025.pdf); IT ~15 mil logopedisti (https://www.quotidianosanita.it/…, sem data). Ambos via `saude-geral-v2.md` | sem gancho de data | tamanho via irmão |
| Aluguel de temporada (UE) | VERIFICAR (nº de anfitriões por país) | **(b)** Regulamento (UE) 2024/1028 (dados de aluguel de curta duração; número de registro exibido nas plataformas): aplicação a partir de **20/05/2026**. VERIFICAR | sem fonte (eur-lex bloqueado) |
| Aluguel ES | VERIFICAR | **(b)** RD 1312/2024: Registro Único de Arrendamientos / ventanilla única digital obrigatória desde 01/07/2025; parte de viajeros (RD 933/2021) desde dez/2024. VERIFICAR | sem fonte (boe.es bloqueado) |
| Aluguel IT | VERIFICAR | **(b)** CIN (codice identificativo nazionale) obrigatório desde 01/01/2025, com multa. Gancho "Dal 2028 serve l'autorizzazione" visto em anúncio da GoHomes: VERIFICAR | sem fonte |
| Aluguel PT | VERIFICAR | **(b)** Regime do Alojamento Local alterado em 2024 (DL 76/2024). VERIFICAR | sem fonte |
| Contabilidade ES | — | **(a)** Verifactu (RDL 15/2025): sociedades 01/01/2027, autónomos 01/07/2027 (via irmão; convalidação VERIFICAR) | PRAZO (via irmão) |
| Contabilidade PL / FR / DE | — | **(a)** KSeF micro 01/01/2027 (possível adiamento); FR faturação eletrônica: emissão PME/micro 01/09/2027; DE E-Rechnung: emissão 2027 (>€800 mil) / 2028 todos (via irmão) | PRAZO, mas mercado de software (não kit) |
| Veterinária (todos) | VERIFICAR | nenhum gancho levantado | BRECHA sem demanda provada |

## 5. Ranking 0–10 (régua: prova no país + tamanho + prazo + encaixe com "kit de documentos + app" − barreiras)

| # | Nicho × país | Nota | Por quê | Status |
|---|---|---|---|---|
| 1 | **Professores PL**: kit "rozkład/plan zgodny z nową podstawą (Kompas Jutra)" + fichas | **7,5** | Mercado nativo provado (Kreatywny Nauczyciel 39 d; notas do usuário: Pani Andzia ~225 d e Centrum Pedagogiczne ~150 d no nicho escolar); reforma com data confirmada (01/09/2026 e 01/09/2027); ninguém com app. Barreiras: polonês, PLN/BLIK, compra de escola. | PROVADO + PRAZO |
| 2 | **Educadoras RO**: kit "planificare + portofoliu + gradul didactic II" | **7,0** | Dois anunciantes nativos com 556 d (um anúncio rodando há 1,5 ano é prova forte); nenhum operador BR ainda. Barreiras: RON, romeno, ticket baixo; tamanho e prazos VERIFICAR. | PROVADO |
| 3 | **Estética ES**: fichas + consentimentos + app | **6,0** | Onda BR começou (Ultra Pack 20,8 d no ES, Piel Lisa, E-books & Inspiração); nenhum kit em euro nativo. Decide em 08/11: se Ultra Pack seguir ativo no ES, vira PROVADO (espanhol neutro). Gancho legal VERIFICAR. | TESTE |
| 4 | **Simulador de inspeção sanitária FR (DDPP) / RO (DSVSA)** = Consultora traduzida | **6,0** | O concorrente (Andrei Kowalski) já faz exatamente isso em FR/RO/CZ/SK desde 18/10; Studio Facile testa HACCP ilustrado em 6+ idiomas. Mostra que operadores acreditam no nicho, mas ninguém tem 30 d. Re-checar 17/11. | TESTE |
| 5 | **Fono/psicopedagogia FR**: atividades + fichas | **6,0** | Jogos Terapêuticos com 35 anúncios no FR e ≥19,7 d a partir de €5. Faz 30 d em 09/11. Tamanho (orthophonistes) VERIFICAR. | TESTE forte |
| 6 | **Fisio PL**: "teczka" de documentos do gabinete | **5,5** | Concorrente começou em 28/10 (FizjoTeczka, 16 anúncios, USD): o operador acredita no nicho, mas é só sinal. Nenhum nativo. Re-checar 27/11. | TESTE |
| 7 | **Oposiciones docentes ES** (programación didáctica / simulador) | **5,5** | Mercado grande e maduro, mas dominado por academias e serviços; janela nov/2026–mar/2027. | PRAZO (concorrido) |
| 8 | **Aluguel de temporada ES/IT/PT** (kit de conformidade: registro, parte de viajeros, CIN, contrato, check-in) | **5,0** | Regulamento UE 2024/1028 e registros nacionais (VERIFICAR); concorrentes só software/gestoras + 2 testes (Chameleon Edge IT €9, Manual do Gestor AL PT). ES sem nenhum kit. | BRECHA/TESTE + PRAZO (VERIFICAR) |
| 9 | **Kita DE** (Portfolio/Beobachtung) | **5,0** | Miluja 19,7 d com 1 anúncio; PRO Kita é editora com isca grátis (184 d). Cultura "kostenlos". Já era o nº 1 DE de 28/10. | TESTE |
| 10 | **Estética FR/DE/PT** (fichas de cosmetologia) | **4,5** | Mia Parker (FR/DE/UK, ≥8,8 d) e Susanarvilhena (PT, €20, 11,6 d): só testes. | TESTE |
| 11 | **Contabilidade/autónomos ES** | **4,5** | Kit Contable Práctico (€23,90, 2,8 d); Verifactu tem prazo (2027), mas se resolve com software. | TESTE + PRAZO |
| 12 | **Fono IT** (logopedisti ~15 mil) | **4,0** | Só Sofia G (BRL, 0 d) e Studio Facile (0 d). | TESTE fraco |
| 13 | **Fisio IT/ES/PT/FR/DE/NL/RO** | **3,5** | Ninguém vende kit (DE "Praxis Vorlagen" = 0; RO/NL só clínicas). BRECHA sem prova de demanda. | BRECHA |
| 14 | **Salão/estética PL/RO/NL** | **3,0** | "kosmetolog karta zabiegowa" = 0; RO/NL não varridos. | BRECHA |
| 15 | **Veterinária (IT/ES/FR)** | **3,0** | Ninguém vende para o veterinário; só produtos pet de consumidor. | BRECHA sem demanda |
| 16 | **Contabilidade PL (KSeF) / FR / DE** | **2,5** | 1.010 anúncios de KSeF, todos software/curso; não é terreno de kit. | saturado por software |
| 17 | **Holanda (todas)** | **2,0** | Só SaaS e poucos anúncios de material escolar. | vazio |

**Leitura para o usuário:** a única prova "dura" fora de dentista/psicólogo está em **educação no Leste** (PL e RO). Nos demais nichos, o sinal é de concorrentes BR **começando agora** (outubro). É a mesma situação que o usuário viu em dentista: vale pré-montar o produto e decidir pelas datas de re-checagem abaixo.

## 6. Calendário de re-checagem (quando um TESTE vira PROVADO)

| Data | Checar (por page_id + país) | Se ainda ativo |
|---|---|---|
| 06/11 | Caixa do Terapeuta no PT (469875186209972) | prova de que kit de terapeuta BR vende em PT |
| 08/11 | Ultra Pack no ES (780532768486149) | Estética ES sobe para PROVADO (espanhol neutro) |
| 09/11 | Jogos Terapêuticos no FR (764728496715153); Miluja DE (114220420764413) | Fono FR e Kita DE sobem |
| 17/11 | Andrei Kowalski FR/RO (1340912605769671); Susanarvilhena PT (571358532735278) | Simulador de inspeção FR/RO e estética PT sobem |
| 20/11 | Mia Parker (1108957155642392) | Estética FR/DE |
| 25–27/11 | Chameleon Edge IT, Kit Contable ES, Cupa Emotiilor RO, E-books & Inspiração ES, **FizjoTeczka PL** | Airbnb IT, contabilidade ES, jogos terapêuticos RO, fisio PL |

## 7. Lista final de VERIFICAR
1. **Páginas de vendas** de todos os vendedores da seção 2: preço, plataforma, conteúdo, bumps e garantia. Nada foi aberto (sem rede). Prioridade: FizjoTeczka, Ultra Pack, Jogos Terapêuticos, Andrei Kowalski, Pentru Educatoare, Kreatywny Nauczyciel, Chameleon Edge, Kit Contable Práctico.
2. **Idade real da página Studio Facile** (920 anúncios; o conector só mostra os 50 mais novos) e de Caixa do Terapeuta (141 no PT), Jogos Terapêuticos (5 anúncios não vistos), Mia Parker (10 não vistos). Usar o SearchAPI depois de 08/11 ou o navegador.
3. **Regulamento (UE) 2024/1028**: aplicação em 20/05/2026 e obrigação de número de registro (eur-lex bloqueado).
4. **ES RD 1312/2024** (Registro Único, 01/07/2025) e **RD 933/2021** (parte de viajeros): datas e multas (boe.es bloqueado).
5. **IT CIN** (multas) e o gancho "Dal 2028 serve l'autorizzazione" (anúncio GoHomes).
6. **PT Alojamento Local**: regime atual (DL 76/2024) e obrigações do gestor.
7. **FR formação em higiene alimentar** (14 h, restauração comercial) e nº de restaurantes; **FR nº de orthophonistes** (DREES).
8. **PL nº de fisioterapeutas (KIF)** e regra de documentação do gabinete; **PL nº de professores**.
9. **RO nº de educatoare** (INS) e regras do "gradul didactic II" / planificação (MEC).
10. **DE nº de profissionais em Kitas** (Destatis) e se algum Land tem prazo novo de documentação.
11. **ES nº de centros de estética** e base legal das fichas/consentimentos (LOPDGDD).
12. **ES Verifactu (RDL 15/2025)**: convalidação e datas finais (o irmão também marcou VERIFICAR).
13. Se **Andrei Kowalski / Studio Facile / Marina cardozo** são o mesmo operador e se algum deles é do próprio usuário (a nota de 28/10 já perguntava isso de consultorioemdia.shop).
14. Células "não varrido" da seção 1 (PT fisio/vet/educação; FR fisio/contabilidade; DE vet/contabilidade; PL vet/aluguel; RO estética/vet/aluguel/contabilidade; NL quase tudo).

## 8. Diferenças em relação à v1
A v1 não estava acessível, então a comparação se baseia só no que o prompt diz dela: "feita só com o conector Meta; sem preço, sem texto de anúncio, tamanhos e normas sem fonte".
- **Medição por país (novo):** mostra se a prova é no país ou em outro mercado. Ex.: Ultra Pack tem 70 d no geral, mas só 20,8 d no ES.
- **Preço:** apareceu para 8 vendedores, via título do anúncio (€5 a €29, 49 zł).
- **Onda de clones BR em outubro:** fisio PL, estética ES/FR/DE, HACCP FR/RO/IT/PT/PL, fono FR/IT/RO, contabilidade ES, Airbnb IT. Não há sinal de que estivesse na v1.
- **Provados nativos em educação:** RO educatoare (556 d) e PL professores (39 d).
- **Continua igual à limitação da v1:** normas e tamanhos sem fonte nova, desta vez por bloqueio de rede e de busca. Usei as fontes que os relatórios irmãos confirmaram.
