# Meios de pagamento e fiscal por país (Hotmart e alternativas)

Data de referência: 30/10/2026. Pesquisa feita só com páginas oficiais da Hotmart (Central de Ajuda), documentação dos meios de pagamento e autoridades fiscais. Onde só achei blog/agregador, marquei VERIFICAR. Nada foi comprado nem cadastrado. SearchAPI sem crédito (não foi necessário aqui).

Premissa: o vendedor é pessoa/empresa com conta Hotmart registrada no BRASIL, vende produto digital sem interação humana (eBook/kit de documentos + app) e já opera EUR (Itália), MXN (México) e BRL.

---

## 1. Resumo executivo (o que muda a decisão)

1. A Hotmart é quem cuida do imposto e da nota ao comprador em: UE inteira (produto ESS = digital sem interação humana, que é o padrão), México, EUA, Austrália, Chile, Canadá, Índia, Nova Zelândia. O CRIADOR cuida em: Colômbia, Peru, Suíça, e em qualquer país não listado (Argentina, Brasil-fora, etc.). Reino Unido: as duas páginas oficiais da Hotmart se contradizem (ver seção 3) = VERIFICAR.
   Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/27142347940749 (atualizado 27/10/2026) e https://suportehotmart.zendesk.com/hc/en-us/articles/360051146712 (09/09/2026).
2. O produto vem por padrão como ESS ("Electronically supplied"). Se a oferta incluir contato humano (consultoria, WhatsApp de suporte vendido como parte do produto, aula ao vivo), a classificação vira non-ESS e o IVA da UE passa a ser do criador (Brasil precisaria do OSS não-União). Regra de ouro: manter o kit 100% automático. Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/4405973421709
3. Preço "sem imposto" (tax exclusive) onde a Hotmart cobra o imposto: o comprador paga preço + IVA no checkout. Ou seja, o €27 anunciado pode virar mais no checkout (Itália 22%). Onde o criador é responsável, o preço que você coloca é o final (tax inclusive) e o imposto sai da sua margem. Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/28274925159437. VERIFICAR no checkout real da Valigetta (ver se o total mostra IVA somado).
4. Meios locais: a Hotmart NÃO lista BLIK (Polônia), iDEAL/Wero (Holanda) nem Bizum (Espanha). Lista para a Europa: Multibanco e MB WAY (Portugal), SeQura (Espanha), BACS e PayPal Credit (Reino Unido), SEPA, Klarna Pay Now/SOFORT, Pay by Bank (Open Banking), Apple Pay, Klarna (pay later/parcelado). Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/25588460435085
5. Alternativas com BLIK/iDEAL (Stripe) exigem conta Stripe sediada num país suportado: o Brasil NÃO está na lista de BLIK nem de iDEAL. Só funcionaria com empresa/conta Stripe na UE/UK/etc. Fontes: https://docs.stripe.com/payments/blik e https://docs.stripe.com/payments/ideal
6. Taxa Hotmart (vigente, ajustada em 21/09/2026): 9,9% + 1,00 (EUR/USD/GBP) para oferta acima de 15; 9,9% + 0,10 para oferta até 15; "moeda divergente" (BR + oferta em outra moeda) pode cair na regra de USD: até US$5 = 20%, acima de 9,9% + US$1,00 (o artigo se contradiz entre 0,50 e 1,00). Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/208298448. Impacto: €19 ≈ 15% de taxa fixa+variável; €27 ≈ 13,6%. VERIFICAR no Relatório de Vendas qual regra caiu nas vendas EUR.
7. Moeda da comissão para produtor brasileiro: regra das 3 moedas (país do produtor, oferta, comprador). Produtor BR + oferta EUR = não casa => comissão em USD. Saque para conta brasileira só em USD ou EUR; transferência automática mensal a partir de US$100; manual mínimo US$/€20 + taxa de 1,99; conversão automática USD→BRL diária com spread de 1%. Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/216440207 e https://suportehotmart.zendesk.com/hc/pt-br/articles/34945044252173
8. Liberação: vendas fora de BRL ficam disponíveis 15 dias após a venda; BRL cartão 30 dias. Opção D+2 (90% em 2 dias, taxa 0,97%) é FORA do Brasil, não serve para conta BR. Fontes: https://suportehotmart.zendesk.com/hc/en-us/articles/360028608652 e https://suportehotmart.zendesk.com/hc/en-us/articles/36866116752525
9. Garantia/reembolso: mínimo 15 dias em qualquer país europeu (7/15/21/30 opções). Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/360034552751

---

## 2. Ranking 0 a 10: facilidade de vender cada país pela Hotmart (conta BR)

Nota = (imposto resolvido pela Hotmart) + (moeda/checkout local confirmado) + (meio de pagamento dominante local disponível) + (pouca fricção de saque). 10 = vender hoje sem cadastro fiscal próprio.

| Pos | País | Moeda | Nota | Imposto | Meios locais na Hotmart | Principais atritos |
|---|---|---|---|---|---|---|
| 1 | Portugal | EUR | 9 | Hotmart (UE, ESS) | Multibanco, MB WAY, SEPA, Klarna, Apple Pay | MB WAY, SEPA e Pay by Bank não entram em order bump (Multibanco entra, sem restrição listada) |
| 2 | México | MXN | 9 | Hotmart (cobra 16% IVA; criador fora do MX) | OXXO, SPEI, Mercado Pago, Kueski, híbrido cartão+OXXO | SPEI e Mercado Pago não entram em bump/funil; OXXO e híbrido OXXO: OXXO puro sem restrição, híbrido cartão+OXXO sem bump |
| 3 | Itália | EUR | 8 | Hotmart | SEPA, Klarna (3x e pay later), Pay by Bank, Apple Pay | Sem Satispay/PostePay/Bizum-like (VERIFICAR no checkout) |
| 4 | Espanha | EUR | 8 | Hotmart | SeQura, SEPA, Klarna, Pay by Bank | Sem Bizum |
| 5 | Grécia | EUR | 7 | Hotmart | SEPA, Klarna (3x), Pay by Bank | Sem método local (ex.: Viva/IRIS) |
| 5 | Eslováquia | EUR | 7 | Hotmart | SEPA, Pay by Bank | Klarna não listado para SK |
| 5 | EUA | USD | 7 | Hotmart cobra em 15 estados | Apple Pay, Venmo, PayPal Credit, Pay in 4, Klarna | Nicho precisa de adaptação (licenciamento por estado) |
| 8 | Chile | CLP | 6 | Hotmart (IVA 19%, criador fora do CL) | Servipag, MACH, Sencillito | Regra especial p/ conteúdo "educacional" (marcar corretamente) |
| 8 | Polônia | PLN (VERIFICAR) | 6 | Hotmart (UE) | Klarna pay later (PLN), cartão, PayPal, Pay by Bank | BLIK ausente, e BLIK é 58-70% do e-commerce polonês |
| 10 | Colômbia | COP | 5 | CRIADOR (IVA 19%, DIAN) | PSE, Nequi, Efecty, Bancolombia | Obrigação fiscal própria (ver seção 3) |
| 10 | Peru | PEN | 5 | CRIADOR (IGV 18%, SUNAT) | Yape, Pago Efectivo | Obrigação fiscal própria |
| 10 | Romênia | RON (VERIFICAR) | 5 | Hotmart (UE) | Klarna (RON), cartão, Pay by Bank | Moeda local não confirmada; vender em EUR perde conversão |
| 10 | Rep. Tcheca | CZK (VERIFICAR) | 5 | Hotmart (UE) | Klarna (CZK financing), cartão | Moeda local não confirmada |
| 14 | Reino Unido | GBP | 5 | CONFLITO nas páginas Hotmart (VERIFICAR); IVA 20% | BACS, PayPal Credit, Klarna | Registro HMRC sem limite se for do criador |
| 14 | Austrália | AUD (VERIFICAR) | 5 | Hotmart (GST 10%, criador fora da AU) | Cartão, PayPal, Google Pay | Meio local (POLi/Afterpay) não listado |
| 16 | Hungria | HUF (VERIFICAR) | 4 | Hotmart (UE) | Cartão, PayPal, Pay by Bank | Sem Klarna listado; HUF não confirmado |
| 17 | Argentina | ARS | 4 | Hotmart NÃO cobra; cartão cobra IVA 21%/Ganancias/IIBB do comprador | Mercado Pago (não entra em bump) | Regras cambiais BCRA, spread padronizado |

Outros países da UE em EUR (França, Alemanha, Países Baixos, Bélgica, Áustria, Irlanda, Finlândia): nota 7 (mesmo regime de Itália/Espanha; iDEAL, Bancontact e Giropay-like ausentes na lista da Hotmart).

Fontes dos meios por país: https://suportehotmart.zendesk.com/hc/en-us/articles/25588460435085 e https://suportehotmart.zendesk.com/hc/en-us/articles/25648853025037 (detalhe de cada método). Klarna por país e moeda (USD, EUR, GBP, DKK, SEK, NOK, CZK, PLN, LEU): https://suportehotmart.zendesk.com/hc/en-us/articles/38465293543309 (Klarna paga o vendedor em D+15, não aparece em bump/funil/bundle, e some se o preço passar do limite do país; PL só "pay later" até 7.000 PLN).

Moedas de venda: a Hotmart diz "22 moedas" mas NÃO lista quais (https://hotmart.com/en/payments). Uma página de ajuda mais antiga cita: BRL, EUR, ARS, USD, MXN, PEN, COP, CLP, CAD, NGN, GBP, JPY. PLN, CZK, RON, HUF e AUD não aparecem em nenhuma fonte oficial que eu tenha conseguido abrir. VERIFICAR no painel (Produtos > Preços e ofertas > Nova oferta > Moeda). Se não houver moeda local, a oferta em EUR/USD é convertida no checkout; isso aumenta recusa de cartão e o comprador vê valor em moeda estrangeira.

---

## 3. IVA/imposto e fatura por país (B2C infoproduto; B2B quando houver número de IVA)

### 3.1 Quem responde (regra Hotmart, produtor com conta no Brasil)
Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/27142347940749

| Comprador em | Quem calcula, cobra e recolhe | Observação |
|---|---|---|
| UE (27) | HOTMART, se ESS | "Hotmart é revendedora", emite autofatura e fatura de venda em nome da Hotmart BV. Non-ESS: o criador |
| México | HOTMART (criador fora do México) | 16% IVA, cobrado no checkout |
| EUA | HOTMART | Coleta imposto em 15 estados + DC (lista na página 360051146712) |
| Austrália | HOTMART (criador fora da AU) | GST 10%; empresa com ABN fica isenta no checkout |
| Chile | HOTMART (criador fora do CL) | IVA 19%; RUT de empresa isenta; "conteúdo educacional" tem tratamento especial |
| Canadá, Índia, Nova Zelândia | HOTMART (criador fora) | Não alvo agora |
| Colômbia | CRIADOR | Preço da oferta = preço final (inclui imposto) |
| Peru | CRIADOR | Idem |
| Suíça | CRIADOR | Hotmart deixou de emitir fatura em 01/11/2024 |
| Reino Unido | CONFLITO | A tabela de cenários (27142347940749, 27/10/2026) não lista o UK => criador por padrão. A página de impostos (360051146712, 09/09/2026) diz que, para ESS, a Hotmart é revendedora e emite as faturas. VERIFICAR no simulador |
| Argentina e demais | CRIADOR (padrão) | Na Argentina a Hotmart não cobra; imposto cai no cartão do comprador (IVA 21%, Ganancias 30%, IIBB) |

Simulador oficial ("Hotmart Tax Responsibility Simulator"): linkado nas duas páginas acima; rodar com país da conta BR + nicho antes de abrir cada país.

### 3.2 Alíquotas padrão e e-book (UE)
- A Hotmart diz que aplica a alíquota padrão de cada país, "exceto e-books, que na maioria dos casos têm alíquota reduzida" (página 360051146712). Se o kit (documentos editáveis + app) conta como e-book, é decisão de classificação, não automática. VERIFICAR com contador: o TJUE tratou e-book como serviço eletrônico, mas a Diretiva (UE) 2018/1713 passou a permitir alíquota reduzida para publicações eletrônicas. Kit de modelos + app provavelmente NÃO é "publicação" => alíquota padrão.
- Alíquotas reduzidas de e-book reportadas por agregador (Taxually, base TEDB de 01/07/2026): PL 5%, RO 11%, CZ 0% (isento com direito a crédito), HU 5%, ES 4%, PT 6%, FR 5,5%, NL 9%, BE 6%, AT 10%, IE 0%, SE 6%, BG 9%. Itália: 4% para livro (outra fonte diz só com ISBN; sem ISBN, 22%). Eslováquia e Grécia: sem dado claro. Fonte: https://www.taxually.com/blog/eu-vat-rates-by-product-category-2026. VERIFICAR no TEDB oficial (https://taxation-customs.ec.europa.eu/taxation/vat/vat-rates_en leva ao banco TEDB).
- Padrão (conhecimento próprio, NÃO conferido nesta rodada, VERIFICAR no TEDB): IT 22, ES 21, PT 23, PL 23, RO 21, CZ 21, SK 23, HU 27, GR 24.
- B2B com número de IVA válido: reverse charge no checkout, Hotmart não cobra.
- Se o criador (BR) tivesse que recolher IVA UE (non-ESS): precisaria do esquema não-União OSS (um registro em um Estado-membro, declaração trimestral para os 27). Fonte: https://revenue.ie/en/vat/vat-ecommerce/non-union-scheme/index.aspx. Evitar mantendo o produto ESS.

### 3.3 Reino Unido
- Gov.uk: e-books e documentos digitalizados entregues de forma automática são "serviços digitais"; empresa fora do UK com vendas sujeitas a IVA UK precisa se registrar, e a página não indica limite. Fonte: https://www.gov.uk/guidance/the-vat-rules-if-you-supply-digital-services-to-private-consumers. Se o marketplace cumprir as condições, o marketplace responde pelo IVA. Agregadores falam em "sem limite para não residentes" e £90k só para estabelecidos no UK: VERIFICAR no gov.uk.
- Decisão prática: não abrir UK até o simulador/suporte da Hotmart confirmar que ela recolhe (cenário ESS UK).

### 3.4 Austrália
- Hotmart recolhe GST 10% em vendas de criador estrangeiro a compradores na AU. ATO: não residente pode registrar voluntariamente abaixo de A$75.000 e é obrigado a partir daí; operador de plataforma eletrônica de distribuição (EDP) responde pelo GST em produtos digitais. Fontes: https://www.ato.gov.au/Business/International-tax-for-business/Non-resident-businesses-and-GST/ e Hotmart 360051146712. VERIFICAR se a Hotmart é EDP neste caso (a Hotmart já diz que recolhe).

### 3.5 Colômbia
- Criador responsável. Alíquota 19%. Fontes só de agregadores: prestador estrangeiro de serviço digital pode se registrar na DIAN e cobrar, ou o IVA é retido pelo emissor do cartão/processador; sem limite mínimo de faturamento. Fonte: https://trykintsugi.com/sales-tax-guides/latam/colombia (não oficial). VERIFICAR na DIAN (página "prestadores de servicios desde el exterior", decreto 1415/2018 citado pelas fontes). Contador Tactus tem artigo sobre mudanças nas vendas para Colômbia: https://tactus.com.br/mudancas-nas-vendas-de-infoprodutos-para-a-colombia
- Efeito: preço de oferta é final; se o IVA não for retido, sai da margem (19% sobre um ticket de baixo valor come muito).

### 3.6 Peru
- Criador responsável. IGV 18% sobre serviços digitais de não domiciliados (D. Leg. 1623; SUNAT; mecanismo de recaudação por pagadores; Resolução 000047-2026/SUNAT desde 01/07/2026 pede declaração informativa prévia). Fontes: https://elperuano.pe/noticia/249505-d-leg-no-1623-esta-es-la-norma-para-recaudar-igv-por-uso-de-servicios-digitales-en-el-peru e https://lacamara.pe/nuevas-reglas-para-el-igv-en-servicios-prestados-por-no-domiciliados/. Não achei texto oficial da SUNAT nem tratamento de e-book: VERIFICAR.

### 3.7 Chile
- Hotmart recolhe IVA 19% para criador fora do Chile. Marcar "conteúdo educacional" só se for verdade: o criador responde e a Hotmart pode pedir prova em 48 horas (https://suportehotmart.zendesk.com/hc/en-us/articles/4405973421709). Kits de documentos para profissional provavelmente NÃO são educacionais: VERIFICAR com contador antes de marcar.

### 3.8 México
- Hotmart cobra 16% (compras de residentes em sites estrangeiros); fatura CFDI emitida pela Hotmart. Já operando.

### 3.9 Argentina
- Hotmart não recolhe; imposto fica no cartão. Conversão ARS/USD com tarifa padronizada (regra BCRA). Página: https://suportehotmart.zendesk.com/hc/en-us/articles/15325356406925. Baixa prioridade.

---

## 4. Taxas, saque e alternativas

### 4.1 Hotmart (conta BR)
- Taxa: 9,9% + fixo (tabela do item 6 do resumo). Taxa fixa BRL passou a R$2,49 e a internacional a 1,00 em 21/09/2026. Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/208298448
- Imposto sobre a taxa Hotmart pode existir conforme país do criador; para criador BR não aparece na lista (UE-pessoa física, Holanda, Texas, México-empresa, Colômbia). Mesma fonte.
- Câmbio: oferta em BRL varia com o câmbio do dia; oferta em USD fica em USD para o criador e o comprador paga convertido. Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/360025069992
- Saque conta BR: BRL mínimo R$2 + R$1,99. Moedas estrangeiras: só USD ou EUR; automático mensal (3ª semana) com mínimo US$100 sem taxa Hotmart; manual mínimo US$/€20 + US$/€1,99, via conta que receba USD/EUR ou Payoneer (Payoneer: mínimo US$50, máximo US$5.000, só comissão em USD; Wise NÃO aceita). Alternativa: conversão automática diária USD→BRL com spread de 1% (mínimo US$1). Depósito de USD/EUR em banco BR aparece como RAPYD. Fontes: https://suportehotmart.zendesk.com/hc/en-us/articles/216440207, https://suportehotmart.zendesk.com/hc/en-us/articles/22224013803149, https://suportehotmart.zendesk.com/hc/pt-br/articles/34945044252173
- Hotmart Card / D+2: D+2 só fora do Brasil. Conta BR segue 15 dias fora de BRL.
- Reembolso: mínimo 15 dias na Europa; opções 7/15/21/30.
- Order bump: NÃO funcionam com bump (ou funil/bundle): Klarna, SEPA, Klarna Pay Now/SOFORT, Pay by Bank, MB WAY, SeQura, BACS, SPEI, Mercado Pago, PSE, Bancolombia, Servipag, Google Pay, Dois cartões. Funcionam sem restrição listada: cartão, PayPal, Multibanco, OXXO, Efecty, Pago Efectivo, Yape, Sencillito, Nequi (só funil/bundle restritos). Quem paga com os primeiros não vê o bump, o que reduz o ticket médio em países de método local forte (ES, MX, CO). Fonte: 25588460435085.

### 4.2 Alternativas (para quem precisar de BLIK, iDEAL, Bizum, Satispay etc.)
| Opção | Taxa | Imposto | Meios locais | Pode vender de conta BR? | Notas |
|---|---|---|---|---|---|
| Stripe (conta BR) | Cartão BR 3,99% + R$0,39; internacional +2%; Pix 1,19%; Boleto R$3,45; Adaptive Pricing a partir de 2% (https://stripe.com/en-br/pricing) | CRIADOR | BLIK e iDEAL não disponíveis (Brasil fora das listas de países sede: https://docs.stripe.com/payments/blik, https://docs.stripe.com/payments/ideal) | Sim, mas sem meios europeus | iDEAL exige site com número de registro empresarial equivalente. Moeda de apresentação EUR/PLN em conta BR: VERIFICAR |
| Stripe (conta EU/UK) | Ver https://stripe.com/pl/pricing/local-payment-methods | CRIADOR (Stripe Tax é à parte) | BLIK (PLN), iDEAL/Wero (EUR), Bancontact etc. | Precisa de entidade num país suportado (ex.: PL, IE, EE...), VERIFICAR custo/legalidade | Muda a estrutura fiscal do vendedor: contador |
| Lemon Squeezy | 5% + US$0,50 (https://www.lemonsqueezy.com/pricing); pagamento sempre em USD, câmbio mid-market | Merchant of Record: recolhe e repassa IVA/sales tax | Até 21 meios (a própria página diz 16 em outro trecho) | Brasil NÃO consta na lista de payout bancário (https://docs.lemonsqueezy.com/help/getting-started/supported-countries); PayPal payout em 200+ países (Brasil não nomeado). Acordo de migração para Stripe Managed Payments em curso (fonte secundária). VERIFICAR | Moedas de venda incluem PLN, CZK, RON, HUF, COP, CLP, PEN, ARS, GBP, AUD (https://docs.lemonsqueezy.com/help/payments/currencies). Políticas de produto (documentos/PDF) VERIFICAR |
| Paddle | MoR; taxa não conferida | MoR | iDEAL, Alipay, Google Pay (comunicado 2021) | Brasil não está na lista de países não suportados (https://www.paddle.com/help/start/account-verification/which-countries-are-supported-by-paddle) mas Paddle costuma restringir a SaaS/software e exige empresa: VERIFICAR | Pix só para itens em BRL de compradores BR |
| Payhip | Free 5%, Plus US$29/mês + 2%, Pro US$99/mês + 0% (https://www.payhip.com/pricing) + taxas Stripe/PayPal | Coleta e remete IVA UE/UK e sales tax US/CA | Cartão e PayPal; BLIK/iDEAL/Bancontact não mencionados | Payout via Stripe/PayPal: Brasil VERIFICAR | Bom para UK/UE sem OSS próprio, mas sem Klarna/SEPA locais |
| Kiwify | 8,99% + R$2,49 (fontes de blog) | Brasil | Pix/boleto | Foco BRL; vendas internacionais NÃO confirmadas | Sem uso para fora do Brasil |

Conclusão: para BR vendendo fora, a Hotmart continua a melhor opção sem abrir empresa no exterior (resolve IVA UE/MX/US/AU/CL e saca para BR). O custo é não ter BLIK/iDEAL/Bizum.

---

## 5. Lado Brasil (receber do exterior)

- Hotmart passou a ser agente do criador: o criador tem relação direta com o comprador e responde por apuração, recolhimento e nota onde a tabela diz "criador". A Hotmart emite ao criador nota/fatura só das taxas de serviço. Fonte: https://suportehotmart.zendesk.com/hc/en-us/articles/20420081457549
- Exportação de serviços (blogs contábeis, NÃO oficial): ISS e PIS/Cofins tendem a não incidir se o resultado do serviço for verificado no exterior. No Simples, a Solução de Consulta Cosit 99015/2019 diz que PIS/Cofins não incidem sobre receita de exportação de serviços, com ressalvas (https://okai.com.br/documento/2019-12-27/solucao-de-consulta-cosit-nº-99015-de-27-de-dezembro-de-2019). ISS: a isenção depende da lei do município. MEI: sem confirmação. A reforma tributária (IBS/CBS) muda o quadro. Tudo VERIFICAR com contador de infoproduto (a LC 116/2003 rege o ISS; não conferi o texto nesta rodada).
- IOF: não achei fonte confirmando alíquota zero no recebimento; um guia contábil indica desconto de câmbio e IOF no valor líquido. VERIFICAR.
- Nota fiscal de venda em moeda estrangeira: a Hotmart orienta pedir ao suporte; quem emite depende do cenário (https://suportehotmart.zendesk.com/hc/en-us/articles/9312586876557).
- Autofatura à Hotmart BV: só para criador da UE (ESS a comprador da UE) e criador mexicano pessoa física. Não se aplica a conta BR.
- Classificação do produto (ESS, educacional) é responsabilidade total do criador; a Hotmart pode exigir prova em 48 horas, sob pena de suspensão (artigo 4405973421709).

## 6. O que bloqueia ou libera cada nicho (pagamento/plataforma)

Política Hotmart de produtos não aceitos (https://suportehotmart.zendesk.com/hc/en-us/articles/31594947721485): contas de streaming, pornografia, software pirata/OEM, promessa de loteria/jogos/venda de ações e ativos, rifas/doações/caridade, drogas ilegais ou "substância cujo uso exige prescrição médica", pirâmide, discurso que desumanize por "condição mental, condição médica ou física". Conteúdo grátis online ou plágio também derruba o produto. Conta pode ser bloqueada por piracy (muitos acessos de IPs diferentes), registro em massa de produtos ou o mesmo produto repetido (https://suportehotmart.zendesk.com/hc/en-us/articles/208278538).

Implicações para os kits:
- Kits de documentos (psicólogo, dentista, nutricionista, fono, pedagogo, contador, advogado, corretor etc.) estão dentro da política, desde que a página não prometa diagnóstico/cura nem trate medicamento sob prescrição como produto. Evitar "receita de medicamento" e protocolo de injetáveis (fora do escopo).
- Mesmo kit em vários países como produtos repetidos pode virar "registro duplicado". Preferir UM produto com ofertas por moeda, ou produtos claramente distintos por idioma/nicho. VERIFICAR com o suporte Hotmart se o mesmo conteúdo traduzido conta como duplicado.
- Anti-pirataria: muitos downloads do mesmo comprador em IPs diferentes bloqueiam. Entregar por área de membros com login.
- Assinatura de app: MB WAY, Pay by Bank e Klarna não suportam assinatura; garantia só na 1ª cobrança.
- Nicho jurídico (modelos de contrato, imobiliária): não proibido pela Hotmart; risco é de conteúdo local (prática de advocacia). VERIFICAR por país.
- Stripe e outros adquirentes têm lista própria de negócios restritos (https://stripe.com/restricted-businesses, não aberta nesta rodada). VERIFICAR antes de usar Stripe em nicho de saúde.
- Meta Ads (políticas de anúncio de saúde) não foi escopo.

## 7. Ranking final por nível de prontidão (para abrir novos países)

Pronto agora (sem passo fiscal novo): Portugal 9, México 9, Itália 8, Espanha 8, Grécia 7, Eslováquia 7, outros países EUR da UE 7, EUA 7.
Pronto com ajuste leve (moeda local ou meio local faltando): Chile 6, Polônia 6 (vender em PLN se existir; senão EUR), Romênia 5, Tchéquia 5, Hungria 4.
Exige decisão fiscal antes: Colômbia 5, Peru 5, Reino Unido 5 (conflito de regra), Austrália 5, Argentina 4.
Exige empresa no exterior para entrar no método local dominante: Polônia (BLIK), Holanda (iDEAL), Bélgica (Bancontact).

Ordem sugerida de abertura (só pelo critério pagamento/fiscal): 1) Portugal e demais EUR; 2) EUA; 3) Chile; 4) Polônia em EUR/PLN; 5) Grécia/Eslováquia (EUR); 6) Romênia/Tchéquia/Hungria depois de confirmar moeda; 7) Colômbia/Peru só com contador; 8) UK/AU só após simulador; 9) Argentina por último.

## 8. Lista VERIFICAR (consolidada)

1. Moedas de oferta disponíveis hoje na Hotmart: PLN, CZK, RON, HUF, AUD, GBP, COP, CLP, PEN, ARS (a página oficial diz 22, sem lista). Conferir em Produtos > Preços e ofertas > Moeda.
2. Moeda da comissão nas vendas EUR de produtor BR (esperado USD pela regra das 3 moedas) e qual linha de taxa foi aplicada (9,9% + 0,50 ou 1,00 USD, ou 20% se ticket até US$5). Conferir no Relatório de Vendas.
3. Preço mostrado no checkout (IVA somado ao €27/€19?) na Itália e MXN no México.
4. Reino Unido: quem recolhe o IVA (Hotmart ou criador). Rodar o Simulador de Responsabilidade Fiscal.
5. Classificação do kit (documentos + app) como e-book para alíquota reduzida, e qual alíquota a Hotmart aplica em IT/ES/PT/PL. Conferir TEDB.
6. Alíquotas padrão IT, ES, PT, PL, RO, CZ, SK, HU, GR no TEDB.
7. Colômbia: registro DIAN ou retenção do emissor do cartão; Peru: SUNAT; Austrália: se a Hotmart atua como EDP; Chile: marcar "educacional" ou não.
8. Isenção de ISS/PIS/Cofins/IOF na exportação (MEI, Simples, município), nota fiscal de exportação.
9. Stripe conta BR: moedas EUR/PLN de apresentação; Stripe restricted businesses para nicho saúde.
10. Lemon Squeezy/Paddle/Payhip: elegibilidade de vendedor brasileiro e política de produto (documentos/PDF); Lemon Squeezy via Stripe Managed Payments.
11. Meios locais ausentes na Hotmart (BLIK, iDEAL/Wero, Bizum, Bancontact): perguntar ao suporte se há roadmap e se o checkout de fato oculta.
12. Valor de "22 moedas" e "30+ métodos" é marketing; o que vale é o que o checkout mostra por país (teste com VPN/aba anônima, sem comprar).
13. Mesmo conteúdo traduzido registrado como produto separado: risco de bloqueio por duplicidade.

## 9. Fontes principais
- Hotmart Central de Ajuda (artigos 27142347940749, 360051146712, 4405973421709, 28274925159437, 20420081457549, 25588460435085, 25648853025037, 208298448, 216440207, 22224013803149, 34945044252173, 360028608652, 36866116752525, 360034552751, 38465293543309, 31594947721485, 208278538, 360025069992, 9312586876557): base https://suportehotmart.zendesk.com/hc/en-us/articles/<id>
- Hotmart marketing: https://hotmart.com/pt-br/internacionalizacao e https://hotmart.com/en/payments
- Stripe: https://stripe.com/en-br/pricing, https://docs.stripe.com/payments/blik, https://docs.stripe.com/payments/ideal
- Lemon Squeezy: https://www.lemonsqueezy.com/pricing, https://docs.lemonsqueezy.com/help/getting-started/supported-countries, https://docs.lemonsqueezy.com/help/payments/currencies
- Payhip: https://www.payhip.com/pricing; Paddle: https://www.paddle.com/help/start/account-verification/which-countries-are-supported-by-paddle
- Autoridades: https://www.gov.uk/guidance/the-vat-rules-if-you-supply-digital-services-to-private-consumers, https://www.ato.gov.au/Business/International-tax-for-business/Non-resident-businesses-and-GST/, https://revenue.ie/en/vat/vat-ecommerce/non-union-scheme/index.aspx, https://taxation-customs.ec.europa.eu/taxation/vat/vat-rates_en
- Agregadores (não oficiais): Taxually (alíquotas e-book), Kintsugi (Colômbia), El Peruano/La Cámara (Peru), Payabl/NBP (BLIK 58-70%).
