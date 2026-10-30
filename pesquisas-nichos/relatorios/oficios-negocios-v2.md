# Ofícios e negócios por país: v2 com medição real, fontes e brechas (30/10/2026)

Substitui `oficios-negocios.md` (29/10, sem busca web). Escopo: restauração/HACCP/inspeção sanitária, SST do pequeno empregador (DVR, DUERP, SG-SST, SSOMA, NOM-035), igreja/pastor, gastronomia LATAM, limpeza, empreiteiro/arquiteto, aluguel curto, pet, cerimonialista, fotógrafo, transporte.

Convenções: PROVADO = vendedor com anúncio ativo há 30+ dias no país/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. Dias contados até 30/10/2026 (±1 dia). Nada inventado: o que não confirmei está como VERIFICAR.

## Como medi e limites (honesto)
- Conector Meta (`ads_library_search`, só ATIVOS), por `page_id`: Andrei Kowalski, Studio Facile, Étudefacile, Solunetpro, Más seguridad, Beatriz Guerra, Mango PR, sklep-haccp.pl. O conector devolve só título do link; lista os mais recentes primeiro, então para páginas com mais de 50 anúncios os dias do mais antigo são mínimos.
- SearchAPI (frase exata, 1 página = ~30 anúncios, ordenada por recência no lote): rodei ~130 buscas país x termo local. Os créditos do SearchAPI chegaram a 10.000/10.000 no meio da rodada (uso compartilhado com outras sessões; rodei 8 workers em paralelo e tomei 429). Buscas que falharam por 429 ou nem rodaram estão marcadas VERIFICAR: wedding planner e fotógrafo (FR, ES, PL, CO, PE, MX), toelettatura/DVR/ispezione ASL/impresa di pulizie (IT, quase tudo), RO/CZ/SK/GR/NL termos locais (só consegui HACCP pelo conector), limpeza e obra em ES/PT/DE/FR/CL/AR/MX/CO/PE, transporte. SearchAPI zerado até 08/11 (renova). Não usei o navegador na Biblioteca (bloqueia IP; o ad individual abriu no navegador só uma vez).
- Os dias de uma busca por termo são do anúncio mais antigo DENTRO do lote lido, não do vendedor inteiro. Onde digo "N cr" é o nº de criativos do lote.

---

## 1. Andrei Kowalski e Studio Facile: resolvido

### Andrei Kowalski (page 1340912605769671)
- Anúncios ativos: 20 (conector) ; mais antigo ativo 18/10/2026 => ~12 dias. Moeda do anúncio USD (conta), preço ao consumidor em EUR. Lotes em 18/10, 20/10, 21/10, 23/10, 26/10, 29/10: cadência de ~1 lote a cada 2-3 dias (escala em andamento, ainda NÃO provado por 30 dias).
- Línguas: FR (DDPP), RO (DSVSA), CZ, SK. Mesmo produto em 4 países.
- Produto (ad FR 1115858381031924 + página): "HACCP au mur": dossier sanitaire / PMS para café e bistrô. Preço **19,60 € pagamento único** (riscado 47 €), sem assinatura e sem app: Word + Excel + PDF. Conteúdo: PMS em 4 partes (boas práticas, plano HACCP, rastreabilidade, não conformidades), fichas diárias "deux signatures" 12 meses, tabela dos 14 alérgenos, guia "jour du contrôle", formação do pessoal em 1 página, dossiê modelo preenchido "Café du Tilleul". Pacote "6 em 1" com 5 presentes (valorizados 12/7/5/3/1 €), timer de 15 min. Garantia 30 dias; renúncia ao direito de retratação (art. L221-28). Sem order bump.
- Checkout: loja Shopify em **concentrare.shop** (a mesma loja serve vários nichos; a home é de um programa de caligrafia em tcheco); pagamento por checkout externo `haccpaumur.impultienda.ar` (Impultienda). Sem razão social, sem SIRET, sem mentions légales; contato em Gmail. Operação anônima de escala.
- O texto do ad cita "Alim'confiance, DGAL, 22/10/2025-20/10/2026": 33.205 controles em restauração, 172 fechamentos, multa até 1.500 €/infração (art. R237-2 do code rural). Número vem do anúncio; NÃO confirmei na fonte (VERIFICAR).

### Studio Facile / Étudefacile / Studio Digitale (mesma operação)
- Studio Facile (page 1232011766670582): 920 anúncios ativos, tudo 29/10 nas páginas lidas (lotes de 30); idade da página VERIFICAR (não deu para ler os mais antigos). Étudefacile (page 1299578486577349, FR): 91 anúncios, mais antigo ~06/10 (24 dias, via SearchAPI primeira página). Studio Digitale (page 1385277191336074, RO/CZ): HACCP/higiene alimentar, anúncios de 27-28/10 (2-3 dias). Conta em USD.
- Produto confirmado (página FR `studiofacilebook.com/fr/haccp`): "L'HACCP Illustré", PDF de 69 páginas em 9 partes + 2 bônus ("Les Fiches d'Autocontrôle Prêtes", "Les 14 Allergènes en Fiches"). **19,90 €** pagamento único (valor riscado 91 €), entrega por e-mail, garantia 30 dias. Vendedor no rodapé: **Quillstone Digital LLC, Miami (FL)**. Checkout não nomeado. Catálogo multi-nicho em `catalogo.studiofacilebook.com` (não consegui ler). Ex.: Farmacologia Illustrata IT 19,90 €.
- HACCP ilustrado ativo em: FR, IT, PT ("O HACCP, com desenhos"), GR, CZ, RO, PL (títulos nos anúncios). Multi-nicho também: segurança do trabalho, toelettatura, soldagem, primeiros socorros, bomba de calor, fotovoltaico.
- Leitura: DUAS operações independentes (Andrei = dossiê/PMS preenchível; Quillstone = livro ilustrado) entraram no mesmo ofício e no mesmo preço (~19,6-19,9 €) em ~3 semanas. Prova de demanda forte e de risco de saturação rápida. Nenhuma tem 30 dias ainda.

---

## 2. Concorrentes medidos (ofício x país)
| Vendedor (page_id) | País/moeda | Produto/preço | Anúncios | Dias | Nota |
|---|---|---|---|---|---|
| Andrei Kowalski (1340912605769671) | FR/RO/CZ/SK, EUR | Dossiê PMS café/bistrô 19,60 € | 20 | ~12 | TESTE quente |
| Étudefacile (1299578486577349) | FR | L'HACCP Illustré 19,90 € | 91 | ~24 | TESTE |
| Studio Facile (1232011766670582) | IT/PL/CZ/GR/PT/DK | livros ilustrados 19,90 € | 920 | ≥1 (VERIFICAR) | rede |
| Studio Digitale (1385277191336074) | RO/CZ | HACCP ilustrado | n/d | 2-3 | rede |
| sklep-haccp.pl (1024438174083225) | PL, PLN | Dokumentacja HACCP: pizzaria PDF 99,90 zł; restaurante .doc 156,45 zł; kebab/food truck 199 zł; GHP/GMP gastronomia 83,80 zł | 12 | ~25 | PROVADO preço, anúncio <30d. Loja Sky-Shop. |
| Mango PR (110580295251486) | PL, PLN | "pakiet dokumentacji do kontroli sanepidu" (hoje diz "dla branży beauty") | 3 | ~418 (set/2025) | PROVADO PL, volume baixo |
| Normattivo (235280853010580) | ES | planes de higiene, registro de temperaturas, "evita sanciones en tu bar" | 1 | 20 | TESTE ES |
| ePackPro España (102859491444283) | ES | software APPCC | 37 | 160 | software, não kit |
| Optimus México/Optimus CO | MX/CO | controle de limpeza/registro sanitario (serviço/software) | 3 | 274 | serviço |
| Aprende y Emprende (944982265371293) | MX | Paquete BPM (restaurante/padaria) | 1 | 2 | TESTE |
| Novelty Nook (207018565827293) | PT, USD | "Guia de Formação HACCP para Cantinas Escolares" | 3 | ~2 | TESTE |
| Solunetpro (1118702291315648) | CO, COP | Formatos SG-SST 2025-2026, "primero recibes y luego pagas" | 15 | ~13 (16/10) | TESTE (no ar menos que a v1 supôs; v1 disse 13) |
| GESEC SST (105349967869378) | CO | Resolución 0312 via WhatsApp | 6 | 120 | serviço |
| Safe Mode (1518421751730925) | CO | landing SG-SST | 1 | 351 | serviço |
| Más seguridad (291789807354053) | MX, MXN | título vazio; produto NÃO lido (ad não abriu: 403/browser travado) | 5 | **~361** (02/11/2025) | VERIFICAR conteúdo |
| Beatriz Guerra (907895875729587) | IT, BRL | "Capisci il rischio, non andare a memoria" (DVR/rischi); produto não lido | 5 | **~34** (25/09) | operador BR testando IT, VERIFICAR conteúdo |
| Daily Faith (1005251422680860) | US-ES, BRL | "+1000 Bosquejos listos para predicar" | 2+ | **~184** (28/04) | PROVADO |
| Predicación Poderosa (1020053301191726) | US-ES, BRL | "+1000 Bosquejos listos para predicar" | 1+ | **~235** (08/03) | PROVADO |
| Clara Martin (100116972606665) | US-ES, BRL | "Central Teológica" | 4+ | **~111** (10/07) | PROVADO |
| Código Divino/Codigo Stella/Palavra & Propósito (clones) | MX/CO/PE/AR | estudo bíblico "Código Divino" | 1-3 cada | 88-121 | PROVADO (estudo bíblico, não bosquejo) |
| Luz y Palabra (115620948182714) | LATAM, USD | 110 bosquejos | 40 | ~22 (v1) | TESTE |
| J'affiche Complet (2023109481277781) | FR | método de aluguel temporada (go.jaffichecomplet.com/methode-jac) | 9 | 703 | PROVADO método/curso, não template |
| Cursos de peluquería canina: CIM Formación (ES), Artero Academy (ES/CO), Espacio Set (AR) | ES/CO/AR | cursos | 2-3 | 310-926 | curso, sem kit |
| Maikranz / LUANA / celebrateUs (DE) | DE | curso/guia para wedding planners | 1 | 153-209 | curso, sem kit de contratos |

---

## 3. Brechas, uma a uma (país x ofício x quem vende x dias)
Formato: país | ofício | quem vende | dias. "Ninguém" = nada de kit/documentos nos termos medidos.

**Restauração / HACCP / inspeção sanitária**
1. FR | café/bistrô PMS+HACCP | Andrei (dossiê 19,60 €), Étudefacile (PDF 19,90 €); software: ePackPro, HACCP Simple, JDC | 12 e 24. Ninguém com 30+. Brecha = fazer melhor: simulateur de contrôle DDPP + app + padaria/boulangerie/traiteur.
2. RO | restaurante/cafenea HACCP+DSVSA | Andrei (RO), Studio Digitale; resto do lote é B2B (Alibaba, SGS) | 12 e 2-3. Ninguém local.
3. CZ | kavárna/restaurace HACCP | Andrei (CZ), Studio Facile/Digitale | 12 e 1-3. Ninguém local.
4. SK | kaviareň HACCP | Andrei (SK) | 12. Ninguém mais medido.
5. GR | εστίαση HACCP | só Studio Facile (1 dia) e controle de pragas | 1. Ninguém com kit.
6. PT | restauração HACCP/ASAE | Studio Facile PT (1 dia), Novelty Nook cantinas (2 dias), thequalitycollege (BRL, curso provável) | ≤2. Ninguém com 30+. Gancho ASAE 2026 existe (seção 5).
7. ES | bar/restaurante APPCC | Normattivo (20 dias, docs), ePackPro (software 160 dias), cursos | 20. Sem kit antigo.
8. IT | ristorazione HACCP | v1: NORMA HACCP 125 dias, HACCP Smart 93, EPC 98 (serviço/software/manual) + Studio Facile IT | sem kit de simulador antigo. Medição IT desta rodada falhou (429): VERIFICAR.
9. PL | gastronomia HACCP/sanepid | sklep-haccp.pl (25 dias, 83,80-199 zł), Mango PR (418 dias, pacote p/ sanepid), HACCP od zera (14 d), Mierz Wysoko (53 d, 1 cr), curso Szkoła Jakości 597 zł | **PROVADO**: único país com vendedor local de documentos HACCP a preço alto.
10. DE | Gastronomie Eigenkontrolle/HACCP | Gastro Monk (software, 157 d, AT), serviços; "Eigenkontrolle Gastronomie" = 0 resultados | ninguém com kit. Alemão = muito "kostenlos"; deixar em hold.
11. NL | HACCP/hygiënecode | não medido (SearchAPI zerou): VERIFICAR.
12. MX | restaurante/panadería NOM-251 BPM | Aprende y Emprende (2 dias), Optimus (274 d, serviço), EECOS (curso) | ninguém com kit antigo.
13. CO | plan de saneamiento básico / BPM restaurante | só uma empresa de fumigação (49 d); "BPM restaurante" = 0 | ninguém.
14. PE | DIGESA/BPM | resultado só ruído (cosméticos/alibaba) | ninguém de kit. PE/CL/AR/EC "BPM/manipulación de alimentos": AR Cfvpraxis 149 d (curso, 10 cr), nenhum kit.

**SST do pequeno empregador**
15. FR | DUERP micro-empregador (1 funcionário+) | total de 12 anúncios; Preventionbtp (24 d, 3 cr, entidade do setor construção), People Vox (pesquisa de clima), FSDL (dentistas), Marina Cardozo (6 cr, 0 d, não identificado) | ninguém vende kit DUERP com simulador. **Brecha com gancho novo (Loi 2026-534).**
16. IT | DVR microimpresa | busca conector "DVR documento valutazione rischi modello": 1 anúncio (Nicola Nocera, consultoria, 3 dias); v1: 51 anúncios de serviço/software; Beatriz Guerra (BRL, 34 d, 5 cr) é operador BR testando | sem kit com simulador de controllo; sinal BR de 34 dias.
17. ES | PRL pequeño empleador | só cursos/máster (Mastermas 339 d, Emagister 185 d etc.) | ninguém de kit.
18. DE | Gefährdungsbeurteilung | manageforwork 490 d (3 cr), Splix 124 d (11 cr, software), TÜV Rheinland | só software/formação.
19. PL | BHP/ocena ryzyka zawodowego | Portal BHP 174 d ("Kontrola PIP"), Usługi BHP24 126 d, BezpieczniePracuj 49 d: serviços/cursos; "ocena ryzyka" total 12 | ninguém de kit.
20. RO/CZ/SK | SSM/BOZP | não medidos (SearchAPI zerou): VERIFICAR.
21. CO | SG-SST 7 padrões (<=10 trabalhadores) | Solunetpro 13 d, Safe Mode 351 d, Sistegra 126 d (software, 6 cr), GESEC 120 d (WhatsApp, 6 cr), v1: 25 anúncios | mercado cheio e barato, nenhum com simulador de visita MinTrabajo.
22. MX | NOM-035 / NOM-030 / comité de seguridad e higiene | cursos (UVM 1.095 d, Cursos Guadalajara 302 d), Formato Empresarial 230 d (1 cr), Higiene y Medicina Industrial 78 d (5 cr), "comité de seguridad e higiene" = 0 | pouco kit; Más seguridad 361 d (MXN) pode ser o único kit antigo, conteúdo VERIFICAR.
23. PE | SSOMA/SUNAFIL/comité | v1: pack SSOMA 46-54 d; CALGESA 23 d (curso), Certus 285 d (curso planilhas/SUNAFIL), Instituto de Salud Ocupacional 486 d | kit SSOMA com 46-54 d é o único.
24. CL | prevención de riesgos / Seremi | busca falhou (429): VERIFICAR. AR | higiene y seguridad laboral | só cursos (AulaClub 79 d, 38 cr; Siglo 21): ninguém de kit.

**Igreja/pastor**
25. US (hispânico) | bosquejos | Daily Faith 184 d, Predicación Poderosa 235 d, Clara Martin 111 d (todos BRL, operadores BR) | PROVADO.
26. MX/CO/PE/AR | bosquejos | total 1.188-1.326 anúncios; Código Divino e clones 88-121 d (estudo bíblico), Luz y Palabra 22 d, Juliana Vargas, Unidos en la Fe (v1) | PROVADO em estudo bíblico; bosquejo puro ainda <30 d na v1. Nicho saturando.
27. PT-PT / Angola / Moçambique | sermões/esboços | NÃO medido: VERIFICAR (possível brecha de idioma/moeda).

**Outros ofícios**
28. ES/CO/PE/AR/DE/FR/PL | pet grooming (banho e tosa) | só cursos e salões (CIM Formación 626 d, Artero 310 d, Hundesalon 183-709 d, Esprit Animal 1.366 d, Activ'Pet produto); kit de fichas/contratos/SOP: ninguém | brecha pura, mas demanda comprovada é de CURSO. IT toelettatura: Studio Facile (1 anúncio, 29/10).
29. FR | aluguel de temporada | J'affiche Complet 703 d (método), NOVASOL 617 d (plataforma), Homerez 163 d (software); template/contrato/livret d'accueil: ninguém | PROVADO método, brecha em kit.
30. ES | alquiler turístico | gestoras e consultoria (Sleepaways 72 d, Place Your Place 55 d); kit de anfitrião: ninguém. DE Ferienwohnung: só investimento (Gigaron 40 d). PL: assessora fiscal 293 d, investimentos.
31. DE | Hochzeitsplaner | curso/guia (Maikranz 153 d, LUANA 153 d), app Bridebook 139 d (31 cr), celebrateUs 209 d | contratos/checklists para planner: ninguém medido.
32. ES | wedding planner/fotógrafo contratos | busca conector "plantillas contrato fotógrafo bodas" = 0 ads; IT "wedding planner modelli contratti" = 0 | ninguém. FR/PL/CO/PE/MX: falhou: VERIFICAR.
33. AR | organizadora de eventos | 11 anúncios: Isabel Orue (serviço, 85 d), Candy Craft (insumos 202 d) | sem kit.
34. Limpeza (empresa de limpieza/Gebäudereinigung/nettoyage), empreiteiro (presupuesto de obra), transporte (transportista autónomo): rodadas falharam por 429 em ES/PT/DE/FR/PL/MX/CO/PE/CL; v1 EUA: coatandquote ~24 d, BNB Tracker Pro 82 d, Cleaning Business in a Box 8 d: **VERIFICAR LATAM/EU**.
35. Gastronomia LATAM (costeo): v1 Gastroguias Hub CO 562 d (3,5 USD), Chef Anna 27 d; não re-medi.

---

## 4. Tamanhos de mercado (com fonte e nível de confiança)
| País | Medida | Número | Fonte | Confiança |
|---|---|---|---|---|
| IT | empresas de ristorazione ativas 2024 | 327.850 (bar 127.667; ristoranti e mobile 195.670) | FIPE-Confcommercio sobre dados InfoCamere/Registro Imprese, via Italpress (https://www.italpress.com/?p=522105) | média (imprensa; FIPE direto: https://www.fipe.it) |
| FR | estabelecimentos de restauração (traditionnelle, rapide, traiteur) | ~179.000 (jun/2024) | citado por sites comerciais atribuindo ao INSEE (https://tool-advisor.fr/blog/chiffres-statistiques-restauration/) | baixa: VERIFICAR no INSEE (NAF 56) |
| PL | lokali gastronomiczne fim de 2024 | ~101.500 (+8,8%); restaurantes ~30 mil, bares ~26 mil | GUS via compilação comercial e BOSBank (https://www.bosbank.pl/__data/assets/pdf_file/0024/76902/BOSBank_Restauracje_2026.07.pdf) | média; VERIFICAR GUS "Rynek wewnętrzny w 2024" |
| MX | unidades econômicas do subsetor 722 (preparação de alimentos e bebidas) | 772.442 (DENUE mai/2025) | DataMéxico/INEGI (https://www.economia.gob.mx/datamexico/en/profile/industry/food-services-and-drinking-places) | média; é subsetor, não só restaurante |
| CO | micronegócios nas 24 cidades principais, 2025 | 2.434.942 | DANE Emicron via El Espectador (https://www.elespectador.com/economia/crecio-el-numero-de-micronegocios-en-colombia-cuantos-empleos-generan-noticias-hoy/) | média (imprensa; boletim DANE não achado) |
| FR | empregadores com DUERP obrigatório (>=1 funcionário) | não achado número 2024 | VERIFICAR (INSEE/Urssaf) | - |
| PT, ES, RO, CZ, SK, GR, PE, CL, AR | restauração / empregadores | não consegui fonte oficial | VERIFICAR (INE PT/ES, INS RO, ČSÚ, ŠÚ SR, ELSTAT, SUNAT/INEI, INE CL, INDEC) | - |

## 5. Ganchos com data e multa (fonte e confiança)
| País | Gancho | Texto/valor confirmado | Fonte | Status |
|---|---|---|---|---|
| **FR** | DUERP: sanção administrativa nova | Loi n° 2026-534 du 25 juin 2026, art. 48: inspeção do trabalho pode dar aviso ou multa administrativa de até **4.000 € por infração** (repetida: 6.000 € / 8.000 € por trabalhador segundo CAPEB); só falta total do DUERP, não falta de atualização; sanção penal 7.500 € (15.000 € reincidência) por não elaborar (service-public) e contravenção 1.500 € pessoa física / 7.500 € pessoa jurídica (CAPEB). DUERP obrigatório a partir do 1º funcionário; atualização anual a partir de 11 funcionários. | https://entreprendre.service-public.gouv.fr/actualites/A18908 (publicado 26/06/2026, atualizado 03/08/2026) ; https://www.capeb.fr/actualites/duerp-obligatoire-de-nouvelles-sanctions-administratives-depuis-la-loi-du-25-juin-2026 | **PRAZO parcial**: lei de 25/06/2026 confirmada em fonte oficial; data de entrada em vigor NÃO informada: VERIFICAR; valores divergem entre as duas fontes: VERIFICAR texto da lei (Légifrance) |
| **IT** | DVR: sanção | Art. 55 c.1 D.Lgs. 81/2008 (Normattiva): arresto 3-6 meses ou ammenda 2.500-6.400 € ao datore di lavoro (art. 29 c.1); c.3: 2.000-4.000 €; c.4: 1.000-2.000 € por DVR sem elementos. Fonte secundária cita valores revalorizados 3.071-7.862 €; outras cifras (4-8 meses / 5.000-15.000 €) são do comma 2 (casos de risco agravado). DL 159/2025 convertido na Legge 198/2025 (GU 30/12/2025 segundo circular ANCE Torino) reforça vigilância/formação | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81~art55 ; https://torino.ance.it/2026/01/09/circolare-8-2026-sicurezza-sul-lavoro-conversione-del-d-l-159-2025-legge-198-2025/ | multa confirmada; **sem prazo de calendário** para microimpresa; valores revalorizados VERIFICAR |
| **CO** | SG-SST estándares mínimos | Res. 0312/2019: até 10 trabalhadores em risco I-III = 7 padrões (art. 3); 11-50 = 21 (art. 9). Circular 027 de 26/02/2026: autoavaliação digital no sgrl.mintrabajo.gov.co **até 31/07/2026** (data passada; próximo ciclo: VERIFICAR). Multa citada "até 500 SMMLV": só fonte secundária | https://actualicese.com/especial-actualicese-generalidades-del-sg-sst/ ; https://www.buk.co/blog/circular-027-sg-sst-plazo-registro ; https://www.garrigues.com/es_ES/noticia/colombia-fija-nuevos-estandares-minimos-para-implementar-el-sistema-general-de-seguridad-y | norma e padrões confirmados (secundária); prazo 2027 e multa VERIFICAR no texto da Res. 0312 / Circular 027 |
| **MX** | NOM-035-STPS | STPS prioriza NOM-035 no programa de inspeção 2026 (fonte secundária); multas por UMA (250-5.000 UMA segundo um guia; valor da UMA diverge entre fontes). Jornada de 40 h / 01/01/2027 NÃO confirmada nesta busca | https://www.veritas.org.mx/Impuestos/Seguridad-social/Inspecciones-STPS-2026-obligaciones-laborales-y-sanciones-en-Mexico | VERIFICAR (DOF/STPS) |
| **PT** | ASAE fiscalização restauração | Operação com 183 estabelecimentos de restauração e bebidas suspensos e 9 detidos, 4+ t apreendidas (jul/2026); suspensões por falta de condições de higiene. Sem balanço anual 2025 nem tabela de coimas por HACCP | https://www.dnoticias.pt/2026/7/18/499558-asae-suspende-183-estabelecimentos-de-restauracao-e-bebidas-e-detem-nove-pessoas/ ; https://www.nit.pt/comida/restaurantes/em-2026-asae-ja-encerrou-183-restaurantes-e-bares-e-apreendeu-4-toneladas-de-produtos | gancho de fiscalização real; **sem data de norma**; coimas VERIFICAR (ASAE) |
| **FR** | contrôles sanitários Alim'confiance | Resultados publicados desde 03/04/2017; nível "à corriger de manière urgente" leva a fechamento. Números 33.205/172/1.500 € vêm só do anúncio do Andrei | https://agriculture.gouv.fr/alimconfiance-les-resultats-des-controles-sanitaires-accessibles-tous/ | número VERIFICAR |
| **UE (RO/CZ/SK/PL/GR/IT/ES/FR/PT)** | HACCP é obrigação do Reg. (CE) 852/2004 | não abri o texto nesta rodada (conhecimento geral) | EUR-Lex | VERIFICAR; base comum, sem data nova |
| **PE** | Ley 29783 / SUNAFIL | microempresas REMYPE têm multas reduzidas; não achei fonte oficial 2026 de mudança | (secundárias: misha.pe, sueldojusto.pe) | VERIFICAR (gob.pe, El Peruano) |
| **PL** | sanepid/GHP-GMP, BHP | sem fonte oficial nesta rodada | - | VERIFICAR (GIS, PIP) |
| **RO** | DSVSA | sem fonte oficial | - | VERIFICAR (ANSVSA) |
| **MX** | NOM-251-SSA1-2009 | busca por "PROY-NOM-251" não achou projeto de revisão; só PROY-NOM-051 (rotulagem, 05/12/2025) | https://mexicobusiness.news/health/news/cofepris-opens-public-consultation-five-draft-noms | sem gancho confirmado |

---

## 6. Ranking 0-10 (evidência x tamanho x gancho x reaproveitamento x risco)
| # | Brecha | Nota | Tipo | País | Evidência | Tamanho | Gancho | Reaproveita | Risco |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Kit DUERP do micro-empregador + simulador de visita da inspeção do trabalho | **8,0** | NOVO, PRAZO | FR | 0 kit; 12 anúncios, todos serviço/setorial; lei nova 25/06/2026 | VERIFICAR | €4.000/infração (Loi 2026-534 art. 48), sem data de vigência | Total da lógica da Consultora/SST; app e simulador | vigência/valores a confirmar; público (TPE) com pouco hábito de comprar online; francês exige jurídico preciso |
| 2 | Dossier PMS/HACCP café-bistrô-boulangerie + simulateur DDPP | **7,8** | TESTE quente | FR (depois RO/CZ/SK/PT/ES) | 2 operações em 12-24 dias a ~19,6-19,9 € | ~179 mil (FR, baixa confiança) | Alim'confiance (sem data nova) | 80% da Consultora | saturação rápida; margem sob pressão; anúncios anônimos (Andrei) podem sumir (nenhum provado 30d) |
| 3 | HACCP/sanepid kit local PL | **7,0** | PROVADO preço | PL | sklep-haccp.pl 83-199 zł, Mango PR 418 d | ~101,5 mil lokali | nenhum confirmado | alto; tradução pl | concorrente local com loja; idioma; Studio Facile também entrou |
| 4 | Bosquejos/predicación para pastores hispânicos (US + LATAM) com calendário litúrgico | **7,0** | PROVADO | US-ES, MX/CO/PE/AR | 111-235 d (3 vendedores BRL) | VERIFICAR | calendário (Natal, Semana Santa), sem fiscalização | média; recorrência | 153+ anúncios, saturando; low ticket US$7-15; é produto "de conteúdo", não de norma |
| 5 | SG-SST micro (<=10) com simulador de visita MinTrabajo | **6,8** | NOVO com mecanismo | CO (PE/MX depois) | 25 anúncios; nenhum com simulador; Solunetpro 13 d, outros serviço | 2,43 mi micronegócios | Res. 0312 + Circular 027/2026 (prazo 31/07/2026 já passou) | alto | mercado lotado e barato; COP baixo |
| 6 | DVR microimpresa + simulatore controllo ASL/ispettorato | **6,5** | NOVO | IT | Beatriz Guerra BR 34 d (5 cr); serviço pesado | 327.850 empresas de ristorazione é só um segmento; total de microimprese VERIFICAR | art. 55 (multa), DL 159/2025 | médio | consultoria forte; sem prazo calendário |
| 7 | HACCP/ASAE kit PT-PT | **6,5** | TESTE/brecha | PT | ninguém com 30+; Studio Facile PT e Novelty Nook 1-2 d | VERIFICAR | ASAE operações 2026 (sem norma datada) | alto | consumidor PT paga €4,90-14,90 (régua); Studio Facile já entrou |
| 8 | Plan de saneamiento/BPM para restaurante e panadería | **6,0** | brecha | CO, PE, MX, CL, AR | ninguém ≥30 d; Aprende y Emprende 2-5 d | MX 772 mil (subsetor) | NOM-251 sem revisão achada | alto | ticket baixo LATAM; sem gancho |
| 9 | APPCC/higiene ES | **5,8** | TESTE | ES | Normattivo 20 d; ePackPro software | VERIFICAR | - | alto | espanhol procura "gratis" |
| 10 | Cuaderno do anfitrião (aluguel curto) FR | **5,0** | brecha | FR | método J'affiche Complet 703 d; kit: ninguém | VERIFICAR | - | baixo | demanda é de curso |
| 11 | Kit groomer (fichas, contrato, SOP) | **4,5** | brecha | ES/LATAM | só cursos 310-926 d | VERIFICAR | - | baixo | ticket e hábito |
| 12 | Wedding planner/fotógrafo (contratos) | **4,0** | VERIFICAR | DE/ES/IT | cursos DE 153-209 d; ES/IT 0 | VERIFICAR | - | baixo | medição incompleta |
| 13 | Gastronomia LATAM (costeo) | **4,0** | módulo | CO/MX | Gastroguias 562 d a US$3,5 | VERIFICAR | - | módulo da Consultora | ticket baixo |
| 14 | Limpeza, empreiteiro, transporte | **3-4** | VERIFICAR | - | falhou 429 (EU/LATAM) | VERIFICAR | - | - | sem dado |

### Diferenças em relação à v1
- v1 colocava 1 = simulado de inspeção (8,5); agora o tema HACCP subiu de risco, não de potencial: surgiram DUAS operações (Andrei 12 d, Quillstone/Studio Facile 24 d) a ~19,6-19,9 €, produto, preço e checkout conhecidos. Passou para 7,8.
- Novo líder: DUERP FR (8,0), por causa da Loi 2026-534 (25/06/2026), confirmada em fonte oficial; v1 não tinha nada de FR/DUERP.
- Corrigidos: Solunetpro (13 d; 15 anúncios; formatos SG-SST), Más seguridad (361 d, MXN, 5 anúncios; produto ainda não lido), Beatriz Guerra (34 d; BRL; 5 anúncios; produto não lido).
- Novo: PL tem vendedor local de documentos HACCP (sklep-haccp.pl; Mango PR 418 d), que a v1 não viu.
- Igreja: agora PROVADO em US-ES (184, 235, 111 dias), v1 dizia "nenhum ≥30 d".
- Pet/cerimonialista/fotógrafo/limpeza/obra/transporte: sem prova de kit nos países medidos; parte da medição incompleta.

## 7. O que continuou VERIFICAR
1. Conteúdo/preço de Más seguridad (MX) e de Beatriz Guerra (IT): abrir os ads 1396762502069360 e 2335666320568282 na Biblioteca (WebFetch 403; navegador travado).
2. Idade real de Studio Facile (920 anúncios) e de Studio Digitale; Andrei passa de 30 dias em ~17/11 (primeiro ativo 18/10): rodar de novo.
3. Alim'confiance: 33.205 controles / 172 fechamentos (só do anúncio); art. R237-2.
4. DUERP FR: data de entrada em vigor da Loi 2026-534 art. 48; valores 4.000/6.000/8.000 vs 7.500/15.000; número de empregadores.
5. IT: valores revalorizados do art. 55; número de microimprese; medição IT de HACCP/DVR/toelettatura/wedding (429).
6. CO: texto da multa (500 SMMLV), prazo do próximo ciclo da Circular 027, boletim DANE.
7. MX: NOM-035 multa em UMA, valor da UMA 2026, jornada 40 h (01/01/2027).
8. PT/ES/RO/CZ/SK/GR/PE/CL/AR: tamanho oficial (INE, INS, ČSÚ, ŠÚ, ELSTAT, INEI, INDEC).
9. Reg. (CE) 852/2004 (EUR-Lex), sanepid/GIS (PL), ANSVSA/DSVSA (RO), ASAE coimas, Ley 29783/SUNAFIL 2026.
10. NL e termos locais em RO/CZ/SK/GR/PL (BHP) por falta de crédito SearchAPI; limpeza, obra, transporte, wedding, fotógrafo em ES/PT/FR/DE/PL/LATAM; igreja em português europeu/Angola/Moçambique.
11. A maioria das fontes de tamanho/gancho acima é secundária (imprensa, blogs de consultoria): reconfirmar nas fontes oficiais antes de qualquer copy.
