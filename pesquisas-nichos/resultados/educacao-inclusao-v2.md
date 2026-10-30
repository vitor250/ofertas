# Educação e inclusão por país (v2, 30/10/2026)

> Status: EM ANDAMENTO (gravado aos poucos).

## Avisos de método
- A v1 (`pesquisas-nichos-2026-10-29/educacao-inclusao.md`) NÃO estava acessível neste ambiente. Usei os candidatos e os itens VERIFICAR listados no próprio prompt e nas notas do usuário (fila-ofertas, pesquisa-europa).
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). Todas as medições de anúncios foram feitas com o conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Limitação: o conector devolve no máximo 50 anúncios, os mais novos primeiro. Em páginas com >50 ativos (Ludo Kids 181, Estimulación en casa 100, Instytut Edukacji 268, Jogos Terapêuticos 123, Edukapol ~66) medi por recorte (página + termo ou país), e o número é um MÍNIMO.
- **Rede bloqueada:** WebFetch e curl não alcançam facebook.com nem a maioria dos sites (tecnicadellascuola.it, newsistruzione.it etc. recusados pela política de rede deste ambiente). Por isso **não abri nenhuma página de vendas**: preço, plataforma, bumps e garantia de TODOS os vendedores ficam como VERIFICAR. Para liberar, é preciso permitir esses domínios em Network access nas configurações do ambiente (https://code.claude.com/docs/en/cloud-environments#network-access).
- **Busca web esgotada no fim:** o limite de buscas da sessão (compartilhado com os agentes irmãos) acabou durante a pesquisa. Ficaram sem checar: tamanho oficial dos psicólogos/pedagogos na Polônia (uso o número da nota de 29/10), nº de inscritos do CRPE, nº de docentes no portafolio do Chile e a vigência das "Nuove Indicazioni" da escola dell'infanzia na Itália.

## Resumo / ranking 0–10

Régua: PROVADO = vendedor ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende.

| # | Oportunidade (país · público · produto) | Régua | Nota | Por quê / risco |
|---|---|---|---|---|
| 1 | **Polônia · pedagogo/psicólogo escolar e pedagogo especial · teczka + IPET/WOPFU + ocena funkcjonalna gerados por app** | PROVADO + PRAZO | **8,0** | Três nativos em PLN: Edu Anima 247 d, Pani Andzia 226 d, Centrum Pedagogiczne 151 d. A ocena funkcjonalna é obrigatória desde 01/09/2026 (Dz.U. 2026 poz. 428) e a Kompas Jutra tem a 2ª fase em 01/09/2027. Ninguém tem app. Riscos: Specjalni.pl já usa o gancho da ocena funkcjonalna desde 26/10, um clonador USD entrou em 30/10, checkout PLN/BLIK, polonês técnico. |
| 2 | **Itália · docente di sostegno · "PEI DL 170" + verbale GLO + relazione finale + app** | quase PROVADO + PRAZO | **7,5** | Mercado de 261 mil professores (57 mil sem especialização), em EUR. Ludo Kids (operador BR) tem 29 criativos de sostegno há 29,8 d; Sostegno Pronto tem 2 anúncios há 44,7 d. O DL 170/2026 muda o calendário do PEI (junho; 15/10 para novos alunos). Esperar a lei de conversão (até 29/11) antes de escrever os documentos. Usa a nossa operação IT. |
| 3 | **França · candidatos ao CRPE 2027 · kit do oral + simulador** | BRECHA + PRAZO | **6,0** | Inscrições até 25/11/2026 e escritas em 30–31/03/2027 (fonte secundária; oficial ainda VERIFICAR). Só academias de ticket alto anunciam; nenhum kit low ticket. Sem prova de compra. |
| 4 | **Espanha · opositores docentes 2027 · programación didáctica + situaciones de aprendizaje + simulador de defensa** | BRECHA + PRAZO | **6,0** | Convocatórias 2027 por CCAA (Baleares com provas a partir de 17/04/2027; Murcia ~2.000 vagas; CyL Maestros). Só academias e apps de IA de 1–2 dias. Riscos: cultura do "gratis" e academias com isca grátis. |
| 5 | **Multi-país · educadora de infância · planejamento anual pronto (modelo "Estimulación en casa")** | TESTE | **5,5** | O produto-mãe em espanhol está vivo há 82,8 d (USD); os clones IT/PL/RO/HU/UK/AU/IE têm 0–4 d. Na Itália, "Nuove Indicazioni 2026 · 3, 4 e 5 anni" pode ser PRAZO (VERIFICAR norma). Re-checar os clones em 28/11. |
| 6 | **Chile · Evaluación Docente · nicho Educación Especial/Escuela de lenguaje + ECEP** | PROVADO (lotado) | **5,5** | 10+ vendedores em CLP com 37–379 d (profe Ernesto 379 d). Temporada termina em nov; a próxima janela é jul–nov/2027. Brecha só no subnicho de Educación Especial. |
| 7 | **México · USAER/educação especial · documentos + app** | PROVADO fraco | **5,0** | Materiales Miss eli 134 d (produto VERIFICAR), Karla Ramirez 138 d (1 anúncio). Preço baixo (planeaciones a MXN 99/mês). Sem PRAZO. |
| 8 | **Colômbia · docentes · "PIAR pronto" (Dec. 1421/2017) + app** | BRECHA | **5,0** | Ninguém vende kit; só cursos e universidades. Reaproveita o motor PEI/IPET. Norma antiga (sem PRAZO). |
| 9 | Argentina · PPI (plantillas) | TESTE | 4,0 | Formacion digital com PPI há 3,6 d; diplomatura ARS 40.000. Moeda fraca. |
| 10 | Alemanha · Kita (Beobachtung/planejamento) | TESTE | 4,0 | Editoras com e-book grátis (PRO Kita ~184 d); clonador USD de 1,8 d. |
| 11 | Romênia · educatoare (planificări) | TESTE | 3,5 | Só páginas de 1 anúncio (RON) e clonadores USD; "Pentru Educatoare" não encontrada. |
| 12 | Portugal · educação inclusiva (RTP/PEI, DL 54/2018) | BRECHA sem prova | 3,5 | Só formações e clonadores USD de 1–4 d; mercado pequeno e preço baixo. |
| 13 | EUA · IEP | saturado | 2,5 | Bancos de metas de IEP são isca grátis + TPT. |

**Apostas:**
- **Certeira:** Polônia escolar (com app "Jedna obserwacja – pięć dokumentów", 79–99 zł; pico de compra jan/2027, na revisão semestral do IPET/WOPFU (VERIFICAR calendário)), depois de resolver o checkout PLN/BLIK.
- **Prazo:** Itália sostegno, lançando o "PEI DL 170" logo depois da lei de conversão (até 29/11) e escalando em abr–jun/2027, para o PEI de junho.
- **Testes baratos:** CRPE oral (FR, antes de 25/11 para pegar quem se inscreve e até mar/2027) e opositores ES 2027 (dez–mar).
- **Diferença em relação à v1 (pelo que estava no prompt e nas notas):** a Kompas Jutra e a ocena funkcjonalna agora têm fonte; o "Sostegno Pronto" e o Ludo Kids passaram a ter dias reais medidos. A novidade é a onda de clonadores em 26–30/10 (IT/PL/RO/HU/UK/AU/IE), que encurta a janela na Polônia e na Itália. A Ucademy é academia (não concorre com kit). O profe Ernesto está ativo há 379 d. "Pentru Educatoare" não está mais visível.

## Por país

### Itália: docente di sostegno / PEI

**Tamanho (oficial):** ISTAT a.s. 2024/25: ~377 mil alunos com deficiência (+5%), >261 mil insegnanti per il sostegno (~250 mil na escola estatal, fonte MIM), ~57 mil SEM especialização (comprador ideal de "PEI pronto"); 22% das vagas não estavam atribuídas no início do ano. Fonte: https://www.istat.it/comunicato-stampa/linclusione-scolastica-degli-alunni-con-disabilita-anno-scolastico-2024-2025/

**Norma/PRAZO (VERIFICAR anterior: prazo do PEI na lei de conversão do DL 170/2026):**
- DL 30/09/2026 n. 170, em vigor 01/10/2026, em conversão no Senado (A.S. 2053, 7ª Commissione). Prazo de conversão: **29/11/2026**. Até 27/10 havia emendas em discussão (GLO também online). NÃO achei a lei de conversão aprovada → texto final = VERIFICAR depois de 29/11.
- O que o DL já fixa (fontes setoriais): alunos já matriculados → PEI definitivo até **junho**, com atualização nas 2 primeiras semanas de outubro; novos matriculados/nova certificação → PEI provisório em junho e definitivo até **15/10**; o antigo prazo de 31/10 (D.I. 182/2020) deixa de valer; o GLO passa a DEFINIR (não só propor) as horas de apoio. Dossiê da Câmara: https://documenti.camera.it/leg19/dossier/pdf/D26170.pdf ; guia: https://www.orizzontescuola.it/pei-2026-27-scadenze-assegnazione-ore-nuove-disposizioni-glo-e-approvazione-con-18-documenti-da-scaricare/ ; https://www.studentville.it/decreto-170-2026-pei-anticipato-glo-docenti/
- Gancho real de venda: "o PEI agora é feito em junho e define horas; o modelo antigo não serve". Próximo pico de uso: PEI provisório/definitivo de **junho/2027** (campanha a partir de abr/2027) + atualização de outubro.

**Vendedores (Meta, ativos, medidos por page_id em 30/10):**
| Página | Oferta | Anúncios | Moeda | Dias reais | Régua |
|---|---|---|---|---|---|
| Ludo Kids (1064674326719515) | "+120 Attività pronte per il sostegno" | 29 no termo "sostegno" (57 da página na IT; 181 no total, multi-idioma: ES/DE/EN/IT "Musicogrammi") | BRL (operador BR) | sostegno: 29,8 d (início 30/09/2026); musicogrammi IT: 11–13 d | quase PROVADO (vira 30 d em 31/10) |
| The Digital Resource VAULT (417217511687270) | "Sostegno Pronto — Kit Operativo 2026/27" | 2 | USD | 44,7 d (início 15/09/2026) | vivo há 30+ d, mas só 2 anúncios e moeda USD → sinal fraco |
| Estimulación en casa - Kids (563516643501385) | "Il PEI già scritto + 120 attività · sostegno" (9 anúncios) e "Nuove Indicazioni 2026 · 3, 4 e 5 anni" | 100 na página | USD | PEI IT: 3,8 d (26/10) | TESTE (clonador em rollout, ver Polônia/UK/AU/IE/HU/RO) |
| Didattica Persuasiva (839518676072641) | guias "ADHD/DOP senza paura" para professores | poucos | EUR | ~11 d | TESTE (nativo) |
| Edizioni Centro Studi Erickson (203065183038056) | SOFIA ICF, plataforma de compilação de PEI/PDP | – | EUR | 72 d | incumbente (software/editora), não low ticket |

- Preço/página de Ludo Kids e Sostegno Pronto: NÃO consegui abrir (Facebook e a maioria dos sites estão bloqueados pela rede deste ambiente; a busca web não indexa as páginas) → VERIFICAR preço, plataforma, bumps e garantia.
- Leitura: há um operador BR (Ludo Kids) chegando a ~30 dias em sostegno IT com 29 criativos e um clonador (Estimulación en casa) que copiou o ângulo "PEI già scritto" em 26/10. Ninguém vende **PEI conforme o DL 170 + app** (gerador de PEI/relazione finale/verbale GLO). BRECHA de mecanismo, não de nicho.

### Polônia: pedagogo/psicólogo escolar, pedagogo especial (teczka, IPET, WOPFU)

**Tamanho:** ~44 mil etaty (15.534 psicólogos, 15.633 pedagogos especiais, 12.923 pedagogos; MEN 09/07/2026) segundo a deep-dive de 29/10 (nota do usuário; não reconferido hoje → VERIFICAR fonte MEN). Além disso, os nauczyciele współorganizujący (professor de apoio) e as educadoras de pré-escola são compradores dos mesmos documentos.

**Normas/PRAZO (VERIFICAR anterior: reforma Kompas Jutra):**
- **Kompas Jutra (Reforma26): CONFIRMADA.** Nova podstawa programowa desde **01/09/2026** em pré-escola e classes I e IV; desde **01/09/2027** na classe I das escolas ponadpodstawowe (a fase seguinte é o próximo gancho com data). Em jul/2026 ainda faltavam podstawy de ciências (publicação posterior). Fontes: https://www.gov.pl/web/edukacja/rada-ministrow-przyjela-projekt-ustawy-o-zmianie-ustawy---prawo-oswiatowe-oraz-niektorych-innych-ustaw ; https://dokumenty.men.gov.pl/PREZENTACJA-NAUCZYCIELE-WRZESIEN-2026-6a8edfa465125.pdf ; https://www.portaloswiatowy.pl/projekty-aktow-prawnych-dla-oswiaty/reforma-edukacji-2026-sprawdz-jakie-zmiany-planuje-men-26568.html . Edukapol já anuncia webinar "Obowiązkowe tygodnie projektowe w ramach Reformy Kompas Jutra" (18/10) → semanas de projeto obrigatórias são um subgancho (VERIFICAR artigo da norma).
- **Ocena funkcjonalna obrigatória desde 01/09/2026: CONFIRMADA.** Rozporządzenie ME de 02/03/2026, Dz.U. 2026 poz. 428 (orzeczenia e opinie das poradnie): antes do orzeczenie a escola faz a ocena funkcjonalna do aluno (§ 7 ust. 6–7 e § 8 vigentes desde 01/09/2026). Fontes: https://www.portaloswiatowy.pl/pomoc-psychologicznopedagogiczna/ocena-funkcjonalna-od-1-wrzesnia-2026-i-inne-zmiany-w-opiniach-i-orzeczeniach-27362.html ; https://www.portaloswiatowy.pl/pomoc-psychologicznopedagogiczna/ocena-funkcjonalna-wyjasniamy-nowe-obowiazki-szkol-i-zasady-wspolpracy-z-poradnia-27514.html

**Vendedores (Meta, ativos, por page_id, 30/10):**
| Página | Oferta | Anúncios ativos | Moeda | Dias reais | Régua |
|---|---|---|---|---|---|
| Pani Andzia – Szkolenia i Konsultacje dla Nauczycieli (106813384719110) | teczka psychologa/logopedy/wychowawcy, "MEGA PAKIET p. specjalnego", teczka koordynatora standardów ochrony małoletnich (SOM), teczka pedagoga/psychologa w przedszkolu | 10 | PLN | **226 d** (17/03/2026) | **PROVADO** |
| Centrum Pedagogiczne (1620840041579216) | WOPFU/IPET/Opinia por etapa, rewalidacja (300/350/420 wpisów do dziennika), plan pedagoga/psychologa e pedagoga specjalnego 2026/27, nauczyciel współorganizujący | 5 | PLN | **151 d** (31/05/2026); criativo novo 26/10 | **PROVADO** |
| Instytut Edukacji i Innowacji (105593247944178) | cursos/szkolenia + "IPET, WOPFU, arkusz PPP", "Dokumentacja, która obroni się przy kontroli" | 268 | PLN | anúncio IPET: 37 d (22/09) | PROVADO como escola de cursos (ticket maior; VERIFICAR preço) |
| Edukapol Szkolenia (644196402392423) | webinars grátis → cursos para pré-escola/escola (ADHD, dostosowania, Kompas Jutra) | ~66 | PLN | ≥28 d visível (01/10; página tem >50 ativos, o mais antigo não aparece) | funil de cursos, não kit (VERIFICAR) |
| Edu Anima – edukacja i rozwój (108220223931574) | "Wzory opinii", "Gotowe materiały do projektu", "Prawie 40 gotowych pomysłów" | 4 | PLN | **247,5 d** (24/02/2026); criativos novos 21–28/10 | **PROVADO** (achado novo da v2) |
| Specjalni.pl (1125669750798210) | "**Ocena funkcjonalna i opinia funkcjonowania ucznia**", "PRZEDSZKOLE. Zajęcia rewalidacyjne" | 3 | PLN | 4,0 d (26/10) | TESTE: 1º nativo usando o gancho da ocena funkcjonalna |
| Moje Pomoce (393318050534836) | IPET i WOPFU, Psychobox, karty obserwacji | 1 | PLN | 23,6 d | TESTE |
| CudaEdukacji.pl (104882618956234) | Teczka Współorganizująca I-III / IV-VIII | 2+ | PLN | 0,5 d | TESTE (novo) |
| Integra. Materiały edukacyjne (1371872112666012) | "Planer na cały rok" | – | PLN | 7,5 d | TESTE |
| Estimulación en casa - Kids (563516643501385) | "WOPFU i IPET już napisane + 120 zajęć" | 4 (PL) | USD | 0,2 d (30/10) | clonador estrangeiro chegou HOJE |

- Preços (Pani Andzia, Centrum Pedagogiczne, COS 149 zł citado na v1): não abri as páginas (rede bloqueada) → VERIFICAR. A nota de 29/10 fala em faixa 88–239 zł e nenhum concorrente com app.
- Leitura: Polônia é o único país europeu deste nicho com vendedores NATIVOS em moeda local há 150–226 dias (o mais antigo de todos os países europeus medidos hoje). É PROVADO. A janela muda: em 30/10 um clonador estrangeiro (USD) entrou com "WOPFU i IPET już napisane". Nosso ângulo continua livre: **ocena funkcjonalna (nova obrigação) + IPET/WOPFU gerados por app a partir de uma observação** ("Jedna obserwacja – pięć dokumentów").


## Lista final de VERIFICAR
(a preencher)

### Espanha: opositores docentes e professores (programación / situaciones de aprendizaje)

**Norma/PRAZO (VERIFICAR anterior: convocatorias 2027):** não há convocatória nacional; cada CCAA convoca (cadência habitual bienal). O que achei para 2027 (fontes secundárias, todas VERIFICAR no boletim autonômico):
- Baleares: provas das oposiciones docentes 2027 começam em **17/04/2027**, 474 vagas (nota do INAP: https://laadministracionaldia.inap.es/noticia.asp?id=1520889 ; o texto parece misturar com procedimento de mobilidade → conferir no BOIB).
- Murcia: ~2.000 vagas 2027 para Secundaria e FP (imprensa regional, via https://redopositor.com/blog/es-calendario-oposiciones-2027-previsiones-ccaa/).
- Castilla y León anunciou que convocará Maestros (https://avilared.com/art/3516/castilla-y-leon-convocara-oposiciones-al-cuerpo-de-maestros).
- Asturias: 199 vagas da OEP 2026 a convocar em 2027, sem Maestros (CSIF: https://www.csif.es/es/articulo/aragon/educacion/96299).
- Mapa vivo: https://www.campuseducacion.com/blog/oposiciones/2027-mapa-actualizado-de-convocatorias/amp/ . A janela comercial é nov/2026–mar/2027 (entrega de programación didáctica antes das provas).

**Vendedores (Meta, ES, ativos, 30/10):**
| Página | Oferta | Moeda | Dias reais | Régua |
|---|---|---|---|---|
| Ucademy.es (100357595817123) | academia online (FP oficial, oposiciones) | EUR | – (337 anúncios no termo; página grande) | incumbente de ticket alto, NÃO concorre com kit (VERIFICAR anterior: Ucademy = academia, não vendedor de kit) |
| Polaris Oposiciones (1066087746583243) | curso por especialidade (PT, AL, Inglés, Infantil/Primaria) | EUR | ≥17 d visível | academia |
| Diego Fuentes Oposiciones (101862168107308) | "Mes de la Programación" | EUR | 6,8 d | academia (promo sazonal) |
| CenEdu (359544345305) | "Nueva Edición 2027. Pack Gratuito" | EUR | 13,5 d | academia/isca grátis |
| Oposiciones PG (1212047198926135) | "Curso de Programación y Unidades Didácticas" | EUR | 22,6 d | curso |
| Landris.ai (1273402572503595) | IA para professores de Primaria, "Programación situación por situación" | EUR | 1,0 d (7 anúncios) | TESTE (app nativo, novo) |
| aulapro.app / Mesa Ligera | app e "8:55 y la asamblea ya está lista" (Infantil) | EUR | 1,8–2 d | TESTE |

- Nenhum vendedor de **kit low ticket** (programación + situaciones de aprendizaje + rúbricas) com 30+ dias em EUR. Os termos "LOMLOE plantillas" e "situaciones de aprendizaje" não trazem vendedor de kit (só academias, mestrados e ruído). → **BRECHA**, com o risco já anotado na nota de 28/10: espanhol busca "gratis" e a concorrência é academia com conteúdo grátis. Prova de compra: nenhuma no país. Espanhol neutro de LATAM não prova Espanha.
- Tamanho: VERIFICAR (nº de opositores docentes 2027 por CCAA; MEFP não publica consolidado).

### França: CRPE (professeur des écoles) e inclusão (AESH/PAP/PPS)

**Norma/PRAZO (VERIFICAR anterior: inscrições CRPE 25/11):** digiSchool (19/10/2026) diz que as inscrições do CRPE 2027 vão até **25/11/2026, 12h (Paris), no Cyclades**, com escritas em **30–31/03/2027** (https://www.digischool.fr/articles/concours/crpe/concours-crpe-2027/). A página oficial (https://www.devenirenseignant.gouv.fr/le-calendrier-des-concours-de-recrutement-de-professeurs-des-ecoles-de-la-session-2027-1091), atualizada em jul/2026, ainda dizia "calendário preciso comunicado depois" → **parcialmente confirmado; conferir no Cyclades/devenirenseignant**. Existem duas vias em 2027 (CRPE nível Licence/bac+3 e nível Master/bac+5), com programas distintos (CNED: https://www.cned.fr/l-actualite-de-la-formation/blog-devenir-professeur/le-programme-de-la-session-2027-du-crpe-niveau-licence). Datas da via bac+3 2027: não publicadas (VERIFICAR).

**Vendedores (Meta, FR, ativos, 30/10):**
| Página | Oferta | Moeda | Dias reais | Régua |
|---|---|---|---|---|
| Objectif CRPE (280326635719182) | preparação (live grátis, RDV, "Devenez PE en 2028") | EUR | ≥6,6 d visível | academia, ticket alto |
| Demain CRPE (1212247188631772) / ForProf CRPE (1947626962173880) | preparação/reconversão | EUR | ~0,5–6,4 d | academia |
| Accès CRPE (1154800614394241) | 1 anúncio | USD | 0 d (29/10) | TESTE estrangeiro (VERIFICAR oferta) |
| Jogos Terapêuticos (764728496715153) | "Plus de 50 activités psychopédagogiques · dès 5 €" e "+30 exercices pour les troubles des sons" (também em IT) | BRL (operador BR, mesma família de produto que Ludo Kids: "25 Musicogramas") | 19,3 d (atividades FR, 10/10); 123 anúncios na página | TESTE |
| Myhandiqr (1263914923466843) | "Une seule fiche pour tous ses profs" (ficha do aluno com deficiência) | EUR | 0,7 d | TESTE nativo |

- Leitura: CRPE é dominado por academias com funil de live/RDV (ticket alto). Kit low ticket para o **oral do CRPE** (fichas de mise en situation professionnelle + simulador) não aparece em nenhum anúncio → BRECHA com PRAZO (inscrição 25/11; escritas 30–31/03; orais mai–jun/2027). No eixo inclusão, ninguém vende "PPS/PAP/GEVA-Sco prêts" para AESH/professores → BRECHA (sem prova de compra).

### Chile: Evaluación Docente / Portafolio / ECEP (Sistema de Reconocimiento)

**Norma/PRAZO (VERIFICAR anterior: data do portafolio 2026/27):** NÃO achei a data oficial de fechamento do Portafolio 2026. Referência: no ciclo 2025 a plataforma docentemas.cl abriu em 08/07 e fechou em **10/11/2025** (boletim CPEIP: https://www.cpeip.cl/wp-content/uploads/2025/07/boletíndocentes_julio2025.pdf). O CPEIP confirma o "Proceso de Reconocimiento 2026" com Portafolio + ECEP (https://s3.amazonaws.com/evaluacionconocimientos.cl/Equivalencia_PF_y_ECEP_proceso_de_reconocimiento2026.pdf). Anúncios de 28–30/10 ("¿Aún no terminas tu Portafolio?") indicam que o prazo 2026 ainda está aberto e próximo → **VERIFICAR em docentemas.cl** (provável início/meados de nov/2026). Para nós a janela útil é o **ciclo 2027** (abertura ~jul/2027); vender agora só faria sentido em "set ECEP/prueba de conocimientos".

**Vendedores (Meta, CL, ativos, 30/10) — mercado com MUITOS vendedores em CLP:**
| Página | Oferta | Anúncios | Moeda | Dias reais | Régua |
|---|---|---|---|---|---|
| Evaluación Docente 2025 con el profe Ernesto de Jesús (633472899847838) | assessoria/curso de avaliação docente | 3 | CLP | **378,9 d** (16/10/2025) | PROVADO (anúncios antigos ainda ativos; volume baixo) |
| Sube IA (107021255756680) | WhatsApp (IA para portafolio) | 3+ | CLP | 75,5 d | PROVADO |
| Planificada.cl (1115373028328117) | planificações | 2+ | CLP | 68,6 d | PROVADO |
| Asesoramiento y acompañamiento portafolio docente 2025 (259402093932921) | assessoria + "OFERTA" | 5+ | CLP | 63,0 d | PROVADO |
| Portafolios Docente (997136753476278) | – | 1+ | CLP | 55,9 d | PROVADO |
| Einstein Academic (101455142895773) | "Asesoría Portafolio Docente 2026", "¿Aún no terminas tu Portafolio?" | 2+ | CLP | 55,7 d | PROVADO |
| Aprenova Capacita (1239145949290283) | "Portafolio Docente 2026: curso completo" | 1+ | CLP | 46,4 d | PROVADO |
| Portafolio en 1-2-3 (881782171675666) | – | 1+ | CLP | 43,5 d | PROVADO |
| Material Educativo Y Complementario Para Docentes 2026 (1093021060556149) | "Set prueba de conocimiento específico 2026 … todas las especialidades" | 1+ | CLP | 39,2 d | PROVADO (ECEP) |
| Profesores Expertos (1231293850074529) | profesoresexpertos.cl | 1+ | CLP | 37,4 d | PROVADO |
| La profe GPT, Corrector Portafolio Docente, Taller Propio (manuais por nível, incl. Educación Especial), Chronos ("Sube de tramo"), Evaluación Docente Chile (USD, "Dossiers Prueba ECEP") | IA/app/manual | – | CLP/USD | 1,9–10 d | TESTE (onda nova de apps de IA) |

- Preços: não abri as páginas (rede bloqueada) → VERIFICAR. Leitura: Chile é PROVADO e lotado (10+ vendedores com 37–379 dias), sazonal (jul–nov) e já com apps de IA corrigindo o portafolio. Entrar agora = fim de temporada. Brecha só em nicho: **Educación Especial / Escuela de lenguaje** (só o Taller Propio, 2 dias, cita manual específico) e ECEP por especialidade.

### México: planeaciones NEM e educação especial (USAER)

- **Planeaciones (geral):** mercado lotado em MXN (126 anúncios no termo "planeaciones NEM"; Editorial MD "Tus planeaciones de preescolar por $99 al mes", Ladocencia e AuxiDocente com IA, dezenas de páginas "...que se Arma", Telesecundaria etc.). Não é brecha.
- **Inclusão/USAER (MXN):**
| Página | Anúncios | Dias reais | Régua |
|---|---|---|---|
| Materiales Miss eli (718224014710342) | ~26 | 134,4 d (17/06/2026) | PROVADO (produto exato = VERIFICAR; apareceu no termo "USAER") |
| Didácticos Karla Ramirez (417063041497691) | 1 | 138,0 d | PROVADO fraco (1 anúncio) |
| Materiales Digitales Inclusivos (1314688911732456) | 1 | 6,1 d | TESTE |
| Mi Diario de USAER by Francia Glz (683701745150580) | 1 | 1,0 d | TESTE |
| Docencia Inclusiva (1355229434344088) | 4 | 0,5 d (criativos de 25–29/10) | TESTE |
- Leitura: há vendedores de material inclusivo há 130+ dias em MXN; os documentos de USAER (evaluación psicopedagógica, "propuesta curricular adaptada", BAP, ajustes razonables) aparecem só em páginas novas. Oportunidade = kit de documentos USAER + app, mas o comprador típico paga pouco (planeaciones a MXN 99/mês). Norma: NEM/Plan de Estudio 2022 (sem prazo novo encontrado) → sem PRAZO.

### Colômbia: PIAR (Decreto 1421/2017)

- Norma: o PIAR (Plan Individual de Ajustes Razonables) é instrumento do Decreto 1421/2017 (compilado no Decreto 1075/2015) para todo estudante com deficiência em escola pública ou privada (fontes: https://www.mineducacion.gov.co/1780/articles-428348_recurso_1.pdf ; https://www.saldarriagaconcha.org/wp-content/uploads/2019/01/Narrativa-PIAR.pdf). Não é norma nova (sem PRAZO). Nº de alunos com PIAR: não achei dado oficial → VERIFICAR (SIMAT).
- Anúncios (CO, "PIAR", 32): só formação (Corporación Internacional Líderes Latinoamérica ONG "De la teoría a la práctica: DUA y PIAR", 0 d; UNIR; Uniminuto) e escolas. **Nenhum kit "PIAR pronto"** → BRECHA (sem prova de compra). Reaproveita o motor do PEI/IPET.

### Argentina: PPI (Proyecto Pedagógico Individual)

- Formacion digital (1281355945066261, ARS): "PPI Paso a Paso | Modelos y Plantillas para Docentes" (3,6 d) numa página multi-produto (DUA en el aula 2026, ABP, até "estados contables") cujo anúncio mais antigo tem 31,6 d → TESTE.
- Centro de Capacitaciones Polo Educativo del Litoral: "Diplomatura en PPI | Promo $40.000" (ARS, 12 d) → curso.
- Leitura: TESTE; moeda fraca (ARS) e inflação → preço baixo.

### Portugal: educação inclusiva (DL 54/2018: RTP, PEI, PIT)

- Termos "educação inclusiva" e "professores materiais prontos" (PT): só formações (Academia INpacto, EduLi, CPF) e clonadores estrangeiros em USD de 1–4 dias (Leonie Schmid "Menos preparação. Mais tempo para ensinar"; Made easy Studio "860 recursos prontos" para inglês). Nenhum kit de RTP/PEI/PIT. → BRECHA sem prova; mercado pequeno e preço de consumidor baixo (€4,90–14,90, nota de 28/10).

### Romênia: educadoras de grădiniță (VERIFICAR anterior: Pentru Educatoare)

- "Pentru Educatoare" NÃO apareceu em nenhum anúncio ativo hoje (termo traz 99 resultados de ruído: presentes, sapatos, flores) e a busca web não achou o site → **VERIFICAR** (pode ter parado ou ter outro nome de página).
- Ativos achados: Atelierul educatoarei, Curs Educatoare, Educatoare de pitici (RON, 1 anúncio cada, 0,3–8,9 d); Poteca (USD) "40 de activități de mișcare gata de imprimat"; Estimulación en casa - Kids "Planificarea anuală, gata făcută · 3–6 ani" (USD, ~3 d). → TESTE; só clonadores e páginas pequenas.

### Alemanha / países de língua inglesa (checagem rápida)

- DE: Verlag PRO Kita (editora, e-book grátis como isca, ~184 d), ErzieherIn (revista, "Gratis Ausgabe"), Spielschachtel (USD, "1.180 Spiele + 120 fertige Einheiten", 1,8 d), Kopfüber ("Adventskalender für Kitas"). Mercado de editoras com isca grátis; kit pago = TESTE.
- EN: o clonador Estimulación en casa - Kids roda "Your EYFS year, ready-made" (UK), "EYLF" (AU) e "Aistear" (IE) desde 28–30/10. EUA: bancos de metas de IEP são isca GRÁTIS (A Day in our Shoes ~37 d; Aba Speech desde fev/2024) + TPT → não é brecha low ticket.

### Padrão transversal: onda de clonadores (importante para o timing)

Em 15 dias apareceram operadores em USD/BRL replicando "kit do professor" em vários países ao mesmo tempo:
- **Estimulación en casa - Kids (USD)**: produto-mãe em espanhol "Planificaciones para maestras de guardería / Todo el año resuelto" ativo há **82,8 d** (desde 07/08/2026) → clonado em 26–30/10 para IT (PEI + Nuove Indicazioni), PL (WOPFU/IPET), RO, HU, UK, AU, IE. Sinal de que o modelo vende em espanhol; os clones são TESTE.
- **Ludo Kids / Jogos Terapêuticos (BRL)**: mesma família de produto ("25 Musicogramas") em ES/DE/EN/IT/FR/PT; o "sostegno" IT tem ~30 d.
- Spielschachtel (DE, USD), Poteca (RO, USD), Leonie Schmid (PT, USD), KompraFácil (PEN, atividades de inglês em italiano).
→ Em PL/IT o nativo ainda lidera, mas a janela de "primeiro com documento normativo + app" está fechando. Re-checar em 12/11 e 28/11 quais clones passaram de 30 dias.
