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
(em andamento)

## 4. Checagem lá fora (30 conceitos novos)
(em andamento)

## 5. Ranking 0–10

## 6. VERIFICAR
