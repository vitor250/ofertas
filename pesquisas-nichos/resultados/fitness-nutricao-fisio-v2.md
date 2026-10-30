# Fitness, nutrição e fisioterapia por país (v2, 30/10/2026)

> Status: EM ANDAMENTO (arquivo gravado aos poucos).

## Avisos de método
- A v1 de 29/10 (`pesquisas-nichos-2026-10-29/fitness-nutricao-fisio.md`) NÃO estava acessível neste ambiente (container na nuvem, sem o Desktop). Usei só a lista de VERIFICAR escrita no prompt e as notas do usuário.
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). Toda medição de anúncios foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
- Régua: PROVADO = anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.

## 1. Base Brasil (o que já vende aqui, EscalaLow 24/10)
(preenchendo)

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

### 2.7 O operador multipaís (achado principal da v2)

Os mesmos produtos aparecem com nome local e o mesmo número de itens em vários idiomas, todos em USD:
- Pilates "100 aulas + 500 exercícios": Centerline Pilates PL (14 d, 40 anúncios) → Centerline Pilates Portugal (0,7 d) → Mesa de Luz ES (0,8 d, "100 clases + 500 ejercicios") → Stundenfertig DE (1,9 d, "104 Stunden + 410 Übungen").
- Idosos "1.320 atividades": GeriActive Portugal e GeriActive Polska (ambos <1 d). Geriactiva em espanhol (143 anúncios, "+3000 profesionales") parece ser a matriz, mas os dias reais dela ficaram fora da janela do conector (VERIFICAR).
- O estilo de copy ("lista para dar", "en 1 minuto", "pagas una vez") se repete em Clara Ríos, Mi Colega T.O, Pilates con Método, Seduta Pronta, Palestra Mentale. Pode ser o mesmo grupo ou o mesmo "molde" de IA. Não dá para afirmar o dono (VERIFICAR).
Implicação: pilates e idosos estão sendo testados AGORA em ES/PT/PL/DE/IT/FR por um concorrente com escala de criativos. Ninguém além dele passou de 30 dias nesses países, exceto Recursos Digitales (espanhol, 57 d) e Geriactiva.

## 3. Concorrentes da v1 (VERIFICAR conteúdo/preço)
(preenchendo)

## 4. Tamanho de mercado e normas (fontes oficiais)
(preenchendo)

## 5. Ranking 0–10
(preenchendo)

## 6. Lista final de VERIFICAR
(preenchendo)
