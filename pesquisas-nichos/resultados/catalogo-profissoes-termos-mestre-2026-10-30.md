# Lista mestra de profissões e termos que vendem low ticket (30/10/2026)

> Status: EM ANDAMENTO (gravado aos poucos).

## Avisos de método
- A versão anterior (v1 de 29/10) e os arquivos do Desktop NÃO estavam acessíveis neste ambiente (container na nuvem). Não há comparação linha a linha com a v1.
- O banco `escalalow-20-10.db` (13.604 anunciantes, 70.600 anúncios) NÃO estava acessível. Base usada: `dados/escalalow-ofertas-24-10.json` (1.946 ofertas de 24/10) + `dados/escalalow-ofertas-validadas.json` (213) + `notas/meta-varredura-low-ticket.md` (varreduras de 07–08/10).
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). Medição feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre anúncios ativos da página.

## 1. Mineração da base (1.946 ofertas)

**Como foi feito:** as 1.946 ofertas de 24/10 foram cruzadas com as 213 validadas (251 linhas batem por nome/URL). Cada oferta foi lida por nicho e agrupada em ~80 conceitos de "profissão/público × termo". Colunas: nº de ofertas na base, maior idade (dias) entre as que tinham anúncio ativo em 24/10, soma de anúncios ativos e quantas estão entre as 213.

**Leitura rápida da base:**
- Mediana de idade das ofertas = 27 dias; 917 de 1.946 têm 30+ dias.
- O grosso é de consumidor final (atividades infantis 297, artesanato/moldes 286, receitas 130, religioso 107). Profissões aparecem em ~25% das ofertas.
- Termos que mais aparecem nas ofertas de profissional: **kit**, **modelos prontos/editáveis**, **documentos**, **fichas**, **protocolos**, **planilha**, **maleta digital**, **biblioteca**, **mapas visuais/mentais**, **atlas visual**, **pack**, **apostila**, **projetos prontos**, **catálogo**, **laudos**, **termo**.
- Formato novo que se espalhou em out/2026: **"Mapas visuais / Atlas visual / Fichas visuais de [área técnica]"** (dor referida, soroterapia, máquinas pesadas, metrologia, CFTV, logística, galvanoplastia, criminalística...). Muitos vendedores, quase todos com menos de 60 dias. É formato de estudo, não de documento de trabalho.
- Outro formato novo: **"Claude/IA para [profissão]"** (pastores, SST, contábil, jurídico, engenharia elétrica/mecânica, agro). Começou em set–out/2026.

### 1.1 Profissões/públicos NOVOS achados na base (fora da lista já coberta)
Coberta = dentista, psicólogo, advogado, contador, fisio, estética, HACCP/Consultora, SST, educação.

| Conceito (profissão × termo) | Evidência na base (24/10) | Nas 213? |
|---|---|---|
| Corretor de imóveis: modelos editáveis, planilha de clientes/imóveis, kit captação | 8 ofertas; Corretor IA 96d/21 anúncios R$47; Léa Fernandez "50 Modelos Editáveis para Corretores" 51d/16 R$17; Central do Corretor planilha 23d/62 R$9,90 | não |
| Avaliador de imóveis: laudo + planilha MCDDM (NBR 14653) | Avalliemais 281d (laudo R$197), 221d (R$97), planilha 68d/20 | 1 |
| Síndico: kit de documentos | AIsind 58d; RPM Síndico "Kit Prático do Síndico" 23d/6 R$67; FacilitaRh "Kit Facilita Condomínio" 11d | não |
| Perito judicial / assistente técnico | Digital Online "Guia do Perito Blindado" 99d (R$67, 213); "Assistente Técnico Blindado" 51d; Juslegalpro "Kit do Perito Nomeado" 20d R$67 | 1 |
| RH/DP: dashboards, campanhas, "kit de adequação" | Kit Profissional de RH "Dashboards RH & DP 2026" 178d/6 R$27; FacilitaRh 6–11d/16 | não |
| Escala 5x2 / nova jornada (PRAZO) | ComportaMente "a partir de 16/12/2026 jornada de até 42h" 2d/7 R$27; Flávia Maria "Kit Fácil da Escala 5x2" 3d/19; Nexo "Mapa Fácil da Nova Jornada" 7d/11; Guilherme Porto "Protocolo Escala 5x2" 2d | não |
| Qualidade ISO 9001/IATF 16949 | Integra SGI "Auditoria ISO e IATF do plano ao PDF" 16d/10 R$37; Engenharia na Web "Kit Implantação da ISO" 10d; "Kit Completo de Documentos da Qualidade" 7d | não |
| Fonoaudiólogo: app/kit/avaliação | 7 ofertas, 197 anúncios; "App Kit Fonoaudióloga Pro" 156d; Luisa Mattos "App Clínico para Fonoaudiólogas" 46d R$29,90; FonoLu Kids 28d/141 | não |
| Terapeuta ocupacional | T.O. na Prática 82d R$27; protocolos TO infantil 47d | não |
| Psicomotricista: documentos | Tia Su "+60 documentos" 114d/20 R$15,90 (213) | 1 |
| Terapeuta ABA/AT: programas e documentos | Inovaba "documentos essenciais da terapia ABA" 148d R$47, programas 158–179d | 1 |
| Enfermagem: anotação/evolução, SAE | "Guia de Anotação e Evolução + Medicamentos" 55d R$17; mapas de curativo/soroterapia <20d | não |
| Farmácia: exposição de gôndola, guia de medicamentos | "+100 Exposições para Farmácias" 19d/10 R$24,90; Farmácia Prática 12d/11 | não |
| Agente comunitário de saúde (ACS/ACE) | Agente do Povo "Kit Carteirinhas ACS" 93d R$19,90; "Bolsa Família 360" 27d; Kit Saúde Brasil 360 103d | não |
| Podólogo | Caminho da Podologia "Biblioteca Podológica" 14d R$49,90; "60 Protocolos" 38d | não |
| Quiropraxista | "60 Protocolos Clínicos de Quiropraxia" 7d/9 R$17,90 | não |
| Massoterapeuta | "Kit Massoterapia Organizada 27 Fichas" 18d/9 R$10; Drenagem Ilustrada 42d | não |
| Doula | "Manual da Doula Profissional" 18d (sem anúncio ativo) | não |
| Médico (PS/residência) | "+300 prescrições de pronto-socorro" 18d/18 R$47; De Gineco pra Gineco 77d R$67 | não |
| Terapeutas holísticos (radiestesia, reiki, constelação, astrologia, ventosa) | Caixa do Terapeuta 164d/41 R$27 (213) + "Pacote Profissional de Astrologia" 9d/58; Portal Huna Reiki 118d R$17 | 1 |
| Equipe de CAPS | "+200 Dinâmicas Terapêuticas para CAPS" 86d R$47 | não |
| Assistente social / CRAS | "+200 Dinâmicas para o CRAS" 53d/9 R$47 | não |
| Musicoterapeuta / arteterapeuta | M.T. na Prática 31d R$27; Arteterapia infantil 6d | não |
| Profissional de educação física / personal | 47 ofertas; ed_fisicadozero "Fichas de Musculação" 187d R$27; packs Canva para personal | 5 |
| Professor de artes marciais | Dinâmicas Jiu-Jitsu 169d R$10; "Biblioteca do Professor de Jiu-Jitsu" 71d; Kit Troca de Faixa Judô/Taekwondo 12–18d | 2 |
| Treinador de futebol | "Biblioteca do Treinador de Futebol" 44d R$37; FutPro planilhas 51d | não |
| Lash/nail/sobrancelha: termos, catálogos | "Termo para lash" (Advocacia Mariane Salles) 319d R$29,90; Encanto Lash 194d; catálogos 25–75d | 4 |
| Cabeleireiro/tricologista/barbeiro | "Guia da Tricologia Clínica" 92d R$67; assistente financeiro barbearias 76d | 1 |
| Body piercer | "+120 Protocolos de cuidados pós-piercing" 33d R$47 (sem ativo) | não |
| Esteticista automotivo | "25 Fichas para Estética Automotiva" 11d R$12,90 | não |
| Fotógrafo | Alex Bernardo "Kit Fotógrafo Blindado" (contratos) 134d R$39; presets 134d/38 (213) | 1 |
| Designer de interiores | "12 Documentos para Designers de Interiores" 10d R$12,90 | não |
| Arquiteto | Arq Louise Maria "Kit de Revisão de Projetos" 9d/15 R$37; Arquiteto 10X 45d/16 | não |
| Engenheiro: laudos (elétrica, insalubridade, acessibilidade, mecânica) | Engenharia na Web "Laudos Elétrica" 15d R$49,90; "Kit Laudo de Acessibilidade" 11d R$49,99; "Laudos de Insalubridade" 5d R$47 | não |
| Engenheiro civil/agrimensor: planilhas | "Pacote de Planilhas Hidrossanitárias" 210d R$37; "Kit de Documentos do Georreferenciamento" 22d R$47 | não |
| Eletricista | "Quadros Elétricos" 184d R$67 (213); "Tabela Digital do Eletricista" 57d/42 (213); manual 90d (213) | 7 |
| Técnico de ar-condicionado | "Tabela de Orçamento 2026 para Técnico de Ar-Condicionado" 6d R$17,90 | não |
| Instalador CFTV/segurança eletrônica | Gilson "Maleta Digital do Instalador" 96d/26 R$17 (213) | 2 |
| Integrador solar | "Gerador de Proposta de Energia Solar" 9d/10 | não |
| Vidraceiro / serralheiro / marmorista | Maleta do Vidraceiro 113d (213); Pack Serralheiro 126d (213); **Maleta Digital do Marmorista** 85d R$17 e "+1.000 projetos para marmoristas" 61d (fora das 213) | 5 |
| Mecânico (auto/caminhão) | Oficina Lucrativa "AJUDA MECÂNICO" 24d/57; Bíblia do Mecânico 204d R$49,90; Truck Labs 32d; "Laudos Mecânica" 18d | não |
| Técnico industrial (caldeiraria, solda, CLP) | Henrique Franco 79–89d; CLP e Ladder 28d/16 | não |
| Pet: tosador, adestrador, pet shop, veterinário | "100 Modelos de Tosas Comerciais" 30d R$27; Combo Veterinária 19d R$67; Kit Pet Shop 6d | não |
| Agro: produtor, meliponicultor, piscicultor | Galinheiros 44d/17 (213); Jardim do Mel (abelhas sem ferrão) 9d, 6 produtos; tilápia 14d | 2 |
| Supermercado: exposição de produtos | Janaina Silva "+200 Ideias de Exposições" 31–33d R$24,90 | não |
| Food service: precificação por tipo de negócio | Minhas Finanças Organizadas: hamburgueria, pizzaria, açaiteria (16–38d, R$27); "Calculadora de Precificação de Carnes" 41d; "50 Fichas Técnicas de Sushi" 38d | não |
| Confeiteira: gestão/precificação | "Preço Certo Confeitaria" 54d R$29,90; "centro de comando da confeiteira" 7d | 2 |
| Merendeira | "Livro de receitas para a merendeira" 5d R$12 | não |
| Pastor / líder de célula / professor de EBD | "500 esboços de pregações para mulheres" 104d; "5.000 esboços" 92d; "Gerador de Sermões" 38d R$37,90; "Claude para Pastores" 28d/13 R$67; "Manual do Obreiro" 8d/24 | não |
| Catequista | "Central da Catequese 2027" 19d/12 R$47 | não |
| Cuidador de idosos / ILPI | Neuromente estimulação cognitiva 165d (213); "+160 Atividades para Idosos" 61d; fichas para idosos 21d | 1 |
| Secretária de consultório | Recepfy "Kit Consultório Organizado" 8d/11 R$67; MktBoost Kit Secretaria/Recepção 6–9d | não |
| Despachante / recurso de multa | "Kit +100 Modelos de Recurso de Multa e Suspensão de CNH" 13d R$29,90 | não |
| Produtor cultural | "40 Projetos Culturais Aprovados" 25d R$9,90 | não |
| Social media / designer freelancer | "Proposta + contrato + portfólio" 13d R$19,90; "Materiais que todo social media precisa" 27d | não |
| Músico / venda de shows | "Kit Profissional de Venda de Shows" 10d R$67 | não |
| MEI | "Mapa Fácil do MEI" 35d/25 R$27 | não |

**Vendedor multinicho a vigiar:** MktBoost (page 662289736960077) lançou em out/2026 "Kit" para oficina, secretaria, recepção, agenda cheia, captação de imóveis e pet shop (R$17,90–27,90). É um clonador testando profissões em série; os testes dele indicam o que vale olhar, mas nenhum tem 30 dias.

## 2. Varredura Meta BR (termo genérico × profissão)

Feita no conector Meta em 30/10, Brasil, só anúncios ATIVOS. Dias = 30/10 − menor início de veiculação entre os ativos da página (quando a página tem mais de 50 ativos, o valor é "pelo menos X", porque a ferramenta devolve os 50 mais novos). A busca do conector é ampla (não é frase exata), então muitos resultados vêm com ruído (vagas, cursos, SaaS); só listo o que é infoproduto.

| Termo buscado | Ativos no termo | Vendedores de infoproduto achados (page_id) | Dias reais / anúncios | Leitura |
|---|---|---|---|---|
| kit documentos corretor de imóveis | 18 | Rafael Sieiro "Kit Corretor Expert em Locação" (269320183432646); Vanguarda Docs "3 kits: gestão, locação, compra e venda" (1344384498755738); ImoTools (SaaS, isca "36 scripts") | Sieiro 33,5d; Vanguarda 4d; ImoTools 51d | **PROVADO fraco** (1 vendedor 30+d) |
| kit do síndico | 63 | GrandCondo (1240006802532311) Kit Prático R$47, Kit Completo R$87 (de R$197), Kit AVCB & Incêndio R$47, Combo R$69,90; RPM Síndico/Rafael Marques (1139281505945813); Kit Síndico (587913247749681) | GrandCondo ~1d com dezenas de anúncios; RPM 28,6d/3; Kit Síndico 1d/3 | **TESTE quente** (alguém despejou dezenas de criativos esta semana) |
| escala 5x2 | 1.547 (maioria vagas) | Guia 5x2 "Migre da 6x1 para a 5x2 sem multa" (1419728794553563); Duda Ramos "Mapa da Escala 5x2: Gestão para Farmácias e Varejo" (1972250792873166); Mente Gestora "Organize sua empresa para a jornada 5x2" (1380041191864550) | todos 0–3d | **PRAZO + TESTE em massa** |
| fonoaudiologia kit | 31 | Fonoaudiologia para Profissionais/Completa "FONO DOCS – Kit de documentos para Fonoaudiólogos" (101618731821509); Elegance IV "Kit de Fichas Clínicas R$59,90"; Bruna Barbosa "Kit Comunicação Pós-AVC" | FONO DOCS: anúncio criado há 155–170d, veiculação reiniciada 28/10 (2d); outros 0–7d | **TESTE** (doc existe desde mai/2026, não contínuo) |
| terapia ocupacional kit | 49 (faculdades) | T.O. Na Prática "APENAS R$10" (1113246765215470); Rebeca Andrade mesmo criativo (711664055361671) | 44,8d e 58,7d | **PROVADO** (atividades a R$10, não documentos) |
| modelos prontos enfermagem | 26 | **APS Na Prática 360 "100 SOAPs prontos / 72 SOAP Cards / Biblioteca Clínica" para UBS** (1118868354653621); A_casaderepousomodelo "+35 documentos essenciais – evite multa e interdição por R$97" (119742206551954); enfermagem de sucesso "132+ modelos por R$10" (117198581410663) | APS ≥31,6d e ~45 ativos (Black Friday rodando); casa de repouso 16,3d; enfermagem 4–12d (oferta na base com 55d) | APS **PROVADO**; ILPI **TESTE** |
| "POPs para farmácia" | 65 | Rogerio Antunes "POPs da sua farmácia prontos em minutos" (1350419811493002); Dr Wender Santos/Grupo T3 Farma "Visa Farma + Vigilância sem surpresa", "Precifica Farma" (993254317213368); Farmatécnica "RDC 1.000 Descomplicada" (100145262860308); Marco Aurélio Farmácia e Gestão | Rogerio 1,4d; T3 Farma página 46,4d/7; Farmatécnica 51,4d (outro produto) e RDC novo; Marco Aurélio 3d | **TESTE quente** (4 vendedores em 7 dias) |
| "personal trainer" planilhas | 6 | ed_fisicadozero (108169348943480); Alan Scherer Personal Trainer (315013239218856) | 72,4d; 143,8d | **PROVADO** |
| "médicos veterinários" kit / documentos veterinária | 4 / 88 | só cursos e SaaS (SimplesVet, Vetmoura, Lauday) | — | **BRECHA** (nenhum kit low ticket) |
| "modelos de atestado" | 54 | Consultório em Ordem "Atestado ou declaração? Tenha os dois" (1444091032114948); Papelaria Médica = gráfica física | 1,4d/4 | **TESTE** |
| contrato para fotógrafos | 67 | Fotografia é o Meu Negócio "Brutos não são obrigação sua" (1738059673077819) | 0–1d | **TESTE** (base: Kit Fotógrafo Blindado 134d) |
| "oficina mecânica" planilha | 20 | só SaaS (4MUD, vhsys, Mecânica OS, Mecaos) | — | **BRECHA** low ticket |
| "ficha de anamnese" salão | 27 | Lari Fonseca "Para cabeleireiros e salões" | 2,6d | TESTE fraco |
| "secretaria da igreja" | 163 | só SaaS de igreja (Mestre EBD, Fideon, Servus IA) | — | **BRECHA** para kit de documentos de igreja |
| "cuidador de idosos" kit | 26 | Enfermeira Lia Cibele "Kit Profissional da Cuidadora de Idosos" (615173701678215) | 7,8d | **TESTE** |
| avaliação de imóveis planilha laudo | 67 | JSM Planilhas (planilhas de engenharia, moeda USD, dezenas de anúncios) | 0–7d nos 15 vistos | sem leitura (Avalliemais na base: 281d) |

**Clonadores multinicho ativos esta semana (sinal do que está sendo testado):**
- **Camila R** (1384001198122660, cobra em USD): lançou de 28 a 30/10 "Modelos de Laudos Periciais", "Farmácia pronta pra vigilância", "Clínica aprovada de primeira", "POPs do consultório", "Fichas técnicas de confeitaria", "Exercícios de voz prontos".
- **MktBoost** (662289736960077): kits de oficina, secretaria, recepção, captação de imóveis, pet shop (R$17,90–27,90).
- **GrandCondo**: síndico em várias faixas de preço e kit AVCB.

**Gancho de PRAZO achado (Brasil):** EC 141/2026 (fim da escala 6x1), promulgada em 16/10/2026. Pelas notícias, a escala 5x2 e o teto de 42h/semana valem 60 dias depois, em **16/12/2026**, e as 40h vêm numa segunda etapa, em 2027 (as fontes divergem: dez/2027 ou 14 meses). O texto no DOU não foi conferido → VERIFICAR. Fontes: [DGABC](https://www.dgabc.com.br/Noticia/4353133/saiba-quando-comeca-a-valer-o-fim-da-escala-6x1), [Mercado&Consumo](https://mercadoeconsumo.com.br/15/10/2026/economia/fim-da-escala-6x1-quando-entra-em-vigor-nova-jornada/), [meutudo](https://meutudo.com.br/blog/noticias/2026/10/15/escala-6x1-acabou-senado-aprova-pec-em-votacao-entenda-como-vai-funcionar-e-quando-comeca/).

**Limite do método:** o WebFetch está bloqueado neste ambiente (planalto.gov.br e outros domínios dão ENOTFOUND). Por isso nenhuma página de vendas foi aberta. Preço, plataforma, bumps e garantia vêm só do título do anúncio ou da base do EscalaLow; o resto fica VERIFICAR.

## 3. LISTA MESTRA

Régua: **PROVADO** = vendedor com anúncio ativo há 30+ dias no país/moeda. **TESTE** = há sinal, mas nenhum vendedor com 30+ dias. **PRAZO** = o gancho é uma norma com data. **BRECHA** = ninguém vende.
- Fonte "base" = EscalaLow 24/10 (dias do EscalaLow / anúncios ativos naquele dia).
- Fonte "Meta" = medição de 30/10.
- Fonte "nota" = notas/meta-varredura-low-ticket.md (07–08/10).

### 3.1 Já cobertas pelo usuário (só para referência; não entram no top 30)
| Profissão | Termo que vende | Evidência BR | Status |
|---|---|---|---|
| Dentista | kit de documentos, RDC 1.002 | Artes para Odontologia 234d/32 (base); nota 216–218d | COBERTA |
| Psicólogo | kit de documentos, prontuário CRP, laudos | ElloCursos 16d/60, Liane Bastos laudos 113d/22 (base); nota 290d/43 | COBERTA |
| Advogado | peças, contratos, playbook | Renato Porto 60d/20, Luiz Guedes bancário 39d/15 (base) | COBERTA |
| Contador | reforma tributária IBS/CBS, calculadoras | Educa Visual "Mapa Fácil da Reforma" 87d/84; VGL 37d (base) | COBERTA |
| Fisioterapeuta | planilhas de exercícios, documentos | Luisa Souza 15d/61; Fisio na Prática 46d (base) | COBERTA |
| Estética/HOF | documentos, anamnese (HOF fora do escopo) | Mai Milena 214d; nota HOF até 545d | COBERTA |
| Consultora de alimentos (HACCP) | documentos para consultoria, pasta sanitária | Domine a Nutrição 50d/51 (base) | COBERTA |
| SST | NR-1, DDS, treinamentos | Seg.Seguro 201d; Guilherme Porto NR-1 104d/13 (base) | COBERTA |
| Educação/AEE | atividades, PEI/PDI, AEE | centenas de ofertas; nota AEE 210 anúncios | COBERTA |

### 3.2 NOVAS (profissão × termo × evidência)
| # | Profissão / público | Termo que vende | Evidência BR | Status BR |
|---|---|---|---|---|
| 1 | Farmacêutico / dono de farmácia | "POPs da farmácia", "farmácia pronta pra vigilância", "RDC 1.000 descomplicada", precificação | Meta: 4 vendedores novos em 7 dias (Rogerio Antunes 1,4d; Camila R; Farmatécnica; Marco Aurélio); Grupo T3 Farma página 46d/7; base "+100 Exposições para Farmácias" 19d/10 | TESTE quente |
| 2 | Médico e enfermeiro da Atenção Primária (UBS/ESF) | "100 SOAPs prontos", "SOAP cards", "biblioteca clínica" | Meta: APS na Prática 360 ≥31,6d, ~45 anúncios, Black Friday | **PROVADO** |
| 3 | Síndico / administradora | "Kit do Síndico", "Kit AVCB & Incêndio" (R$47–87) | Meta: GrandCondo dezenas de anúncios em 1–2d; RPM Síndico 28,6d; base AIsind 58d | TESTE quente |
| 4 | RH/DP, contador e pequeno empregador | "escala 5x2", "migre da 6x1 sem multa", "mapa da escala 5x2 para farmácias e varejo" | Meta: 1.547 anúncios no termo; vários infoprodutos 0–3d; base "Kit Fácil da Escala 5x2" 3d/19 | **PRAZO 16/12/2026** + TESTE |
| 5 | Fonoaudiólogo | "kit de documentos para fonoaudiólogos", "fichas clínicas", "app kit fono", "exercícios de voz" | Meta: FONO DOCS (criado mai/2026, reativado 28/10); Elegance IV R$59,90 7d; base App Kit Fono 156d, App Clínico 46d | TESTE |
| 6 | Terapeuta ABA / acompanhante terapêutico | "documentos essenciais da terapia ABA", "programas de intervenção" | base: Inovaba 148–179d (R$47–69); ABA na Prática 33d | **PROVADO** |
| 7 | Psicomotricista | "+60 documentos de psicomotricidade" | base: Tia Su 114d/20 R$15,90 (está nas 213); nota 97d/10 e 28 anúncios | **PROVADO** |
| 8 | Terapeuta ocupacional | "atividades de TO por R$10", "protocolos clínicos TO infantil" | Meta: T.O. na Prática 44,8d; Rebeca Andrade 58,7d | **PROVADO** (atividades; documentos não testados) |
| 9 | ILPI / casa de repouso | "+35 documentos essenciais – evite multa e interdição" R$97 | Meta: A_casaderepousomodelo 16,3d | TESTE |
| 10 | Veterinário / clínica veterinária | kit de documentos (termos, prontuário, receituário) | Meta: só SaaS e cursos; base: "Combo Veterinária" multinicho 19d R$67 | **BRECHA** |
| 11 | Corretor de imóveis | "Kit Corretor Expert em Locação", "50 modelos editáveis", planilha de clientes e imóveis | Meta: Rafael Sieiro 33,5d; Vanguarda Docs 4d; base Corretor IA 96d/21, Léa Fernandez 51d/16, Central do Corretor 23d/62 | **PROVADO** (fraco) |
| 12 | Avaliador de imóveis / perito avaliador | laudo de avaliação + planilha MCDDM (NBR 14653) | base: Avalliemais 281d (R$197), 221d (R$97), planilha 68d/20 | **PROVADO** (ticket R$97–197) |
| 13 | Perito judicial / assistente técnico | "Guia do Perito Blindado", "Kit do Perito Nomeado", "modelos de laudos periciais" | base: Digital Online 99d/8 R$67 (213); Juslegalpro 20d R$67; Meta: Camila R testando laudos periciais | **PROVADO** |
| 14 | Médico de consultório | "atestado e declaração", "POPs do consultório", "clínica aprovada de primeira" | Meta: Consultório em Ordem 1,4d; Camila R 1–2d; base "+300 prescrições de PS" 18d/18 | TESTE |
| 15 | Enfermeiro / técnico de enfermagem | "132+ modelos de evolução por R$10", "guia de anotação e evolução" | Meta: enfermagem de sucesso 4–12d; base 55d | TESTE recorrente |
| 16 | Cuidador de idosos | "Kit Profissional da Cuidadora de Idosos", atividades para idosos | Meta: Enfermeira Lia Cibele 7,8d; base "+160 atividades para idosos" 61d | TESTE |
| 17 | Lash / nail / sobrancelha | "Termo para lash" (termo de consentimento), catálogos, apostilas | base: Advocacia Mariane Salles "Termo para lash" 319d R$29,90; Encanto Lash 194d | **PROVADO** |
| 18 | Profissional de educação física / personal | fichas de musculação, avaliação física, packs | Meta: ed_fisicadozero 72d; Alan Scherer 144d; base 187d; nota "avaliação física 68 anúncios" | **PROVADO** |
| 19 | Professor de jiu-jitsu/judô/taekwondo | dinâmicas, drills, planos de aula, "kit troca de faixa" | base: Dinâmicas Jiu-Jitsu 169d; Wrestling p/ Jiu-Jitsu 95d/32; Biblioteca do Professor 71d | **PROVADO** |
| 20 | Fotógrafo | "Kit Fotógrafo Blindado" (contratos), cláusula "brutos", presets | base: Alex Bernardo 134d R$39; Meta: Fotografia é o Meu Negócio 0–1d | **PROVADO** |
| 21 | Arquiteto / designer de interiores | revisão de projetos, controle de horas, "12 documentos para designers de interiores" | nota 08/10: "Arquiteto docs 430d"; base Arq Louise Maria 9d/15, designer de interiores 10d | PROVADO pela nota (VERIFICAR hoje) |
| 22 | Engenheiro (elétrico, civil, segurança) | modelos de laudos (elétrico, insalubridade, acessibilidade, mecânica), planilhas hidrossanitárias | base: Engenharia na Web 15–18d; LJ Soluções 5d; Montante 210d; Meta: JSM Planilhas dezenas de anúncios | TESTE (laudos) / PROVADO (planilhas) |
| 23 | Eletricista | tabela digital de preços, manual, quadros elétricos | base: 184d/13 (R$67), 57d/42, 90d (todos nas 213) | **PROVADO** |
| 24 | Instalador CFTV / técnico de ar-condicionado / integrador solar | "maleta digital do instalador", tabela de orçamento, gerador de proposta solar | base: Gilson 96d/26 (213); ar-condicionado 6d; solar 9–18d | PROVADO (CFTV) / TESTE |
| 25 | Vidraceiro, serralheiro, **marmorista** | "maleta digital", "+1.000 projetos para marmoristas" | base: Marmorista 85d R$17 e 61d (fora das 213); vidraceiro 113d, serralheiro 126d (213) | **PROVADO** |
| 26 | Mecânico / oficina | "ajuda mecânico", laudos de mecânica, manuais de caminhão | base: Oficina Lucrativa 24d/57; Bíblia do Mecânico 204d; Meta: só SaaS | TESTE / **BRECHA** de kit |
| 27 | Pastor / líder de célula / secretaria de igreja | esboços de pregação, gerador de sermões, "Claude para pastores"; documentos de igreja | base: 92–104d (esboços), 38d (sermões), 28d/13 (IA); Meta: secretaria de igreja só SaaS | **PROVADO** (pregação) / **BRECHA** (documentos) |
| 28 | Assistente social / CRAS | "+200 dinâmicas para o CRAS" | base: Juliana Mendes 53d/9 R$47 | **PROVADO** (1 vendedor) |
| 29 | Agente comunitário de saúde (ACS/ACE) | carteirinhas, "Bolsa Família 360", "Saúde Brasil 360" | base: Agente do Povo 93d/4 R$19,90 | **PROVADO** (fraco) |
| 30 | Food service (hamburgueria, pizzaria, açaí, açougue, sushi, confeitaria) | planilha de precificação por tipo de negócio, fichas técnicas | base: Minhas Finanças Organizadas 16–38d; Preço Certo Confeitaria 54d; Camila R testando fichas de confeitaria | **PROVADO** |
| 31 | Terapeuta holístico | kit radiestesia, reiki, constelação, astrologia profissional, ventosaterapia | base: Caixa do Terapeuta 164d/41 (213) + 58 anúncios em astrologia; Portal Huna 118d | **PROVADO** |
| 32 | Qualidade ISO 9001 / IATF | auditoria "do plano ao PDF", kit de implantação | base: Integra SGI 16d/10; Engenharia na Web 10d | TESTE |
| 33 | Podólogo / quiropraxista / massoterapeuta | protocolos, fichas, biblioteca | base: 7–38d | TESTE |
| 34 | Tosador / adestrador / pet shop | "100 modelos de tosas", cartilhas de adestramento, kit pet shop | base: 30d (1 vendedor), 2–6d | TESTE |
| 35 | Despachante / motorista | "+100 modelos de recurso de multa e CNH" | base: 13d | TESTE |
| 36 | Secretária de consultório | "Kit Consultório Organizado", kit recepção | base: Recepfy 8d/11 R$67; MktBoost 6–9d | TESTE |
| 37 | Produtor cultural | "40 projetos culturais aprovados" | base: 25d R$9,90 | TESTE |
| 38 | Body piercer / esteticista automotivo / doula | protocolos pós-piercing, fichas, manual | base: 11–33d sem anúncio ativo | sinal fraco |

## 4. Checagem lá fora (30 conceitos novos)

Feita no conector Meta (anúncios ativos, 30/10), com o termo traduzido e vários países numa mesma consulta. O conector devolve só os anúncios mais novos e mede só ativos. "Não checado" = faltou orçamento de chamadas: o WebSearch esgotou a cota do turno (200 buscas, compartilhada entre os agentes) e o WebFetch está bloqueado. Esses ficam VERIFICAR.

| # | Conceito | Resultado lá fora (termo usado → achado) | Leitura |
|---|---|---|---|
| 1 | Farmácia: POPs e vigilância | **MX** "PNO farmacia COFEPRIS" → **Recursos Legales PRO / Salud Mx** (page 880855681786807): PNOs Farmacia Lite $249, Estándar $699, PRO $999 MXN no mesmo catálogo de kits de consultório médico, dentista, **psicologia** ($499) e spa ($699); página com ativo de **98,8d**, 5 anúncios. ES-LATAM "plantillas para farmacias" → só lojas e FarmaAyuda (MX, consultoria) 15,5d | **PROVADO no MX** (vendedor multikit); BRECHA nos outros LATAM checados |
| 2 | APS: SOAPs prontos | EN "SOAP notes templates" (US/GB/AU/CA) → 52 anúncios, quase todos de escriba com IA (Commure, Phorest); SigmaSmart.en "Ready-to-Use Templates for PTs" 2,9d. ES-LATAM "notas SOAP plantillas" → 0 | EN tomado por SaaS; ES BRECHA sem demanda visível |
| 3 | Síndico | ES-LATAM "administración de condominios" → 184, só administradoras e SaaS (CostaNexa, CAZU MX); "kit administrador de condominios" → 0. **IT** "amministratori di condominio" → 172, só B2B (empreiteiras, seguros, associação Anapi). **PT** "administração de condomínios" → 13, só SaaS (Condoroo, CondoOps) e curso (ESAI) | **BRECHA** em ES-LATAM, IT e PT |
| 4 | Jornada 5x2 / redução de jornada | **MX** "jornada 40 horas" → 142: Capacita Plus "De 48 a 46 horas en 2027", Humand "Enero 2027: el registro de jornada ya es obligatorio", Canacintra "Prepara tu empresa para las 40 horas" (0–1d, cursos/SaaS, sem kit barato) | Confirma o item **Jornada México** da fila (PRAZO jan/2027) |
| 5 | Fonoaudiólogo | **PL** "materiały dla logopedy" → **Pani Andzia "Teczka logopedy" 226d**, Agnieszka Kaproń "T,D,L,N – kompletny system pracy" 193d, Instytut Sylwia Zasada "Kompletny pakiet dla początkującego logopedy" 115d (PLN). **IT** "materiale per logopedisti" → Arianna Allegretti 37d (1 vendedora nativa). ES-LATAM "kit fonoaudiología" → "Fonoaudiología Profesional" (USD) 2,6d e Laura Gomes (COP) 3,2d, ambos clones novos | **PROVADO PL** (forte, escolar), **PROVADO fraco IT**, TESTE LATAM |
| 6 | Terapeuta ABA | ES-LATAM "terapia ABA programas" → 5, só clínicas (Jokipoky MX, MABC) | **BRECHA** ES |
| 7 | Psicomotricista | ES-LATAM "psicomotricidad kit documentos" → 1 (Peru vendendo "kit de evaluación psicológica", 0d) | **BRECHA** ES |
| 8 | Terapeuta ocupacional | ES-LATAM "material terapia ocupacional" → **Mi Colega T.O** (conta CLP) "+1.500 actividades por edad", US$17,99, 2d, ~8 anúncios | TESTE (CL) |
| 9 | ILPI | PT "documentos lar de idosos" → 0; ES-LATAM "residencia adultos mayores formatos" → 0 | BRECHA (sem sinal de demanda) |
| 10 | Veterinário | ES-LATAM "formatos veterinaria kit" → 5, nenhum kit vet; EN "veterinary forms templates" → 0 | **BRECHA** (sem prova de demanda em lugar nenhum) |
| 11 | Corretor de imóveis | ES-LATAM "plantillas para agentes inmobiliarios" → 22, só SaaS/serviços (Lobbie CO, Inmoview ES) | BRECHA |
| 12 | Perito judicial | ES-LATAM "perito judicial modelos de informes" → 1 (curso AR) | BRECHA |
| 13 | Lash (termo de consentimento) | EN "lash tech consent forms templates" → 0; "consent forms templates" → 61, nenhum de lash | BRECHA no Meta EN (Etsy não checado: bloqueia) |
| 14 | Fotógrafo (contratos) | EN "photography contract template" → **The Legal Paige** (EUA, marca antiga de contratos; preço VERIFICAR) ~21d nos anúncios vistos; Studio Kit by D'Argent Weddings (AUD) "the contract our couples sign" 0,5d | EN servido por marca forte |
| 15 | Pastor / sermões | ES-LATAM "bosquejos de sermones" → 62: Luz y Palabra (USD) "Premium US$9,90", "Deja de buscar qué predicar" 0–1d; JSN 1d; "Dinámicas con Laura/Sara" | TESTE ativo (idade das páginas VERIFICAR) |
| 16 | Médico de consultório | MX: Recursos Legales PRO "Kit Consultorio Médico $499 MXN" (mesma página do item 1, 98,8d) | **PROVADO MX** |
| 17 | Psicopedagogo em inglês | EN: ormacionprofesional.psp (USD) "Complete Learning Assessment Toolkit +60 tests, 9 areas" 6,6d, ~16 anúncios | TESTE (operador latino indo para EN) |
| 18–30 | Avaliador de imóveis, enfermagem, cuidador, personal, artes marciais, arquiteto/designer, engenheiro (laudos), eletricista, marmorista, mecânico, assistente social, ACS, food service, terapeuta holístico | **não checados lá fora** | VERIFICAR |

**Sinais para a fila atual (fora do escopo, mas úteis):**
- **Concorrente no México para o Maletín del Psicólogo:** Recursos Legales PRO vende "Kit Legal Psicología" a $499 MXN, numa página com ativo de 98,8d. Abrir a página (bloqueado aqui) → VERIFICAR conteúdo, normas citadas e app.
- **Dentista EUA (Lic. Zulma Laguna, 778739435326228):** a página tem anúncio ativo desde 1/out (28,8d em 30/10), então **cruza 30 dias em 31/10**. Criativos novos em 23–24/10: "Dental Docs, Done for You", "Not a Blank Template", "Lawyer-Reviewed Dental Consents". Ela vira PROVADO na janela de re-checagem combinada (31/10–05/11).

## 5. Ranking 0–10

## 6. VERIFICAR
