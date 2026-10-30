# Catálogo EscalaLow, parte 4 (índices 159 a 212, 54 ofertas): brechas fora do Brasil — 30/10/2026

## Leia primeiro: o que esta rodada consegue e não consegue afirmar
- **SearchAPI sem crédito.** A chave compartilhada tinha 971 créditos quando comecei e caiu para 56 enquanto os outros agentes rodavam. Meu script parou no piso de 400 depois de ~20 buscas medidas por `page_id`. Essas 20 trazem dias reais (marcadas "SA").
- **O resto veio do conector Meta (ads_library_search, só ativos).** Ele devolve só os anúncios MAIS NOVOS primeiro, sem texto do corpo e sem preço. Por isso, quando um vendedor tem muitos anúncios, os **dias são piso** (marcados "piso"). Termos longos em frase exata voltam 0 e podem subestimar. Quando escrevo "ninguém" quero dizer "nenhum vendedor de kit/infoproduto apareceu nos anúncios ativos retornados", não prova de vazio absoluto.
- **Moeda é pista de origem.** Vendedor em BRL ou USD numa página em ES/IT/DE/PL costuma ser operador brasileiro/latino exportando. Conta como sinal de demanda, mas NÃO é vendedor nativo.
- **Conversão de datas do conector:** timestamp 1793318400 = 30/10/2026; dias = (1793318400 menos início) / 86400.
- Não há preço de venda estrangeiro no conector. Só aparece o que estava no título/texto do SearchAPI. Preços de venda abaixo são do JSON do EscalaLow (BR).
- **Web search:** achou poucos números de tamanho (fontes no fim). Gancho legal com data: NÃO confirmei nenhum para esta faixa; onde há data é sazonal (Natal, casamento, maratona) e está marcado.
- Itens de copyright duvidoso (161 desenhos antigos, 163 dramas): excluí da recomendação por risco de direitos autorais, não pesquisei profundamente.
- Evidência "herdada" dos arquivos de 28 e 29/10 (mesma pasta) está marcada **[herdado]**, para não gastar crédito de novo.

---

## 1. Conceitos (agrupados) e profissão/público

| Conceito | Índices | Profissão/público | Termo do produto |
|---|---|---|---|
| A. Apostila de cílios | 170, 205 | Lash designer / educadora lash | apostila editável Canva |
| B. Unhas (curso) | 159 | Manicure/nail designer | curso blindagem/banho de gel |
| C. Barbearia | 186 | Barbeiro / dono de curso | apostila + certificado editável |
| D. Vidraceiro/esquadria | 160, 210 | Vidraceiro, serralheiro de alumínio | maleta de projetos; manual de folgas |
| E. Chaveiro | 190 | Chaveiro residencial | curso completo (WhatsApp) |
| F. Elétrica | 191 | Eletricista | quadros elétricos realistas (esquemas) |
| G. Terapia de casal | 204 | Psicólogo/terapeuta | guia prático |
| H. Psicopedagogia | 211 | Psicopedagogo | apostila de avaliação e intervenção |
| I. TEA crises | 196 | Psicólogo/terapeuta ABA, pais | kit com protocolos e cartões |
| J. Implantodontia visual | 206 | Dentista | mapas clínicos visuais |
| K. Estimulação cognitiva idosos | 194 | Familiar/cuidador | +250 atividades (cadernos) |
| L. Alfabetização/atividades infantis | 166, 178, 182, 188, 197 | Pais e professores | PDF para imprimir |
| M. Caligrafia adulto | 185 | Adulto leigo | 500 atividades cursiva/bastão |
| N. Bebê | 177, 207 | Mães de bebê | introdução alimentar; 151 atividades |
| O. Rotinas infantis | 187 | Pais | 60 modelos de rotina |
| P. Receitas | 162, 164, 175, 179, 192, 202 | Dona de casa / renda extra | laticínios; adventista; 21 dias; lanchinhos; macarrão no pote; pão diabético |
| Q. Mapas/estudo | 168, 172, 173, 208 | Estudantes | atlas bioquímica; supermapas português; "biblioteca"/app |
| R. Finanças/planilhas | 174, 199, 201, 176 | Autônomo/MEI | assistente WhatsApp; gestão; precificação; planner |
| S. Festa/papelaria imprimível | 165, 209, 212, 193 | Artesã de festa, noivas | cestas, kit festa IA, topo de bolo, convites Canva |
| T. Artes prontas | 189, 198, 203 | Designer leigo, igreja, gráfica | músicos/ministério; retrovisor; sublimação |
| U. Artesanato têxtil/couro/3D | 167, 169, 180, 200 | Artesã | STL Natal; moldes couro; tapetes crochê; sousplat |
| V. Fitness | 181, 195 | Praticante | treinos jiu-jitsu; guia corredores |
| W. Religioso | 183, 184 | Evangélico | ebook ansiedade; biblioteca teológica |
| X. Robótica | 171 | Estudante/maker | pack Arduino/MATLAB |
| Y. Entretenimento | 161, 163 | Consumidor | desenhos antigos; dramas |

---

## 2. Tabela com TODAS as 54 ofertas (BR e achado por país)

Legenda: SA = SearchAPI com dias reais; C = conector (piso/janela); cr = criativos; "BR-op" = operador que parece brasileiro/latino (moeda BRL/USD).

| # | Oferta BR (dias/ativos/preço) | Conceito | Achados por país |
|---|---|---|---|
| 159 | Cuticulagem Combinada Premium (168d/13, preço n/d, curso) | B | IT "ricostruzione unghie" 367 ads, SA: só academias (Nails Master Academy 629d/4cr, Nail Artist Academy 513d/3cr), sem kit PDF. ES/FR/GB/PL não medido. Leitura: mercado de curso presencial maduro; kit apostila = VERIFICAR. |
| 160 | Maleta Digital do Vidraceiro (117d/13, R$17) | D | ES (conector, "catálogo vidriería aluminio"): 0. PT/IT/FR/DE: não medido (sem crédito). Leitura: VERIFICAR; ES 0 sugere brecha, termo longo. |
| 161 | 2.500+ Desenhos Antigos (76d/13, R$12,90) | Y | Não pesquisado. Risco de direitos autorais (personagens). Descartado. |
| 162 | Laticínios caseiros (83d/13, preço n/d, WhatsApp) | P | ES 7 ads, nenhum vendedor de kit (Gabriel Ferrari, livros, USD, novo). PL 0. DE: só loja de culturas Kefirko (EUR). FR: sem kit (46 ads de ruído). RO: sem kit. PT: "Tu Ebook Favorito" USD 4cr ~7d (genérico). IT: termo poluído (4.106). Leitura: **BRECHA sem sinal de demanda paga**; Brasil tem cultura de queijo caseiro vendável, Europa compra queijo pronto. |
| 163 | +5.000 Dramas (74d/13, R$19,99) | Y | PL: apps de minidrama (DramaboxLite, USD, 4.387 ads). Direitos autorais; descartado. |
| 164 | Receitas p/ Adventista (70d/13, WhatsApp) | P | Não medido. Prior: RO/ES-LATAM religioso pequeno. VERIFICAR. |
| 165 | 100 Sacolinhas p/ imprimir (46d/13, R$67) | S | ES "bolsitas imprimibles" não medido. Prior: ES-LATAM Kits Listos (PEN), pequeno [herdado]. |
| 166 | Quebra-cabeça tabuada (69d/13, WhatsApp) | L | Termos de tabuada (ES/DE/IT/FR/PL/RO/GB) não medidos. Ver L. |
| 167 | Impressora 3D Natal (60d/12, R$9,90) | U | Prior [herdado]: ES-LATAM e EN saturados com operadores BR (Giselly Reis, Carlos Oliveira). Descartar. |
| 168 | Atlas da Bioquímica (51d/12, R$26,90) | Q | ES: Daniel Herrera "Bioquímica en resúmenes visuales" BRL ~7d, Estudia Sencillo BRL ~13d (C): **BR-op entrando, <30d**. PL "biochemia notatki": 7 ads, só Eduloop (curso biologia) PLN. Outros não medido. |
| 169 | Guia dos Moldes (couro/guasqueiro) (445d/12, R$36,90) | U | Não medido. Nicho gaúcho, sem equivalente evidente. Descartar para Europa; ES-LATAM (AR/UY gaucho) = ideia VERIFICAR. |
| 170 | Apostila de Cílios (118d/12, R$47) | A | **ES (C, piso):** Zenah Sanchez Beauty (a própria dona BR) USD "Producto 100% en español", 4 ads, ~118d; Dollis Templates USD ~11d ("Empieza a enseñar extensiones"); Universo Pestañas BRL "$7" ~7d; pestanas.vlc curso básico ~4d. **PT-PT (SA):** Zenah 119d/6cr. **IT (SA):** 334 ads, só salões e academias, nenhum kit. **FR (SA):** Estheca (fornecedor) 901d/16cr, sem apostila. **DE (SA):** 1 anúncio (academia). GB: 0. |
| 171 | Pack Mecatrônica e Robótica (164d/12, R$27) | X | ES "robótica Arduino": 0. IT: STEM in Classe USD ~12d, 17 ads (educação infantil, não é pack técnico). Outros não medido. |
| 172 | Supermapas de Língua Portuguesa (88d/12, R$57) | Q | Ver `mapas-mentais-por-pais-2026-10-29.md` [herdado]: ES oposiciones 9,0, PL matura 8,5. Lengua/gramática específica não medida (VERIFICAR). |
| 173 | Biblioteca de Arquivos (82d/12, R$9,90) | Q | Oferta vaga (app hospedado em run.app, anunciante de velas). VERIFICAR o que vende antes de buscar. |
| 174 | Assistente financeiro WhatsApp (79d/12, R$10) | R | Não medido. VERIFICAR (apps de despesa saturados). |
| 175 | 21 dias comendo bem (85d/12, WhatsApp) | P | ES "alimentación" janela: Bihotzcare "28 días de comidas" EUR (novo). Resto não medido. |
| 176 | Meu Planner FEITO (85d/12, R$9,90) | R | Não medido. Prior: planner "não vale" (28/10). |
| 177 | Guia Introdução Alimentar (170d/12, R$12,90) | N | **ES (C):** 60 ads; Academy Bebe BRL "Guía de Alimentación Complementaria" (BR-op), Sabores para Mi Bebé USD (novo), Bihotzcare EUR. IT/PL [herdado]: criadores locais fortes (BabyRicette di Anna, Dietista Verdiana Ramina EUR). DE/FR/PT não medido. |
| 178 | Combo das Sílabas (57d/12, R$10) | L | Prior [herdado]: RO Mister Shop 25d; IT Attivita Premium 13 ads; PT atividadespremium.pt 98d/5cr; ES-LATAM saturado. |
| 179 | 56 lanchinhos air fryer (56d/12, preço n/d) | P | Não medido (lunchbox). Prior [herdado]: air fryer FR Tuto Airfryer 47d/18cr, Mon Airfryer 34d/13cr; DE MaMa Verlag 55d. |
| 180 | 50 Tapetes em Crochê (53d/12, R$10) | U | ES "alfombras de ganchillo": 2 ads (app Mega Apps USD novo). DE "Häkelanleitung": 137 ads, Crochet school USD novo (anúncios de Natal); IT "uncinetto schemi": 208 ads, Espacio Noble Home USD novo (3 ads de 0 dias visíveis); PL: Katarzyna Kowalska USD, 19 ads, novo. Prior [herdado]: DE Stitchy 35d/11cr; ES Las Tijeras Mágicas 123d (loja). Leitura: **demanda existe e há BR/LATAM-op novos em DE/IT/PL**, mas sem vendedor nativo de 30+d de PDF medido. |
| 181 | +600 Treinos de Jiu-Jitsu (115d/11, R$29,90) | V | ES 0 (entrenamiento jiu jitsu en casa). IT/GB/DE/FR/PL: não medido (GB voltou ruído). Leitura: BRECHA provável, nicho pequeno na Europa. |
| 182 | Kit +50 Atividades (70d/11, R$37) | L | Ver L. |
| 183 | Ebook 3 passos ansiedade, bíblico (112d/11, preço n/d) | W | Não medido. Prior [herdado]: RO bíblia pequeno; ES-LATAM saturado. |
| 184 | Biblioteca Teológica (129d/11, R$39,90) | W | Não medido. Prior [herdado]: igual 183. Direitos autorais de livros = risco. |
| 185 | Kit Caligrafia Adultos 500 (53d/11, R$19,90) | M | **DE "Schreibschrift Erwachsene": 0. IT "calligrafia adulti": 0.** ES: Impulso Creativo USD, 26 ads, ~2d (BR-op novo). FR/GB/PL: não medido (SA parou). |
| 186 | Guia da Maqui Barber Kit (154d/11, R$57) | C | ES "curso de barbería" 12 ads (SA): só academias (Josep Pons 174d/1cr, CENTE 80d, Fanny Academy 11d/4cr). IT "corso barbiere" 34 ads: Professione Accademia 292d/4cr, Formapro 47d, PM Formazione 20d/22cr (cursos presenciais). GB "barber course" 13 ads: Studio26 66d/2cr. **Nenhum vende apostila/kit digital editável.** |
| 187 | 60 modelos de rotina 4 a 16 anos (152d/11, R$27,90) | O | DE "Routinekarten Kinder": 0. Outros países não medidos. |
| 188 | Atividades de Caligrafia Infantil (123d/11, R$15) | L | Ver L. |
| 189 | Artes p/ Ministério / Design p/ Músicos (189d/11, R$15,20) | T | Não medido. VERIFICAR (templates de igreja em EN/ES provavelmente saturados). |
| 190 | Curso Chaveiro Residencial (78d/11, WhatsApp) | E | ES "cerrajería": 108 ads, tudo serviço (Tecno-key, Cerrajería Badra "apertura urgente 92 €", EAATA); MX: 26 ads, Info Master USD (cursos genéricos, 8 ads ~1d). GB/IT/FR/DE/PL: não medido. **Nenhum vendedor de curso/kit de chaveiro.** |
| 191 | Quadros Elétricos Realistas (188d/11, R$67) | F | ES "cuadros eléctricos": 3 ads, Nova Mind USD "Manual del Electricista Residencial" ~5d (BR-op). Prior [herdado]: AR/PE cópias do BR ~16d, 12 ads. DE/IT/PL/FR: não medido. |
| 192 | Macarrão no pote (133d/11, WhatsApp) | P | Não medido. VERIFICAR. |
| 193 | 14 convites digitais p/ noivas, Canva (103d/11, R$47) | S | ES: Pack de Plantillas USD, 6 ads, ~8d ("pack de invitaciones listos para editar 4.9/5") (BR-op). IT/DE/PT-PT: 0 (termo longo, pode subestimar). |
| 194 | Mente Ativa 250 (idosos) (65d/11, WhatsApp) | K | [herdado 29/10] DE CareTable 127d/9cr + The Resource Lab (USD, novo 29/10); IT Seduta Pronta e The Mind Market (USD, ~22/10); FR SilverSessions; PL CKO ~27d; PT-PT Mais Educação (BRL, BR-op); RO Creative Box 22d; ES-LATAM saturado (369 ads). |
| 195 | Guia Completo p/ Corredores (79d/11, R$9,90) | V | ES "plan de entrenamiento 10k": Carlos Villauba BRL (BR-op) <1d; DE "Laufplan": Coach Camille Dubois USD ~3d; FR: app Campus.coach CAD (111 ads); PL: treinadores locais PLN (Adrian Zambrzycki); IT "tabella allenamento mezza maratona": 0; PT: ruído. |
| 196 | Kit Acalmar TEA (57d/11, R$27) | I | ES: teanexia EUR, 1 ad, ~11d. IT [herdado]: ABA Tools 90d/9cr (fichas de terapia infantil, **provado**). IT "autismo attività": só editora Erickson. DE/FR/GB: 0 nos termos testados. |
| 197 | Kit Completo p/ Imprimir SARESP (63d/11, R$59,70) | L | SARESP é prova paulista; sem equivalente 1:1. Análogos: IT INVALSI (0 no termo testado), PL egzamin ósmoklasisty [herdado]. |
| 198 | Pack de Artes p/ Retrovisor (146d/10, R$10) | T | **ES "colgante espejo retrovisor": 0.** MX mesmo termo: 0. Leitura: novidade local BR, sem prova em lugar nenhum. |
| 199 | Gestão Financeira ebook (144d/10, R$37) | R | Não medido. VERIFICAR (concorrência enorme esperada). |
| 200 | Sousplat (107d/10, WhatsApp) | U | Não medido. Nicho BR (sousplat = prato de apoio de crochê/EVA). VERIFICAR. |
| 201 | Planilha de Precificação (374d/10, R$10) | R | Prior [herdado]: ES-LATAM 1 anúncio, sem prova. PT/IT/GB não medido. |
| 202 | Pães p/ diabéticos (135d/10, WhatsApp) | P | [herdado] RO Editura Gold ~440d (**provado**, RON); PL Tłuste Gary, Mister Shop (clone BR), Małe Nawyki, 361 ads; IT L'Arte di Nutrirsi Bene (MXN); DE Peyton Ashford (USD). |
| 203 | Pack Sublimação Premium (172d/10, R$14,90) | T | **ES (C, piso):** Pixelpack USD "+500.000 diseños por US$9.99" ~42d (BR-op), PixelPack-DFT BRL ~14d, "Diseños para Sublimación" USD ~6d. DE "Sublimation Vorlagen Tassen": 0. IT: 0. PT/FR/PL/GB: não medido. |
| 204 | Guia p/ Atender Casais (69d/10, R$27) | G | ES (SA) 176 ads: cursos e clínicas (Psiko Aprende 219d, Creando Diálogos 153d). IT 82: Master Spazio IRIS 85d, Unobravo 138d. DE 293: coach Doktor Hermes 619d/4cr. FR 79: cursos (MN Coaching 153d/8cr, L'Espace du Couple 127d/9cr). GB 312: ARC System 463d, **ClearMind Counseling 128d/2cr** (cheat sheet de técnicas para terapeutas = o produto mais parecido). Nenhum kit/guia para o terapeuta fora do GB. |
| 205 | 4 Apostilas Lash (80d/10, R$37) | A | Ver 170. |
| 206 | Biblioteca Clínica Visual, implantodontia (73d/10, R$19) | J | ES "implantología dental": 981 ads, só clínicas (Smylife). Sem kit visual de estudo. IT/DE/GB/PL/FR: não medido (SA parou). Cruzar com `dentista-*-2026-10-29.md`. |
| 207 | Desenvolve Bebê, 151 atividades (46d/10, R$57) | N | ES "estimulación temprana bebés": 75 ads, clínicas e talleres (toencasa.tea, Mi otro yo), nenhum kit PDF. DE/IT/FR/GB/PT/PL: não medido. |
| 208 | Bibliopédia, app de estudos (106d/10, preço n/d) | Q | Oferta vaga. VERIFICAR. |
| 209 | Kit de Festas com IA (46d/10, curso) | S | Não medido. Curso, não kit. |
| 210 | Manual Técnico Esquadria PRO (89d/10, R$67) | D | Referente à linha Suprema (marca BR de esquadrias), então é produto específico de fabricante. Equivalente local = manual por fabricante (Schüco, Technal, Reynaers). VERIFICAR. |
| 211 | Apostila de Avaliação e Intervenção Psicopedagógica (48d/10, R$10) | H | **ES (C, piso):** "Psicopedagogia sem Pressão" (BR-op, página .com.br em ES) "75 Pruebas Psicopedagógicas Esenciales", ~100d, 1 cr visível. IT "valutazione DSA": 8 ads, só clínicas (Pegaso 153d, Affidea CDC 44d). Outros não medido. |
| 212 | +100 Moldes topo/vela cenário (47d/10, R$11,99) | S | Não medido (cake topper). VERIFICAR; sazonal Natal. |

---

## 3. Ranking 0 a 10 das brechas mais fortes desta faixa

Critérios (0 a 2 cada): prova de demanda, tamanho, gancho/data, ticket, facilidade de adaptar. Nota máxima 10. "[herdado]" = evidência dos arquivos de 28 e 29/10 nesta mesma pasta, que reaproveito sem remedir.

| # | Brecha (oferta × país) | Nota | Tipo | Evidência | Tamanho (fonte) | Gancho | Reaproveitamento |
|---|---|---|---|---|---|---|---|
| 1 | **Pães/receitas p/ diabéticos (202) × Romênia** [herdado] | 8,5 | PROVADO | Editura Gold ~440d, RON (`arbitragem-kits-br-2026-10-29.md`) | n/c nesta rodada | Não confirmado | Receitas locais baixo IG; sem promessa de cura |
| 2 | **Estimulação cognitiva idosos (194) × Alemanha** [herdado] | 8,0 | PROVADO, janela fechando | CareTable 127d/9cr; Resource Lab entrou 29/10 | Betreuungskräfte (§43b SGB XI) citado no arquivo herdado, não reverificado | Não confirmado | Valigetta/Consultora: não; kit de atividades; trocar para Biografiearbeit |
| 3 | **Kit TEA/terapia infantil (196) × Itália** [herdado + novo] | 6,5 | PROVADO (adjacente) | ABA Tools IT 90d/9cr [herdado]; Kit Acalmar: protocolos de crise sem concorrente direto em IT/DE/FR/GB (0 nos termos testados); ES teanexia 1 ad ~11d | n/c | Não confirmado | Aproveitar logo de psicólogo/Fono; "sem diagnóstico" |
| 4 | **Apostila de cílios/lash editável (170, 205) × IT, FR, DE** | 6,5 | BRECHA nos 3, PROVADO por BR-op em ES/PT | ES: Zenah 118d USD + 3 BR-op novos; PT-PT Zenah 119d/6cr; IT 334 ads só salões/academias; FR só fornecedor; DE 1 ad | Espanha tem ~72.300 estabelecimentos de peluquería e estética (DBK 2021, fonte no fim); IT/FR/DE não pesquisei | Natal/festas (sazonal), sem lei | Ticket BR R$37 a R$47; template Canva traduz fácil; **ES já tem o BR vendendo, então IT/DE é a janela** |
| 5 | **Apostila + certificado p/ barbeiro (186) × ES, IT, GB** | 6,5 | BRECHA | Só academias presenciais (ES 12 ads, IT 34, GB 13); zero kit digital | n/c (barbearia em alta, não quantifiquei) | Sem data | Apostila editável pra o dono de curso (B2B do próprio barbeiro) |
| 6 | **Avaliação psicopedagógica (211) × Itália (DSA)** | 6,0 | BRECHA IT, PROVADO por BR-op em ES (100d) | IT 8 ads, só clínicas; ES: "75 Pruebas" BR-op 100d | Espanha: 4.611 orientadores citados em doc da UMH 2022 (fonte no fim; leitura incerta) | DSA/Lei 170/2010 não verificada | Cruzar com Psicólogo Itália (La Valigetta dello Psicologo) |
| 7 | **Caligrafia p/ adultos (185) × DE e IT** | 6,0 | BRECHA aparente | DE 0, IT 0; ES só BR-op novo (~2d) | n/c | Natal (cartões escritos à mão), sazonal fraco | Produto simples; ticket baixo |
| 8 | **Sublimação (203) × DE e IT** | 5,5 | BRECHA aparente; PROVADO por BR-op em ES (~42d) | ES Pixelpack ~42d USD; DE e IT 0 (termos longos, pode subestimar) | n/c | Natal (canecas) | Packs de arte; risco de licença dos desenhos |
| 9 | **Terapia de casal, guia p/ terapeuta (204) × ES, IT, DE, FR** | 5,5 | BRECHA parcial | Só cursos/clínicas/coaches; GB ClearMind 128d é o único parecido | n/c | Sem data | Dentro do plano Valigetta do Psicólogo |
| 10 | **Quadros elétricos/esquemas (191) × ES, DE, IT** | 5,5 | TESTE | ES Nova Mind USD ~5d (BR-op), AR/PE cópias ~16d [herdado]; DE/IT não medido | Alemanha: ZVEH, dado de empregados desatualizado e não obtido (fonte no fim) | Norma local (REBT na ES, DIN VDE 0100 na DE) não pesquisada | **Reaproveita o app de inspeção**; trocar norma |
| 11 | Convites digitais de casamento Canva (193) × ES, IT, DE, PT | 5,0 | TESTE | ES Pack de Plantillas USD ~8d; IT/DE/PT 0 | Espanha: 179.107 casamentos em 2022 (bodas.net via INE; 2025 não obtido) | Sazonal: casamentos de 2027 | Pacote Canva fácil |
| 12 | Chaveiro (190) × ES, MX | 5,0 | BRECHA | ES 108 ads e MX 26 ads, só serviço e cursos genéricos | Espanha: sem número do setor (busca não achou; DIRCE por CNAE seria a fonte) | Pode exigir habilitação em segurança privada (não verificado) | Curso/apostila de baixo ticket |
| 13 | Bioquímica visual (168) × ES e PL | 5,0 | TESTE | ES BR-op ~7 e ~13d; PL 0 de notas | n/c | Calendário universitário | Prior: mapas por país [herdado] |
| 14 | Guia de corredores (195) × IT/DE | 5,0 | BRECHA parcial | IT 0; DE operador USD novo ~3d; PL treinadores locais | Maratona de Madrid 2027: 17.000 vagas de maratona e 30.000 de meia (eldiario via madridinforma); Valencia lotou 33.000 a 35.000 dorsais em 2023/2024 | Data de Valencia 2026: 06/12/2026 (fonte secundária, trainerday); 2027 (05/12) é de blog, não confirmado | Planilhas PDF |
| 15 | Tapetes de crochê (180) × DE, IT, PL | 4,5 | TESTE saturando | BR/LATAM-op novos em DE/IT/PL com Natal; sem vendedor nativo de 30+d medido | n/c | Natal | Concorrência de apps e padrões grátis |

**Não recomendo:** 161 e 163 (direitos autorais), 167 e demais STL (saturado), 169 (nicho gaúcho), 176 (planner), 173 e 208 (oferta vaga).

---

## 4. O que continuou VERIFICAR (e por que)

1. **Dias reais de quase tudo que veio do conector** (os "piso"): precisa de SearchAPI (renova em 08/11) ou da própria biblioteca com `page_id`. Prioridade: Zenah (ES/PT), Pixelpack (ES), "Psicopedagogia sem Pressão" (ES), Academy Bebe (ES), Espacio Noble Home (IT), Crochet school (DE).
2. **Vidraceiro/esquadria (160, 210)**: só 1 termo ES medido (0). Falta PT, IT, FR, DE, PL, GB e MX/AR/CO.
3. **Cursos/países não buscados por falta de crédito:** unhas (ES/FR/GB/PL), chaveiro (IT/FR/DE/GB/PL), quadros elétricos (DE/IT/PL/FR), cheese em GB, adventista, macarrão no pote, 21 dias, lanchinhos, precificação, assistente WhatsApp, finanças (R), artes p/ igreja (189), cake topper e kit festa (209, 212, 165), sousplat, ebook ansiedade e biblioteca teológica, jiu-jitsu fora da ES, rotinas fora da DE, bebê (DE/IT/FR/GB/PT/PL), tabuada.
4. **Ofertas vagas** (173, 208): abrir a página de vendas para saber o produto.
5. **Preço de venda estrangeiro:** o conector não entrega. Não abri nenhuma página estrangeira nesta rodada; só o ClearMind (GB) e Zenah têm URL conhecida (zenahacademy.com.br).
6. **Gancho legal com data:** nenhum confirmado. Os candidatos a checar: DSA (Lei 170/2010, IT), REBT (ES) e DIN VDE 0100 (DE) para elétrica, habilitação de chaveiro na ES.
7. **Tamanho de profissão:** só três números parciais (abaixo). Faltam: nº de barbeiros, lash designers, cerrajeros, psicopedagogos e Elektrofachkräfte com fonte oficial.
8. Validar a leitura de "0 anúncios" nas buscas longas (convites, sublimação, retrovisor, caligrafia): repetir com termo curto antes de chamar de BRECHA firme.

## 5. Fontes citadas (web search desta rodada)
- Estabelecimentos de peluquería e estética na Espanha (72.300 em 2021, DBK): https://dbk.es/en/estudios/16575/summary
- Casamentos na Espanha em 2022 (179.107, bodas.net citando INE): https://www.bodas.net/articulos/es-verdad-que-en-espana-las-parejas-ya-no-se-casan--c9283 ; metodologia INE: https://ine.es/dynt3/metadatos/RespuestaDatos.htm?oper=305
- Maratona e meia de Madrid 2027 (17.000 + 30.000 vagas): https://madridinforma.eldiario.es/?p=50535
- Maratona de Valencia lotada (33.000 dorsais): https://espndeportes.espn.com/espn-run/nota/_/id/12024980/el-maraton-de-valencia-agoto-los-33000-dorsales ; 2026 em 06/12 (secundária): https://trainerday.com/el/events/es/maraton-valencia-2026-2026
- Orientadores na Espanha (4.611, leitura incerta): https://comunicacion.umh.es/files/2022/05/12-05-22-jornada-orientacion-educativa.pdf
- Setor elétrico alemão (ZVEH, crescimento de emprego 2022 a 2023): https://www.handwerksblatt.de/handwerkspolitik/e-handwerke-fachkraeftemangel-verschaerft-sich
- Evidências herdadas: `arbitragem-kits-br-2026-10-29.md`, `mapas-mentais-por-pais-2026-10-29.md`, `brechas-europa-2026-10-28/arbitragem-br-eu/resultado.json` (mesma pasta de pesquisas).
