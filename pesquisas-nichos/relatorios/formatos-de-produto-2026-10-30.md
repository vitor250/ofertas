# Formatos de produto além de kit de documentos (30/10/2026)

## 0. Método e limites (ler primeiro)
- Fontes: conector Meta (`ads_library_search`, só anúncios ATIVOS; medição por page_id), navegador embutido (aba própria, já fechada) para ler texto/link de anúncios, WebFetch das páginas de venda, e os relatórios base (`funil-preco-bumps-concorrentes`, `marketplaces`, `produtos-adjacentes`, `arbitragem-kits-br-v2` em `3 - EU/pesquisas/`).
- SearchAPI sem crédito (até 08/11): não usado. Nada comprado, nenhum cadastro, nenhum formulário.
- Dias = 30/10/2026 menos o início do anúncio ATIVO mais antigo da página (piso; o conector só vê anúncios hoje ativos).
- **Limite da busca por palavra-chave:** frases longas devolvem 0. Os zeros abaixo valem só para as frases testadas, não provam ausência. Vários formatos (calendário, mapa mental, simulado, calculadora) deram 0 em ES/IT/DE/FR/PL: tratar como BRECHA PROVÁVEL, não certa.
- Régua: PROVADO = vendedor com anúncio ativo 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro (USD) não prova país.
- Não consegui medir: preço da Rafaella Lopes (anúncio "não está na Biblioteca" ao abrir; sem link), Cardápio Lucrativo/Prato CMV (página não aberta), IA Programas (preço, só WhatsApp). Marcados VERIFICAR.

## 1. Achado principal (novo, muda a recomendação de preço)
**"Sorrisi in Regola" (Itália, dentista) vende por MÓDULO TEMÁTICO a preços 2 a 6 vezes maiores que o clone de €19,99.** Loja Shopify própria (sorrisiinregola.com), li a página em 30/10:

| Produto (formato) | Preço (de) | Observação |
|---|---|---|
| Kit DVR + DUVRI (documento de avaliação de riscos Lgs 81/08: Word de 137 págs, 26 riscos, 43 módulos, 32 cartazes, Excel de prazos) | **€127** (€197) | anúncio "Dottore, mi mostra il DVR?"; assinado por engenheiro RSPP |
| Kit Sterilizzazione a Norma (guia + registros + pasta) | €49 (€95) | anúncio "Tracciabilità autoclave in 5 PDF" |
| Kit Consensi Informati Pro | €34 (€44) | consentimentos |
| Kit Consensi Medicina Estetica | €34 (€56) | |
| Studio Sotto Controllo + Cruscotto KPI + Codici UDI (planilha de prazos/inventário/KPI) | €43 (€62) | formato planilha |
| **Pazienti Dormienti, riattiva chi non torna** (lista + dados de recall + painel) | **€67** (€98) | formato "reativação de pacientes" |
| Kit Igienista in Regola (tabela de tarifas + agenda de recall + guia de quanto cobrar) | €74 (€127) | segunda profissão (higienista) |
| eBook "Studio Odontoiatrico a Norma di Legge" (130+ págs + 4 PDFs + checklist 16 págs) | €43 (€74) | |
| Webinar Sicurezza sul Lavoro | €60 | formato sessão ao vivo/gravada |
| Quando lo studio produce chairside | €53 | |
| App "Scadenze in Regola" | €0 (isca) | |

Anúncios: 13 ativos, mais antigo 13 dias (17/10/2026), EUR. Status: **TESTE** (ainda sem 30 dias), mas a PÁGINA tem 11 produtos e preços altos, sinal de que o público IT paga €34 a €127 por módulo. Ângulo de copy deles: multa/arresto citando art. 55 D.Lgs. 81/08 (norma não confirmada por mim, ver VERIFICAR).
Leitura: o clone de €19,99 (252 docs, app) e o Sorrisi (módulos €34 a €127) estão em extremos opostos; o nosso €27/€19 fica no meio com app. Os módulos do Sorrisi são exatamente os "temas legais" propostos como bump em `produtos-adjacentes` (DVR, GDPR, simulado, consensi) e agora há preço de mercado para eles.

## 2. Ranking FORMATO × PROFISSÃO × PAÍS (0 a 10)
Nota = evidência de demanda (40%), vazio de concorrente (30%), facilidade/risco para nós (30%). Esforço: P = reaproveita o que temos; M = 1-3 dias; G = exige humano/terceiro.

| # | Formato × profissão × país | Nota | Evidência (dias reais) | Preço visto | Status | Esforço |
|---|---|---|---|---|---|---|
| 1 | **Pacote DVR/sicurezza (Word guiado) × dentista × IT** | 8,5 | Sorrisi in Regola vende a €127 (13 d, 13 anúncios); âncora €150-300 do consultor (`produtos-adjacentes`) | €127 / €197 | TESTE no formato, âncora forte | M (precisa revisão de engenheiro RSPP real; não prometer conformidade) |
| 2 | **Reativação de pacientes inativos (lista + scripts + painel) × dentista × IT** | 8,0 | Só Sorrisi (€67, "Pazienti Dormienti"); "pacienti dormienti" no conector: 0 anúncios dedicados. No BR: "reativar pacientes" só agência/gestão (258 resultados, nenhum kit) | €67 | BRECHA fora do Sorrisi | P-M |
| 3 | **Scripts de WhatsApp/orçamento + precificação × dentista × BR** | 7,5 | Rafaella Lopes: 13 anúncios, 39 d (21/09), títulos "Scripts de orçamento para dentistas", "Precificação simples para dentistas", "Padronize os orçamentos da clínica" | VERIFICAR | **PROVADO BR** (nicho pequeno, 1 vendedor) | M. Oportunidade: no nosso kit BR de dentista (já saturado em documentos) é bump de maior valor percebido |
| 4 | **Banco de posts / pack Canva × dentista × BR** | 6,5 | Ultra Pack Dentista (37 d, page 116497988215732): 500+ posts, 500 stories, 200+ reels, 500 legendas, calendário 30 d; Hotmart; **R$37 (de R$97)**, garantia 7 d, bônus "Tabela de preços de procedimentos" R$27. Post Pra Dentista (BR, 8 anúncios, 0 d, "Linha Prestige/Elegance/Fresh" por paleta) entrando agora | R$37 | **PROVADO BR (37 d), já em saturação** | M, mas concorre por R$37 |
| 5 | **Banco de posts × dentista × ES-LATAM** | 6,0 | Ultra Pack Dentista roda em ES ("+500 Publicaciones Dentales", "+200 Reels", USD, 22-37 d) | USD (VERIFICAR) | PROVADO em ES neutro (não prova país) | M |
| 6 | **Biblioteca de estudo (carpetas/tarjeteros/esquemas) × enfermagem × MX/LATAM** | 7,0 | IA Programas (MXN, 14 anúncios, 39 d, 21/09): "210 carpetas con tarjeteros, libros, esquemas, resúmenes, atlas", NANDA/NIC/NOC, entrega por Drive/WhatsApp, PDF imprimível | VERIFICAR | **PROVADO MX 39 d**, mas é pacote pirata-like (livros com copyright); risco | G (conteúdo próprio; não copiar livros). Profissão fora do nosso foco atual |
| 7 | **Prompts de IA × nutricionista × BR** | 5,5 | "Prompts Prontos": "150 prompts de IA para nutricionistas", R$27 (6 anúncios, 11 d); "IA PARA NUTRI" (2 anúncios, 0 d). Prompts para psicólogo BR: só "100 prompts de fotos IA da sua profissão" (Daiane Neves, 3 anúncios, 15 d) | R$27 | TESTE | P (texto) |
| 8 | **Cardápio + precificação (CMV) × alimentação BR** | 6,5 | Cardápio Lucrativo (580612692618224): 17 anúncios, 56 d, "POR APENAS 29,90"; Prato CMV, Delivery do Zero e outros 89 resultados para "planilha precificação cardápio" | R$29,90 | **PROVADO BR (56 d)**; mercado de confeitaria/delivery, não de profissão regulada | M. Encaixa na Consultora de Alimentos como bump (planilha CMV) |
| 9 | **Pasta de sterilização/autoclave (registros) × dentista × IT** | 7,5 | Sorrisi vende Kit Sterilizzazione a €49 (12 d de anúncio "Tracciabilità autoclave in 5 PDF" e "Registri di sterilizzazione da stampare") | €49 | TESTE | P (já temos POPs de biossegurança) |
| 10 | **Checklist/simulado de inspeção ASL-NAS × dentista × IT** | 7,5 | "checklist ispezione ASL studio dentistico": só Sorrisi ("Lo studio a norma", 1 anúncio). Qualitiva COP 79.900 prova semáforo em CO (276 d, `produtos-adjacentes`) | n/d | BRECHA parcial | M |
| 11 | **Planilha-semáforo Res. 3100 × dentista × CO** | 8,0 | Qualitiva 276 d, COP 79.900 (`funil-preco-bumps`); ninguém com versão odonto | COP 79.900 | PROVADO (genérico), BRECHA odonto | M |
| 12 | **Planilha de tarifas + agenda de recall + guia "quanto cobrar" × higienista × IT** | 6,5 | Sorrisi Kit Igienista €74; higienista fora do nosso catálogo | €74 | TESTE | M |
| 13 | **Scripts WhatsApp × consultório × ES-LATAM** | 3,0 | 0 anúncios de produto; só agências de marketing (Despacho de Marketing de BC, Digital Friends, MX/CO) | - | BRECHA PROVÁVEL (frase longa; confirmar) | P |
| 14 | **Calendário de conteúdo / banco de posts × psicólogo (MX, IT, BR)** | 4,0 | MX: 0 anúncios de produto no termo; IT "post Instagram per dentisti": 0 produto; BR "banco de posts psicólogos": 0 | - | BRECHA PROVÁVEL; psicólogo evita "post pronto" por ética de conselho | P-M |
| 15 | **Flashcards/simulado × psicólogo, nutri, fisio** | 3,5 | BR "simulado concurso flashcards psicólogo": 0 anúncios ativos; ES "flashcards psicología": 0 produto relevante (só IA Programas, enfermagem) | - | BRECHA PROVÁVEL, mas demanda por prova de conselho não confirmada | M |
| 16 | **Planner/agenda clínica × psicólogo BR** | 3,5 | "planner psicólogo": 3 resultados, nenhum produto (Ser Psicólogo = curso anual 12x R$42,42; Reservatório de Dopamina) | - | BRECHA PROVÁVEL | P |
| 17 | **Prompts IA × psicólogo/dentista × ES, IT, DE, FR, PL** | 3,0 | 0 anúncios (ES/MX/CO "prompts ChatGPT para dentistas"; IT "prompt ChatGPT per psicologi") | - | BRECHA, sem sinal de demanda pago | P |
| 18 | **Kits de documentos × dentista × DE, FR, PL** | 7,0 | 0 vendedores de kit pago nativo com os termos curtos (DE "Vorlagens Zahnarztpraxis QM": 0; FR "modèles cabinet dentiste": só Académie du Sourire, formação; PL: 0). Consistente com `marketplaces` (Hotmart IT/FR/EN espelho BR) | - | BRECHA (já constava nos relatórios; confirmado com formato) | M-G (norma local de cada país) |

Formatos sem teste útil hoje: mapas mentais (outro agente), contratos-modelo (já em kit), apostilas (cobertas por "eBook" do Sorrisi), calculadoras (0 resultado em MX/IT/BR com termos testados), sessões prontas (PROVADO em fono/ABA, ver `arbitragem-kits-br-v2`).

## 3. Formatos que servem de BUMP/BÔNUS (com âncora de preço medida)
| Formato | Onde entra | Âncora de mercado | Preço sugerido (hipótese a testar) | Nota |
|---|---|---|---|---|
| Pacote DVR/DUVRI guiado | dentista IT bump forte | Sorrisi €127; consultor €150-300 | bump **€19,90 a €29** (versão enxuta) ou upsell €49-67 | 8,5 |
| Pazienti dormienti (lista + 6 mensagens + painel) | dentista IT/BR bump | Sorrisi €67 | €9,90-14,90 | 8,0 |
| Registro de esterilização/autoclave (5 PDFs) | dentista IT/MX bump | Sorrisi €49 | €9,90 | 7,5 |
| Planilha-semáforo / simulado de inspeção | todos | Qualitiva COP 79.900 | €9,90 / COP 39.900-79.900 | 8,0 |
| Scripts de orçamento + WhatsApp (10 a 20 mensagens) | dentista BR e IT | Rafaella Lopes (39 d) | R$19,90 / €9,90 | 7,5 |
| Tabela de preços de procedimentos | dentista | Ultra Pack dá como bônus de R$27 | bônus dentro do Completo | 6,0 (defesa) |
| Banco de posts (50 a 100, só como bônus) | dentista | Ultra Pack: R$37 com 500+; clone IT já dá "20 grafiche IG" de bônus | **só bônus**, nunca produto (R$37 é piso) | 5,0 |
| Prompts de IA da profissão (30 a 50) | psicólogo, nutri | R$27 por 150 (Prompts Prontos, 11 d) | bônus ou bump R$9,90 | 5,0 |
| Webinar gravado "Studio in regola in 60 minuti" | dentista IT upsell | Sorrisi €60 | €29-49 | 5,5 (G: vídeo/humano) |
| Planilha CMV/precificação de cardápio | Consultora de Alimentos BR | Cardápio Lucrativo R$29,90 (56 d) | bump R$14,90-19,90 | 7,0 |

## 4. Respostas diretas
1. **O que vende e ainda não é vendido onde?** (a) Módulos legais pagos de dentista (DVR, esterilização, consensi) existem só em IT (Sorrisi), ainda não em ES/PT/FR/DE/PL nem em MX/CO com preço público: BRECHA de formato em todos esses países. (b) Reativação de pacientes como produto: só Sorrisi IT; no BR só agências.
2. **Dá para cobrar mais que €19,99?** Sim, em módulos: Sorrisi tem 11 SKUs de €34 a €127. O ponto de decisão é o clone de €19,99 não tem módulos nem DVR, e o Sorrisi não tem app nem 252 documentos. Combinar: Completo €19-27 + módulos €9,90-29 por tema é o espaço vazio entre os dois.
3. **BR:** formatos de marketing para dentista (posts, scripts, precificação) estão PROVADOS (37 e 39 d) e baratos (R$37). Não é lugar para entrar com produto próprio, só como bônus.
4. **Psicólogo:** sem sinal pago para banco de posts, prompts, planner, flashcards em nenhum país testado. O dinheiro continua em documentos + modelos clínicos (fichas TCC, laudo), conforme `produtos-adjacentes`.

## 5. Lista final de VERIFICAR
1. Art. 17 e art. 55 do D.Lgs. 81/2008 (obrigação do DVR e sanção de arresto/ammenda): a fonte oficial (normattiva.it) não abriu por completo no WebFetch; hoje só tenho o texto do anúncio do Sorrisi. Conferir em https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81 antes de citar em copy. Idem a obrigação de DVR para consultórios sem funcionários.
2. Sorrisi in Regola: reembolso (a página linka política sem mostrar prazo), vendas reais, quando começou a loja, se os anúncios de módulos passam de 30 d na próxima semana (rodar em 7 dias), se há outras páginas (igienista kit anunciado desde 17/10 em 1 anúncio).
3. Rafaella Lopes (BR, page 1118482651342056): preço, plataforma e se é produto ou serviço de consultoria (anúncio não abriu).
4. Cardápio Lucrativo, Prato CMV, Delivery do Zero (BR): preço real, plataforma, idade de cada page (medi só Cardápio: 56 d).
5. IA Programas (MX): preço e se o conteúdo é de terceiros com direitos autorais (risco); WhatsApp como canal de venda.
6. Ultra Pack Dentista: preço em ES/USD (a página lida estava em PT/BR; R$37 de R$97); país real de venda dos anúncios em ES.
7. Post Pra Dentista (BR, 8 anúncios, 0 d): rechecar em 30 d.
8. Frases de busca curtas em DE/FR/PL/ES para calendário, flashcards, planner, calculadora: refazer com SearchAPI quando voltar o crédito (08/11) ou com termos locais.
9. Tamanho de mercado/normas: não reconfirmei hoje (usar `tamanho-publico-2026-10-30.md` e `prazos-de-norma-2026-10-30.md`).
10. Conversões de moeda: aproximadas.

## 6. Fontes
- Conector Meta Ad Library (30/10/2026): page_ids 1063538733498593 (Sorrisi in Regola), 1118482651342056 (Rafaella Lopes), 104897328145693 (Post Pra Dentista), 116497988215732 (Ultra Pack Dentista), 580612692618224 (Cardápio Lucrativo), 809461785581622 (IA Programas), 1383946858134782 (Prompts Prontos), 1425921197272607 (IA PARA NUTRI), 1514939898362514 (Consultorio en Orden), 1316795101520270 (Kit di Documenti Psicologici).
- https://sorrisiinregola.com/ (página lida em 30/10/2026); https://dentistapro.ultrapackcanva.com/ (lida em 30/10/2026); Ad Library IDs 1429628915360534 e 1112839151396476 (textos de anúncio lidos no navegador).
- Relatórios internos: `funil-preco-bumps-concorrentes-2026-10-30.md`, `marketplaces-2026-10-30.md`, `produtos-adjacentes-2026-10-30.md`, `3 - EU/pesquisas/arbitragem-kits-br-v2-2026-10-30.md`.
