# Catálogo EscalaLow, parte 3 (índices 106 a 158) — brechas por país

Data de referência: 30/10/2026. Fonte: `dados/escalalow-ofertas-validadas.json` (213 ofertas BR validadas), índices 106–158 (53 ofertas).

## Avisos de método (ler primeiro)
- A versão anterior (v1 de 29/10) e os arquivos do Desktop NÃO estavam acessíveis neste ambiente; este relatório parte do zero, usando o próprio JSON e as notas `fila-ofertas.md`, `pesquisa-europa.md` e `meta-varredura-low-ticket.md`.
- SearchAPI NÃO disponível (sem chave aqui e sem crédito até 08/11). Toda a medição de anúncios foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` da busca por página.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.
- WebFetch bloqueado pela rede do container para páginas de vendas e fontes oficiais (lovable.app, inovaba.com.br, alaincarboni.com, boe.es; hotmart/kiwify com 403). WebSearch: a cota da sessão (compartilhada entre agentes) esgotou-se após a 1ª busca. Por isso nenhum tamanho de profissão nem norma foi confirmado com URL oficial; tudo isso está como VERIFICAR (seção 6).
- Única busca web concluída (videovigilância ES) não trouxe número de instaladores. Só deu o marco: instalação com fim de segurança privada exige empresa inscrita no registro do Ministerio del Interior, com liberalização parcial pela Diretiva de Serviços (fontes de 2007–2014, desatualizadas). Fontes: [xatakahome.com](https://www.xatakahome.com/espacioprosegur/puedo-poner-videovigilancia-en-mi-negocio-conoce-la-normativa-vigente), [legaltoday.com](https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/menos-control-de-la-videovigilancia-mas-observados-2010-01-05/).

## 0. Resumo (o que levar desta faixa)
- Das 53 ofertas (índices 106–158), 7 estão fora do modelo: livro autoral, Pencil Method (já internacional), curso de cílios, pack de PC, loja de toner, monetização de contador presa à Reforma Tributária BR e treinos fitness. As 53 foram agrupadas em 26 conceitos (C1–C26). Medi 24 deles no conector Meta (≈77 consultas, 30/10/2026).
- Só **3 conceitos desta faixa casam com o modelo "kit de documentos + app por profissão"** e têm brecha na Europa ou na LATAM:
  1. **Kit ABA**, nota 7,5. Inclui programas, folhas de registro e um app de coleta de dados.
  2. **Oficinas prontas de estimulação cognitiva para profissionais de lares de idosos**, nota 7,0.
  3. **Maleta do instalador de CFTV com pacote RGPD + app de vistoria**, nota 6,0.
- Depois vêm dois aproveitamentos:
  - o **Maletín del Psicólogo** levado para Argentina e Chile (6,0);
  - um **Kit del Consultor** em espanhol, feito sobre a Consultora (5,5).
- O padrão mais importante do dia é que **operadores brasileiros já estão abrindo IT e FR com estimulação cognitiva para profissionais**, todos com conta em USD:
  - Palestra Mentale: 11 anúncios, ~15 dias;
  - Seduta Pronta;
  - The Resource Lab (FR), ~10 dias.

  Na Espanha esse produto ainda não existe. A janela para chegar primeiro é a Espanha, e IT/FR devem ser re-checados quando esses anúncios fizerem 30 dias (13–18/11).
- **Bloqueios desta rodada:**
  - SearchAPI indisponível; usei o conector Meta.
  - WebFetch das páginas de vendas e de fontes oficiais foi bloqueado pela rede do container (lovable.app, inovaba, boe.es, hotmart, kiwify).
  - A cota de WebSearch da sessão se esgotou na 2ª busca.

  Consequência: **nenhum tamanho de profissão nem gancho legal foi confirmado com fonte oficial nesta rodada.** Tudo isso está marcado VERIFICAR na seção 6.
- Comparação com a v1 (29/10): a v1 não estava acessível neste ambiente, então não dá para listar diferenças.

## 1. Agrupamento das 53 ofertas em conceitos (com tradução dos termos)

| Conceito | Ofertas (índice) | Profissão/público | Encaixe no modelo kit + app |
|---|---|---|---|
| C13 Programas ABA + relatórios psico/neuropsicopedagogia | 130, 120 | terapeuta ABA/acompanhante terapêutico; psicopedagoga | ALTO |
| C9 Estimulação cognitiva | 124 | BR: família/cuidador; IT/FR: animador/educador de lar de idosos | ALTO (versão profissional) |
| C15 Maleta do instalador de segurança eletrônica | 153 | instalador de CFTV/alarme/cerca | ALTO |
| C12 Documentos clínicos do psicólogo | 117 | psicólogo | ALTO (já é o produto da casa) |
| C18 Sistema de consultoria pronto | 127 | consultor autônomo | MÉDIO |
| C5 Catálogo de pergolados/toldos | 113 | serralheiro/montador | MÉDIO |
| C17 Modelos de projetos ambientais | 134 | engenheiro/consultor ambiental | MÉDIO |
| C19 Guia do perito judicial | 155 | perito | BAIXO (marketing, sem norma) |
| C21 Planilha de gestão/precificação | 157 | pequeno empresário | MÉDIO (motor Termometro) |
| C14 Mapas mentais concursos / resumo psicologia | 154, 133 | concurseiro / estudante | BAIXO-MÉDIO |
| C11 Gerador de apostilas com IA | 118, 119 | professor | MÉDIO (exige software) |
| C22 Posts prontos por profissão | 135, 151, 144 | lash, estética, personal | BAIXO (saturado) |
| C10 Infantil: grafomotricidade, alfabetização, caligrafia, massinha, jogos | 115, 136, 142, 143, 158 | pais e professores de infantil | consumo |
| C1 Papelaria personalizada 2027 | 106, 107, 122 | artesã de papelaria | consumo sazonal |
| C2 Papelaria de casamento Canva | 111 | noivas | consumo |
| C3 Moldes de artesanato/costura | 112, 114, 128, 145 | artesã/costureira | consumo |
| C4 Projetos de marcenaria hobby | 138, 146, 125, 149 | marceneiro iniciante/pais | consumo saturado |
| C6 Plantas de casas | 129 | quem vai construir | consumo |
| C7 Receitas para vender | 110, 147 | renda extra | consumo |
| C8 Ervas medicinais / capilar | 148, 132 | consumidor | consumo |
| C16 Eletricista residencial | 108 | DIY/aprendiz | consumo/ofício |
| C23 Estampas e sublimação | 137, 139, 123 | estampador/sublimador | ofício |
| C24 Cifras para igreja | 121 | músico de igreja | consumo |
| C25 Religioso (Ifá, São Bento) | 126, 150 | religioso | consumo |
| C26 Fora do modelo | 109, 116, 131, 140, 141, 152, 156 | — | — |

### Glossário de termos por idioma (conceitos de topo)
| Conceito | ES (ES / MX-CO-AR-CL-PE) | PT-PT | IT | FR | DE | PL | RO | CZ / SK | HU | GR | NL | EN (UK/US/AU/CA) | TR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kit ABA | programas ABA listos; hojas de registro ABA (AR: planillas de registro) | programas ABA prontos; folhas de registo | programmi ABA; schede raccolta dati | programmes ABA; grilles de cotation | ABA-Programme; Datenerhebungsbögen | programy terapii behawioralnej; arkusze rejestracji | programe ABA; fișe de înregistrare | programy ABA; záznamové archy / hárky | ABA programok; adatrögzítő lapok | προγράμματα ABA; φύλλα καταγραφής | ABA-programma's; registratieformulieren | ABA programs; ABA data sheets | UDA (ABA) programları; veri kayıt formu |
| Estimulação cognitiva (profissional de lar) | talleres de estimulación cognitiva (residencias); LATAM: adultos mayores | estimulação cognitiva; atividades para lares (ERPI) | stimolazione cognitiva; laboratori RSA | ateliers mémoire; animation EHPAD | Gedächtnistraining; Beschäftigung Demenz (Betreuungskräfte) | trening pamięci seniorów; terapia zajęciowa DPS | stimulare cognitivă vârstnici | trénink paměti seniorů / tréning pamäti | memóriatréning időseknek | γνωστική ενδυνάμωση ηλικιωμένων | geheugentraining ouderen; activiteitenbegeleiding | dementia activities; cognitive stimulation | yaşlılar için bilişsel uyarım |
| Instalador CFTV | instalador de cámaras de seguridad / videovigilancia (AR: CCTV) | instalador de videovigilância | installatore videosorveglianza | installateur vidéosurveillance | Errichter Videoüberwachung | instalator monitoringu | instalator supraveghere video | montáž kamerových systémů / systémov | kamerarendszer telepítő | εγκαταστάτης CCTV | installateur camerabewaking | CCTV installer | güvenlik kamerası kurulumu |
| Grafomotricidade | grafomotricidad; cuadernillo de trazos | grafomotricidade | pregrafismo | graphisme maternelle; écriture cursive | Schwungübungen; Grafomotorik | grafomotoryka; karty pracy | exerciții de pregrafie | grafomotorika | grafomotoros feladatok | γραφοκινητικές ασκήσεις | voorbereidend schrijven | pre-writing / handwriting worksheets | çizgi çalışmaları |
| Documentos do psicólogo | historia clínica; consentimiento informado (psicología) | processo clínico; consentimento informado | cartella clinica; consenso informato | dossier patient psychologue | Dokumentation Psychotherapie | dokumentacja psychologa | dosar clinic psiholog | dokumentace psychologa | pszichológus dokumentáció | φάκελος ασθενούς ψυχολόγου | dossiervoering psycholoog | therapy notes templates | psikolog danışan dosyası |
| Kit do consultor | kit del consultor; plantillas para consultores | kit do consultor | kit consulente; modelli proposta | kit consultant; modèles de proposition | Berater-Vorlagen | szablony dla konsultanta | șabloane consultant | šablony pro konzultanty | tanácsadói sablonok | πρότυπα συμβούλου | adviseur templates | consulting templates | danışman şablonları |
| Catálogo serralheiro/pergolado | planos de herrería; pérgolas (ES: cerrajería metálica) | serralharia; pérgolas | progetti pergole; carpenteria metallica | plans de pergola; métallerie | Pergola Bauplan; Metallbau | projekty pergoli | proiecte pergole | pergoly projekty | pergola tervek | σχέδια πέργκολας | pergola bouwtekening | pergola plans | pergola projeleri |
| Planilha de precificação | planilla de costos y precios (MX/ES: plantilla Excel) | folha de cálculo de preços | foglio Excel calcolo prezzi | tableur prix de revient | Excel Preiskalkulation | arkusz kalkulacji cen | foaie de calcul prețuri | kalkulace cen Excel | árkalkulációs táblázat | υπολογιστικό φύλλο τιμολόγησης | prijscalculatie Excel | pricing spreadsheet | fiyatlandırma tablosu |
| Calendários 2027 | calendarios 2027 para imprimir | calendários 2027 para imprimir | calendario 2027 da stampare | calendrier 2027 à imprimer | Kalender 2027 zum Ausdrucken | kalendarz 2027 do druku | calendar 2027 de printat | kalendář / kalendár 2027 k tisku | 2027-es naptár nyomtatható | ημερολόγιο 2027 εκτύπωση | kalender 2027 printen | 2027 printable calendar | 2027 yazdırılabilir takvim |
| Mapas para concursos | esquemas / mapas mentales oposiciones | mapas mentais concursos | mappe concettuali concorsi | fiches de révision concours | Lernkarten Beamtenprüfung | mapy myśli egzamin | hărți mentale concurs | myšlenkové mapy | gondolattérkép | νοητικοί χάρτες ΑΣΕΠ | mindmaps examen | — | KPSS zihin haritaları |

## 2. Tabela completa (todas as ofertas 106–158)
Dias/ativos/preço BR = do JSON EscalaLow. "Resultado por país" = conector Meta em 30/10 (dias de cada vendedor no Anexo A).

| # | Oferta BR | Nicho | Dias BR | Ativos BR | Preço BR | Conceito | Profissão/público | Resultado por país (30/10) | Régua |
|---|---|---|---|---|---|---|---|---|---|
| 106 | Biblioteca Profissional de Moldes de Caixas 2026 | Artesanato, moldes e papelaria | 68 | 19 | R$ 27,90 | C1 Papelaria 2027 (calendários/caixas) | artesã de papelaria personalizada | ES/LATAM: 183 anúncios, packs USD novos (disputado); IT: ninguém; FR/DE/PL: não pesquisado | IT BRECHA sazonal |
| 107 | ✨ CALENDÁRIOS 2027 | Veterinária e pets | 50 | 18 | WhatsApp/— | C1 Papelaria 2027 (calendários) | artesã de papelaria / revenda | idem C1 | IT BRECHA sazonal |
| 108 | Apenas 10 reais | Engenharia e arquitetura | 76 | 18 | WhatsApp/— | C16 Eletricista residencial (DIY) | dono de casa / aprendiz | LATAM: Faradayos USD ~56 d, Mentes Ganadoras ARS ~79 d, Academia Online PRO USD ~5 d; Europa não pesquisado | PROVADO (ES neutro/AR) |
| 109 | Livro físico ou em e-book , no site do autor | Outros | 209 | 18 | R$ 37,00 | — Livro de autor | leitor | não replicável (obra autoral) | fora |
| 110 | Receba o Guia no WhatsApp | Receitas e confeitaria | 71 | 18 | WhatsApp/— | C7 Receitas para vender (caseirinhos) | renda extra doméstica | ES/LATAM: Máster Class Online COP ~79 d, Rincón Artesanal USD ~61 d | PROVADO (ES) |
| 111 | Kit Minha Papelaria de Casamento | Artesanato, moldes e papelaria | 114 | 18 | R$ 37,00 | C2 Papelaria de casamento Canva | noivas | ES/LATAM: Pack de Plantillas USD ~3 d, Mara Cursos USD ~44 d; Europa não pesquisado | PROVADO fraco (USD) |
| 112 | Pack Oficina Lucrativa | Artesanato, moldes e papelaria | 172 | 18 | R$ 9,90 | C3 Moldes para fabricar e vender | artesão/oficina | busca genérica não feita (produto vago); ver C3 | VERIFICAR produto |
| 113 | Projetoteca dos Pergolados, Toldos e Coberturas | Projetos e marcenaria | 105 | 18 | R$ 17,00 | C5 Catálogo de pergolados/toldos | serralheiro/montador | MX: Planos y Diseños de Herrería MXN ~13 d (7 anúncios); demais: ninguém | MX TESTE; resto BRECHA |
| 114 | ✂️ +100 Moldes de Vestidos Infantis que Encantam💖 | Artesanato, moldes e papelaria | 82 | 18 | WhatsApp/— | C3 Moldes de vestidos infantis | costureira | ES/LATAM: Domina tu arte USD, Cursos PDF CLP, todos novos | TESTE |
| 115 | Caligrafia Cursiva Com os Salmos | Educação e professores | 92 | 18 | R$ 49,99 | C10 Caligrafia com Salmos | pais cristãos/professores | ver C10 (grafomotricidade) | ver C10 |
| 116 | A Cor Certa: porque é que os seus lápis de cor ficam baço… | Fotografia e vídeo | 57 | 18 | WhatsApp/— | — The Pencil Method (lápis de cor) | hobby de desenho | vendedor estrangeiro (USD) já localizando para o BR; não pesquisado | fora (já é internacional) |
| 117 | Combo PSI Prático | Psicologia e terapias | 72 | 18 | R$ 37,90 | C12 Documentos clínicos do psicólogo | psicólogo | AR: Psicoagenda ARS ~22 d (sem kit); MX: Aprende y Emprende ‘Pack Psicología’ MXN ~58 d; CL/PE/EC/UY: ninguém no termo. MX/CO/IT/ES/PL/SK já na fila (notas) | AR/CL TESTE; pipeline |
| 118 | Apostila Visual | Educação e professores | 55 | 18 | R$ 37,00 | C11 Gerador de apostilas (IA) | professor | ES/LATAM: 0; IT: só fichas prontas BR (USD) e Edudoro PLN ~58 d | ES BRECHA (software) |
| 119 | Gerador de Apostilas | Educação e professores | 70 | 18 | R$ 37,00 | C11 Gerador de apostilas (IA) | professor | idem 118 | ES BRECHA (software) |
| 120 | Plataforma Clínica Inteligente | Enfermagem e medicina | 80 | 17 | R$ 49,00 | C13 Plataforma IA de relatórios psico/neuropsicopedagogia | psicopedagoga/neuropsicopedagoga | ES/LATAM ‘informe psicopedagógico plantilla’: 0 | BRECHA (software) |
| 121 | K34/ Quer tocar e cantar na sua igreja sem complicação? | Música e instrumentos | 186 | 17 | WhatsApp/— | C24 Cifras simplificadas para igreja | músico de igreja | ES/US: Colección Digital De Fe ARS ~4 d, TDCG USD, Viva Semente BRL | TESTE |
| 122 | Kit Encadernação 2027 | Artesanato, moldes e papelaria | 112 | 17 | R$ 10,00 | C1 Kit encadernação 2027 | artesã de papelaria | idem C1 | IT BRECHA sazonal |
| 123 | Macros e Templates que automatizam processos para Sublimação | Design e redes sociais | 181 | 17 | R$ 37,00 | C23 Macros CorelDRAW para sublimação | sublimador | ES/LATAM: Smartsubli (BRL, brasileiro) ~23 d | TESTE |
| 124 | 💛 Um presente que cuida de quem você ama, mesmo quando vo… | Educação e professores | 85 | 17 | WhatsApp/— | C9 Estimulação cognitiva para idosos | família/cuidador (BR); profissional de RSA (IT/FR) | LATAM: Cognimente PEN, Tu Libro Digital MXN, Mejora tu Memoria MXN; IT: Palestra Mentale USD 11 anúncios ~15 d, Seduta Pronta ~2 d; FR: The Resource Lab USD ~10 d; ES (profissional): 0; DE: 0 | IT/FR TESTE; ES/DE BRECHA |
| 125 | +60 Projetos de Galinheiros Lucrativos | Projetos e marcenaria | 48 | 17 | R$ 19,90 | C4 Projetos de galinheiro | pequeno produtor | dentro de C4 (marcenaria saturada em EN/ES) | não priorizado |
| 126 | Os 16 Odus Meji Ilustrado | Outros | 75 | 17 | R$ 17,90 | C25 Odus Meji (Ifá) | religioso afro | ES/US: Secretos de la Santería MXN ~10 d | TESTE pequeno |
| 127 | Sistema Consultoria Única | Jurídico | 83 | 17 | R$ 27,00 | C18 Sistema de consultoria pronto | consultor autônomo | ES/LATAM: 0; EN: 350 anúncios (saturado) | ES BRECHA |
| 128 | ↪️ Para ter acesso aos +300 Moldes de Mesa Posta, comente… | Artesanato, moldes e papelaria | 72 | 17 | R$ 10,00 | C3 Moldes de mesa posta | artesã | não pesquisado à parte | — |
| 129 | Vai construir? | Engenharia e arquitetura | 195 | 16 | WhatsApp/— | C6 Plantas de casas | quem vai construir | LATAM: Creativo AZ COP ~129 d (produto VERIFICAR), Aprendia MXN ~13 d, Homtak MXN | PROVADO? (VERIFICAR) |
| 130 | Kit de Programas Transformação | Psicopedagogia, TEA e TDAH | 183 | 16 | R$ 47,00 | C13 Programas ABA (VB-MAPP) | terapeuta ABA/AT | FR: ABA Online EUR 44 anúncios ~148 d; US: ABA Tools ~133 d; LATAM: Conecta ABA USD ~7 d, Mini Logros PEN ~1 d; IT/ES/PT: só cursos; PL: Pro-Edukacja PLN ~280 d (pacote autismo) | IT/ES/PT BRECHA; LATAM TESTE; FR/US/PL PROVADO |
| 131 | This Page Does Not Exist | Lash, nail e sobrancelha | 198 | 16 | WhatsApp/— | C26 Curso de extensão de cílios | lash designer | não pesquisado (curso, fora do modelo) | fora |
| 132 | Protocolo Capilar Natural | Cabelo e barbearia | 72 | 16 | WhatsApp/— | C8 Protocolo capilar natural | consumidora | não pesquisado à parte (bump de C8) | — |
| 133 | Resumo Esquematizado | Concursos e estudos | 70 | 16 | R$ 37,00 | C14 Resumo esquematizado de psicologia | estudante de psicologia | não pesquisado à parte | — |
| 134 | Biblioteca Profissional Ambiental | Outros | 48 | 16 | R$ 19,90 | C17 Modelos de projetos ambientais | engenheiro/consultor ambiental | LATAM: só cursos (ISE-Ambiental PEN, IMIIL MXN, FaunaLab MXN); pack de modelos: ninguém | LATAM BRECHA |
| 135 | Pack MasterLash Canva 2.0 | Design e redes sociais | 48 | 16 | R$ 27,90 | C22 Posts Canva para lash designer | lash designer | ES/LATAM: packs genéricos USD/BRL; IT: nenhum pack para estetista | saturado ES; IT sem prova |
| 136 | 🧠✨ 50 pranchas para brincar de massinha em um único arquivo | Educação e professores | 61 | 16 | R$ 10,00 | C10 Pranchas de massinha | pais/professores infantil | ver C10 | ver C10 |
| 137 | 2500+ Artes Cristãs Premium para Camisetas e Estamparia | Design e redes sociais | 134 | 15 | R$ 10,00 | C23 Artes cristãs para camisetas | estampador/sublimador | ES/US: Creación Cristiana USD ~95 d, Fe y Diseño BOB ~23 d, Pixelpack USD | PROVADO (USD) |
| 138 | 🪑Transforme madeira em móveis profissionais - mesmo sendo… | Projetos e marcenaria | 73 | 15 | WhatsApp/— | C4 Projetos de marcenaria (móveis) | marceneiro iniciante | ES/LATAM: 144 anúncios; EN: 714 (inclui BR em BRL/CZK) | SATURADO |
| 139 | 🌺 Mais de 1.000 estampas que deixam qualquer pano de prat… | Design e redes sociais | 83 | 15 | WhatsApp/— | C23 Estampas para pano de prato | artesã de pintura/estampa | não pesquisado à parte | — |
| 140 | Entre em contato | Design e redes sociais | 48 | 15 | WhatsApp/— | C26 Pack de otimização de PC | usuário de PC | não pesquisado | fora |
| 141 | 📦 Reponha seu toner antes de acabar | Artesanato, moldes e papelaria | 55 | 15 | WhatsApp/— | — Toner (loja física) | empresa | não é infoproduto | fora |
| 142 | Kit de Alfabetização Alfa Kids | Educação e professores | 165 | 14 | R$ 57,00 | C10 Kit de alfabetização | pais | ver C10 | ver C10 |
| 143 | Ludica pedagogica | Educação e professores | 148 | 14 | R$ 15,00 | C10 Jogos de leitura | professores/pais | ver C10 | ver C10 |
| 144 | 50 Viral Kids | Design e redes sociais | 59 | 14 | R$ 47,00 | C22 Posts para personal trainer | personal trainer | não pesquisado à parte (mesmo padrão de C22) | — |
| 145 | Crie peças lindas em apenas 15 minutos, sem sair de casa | Artesanato, moldes e papelaria | 66 | 14 | R$ 37,00 | C3 Bordado no papel | artesã | ES/LATAM: Bordados en Papel USD (clone da copy BR) ~1 d | TESTE |
| 146 | +100 Moldes em PDF | Projetos e marcenaria | 96 | 14 | WhatsApp/— | C4 Moldes de casinhas/comedouros | artesão de madeira | dentro de C4 | SATURADO |
| 147 | Quem vende geladinho em 2026 sabe de um segredo… | Receitas e confeitaria | 113 | 14 | WhatsApp/— | C7 Receitas de geladinho gourmet | renda extra | ES/LATAM: Marcianitos Pro ARS, Heladitos Gourmet USD, Máster Class COP ~79 d | PROVADO (ES) |
| 148 | 🌿 Você já pensou em conhecer o poder das ervas medicinais? | Receitas e confeitaria | 111 | 14 | WhatsApp/— | C8 Ervas medicinais/garrafadas | consumidor | ES/LATAM: Saber Digital USD ~322 d, Secretos Naturales COP | PROVADO (USD) |
| 149 | 🏠 Dê asas à imaginação do seu filho com projetos incrívei… | Engenharia e arquitetura | 75 | 14 | WhatsApp/— | C4 Projetos de papelão (infantil) | pais | não pesquisado à parte | — |
| 150 | Responda o questionário e, no final, você pode receber o kit | Religioso | 71 | 14 | WhatsApp/— | C25 Kit São Bento (quiz) | católico | não pesquisado (kit físico/quiz) | fora |
| 151 | ✨São mais de 70 posts🤎 | Design e redes sociais | 49 | 14 | R$ 47,00 | C22 Posts para ‘Dra.’ (estética) | profissional de estética | ver C22; atenção: fora do escopo se for HOF | saturado |
| 152 | A Axxen oferece modelos prontos de monetização para conta… | Contábil e tributário | 49 | 14 | WhatsApp/— | C20 Monetização para contadores (Reforma Tributária BR) | contador | gancho exclusivo do Brasil | fora |
| 153 | Maleta Digital do Instalador de Segurança Eletrônica | Elétrica, eletrônica e indústria | 100 | 14 | R$ 17,00 | C15 Maleta digital do instalador de segurança eletrônica | instalador de CFTV/alarme | AR: Iad Cursos ARS curso ~75 d; LATAM USD: testes ≤17 d; ES/IT/PT/FR/DE/PL: ninguém; UK: InstallerDocs 0 d | EU BRECHA; LATAM TESTE |
| 154 | Mapas Mentais | Concursos e estudos | 89 | 13 | R$ 67,00 | C14 Mapas mentais para concursos | concurseiro | ES: só academias + Emma Schneider (BRL) ~7 d; IT: concorsi_essentials EUR ~4 d | ES/IT TESTE |
| 155 | Guia do Perito Blindado | Jurídico | 103 | 13 | R$ 67,00 | C19 Guia do perito judicial | perito judicial | ES/LATAM: 220 anúncios, cursos/serviços; nenhum guia de posicionamento | TESTE fraco |
| 156 | A TransformaFit é o método que te mostra como ter resulta… | Fitness e educação física | 330 | 13 | WhatsApp/— | C26 Treinos com peso do corpo | consumidor fitness | não pesquisado (oceano vermelho) | fora |
| 157 | Planilha de Gestão Financeira Empresarial | Negócios, finanças e planilhas | 166 | 13 | R$ 10,00 | C21 Planilha de gestão financeira/precificação | pequeno empresário | CL: Eve Uribe CLP ~39 d; Educateka USD ~35 d | CL PROVADO |
| 158 | Desenvolva a escrita do seu filho | Outros | 97 | 13 | R$ 37,00 | C10 Grafomotricidade | pais/professores | MX: Kid Genius ~251–325 d, Stardex ~269 d; PE: Aprendo contigo ~124 d; IT: Mente Gentile EUR ~41 d; PL: Gugu Rabbit PLN ~807 d, ABC w dydaktyce ~114 d; FR: 0 | FR BRECHA; IT/MX/PL PROVADO |

## 3. Resultado por país dos conceitos pesquisados
P = PROVADO (≥30 d no país/moeda) · T = TESTE (vendedor <30 d) · B = BRECHA (ninguém no termo) · S = saturado · — = não pesquisado. "Neutro" = espanhol em USD sem país.

| Conceito | ES | MX | CO | AR | CL | PE | Neutro USD | PT | IT | FR | DE | PL | EN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kit ABA | B | B? (Jokipoky MXN, VERIFICAR) | B (só diplomados) | B | B | T (Mini Logros, 1 d) | T (Conecta ABA, 7 d) | B | B (só cursos) | **P** (ABA Online, 148 d, 44 anúncios) | — | **P** (Pro-Edukacja, 280 d, pacote autismo) | **P** (ABA Tools 133 d) |
| Estimulação cognitiva p/ profissional de lar | **B** | T (consumo) | — | — | — | T (Cognimente, consumo) | — | — | T (BR: Palestra Mentale 15 d) | T (BR: The Resource Lab 10 d) | B | — | — |
| Maleta instalador CFTV | B | B (só serviços) | B | P (curso Iad 75 d) | B | B | T (≤17 d) | B | B | B | B | B | B (UK InstallerDocs 0 d) |
| Documentos do psicólogo* | P/T (notas: Herramientas Terapéuticas 68 d + LATAM vazando) | P | P | T (Psicoagenda 22 d) | B | B | — | B | P (BR €19,99) | B | B | P (escolar) | — |
| Grafomotricidade | B | **P** (250–325 d) | B | B | B | **P** (124 d) | — | — | **P** (Mente Gentile 41 d, EUR) | B | — | **P** (nativos, até 807 d) | — |
| Kit do consultor | B | B | B | B | B | B | B | — | — | — | — | — | S |
| Catálogo herrería/pérgolas | B | T (13 d) | B | B | B | B | — | — | — | — | — | — | S (marcenaria) |
| Planilha precificação | — | T | — | — | **P** (Eve Uribe 39 d) | — | T/P (Educateka 36 d) | — | — | — | — | — | — |
| Mapas/esquemas concursos | T (BR 7 d) | — | — | — | — | — | — | — | T (4 d) | — | — | — | — |
| Calendários 2027 | S | S | S | S | S | S | S | — | B | — | — | — | — |
| Projetos ambientais | B | B (só cursos) | B | B | B | B (só cursos) | — | — | — | — | — | — | — |
| Receitas para vender | — | T | **P** (79 d) | T | — | — | **P** (61 d) | — | — | — | — | — | — |
| Ervas medicinais | — | — | T | — | — | T | **P** (322 d) | — | — | — | — | — | — |
| Eletricista | — | T | — | **P** (79 d) | — | — | **P** (56 d) | — | — | — | — | — | — |
| Artes cristãs | — | — | — | — | — | — | **P** (95 d) | — | — | — | — | — | — |
| Plantas de casas | — | T | P? (129 d, VERIFICAR) | T | T | T | — | — | — | — | — | — | — |
| Marcenaria hobby | S | S | S | S | S | S | S | — | — | — | — | — | S |
| Posts por profissão | S | S | S | S | S | S | S | — | B (sem pack) | — | — | — | — |
| Bordado no papel / moldes / cifras / Ifá | — | T (Ifá, 10 d) | — | T (cifras, 4 d) | T (moldes, CLP) | — | T (bordado clone BR 1 d; cifras; moldes) | — | — | — | — | — | — |

\* Psicólogo: ES/MX/CO/IT/PT/FR/DE/PL vêm das notas de 28–29/10 (`fila-ofertas.md`, `pesquisa-europa.md`); AR/CL/PE/EC/UY medidos hoje.

## 4. Aprofundamento das brechas fortes
Nenhuma página de vendas abriu (bloqueio de rede). Preço e conteúdo vêm do texto dos anúncios e do JSON. Tamanho de mercado e normas estão marcados VERIFICAR porque não foi possível consultar fonte oficial nesta sessão.

### 4.1 Kit ABA: programas prontos + folhas de registro + app de coleta (130, com 120 como bump)
- **Prova BR:** Inovaba "Kit de Programas Transformação", 183 dias, 16 ativos, R$47, "programas baseados no VB-MAPP".
- **Prova de que a Europa paga:** ABA Online (FR, EUR). 44 anúncios, o mais antigo com ~148 dias ("Mesurer avant d'intervenir : 8 grilles à télécharger"). Vende grilles de cotation, livrets VB-MAPP, contrato terapêutico, formações e um app no Google Play. É exatamente o formato kit + app.
- **Prova EN/PL:**
  - ABA Tools (US), ~133 dias;
  - The Autism Helper "VB-MAPP Assessment Kit", ~101 dias;
  - Pro-Edukacja.pl "Pakiet Autyzm 79 zł", ~280 dias.
- **Onde ninguém vende kit:** Itália (só cursos: Intandem "Corso VB-MAPP", Iescum, ICOTEA, ComportaMente), Espanha e Portugal.
- **Na LATAM a onda começou esta semana:**
  - Conecta ABA (USD): "58 programas ABA listos para aplicar", "con registro incluido", ~7 d;
  - Mini Logros (PEN): "Abres, aplicas y registras", ~1 d.
- **Produto proposto:** "La Valigetta del Terapista ABA" (IT) e "Maletín del Terapeuta ABA" (ES/LATAM). Conteúdo:
  - programas por área (mando, tato, imitação, ecoico, AVD);
  - folhas de registro (tentativas, ABC, intervalo);
  - plano de intervenção e relatório para a família/escola;
  - contrato e consentimento;
  - app de coleta: toque por tentativa → % de acerto → gráfico → PDF. O app de inspeção serve de base: checklist que vira formulário e relatório.
- **Cuidado:** VB-MAPP é instrumento protegido por direitos autorais (Sundberg/AVB Press). Usar "programas por marcos de desenvolvimento", com conteúdo próprio, sem copiar o protocolo. Status: VERIFICAR.
- **Gancho legal:** IT, linha-guia ISS sobre autismo que recomenda intervenções comportamentais (VERIFICAR número/ano); ES, sem profissão ABA regulamentada (VERIFICAR); MX/CO, centros ABA privados.
- **Tamanho:** VERIFICAR no registro de certificados BACB por país e no número de centros.
- **Reaproveitamento:** Valigetta (estrutura e checkout) + app de inspeção (formulário → relatório).

### 4.2 Oficinas prontas de estimulação cognitiva para profissionais de lares (124, versão profissional)
- **Prova BR:** a oferta 124 é de consumo (presente para os pais): 85 dias, 17 ativos, via WhatsApp.
- **O sinal forte vem de fora do BR.** Operadores com conta em USD (padrão brasileiro) e copy idêntica no formato "pronto":
  - Palestra Mentale (IT): "Un anno di laboratori, pronto da stampare", 11 anúncios, ~15 d, criativos novos há ~9 d;
  - Seduta Pronta (IT): "La seduta di domani, già pronta", ~2 d;
  - The Resource Lab (FR): "Votre semaine d'ateliers, déjà prête", ~10 d.

  Isso repete o que aconteceu com o dentista na Itália (Kit Studio Blindato, que agora também anuncia "APP", ~8 d).
- **Espanha:** 0 anúncios para profissionais ("talleres estimulación cognitiva residencias", "sesiones… para terapeutas"). **Alemanha:** 0.
- **LATAM:** só consumo (Cognimente PEN, Tu Libro Digital MXN, Mejora tu Memoria MXN).
- **Produto proposto:** "Maletín del Animador/Terapeuta Ocupacional de Residencias", com:
  - 52 semanas de talleres (memória, atenção, linguagem, orientação);
  - fichas impressas por nível (GDS 3–5);
  - registro de participação e avaliação para o plano individual;
  - app de agenda das oficinas + registro de presença → relatório mensal à família/direção.
- **Gancho:** documentação de atividades no plano de atenção individual exigido pelas normas regionais de residências (ES), PAI nas RSA (IT) e projet d'animation nos EHPAD (FR). VERIFICAR norma e artigo em cada um.
- **Tamanho:** número de residências e de animadores/TO por país. VERIFICAR (IMSERSO/CCAA, ISTAT presidi residenziali, DREES EHPAD).
- **Ação:** lançar na **Espanha primeiro** (ninguém). Re-checar IT/FR em 13–18/11, quando os BR completam 30 dias. Se continuarem, IT/FR viram PROVADO e valem o port.
- **Reaproveitamento:** Valigetta + app de inspeção (registro de sessão).

### 4.3 Maleta do instalador de CFTV com pacote RGPD + app de vistoria (153)
- **Prova BR:** 100 dias, 14 ativos, R$17. Conteúdo: tutoriais de câmera, DVR, acesso remoto, alarme, cerca elétrica.
- **Fora do BR:**
  - Iad Cursos Online (AR, ARS) tem curso de CFTV com ~75 d. É PROVADO, mas é curso, não kit.
  - Academia Online PRO, Bien laburado e CMDigital (USD) são testes de ≤17 d.
  - Espanha, Itália, Portugal, França, Alemanha, Polônia, UK/US/AU/CA: ninguém vende kit ou curso para o instalador; só aparecem empresas de instalação. InstallerDocs (UK, 0 d) VERIFICAR.
- **Diferencial europeu:** o instalador entrega ao cliente os documentos de proteção de dados. Itens:
  - cartaz de "zona videovigilada";
  - informação de 2ª camada;
  - registro de atividades de tratamento;
  - contrato de encarregado de tratamento quando faz manutenção remota;
  - em IT, acordo sindical/autorização da Inspeção do Trabalho para câmeras com empregados;
  - checklist de vistoria + relatório fotográfico de entrega (app de inspeção) + orçamento.
- **Normas:** ES LOPDGDD art. 22; IT Garante + art. 4 L. 300/1970; PT Lei 58/2019. Todas VERIFICAR.
- **Risco:** instalador europeu compra pouco por Meta (Espanha/Itália com 0 anúncios pode ser falta de demanda). Testar barato.
- **Tamanho:** VERIFICAR (registro de empresas de segurança do Ministerio del Interior ES; imprese installatrici IT).
- **Reaproveitamento:** app de inspeção (núcleo) + Valigetta (documentos).

### 4.4 Maletín del Psicólogo para Argentina e Chile (117)
- **Prova BR:** Combo PSI Prático, 72 dias, 18 ativos, R$37,90, "+3.000 psicólogos".
- **Hoje:**
  - AR: Psicoagenda (ARS), ~22 d, produto a confirmar (agenda/software?);
  - CL, PE, EC, UY: ninguém no termo.
- **Já conhecido (notas):** MX e CO GO, IT com BR a €19,99, PL escolar.
- **Por que considerar:** reaproveitamento máximo do Maletín MX. Precisa de voseo e das normas AR (Ley 26.657 de Salud Mental; lei de exercício profissional; secreto profesional). VERIFICAR.
- **Régua:** sem prova no país. É TESTE barato depois de MX e CO.

### 4.5 Kit del Consultor em espanhol (127)
- **Prova BR:** Sistema Consultoria Única, 83 dias, 17 ativos, R$27. Conteúdo: proposta, contrato, diagnóstico, onboarding, plano de ação, cronograma.
- **Fora do BR:** espanhol com 0 anúncios; inglês saturado (350).
- **Reaproveitamento:** a **Consultora** (simulador de inspeção) vira o "diagnóstico do cliente" dentro do kit.
- **Ressalva:** público difuso (consultor de quê?). Melhor nichar, por exemplo "consultor de seguridad alimentaria", que é a ponte natural com a Consultora.

## 5. Ranking 0–10 das brechas desta faixa
Critérios: prova BR (dias/ativos) + prova estrangeira de que o formato vende + vazio no país-alvo + encaixe kit + app + reaproveitamento − custo de produção/risco.

| # | Brecha | Países-alvo | Nota | Régua | Reaproveitamento |
|---|---|---|---|---|---|
| 1 | Kit ABA (programas + registros + app de coleta) | IT, ES, PT; LATAM (corrida) | **7,5** | IT/ES/PT BRECHA; FR/US/PL PROVADO; LATAM TESTE (7 d) | Valigetta + app de inspeção |
| 2 | Oficinas de estimulação cognitiva para profissionais de lares | ES (1º), depois IT/FR | **7,0** | ES BRECHA; IT/FR TESTE (BR 10–15 d) | Valigetta + app (registro de sessões) |
| 3 | Maleta do instalador CFTV + RGPD + app de vistoria | ES, IT, PT | **6,0** | BRECHA total na UE; AR PROVADO (curso) | App de inspeção + Valigetta |
| 4 | Maletín del Psicólogo AR/CL | AR, CL | **6,0** | TESTE (AR 22 d, produto incerto) | Maletín MX direto |
| 5 | Kit del Consultor (nichado em segurança alimentar) | ES, LATAM | **5,5** | BRECHA em espanhol | Consultora |
| 6 | Cahier de graphisme / grafomotricidade | FR (IT já tem nativo) | **5,5** | FR BRECHA no termo; IT/MX/PL PROVADO | — (consumo) |
| 7 | Catálogo de herrería/pérgolas para cotar no WhatsApp | MX, ES, CO | **5,0** | MX TESTE (13 d); resto BRECHA | App de inspeção como app de orçamento |
| 8 | Planilha de precificação | CL/AR; PT-PT/IT via motor Termometro | **5,0** | CL PROVADO (39 d) | Motor do Termometro 85k |
| 9 | Esquemas para oposiciones / concorsi | ES, IT | **5,0** | TESTE (BR na ES 7 d; IT 4 d) | — |
| 10 | Calendários 2027 para imprimir/vender | IT (PRAZO natural: até jan/2027) | **4,5** | IT BRECHA; ES saturado | — |
| 11 | Pack de modelos de projetos ambientais | PE, CO, MX | **4,0** | LATAM BRECHA (só cursos) | — |
| 12 | Gerador de apostilas/fichas com IA | ES, IT | **4,0** | ES BRECHA; IT com onda BR de fichas | — (software) |
| 13 | Receitas para vender (bolis/marcianitos) | LATAM | 4,0 | PROVADO (CO 79 d) com concorrência | — |
| 14 | Ervas medicinais / artes cristãs / eletricista | espanhol neutro | 3,5 | PROVADO (56–322 d), saturando | — |
| 15 | Bordado no papel, cifras de igreja, Ifá, moldes de vestido | espanhol neutro/MX | 3,0 | TESTE (BR já clonando) | — |
| 16 | Posts por profissão, marcenaria hobby, perito | — | 2,5 | saturado / sinal fraco | — |

**Datas de re-checagem** (quando os testes atuais completam 30 dias):
| Data | O que olhar |
|---|---|
| 07/11 | Psicoagenda AR |
| 13/11 | Palestra Mentale IT |
| 16/11 | Herrería MX |
| 18/11 | The Resource Lab FR |
| 21/11 | Conecta ABA (neutro) e Emma Schneider (ES) |
| 25/11 | concorsi_essentials IT |
| 28/11 | Bordados en Papel e Mini Logros |

## 6. Lista final de VERIFICAR
1. **Páginas de vendas BR não abertas** (bloqueio de rede): instaladorseguranca.lovable.app, inovaba.com.br/kit-documentos-terapia-aba/, packengambiental.lovable.app, alaincarboni.com/consultoria-singular/, projetotecapergolados.lovable.app, combopsi.lovable.app, neurolyn.com.br, mapeei.com, oficinalucrativa.xyz (qual é o "+5.000 moldes"?). Pegar preço, bumps, garantia e plataforma no navegador do Mac.
2. **ABA:**
   - contagem de BCBA/RBT por país (registro BACB) para IT/ES/MX/CO;
   - linha-guia ISS (IT) sobre intervenções comportamentais no autismo (número/ano);
   - situação legal do ABA na Espanha;
   - limites de uso do VB-MAPP (direito autoral);
   - preço e conteúdo de Conecta ABA, Mini Logros, ABA Online (FR) e Pro-Edukacja (PL).
3. **Estimulação cognitiva:**
   - Palestra Mentale, Seduta Pronta e The Resource Lab são o mesmo operador? Preço?
   - re-checar IT/FR quando completarem 30 dias;
   - norma de atividades/PAI em residências ES (por comunidade autônoma), RSA (IT) e projet d'animation EHPAD (FR);
   - número de residências/animadores (IMSERSO, ISTAT, DREES);
   - dias reais de Cognimente, Tu Libro Digital e Mejora tu Memoria.
4. **CFTV:**
   - ES LOPDGDD art. 22 e guia AEPD de videovigilância (cartaz, prazo de conservação);
   - IT Garante (FAQ videosorveglianza) + art. 4 L. 300/1970;
   - PT Lei 58/2019 / CNPD;
   - nº de empresas instaladoras (Ministerio del Interior ES);
   - o que é InstallerDocs (UK).
5. **Psicólogo AR:** produto da Psicoagenda; Ley 26.657 e lei de exercício da psicologia (nacional/provincial); nº de psicólogos na AR.
6. **Grafomotricidade FR:** testar outros termos ("écriture cursive", "graphisme PS MS GS", "cahier d'écriture") antes de declarar brecha; preço da Mente Gentile (IT).
7. **Planilha:** total de anúncios e preço da Eve Uribe (CL); produto real da Creativo AZ (CO, 129 d, apareceu em "planos de casas").
8. **Kit Immobiliare Pro (Paulina Vera, IT, USD, ~1 d):** brasileiro levando kit de corretor para a Itália. Fora desta faixa, mas vale repassar ao agente de imobiliário.
9. **Kit Studio Blindato** agora anuncia "APP" na Itália (~8 d). Concorrente direto da Valigetta: abrir a página e ver o app.
10. **Idiomas não pesquisados:** RO, CZ, SK, HU, GR, NL, TR em todos os conceitos; DE/PL/PT-PT/FR na maioria dos conceitos de consumo. Rodar quando o SearchAPI voltar (08/11), com os termos do glossário.
11. **Dias por página:** só foram medidos por `page_ids` Iad Cursos, Academia Online PRO, Bien laburado, InstallerDocs, Mini Logros, Conecta ABA, ABA Online, Herrería e Palestra Mentale. Os demais dias são o anúncio mais antigo visto na busca, ou seja, um piso, não o valor exato.

---
## ANEXO A — Diário de medições (conector Meta, 30/10/2026, só anúncios ativos)
Observação de método: a busca do conector ordena do anúncio mais novo para o mais velho e devolve no máximo 50; em termos com muitos resultados, vendedores antigos podem ficar fora da janela. Por isso usei frase exata (entre aspas) e termos de infoproduto ("curso", "PDF", "plantillas", "kit"), e medi DIAS REAIS por `page_ids` só nos vendedores relevantes. WebFetch das páginas de vendas foi BLOQUEADO pela rede do container (lovable.app, inovaba.com.br, alaincarboni.com etc. não resolvem; hotmart/kiwify com 403 no proxy). Preço e conteúdo vêm do texto do anúncio no JSON; o que não deu para abrir fica VERIFICAR.

### A1. Maleta do instalador de segurança eletrônica (153)
- ES-LATAM (MX/CO/AR/CL/PE), termo "instalación de cámaras de seguridad": 2.207 anúncios, quase todos de prestadores de serviço/lojas (ruído). Frase exata "instalador de cámaras" + PDF: 15 anúncios.
  - Iad Cursos Online (page 101583268685680, ARS): 13 ativos, mais antigo há ~93 dias (curso de eletricidade); anúncio específico "Aprendé Cámaras de Seguridad" há ~75 dias; "Convertite en instalador de CCTV" há ~44 dias. CURSO, não kit de documentos. PROVADO (AR, curso).
  - Academia Online PRO (114590668253097, USD neutro): 6 ativos, ~5 dias (guia de instalação/eletricidade). TESTE.
  - Bien laburado (1271362576071315, USD): 5 ativos, ~2 dias. TESTE.
  - CMDigital (962417550298160, USD): "Mega pack instalador de redes WiFi y cableado", ~17 dias. TESTE.
- ES (Espanha), "curso instalador cámaras": 0.
- EN (US/GB/AU/CA), "CCTV installer": 47 anúncios, todos prestadores de serviço; exceção InstallerDocs (1406430925887218, GBP), 1 anúncio, 0 dia (documentação para instaladores, VERIFICAR o que é).
- IT "corso videosorveglianza": 7, todos empresas de instalação/imobiliárias. Ninguém vende kit/curso. BRECHA.
- FR "formation vidéosurveillance": 2 (MaxioM, ~8 dias, parece DIY; SurveyCam, empresa local). BRECHA.
- PT "curso CCTV": 0 relevante. BRECHA.
- Leitura: nenhum vendedor de "maleta" (documentos + checklists) para instalador em nenhum país; em AR existe CURSO provado (Iad, ~75 d no anúncio de câmeras). Gancho legal possível na Europa: cartaz/aviso obrigatório de zona videovigiada e informação RGPD (ES LOPDGDD art. 22; IT GDPR + art. 4 Statuto dei Lavoratori para câmeras com funcionários; PT Lei 58/2019) → VERIFICAR com fonte oficial antes de usar.

### A2. Programas ABA / VB-MAPP (130) e plataforma IA psico/neuropsicopedagogia (120)
- Busca "VB-MAPP" em 15 países (LATAM, ES, EN, IT, PT, FR, DE, PL): 25 anúncios.
  - FR: **ABA Online** (page 1850476768389167, EUR): 44 ativos, mais antigo ~148 dias ("Mesurer avant d'intervenir : 8 grilles à télécharger"); vende grilles, livrets VB-MAPP, contrato, formações e app (Google Play). PROVADO FR (documentos + app + formação). Concorrente direto do modelo kit + app.
  - US: ABA Tools (108617997275390, USD) ~133 dias, 10+ anúncios; The Autism Helper "VB-MAPP Assessment Kit" ~101 dias. PROVADO EN-US (mercado TPT saturado).
  - IT: só cursos (Intandem Formazione "Corso VB-MAPP" ~14 d; Iescum; ICOTEA; Centro APP; ComportaMente). Nenhum kit low ticket. BRECHA IT para kit de programas/registros.
- "programas ABA" (LATAM + ES): 24 anúncios.
  - Conecta ABA (1467060063146717, USD neutro): 3 ativos, ~7 dias ("58 programas ABA listos para aplicar", "Programas ABA con registro incluido"). TESTE.
  - Mini Logros (1393263263878199, PEN): 3 ativos, ~1 dia ("Abres, aplicas y registras"). TESTE Peru.
  - PsicoKids and Teens (COP): diplomados ABA/TEA (curso). Abaedu Latam (BRL, curso de aplicador).
- "terapia ABA" ES+PT: nada de kit (NeuroIdea COP vazando). BRECHA ES e PT.
- PL "ABA autyzm materiały": **Pro-Edukacja.pl** (840454552492924, PLN) "PAKIET AUTYZM 2+2 GRATIS! Tylko 79 zł" com anúncio ativo há ~280 dias. PROVADO PL (pacote de formações/materiais sobre autismo para professores/terapeutas, 79 zł).
- Leitura: ABA é o único conceito desta faixa com vendedor de "documentos + app" provado fora do Brasil (FR, ABA Online, 148 d). Na LATAM há dois testes de "programas ABA listos" com 7 dias ou menos (USD e PEN), sinal de que a onda está começando. IT/ES/PT: só cursos, ninguém com kit.

### A3. Biblioteca de projetos ambientais (134)
- ES-LATAM+ES "plan de manejo ambiental" modelos: 2 anúncios sem relação. "ingeniero ambiental plantillas": 2 (página genérica de IA, MXN).
- "estudio de impacto ambiental" curso: 16 anúncios, todos de institutos/cursos (ISE-Ambiental PEN, Instituto Mexicano de Ingeniería Industrial MXN, FaunaLab MXN "Guía Integral de Monitoreo… Arrecifes", GeoCaps, Ecoambiental Group PEN). Nenhum pack de modelos low ticket. BRECHA LATAM (demanda existe via cursos; produto de modelos não existe). Europa não pesquisada a fundo: na UE o trabalho ambiental é assinado por técnico habilitado e os modelos variam por região (baixo encaixe).

### A4. Sistema de consultoria pronto (127)
- ES-LATAM+ES "plantillas para consultores propuesta contrato": 0. BRECHA em espanhol.
- EN "consulting templates": 350 anúncios (US/GB/AU/CA), com vendedores de PDF instantâneo (Dan Hart, Business Explained, USD). Mercado EN saturado/PROVADO por volume (dias não medidos).

### A5. Perito judicial (155)
- ES+LATAM "perito judicial": 220 anúncios; maioria cursos/diplomados (Instituto Dasein Meraki MXN "Diplomado Perito en Medicina Forense"), serviços (perito_judicial_edificacion EUR, PsicologosForenses.com ARS), "Guias profesionales - aprendia" (MXN, guias profissionais, VERIFICAR) e Ratio Studio "Guía Práctica de Daños y Perjuicios" (USD, para advogados). Nenhum "guia de marketing do perito" como o BR. TESTE fraco; produto BR é de posicionamento/marketing, pouco ligado a norma.

### A6. Projetoteca de pergolados/toldos (113) e projetos de marcenaria (138, 146, 125, 149)
- ES-LATAM+ES "proyectos de pérgolas": 331 anúncios, quase tudo fabricante/loja. Achado: **Planos y Diseños de Herrería** (page 1197011490158539, MXN), 7 ativos, mais antigo ~13 dias ("MEGA PACK DE PLANOS HERRERÍA Y CARPINTERÍA", "diseños para explorar, cotizar y fabricar"). Mesmo conceito do BR (catálogo para o profissional cotar), para herrero. TESTE MX.
- "planos de carpintería PDF" (LATAM+ES): 144 anúncios; Proyectos Carpinteros (USD, "+150 Proyectos de Carpintería", 10+ criativos novos), Al Interiorismo (USD, "50 planos + 5 regalos"), Metal & Madera (ARS), Elias Joel "Curso Melamina Pro 360 PDF" (ARS), Tienda Digital Perú (PEN). Mercado aquecido/competitivo em espanhol neutro.
- EN "woodworking plans": 714 anúncios; Weekend Woodshop (anunciante em BRL vendendo em inglês, "16,000+ plans"), Woodworking DIY Ideas (CZK), Wood Atlas Plans (EUR), The Backyard Woodworker (AUD), WoodSense, Go4Wood. SATURADO (inclusive por brasileiros).
- Leitura: marcenaria hobby já é oceano vermelho em EN e ES. O ângulo que sobra é o PROFISSIONAL (catálogo para serralheiro/herrero/instalador de toldos cotar no WhatsApp), que só tem 1 teste de 13 dias no México.

### A7. Gerador de apostilas para professores (118, 119)
- ES-LATAM+ES "generador de fichas docentes inteligencia artificial": 0. Ninguém anuncia gerador de apostilas/fichas com IA em espanhol. BRECHA (mas é software; exige produto SaaS).
- IT "schede didattiche pronte da stampare": 8 anúncios, todos recentes e de vendedores com conta em USD (padrão de brasileiro exportando): Attività Premium ("2.500 schede a 7,90 €", ~0 d), Prof di Scienze ("120 schede di scienze", ~1 d), Mondo Infanzia Didattica (~9 d); Edudoro.eu (empresa polonesa, PLN) ~58 dias. A onda BR de fichas prontas já chegou à Itália; gerador com IA ainda não.

### A8. Mapas mentais para concursos (154) e resumo esquematizado de psicologia (133)
- ES "mapas mentales oposiciones": 4 anúncios, só academias (Granapol Formación Policial, Academia Prefortia). Nenhum vendedor low ticket de mapas. BRECHA ES (oposiciones = mercado grande; ver CONSOLIDADO 28/10, nº 1 da Espanha foi simulador de opositores docentes).
- IT "mappe concettuali concorsi": 8; concorsi_essentials (EUR, ~4 d, "essentials" por concurso, ex.: ASMEL Istruttore amministrativo) = TESTE; Quizly (app de quiz); Ivan Lettura Veloce (método de estudo). BRECHA/TESTE IT.

### A9. Planilha de gestão financeira/precificação (157)
- ES-LATAM+ES "planilla excel costos precios negocio": 13. **Eve Uribe** (page 986872747852950, CLP) "Calcula y vende con seguridad"/"Haz rentable tu negocio", anúncios ativos há ~39 dias = PROVADO CL (≥30 d; nº total de anúncios não medido, VERIFICAR). Educateka (USD) ~35 d; Formatos digitales pro (MXN) novo; Kaptia (ARS) negócio de pan dulce.

### A10. Plantas de casas (129)
- ES-LATAM+ES "planos de casas PDF": 28. **Creativo AZ** (page 110852248404371, COP) com anúncios ativos há ~129 dias ("Adquiérelo ahora mismo", produto VERIFICAR); Aprendia: Guías Oficiales (MXN, "planos acotados, medidas por ambiente y metrados", ~13 d); Homtak (MXN, marketplace de casas, ~10 d); Prof Amanda Lacerda (USD, brasileira em espanhol, novo); Tienda Digital Perú (PEN). Mercado ativo em espanhol; produto BR (VGProjetos) é venda de projeto, não kit.

### B1. Papelaria personalizada 2027: calendários, encadernação, caixas (106, 107, 122)
- ES-LATAM+ES "calendarios 2027 para imprimir": 183 anúncios; muitos packs em USD neutro, todos de poucos dias (Maria Dibujos 3D "12 calendarios 2027 para imprimir y armar", Mente Viva, Decora con Pasión "Superpack viral", Megapack Digital, El Taller de Liz, Mentoría Global). Sazonal e disputado em espanhol neutro.
- IT "calendario 2027 da stampare": 1 (gráfica local). BRECHA sazonal IT (janela nov–jan). FR/DE/PL: não pesquisado (orçamento de buscas).

### B2. Papelaria de casamento editável no Canva (111)
- ES-LATAM+ES "invitaciones de boda editables Canva": 16. Pack de Plantillas (USD, "Pack de invitaciones listos para editar", ~2–3 d, 6 criativos), Mara Cursos y Packs Online (USD, ~44 d), PlayKids (PEN, ~33 d, genérico), Morador marketer (COP, curso de convites digitais). PROVADO fraco em espanhol neutro (USD, sem país definido). Europa não pesquisada.

### B3. Moldes para artesanato e costura (112, 114, 128, 145)
- "moldes de vestidos para niña PDF": 6 (Domina tu arte USD, Cursos PDF CLP), todos novos. TESTE.
- "bordado en papel moldes": 32. **Bordados en Papel** (page 1329354533602746, USD) com a MESMA copy do BR (145: "Creá piezas hermosas en solo 15 minutos, desde tu casa"), 6+ criativos de ~1 dia = clone BR em espanhol neutro. Recursos creativos (USD). TESTE (onda começando).

### B4. Receitas para vender: caseirinhos, geladinho (110, 147)
- "recetas de bolis gourmet para vender": 21. Máster Class Online (COP) anúncio há ~79 dias; Rincón Artesanal (USD) ~61 dias; Marcianitos Pro (ARS, "Tu negocio de marcianitos desde casa"), Dulcaria Repostería (USD, "Heladitos gourmet"), mega pack vips recetas (MXN). PROVADO em espanhol (CO/neutro); equivalente local do geladinho = bolis (MX), marcianitos (AR), helados de vasito (CO).

### B5. Estimulação cognitiva para idosos (124)
- ES-LATAM+ES "estimulación cognitiva adultos mayores cuadernillo": 31. Cognimente (PEN, "Libro de entrenamiento mental", 7 criativos novos), Tu Libro Digital (MXN, "+4.262 descargas"), Mejora tu Memoria (MXN), Recursos Didácticos (PEN). Ativo; dias dos principais não medidos (VERIFICAR).
- IT "stimolazione cognitiva anziani esercizi": 17. **Palestra Mentale** (page 1389699987550571, USD = brasileiro) "Un anno di laboratori, pronto da stampare", ~15 dias, voltado a educadores/animadores de RSA (profissional!); **Seduta Pronta** (1447072035149109, USD) "La seduta di domani, già pronta", ~2 dias (para terapeutas). Onda BR entrando na Itália. TESTE IT.
- FR "stimulation cognitive seniors exercices": 0. BRECHA FR.

### B6. Infantil: grafomotricidade, alfabetização, caligrafia, massinha (115, 136, 142, 143, 158)
- ES-LATAM+ES "grafomotricidad cuadernillo imprimible": 6. **Kid Genius Digital** (MXN) anúncio ativo há ~251 dias; **kidgenius_digital** (MXN) ~325 dias; **Stardex Educación** (MXN) ~269 dias; **Aprendo contigo en PDF** (PEN) ~124 dias. PROVADO MX e PE (longo prazo).
- IT "pregrafismo schede bambini": 4. **Mente Gentile** (page 1263061760225674, EUR) "Radici per la Primaria", ~41 dias = PROVADO IT em euro; Mondo Infanzia Didattica (USD, BR) ~9 d.
- FR "graphisme maternelle fiches à imprimer": 0. BRECHA FR (no termo testado).

### B7. Plantas medicinais/garrafadas (148) e protocolo capilar natural (132)
- ES-LATAM+ES "plantas medicinales recetas remedios PDF": 4. **Saber Digital** (USD) anúncio ativo há ~322 dias; Secretos Naturales (COP, "+900 remedios en PDF", ~2,5 d); Andrés Navarro (PEN, ~16 d). PROVADO em espanhol neutro (USD). Capilar não pesquisado à parte (mesmo público; tratar como bump).

### B8. Música para igreja: cifras simplificadas (121)
- ES+US "tocar en la iglesia acordes": 17. Colección Digital De Fe (ARS, "Cancionero con los Bonos", ~4 d), Tocar Desde Cero Guitarra (USD), Sam On Bass (USD), Viva Semente (BRL = brasileiro vendendo em espanhol, ~14 d). TESTE (ninguém ≥30 d visto).

### B9. Religioso: Odus Meji/Ifá (126) e Kit São Bento (150)
- "Odu Ifá libro PDF": 0; "Ifá Odun": 2 (Secretos de la Santería, MXN, ~10 d). TESTE pequeno (público santero MX/CU/VE/US; Cuba fora do Meta Ads). São Bento: não pesquisado (funil de quiz com kit físico, fora do modelo).

### B10. Estampas: artes cristãs para camisetas (137) e pano de prato (139)
- ES+US "diseños cristianos para sublimar camisetas": 6. **Creación Cristiana** (page 769199572940540, USD) "1000 Diseños Cristianos de calidad", ativo há ~95 dias = PROVADO (espanhol neutro); Fe y Diseño (BOB, Bolívia, "+20.000 diseños religiosos", ~23 d); Pixelpack (USD, "+2.000 diseños cristianos", ~3 d); Bendiciones creativas (USD).

### B11. Posts prontos por profissão (135 lash, 151 estética "Dra.", 144 personal trainer)
- ES-LATAM+ES "posts editables Canva para esteticistas": 95 (busca ampla); Mind Digital Studio (USD, "Tu marca de coach"), Pack Insta de Impacto (BRL = brasileiro em espanhol, "Plantillas Black Friday"). Mercado tomado por packs genéricos em USD/BRL.
- IT "post pronti Canva estetiste": 16; sem pack de posts para esteticista. Achados laterais relevantes: **Kit Studio Blindato - APP** (1294553453740890, USD; o concorrente BR do dentista/psicólogo na Itália agora anuncia "APP", ~8 d); **Paulina Vera** "Kit Immobiliare Pro" (USD, ~1 d = BR levando kit de corretor para a Itália); Marjposa Phytocosmesi (EUR, protocolos para centros de emagrecimento).

### B12. Macros de sublimação (123) e eletricista residencial (108)
- "plantillas sublimación CorelDRAW" (LATAM+ES): 18. **Smartsubli** (BRL = brasileiro vendendo em espanhol) "Diseño en todos los moldes con 1 clic", ~23 dias. TESTE (o próprio BR exportando).
- "instalaciones eléctricas residenciales paso a paso PDF": 10. **Faradayos** (USD) "Guía ilustrada de instalaciones eléctricas", ~56 dias; **Mentes Ganadoras - Packs Digitales** (ARS) "Mega Pack Electricidad", ~79 dias; Academia Online PRO (USD) ~5 d; CEDAP e ProAcademy (MXN, cursos). PROVADO (AR e espanhol neutro).

### Checagens finais (top do ranking)
- Psicólogo, AR/CL/PE/EC/UY "documentos clínicos psicólogo plantillas consentimiento informado": 0. "historia clínica psicología plantillas" (AR/CL/PE/EC/UY/ES): 3; **Psicoagenda** (ARS) ~22 dias (produto VERIFICAR: agenda/software?); Aprende y Emprende en Casa "Pack Psicología" (MXN) ~58 dias (México, já conhecido).
- "informe psicopedagógico plantilla" (LATAM+ES): 0.
- ABA, "hojas de registro ABA terapeutas" (LATAM+ES+US): só Conecta ABA (USD, ~5–7 d). Confirma: em espanhol só há 1 vendedor de kit ABA, com 1 semana.
- Estimulação cognitiva profissional: FR "animation EHPAD fiches activités": 1 = **The Resource Lab** (USD) "Votre semaine d'ateliers, déjà prête", ~10 dias (mesmo padrão de copy de "Palestra Mentale"/"Seduta Pronta" na Itália; provável mesmo operador BR, VERIFICAR). DE "Beschäftigung Senioren Demenz Material": 0. ES "talleres estimulación cognitiva residencias mayores listos": 0; LATAM "sesiones de estimulación cognitiva listas para terapeutas": 0. Palestra Mentale medida por página: 11 ativos, mais antigo ~15 dias, criativos novos há ~9 dias (escalando).
- Instalador CFTV: PL "kurs instalator monitoringu kamer": 0; DE "Videoüberwachung Kurs Errichter": 0.
- Grafomotricidade PL "karty pracy grafomotoryka": 9; vendedores nativos em PLN de longa data: **Pomoce dydaktyczne - Gugu Rabbit** ~807 dias, **ABC w dydaktyce** ~114 dias, Zakątek Pedagogicznych Inspiracji ~44 d, Przedszkolne EduStory (900 páginas PDF) ~3 d. PL = PROVADO e competitivo (nativo).
- Concursos ES "esquemas oposiciones PDF temario": 8; academias (Esfera, Junta de Andalucía, Prefortia, Pilar Fernández) + **Emma Schneider** (BRL = brasileira) "De 300 páginas a 42 esquemas", ~7 dias. TESTE ES (BR chegando).

### Idiomas não pesquisados (orçamento de buscas)
RO, CZ, SK, HU, GR, NL e TR não foram consultados com termos próprios; DE e PL só nos conceitos de topo. Aparições laterais: CZK em marcenaria (Woodworking DIY Ideas, Dřevo Chotyně). Os termos traduzidos estão na seção 1 para a próxima rodada.
