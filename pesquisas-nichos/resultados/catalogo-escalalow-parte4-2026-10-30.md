# Catálogo EscalaLow — parte 4 (índices 159 a 212) — 30/10/2026

> **Avisos de método (ler antes)**
> - A v1 (29/10) e os relatórios citados em "Ler antes" **não estavam acessíveis** neste ambiente (ficam no Desktop). Este relatório foi feito do zero, com o JSON `dados/escalalow-ofertas-validadas.json` (índices 159–212 = 54 ofertas) e as notas em `notas/`. Por isso **não há comparação com a v1**.
> - **SearchAPI indisponível** (sem chave neste container e sem crédito até 08/11). Toda medição de anúncios foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
> - O conector devolve página, título do link, data de início e moeda. **Não devolve o texto do anúncio nem o link de destino**, e o facebook.com está bloqueado pela rede do container. A classificação de cada anunciante vem do nome da página, do título e da moeda.
> - A busca por `page_id` devolve no máximo 50 anúncios, os mais novos primeiro. Quando a página tem mais de 50 anúncios, o número de dias é um piso (marcado "≥").
> - **Páginas de vendas e fontes oficiais não abriram.** O WebFetch foi bloqueado pela lista de domínios da rede (eletricadealtaperformance.com.br, maletadovidraceiro.lovable.app, gazzettaufficiale.it). O WebSearch esgotou o limite de 200 buscas por turno, que é compartilhado com os agentes irmãos. Por isso preço, conteúdo, normas e tamanho de mercado **não foram confirmados com fonte nesta rodada** e estão marcados VERIFICAR.
> - **DIAS** = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página. "(termo)" quer dizer que o dia foi medido na busca por termo, não por page_id; é um piso.
> - **Moeda.** USD ou BRL em anúncio escrito em espanhol, italiano etc. é quase sempre operador brasileiro e não prova o país. Moeda local (MXN, PEN, ARS, COP, CLP, ou EUR de página nativa) é sinal de vendedor local.
> - **Régua.** PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.

## Resumo

1. **Maior achado: onda de clones brasileiros do "Quadros Elétricos Realistas" (191) na Europa, iniciada há 1 a 8 dias.** São páginas novas em USD/BRL, com perfil de operador BR, em IT, ES, CZ e PL: Studio Quadri (213 anúncios em italiano, tcheco e polonês), Tablero Studio, Marco Ferri, Claude Ingegneria Elettrica PRO e Arquimax-Academy. Ninguém está PROVADO ainda, então a janela é curta.
2. **Estimulação cognitiva para idosos (194).** PROVADO no Peru: Cognimente, em PEN, há 64 dias, com 37 anúncios. Uma onda brasileira começou em IT, DE, PT, EN e ES nas últimas duas semanas. A França está zerada.
3. **Apostila editável para instrutoras de cílios e barbeiros (170/205/186).** PROVADO em espanhol neutro pela própria Zenah: 119 dias, em USD. O inglês está quase vazio e IT, PT e FR estão zerados.
4. **Kit do vidraceiro (160/210).** Em espanhol só existe um clone brasileiro com 1 dia ("Kit del vidriero", USD). MX, PT e IT não têm ninguém.
5. **O resto da faixa é consumo ou está fora do escopo.** Receitas, festas, atividades infantis, sublimação, crochê e arquivos STL estão saturados em espanhol. Doramas e desenhos antigos têm problema de direito autoral.

## 1. Ofertas da faixa (159–212): profissão/público, termo e conceito

Dias, ativos e preço são os do JSON do EscalaLow (Brasil). Uma letra igual na coluna "Conceito" indica o mesmo conceito.

| Índ. | Oferta (BR) | Dias BR | Ativos BR | Preço BR | Profissão / público | Termo do produto | Conceito | Resultado fora do BR (resumo; detalhe na seção 2) |
|---|---|---|---|---|---|---|---|---|
| 159 | Cuticulagem Combinada Premium | 168 | 13 | — | Manicures / nail designers | curso blindagem + banho de gel | G: curso de beleza | não medido (curso) |
| 160 | Maleta Digital do Vidraceiro | 117 | 13 | R$ 17,00 | Vidraceiros | maleta digital: projetos prontos + catálogo | A: vidraceiro | ES-LATAM TESTE (1 clone BR, 1d); MX/PT/IT BRECHA |
| 161 | 2.500+ Desenhos Antigos para Reviver | 76 | 13 | R$ 12,90 | Público geral (nostalgia) | acervo de desenhos antigos | Z: fora (direito autoral) | fora |
| 162 | 🧀LATICÍNIOS CASEIROS QUE VENDEM TODOS OS DIA… | 83 | 13 | — | Renda extra (cozinha) | laticínios caseiros p/ vender | L: receitas p/ vender | não medido |
| 163 | 🎬 +5.000 Dramas | 74 | 13 | R$ 19,99 | Público geral | acervo +5.000 doramas | Z: fora (direito autoral) | fora |
| 164 | Se você é Adventista e tá tentando deixar su… | 70 | 13 | — | Adventistas | alimentação/receitas adventistas | M: receitas saúde/dieta | não medido |
| 165 | 100 Sacolinhas para Imprimir | 46 | 13 | R$ 67,00 | Festeiras / papelaria personalizada | 100 sacolinhas p/ imprimir | N: festa/papelaria | ES neutro PROVADO (cienacres 507d) |
| 166 | Um quebra-cabeça, três peças, uma tabuada be… | 69 | 13 | — | Pais / professores 1º ciclo | quebra-cabeça de tabuada | J: atividades infantis | ES-LATAM PROVADO/saturado; IT PROVADO + onda BR |
| 167 | Por menos , ganhei acesso VITALÍCIO a TUDO I… | 60 | 12 | R$ 9,90 | Donos de impressora 3D | pacote de arquivos STL | O: artesanato/maker | ES saturado (640 anúncios) |
| 168 | Atlas da Bioquímica | 51 | 12 | R$ 26,90 | Estudantes saúde (bioquímica) | atlas visual / mapas | K: mapas visuais/estudo | não medido (ver relatório irmão de mapas) |
| 169 | Guia dos Moldes | 445 | 12 | R$ 36,90 | Guasqueiros / artesãos de couro | guia de moldes de couro | O: artesanato/maker | AR TESTE nativo (17,5d) |
| 170 | Apostila de Cílios | 118 | 12 | R$ 47,00 | Instrutoras de cílios (lash) | apostila editável p/ curso | F: apostila editável p/ instrutor | ES neutro PROVADO (Zenah 119d); EN TESTE; IT/PT/FR BRECHA |
| 171 | Pack Digital de Mecatrônica e Robótica | 164 | 12 | R$ 27,00 | Estudantes técnicos | pack mecatrônica/robótica | G: curso técnico | não medido |
| 172 | Supermapas de Língua Portuguesa | 88 | 12 | R$ 57,00 | Concurseiros / estudantes | mapas mentais de português | K: mapas visuais/estudo | não medido (ver relatório irmão de mapas) |
| 173 | Biblioteca de Arquivos | 82 | 12 | R$ 9,90 | Estudantes (genérico) | biblioteca de arquivos | K: mapas visuais/estudo | não medido |
| 174 | Use para Vida Pessoal e de Trabalho | 79 | 12 | R$ 10,00 | Pessoa física / MEI | assistente financeiro no WhatsApp | P: finanças/planilhas | não medido |
| 175 | “Imagina passar 21 dias comendo bem e sem aq… | 85 | 12 | — | Mulheres (dieta) | cardápio 21 dias | M: receitas saúde/dieta | não medido |
| 176 | Meu Planner FEITO | 85 | 12 | R$ 9,90 | Público geral | planner digital | N: festa/papelaria | não medido |
| 177 | Guia Introdução Alimentar | 170 | 12 | R$ 12,90 | Mães de bebês 6–24m | introdução alimentar (cardápios) | M: receitas saúde/dieta | ES TESTE (2 vendedores novos) |
| 178 | Combo das Sílabas | 57 | 12 | R$ 10,00 | Pais / alfabetizadoras | combo de sílabas | J: atividades infantis | ES-LATAM PROVADO/saturado; IT PROVADO + onda BR |
| 179 | Todo santo dia é a mesma coisa | 56 | 12 | — | Mães (lancheira) | 56 lanchinhos air fryer | M: receitas saúde/dieta | não medido |
| 180 | 50 Tapetes em Crochê | 53 | 12 | R$ 10,00 | Crocheteiras | 50 tapetes/peças em crochê | O: artesanato/maker | ES onda BR (<1d) |
| 181 | +600 Treinos de Jiu-Jitsu em Casa | 115 | 11 | R$ 29,90 | Praticantes de jiu-jitsu | +600 treinos em casa (app) | Q: fitness | ES BRECHA (2 anúncios) |
| 182 | Kit +50 Atividades Educativas para Crianças | 70 | 11 | R$ 37,00 | Pais / professores EI | +50 atividades educativas | J: atividades infantis | ES-LATAM PROVADO/saturado; IT PROVADO + onda BR |
| 183 | Ebook: 3 Passos para vencer a Ansiedade | 112 | 11 | — | Cristãos | e-book ansiedade (bíblico) | R: religioso | não medido |
| 184 | Biblioteca Teológica Atualizada | 129 | 11 | R$ 39,90 | Pastores / seminaristas | biblioteca teológica digital | R: religioso | ES neutro PROVADO por BR (112d) |
| 185 | Kit Caligrafia para Adultos com 500 | 53 | 11 | R$ 19,90 | Adultos | caligrafia p/ adultos (500 ativ.) | J: atividades infantis | ES TESTE (clones BR <2d) |
| 186 | Guia da Maqui | 154 | 11 | R$ 57,00 | Barbeiros instrutores | Barber Training Kit (apostila editável + certificados) | F: apostila editável p/ instrutor | ES BRECHA (só escolas); EN: a própria Bucha, 1 anúncio, 49d |
| 187 | 60 modelos dos 4 aos 16 anos | 152 | 11 | R$ 27,90 | Pais (4–16 anos) | 60 modelos de rotina/disciplina | S: parentalidade | ES TESTE (≤8d) |
| 188 | Atividades de Caligrafia Infantil | 123 | 11 | R$ 15,00 | Pais / professores | caligrafia infantil (cursiva) | J: atividades infantis | MX PROVADO (Stardex 269d termo); PE 67d |
| 189 | Artes Profissionais para seu Ministério | 189 | 11 | R$ 15,20 | Músicos / ministérios | +2.500 artes editáveis p/ shows | N: festa/papelaria | não medido |
| 190 | 🔑 Quer aprender uma profissão que sempre tem… | 78 | 11 | — | Renda extra | curso de chaveiro | G: curso técnico | ES genérico (multicurso) |
| 191 | Quadros Elétricos Realistas | 188 | 11 | R$ 67,00 | Eletricistas | quadros elétricos realistas (montar e mostrar ao cliente) | B: eletricista | IT/CZ/PL/ES/PT TESTE (onda BR 1–8d); FR BRECHA |
| 192 | GUIA COMPLETO | 133 | 11 | — | Renda extra (cozinha) | macarrão no pote p/ vender | L: receitas p/ vender | não medido |
| 193 | 14 convites digitais | 103 | 11 | R$ 47,00 | Noivas | 14 convites digitais (Canva) | N: festa/papelaria | MX PROVADO (65d); BR em ES 85d |
| 194 | Sua mãe, seu pai ou alguém que você ama pass… | 65 | 11 | — | Filhos de idosos / cuidadores | Mente Ativa 250 (estimulação cognitiva) | H: estimulação cognitiva idosos | PE PROVADO (Cognimente 64d); ES/IT/DE/PT/EN TESTE; FR BRECHA |
| 195 | Guia Completo para Corredores | 79 | 11 | R$ 9,90 | Corredores | planilhas de treino 3k–42k | Q: fitness | ES: o próprio BR testa (5,6d); coaching AR 99d |
| 196 | Kit Acalmar | 57 | 11 | R$ 27,00 | Psicólogos / terapeutas TEA | Kit Acalmar (crises no TEA) | C: psicólogo (módulos) | ES-LATAM só genéricos (Kits Digitales MXN 139d, VERIFICAR) → TESTE |
| 197 | Kit Completo para Imprimir | 63 | 11 | R$ 59,70 | Professores 5º ano (SP) | 41 simulados SARESP | I: simulados de avaliação externa | IT BRECHA (só editoras); CO BRECHA p/ professor |
| 198 | Pack de Artes para Retrovisor | 146 | 10 | R$ 10,00 | Comunicação visual / vendedores | +160 artes p/ adesivo de retrovisor | N: festa/papelaria | não medido |
| 199 | GESTÃO FINANCEIRA | 144 | 10 | R$ 37,00 | Pequenos empresários | e-book gestão financeira | P: finanças/planilhas | não medido |
| 200 | O segredo das mulheres que vendem Sousplat t… | 107 | 10 | — | Artesãs (renda extra) | sousplat p/ vender (curso PDF) | O: artesanato/maker | não medido |
| 201 | Planilha de Precificação Inteligente | 374 | 10 | R$ 10,00 | Pequenos empresários | planilha de precificação | P: finanças/planilhas | não medido |
| 202 | 🥖 +50 RECEITAS de PÃES para DIABÉTICOS que q… | 135 | 10 | — | Diabéticos | +50 receitas de pães | M: receitas saúde/dieta | ES-LATAM concorrido (200 anúncios) |
| 203 | Pack Sublimação Premium | 172 | 10 | R$ 14,90 | Personalizados (canecas) | pack de artes p/ sublimação | N: festa/papelaria | ES saturado (81 anúncios) |
| 204 | Guia Prático para Atender Casais | 69 | 10 | R$ 27,00 | Psicólogos (casal) | guia prático p/ atender casais | C: psicólogo (módulos) | ES-LATAM só genéricos; IT BRECHA |
| 205 | 4 APOSTILAS LASH BRASIL | 80 | 10 | R$ 37,00 | Instrutoras de cílios (lash) | 4 apostilas editáveis (Canva) | F: apostila editável p/ instrutor | ES neutro PROVADO (Zenah 119d); EN TESTE; IT/PT/FR BRECHA |
| 206 | Biblioteca Clínica Visual | 73 | 10 | R$ 19,00 | Dentistas (implante) | biblioteca clínica visual de implantodontia | D: dentista (mapas clínicos) | ES/IT BRECHA |
| 207 | +151 atividades práticas | 46 | 10 | R$ 57,00 | Mães de bebês 0–12m | 151 atividades de estimulação | S: parentalidade | ES TESTE (PEN 23d) |
| 208 | Bibliopédia— Aplicativo de Estudos | 106 | 10 | — | Estudantes | app de estudos (Bibliopédia) | K: mapas visuais/estudo | não medido |
| 209 | Kit de Festas com IA | 46 | 10 | — | Festeiras | curso kit de festa com IA | N: festa/papelaria | ES neutro PROVADO (cienacres 507d) |
| 210 | Manual Técnico Esquadria PRO | 89 | 10 | R$ 67,00 | Vidraceiros / serralheiros | manual técnico de esquadrias (folgas, perfis) | A: vidraceiro | ES-LATAM TESTE (1 clone BR, 1d); MX/PT/IT BRECHA |
| 211 | Apostila Completa de Avaliação e Intervenção… | 48 | 10 | R$ 10,00 | Psicopedagogos | apostila de avaliação e intervenção | C: psicólogo (módulos) | ES-LATAM: clínicas; material só BR (4,5d) → TESTE/BRECHA |
| 212 | ✂️ +100 MOLDES | 47 | 10 | R$ 11,99 | Artesãs de personalizados | +100 moldes topo/vela cenário | N: festa/papelaria | ES neutro PROVADO (cienacres 507d) |

**Conceitos agrupados.** Profissionais primeiro, que é o modelo do usuário (kit de documentos + app por profissão).
- **A. Vidraceiro:** 160, 210 (dois vendedores BR, 117d e 89d).
- **B. Eletricista, quadro elétrico:** 191.
- **C. Psicólogo/psicopedagogo, módulos:** 196 (crises no TEA), 204 (terapia de casal), 211 (avaliação psicopedagógica).
- **D. Dentista, mapas clínicos:** 206 (implantodontia).
- **F. Apostila editável para instrutor de beleza:** 170, 205 (cílios), 186 (barbearia).
- **H. Estimulação cognitiva de idosos:** 194.
- **I. Simulados de avaliação externa para professor:** 197.
- **Consumo e outros:**
  - J. atividades infantis/caligrafia: 166, 178, 182, 185, 188.
  - K. mapas visuais/estudo: 168, 172, 173, 208.
  - L. receitas para vender: 162, 192.
  - M. receitas saúde/dieta: 164, 175, 177, 179, 202.
  - N. festa/papelaria/design: 165, 176, 189, 193, 198, 203, 209, 212.
  - O. artesanato/maker: 167, 169, 180, 200.
  - P. finanças/planilhas: 174, 199, 201.
  - Q. fitness: 181, 195.
  - R. religioso: 183, 184.
  - S. parentalidade: 187, 207.
  - G. cursos: 159, 171, 190.
- **Z. Fora:** 161 e 163, acervos de conteúdo de terceiros (direito autoral).

## 2. Resultado por conceito e país

### 2.0 Termos traduzidos (conceitos profissionais)

| Idioma / país | A. Vidraceiro | B. Eletricista (quadro) | F. Apostila p/ instrutora de cílios | H. Estimulação cognitiva | C. Terapia de casal |
|---|---|---|---|---|---|
| ES (Espanha) | cristalero; carpintería de aluminio | cuadro eléctrico; electricista | manual de pestañas editable | estimulación cognitiva para mayores | terapia de pareja |
| MX | cancelero; cancelería de aluminio | tablero eléctrico; electricista | manual de pestañas editable | estimulación cognitiva adultos mayores | terapia de pareja |
| CO | vidriero; ventanería en aluminio | tablero eléctrico | manual de pestañas | estimulación cognitiva adulto mayor | terapia de pareja |
| AR | vidriero; aberturas de aluminio | tablero eléctrico (seccional) | manual de pestañas | estimulación cognitiva adultos mayores | terapia de pareja |
| CL | vidriero; ventanas de aluminio/termopanel | tablero eléctrico | manual de pestañas | estimulación cognitiva adulto mayor | terapia de pareja |
| PE | vidriero; carpintería de aluminio y vidrio | tablero eléctrico | manual de pestañas | estimulación cognitiva adulto mayor | terapia de pareja |
| PT-PT | vidraceiro; caixilharia de alumínio | quadro elétrico; eletricista | manual de formação de extensão de pestanas | estimulação cognitiva para idosos | terapia de casal |
| IT | vetraio; serramentista | quadro elettrico; elettricista | dispensa/manuale corso extension ciglia | stimolazione cognitiva anziani | terapia di coppia |
| FR | miroitier; menuisier alu | tableau électrique; électricien | support de formation extension de cils | stimulation cognitive / ateliers mémoire seniors | thérapie de couple |
| DE | Glaser; Metallbauer | Unterverteilung/Verteiler; Elektriker | Schulungsunterlagen Wimpernverlängerung | Gedächtnistraining Senioren | Paartherapie |
| PL | szklarz; stolarka aluminiowa | rozdzielnica; elektryk | skrypt szkoleniowy stylizacja rzęs | stymulacja poznawcza seniorów | terapia par |
| RO | geamgiu; tâmplărie din aluminiu | tablou electric; electrician | suport de curs extensii gene | stimulare cognitivă vârstnici | terapie de cuplu |
| CZ | sklenář | rozvaděč; elektrikář | skripta prodlužování řas | trénink paměti pro seniory | párová terapie |
| SK | sklenár | rozvádzač; elektrikár | skriptá predlžovanie mihalníc | tréning pamäti pre seniorov | párová terapia |
| HU | üveges | elosztószekrény; villanyszerelő | műszempilla oktatási jegyzet | memóriatréning időseknek | párterápia |
| GR | τζαμάς | ηλεκτρικός πίνακας; ηλεκτρολόγος | εγχειρίδιο σεμιναρίου βλεφαρίδων | νοητική ενδυνάμωση ηλικιωμένων | θεραπεία ζεύγους |
| NL | glaszetter | groepenkast; elektricien | lesmateriaal wimperextensions | geheugentraining ouderen | relatietherapie |
| EN UK | glazier | consumer unit; electrician | lash training manual | activities for seniors / dementia activities | couples therapy |
| EN US/CA | glass installer / glazier | electrical panel; electrician | lash training manual | dementia activities | couples therapy |
| EN AU | glazier | switchboard; electrician | lash training manual | activities for seniors | couples therapy |
| TR | camcı; alüminyum doğrama | elektrik panosu; elektrikçi | ipek kirpik eğitim kitapçığı | yaşlılar için hafıza egzersizleri | çift terapisi |

Os termos de RO, CZ, SK, HU, GR, NL e TR foram traduzidos, mas **não foram medidos** na Biblioteca nesta rodada (orçamento e tempo); a exceção é CZ/PL no conceito B (ver 2.B).

### 2.1 Matriz resumida

| Conceito | ES-LATAM (neutro/USD) | MX | PE | AR / CO / CL | ES (Espanha) | PT | IT | FR | DE | CZ / PL | EN |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A. Vidraceiro | TESTE (1 clone BR, 1d) | BRECHA | — | — | — | BRECHA | BRECHA | não medido | não medido | não medido | não medido |
| B. Eletricista quadro | TESTE (Tablero Studio 2d; cursos genéricos) | — | — | MarKa2 CLP 10d (genérico) | TESTE | TESTE (≤1,4d) | **TESTE, onda BR 1–8d** | BRECHA | não medido | **TESTE (Studio Quadri ≤3d)** | não medido |
| C. Psicólogo módulos | TESTE (genéricos ≤7d) | Kits Digitales 139d (genérico, VERIFICAR) | PsicoTools 28d | MenteCloud CLP 7d | — | — | BRECHA (casal) | não medido | não medido | — | não medido |
| D. Implante mapas | BRECHA | BRECHA | — | — | BRECHA | — | BRECHA | — | — | — | — |
| F. Apostila instrutora | **PROVADO neutro (Zenah 119d)** | AvaStudio2 9d | — | — | — | BRECHA | BRECHA | BRECHA (1 formação) | não medido | — | TESTE (Lashful 0,3d; Bucha 49d, 1 anúncio) |
| H. Estimulação cognitiva | TESTE (Recursos Digitales <1d) | — | **PROVADO (Cognimente 64d, PEN)** | — | TESTE (Geriactiva ≥8,8d, ~140 anúncios) | TESTE (Ginástica Mental 14d) | TESTE (onda BR ~2d) | **BRECHA** | TESTE (The Resource Lab 3d) | — | TESTE (Un Mundo Genial <1d) |
| I. Simulados | — | — | — | CO: BRECHA p/ professor | — | — | BRECHA (só editoras) | — | — | — | não medido |
| J. Atividades infantis | PROVADO (saturado) | PROVADO (Stardex 269d termo) | PROVADO (67d termo) | ARS 22d | — | — | PROVADO (L'angolo del Docente 209d termo) + onda BR | — | — | — | — |

"—" = não pesquisado para aquele conceito/país.

### 2.A Vidraceiro (160 Maleta Digital do Vidraceiro 117d/13 ativos/R$17; 210 Manual Técnico Esquadria PRO 89d/10/R$67)
- **ES/LATAM** (busca "vidriero" em MX, CO, AR, CL, PE, ES e US): 87 anúncios, quase todos vidrarias.
  - O único infoproduto é **"Kit del vidriero"** (page 1395867183609022): USD, 4 anúncios, iniciado em 29/10 (0,6 dia). Títulos: "Kit del Vidriero: 73 modelos" e "Kit del Vidriero · todo en el celular". É um clone brasileiro que acabou de entrar.
  - "Desafío Pruébalo" (BRL, 206 anúncios, cerca de 2 dias) vende "certificaciones" multinicho, uma delas de vidriero. Não é kit.
  - **Status: TESTE recém-aberto. Ninguém antigo.**
- **MX:** "cancelería PDF" deu 4 resultados e "vidriería proyectos listos" deu 5. Nenhum é infoproduto, só fábricas. **BRECHA** num mercado que, a julgar pela quantidade de anúncios de cancelería (1.046 ativos só em MX), é enorme. O tamanho do mercado está em VERIFICAR.
- **PT:** "vidraceiro" deu 1 anúncio (loja). **BRECHA.**
- **IT:** "vetraio" deu 17 anúncios: vidrarias, Murano e o "Kit Panorama" (perfis físicos com manual técnico, Cristal Beauty). **BRECHA** para kit digital.
- **FR, DE, PL, RO, EN, TR:** não medidos.

### 2.B Eletricista: quadro elétrico (191 Quadros Elétricos Realistas 188d/11/R$67)
- **BR:** página Elétrica de Alta Performance (101365762967853). O anúncio mais antigo visto na busca por termo tem 108 dias (termo). Títulos: "Mostre ao cliente como o quadro ficará antes da montagem", "Crie quadros profissionais em poucos minutos".
- **IT: onda de clones brasileiros, todos com menos de 10 dias.**
  - **Studio Quadri** (721617357705716): USD, 213 anúncios. Os 50 mais novos têm no máximo 2,7 dias. Títulos: "Progetta i tuoi quadri in 15 minuti", "+200 componenti", "Unifilare automatico", "PDF su WhatsApp", "Paghi una volta". A mesma página já roda em **tcheco** ("Navrhuj rozvaděče za pár minut") e em **polonês** ("Projektuj rozdzielnice w kilka minut").
  - **Marco Ferri** (1391669727368636): USD, 3 anúncios, 0,5 dia, "Quadri elettrici professionali in meno di 15 minuti". Outra página **Marco Ferri** (1464775986709724): BRL, 4 anúncios, 3,5 dias, "+100 Mappe Visive di Impianti Elettrici".
  - **Claude Ingegneria Elettrica PRO** (1388019914391217): BRL, 4 anúncios, cerca de 1 dia, "500+ Progetti Elettrici + 4 Bonus | 27 €".
  - **Arquimax-Academy** (110059091610423): USD, cerca de 10 anúncios, 7,8 dias. Bônus anunciados: "Calcolatore Preventivo (Excel) · Modelli di preventivo e offerta · Checklist di collaudo e DiCo · Quanto far pagare".
  - Studio Facile e Atlante Visivo del Cantiere: USD, menos de 1 dia.
  - **Status IT: TESTE, e quente.** Pelo menos 6 operadores brasileiros entraram em uma semana. Ninguém está PROVADO.
- **ES/LATAM:**
  - **Tablero Studio** (603360102852473): USD, cerca de 1,9 dia, "Diseña tus cuadros eléctricos en minutos". É o mesmo molde do Studio Quadri.
  - Infoprodutos genéricos de eletricista:
    - Juan Carlos Pérez – Electricista: cursos em USD e BRL, "+18.300 alumnos", dias VERIFICAR.
    - Academia Online PRO: USD, 6 anúncios, 4,6 dias, "Pack Eléctrico Completo".
    - Vifalio App Tec: "Kit del electricista gratis", cerca de 3 dias.
    - Kit de Guías Sara: COP, cerca de 2,4 dias.
    - MarKa2 Academy: CLP, cerca de 9,7 dias.
  - **Status: TESTE.** Ninguém tem 30+ dias no produto "quadro".
- **PT:** GG Express (EUR, "Eletricista Profissional", cerca de 0,1 dia) e Miguel Ferreira (BRL, "Manual Prático do Eletricista Residencial", cerca de 1,4 dia). **TESTE.**
- **FR:** "tableaux électriques" só trouxe lojas e empregos. **BRECHA**, com a barreira do francês.
- **DE, RO, SK, HU, GR, NL, EN, TR:** não medidos.

### 2.C Psicólogo: módulos (196 Kit Acalmar 57d/11/R$27; 204 Guia Prático para Atender Casais 69d/10/R$27; 211 Apostila de Avaliação Psicopedagógica 48d/10/R$10)
- **ES/LATAM:** "kit terapia de pareja" deu 91 anúncios e "crisis autismo kit" deu 4. Só aparecem vendedores **genéricos** de recursos de psicologia:
  - **Kits Digitales** (101231043033890): MXN, 3 anúncios, **139 dias**. Aparece nas duas buscas, mas o conteúdo não está visível (VERIFICAR).
  - **PsicoTools** (195198090343781): PEN, 1 anúncio, 28 dias.
  - Material Digital: MXN, multinicho, 23 dias.
  - MenteCloud.com: CLP, 16 anúncios, 6,6 dias.
  - Bienestar Emocional: USD, "QUIERO EL KIT", cerca de 2,6 dias.
  - Psicología & Recursos: COP, "Kit manejo del duelo", cerca de 2 dias.
  - El Taller del Terapeuta (PEN) e Media Center México (MXN, "+1,000 tests en Excel + 2,500 Libros en pdf + Guías Clínicas por $99 mxn").
  - Nenhum título fala de kit de casal ou de crises no TEA.
- **Psicopedagogía:** "evaluación psicopedagógica" deu 136 anúncios: clínicas (AR, PE, MX) e o máster da TECH. O único vendedor de material é Valeria Mendoza (BRL, 16 anúncios, 4,5 dias). **TESTE/BRECHA.**
- **IT:** "terapia di coppia psicologi" deu 5 anúncios, só formação (Spazio IRIS) e consultórios. **BRECHA** para um módulo de casal.
- **Concorrente BR do formato:** Psiflow.clin ("Documentos clínicos prontos para adultos", BRL, cerca de 0,6 dia).

### 2.D Dentista: mapas clínicos de implantodontia (206 Biblioteca Clínica Visual 73d/10/R$19)
- **BR:** Bianca Carvalho (1250052431533441), "Implantodontia em Mapas Visuais", 73,8 dias, 10 anúncios.
- **ES/LATAM:** "implantología mapas" deu 0 e "implantología PDF" deu 1 (livraria MXN).
- **IT:** "implantologia mappe" deu 0.
- **BRECHA total.** Serve como bônus ou bump dos kits de dentista (IT e CO).

### 2.F Apostila editável para instrutoras (170 Apostila de Cílios 118d/12/R$47; 205 4 Apostilas Lash 80d/10/R$37; 186 Barber Training Kit 154d/11/R$57)
- **Espanhol neutro: PROVADO pelo próprio vendedor BR.**
  - **Zenah Sanchez Beauty** (104514235651253), a mesma página da oferta 170, roda a versão em espanhol: "¡Producto 100% en español!" e "Tu curso merece un material más profesional". Moeda USD. O anúncio em espanhol mais antigo tem **118,7 dias**.
  - Dollis Templates (621393921048013): USD, 3 anúncios, 21,3 dias, "Empieza a enseñar extensiones de pestañas de la manera correcta".
  - AvaStudio2: MXN, cerca de 9 dias.
- **EN (US, GB, AU, CA):** "lash training manual" deu 71 anúncios, quase todos estúdios e cursos presenciais.
  - Infoproduto: **Lashful** (1235489159657036), EUR, 2 anúncios, cerca de 0,3 dia, "Launch Your Own Lash Course" e "Your Lash Course, Ready to Launch".
  - International Lash Masters (AUD) vende um programa de educadora, não um kit.
  - **Status EN: TESTE/BRECHA.**
- **Barbearia:**
  - BR: Bucha Barbearia (347739515954218), "APOSTILA BARBER", 155 dias. A Bucha **já testa inglês**: 1 anúncio em US/GB/AU/CA há **49,4 dias** ("barber training manual").
  - ES: "manual de barbería" deu 86 anúncios, todos de escolas presenciais (MX, PE). **BRECHA** para kit editável de barbearia em espanhol.
- **IT:** "manuale extension ciglia corso" deu 0. **PT:** "manual pestanas formadoras" deu 0. **FR:** "support de cours extension de cils" deu 1 (L'académie by Lau, formação a €50, 132 dias). **BRECHA** em IT, PT e FR.

### 2.H Estimulação cognitiva de idosos (194 Mente Ativa 250, 65d/11, venda via WhatsApp)
- **PE: PROVADO.** **Cognimente** (618983884633295): PEN, **37 anúncios, 64,2 dias**. Títulos: "Libro de entrenamiento mental" e "Para una mente sana, útil y ágil".
- **ES (Espanha) e LATAM:**
  - **Geriactiva** (1259324537268785): USD, cerca de 140 anúncios, "+3000 Profesionales lo recomiendan". Os 50 mais novos têm até 8,8 dias, então o mais antigo pode ser bem mais velho (VERIFICAR).
  - Recursos Digitales: USD, "+500 actividades para mantener la mente activa", cerca de 0,8 dia.
  - Academia Digital: PEN, "Ejercita tu memoria por solo s/. 10", cerca de 0,5 dia.
  - Professora Maria: BRL, "Fichas Visuales de Estimulación Cognitiva para Adultos Mayores", cerca de 1,8 dia.
  - **TESTE**, com escala forte na Geriactiva.
- **IT: TESTE, onda BR.**
  - Seduta Pronta (1447072035149109): USD, 3 anúncios, 1,7 dia, "La seduta di domani, già pronta".
  - The Mind Market (884241854764422): USD, "96 sedute pronte da stampare" e "Laboratorio Pronto", 1,7 dia. Também roda em PT-PT ("Ritmolândia | 50 aulas de música prontas").
  - The Resource Lab (1123744187496255): USD, "6 volumi + 5 volumi speciali", 1,8 dia.
- **DE: TESTE.** A mesma The Resource Lab roda em alemão: "52 Wochenthemen für das ganze Jahr", "6 Bände + 5 Sonderbände", "100 Kurzaktivierungen in 10 Minuten", cerca de 2,9 dias.
- **PT: TESTE.**
  - Ginástica Mental (1344439098756901): USD, "Um ano de sessões, pronto a imprimir", em PT-PT, 13,8 dias (termo).
  - Mais Educação: BRL, "1001 Atividades para Estimular a Mente", cerca de 0,7 dia.
- **EN: TESTE.** Un Mundo Genial: USD, "Your whole week in 8 volumes" e "Suddenly alone with the group?", cerca de 0,8 dia.
- **FR: BRECHA.** "stimulation cognitive seniors activités" deu 0.
- **Leitura.** Os títulos em IT, DE e EN ("seduta", "Wochenthemen", "alone with the group") miram **profissionais**: animadores de RSA e Tagespflege, terapeutas e cuidadores. Não miram só os filhos. Isso encaixa no formato "kit por profissão".

### 2.I Simulados de avaliação externa (197 41 Simulados SARESP 63d/11/R$59,70)
- **IT:** "simulazioni INVALSI" deu 2 anúncios, só editoras (La Scuola, LS Scuola). **BRECHA** para kit digital low ticket. A demanda está em VERIFICAR, porque o INVALSI publica provas antigas de graça.
- **CO:** "simulacros pruebas saber" deu 23 anúncios, todos de pré-ICFES para alunos do 11º ano. Nada para o professor de 3º/5º ano. **BRECHA** (VERIFICAR demanda).
- **Equivalentes não medidos:** SIMCE (CL), avaliações nacionais do MINEDU (PE), Aprender (AR), pruebas de diagnóstico (ES), provas ModA (PT), évaluations nationales (FR) e KS2 SATs (UK).

### 2.J–S Consumo (pesquisa rápida, uma busca por conceito)
- **J. Atividades infantis, caligrafia e alfabetização (166, 178, 182, 185, 188):**
  - ES/LATAM saturado:
    - Stardex Educación: MXN, anúncio com **269 dias** (termo).
    - Material Educativo de Educación Infantil: PEN, 67 dias (termo).
    - Rincón Infantil: ARS, 22,5 dias.
    - Momentos que unen: MXN, "330 fichas por $69", 9,4 dias.
    - Também Jengibre Imprimibles (ARS), Eduki (MXN), Volver a mí (MXN), Pequenos Peregrinos (USD, BR, "Kit de Caligrafía 317 fichas") e La Casita del Saber (BRL).
    - "sílabas actividades imprimir" deu 355 anúncios.
  - Caligrafia para adultos: Regina López (BRL, cerca de 0,1 dia) e Impulso creativo (USD, 1,8 dia).
  - IT:
    - **L'angolo del Docente**: EUR, **208,7 dias** (termo), nativo.
    - Edudoro.eu: PLN, plataforma, 58 dias (termo).
    - Onda BR: Attivita Premium (USD, "2.500 schede così, a 7,90 €", "Dalle sillabe semplici alle complesse", 2,8 dias), Mondo Infanzia Didattica (USD, "Oltre 1.000 Attività per la Scuola dell'Infanzia (PDF da Stampare)", 8,8 dias), Prof di Scienze, Orbis Atlas e Navigo (20 dias).
  - **PROVADO e concorrido.**
- **K. Mapas visuais e estudo (168, 172, 173, 208):** não medidos aqui. Ver o relatório irmão `resultados/mapas-mentais-por-pais-v2-2026-10-30.md`.
- **L/M. Receitas:**
  - Diabéticos em ES/LATAM: 200 anúncios. Vendedores: Salud para todos (MXN, "+971 Personas nos recomiendan"), Cocina vital sin azúcar (USD, "50 Recetas para Diabéticos: App Web"), Nutri de Confianza (ARS, "+500 argentinos lo adquirió"), Mesa y Sabor (USD, pães). **Concorrido**, dias em VERIFICAR.
  - Introdução alimentar em ES: 4 anúncios, Cucharita lista (ARS, cerca de 0,2 dia) e Olivia Sousa (BRL, "Primer Bocado", 2,8 dias). **TESTE.**
  - Laticínios, macarrão no pote, adventista, 21 dias e lanchinhos: não medidos (consumo, fora do modelo).
- **N. Festa, papelaria e design:**
  - Kit de festa: **cienacres.imprimibles** (USD, **506,8 dias**), PROVADO em espanhol neutro.
  - Convites: Archivos Digitales Express (MXN, 65,1 dias), Fabrica de Fiestas (BRL, 85,1 dias) e Mara Cursos y Packs (USD, 43,8 dias). PROVADO.
  - Sublimação: 81 anúncios (Sublinova, PixelPack LATAM, PP Studio), saturado.
  - Retrovisor, planner e artes para músicos: não medidos.
- **O. Artesanato:**
  - STL: 640 anúncios (Marcos Santiny, USD, "Gana Dinero con la Impresión 3D en el Nicho Católico"), saturado.
  - **Moldes de couro:** Marroquineria_emprendedora (112777348457826), ARS, 7 anúncios, 17,5 dias, "+200 moldes listos para imprimir". É TESTE de vendedor nativo da AR, onde o "guasquero" existe como ofício. El Plano del Cuero (USD, 24,6 dias) vende curso.
  - Crochê: Crochet al Hogar (USD, "200 patrones de crochet para tu casa", menos de 1 dia), parte da onda BR.
- **P. Finanças e planilhas (174, 199, 201):** não medidos.
- **Q. Fitness:**
  - Corrida: **Zero Pace Club**, o mesmo anunciante BR da oferta 195, já roda em espanhol (BRL, "2384 reseñas", 5,6 dias). Também Runners academy (USD, AR, coaching, 98,7 dias) e Entrenamiento Rodado (EUR, Espanha, 25,1 dias).
  - Jiu-jitsu em ES: 2 anúncios. **BRECHA**, mas é nicho pequeno.
- **R. Religioso:** "biblioteca teológica" em ES tem **Clara Martin** (BRL, "Accede a la Central Teológica", **111,8 dias**). É um BR vendendo em espanhol, PROVADO neutro. Também Prof. Paulo Henrique (BRL, app teológico, cerca de 1 dia).
- **S. Parentalidade:**
  - Rotinas visuais em ES: 18 anúncios, entre eles Universo educativo digital (MXN, cerca de 3 dias) e Educación Online (USD, 4 a 8 dias).
  - Estimulação de bebê em ES: 20 anúncios, entre eles Mi Dulce Bebé (PEN, 23 dias), FamyHub (COP, 17 dias) e mundo infantil (USD, 12 dias).
  - **TESTE.**
- **G. Cursos:** chaveiro em ES deu 91 anúncios (Info Master, USD, multinicho, menos de 1 dia). Cuticulagem e mecatrônica não foram medidas.
- **Z. Fora:** 161 (desenhos antigos) e 163 (+5.000 doramas) são acervos de conteúdo de terceiros, com risco de direito autoral. Não pesquisados.

## 3. Páginas de vendas e gancho legal (sinais fortes)

**Não foi possível abrir nenhuma página de vendas nem fonte oficial nesta rodada** (bloqueio de rede e cota de busca; ver avisos). Abaixo está o que já se sabe pelo JSON e o que falta conferir.

| Brecha | O que o JSON já dá (BR) | Abrir e conferir | Gancho legal (hipótese, VERIFICAR com fonte oficial) |
|---|---|---|---|
| B. Eletricista | R$67; eletricadealtaperformance.com.br/quadros-eletricos-realistas; promessa "mostrar o quadro ao cliente antes da execução" | Formato (app ou PDF?), bumps, garantia; páginas dos clones IT (Studio Quadri "Paghi una volta", "PDF su WhatsApp"; Claude Ingegneria "27 €") | IT: DM 37/2008, Dichiarazione di Conformità (a Arquimax já usa "Checklist di collaudo e DiCo" como bônus). ES: REBT (RD 842/2002) e Certificado de Instalación Eléctrica. PT: termo de responsabilidade/ficha eletrotécnica. Número de instaladores por país: VERIFICAR |
| H. Estimulação cognitiva | Venda por WhatsApp, 250 atividades em 5 cadernos | Página da Cognimente (PE): preço em PEN, formato; Geriactiva (ES/LATAM); Seduta Pronta e The Resource Lab (IT/DE) | Sem norma com prazo conhecida. Gancho de mercado: população idosa e demência (fontes INEI PE, ISTAT/ISS IT, INSEE FR): VERIFICAR |
| F. Apostila instrutora | R$47 (170), R$37 (205), R$57 (186); 100% editável no Canva; certificados editáveis | Preço USD da versão ES da Zenah; Lashful (EUR) em inglês | Sem norma com prazo. EN/UK: formação de lash não regulada por lei específica (VERIFICAR) |
| A. Vidraceiro | R$17 (160) e R$67 (210); "projetos prontos, catálogo", "fórmulas de folga, perfis e acessórios da Linha Suprema" | Página "Kit del vidriero" (USD): preço, "73 modelos", app | ES: CTE DB-SUA (vidros de segurança). IT: UNI 7697 (vetri di sicurezza). MX: NOM para vidro de segurança. Todas como hipótese, VERIFICAR |
| C. Psicólogo, módulos | R$27 (196, 204), R$10 (211) | Conteúdo dos Kits Digitales (MXN, 139d) e PsicoTools (PEN, 28d) | Herdar dos kits já pesquisados, conforme as notas do usuário: CO Res. 839/2017 (guarda de 15 anos) e IT L.132/2025 (aviso de uso de IA). MX: VERIFICAR |

## 4. Ranking das brechas (0–10) e reaproveitamento

| # | Brecha | País/idioma | Status | Nota | Por quê | Reaproveitamento |
|---|---|---|---|---|---|---|
| 1 | **Kit do eletricista: quadro + documentos de conformidade** | IT (depois ES, PT) | TESTE + gancho legal a confirmar | **7,0** | BR com 188 dias. Pelo menos 6 páginas novas em USD/BRL, com perfil de operador BR, entraram em IT, ES, CZ e PL em 1 a 8 dias, ou seja, leram o mesmo sinal. Ninguém está PROVADO. O diferencial possível é o documento legal local (DiCo/CIE), que os clones de "desenho de quadro" não têm (só a Arquimax cita DiCo como bônus). Risco: saturação rápida. | App de inspeção (checklist de collaudo/verifica) + estrutura da Valigetta (documentos + app); Consultora (simulador de vistoria) adaptável para "verifica impianto" |
| 2 | **Estimulação cognitiva: sessões prontas para profissionais e cuidadores** | PE/LATAM (provado); FR (brecha) | PE PROVADO; ES/IT/DE/PT/EN TESTE; FR BRECHA | **6,5** (PE/LATAM) / 6,0 (FR) | Único vendedor nativo PROVADO da faixa (Cognimente: PEN, 64 dias, 37 anúncios). Geriactiva escala em espanhol. A França está zerada. Risco: o operador BR multipaís (The Resource Lab em IT e DE) avança rápido. | Log diário da Valigetta, virando registro de sessão por residente; formato "seduta pronta"; o mesmo pacote serve para animador de RSA (IT) e Tagespflege (DE) |
| 3 | **Apostila/kit editável para instrutoras de cílios e barbeiros** | EN (US/UK/AU), IT | ES neutro PROVADO; EN/IT BRECHA | **6,0** | A Zenah prova em espanhol há 119 dias que o conceito atravessa idioma. EN e IT estão quase vazios. A Bucha já testa EN (49 dias, 1 anúncio), então é preciso entrar antes de ela escalar. | Estrutura da Valigetta (kit editável + certificados); app de quiz/avaliação da aluna |
| 4 | **Kit do vidraceiro (projetos + fórmulas de folga + orçamento)** | MX (cancelería), ES-LATAM | BRECHA / TESTE de 1 dia | **6,0** | Dois vendedores BR provados (117 e 89 dias). Em espanhol há só um clone BR de 1 dia. MX tem muita cancelería anunciando (1.046 anúncios) e nenhum infoproduto. | App de inspeção (medição e checklist de instalação) + calculadora de orçamento (motor do Termometro) |
| 5 | **Módulos para psicólogo: terapia de casal, crises no TEA, avaliação psicopedagógica** | MX/CO (Maletín), IT (Psicologo) | TESTE/BRECHA | **5,5** | Nenhum vendedor com esses módulos. Só há genéricos (Kits Digitales MXN 139d, a checar). Funciona melhor como bump do que como oferta nova. | Reuso total: Maletín del Psicólogo MX e futura Valigetta dello Psicologo |
| 6 | **Mapas clínicos de implantodontia** | IT, CO/ES (dentista) | BRECHA | **5,0** | Ninguém vende fora do BR. No BR o sinal é médio (74 dias, 10 anúncios). | Bônus/bump da Valigetta del Dentista e do Maletín dentista CO |
| 7 | **Simulados de avaliação externa para professor** | IT (INVALSI) | BRECHA + PRAZO sazonal (provas na primavera; calendário 2027 VERIFICAR) | **5,0** | Só editoras anunciam. A demanda é incerta porque há provas oficiais grátis. | Motor de quiz/simulador da Consultora |
| 8 | Moldes de couro/marroquinaria | AR | TESTE nativo (17,5d) | 4,0 | Um vendedor ARS recente; BR com 445 dias (169) | — |
| 9 | Introdução alimentar em espanhol | ES-LATAM | TESTE | 4,0 | 2 vendedores novos (ARS e BR) | — |
| 10 | Treinos de jiu-jitsu em espanhol | ES-LATAM | BRECHA | 3,5 | Ninguém vende, mas o nicho é pequeno e fora do modelo | — |
| — | Atividades infantis/caligrafia, festas/convites/sublimação, receitas para diabéticos, STL, crochê, biblioteca teológica, corrida | ES-LATAM, IT | PROVADO/saturado | ≤3 | Vendedores nativos antigos (Stardex 269d, L'angolo del Docente 209d, cienacres 507d) ou BR já em ES há mais de 100 dias (Clara Martin 112d) | — |
| — | 161 desenhos antigos, 163 doramas | — | Fora | 0 | Direito autoral | — |

**Ordem sugerida para conferir:**
1. Eletricista IT: confirmar DM 37/2008 e a página do Studio Quadri. A janela pode fechar em semanas.
2. Cognimente PE e Geriactiva: abrir as páginas, ver preço e formato, e medir o anúncio mais antigo da Geriactiva.
3. "Kit del vidriero": abrir a página e acompanhar se passa de 30 dias (re-checar em 29/11).
4. Lash em EN: medir Lashful e Bucha de novo em 15 dias.

## 5. VERIFICAR

1. **Sem fonte oficial nesta rodada.** Nenhuma norma nem tamanho de profissão foi confirmado (WebSearch esgotado, WebFetch bloqueado). Normas que precisam de fonte:
   - DM 37/2008 (IT);
   - REBT RD 842/2002 e Certificado de Instalación Eléctrica (ES);
   - regime das instalações elétricas de serviço particular (PT);
   - CTE DB-SUA (ES) e UNI 7697 (IT) para vidro;
   - calendário INVALSI 2027.
2. **Páginas de vendas não abertas** (191, 160, 210, 170, 186, 196, 204, 206, 211): preço atual, plataforma, bumps e garantia.
3. **Kits Digitales** (MXN, page 101231043033890, 139 dias): o que vende? Aparece nas buscas "terapia de pareja" e "crisis autismo kit".
4. **Geriactiva** (page 1259324537268785, cerca de 140 anúncios): anúncio mais antigo (só vi os 50 mais novos, ≥8,8d), país e preço.
5. **Studio Quadri** (page 721617357705716, 213 anúncios): anúncio mais antigo (amostra ≤2,7d), preço em € e países (IT, CZ, PL e outros?). Também Tablero Studio (ES): ver se é o mesmo operador.
6. **Juan Carlos Pérez – Electricista** (pages 1305285269324908 USD e 1320279351165472 BRL): dias reais e país.
7. **Cognimente** (PE): preço em PEN, formato (livro físico ou PDF?) e público (família ou profissional).
8. **Zenah** em espanhol: preço em USD e se segmenta algum país específico.
9. **Bucha Barbearia** em inglês: 1 anúncio há 49 dias. Conferir se escalou (re-checar em 15/11).
10. **Kit del vidriero** (page 1395867183609022): re-checar em 29/11 se passou de 30 dias e se abriu mais anúncios.
11. **Stardex Educación** (MXN, 269d), **Material Educativo de Educación Infantil** (PEN, 67d) e **L'angolo del Docente** (EUR, 209d): medidos por termo, não por page_id. Confirmar número de anúncios.
12. **Países não medidos** em todos os conceitos: RO, CZ, SK, HU, GR, NL, TR e EN, exceto lash/barber e cognitivo.
13. **Mercado MX de cancelería e vidrio:** número de oficinas (INEGI/DENUE) para dimensionar a brecha do vidraceiro.
14. **INVALSI:** existe demanda paga (professores compram simulados) ou o material grátis basta?
15. **Conteúdo dos anúncios** (texto e link): não visível pelo conector. Todas as classificações vêm de nome da página, título e moeda.

## 6. Bloqueios desta rodada

- SearchAPI: sem chave neste container e sem crédito até 08/11.
- facebook.com, os sites de venda (eletricadealtaperformance.com.br, maletadovidraceiro.lovable.app) e gazzettaufficiale.it estão fora da lista de domínios permitidos da rede. Para abrir páginas e fontes oficiais, esses domínios precisam ser liberados nas configurações de rede da sessão.
- WebSearch: o limite de 200 buscas por turno, compartilhado com os agentes irmãos, já tinha sido usado.
- O conector Meta não devolve o texto do anúncio e corta em 50 anúncios por consulta. Em páginas grandes, os dias reais ficam como piso.
