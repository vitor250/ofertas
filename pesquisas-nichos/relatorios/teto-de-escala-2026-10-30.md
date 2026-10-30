# Teto de escala por país e nicho: quantas vendas por dia cada um aguenta (30/10/2026)

Data de referência: 30/10/2026. Meta (conector, somente leitura) consultado nas contas 03 e 05, últimos 90 dias; nada foi alterado. SearchAPI sem créditos até 08/11 (não usado). Navegador embutido não foi necessário.

## 1. Resumo (o que decide)

1. **Os tetos reais são pequenos para profissão de nicho.** Um kit de profissional em país de 30 a 90 mil profissionais aguenta **1 a 4 vendas/dia no cenário base** (0,5 a 8 nos extremos). Para chegar a 10+/dia só dois tipos de público servem: (a) profissão grande (psicólogo MX 159 mil, professora de pré-escola PL 138 mil) ou (b) público NÃO profissional enorme (host de aluguel IT, ZZP NL, landlord UK), onde a conta é incerta.
2. **Melhor teto com unit economics saudável (profissionais):** IT psicólogo (3,6/dia base), PL professora de pré-escola (5,4), GR HACCP (3,0), CO odontólogo (2,9), IT dentista (2,6), CO independentes de saúde (2,6), ES psicólogo (1,8), PL dentista (1,6).
3. **México é grande no teto (psicólogo 7,1/dia base) mas fraco na economia:** o ticket observado é R$46 contra CPA ~R$30, ROAS ~1,2. Sem subir o ticket (bumps, preço MXN 299+), MX não escala.
4. **Itália:** CPM bom (R$24), mas o funil do histórico italiano converteu só 19% do checkout (CPA R$40 observado vs R$29 no BR). Isso já está no modelo (fator 0,55). Teto base: psicólogo 3,6/dia e dentista 2,6/dia = ~6 vendas/dia somando, ~R$700 de faturamento líquido/dia. Esse é o limite da Itália para essas duas profissões, e a ordem é conferir os meios de pagamento antes de passar de R$100/dia (diagnóstico do funil, item 6).
5. **Reino Unido/Austrália (ticket alto):** poucos profissionais (UK childminders 24,7 mil; AU NDIS 17,5 mil), teto 0,8 a 1,4/dia, mas ticket R$150 a R$300 faz o ROAS ser o melhor da lista (AU NDIS 5,4; UK CQC 4,5 em amostra mínima). Venda baixa, margem alta.
6. **Nada aqui é meta de venda.** Modelo de teto de longo prazo (90 dias) com premissas explícitas (seção 3). Calibração: dentista BR real hoje ~3,4 vendas/dia (96 compras em 28 dias) com ~R$125/dia; o teto do modelo para o Brasil seria muito maior, ou seja, o BR ainda não bateu o teto; o que limita é criativo e margem.

## 2. Dados reais das nossas contas (Meta, 90 dias, por país)

Conta 05 (Brasil + LATAM profissional) e conta 03 (ES/EU + histórico de produto infantil/mass). Números de CPM, CPC, CTR e compras do pixel (não conciliados com Wiapy/Hotmart).

| País | Conta | Gasto R$ | CPM R$ | CPC R$ | CTR | LPV/clique | Compras pixel | CPA R$ | Observação |
|---|---|---|---|---|---|---|---|---|---|
| BR | 05 | 99.748 | 30,36 | 1,09 | 2,78% | 69% | 4.116 | 24,2 | Mistura de ofertas e ticket baixo; dentista sozinho CPM ~40 |
| MX | 05 | 4.295 | 28,20 | 0,75 | 3,77% | 48% | 142 | 30,2 | Conta 05, ofertas LATAM |
| CO | 05 | 2.864 | 33,14 | 0,95 | 3,50% | 59% | 85 | 33,7 | |
| CO | 03 | 1.712 | 11,98 | 0,32 | 3,75% | 32% | 81 | 21,1 | Público de massa (produto infantil) |
| CL | 05 | 871 | 24,96 | 0,63 | 3,98% | 56% | 36 | 24,2 | |
| CL | 03 | 667 | 7,71 | 0,24 | 3,16% | 31% | 28 | 23,8 | |
| PE | 05 | 1.460 | 26,20 | 0,59 | 4,44% | 49% | 59 | 24,7 | |
| IT | 03 | 7.934 | 24,12 | 0,36 | 6,68% | 46% | 198 | 40,1 | Inclui produto antigo; compra/IC de 19% |
| ES | 03 | 482 | 5,59 | 0,30 | 1,88% | 26% | 16 | 30,2 | Muito barato, público de massa |
| DE | 03 | 65 | 14,32 | 0,32 | 4,47% | 43% | 2 | 32,5 | Amostra pequena |
| CH | 03 | 225 | 38,49 | 0,68 | 5,66% | 46% | 6 | 37,5 | Amostra pequena |
| GB | 03 | 34 | 25,91 | 0,36 | 7,15% | 23% | 0 | n/d | Amostra mínima |
| AR / EC / CR / GT / DO / BO / HN | 03 | 100 a 410 cada | 6 a 14 | 0,12 a 0,27 | 3,8 a 5,6% | 25 a 40% | 7 a 18 | 15 a 30 | Público de massa, LATAM barato |
| FR, GR, HU, CZ, PL, RO, NL, UK (profissional) | 03/05 | < R$25 cada | n/m | n/m | n/m | n/m | 0 | n/d | **Sem dado próprio**; usei benchmark |

Funil por oferta (do diagnóstico): LPV/clique 89 a 96% no dentista BR contra 57% em MX e advogado: parte do que parece "CPC baixo" no MX é perda de clique.

**Compras por pessoa alcançada (campanhas da conta 05, 90 dias):**
dentista "escala 24.10" 37/21.222 = 0,17%; dentista "simulado 22.10" 30/12.251 = 0,24%; consultora "teste 1.0" 26/7.581 = 0,34%; fono "teste 1.5.2" 60/15.429 = 0,39%; "maleta 06 vídeo" 501/167.269 = 0,30%. Frequência 1,2 a 2,5. **Âncora usada: 0,2% de conversão por alcançado em kit profissional.**

## 3. Método e premissas (para você poder questionar)

- **Preço do clique/CPM por país:** nosso CPM real onde existe (BR, MX, CO, CL, IT). Onde não existe, benchmark Meta de e-commerce de 2026 da Lebesgue (CPM USD: [fonte](https://lebesgue.io/facebook-ads/facebook-cpm-by-country), 27/07/2026: US 16,08; UK 11,81; AU 11,63; DE 9,05; NL 8,58; FR 6,95; ES 6,65; PT 6,02; IT 6,06; CZ 5,70; PL 5,55; RO 5,38; HU 5,24; GR 4,89; BG 4,21; MX 3,92; ZA 2,99; BR 2,63; CL 2,44; CO 2,00). O benchmark é de e-commerce geral e não traz CPC/CTR. Para ver se serve, comparei: BR real é 2,1x o benchmark; MX 1,3x; CO 1,1x (massa) a 3x (profissional); IT 0,7x. Ou seja: **a nossa segmentação por profissão custa mais que o benchmark na América Latina** e é igual ou mais barata na Itália. Usei CPM observado onde há e benchmark x 1,0 nos demais (não apliquei prêmio, o que pode subestimar o CPM europeu para profissional; ver sensibilidade).
- **Câmbio (premissa, sem fonte oficial nesta rodada, VERIFICAR):** US$1 = R$5,5; €1 = R$6,0; £1 = R$7,3; A$1 = R$3,6.
- **CPA = CPM x frequência 1,8 / (1000 x 0,2% x fator de funil do país).** Fator de funil (premissa): BR 1,0; UK/AU/IE/US 1,0; PT/CO/CL 0,9; ES/RO/GR/HU/CZ/BG/MX/ZA 0,8; FR/DE/PL/NL 0,7 (sem BLIK/iDEAL/Bancontact na Hotmart, ver `pagamento-fiscal-por-pais-2026-10-30.md`); IT 0,55 (calibrado com o CPA italiano observado de R$40). **Teste de consistência:** o modelo reproduz o CPA real do dentista BR (R$36 modelo vs R$37 real), MX (R$32 vs R$30), CO (R$33 vs R$34), CL (R$25 vs R$24) e IT (R$39 vs R$40). Em MX/CO/CL/IT o fator foi ajustado a esses dados, então isso confirma a conta, não prova o fator. Os demais países são extrapolação.
- **Teto de vendas em 90 dias = N x alcance x conversão acumulada x fator de prova.** N = profissionais da fonte oficial (ver tabela). Alcance: 50% (35% para host/landlord/ZZP, 15% UK landlords: não são públicos de interesse "profissional"). **Conversão acumulada em 90 dias: 0,5% / 1,0% / 2,0% do público alcançado** (cenários conservador / base / otimista). Isso vem de 0,2 a 0,4% por alcançado por rodada (seção 2) x 2 a 5 rodadas com rendimento decrescente. **É a premissa mais fraca do modelo**; não há dado de 90 dias de exposição repetida. Dividi por 90 para vendas/dia.
- **Fator de prova:** PROVADO 1,0 (0,8 a 0,9 quando só parcial ou concorrência BR já presente); TESTE/PRAZO 0,6 a 0,7; BRECHA (ninguém vende) 0,5, porque ausência de vendedor pode ser ausência de demanda.
- **Ticket líquido:** preço sugerido nos relatórios x 0,86 (Hotmart 9,9% + fixa + imposto). MX usei o ticket observado (R$46 bruto). Não incluí reembolso (garantia 7 a 30 dias) nem bumps não observados.
- **Gasto/dia no base** = vendas/dia x CPA. **Faturamento líquido/dia** = vendas/dia x ticket líquido.
- **Nota 0 a 10 = 50% teto de vendas** (escala log: 20 vendas/dia = 10) **+ 35% economia** (ROAS de 0,8 = 0 a 2,5 = 10) **+ 15% confiança no N** (10 se N oficial, 5 se VERIFICAR ou suposto).

## 4. Ranking 0-10 com vendas/dia por nicho e país

| # | Nota | País · nicho | N (fonte) | Prova | Vendas/dia cons. / base / otim. | CPM R$ | CPA R$ | Ticket líq. R$ | ROAS | Gasto/dia no base R$ | Fat. líq./dia R$ | N p/ 5 vendas/dia |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **9,5** | IT · Host de affitti brevi (CIN/sanções) | 370.000 (CIN emitidos dez/2024 (immobiliare); 538.674 estruturas) | PROVADO | 7,2 / **14,4** / 28,8 | 24 | 39 | 114 (€22 médio) | 2,9 | 567 | 1.633 | 128.571 |
| 2 | **9,5** | NL · ZZP: dossiê DBA (01/01/2027) | 1.200.000 (~1,2 mi ZZP (relatório v2)) | PRAZO/BRECHA | 9,3 / **18,7** / 37,3 | 47 | 61 | 139 (€27) | 2,3 | 1.133 | 2.601 | 321.429 |
| 3 | **9,0** | UK · Landlords (RRA) | 2.800.000 (fonte não oficial, VERIFICAR) | TESTE | 14,0 / **28,0** / 56,0 | 65 | 58 | 138 (£22) | 2,4 | 1.637 | 3.867 | 500.000 |
| 4 | **7,5** | IT · Psicólogo (Valigetta Psicólogo) | 93.521 (ENPAP 31/12/2025) | TESTE | 1,8 / **3,6** / 7,3 | 24 | 39 | 114 (€22) | 2,9 | 143 | 413 | 128.571 |
| 5 | **7,5** | PL · Professora de pré-escola (Kompas Jutra 01/09/2026) | 138.743 (GUS/ORE (relatório v2)) | PRAZO/TESTE | 2,7 / **5,4** / 10,8 | 31 | 39 | 88 (€17) | 2,2 | 212 | 473 | 128.571 |
| 6 | **7,3** | GR · HACCP + treinamento ΕΦΕΤ | 76.728 (Eurostat 2024 (restauração)) | TESTE/PRAZO | 1,5 / **3,0** / 6,0 | 27 | 30 | 98 (€19) | 3,2 | 90 | 293 | 128.571 |
| 7 | **7,2** | CO · Odontólogo | 65.650 (ReTHUS mar/2023 (secundária)) | TESTE (nenhum kit odonto) | 1,5 / **2,9** / 5,8 | 33 | 33 | 82 (R$95) | 2,5 | 97 | 238 | 112.500 |
| 8 | **7,1** | IT · Dentista (Valigetta, no ar) | 51.680 (Eurostat 2024 (Albo 64,9 mil)) | PROVADO (BR a €19,99) | 1,3 / **2,6** / 5,2 | 24 | 39 | 114 (€22) | 2,9 | 102 | 293 | 100.000 |
| 9 | **7,0** | CO · Independentes de saúde (Res. 3100) | 47.219 (REPS out/2025 (secundária)) | PROVADO (Qualitiva 276 d) | 1,3 / **2,6** / 5,2 | 33 | 33 | 82 (R$95 (COP ~80 mil)) | 2,5 | 87 | 214 | 90.000 |
| 10 | **6,7** | ES · Psicólogo | 47.396 (INE 2025 (rama sanitaria)) | TESTE | 0,9 / **1,8** / 3,7 | 37 | 41 | 114 (€22) | 2,8 | 76 | 209 | 128.571 |
| 11 | **6,6** | PL · Dentista | 36.965 (Eurostat 2024) | PROVADO parcial (Kontrola ≥200 d; janela fechando) | 0,8 / **1,6** / 3,3 | 31 | 39 | 98 (€19 (~80 zł)) | 2,5 | 64 | 161 | 112.500 |
| 12 | **6,5** | ES · Veterinário (PRESVET) | 36.989 (INE 2023) | PRAZO/TESTE | 0,7 / **1,4** / 2,9 | 37 | 41 | 114 (€22) | 2,8 | 59 | 163 | 128.571 |
| 13 | **6,4** | UK · Childminders/early years (Ofsted) | 24.700 (gov.uk 31/03/2026 (59.700 provedores no total)) | PROVADO (CRH 485 d) | 0,7 / **1,4** / 2,7 | 65 | 58 | 157 (£25) | 2,7 | 80 | 215 | 90.000 |
| 14 | **6,4** | CL · Kine/fono/TO | 47.700 (kine CL ≈47,7 mil) | BRECHA | 0,7 / **1,3** / 2,6 | 25 | 25 | 69 (R$80) | 2,8 | 33 | 91 | 180.000 |
| 15 | **6,3** | CZ · Estética/cabeleireiro/tatuagem (KHS) | 43.396 (Eurostat) | BRECHA | 0,6 / **1,2** / 2,4 | 31 | 35 | 98 (€19) | 2,8 | 43 | 118 | 180.000 |
| 16 | **6,2** | ZA · ECD / creche | 46.000 (42–50 mil programas) | TESTE | 0,8 / **1,5** / 3,1 | 25 | 28 | 64 (R$ ~75) | 2,3 | 43 | 99 | 150.000 |
| 17 | **6,1** | ES · Dentista | 33.300 (Eurostat 2024) | BRECHA | 0,5 / **0,9** / 1,9 | 37 | 41 | 114 (€22) | 2,8 | 38 | 105 | 180.000 |
| 18 | **6,0** | HU · HACCP | 26.370 (Eurostat) | TESTE | 0,4 / **0,9** / 1,8 | 29 | 32 | 98 (€19) | 3,0 | 28 | 86 | 150.000 |
| 19 | **6,0** | FR · Dentista | 48.413 (DREES 2026 (~40 mil liberais)) | BRECHA | 0,7 / **1,3** / 2,7 | 38 | 49 | 114 (€22) | 2,3 | 66 | 153 | 180.000 |
| 20 | **6,0** | RO · Dentista | 21.647 (Eurostat 2024) | TESTE (clones BR 1,5–6 d) | 0,4 / **0,8** / 1,7 | 30 | 33 | 88 (€17) | 2,6 | 28 | 74 | 128.571 |
| 21 | **5,9** | AU · NDIS providers | 17.464 (NDIS Commission dez/2025 (ativos)) | Demanda PROVADA; preço baixo = TESTE | 0,4 / **0,8** / 1,6 | 64 | 58 | 310 (A$100) | 5,4 | 45 | 240 | 112.500 |
| 22 | **5,8** | MX · Psicólogo (Maletín, no ar) | 159.000 (relatório top10 MX 27/10 (oficial)) | PROVADO (RLPRO 99 d, $499) | 3,5 / **7,1** / 14,1 | 28 | 32 | 40 (ticket observado R$46) | 1,2 | 224 | 280 | 112.500 |
| 23 | **5,8** | US · Preparador de impostos hispânico (assumindo 10% do total, VERIFICAR) | 87.970 (879.698 total BLS/IRS; fração hispânica NÃO achada) | TESTE+PRAZO | 1,7 / **3,4** / 6,8 | 88 | 80 | 166 (US$35) | 2,1 | 272 | 566 | 128.571 |
| 24 | **5,7** | BG · HACCP | 19.441 (Eurostat) | BRECHA | 0,3 / **0,5** / 1,1 | 23 | 26 | 77 (€15) | 3,0 | 14 | 42 | 180.000 |
| 25 | **5,7** | GR · Dentista | 13.840 (Eurostat 2024) | TESTE | 0,3 / **0,5** / 1,1 | 27 | 30 | 98 (€19) | 3,2 | 16 | 53 | 128.571 |
| 26 | **5,6** | PT · Dentista | 12.796 (OMD/INE 2025) | TESTE | 0,2 / **0,4** / 0,9 | 33 | 33 | 98 (€19) | 3,0 | 14 | 42 | 150.000 |
| 27 | **5,3** | DE · Dentista | 71.983 (Eurostat 2024) | BRECHA | 1,0 / **2,0** / 4,0 | 50 | 64 | 114 (€22) | 1,8 | 128 | 227 | 180.000 |
| 28 | **5,2** | MX · Consultório de saúde (fisio, podologia, nutri…) | 85.908 (DENUE/relatório v2) | PROVADO (RLPRO, ADE ≥199 d) | 2,1 / **4,3** / 8,6 | 28 | 32 | 40 (R$46) | 1,2 | 136 | 170 | 100.000 |
| 29 | **5,1** | PT · Psicólogo | 26.000 (OPP (>26 mil, VERIFICAR)) | BRECHA | 0,4 / **0,7** / 1,4 | 33 | 33 | 98 (€19) | 3,0 | 24 | 71 | 180.000 |
| 30 | **4,9** | UK · Care agencies (CQC) | 11.000 (setorial, VERIFICAR) | PROVADO parcial (Care Daily 130 d) | 0,2 / **0,5** / 1,0 | 65 | 58 | 264 (£42) | 4,5 | 29 | 129 | 112.500 |
| 31 | **4,6** | DE · Psicoterapeuta (Kassen) | 36.197 (KBV 31/12/2025) | BRECHA | 0,5 / **1,0** / 2,0 | 50 | 64 | 114 (€22) | 1,8 | 64 | 114 | 180.000 |


Como ler: "Vendas/dia" são do teto de 90 dias, não de amanhã. A coluna "N p/ 5 vendas/dia" é o tamanho de público necessário no cenário base para o nicho chegar a 5 vendas/dia, útil quando o N for VERIFICAR.

### Ressalvas por linha (as três primeiras notas são enganosas)
- **IT host de affitti brevi, NL ZZP e UK landlords (notas 9 a 9,5):** públicos enormes e NÃO profissionais. A conversão de 1% do alcançado vem de kits profissionais; para host/ZZP/landlord não existe dado nosso. IT host tem prova real (Protocollo Zero Sanzioni, 163 dias, €27, garantia 30 dias) e portanto é o único dos três em que eu confiaria; NL ZZP é PRAZO (01/01/2027) sem vendedor; UK landlords tem concorrência grátis forte e nenhum vendedor com 30 dias. **Tratar como "teto alto, confiança baixa": teste de R$300 antes de qualquer conclusão.**
- **US preparador de impostos:** N total 879.698; a fração hispânica NÃO foi achada nas pesquisas; usei 10% como suposição visível (87.970). CPM US de R$88 e CPA R$80 torna o ROAS 2,1 só se o ticket for US$35.
- **UK/AU alto ticket:** nota baixa pelo teto de vendas, mas ROAS 2,7 a 5,4 (AU NDIS, UK CQC) com poucas vendas. O preço de £42/A$100 está acima do que o concorrente barato cobra no UK (CRH £30) e abaixo do pacote de £789 (Care Daily): faixa sem teste.
- **ZA:** ticket suposto (R$75) e CPM sem dado; confiança mínima.
- **MX:** o ticket de R$46 é o observado; se subir para R$93 (MXN ~300) o ROAS vai a ~2,5 e a nota sobe.

## 5. Sensibilidade (o que muda o resultado)

| Premissa | Se piorar | Efeito no ranking |
|---|---|---|
| Conversão acumulada 90 dias | 0,5% em vez de 1,0% (coluna "cons.") | Tudo cai pela metade; só IT host, NL e UK landlords mantêm 7+ vendas/dia |
| CPM europeu +50% (profissional > e-commerce) | CPA PL/RO/GR/HU/CZ vai de ~R$30-39 para ~R$45-58 | ROAS cai de 2,2-3,2 para 1,5-2,2. GR HACCP segue acima de 1,5; PL pré-escola vai a ~1,5 |
| Funil IT sem corrigir (fator 0,55) | Já aplicado | Se os meios de pagamento forem corrigidos e o fator chegar a 0,8, CPA IT vai de R$39 a R$27 e o ROAS de 2,9 a 4,2 |
| Fator de prova BRECHA 0,5 | Se a ausência de vendedor significar ausência de demanda, o fator real é ~0 | ES dentista, FR/DE dentista e psicólogo, PT psicólogo, CZ, BG, CL viram teste de R$300 antes de qualquer conta |
| Concorrência BR clonando | Já visto em IT, PT, RO, GR, PL | Reduz o fator de prova de PROVADO para 0,6 em 60 a 90 dias; vale lançar primeiro |

## 6. Leitura por prioridade (decisão, não meta)

1. **Subir a Itália para o teto antes de abrir país novo:** psicólogo IT (3,6/dia) + dentista IT (2,6/dia) já cobrem 6 vendas/dia e R$700/dia líquidos se o funil chegar ao fator 0,55; é a combinação com maior N provado e CPM mais barato da Europa. Condição: checar Hotmart EUR (Apple Pay, Klarna, Satispay) antes de passar de R$100/dia (diagnóstico do funil).
2. **Polônia (pré-escola 5,4/dia, dentista 1,6/dia):** pré-escola é o maior teto profissional da lista fora do MX, com gancho de 01/09/2026 e N de 138.743; risco: BLIK ausente (fator 0,7 já aplicado) e vendedor local barato (Centrum Pedagogiczne: 17 a 27 zł por documento).
3. **Grécia HACCP (3,0/dia, ROAS 3,2):** melhor economia da Europa por CPM baixo, N de 76.728 (Eurostat); prova só de cursos pagos, sem kit.
4. **Colômbia (odontólogo 2,9/dia + independentes de saúde 2,6/dia):** prova local de 276 dias (Qualitiva); os dois nichos se sobrepõem em audiência (não somar 5,5 sem teste). Ticket suposto R$95 (COP ~80 mil) com IVA 19% por conta do criador (ver `pagamento-fiscal-por-pais-2026-10-30.md`); se o IVA não for retido, sai da margem e o ROAS cai de 2,5 para ~2,0.
5. **México (psicólogo 7,1/dia):** é o maior N profissional (159 mil) mas o ticket de R$46 só fecha ROAS 1,2. Prioridade é subir ticket antes de escalar.
6. **UK childminders e AU NDIS (ticket alto):** pouco volume e margem alta; bons candidatos a segunda onda em inglês, sem pressa.
7. **Não escalar por enquanto:** FR, DE, PT psicólogo, CZ, BG, CL, ES dentista (todos BRECHA, nota ≤ 6,3 e prova nula).

## 7. VERIFICAR (lista final)

1. **Conversão acumulada em 90 dias (0,5/1,0/2,0%) e alcance de 50%:** são premissas; nenhuma conta nossa tem 90 dias de exposição repetida a um público fechado. Medir com `reach` acumulado por campanha de dentista IT e dentista BR em 30 dias.
2. **Câmbio** (R$5,5/US$, R$6,0/€, R$7,3/£, R$3,6/A$): sem fonte nesta rodada.
3. **CPM europeu e anglo para público profissional:** usei benchmark de e-commerce geral; nenhum país de PL, RO, GR, HU, CZ, BG, NL, UK, AU, ZA, IE tem dado nosso (gasto < R$25). Conferir com R$100 de teste por país.
4. **Fatores de funil por país** (checkout/meios de pagamento): apenas IT, MX, CO, CL, BR estão calibrados.
5. **N faltante ou fraco:** PL (salões/fisioterapeutas/psicólogos escolares/gastronomia), RO professoras, IT fisioterapista/HACCP/veterinário, FR fonoaudiólogo, IE hosts, CL Ley 21.719 (RNPI), MX dentista, HU segurança do trabalho, PE; fração hispânica dos preparadores de impostos dos EUA; UK CQC (11 mil é fonte setorial); UK landlords (2,8 mi é fonte não oficial); PT psicólogos (>26 mil sem página aberta); ZA 42 a 50 mil (faixa).
6. **Ticket real com bumps** em IT (€22 suposto) e CO/CL (suposto): nenhum dado de venda com a Valigetta ainda (R$0,46 gastos em 30/10).
7. **Vendas do pixel não conciliadas** com Wiapy/Hotmart/Utmify (MX: 3 compras podem incluir teste).
8. **Reembolso e IVA** não entram no ticket líquido; Colômbia/Peru têm IVA por conta do criador.
9. **Sobreposição de nichos** (CO odonto x independentes; IT dentista x psicólogo não se sobrepõem, mas compartilham verba e criativo): não somar tetos de nichos da mesma audiência sem teste.
10. Qualquer "BRECHA" do ranking: ausência de vendedor não prova demanda.

## 8. Fontes

- Conector Meta (somente leitura), contas 623752106927686 (03) e 574561479021139 (05), breakdown por país e campanhas, 90 dias até 30/10/2026.
- CPM por país: https://lebesgue.io/facebook-ads/facebook-cpm-by-country (27/07/2026, e-commerce).
- N, provas e preços de concorrentes: relatórios `-v2` da pasta (`3 - EU/pesquisas/novos-nichos-*-v2-2026-10-30.md`, `2 - ES/pesquisas/novos-nichos-americas-v2-2026-10-30.md`, `psicologo-dentista-4-paises-2026-10-29.md`, `dentista-resto-europa-2026-10-29.md`, `psicologo-resto-europa-2026-10-29.md`, `top10-por-pais-2026-10-27/mexico.md`), `nosso-funil-diagnostico-2026-10-30.md` e `pagamento-fiscal-por-pais-2026-10-30.md`. As fontes oficiais de N estão citadas em cada relatório.
