# Catálogo mestre de profissões e termos que vendem como kit/documento (BR) e checagem internacional (30/10/2026)

## 0. Método e limites (leia primeiro)

- **Base BR usada:** a maior que existe no disco. `escalalow-20-10.db` (13.604 anunciantes, 70.600 anúncios, 805 "ok" + 3.012 "provável") + `escalalow-ofertas-24-10.json` (1.946 ofertas já por campanha, com dias/ativos/preço) = 2.057 ofertas únicas. Removi as 213 de `escalalow-ofertas-validadas.json` (por nome e anunciante). Sobraram 1.705; **189** têm 45+ dias e 5+ anúncios, e mais **101** têm 30+ dias e 3+ anúncios. As duas listas estão no apêndice. O banco vivo da VPS (mais novo que 24/10) não foi lido: o acesso SSH foi barrado nesta sessão. Se quiser, rode o mesmo corte lá.
- **Dados BR (dias, ativos, preço) são do EscalaLow em 20-24/10.** Os dias podem ter subido 6 a 10 desde então.
- **SearchAPI está sem crédito** (`remaining_credits` 0, 8.903 usados de 10.000; ciclo vira em **08/11/2026**). Tentei 97 buscas BR "kit para <profissão>" e a API devolveu "usou todas as buscas do mês": **nenhum dado novo de BR por SearchAPI**. Não gastei nada além disso.
- **`ads_library_search` (conector Meta):** só funciona com 1 a 3 palavras (frase longa devolve 0), vem do mais novo para o mais velho e **não dá texto do anúncio nem dias totais**. Então na checagem internacional eu consigo dizer "existe vendedor ativo e com quantos anúncios no termo", mas **dias reais só quando o anúncio mais antigo da amostra aparece**. Onde não consegui, está escrito "dias não medidos".
- Checagem internacional feita: **17 consultas** (US, MX, ES, IT, DE). **Não** cobri PT-PT, FR, PL, RO, CO, AR, CL, PE, UK, AU por conector. Tudo que não foi medido está em "VERIFICAR" (seção 6).
- Preço de página de vendas internacional: **não abri nenhuma**. Só o que o anúncio mostra (ex.: US$19,99; 349 MXN).
- Harmonização/injetáveis ficaram fora, como pedido.

## 1. O que já está coberto (não é "novo")

Dentista, psicólogo, advogado, contador, corretor/imobiliário, síndico/condomínio, RH (parcial, ver 3.7), fisioterapeuta, nutricionista, personal/pilates, veterinário/pet (clínica), estética/beleza (cílios, unhas, tatuagem, PMU), HACCP/inspeção sanitária (Consultora), SST/NR-1/DVR, eletricista, perito, host de aluguel curto, igreja/pastor/catequese, educação infantil/sostegno/concursos docentes, ABA/TEA/TDAH, fono/logopedia, estimulação cognitiva idosos, receitas (diabéticos, Bimby, air fryer), mapas mentais de concursos, empreiteiro/obra, gastronomia LATAM, cerimonialista, fotógrafo (contrato), agro (software).

## 2. LISTA MESTRE: profissões/públicos e termos NOVOS (não estavam nas pesquisas anteriores)

Legenda de evidência BR: `dias / anúncios ativos / preço`. Fonte: EscalaLow 20-24/10. "Cobertura" = NOVO ou PARCIAL (já tocado numa pesquisa, mas não como esse termo).

| # | Profissão / público | Termo do produto (como o BR vende) | Evidência BR (anunciante: dias/ativos/preço) | Cobertura |
|---|---|---|---|---|
| 1 | Advogado, arquiteto, engenheiro, corretor, RH (todos) | **Skills + prompts de IA por profissão** ("Claude Jurídico PRO", "Arquiteto 10X", "50 Skills + 1000 Prompts") | Corretor.IA: 96d/21/R$47; Powerbots 50 Skills: 78d/8/R$47; Claude People PRO (Franciele): 73d/23/R$47,90; IA Builders: 73d/9; Claude Jurídico PRO: 36d/13/R$67; Claude Engenharia Elétrica PRO: 36d/29/R$67; Arquiteto 10X (Amanda IA): 45d/16/R$67; Biblioteca de Prompts para Advogados: 51d/4/R$47 | NOVO |
| 2 | Soldador, caldeireiro, mecânico industrial, instrumentista | "Atlas Visual", "Mapas Visuais", "Na Prática" | Mecânico Industrial na Prática (Henrique Franco): 89d/15/R$37; Atlas da Soldagem: 37d/6/R$10,90; Caldeiraria Industrial: 79d/4/R$10; Mapas de Mecânica Industrial: 35d/5/R$29,90; Biblioteca Visual da Instrumentação: 30d/14/R$9,90 | NOVO |
| 3 | Marmorista / marmoraria | "+1.000 Projetos para Marmoristas", "Maleta Digital do Marmorista" | Danilo Marmorista: 61d/8/R$17; Douglas Marmorista: 85d/3/R$17 | NOVO |
| 4 | Instalador de CFTV / segurança eletrônica | "+200 Mapas Visuais de Instalação de CFTV" | Paulo Borges: 47d/5/R$17,90 | NOVO |
| 5 | Logística, almoxarifado, caminhoneiro, operador de máquinas | "Atlas Visual da Logística"; "Manuais Técnicos para Caminhões"; "200 páginas sobre máquinas pesadas" | Mayara Ferreira: 33d/9/R$10,90; Truck Labs: 32d/8/R$37,90; Central das Máquinas: 36d/3/R$19,90 | NOVO |
| 6 | Hidráulica/encanador/engenheiro civil | "Pacote de Planilhas Hidrossanitárias" | Montante Educação: 210d/3/R$37 | NOVO |
| 7 | Marceneiro, serralheiro, quintal/ranchos | "Projetos Prontos", "Biblioteca dos Ranchos de Lazer", "Casinhas de Quintal", "Topo de Tábuas p/ Churrasco" | Planeta Marcenaria: 58d/7/R$14,90; Jonas: 67d/4/R$19,90; Seu Valdir: 41d/8/R$19,90; Drive de Projetos Prontos: 30d/8/R$39,90; +100 Casas Container (Alex Franco): 135d/8/R$37 | PARCIAL (ofícios) |
| 8 | Técnico/biomédico de análises clínicas | "+250 Materiais de Análises Clínicas" | Isabela Fontana: 40d/52/R$14,90 | NOVO |
| 9 | Enfermagem / técnico (mapas clínicos, anotação, radiologia) | "120 Mapas Clínicos Visuais"; "Guia de Anotação e Evolução"; "RADIOMAP"; "Carteirinhas ACS" | Fabiola ISB: 86d/9/R$26; enfermagem de sucesso: 55d/6/R$17; Fernanda Alves RADIOMAP: 52d/9/R$17,90; Agente do povo (ACS): 93d/4/R$19,90 | PARCIAL (mapas) |
| 10 | Massoterapeuta / quiropraxista / fisio manual | "Mapas Visuais de Dor Referida e Pontos-Gatilho"; "Drenagem Linfática Ilustrada" | Jose Roberto: 84d/7/R$37; Drenagem Ilustrada: 42d/6/R$10 | NOVO |
| 11 | Tricologista / cabeleireiro técnico | "Guia da Tricologia Clínica" | Rafaelly Smil: 92d/6/R$67 | NOVO |
| 12 | Pet groomer / tosador | "100 Modelos de Tosas Comerciais" | Guia do Animal: 30d/3/R$27 | NOVO |
| 13 | Treinador de jiu-jitsu / de futebol / personal de modalidade | "+250 Dinâmicas de Jiu-Jitsu"; "Biblioteca do Professor de Jiu-Jitsu"; "+50 Planilhas de Treinos para Jogadores de Futebol"; "Biblioteca do Treinador de Futebol" | Dinâmicas Jiu-Jitsu: 169d/5/R$10; Biblioteca JJ: 71d/8/R$19,90; FutPro: 38-51d/4-7/R$15,90-17; Prof. Ricardo: 44d/7/R$37; ed_fisicadozero: Fichas de Musculação 187d/4/R$27 | PARCIAL (personal) |
| 14 | Regente de coral / professor de música / musicoterapeuta | "Coral em Sintonia +120 atividades"; "280 Atividades Musicais"; "+150 Atividades de Musicoterapia" | Coral em sintonia: 67d/25/R$10; Ana Clara: 44d/3/R$19; M.T. Na Prática: 31d/4/R$27 | NOVO |
| 15 | Assistente social / CRAS / CAPS | "+200 Dinâmicas para o CRAS"; "+200 Dinâmicas Terapêuticas para CAPS" | Juliana Mendes: 53d/9/R$47; Bianca Ribeiro: 86d/3/R$47 | NOVO |
| 16 | Caligrafia (adulto, autoajuda) | "Método Caligrafia Antiga"; "Treino guiado para letra mais bonita"; "Do Rabisco à Caligrafia" | Fenaeducacao: 59d/54/R$37 e 64d/17/R$37; Uiara Oliveira: 64-82d/3-7/R$14,90; Salmografia: 87d/7/R$49,99 | NOVO |
| 17 | Dono de loja / lojista / crediário | "Gestão de crediário"; "Método Loja Cheia"; "Calculadora de Precificação de Carnes"; "Ideias de Exposições para Supermercados" | Meu Crediário: 749d/16; Método Loja Cheia: 174d/9/R$60; Método Carrinho: 41d/9/R$14,90; Janaina Silva: 31d/3/R$24,90 | NOVO |
| 18 | Excel para pequeno negócio / escritório | "Planilhas prontas para seu negócio"; "Planilhas Premium"; "Office Pack 2026"; "Super planilha online 2.0"; "Mapas Visuais de Fórmulas do Excel" | BeM Digital: 260d/5; Planilhas Premium: 160d/6/R$12,90; Aureon: 64d/7/R$37; OfficePack: 84d/3/R$27; Juliana Ribeiro: 49d/3/R$27 | PARCIAL (planilhas) |
| 19 | RH e DP | "Kit Completo Dashboards RH & DP 2026"; "Biblioteca de Dashboards" | Kit Profissional de RH: 178d/6/R$27; Jenifer Rinara: 134d/6/R$31 | PARCIAL (RH) |
| 20 | Confeiteira / doceira (cardápio e catálogo) | "Cardápio Editável de Confeitaria"; "Catálogo Editável de Doces Natalinos"; "100 cardápios prontos" | Doce Criative Cardápio: 337d/10/R$7,90 e 71-76d/8/R$7,90; Cozinha Prática: 156d/7/R$10 | PARCIAL (receitas) |
| 21 | Feltro / EVA / lembrancinhas | "+1900 Moldes de Feltro"; "Apostila de Feltro e EVA"; "Moldes de Natal em Feltro e EVA" | Universo Feltro: 148d/8/R$10; Feltro Online: 154d/6/R$17,90; Rosemeire: 82d/9 | NOVO |
| 22 | Modelista / costureira (molde PDF) | "Molde em PDF"; "Molde do Avental Japonês Viral" | Jéssica Modelista: 232d/5/R$8; Ponto Certo App: 93d/5/R$25; Aline Moldes e Costura: 46d/6 | NOVO |
| 23 | Bordadeira / riscos | "Riscos para Bordar"; "Kit Encantado" | Riscos para Bordar: 182d/8/R$67,90; Bordado perfeito: 58d/44/R$67,90 | NOVO |
| 24 | Crocheteira | "Mais de 200 receitas de bolsas de crochê"; "100 modelos de porta-copos"; "Kit Receitas Crochê Católico"; "Kit Amigurumi" | Artesanato da Daiane: 55d/6/R$37,90; Croche da Gi: 53d/9; Vida Católica: 122d/7/R$27; Amigurumi Natalino: 50d/7/R$27 | NOVO |
| 25 | Impressão 3D (STL) | "O Maior Pack de STL do Brasil" | Mestre 3D: 102d/8/R$14,90 | NOVO |
| 26 | Resina / chaveiros / velas | "Kit Chaveiros Personalizados em Resina"; "Velas Artesanais"; "Guia de Velas Comestíveis" | Enkanto Resina: 99d/5/R$37; Haromalita: 57-58d/6-9/R$11,90-27 | PARCIAL (velas) |
| 27 | Papelaria personalizada / sublimação / DTF / canecas | "Kit Bloco de Anotações"; "Kits Bottons"; "+25 mil Estampas DTF"; "+201 mil Artes para Canecas"; "Kit Festa na Mesa"; "Kit de Embalagens" | De Rocha: 60d/5/R$15; Flor de Cactos: 52d/5/R$30; Taketo: 54d/4/R$24,70; Lavynia: 31d/5/R$47; Pack sublimação: 66d/10/R$13,99; Haromalita: 57d/6/R$11,90; DTF Personalização: 60d/5 | NOVO |
| 28 | Adesivagem / envelopamento | "Adesivagem Residencial" | Adesivagem Profissional: 75d/7/R$37 | NOVO |
| 29 | Serigrafia / gráfica | "halftone manual" (software/arquivos) | Aguiarts: 96d/6/R$49,90 | NOVO |
| 30 | Encadernação | "Super Aula de Encadernação" | Pri Lima: 66d/47 | NOVO |
| 31 | Fotógrafo (nicho parto) e editor (presets) | "Do ZERO aos Primeiros Partos Pagos"; "Paleta do Editor" | Primeiro Minuto Lab: 57d/6/R$29,90; David Johan: 72d/22 | PARCIAL (fotógrafo) |
| 32 | Criador de conteúdo / social media | "900 ganchos virais"; "365 Roteiros Validados"; "Pack Edição Simplificada"; "Kit Social Media"; "Biblioteca de Cortes Virais" | Micha Menezes: 61d/22/R$27 e 116d/17/R$67; Edição Simplificada: 129d/5/R$24,90; Cida Valcanaia: 74d/6/R$37; TomazCreator: 47d/4/R$19 | NOVO |
| 33 | Música/produtor | "Packs musicais exclusivos"; "Music Creator Pro" | Pack de Músicas: 478d/51/R$47; Music Creator: 44d/32/R$37 | NOVO |
| 34 | Gestor de condomínio/ imobiliária (aluguel) | "AlugaMais" (software) | AlugaMais: 459d/13 | já coberto |
| 35 | Técnico de segurança do trabalho (TST) rotina | "Seu apoio na rotina do TST"; "Kit de Treinamentos SST" | Prático de Saber: 40d/26/R$10; Seg.Seguro SST: 201d/3/R$67 | já coberto (SST) |
| 36 | Brigadista / combate a incêndio | "Atlas Visual de Prevenção e Combate" | Luana Gomes: 73d/9/R$10,90 | NOVO |
| 37 | Cuidador/treinador de saúde 50+ | "+300 Exercícios para Neuropatia" | Luciana Lopes: 33d/19/R$47 | NOVO (saúde, cuidado) |
| 38 | Esoterismo (cartomante, umbanda, astrologia) | "36 Cartas do Baralho Cigano em Mapas Mentais"; "Biblioteca Astral"; "Códice" | Eloa: 70d/8/R$27,90; Biblioteca Astral: 57d/8/R$47 | NOVO |
| 39 | Genealogia / cidadania | "As Fontes da Sua Árvore Genealógica" | Descubra sua Herança: 58d/25/R$19,90 | NOVO (nicho BR-específico) |
| 40 | Terapeuta holístico / reiki | "Kit Terapeuta Reiki" | Portal Huna: 118d/5/R$17 | NOVO |
| 41 | Psicólogo (ferramentas) | "Kit Clínico DBT"; "Terapia de Casal"; "Ferramentas de Carl Jung"; "Testes Comportamentais"; "Laudos" | DBT: 109d/6/R$47; Terapia de Casal: 35d/36/R$27; Jung (Suzana): 43d/4/R$47; MenteLab: 32d/57/R$29,90; Liane Bastos laudos: 113d/22/R$30 | já coberto (psicólogo) |
| 42 | Fonoaudiólogo (app) | "App Clínico para Fonoaudiólogas" | Luisa Mattos: 46d/7/R$29,90 | já coberto |
| 43 | Fisio infantil / TO / psicomotricidade | "+150 Atividades de Fisioterapia Infantil"; "+150 Atividades de TO"; "Kit Psicomotor" | Fisio Na Prática: 46d/4/R$27; T.O. Na Prática: 82d/6/R$27; Dra. Camila: 43d/3/R$27 | já coberto |
| 44 | Enfermeiro/acadêmico (HOF fora) | "Guia de Reconstituição da Toxina" | excluído (HOF) | fora |
| 45 | Vigilância sanitária (POPs) | "Mais de 100 POPs" | Regulariza Visa: 148d/4/R$29,90 | já coberto (pasta sanitária) |
| 46 | Lash/Nail (catálogos) | "Catálogo Profissional de Nail Art"; "Catálogo Nail Premium"; "Kit Catálogo Lash"; "Catálogo Cabelo Premium" | Clara Nail: 75d/9; Eu sou a Nat: 37-43d/5-11/R$10-19,90; Produtos Digitais: 41d/7/R$67 | PARCIAL (catálogo, não documentos) |
| 47 | Advogado nichos (bancário, contratos) | "Kit de Documentos do Advogado Bancário"; "Contratos Feitos por Advogado"; "Termo para lash" | Luiz Guedes: 39d/15/R$47; Andrieli: 111d/6/R$67; Advocacia Marian: 319d/4/R$29,90 | já coberto |
| 48 | Contábil (MEI, classificação tributária) | "Mapa Fácil do MEI"; "Classificação Tributária 2026"; "301 Nulidades Tributárias" | Mapa MEI: 35d/25/R$27; VGL: 37d/13/R$47; Peccini: 70d/3/R$57 | já coberto |
| 49 | Orçamentos/contratos de obra | "Orçamentos e Contratos em 2 Minutos" | Orça Obra Pro: 57d/3/R$19,90 | já coberto (empreiteiro) |
| 50 | Elétrica | "ConduzCabos", "Clube do Eletricista" | ConduzCabos 130d/19; Clube do Eletricista 739d/13 | já coberto |
| 51 | Concursos/estudos (mapas, flashcards, simulados) | "50 Mapas Mentais de RLM"; "SEDUC em Mapas"; "Flashcards ENEM"; "Simulados SAEB"; "Mapas de Fisiologia" | RLM: 81d/6/R$9,90; Vibe Federal: 66d/5/R$67; Prof. Ana Caroline: 46d/7/R$10; Aurora: 70d/3/R$10; Ana Maria Souza: 52d/7/R$57 | já coberto (mapas) |
| 52 | Professores: caligrafia, leitura, ditado, matemática, história, AEE, massinha, bingo de sílabas | "Kit Ditado Sorteado" 33d/74/R$7,90; "Kit Textos Fatiados" 32d/31/R$24,95; "+970 Atividades de História" 63d/4/R$9,90; "120 Atividades de AEE" 48d/3; "+100 Pranchas de Massinhas" 46-51d/3-8/R$10; "Bingo de sílabas" 53d/24 | mix | já coberto (educação) |
| 53 | Ministério infantil / catequese / devocional | "Kit Completo Ministério Infantil"; "Devocional Infantil"; "Atividades Bíblicas Infantis"; "Turminha da Promessa"; "Manual da Bíblia"; "80 Mini Bíblias" | Regina: 51d/9; Academia Kids: 201d/8; Sementinhas: 189d/6/R$14,99; Turminha: 73d/9/R$10; Josué: 95d/9 | já coberto (igreja) |
| 54 | Calendários religiosos | "Calendário Judío 5787"; "Calendários de 2027" | Shalom Mamãe: 83d/10; Cantinho da Oração Kid: 46d/33 | PARCIAL |
| 55 | Doenças raras / neuropsicopedagogia (rastreio) | "combo para rastreio de dificuldades"; "Biblioteca Neuro Visual"; "Investiga Autismo" | Educacao mind: 280d/9/R$10; Sara Fialho: 104d/8/R$10; Investiga Autismo: 51d/9/R$49,90 | já coberto |

**Contagem:** 55 linhas; **38 NOVO ou PARCIAL** (os demais são reencontros do que já estava coberto). Se contar cada termo de produto separado dentro das linhas, são **cerca de 85 termos novos**.

## 3. Checagem internacional dos conceitos mais promissores

Todas as consultas: `ads_library_search`, só ativos, 30/10/2026. "Termo" = busca em 1 a 3 palavras. Contagem = `estimated_total_count`.

### 3.1 Prompts / skills de IA por profissão (linha 1)
- **US (EN):** "ChatGPT prompts for lawyers" = 389 anúncios no termo. Vendedores específicos de profissão: **LocalLead** ("5 ChatGPT Prompts Every Realtor"), **Coleman Consulting Co** ("AI for Realtors: Prompt Playbook"), Quick Launch Today (US$19,99, genérico), Reaz Dewan ("1.500+ prompts"), Journalname shop ("10.000 prompts"). **Nenhum vendedor de advogado/arquiteto/contador específico** na amostra. Dias não medidos (amostra é só dos anúncios novos).
- **MX:** "prompts abogados" = 46. **Automatiza jurídico**: "Claude para Abogados | Edición México", **349 MXN pago único**, 2 criativos novos (iniciaram 29-30/10). Inteligencia Artificial Aplicada (WhatsApp, MXN, 5+ criativos). Universo de Prompts (anunciante BR, BRL).
- **ES:** "Claude para abogados" = 142, quase tudo curso ("Academia Claude AI", "Escuela de Claude AI", 6 criativos com mesmo texto). Sem kit por profissão medido.
- **IT:** "prompt per commercialisti" = 5 (software: Scadero, Sibill; Giacomo Bruno, e-book/formação). Sem kit.
- **Leitura:** o BR vende "Claude + profissão + R$47-67". Fora, só MX tem um clone muito novo. **Lacuna por profissão e por lei local** (abogados ES/MX/AR/CO, commercialisti IT, Steuerberater DE). Risco: tendência de curta duração, sensível a regras de ética profissional.

### 3.2 Soldador / mecânica industrial (linha 2)
- **US:** "welding cheat sheet" = 44. **Quinn Morrissette Studio** (page_id 101975594666133): 5+ criativos, o mais antigo da amostra com **~30 dias** ("5 Welding Cheatsheets Every Beginner Needs", "30.000+ students learning to weld from home"). RowginsDiy (3 anúncios). Este é um curso com cheatsheets de isca; nenhum "atlas visual" vendido como documento.
- **Não medido:** ES/MX (soldadura), IT (saldatura), PL, DE.

### 3.3 Cuidado/grooming (linha 12)
- **US:** "grooming templates" = 8. **The Practical Founder** (SOPs de boarding/daycare, já registrado), **TheFixer Designs** ("Invoice templates built for your trade", novo), franquia e escola. **Nenhum vendedor de modelos de tosa/forms de grooming.** Lacuna aparente, mas o termo é muito estreito.

### 3.4 Moldes de costura PDF (linhas 21-22)
- **US:** "sewing patterns pdf" = 430, mercado grande: Leomts.dg ("500+ Ready-to-Use Sewing Patterns"), Motif Studio Patterns (GBP, "20 bag patterns"), Stitch Well, Grovelen Patterns, Sew Chic, Blissebook. **Saturado**, não é lacuna.
- **MX:** "moldes costura pdf" = 75: **Angela Moldes**, **Isabela Costurera ("Moldes que sí se venden")**, Domina tu arte, Tu Evolución Activa (anunciante também presente em IT). Já é o formato BR traduzido.
- **IT:** "cartamodelli PDF" = 15: **Sartoria a 4 Zampe** (moldes de roupa de pet, USD), **Il Mio Quaderno di Cucito**, Studio Facile, Tu Evolución Activa. Pouca concorrência nativa.
- **DE:** "Schnittmuster PDF" = 29: Lybstes (4 criativos, EUR), emborado, Schleiferlwerk.
- **Leitura:** nicho dentro do nicho (**roupa de pet, aventais, feltro/EVA**) tem espaço; o genérico não.

### 3.5 Excel/planilhas para negócio (linha 18)
- **MX/AR:** "planillas Excel negocio" = 10: **Potencialia GO "Pack Emprendedor"** (ARS), **BeautyPro "Ordená tu negocio de uñas"** (ARS), Mis Finanzas Organizadas ("Calcula tus precios", USD), Dolchere, Soluciones Digitales "Mega Pack Excel" (anunciante BR, BRL). **Vendedores nativos pequenos, por nicho (uñas)**.

### 3.6 CFTV (linha 4)
- **MX:** "instalación cámaras CCTV guía" = 1: **CCTV Visual** (BRL) = anunciante BR já testando LATAM. Sem concorrente nativo.

### 3.7 Caligrafia (linha 16)
- **US:** "calligraphy practice" = 218. Wild Plains Calligraphy ("Handwriting, built step by step"), Calligraphy Techniques Studio (guia grátis, 4+ criativos), The Tilted Brick. Mercado grande e comprovado; BR vende como "treino de letra".

### 3.8 STL / impressão 3D (linha 25)
- **US:** "STL files" = 938, **saturado** (STL Live, NexModulo, Cardfinity).

### 3.9 Termos que dão 0 resultado no conector
"trigger point charts" (US), "welding visual guide" (US, frase longa), "dog grooming templates forms pack" (US, frase longa). O conector não aceita frases longas; não equivale a "sem mercado".

## 4. TOP 10 BRECHAS (ordenadas; nota = prova BR + sinal fora + facilidade de reaproveitar nosso motor)

1. **Skills/prompts de IA por profissão, local por lei do país** (linha 1). BR tem 8 anunciantes com 36-96 dias, 4-29 anúncios, R$47-67. Fora só um clone MX de 1-2 dias (349 MXN). Vender "Claude para abogados" com plantilhas locais (ES, MX, AR, CO) ou "commercialisti" (IT). Prova de preço fora: 349 MXN. Nota 8,0. Risco: ciclo curto.
2. **Atlas/mapas visuais para ofícios industriais** (soldador, caldeireiro, instrumentista, CFTV, logística; linhas 2, 4, 5). BR tem 6-7 vendedores novos com R$9,90-37 e 30-89 dias. US tem Quinn com 30+ dias (curso). Ninguém vende "atlas visual" fora. Nota 7,5. Só é possível se os mapas forem desenhados por nós (ou gerados por imagem).
3. **Moldes PDF de nicho pequeno** (roupa pet, avental, feltro/EVA; linhas 21-22). IT tem só 2-3 vendedores pequenos; MX já copiado do BR. Nota 7,0. Genérico é saturado.
4. **Caligrafia adulto "treino guiado"** (linha 16). BR: 54 e 17 anúncios, 59-64 dias, R$37. US: 218 anúncios no termo, validado. Nota 7,0. Disputado, mas ticket tem espaço.
5. **Planilhas por micronegócio** (nail business, confeiteira, açougue, loja; linhas 17, 18, 20). LATAM tem nativos pequenos em ARS/USD; BR tem 160-749 dias. Nota 7,0. Ideal para empacotar com precificação.
6. **Treinador de futebol e de jiu-jitsu** (linha 13). BR: 169d (jiu-jitsu, R$10), 38-51d (FutPro). Fora: **não medi**; futebol de base em ES/IT/MX/AR é enorme. Nota 6,5 até medir.
7. **Marmorista** (linha 3). BR: 61-85d, R$17. Fora não medido; IT (Carrara/Verona) e ES (Macael) têm indústria. Nota 6,5 até medir.
8. **Regente de coral / musicoterapia** (linha 14). BR: 67d, 25 anúncios (Coral em Sintonia), R$10. Fora não medido; coros paroquiais IT/ES/PL. Nota 6,0.
9. **Assistente social / CRAS** (linha 15). BR: 53-86d, R$47 (ticket alto para o formato). Fora não medido ("trabajo social", "assistente sociale"). Nota 6,0.
10. **Análises clínicas / biomédico** (linha 8). BR: 52 anúncios em 40d, R$14,90. Fora não medido ("laboratorio clínico"). Nota 5,5.

## 5. Padrões de termos que repetem no BR (para orientar buscas futuras)

"Atlas Visual de", "Mapas Visuais de", "Biblioteca do/da", "Na Prática", "Maleta Digital do", "+N Projetos para", "Kit Completo de", "Catálogo Editável", "Cardápio Editável", "Pack de", "Moldes em PDF", "Planilha Premium". Formatos de preço: **R$7,90 a 17** (volume) e **R$27 a 67** (profissional). Quem dura mais de 150 dias costuma ser **planilha/cardápio/molde** (documento de uso diário), não "atlas".

## 6. O que continuou VERIFICAR

1. **Banco vivo da VPS** (mais novo que 24/10): rodar o mesmo corte lá; SSH foi barrado nesta sessão.
2. **SearchAPI sem crédito até 08/11** ("remaining_credits" 0): refazer as 97 buscas BR "kit para <profissão>" e medir dias reais por page_id.
3. **Dias reais por page_id fora do BR:** o conector devolve só os anúncios novos; usar `meta_busca.py` / `medir.py` após 08/11 para: Quinn Morrissette (US, soldadura), Automatiza jurídico (MX), LocalLead e Coleman (US), Lybstes (DE), Sartoria a 4 Zampe e Il Mio Quaderno di Cucito (IT), Potencialia GO e BeautyPro (AR).
4. **Idiomas não cobertos por conector:** PT-PT, FR, PL, RO, CO, CL, PE, UK, AU. Em especial: treinador de futebol (ES, IT, MX, AR), marmorista (IT, ES), coral (IT, PL), assistente social (ES, IT), análises clínicas (ES, PT), tricologia (US, UK, ES), CRAS/trabajo social.
5. **Páginas de vendas internacionais:** nenhuma foi aberta; **preço só visível** para Automatiza jurídico (349 MXN) e Quick Launch Today (US$19,99).
6. **Tamanho do mercado e gancho legal** por busca web com URL: **não feito** para os 30 conceitos (a busca web exige URL de fonte e o tempo foi usado na base). Para #1 verificar regra de ética/publicidade da advocacia por país; para #2 e #3 não há gancho legal (puro conhecimento); para #7 normas de segurança em marmoraria (NR/EU) e para #5 não há gancho.
7. **Conferir se os 10 acima não são o mesmo anunciante rodando várias páginas** (ex.: ed_fisicadozero, Haromalita, Educacao mind, Maria Receitas, Doce Criative aparecem várias vezes).
8. **Ofertas do EscalaLow marcadas "provável"** (não confirmadas por preço): Corretor.IA, Bill Advocacia, Clube do Eletricista, Nine One Imports etc. Preço "None" nas linhas de #1 que não têm R$ confirmado.

---
## Apêndice A. 189 ofertas BR (45+ dias, 5+ anúncios) fora das 213

nicho | oferta | anunciante | dias | ativos | preço
Artesanato, moldes e papelaria | Katiuscia Hoepers - criatividade pedagógica  | Katiuscia Hoepers - criativida | 414d | 5 | None
Artesanato, moldes e papelaria | Molde em PDF conjunto colete e short alfaiataria | Jéssica Modelista | 232d | 5 | 8.0
Artesanato, moldes e papelaria | Mais de 1000 vendas na última semana | Riscos para Bordar | 182d | 8 | 67.9
Artesanato, moldes e papelaria | 🔥 APOSTILA COMPLETA DE FELTRO E E.V.A (PAGAMENTO ÚNICO) | Feltro Online | 154d | 6 | 17.9
Artesanato, moldes e papelaria | 👉 +1900 Moldes de Feltro | Universo Feltro | 148d | 8 | 10.0
Artesanato, moldes e papelaria | Kit Receitas Crochê Católico 2026 | Vida Católica | 122d | 7 | 27.0
Artesanato, moldes e papelaria | O Maior Pack de STL do Brasil | Mestre 3D | 102d | 8 | 14.9
Artesanato, moldes e papelaria | Kit Chaveiros Personalizados em Resina | Enkanto Resina | 99d | 5 | 37.0
Artesanato, moldes e papelaria | Molde do Avental Japonês Viral em PDF ⭐⭐⭐⭐⭐(748) | Ponto Certo App | 93d | 5 | 25.0
Artesanato, moldes e papelaria | Calendario Judío 5787 | Shalom Mamãe | 83d | 10 | None
Artesanato, moldes e papelaria | 🎄✨ MOLDES DE NATAL EM FELTRO E EVA | Rosemeire Moldes | 82d | 9 | None
Artesanato, moldes e papelaria | 🔥 PACK SACOLINHAS | Ita Criativa | 71d | 5 | None
Artesanato, moldes e papelaria | Super Aula de Encadernação | Pri Lima Personalizados | 66d | 47 | None
Artesanato, moldes e papelaria | Kit Bloco de Anotações Dobrável | De Rocha Design | 60d | 5 | 15.0
Artesanato, moldes e papelaria | Kit Encantado | Bordado perfeito | 58d | 44 | 67.9
Artesanato, moldes e papelaria | +70 Moldes de Topo de Tábuas para Churrasco e Mesa Posta | Planeta Marcenaria | 58d | 7 | 14.9
Artesanato, moldes e papelaria | 🚨 ALERTA DE OPORTUNIDADE | Pistache Aroma & Decor | 55d | 7 | None
Artesanato, moldes e papelaria | Mais de 200 receitas de bolsas de crochê | Artesanato da Daiane | 55d | 6 | 37.9
Artesanato, moldes e papelaria | Mais de 100 modelos de porta-copos de bichinho em crochê 🐸🧶 | Croche da Gi | 53d | 9 | None
Artesanato, moldes e papelaria | Kit Amigurumi | Amigurumi Natalino  | 50d | 7 | 27.0
Artesanato, moldes e papelaria | ✨ Transforme juta, cordão e criatividade em peças lindas para sua casa | Aline Moldes e Costura Criativ | 46d | 6 | None
Artesanato, moldes e papelaria | 80 Mini Bíblias + Guia de Montagem | Vanessa Kelly Lima | 45d | 9 | None
Astrologia e esotérico | 36 Cartas do Baralho Cigano em Mapas Mentais | Eloa Ferreira | 70d | 8 | 27.9
Astrologia e esotérico | Biblioteca Astral | Biblioteca Astral Digital | 57d | 8 | 47.0
Cabelo e barbearia | Lembra quando a infância cabia numa folha de papel? | Rebeca Flores | 92d | 8 | None
Cabelo e barbearia | Guia da Tricologia Clínica | Rafaelly Smil | 92d | 6 | 67.0
Concursos e estudos | A prova custa US$ 300. | DlteC do Brasil | 126d | 10 | 17.0
Concursos e estudos | Preparadão do Enem 2026 - Quero Bolsa | Preparadão ENEM | 115d | 14 | None
Concursos e estudos | Cabral & Vicente Advogados | Cabral & Vicente Advogados | 105d | 6 | None
Concursos e estudos | PREP Concursos | Prof Felippe Loureiro | 92d | 47 | None
Concursos e estudos | 50 Mapas Mentais de RLM | RLM - Os Aprovados | 81d | 6 | 9.9
Concursos e estudos | Teve sua capacidade reduzida após um acidente? | Reche e Sá Sociedade de Advoga | 80d | 5 | None
Concursos e estudos | SEDUC CE em Mapas Mentais | Vibe Federal | 66d | 5 | 67.0
Concursos e estudos | Teoria, prática, charadas e 10 questões já organizadas para trabalhar | Ajuda com as letras | 52d | 8 | 8.99
Concursos e estudos | +100 Mapas Mentais de Fisiologia | Ana Maria Souza | 52d | 7 | 57.0
Concursos e estudos | Flashcards ENEM 2026 | 447 Cards Visuais por Matéria | Prof. Ana Caroline Campos - Re | 46d | 7 | 10.0
Design e redes sociais | Pack Eternizar | Rumo ao Nós | 153d | 8 | 27.0
Design e redes sociais | Pack de Edição Simplificada | Edição Simplificada | 129d | 5 | 24.9
Design e redes sociais | figurinhas artesãs 2 | Ateliê de Conteúdo | 127d | 6 | 10.0
Design e redes sociais | Templates da Atenção | Elias Maman - Atenção Digital | 123d | 6 | None
Design e redes sociais | Transforme Seus Stories com 72% de Desconto | Marcela Scavuzzi | 113d | 8 | 27.0
Design e redes sociais | Kit de Ferramentas Essenciais para Social Media: Organize seu Negócio  | Cida Valcanaia | 74d | 6 | 37.0
Design e redes sociais | IA Builders | Workflow profissional de desenvolvimento com IA | Py.codebr | 73d | 9 | None
Design e redes sociais | Paleta do Editor | David Johan fotografia | 72d | 22 | None
Design e redes sociais | 900 ganchos virais | Micha Menezes | 61d | 22 | 27.0
Design e redes sociais | DTF Personalização | DTF Personalização | 60d | 5 | None
Design e redes sociais | PACK DE CRIATIVOS | AFILIADAS | Anna Lídia l Marketing e Venda | 60d | 9 | 14.9
Design e redes sociais | Kit de Embalagens Que Faz Seu Produto Artesanal Parecer | Haromalita | 57d | 6 | 11.9
Design e redes sociais | Kits Bottons Digitais - Prontos pra Imprimir | Flor de Cactos Personalizados | 52d | 5 | 30.0
Design e redes sociais | catalogoautomatizado organico | Vitrine Mágica | 49d | 9 | 35.0
Design e redes sociais | Kit Caixas Envelope Express | Isa e Ju Ateliê Arquivos Digit | 45d | 5 | 37.9
Educação e professores | Kit Kids Escolar | Kit Kids Escolar | 486d | 18 | 8.9
Educação e professores | +80 ATIVIDADES PEDAGÓGICAS | Genious | 177d | 8 | None
Educação e professores | O CASO DO BOLINHO- SEQUÊNCIA DIDÁTICA – Prof. Tatiane Alves | Prof Tatiane- recursos Pedagóg | 158d | 7 | 7.9
Educação e professores | Atividades prontas para imprimir | Clube da Pedagogia | 112d | 7 | 39.9
Educação e professores | Conversa connosco | Ana Silva | 97d | 14 | None
Educação e professores | 📖 MOMENTO DA LEITURA | Prof º Jaqueline | 95d | 8 | None
Educação e professores | Kit Berçário Pronto | Tia Luciana | 92d | 6 | 39.0
Educação e professores | Salmos da Bílbia | Salmografia a Caligrafia dos S | 87d | 7 | 49.99
Educação e professores | Kit Interpretar Para Evoluir 2.0 | Camila Medeiros - Psicopedagog | 83d | 16 | 67.0
Educação e professores | Professora, e se a criança aprendesse a ler e marcar horas no relógio | Gênios no Futuro | 81d | 6 | None
Educação e professores | +360 Atividades de Matemática no Mundo dos Blocos | Aprendizado Divertido | 80d | 8 | 17.9
Educação e professores | 102 atividades prontas para imprimir | Método Mamãe | 78d | 6 | 19.9
Educação e professores | +1000 atividades lúdicas para sala de aula | Cantinho da Professora | 75d | 6 | 10.0
Educação e professores | 🎈5 Atividades para o Dia das Crianças 🎈 | Criativizando e Educando | 68d | 7 | None
Educação e professores | Roda a Roda Escolar | Guias e Manuais para ajuda | 68d | 6 | 37.9
Educação e professores | Coral em Sintonia • +120 Atividades Prontas para Regentes | Coral em sintonia | 67d | 25 | 10.0
Educação e professores | Yay! Forms | Casa da Eulalia | 67d | 12 | None
Educação e professores | Seus alunos ainda confundem os gêneros textuais e têm dificuldade para | Criatividade pedagógica | 66d | 5 | None
Educação e professores | +300 Dinâmicas de Arte Infantil para Professoras | 300 Dinâmicas de Arte | 65d | 6 | 65.9
Educação e professores | Do Rabisco a Caligrafia | Uiara Oliveira - Materiais Ped | 64d | 7 | 14.9
Educação e professores | Treino guiado para uma letra mais bonita | Fenaeducacao | 64d | 17 | 37.0
Educação e professores | Método Caligrafia Antiga | Fenaeducacao | 59d | 54 | 37.0
Educação e professores | Biblioteca do Funcional | Biblioteca del Funcional | 59d | 8 | 10.0
Educação e professores | Combo Neuro Kids | NeuroKids  Desenvolvimento Inf | 56d | 8 | 14.9
Educação e professores | O bingo que chegou pra acabar com a resistência às sílabas em sala de | Ana Silva | 53d | 24 | None
Educação e professores | +200 Dinâmicas para o CRAS | Juliana Mendes | 53d | 9 | 47.0
Educação e professores | +100 Pranchas de Massinhas para Imprimir | Mundo do Aprender | 51d | 8 | 10.0
Educação e professores | Combo Mimos - Dia dos Professores | Loja de Arquivos  | 45d | 6 | 19.9
Elétrica, eletrônica e indústria | ConduzCabos | ConduzCabos | 130d | 19 | None
Elétrica, eletrônica e indústria | Mecânico Industrial na Prática | Henrique Franco | 89d | 15 | 37.0
Elétrica, eletrônica e indústria | Imagina transformar 25 minutos em , ou mais | Рrоf Rоberto Sоuza | 80d | 5 | None
Enfermagem e medicina | BaroScan | BaroScan | 170d | 6 | None
Enfermagem e medicina | 120 Mapas Clínicos Visuais | Fabiola ISB | 86d | 9 | 26.0
Enfermagem e medicina | +100 Mapas Visuais de Dor Referida e Pontos-Gatilho | Jose roberto | 84d | 7 | 37.0
Enfermagem e medicina | Guia de Anotação e Evolução + Medicamentos na Prática | enfermagem de sucesso  | 55d | 6 | 17.0
Enfermagem e medicina | RADIOMAP 2026 | Fernanda Alves | 52d | 9 | 17.9
Engenharia e arquitetura | Comece sua Jornada - Clube do Eletricista | GRUPO INTELLI | Clube do Eletricista | 739d | 13 | None
Engenharia e arquitetura | +100 Projetos de Casas Container | Alex Franco | 135d | 8 | 37.0
Engenharia e arquitetura | ConstruCode | ConstruCode | 101d | 16 | None
Engenharia e arquitetura | 50 Skills + 1000 Prompts | Powerbots | 78d | 8 | 47.0
Engenharia e arquitetura | Arquiteto 10X | Amanda IA | 45d | 16 | 67.0
Entretenimento | Protocolo Glúteos de Ouro | Fitness GO - Melhores Ofertas | 79d | 15 | None
Fitness e educação física | Participe do Desafío Atleta Híbrido | Victor Pareto | 358d | 122 | None
Fitness e educação física | +250 Dinâmicas Interativas de Jiu-Jitsu | Dinâmicas Jiu-Jitsu | 169d | 5 | 10.0
Fitness e educação física | Combo: Bases da Educação Física | ed_fisicadozero | 163d | 6 | 67.0
Fitness e educação física | Glúteo Crescendo em 21 Dias | Elisa Candido | 128d | 7 | 39.9
Fitness e educação física | Biblioteca do Professor de Jiu-Jitsu | Biblioteca de jiujitsu | 71d | 8 | 19.9
Fitness e educação física | Sistema Fullbody e | ed_fisicadozero | 67d | 6 | 10.0
Fitness e educação física | Manto Sagrado Sports | Manto Sagrado Sports | 51d | 6 | None
Fono, TO e fisio | Super Kit - nataliafisio.com | Natália Oliveira - Fisioterape | 108d | 14 | 19.78
Fono, TO e fisio | +150 Atividades de Terapia Ocupacional para Desenvolvimento Motor e… | T.O. Na Pratica | 82d | 6 | 27.0
Fono, TO e fisio | App Clínico para Fonoaudiólogas | Luisa Mattos | 46d | 7 | 29.9
Fotografia e vídeo | Do ZERO aos Primeiros Partos Pagos | Primeiro Minuto Lab. | 57d | 6 | 29.9
Idiomas | 🔥 OS CALENDÁRIOS DE 2027 QUE ESTÃO CHAMANDO ATENÇÃO | Cantinho da Oração Kids | 46d | 33 | None
Imobiliário | AlugaMais | AlugaMais | 459d | 13 | None
Imobiliário | cadastro ebook ia para síndico t13 | Condohabil | 161d | 6 | None
Imobiliário | Corretor.IA | Corretor IA | 96d | 21 | 47.0
Imobiliário | 50 Modelos Editáveis para Corretores | Léa Fernandez | 51d | 16 | 17.0
Jurídico | Bill Advocacia | Bill Advocacia | 481d | 18 | None
Jurídico | Contratos Feitos por Advogado | Andrieli | 111d | 6 | 67.0
Jurídico | Medeiros Diniz Advocacia | Medeiros Diniz Advocacia | 99d | 5 | None
Jurídico | Demonstração · Guimoo CRM | Guimoo | 94d | 34 | None
Lash, nail e sobrancelha | Catálogo Profissional de Nail Art | Clara Nail Designer | 75d | 9 | None
Maternidade e bebês | Dê o primeiro passo hoje | Dr.Raphael Haber | 98d | 6 | None
Negócios, finanças e planilhas | Gestão de crediário avançado para vender mais | Meu Crediário | Meu Crediário | 749d | 16 | None
Negócios, finanças e planilhas | Planilhas prontas para seu negócio | BeM Digital | 260d | 5 | None
Negócios, finanças e planilhas | Link na Bio | WJR Consulting | 183d | 29 | None
Negócios, finanças e planilhas | Kit Completo Dashboards RH & DP 2026 | Kit Profissional de RH | 178d | 6 | 27.0
Negócios, finanças e planilhas | Método Loja Cheia | Método Loja Cheia | 174d | 9 | 60.0
Negócios, finanças e planilhas | Planilhas excel | Planilhas Premium | 160d | 6 | 12.9
Negócios, finanças e planilhas | Biblioteca de Dashboards | Jenifer Rinara  | 134d | 6 | 31.0
Negócios, finanças e planilhas | Astron Members 3 | Astron Members 3 | 128d | 6 | None
Negócios, finanças e planilhas | PMOVEL - Tecnologia para RH | Pmovel | 81d | 11 | None
Negócios, finanças e planilhas | O Claude People PRO reúne mais de 50 Skills, 1.000 prompts, modelos e | Franciele Soaress | 73d | 23 | 47.9
Negócios, finanças e planilhas | Super planilha online 2.0 | Aureon Sistemas | 64d | 7 | 37.0
Negócios, finanças e planilhas | +de 1.000 Projetos para Marmoristas | Danilo Marmorista | 61d | 8 | 17.0
Negócios, finanças e planilhas | +200 Mapas Visuais de Instalação de CFTV | Paulo Borges | 47d | 5 | 17.9
Nutrição | Planilha Nutricional | Nutri Organizado | 180d | 5 | 37.0
Nutrição | 100 cardápios prontos para aumentar seus pedidos | Cozinha Prática | 156d | 7 | 10.0
Nutrição | 🥗 Receba o PDF Primeiro no WhatsApp | Carolina Mendes nutri | 151d | 6 | None
Nutrição | Cardápio Editável de Confeitaria | Doce Criative Cardápios Editáv | 76d | 8 | 7.9
Nutrição | Cardápio Editável de Confeitaria - Cardápio Editável de Confeitaria | Doce Criative Cardápios Editáv | 71d | 8 | 7.9
Nutrição | Nutri Prime | Bianca Andrade | 51d | 5 | 67.0
Nutrição | Crie tabelas automáticas + modelos editáveis no Canva | Nutricionista Fernanda Lopes | 45d | 5 | 67.99
Outros | Nine One Imports | Nine One Imports | 843d | 35 | None
Outros | Imatize | Imatize | 673d | 19 | None
Outros | A Mulher Que Eu Matei Em Silencio 2 | Levezas em palavras | 172d | 8 | 19.9
Outros | 👉 — edição Premium | Mac Allister Oliveira | 133d | 7 | None
Outros | 365 Roteiros Validados | Micha Menezes | 116d | 17 | 67.0
Outros | Plataforma Rápida para Laudos Psicológicos | Liane Bastos | 113d | 22 | 30.0
Outros | Não perca mais tempo preparando halftone manualmente em programas comp | Aguiarts  | 96d | 6 | 49.9
Outros | Standard Treinamentos | Standard Treinamentos | 87d | 14 | None
Outros | Hazap | Hazap | 85d | 34 | None
Outros | Adesivagem Residencial | Adesivagem Profissional | 75d | 7 | 37.0
Outros | Revista MAD | Acervo Nostálgico | 75d | 5 | 27.0
Outros | Atlas Visual de Prevenção e Combate | Luana Gomes | 73d | 9 | 10.9
Outros | 60 Etapas Técnicas Ilustradas | Casa com Economia | 63d | 11 | 27.0
Outros | Kit de Ebooks | ebooks prontos | 60d | 12 | 37.0
Outros | Velas Artesanais | Haromalita | 58d | 9 | 27.0
Outros | Vagas Somente Hoje | Haromalita | 58d | 5 | 15.0
Outros | Mundo das Griffes | Mundo das Griffes | 52d | 10 | None
Outros | Códice de Confirmação de Exu | Tata N'Ganga Kavungo | 49d | 8 | 47.0
Projetos e marcenaria | Artesanato com Madeira | Marcenaria Criativa | 45d | 6 | 37.0
Psicologia e terapias | Kit Terapeuta Reiki | Portal Huna | 118d | 5 | 17.0
Psicologia e terapias | Kit Clínico DBT | Gabriela Fernandez | 109d | 6 | 47.0
Psicologia e terapias | 500 Sesiones Terapéuticas Listas | Manual clínico aplicable | Clara Queiroz | 89d | 12 | None
Psicologia e terapias | Manual do Psicólogo Moderno | Psico Jhordana Borges  | 87d | 9 | 14.9
Psicopedagogia, TEA e TDAH | Tenha um combo completo para rastreio de dificuldades de aprendizagem | Educacao mind | 280d | 9 | 10.0
Psicopedagogia, TEA e TDAH | Mais de 3000 Atividades para autistas | Rebeca Barreto | 185d | 6 | 9.9
Psicopedagogia, TEA e TDAH | Biblioteca Neuro Visual | Sara Fialho - Psicopedagoga | 104d | 8 | 10.0
Psicopedagogia, TEA e TDAH | Kit Neuro | Educacao mind | 102d | 8 | 34.9
Psicopedagogia, TEA e TDAH | Kit Interpretar para Evoluir | Camila Medeiros - Psicopedagog | 87d | 16 | 67.0
Psicopedagogia, TEA e TDAH | 250 Atividades TDAH | Maria Eduarda | 73d | 6 | 24.9
Psicopedagogia, TEA e TDAH | Investiga Autismo | Investiga Autismo | 51d | 9 | 49.9
Receitas e confeitaria | Catálogo Editável de Doces Natalinos | Doce Criative Cardápios Editáv | 337d | 10 | 7.9
Receitas e confeitaria | Aprenda fazer caseirinhos que vendem rápido, mesmo sem experiência 😍 | Laura Fagundes | 144d | 15 | None
Receitas e confeitaria | 200 Doces Zero Açúcar | Chef Isadora Leblanc | 139d | 5 | 10.0
Receitas e confeitaria | Receitas Que Nutrem | Receitas Que Nutrem | 106d | 18 | 37.0
Receitas e confeitaria | +200 Receitas Deliciosas na Air Fryer | Chef Luana  | 102d | 7 | 10.0
Receitas e confeitaria | Quem vеndе gеlаdinho gourmеt em 2026 conhеce um truquе… | Receitas Lucrativas  | 101d | 8 | None
Receitas e confeitaria | Esses dias percebi uma coisa curiosa | Maria Receitas | 91d | 5 | None
Receitas e confeitaria | Apostila Festival Bolos de Feira | Telma Cristina confeiteira | 88d | 8 | 49.9
Receitas e confeitaria | Simone Ribeiro Receitas | Simone Ribeiro Receitas | 85d | 8 | None
Receitas e confeitaria | 🕯️ Guia Completo de Velas Comestíveis Gourmet | Maria Receitas | 71d | 6 | None
Receitas e confeitaria | Kit Festa na Mesa | Pack sublimação | 66d | 10 | 13.99
Receitas e confeitaria | Receba todo material no Whatsapp 🟢 | Lidiane silva | 64d | 6 | None
Receitas e confeitaria | ⏰ PARE DE PERDER HORAS FAZENDO MASSA E SALGADOS DO ZERO A CADA PEDIDO | Maria Receitas | 48d | 9 | None
Religioso | Devocional Infantil | Academia Kids | 201d | 8 | None
Religioso | Atividades Bíblicas Infantis | Sementinhas de Cristo | 189d | 6 | 14.99
Religioso | Gabriela Nogueira | Gabriela Nogueira | 131d | 6 | None
Religioso | 📖 E se a criança pudesse aprender histórias e ensinamentos da Bíblia e | Mundo Bíblico Kids | 109d | 6 | None
Religioso | ✨ O Cartãozinho Abraço de Jesus é uma lembrancinha cristã emocionante | Projeto mulher | 101d | 8 | None
Religioso | Manual da Bíblia | Josué Martins | 95d | 9 | None
Religioso | Turminha da Promessa | Turminha da promessa | 73d | 9 | 10.0
Religioso | Kit Passa | Casinhas dos Sonhos | 58d | 12 | 29.9
Religioso | As Fontes da Sua Árvore Genealógica | Descubra sua Herança | 58d | 25 | 19.9
Religioso | 🎉💝 Kit Completo Ministério Infantil | Regina Pereira | 51d | 9 | None
Segurança do trabalho | Protocolo NR-1 2026 | Guilherme Porto | 104d | 13 | 47.0

## Apêndice B. 30+ dias e 3+ anúncios (excluídos Receitas/Religioso/Artesanato/Concursos)

Educação e professores | Kit Jornada da Leitura | Hora de Aprender Cristão . | 36d | 26 | 27.0
Educação e professores | Kit de Textos Fatiados | Universo do Aprendizado Infant | 32d | 31 | 24.95
Psicopedagogia, TEA e TDAH | +150 Programas de Intervenção ABA para Desenvolvimento Infantil | ABA na Prática | 33d | 10 | 27.0
Lash, nail e sobrancelha | Catálogo Nail Premium | Eu sou a Nat | 37d | 11 | 10.0
Enfermagem e medicina | +250 Materiais de Análises Clínicas | Isabela Fontana | 40d | 52 | 14.9
Harmonização e estética | Kit de automaquiagem | Guia da maqui | 106d | 3 | 47.0
Contábil e tributário | Mapa Fácil do MEI | Mapa Fácil do MEI | 35d | 25 | 27.0
Segurança do trabalho | Seu apoio na rotina do TST | Prático de Saber | 40d | 26 | 10.0
Veterinária e pets | Atlas Visual da Anatomia Veterinária | Mayara Ferreira | 32d | 18 | 10.9
Outros | +100 Testes Comportamentais Prontos para Usar | MenteLab | 32d | 57 | 29.9
Educação e professores | Kit Ditado Sorteado | Aula Turbinada | 33d | 74 | 7.9
Educação e professores | Kit Completo de Simulados SAEB | Aurora Fernandes | 70d | 3 | 10.0
Enfermagem e medicina | Explicar procedimento 10 minutos não fecha | Full Face Academy | 30d | 58 | 9.9
Design e redes sociais | Pack Insta Decoração Premium | Feed Criativo | 36d | 20 | 29.9
Design e redes sociais | Music Creator Pro™ | Music Creator Pro | 44d | 32 | 37.0
Harmonização e estética | Guia de Reconstituição da Toxina Botulínica | Enferya Resumos | 188d | 4 | 37.0
Enfermagem e medicina | Kit Completo para Emoções DBT | MindUp | 87d | 4 | 27.0
Lash, nail e sobrancelha | Termo para lash | Advocacia Mariane Salles | 319d | 4 | 29.9
Fitness e educação física | Fichas de Musculação | ed_fisicadozero | 187d | 4 | 27.0
Enfermagem e medicina | Mais de 100 POPs - PROCEDIMENTOS OPERACIONAIS PADRÃO editáveis | Regulariza Visa | 148d | 4 | 29.9
Psicologia e terapias | Liberte-se do Ciúme | Dr Wimer Bottura Junior Psiqui | 130d | 4 | 29.9
Outros | Macho de Valor | Macho de Valor | 781d | 3 | 39.9
Segurança do trabalho | Pacote Premium | Seg.Seguro SST | 160d | 3 | 67.0
Segurança do trabalho | Kit Completo de Treinamentos SST 2026 | Seg.Seguro SST | 201d | 3 | 67.0
Enfermagem e medicina | Nova Era Kids | Nova Era Kids | 148d | 3 | 28.84
Engenharia e arquitetura | Claude Engenharia Elétrica PRO | Profissional com IA | 36d | 29 | 67.0
Nutrição | 🚀 Em apenas 30 dias, o Clube CCAFE já pode transformar a sua prática c | Clube Ccafe | 73d | 3 | 34.99
Harmonização e estética | Kit Profissional de Documentação para HOF | Artes para HOF - Anunciante 01 | 36d | 15 | 67.0
Negócios, finanças e planilhas | Atlas Visual da Logística | Mayara Ferreira | 33d | 9 | 10.9
Design e redes sociais | Proposta irresistível | Carol Cantanhêde | 36d | 17 | 47.0
Outros | +300 Exercícios Para Quem Tem Neuropatia | Luciana Lopes | 33d | 19 | 47.0
Enfermagem e medicina | Kit Carteirinhas ACS Saúde Brasil 360 | Agente do povo | 93d | 4 | 19.9
Fitness e educação física | Pack Fit Mídias | Maromba Lascado | 98d | 3 | 9.9
Jurídico | Kit de Documentos do Advogado Bancário | Luiz Guedes | 39d | 15 | 47.0
Educação e professores | Matemática 4 Operações | Lição Kids | 34d | 7 | 10.0
Contábil e tributário | CLASSIFICAÇÃO TRIBUTARIA [2026] | VGL Treinamento Digital | 37d | 13 | 47.0
Elétrica, eletrônica e indústria | Caldeiraria Industrial na Prática | Henrique Franco | 79d | 4 | 10.0
Psicologia e terapias | Pack com +200 Dinâmicas Terapêuticas para CAPS | Bianca Ribeiro | 86d | 3 | 47.0
Outros | Sherlock Holmes | Casos e Enigmas | 76d | 4 | 10.0
Psicopedagogia, TEA e TDAH | Kit InterExpert | Camila Medeiros - Psicopedagog | 40d | 12 | 67.0
Negócios, finanças e planilhas | Maleta Digital do Marmorista | Douglas Marmorista | 85d | 3 | 17.0
Projetos e marcenaria | Biblioteca dos Ranchos de Lazer | Jonas Marcenaria e Serralheria | 67d | 4 | 19.9
Negócios, finanças e planilhas | Office Pack 2026 | OfficePack | 84d | 3 | 27.0
Psicologia e terapias | Guia Prático de Terapia de Casal para Psicólogos | Fabiana Alves | 35d | 36 | 27.0
Educação e professores | Kit “Entre nós” | Meus Recursos Pedagógicos | 66d | 3 | 8.0
Projetos e marcenaria | Casinhas de Quintal | Seu Valdir Marceneiro | 41d | 8 | 19.9
Nutrição | Pack Nutri da Clínica | Karol Souza | 31d | 8 | 37.0
Educação e professores | Kit +10.000 Atividades Pedagógicas Prontas para Imprimir | Clube das Atividades | 41d | 8 | 39.9
Lash, nail e sobrancelha | Kit Catálogo Lash | Produtos Digitais | 41d | 7 | 67.0
Fitness e educação física | Livro Cinesiologia da Musculação | ed_fisicadozero | 58d | 4 | 37.0
Design e redes sociais | +25 mil Estampas DTF em PNG, CDR e JPEG | Taketo | 54d | 4 | 24.7
Negócios, finanças e planilhas | Calculadora de Precificação de Carnes | Método Carrinho Cheio | 41d | 9 | 14.9
Nutrição | 58 receitas para facilitar sua rotina | Método Mamãe | 46d | 4 | 19.9
Elétrica, eletrônica e indústria | Atlas Visual da Soldagem | Mateus Ramirez | 37d | 6 | 10.9
Contábil e tributário | Guia 301 Nulidades Tributárias | Ângelo Peccini | 70d | 3 | 57.0
Fitness e educação física | Biblioteca do Treinador de Futebol | Prof.RicardoMenezes | 44d | 7 | 37.0
Lash, nail e sobrancelha | ✨ Durante 14 anos trabalhei como manicure | Ita Criativa | 38d | 7 | 11.99
Projetos e marcenaria | Drive de Projetos Prontos | Allan Arruda | 30d | 8 | 39.9
Cabelo e barbearia | Catálogo Cabelo Premium | Eu sou a Nat | 43d | 5 | 19.9
Outros | Plataforma de Manuais Técnicos para Caminhões | Truck Labs | 32d | 8 | 37.9
Automotivo e serviços | Segurança Visual 2026 | AprovaMais | 44d | 9 | 19.0
Jurídico | Biblioteca de Prompts para Advogados | Rafael Egg | 51d | 4 | 47.0
Outros | Kit Mais Completo de Drenagem Linfática Ilustrada | Drenagem Ilustrada | 42d | 6 | 10.0
Engenharia e arquitetura | Pacote de Planilhas Hidrossanitárias | Montante Educação | 210d | 3 | 37.0
Educação e professores | 300 Atividades Escolares | Educa Fácil | 48d | 3 | 19.9
Fono, TO e fisio | +150 Atividades de Fisioterapia Infantil para Desenvolvimento Motor | Fisio Na Pratica | 46d | 4 | 27.0
Automotivo e serviços | Orçamentos e Contratos em 2 Minutos | Orça Obra Pro | 57d | 3 | 19.9
Fitness e educação física | +50 Planilhas de Academia para Jogadores de Futebol | Método FutPro | 51d | 4 | 15.9
Entretenimento | Biblioteca de Cortes Virais | TomazCreator | 47d | 4 | 19.0
Educação e professores | 120 Atividades de AEE | Mundo Seletivo | 48d | 3 | 14.9
Educação e professores | +970 Atividades e Jogos de História | Leticia Costa | 63d | 4 | 9.9
Psicologia e terapias | Kit com +350 Ferramentas Terapêuticas de Carl Jung | Suzana Machado | 43d | 4 | 47.0
Educação e professores | 280 Atividades Musicais Prontas para Aplicar | Ana Clara | 44d | 3 | 19.0
Negócios, finanças e planilhas | Mapas Visuais de Fórmulas e Funções do Excel | Juliana Ribeiro | 49d | 3 | 27.0
Educação e professores | Kit “Entre nós” | Meus Recursos Pedagógicos - Je | 36d | 3 | 8.0
Engenharia e arquitetura | Projetos Econômicos | Engenheiro Victor Prado | 35d | 3 | 37.0
Educação e professores | Kit Psicomotor Infantil | Dra. Camila R. | 43d | 3 | 27.0
Fitness e educação física | +50 Planilhas de Treinos para Jogadores de Futebol | Método FutPro | 38d | 7 | 17.0
Elétrica, eletrônica e indústria | Biblioteca Visual da Instrumentação Industrial | Rodrigo Ribeiro | 30d | 14 | 9.9
Educação e professores | Materiais para ensino fundamental | EducaClass | 43d | 5 | 19.9
Nutrição | 300 Sobremesas Zero | Amanda Ballis Nutri | 31d | 4 | 10.0
Educação e professores | +150 Atividades de Musicoterapia Infantil para Estimulação e… | M.T Na Pratica | 31d | 4 | 27.0
Outros | 300 Modelos para o Outubro Rosa | Jana Sousa  | 32d | 3 | 19.9
Psicopedagogia, TEA e TDAH | 50 Atividades de TDAH para Adolescentes e Adultos | Exercitando o Cérebro | 31d | 3 | 34.9
Outros | +200 Ideias de Exposições para Supermercados | Janaina Silva | 31d | 3 | 24.9
Jurídico | CLAUDE JURÍDICO PRO | Claude IA Pro | 36d | 13 | 67.0
Outros | 🚜 200 páginas sobre máquinas pesadas | Central das Máquinas | 36d | 3 | 19.9
Projetos e marcenaria | 80 Projetos Práticos com Arduino | Educação Inteligente | 32d | 16 | 37.0
Outros | +201 Mil Artes para Canecas | Lavynia alexandra | 31d | 5 | 47.0
Odontologia | Pack Odonto Premio | Eu.lindaestrella1 | 33d | 3 | 67.9
Elétrica, eletrônica e indústria | +300 Mapas Visuais de Mecânica Industrial | Mecânica Visual PRO | 35d | 5 | 29.9
Engenharia e arquitetura | +300 Plantas de Casas | Projetos Casas | 43d | 5 | 17.9
Psicopedagogia, TEA e TDAH | 🧠 Protocolo Completo de Altas Habilidades | Educacao mind | 63d | 3 | 24.9
Design e redes sociais | pack minimalista 4.0 | Clube dos packs  | 33d | 3 | 67.0
Psicologia e terapias | Kit Terapêutico Completo | MindUp | 220d | 4 | 27.0
Engenharia e arquitetura | Transforme Sua Carreira com Projetos Ambientais | Consultores Ambientais do Bras | 49d | 3 | 67.0
Outros | 100 MODELOS DE TOSAS COMERCIAIS PRONTOS PARA CONSULTA (cópia) | Guia do Animal | 30d | 3 | 27.0
Educação e professores | NeuroKids — +200 Atividades para o Desenvolvimento Infantil | NeuroKids  Desenvolvimento Inf | 80d | 4 | 14.9
Educação e professores | +100 Pranchas de Massinhas para Imprimir | Kit Digital | Isabela Mendonça | 46d | 3 | 10.0
Educação e professores | Kit “Entre nós” – Meus Recursos Pedagógicos | Meus Recursos Pedagógicos - Je | 32d | 3 | 8.0
Educação e professores | Do Rabisco a Caligrafia | Uiara Oliveira - Materiais Ped | 82d | 3 | 14.9
