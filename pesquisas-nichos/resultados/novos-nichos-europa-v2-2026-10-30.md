# Novos nichos profissionais na Europa principal — v2 (30/10/2026)

Países: PL, IT, FR, ES, PT, DE, RO, NL. Profissões: salões/estética (sem injetáveis), HACCP/gastronomia, fisioterapia, fono/ABA, veterinária, educação, aluguel de temporada, contabilidade.

## Avisos de método (leia antes)
- A v1 de 29/10 (`3 - EU/pesquisas/novos-nichos-europa-2026-10-29.md`) NÃO estava acessível neste ambiente. Esta v2 foi feita do zero, usando como lista de candidatos só o que está no prompt e nas notas do usuário (`notas/pesquisa-europa.md`, `notas/fila-ofertas.md`).
- SearchAPI NÃO disponível (sem chave aqui e créditos zerados até 08/11). Tudo medido com o conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` na busca por page_id.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.
- O que não foi confirmado com fonte está marcado **VERIFICAR**.

## Status
(em andamento — arquivo gravado aos poucos; seções 1–2 parciais gravadas)

## Achado de método importante
- A busca por palavra do conector Meta funciona como "OU" (palavras soltas trazem muito ruído: clínicas, fornecedores, Alibaba). Aspas melhoram, mas não viram frase exata.
- **`page_ids` + `countries` funciona**: dá os dias reais do vendedor DENTRO do país (ex.: Ultra Pack tem 70 dias no geral, mas só 21 dias no ES). Usei isso para separar "prova no país" de "prova em outro mercado".
- A busca devolve os anúncios mais novos primeiro (máx. 50). Em páginas com mais de 50 anúncios ativos o mais antigo pode não aparecer; nesses casos escrevo "≥ X dias (amostra)".
- O conector não traz o texto do anúncio nem a URL de destino, só o título do link, a moeda e as datas. Moeda USD/BRL numa página em idioma europeu = quase sempre operador brasileiro/estrangeiro.

## 1. Varredura país × profissão (Biblioteca de Anúncios, só ativos, 30/10/2026)

Legenda: nº = estimated_total_count da busca (inclui ruído). "Kit" = produto digital low ticket de documentos/modelos/material para o profissional.

| País | Salões/estética | HACCP/gastronomia | Fisioterapia | Fono/ABA | Veterinária | Educação | Aluguel de temporada | Contabilidade |
|---|---|---|---|---|---|---|---|---|
| IT | só clínicas/fornecedores (1.940) | serviços e softwares (HACCP Smart, Norma HACCP, Facile Sicurezza 644d = consultoria); infoproduto só Studio Facile (0d) e Sb food consulting (16d) | só clínicas (2.410) | Sofia G (BRL, 0d), Studio Facile "logopedia con i disegni" (0d) | (pendente) | (pendente) | **Chameleon Edge "500+ modelli per il tuo Airbnb a 9 €" (USD, 3d)** | (pendente) |
| ES | **Ultra Pack "+50 fichas estética" (USD, 21d no ES)** | Appticc (app APPCC), Trazabilidad Express (0–2d), cursos grátis | E-books & Inspiração kinesiotaping (BRL, 2d) | Wumbox masterclasses (USD, LATAM) | (pendente) | mercado maduro de oposiciones (Polaris, Sara Cabo, Diego Fuentes) + Tu Programación Didáctica (serviço) + Landris.ai (IA) | Regi (app parte de viajeros), Interhome; nenhum kit | (pendente) |
| PT | Susanarvilhena "Laser Díodo de 47€ por 20€" (EUR nativa, 12d) | Studio Facile (0d), Novelty Nook "HACCP cantinas escolares" (USD, 0d) | (pendente) | Caixa do Terapeuta (BRL, 141 anúncios no PT, ≥23d) — terapeuta geral | (pendente) | (pendente) | (pendente) | Studio Facile "Contabilidade Ilustrada" (0d) |
| FR | (pendente) | **Andrei Kowalski "L'inspecteur de la DDPP est à la porte" (USD, 0d)** = simulador de inspeção tipo Consultora; HACCP Simple (app) | (pendente) | **Jogos Terapêuticos (BRL, 35 anúncios no FR, ≥20d)** "+50 activités psychopédagogiques dès 5 €" / "+30 exercices troubles des sons" | (pendente) | (pendente) | só conciergeries | (pendente) |
| DE | Irina Kunkel Academy (curso) | "HACCP Vorlagen" = 0 | (pendente) | Tebeeo (plataforma), K2-Verlag (material físico) | (pendente) | Miluja "480 Portfolio-Vorlagen" Kita (EUR, 1 anúncio, 20d); Verlag PRO Kita (184d, e-book grátis = editora) | FeWo-Butler e Hendrik Kuhlmann (cursos), gestoras | (pendente) |
| PL | "kosmetolog karta zabiegowa" = 0 | Studio Facile (0d); Szkoła Jakości curso 597 zł | **FizjoTeczka "Wzory dokumentów dla gabinetu fizjoterapii" (USD, 16 anúncios, 2d)** | SAREO (jogos), gabinetes | (pendente) | **Sklep Kreatywny Nauczyciel (PLN, 39d) PROVADO**; EduPaczka, Rozwojowe Karty, Dar Dysleksji (49 zł) | (pendente) | KSeF: 1.010 anúncios, só software/cursos |
| RO | (pendente) | (pendente) | só clínicas (65) | Cupa Emotiilor "4 jocuri terapeutice" (USD, 3d) | (pendente) | **Pentru Educatoare (RON, 556d) e Gradul didactic II Educatoare (556d) PROVADO**; Aricel Învățăcel (33d) | (pendente) | (pendente) |
| NL | (pendente) | Apprendo Horeca (software) | (pendente) | (pendente) | (pendente) | Kleuterflits, Uitgeverij Eduforce (poucos anúncios) | (pendente) | (pendente) |

## 2. Vendedores medidos por page_id (dias reais = 30/10/2026 − anúncio ativo mais antigo)

| Página (page_id) | País medido | Nº anúncios ativos | Moeda | Dias reais | Produto (título do anúncio) | Régua |
|---|---|---|---|---|---|---|
| Studio Facile (1232011766670582) | todos | 920 | USD | 0–1 nos 50 mais novos; mais antigo não alcançado | manuais "X com desenhos" em IT/PT/PL/CZ/DA/EL: HACCP, logopedia, contabilidade, nutrição, unhas, primeiros socorros, solda, bomba de calor, fotovoltaica, tosa | TESTE em massa (operador estrangeiro testando dezenas de nichos×idiomas) |
| Sofia G (1215203431679518) | todos | 6 | BRL | 0 | IT ("Valutazione dell'utente 4,89") | TESTE |
| Chameleon Edge (1184706708060086) | todos (IT) | 12 | USD | 3 | "500+ modelli per il tuo Airbnb a 9 €" | TESTE |
| Infolabs Digital (786768801191850) | todos | 35 | USD | 19 | perito avaliador IT/LATAM/JP (fora do escopo) | TESTE |
| Ultra Pack (780532768486149) | geral / ES | 16 / 5 no ES | USD | 70 geral (PT-BR) / **21 no ES** | "Más de 50 Fichas para Estética", "Tu Clínica Más Profesional", "Ficha Depilación Láser", "+200 Reels estética" | TESTE no ES (espanhol neutro) |
| E-books & Inspiração (433476344159696) | ES | 10 no ES | BRL | 2 | kinesiotaping, Hair Stroke US$ 9,90 | TESTE |
| Susanarvilhena (571358532735278) | todos (PT) | 9 | EUR | 12 | "Domina o Laser Díodo · de 47€ por 20€" | TESTE (nativa PT) |
| Caixa do Terapeuta (469875186209972) | PT | 141 no PT | BRL | ≥23 (amostra) | "+200 Ferramentas Práticas", "Kit Completo" | TESTE→quase PROVADO, mas fora das 8 profissões |
| Jogos Terapêuticos (764728496715153) | FR | 35 no FR | BRL | ≥20 (amostra 30/35) | "+50 activités psychopédagogiques dès 5 €", "+30 exercices troubles des sons" | TESTE |
| Miluja (114220420764413) | todos (DE) | 1 | EUR | 20 | "480 Portfolio-Vorlagen (Waldtiere XL)" Kita | TESTE |
| FizjoTeczka (716677868202484) | todos (PL) | 16 | USD | **2** | "Wzory dokumentów dla gabinetu fizjoterapii" | TESTE (clone do modelo kit-por-profissão em PL) |
| Sklep Kreatywny Nauczyciel (259563790572645) | todos (PL) | 7 | PLN | **39** | loja de material para professores | **PROVADO** |
| Cupa Emotiilor (1397039396826105) | todos (RO) | 12+ | USD | 3 | "4 jocuri terapeutice la prețul unuia" | TESTE |
| Pentru Educatoare (105297442237606) | todos (RO) | 3 | RON | **556** | material para educadoras (jardim de infância) | **PROVADO** |
| Gradul didactic II Educatoare (109434637495032) | todos (RO) | ≥1 | RON | **556** | material para progressão de carreira de educadoras | **PROVADO** |
| Aricel Învățăcel (1311784828686389) | RO | ≥1 | RON | 33 | material educadoras | PROVADO (fraco) |
| Verlag PRO Kita (338558226784) | DE | ≥1 | EUR | 184 | e-book grátis para Erzieher (editora, isca) | PROVADO como editora, não low ticket |
| K2-Verlag (139567646066162) | todos | 33 | EUR | 139 | material físico (Lernkarten, CHF) | fora (produto físico) |

## 3. Páginas de vendas abertas

## 4. Tamanho de mercado e gancho legal (com fonte)

## 5. Ranking 0–10

## 6. Lista final de VERIFICAR
