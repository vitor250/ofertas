# Nosso funil: o que converte (diagnóstico 30/10/2026)

> Status: CONCLUÍDO (gravado aos poucos em 30/10/2026).

## Resumo
- **O que mais converte hoje (lista do prompt): Fono infantil** (R$12,5 mil, 475 compras atribuídas, ROAS 1,85, CPA R$26), depois **Consultora** (ROAS 2,03, página que mais converte) e **Maleta do Dentista BR** (ROAS 1,53). Nenhuma chega ao campeão da casa, a Maleta do Vistoriador BR (ROAS 2,53, CPA R$22,7), que não estava na lista.
- **Gargalos:** dentista = checkout (só 39% dos checkouts compram, contra 58–63% nas outras ofertas no mesmo checkout Wiapy); consultora e psicólogo infantil = criativo caro (CPC R$2,5–4,0); advogado e MX = página (só 57% dos cliques viram visita); fono = criativos cansando e escalas duplicadas piorando.
- **Escala por duplicação ("escala ..." com 1 anúncio) piora o CPA em quase todas as ofertas.**
- **Valigetta IT** começou à 00:08 de hoje (R$0,53): sem dados; antes de gastar, corrigir título vazio, rever o conjunto "RENTRI" (gancho descartado nas notas de 28/10) e o pixel compartilhado com o dentista BR.
- **Maletín MX**: R$118, 3 compras; criativo forte (mx04 "niños" com CTR 11,2%), página e pixel (sem servidor) fracos.
- Em todas as ofertas os anúncios variam só o vídeo: texto e título são iguais. O 3×3×3 da seção 5 abre também texto e título.

## Avisos de método e ambiente
- **Somente leitura.** Usadas apenas ferramentas de consulta do conector Meta: `ads_get_ad_accounts`, `ads_get_field_context`, `ads_get_ad_entities` (campanha, conjunto e anúncio), `ads_get_creatives` (texto dos anúncios), `ads_get_datasets`, `ads_get_dataset_quality` e `ads_get_dataset_stats` (pixels). Nada foi criado, editado, ativado, pausado ou excluído.
- Os relatórios anteriores citados nas instruções (v1 de 29/10) e os arquivos do Desktop do usuário **não estavam acessíveis** neste ambiente (container na nuvem).
- **Vendas citadas:** as únicas "vendas registradas nos arquivos e memórias" acessíveis aqui são as das notas em `pesquisas-nichos/notas/` (`fila-ofertas.md`, `meta-varredura-low-ticket.md`, `pesquisa-europa.md`). Essas notas **não registram nenhuma venda nossa** (nem quantidade nem faturamento). Toda contagem de compra abaixo vem do pixel/atribuição da Meta (eventos `purchase` dentro da Meta), não da Wiapy (checkout das ofertas BR) nem da Hotmart (MX e IT); por isso cada número de compra é "compra atribuída pela Meta" e precisa ser conferido na plataforma de pagamento (VERIFICAR).
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). WebFetch/curl para sites externos bloqueado pela política de rede: as páginas de vendas e checkouts NÃO foram abertas.

## 1. Contas e estrutura

Consulta feita em 30/10/2026 (madrugada, horário de Brasília) pelo conector Meta, só leitura. As duas contas são da empresa VH Inova Digital, em BRL, ativas e consultáveis.

| Conta | ID | O que roda nela (últimos 90 dias) |
|---|---|---|
| Conta 03 | 623752106927686 | Histórico grande de PB Kids (ES/IT), Orações, Presetão (todas pausadas). **Novas:** Valigetta del Dentista IT (criada 30/10 00:08), Maletín del Psicólogo MX (v1.0 de 29/10, pausada; v1.0 de 30/10, ativa), "GC" Espanha (pixel "concursos latam"; fora da lista do prompt) |
| conta 05 | 574561479021139 | Maleta do Vistoriador BR e ES, Painel Pro (pixel do vistoriador), Maleta do Dentista BR, Fono infantil, Psicólogo infantil, Psicopedagogia, Consultora (alimentos), Maleta do Advogado (previdenciário), Kit "pronta" (pixel "construa certo"), bolo, orações e outros testes |

**Como cada oferta foi identificada** (nome da campanha + pixel de otimização do conjunto + país do público):

| Oferta (prompt) | Conta | Campanhas (padrão do nome) | Pixel (dataset) | País |
|---|---|---|---|---|
| Valigetta del Dentista IT | 03 | `valigetta dentista IT teste abo 1.0 - 30.10` (5 conjuntos: 01 asl entra nello studio, 02 rentri, 03 consenso, 04 lazio, 05 studio condiviso; R$60/dia cada) | **odonto** 1129138929579397 (o MESMO do dentista BR) | IT |
| Maletín del Psicólogo MX | 03 | `maletin psicologo mx teste abo 1.0 - 29.10` (pausada) e `- 30.10` (ativa); conjuntos mx01 expediente, mx02 nota de sesión, mx03 documentos, mx04 niños, mx05 geral 200; R$40/dia cada | psico latam 1211112451577080 | MX |
| Maleta do Dentista BR | 05 | `dentista teste abo 1.0 - simulado 22.10`, `dentista teste abo 1.2 - variacoes do 01 26.10`, `maleta dentista teste abo 1.3 - quadro hooks 29.10`, `escala dentista 24.10/25.10/26.10`, `escala dentista 13/14 ... 28.10` | odonto 1129138929579397 | BR |
| Consultora BR | 05 | `consultora alimentos teste abo 1.0 - 26.10`, `... 1.1 - variacoes 29.10`, `escala consultora CN1/CN5 28.10`, `escala consultora cbo 5 criativos 29.10` | consultora nutri 1120215370498026 | BR |
| Advogado | 05 | `maleta advogado prev teste abo 1.0 - 28.10`, `escala advogado 01/02 ... cbo - 30.10` | advogado 1136211688855218 | BR |
| Fono | 05 | `fono infantil teste abo 1.3.x/1.5.x/1.6`, `escala fono NN`, `escala isolado 28 gagueira`, `escala isolado 31 respiracao oral`, `escala validados fono` | psicopedagogia 1151947373936212 | BR |
| Psicólogo Infantil | 05 | `psicologo infantil teste abo 1.1 21.10` (pausada) | psicopedagogia 1151947373936212 | BR |
| (referência) Maleta do Vistoriador BR | 05 | `maleta NN`, `testes abo maleta 1.x.1`, `escala maleta ...` | maleta do vistoriador 1126831149850854 | BR |
| (referência) Maleta do Vistoriador ES | 05 | `maleta espanhol NN` (todas pausadas) | maleta do vistoriador espanhol 1056348527382333 | CL, CO, MX, PE |
| (referência) Painel Pro | 05 | `painel pro NN`, `teste criativos abo painel pro NN` | maleta do vistoriador (mesmo pixel) | BR |

Observação: "maleta" sem complemento na conta 05 é a **Maleta do Vistoriador**, não a do dentista (o pixel se chama "maleta do vistoriador" e os anúncios falam de vistoria/laudo). A Maleta do Dentista BR usa o pixel "odonto", criado em 21/10.

Configuração comum: objetivo Vendas (OUTCOME_SALES), otimização para Compra (PURCHASE) no pixel, ABO nos testes, público aberto (Advantage+ audiência, 18–65, só o país), todas as posições. Atribuição: 7 dias clique (Valigetta, MX, Consultora, Advogado e parte dos outros) ou 1 dia visualização + 7 dias clique (+ "1d_ev") nos demais. **As contagens de compra de campanhas com atribuições diferentes não são 100% comparáveis.**

## 2. Métricas por oferta (desde criação, 14 dias, 7 dias)

Fonte: `ads_get_ad_entities` no nível de anúncio, somado por oferta. Janelas da Meta: "desde criação" = `maximum` (inclui hoje, 30/10); "14 dias" = `last_14d` (16/10–29/10); "7 dias" = `last_7d` (23/10–29/10). Valores em R$ (moeda das contas). Compras = compras atribuídas pela Meta (pixel). CTR = CTR de link; CPC = custo por clique no link; Visitas = visualizações da página de destino (LPV); Checkout = InitiateCheckout. Frequência = média ponderada aproximada. Ticket = valor de compra ÷ compras (inclui order bumps, se o checkout envia o valor total; VERIFICAR).

### 2.1 Ofertas do prompt

| Oferta | Janela | Gasto | CTR | CPC | CPM | Freq. | Cliques | Visitas (% dos cliques) | Checkout (% das visitas) | Compras (% dos checkouts) | CPA | ROAS | Ticket |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Valigetta Dentista IT** (desde 30/10 00:08) | criação | 0,53 | — | — | — (7 impressões) | 1,2 | 0 | 0 | 0 | 0 | — | — | — |
| **Maletín Psicólogo MX** (v29.10 + v30.10, desde 28/10) | criação ≈ 7d ≈ 14d | 118,28 | 5,95% | 0,95 | 56,8 | 1,36 | 124 | 71 (57%) | 7 (10%) | 3 (43%) | 39,43 | 1,17 | 46,2 |
| **Maleta do Dentista BR** (desde 21/10) | criação | 3.512,70 | 2,64% | 1,59 | 42,1 | 1,25 | 2.205 | 2.059 (93%) | 244 (11,9%) | 96 (39%) | 36,59 | 1,53 | 56,1 |
| | 14d | 3.506,87 | 2,64% | 1,59 | 42,1 | 1,25 | 2.202 | 2.055 (93%) | 244 (11,9%) | 96 (39%) | 36,53 | 1,54 | 56,1 |
| | 7d | 3.276,38 | 2,58% | 1,64 | 42,3 | 1,22 | 1.996 | 1.868 (94%) | 222 (11,9%) | 87 (39%) | 37,66 | 1,49 | 56,1 |
| **Consultora BR** (desde 25/10) | criação = 14d ≈ 7d | 1.146,80 | 1,54% | 2,54 | 39,3 | 1,32 | 451 | 369 (82%) | 74 (20,1%) | 36 (49%) | 31,86 | 2,03 | 64,6 |
| **Advogado** (prev., desde 27/10) | criação ≈ 14d ≈ 7d | 378,68 | 3,98% | 1,14 | 45,5 | 1,22 | 331 | 188 (**57%**) | 24 (12,8%) | 9 (38%) | 42,08 | 1,34 | 56,4 |
| **Fono infantil** (desde 07/10) | criação | 12.490,63 | 2,01% | 1,97 | 39,6 | 1,42 | 6.351 | 5.143 (81%) | 756 (14,7%) | 475 (63%) | 26,30 | 1,85 | 48,7 |
| | 14d | 9.372,76 | 2,04% | 1,90 | 38,7 | 1,35 | 4.934 | 3.943 (80%) | 553 (14,0%) | 340 (61%) | 27,57 | 1,77 | 48,9 |
| | 7d | 3.381,12 | 2,14% | 1,65 | 35,3 | 1,28 | 2.051 | 1.680 (82%) | 209 (12,4%) | 111 (53%) | 30,46 | 1,55 | 47,1 |
| **Psicólogo Infantil** (20/10, pausada) | criação = 14d | 348,67 | 1,52% | 4,01 | 61,0 | 1,28 | 87 | 80 (92%) | 17 (21,2%) | 12 (71%) | 29,06 | 1,41 | 41,0 |
| | 7d | 112,67 | 1,81% | 4,17 | 75,7 | 1,17 | 27 | 27 (100%) | 8 (29,6%) | 2 (25%) | 56,33 | 0,99 | 55,9 |

Maletín MX por versão: v29.10 (pausada) gastou R$110,20, 1.908 impressões, 114 cliques (CTR 5,97%), 65 visitas, 5 checkouts, 2 compras (R$46,26 cada), CPA R$55,10, ROAS 0,84. v30.10 (ativa, poucas horas): R$8,08, 10 cliques, 6 visitas, 2 checkouts, 1 compra (R$46,12).

Valigetta IT: no momento da consulta só 7 impressões e R$0,53; dois anúncios ainda sem entrega ("01 - asl entra nello studio", "02 - rentri", "05 - studio condiviso" com 0 impressões). Nada a concluir antes de ~R$150–300 por conjunto.

### 2.2 Referências internas (o que já escala nas mesmas contas)

| Oferta | Janela | Gasto | CTR | CPM | Visitas/cliques | Checkout/visitas | Compras/checkouts | CPA | ROAS | Ticket |
|---|---|---|---|---|---|---|---|---|---|---|
| Maleta do Vistoriador BR (desde 31/08) | criação | 52.375,30 | 2,21% | 31,4 | 92% | 11,9% | 58% | 22,69 | 2,53 | 57,4 |
| | 14d | 6.522,88 | 1,65% | 30,9 | 88% | 13,8% | 58% | 26,52 | 2,36 | 62,6 |
| | 7d | 3.089,42 | 1,71% | 30,2 | 87% | 12,0% | 52% | 32,87 | 1,89 | 62,1 |
| Painel Pro (vistoriador) | criação | 5.754,62 | 1,72% | 41,5 | 85% | 19,1% | 56% | 26,64 | 2,46 | 65,5 |
| | 7d | 1.336,71 | 1,53% | 33,3 | 83% | 15,2% | 52% | 33,42 | 1,88 | 62,8 |
| Maleta do Vistoriador ES (CL/CO/MX/PE; 24/09–~16/10) | criação | 9.489,83 | 2,33% | 28,8 | 85% | 16,3% | **30%** | 29,47 | 1,58 | 46,5 |
| Kit "pronta" (pixel construa certo) | criação | 7.422,16 | 2,44% | 21,2 | 92% | 7,2% | 86% | 15,30 | 2,13 | 32,6 |

Leitura rápida: a régua interna de "oferta que escala" é o Vistoriador BR (CPA R$19–23 nas campanhas campeãs e ROAS 2,5–3,5 desde criação). Nenhuma oferta da lista do prompt está nesse patamar ainda; a mais perto é a Consultora (ROAS 2,03, mas com só R$1,1 mil gastos). Todas as ofertas BR, inclusive o Vistoriador, pioram na janela de 7 dias (ROAS 7d < 14d < criação), o que sugere queda geral de eficiência na conta 05 nesta semana (VERIFICAR: leilão de fim de mês, saturação dos públicos, ou atraso de atribuição das compras mais recentes).

## 3. Campeões e perdedores (anúncios)

Achado de estrutura: **em cada oferta, todos os anúncios usam o MESMO texto (body) e o MESMO título; só muda o vídeo** (o nome do anúncio = gancho do vídeo). Então "campeão/perdedor" abaixo = gancho do vídeo. Os testes até agora são "N vídeos × 1 texto × 1 título". Números "desde criação"; CTR = CTR de link.

### 3.1 Maleta do Dentista BR (texto único: "Se a vigilância chegasse hoje, a pasta da RDC 1.002 do seu consultório passaria?" + Simulado de Inspeção; título "+115 recursos prontos para a pasta da RDC 1.002")
| | Anúncio (gancho do vídeo) | Campanha | Status | Gasto | CTR | Compras | CPA | ROAS |
|---|---|---|---|---|---|---|---|---|
| CAMPEÃO | 01 - fiscal chegou | escala dentista 24.10 | ativo | 1.087,98 | 2,48% | 37 | 29,4 | 1,88 |
| CAMPEÃO | 01 - fiscal chegou | teste 1.0 simulado 22.10 | ativo | 276,39 | 3,09% | 9 | 30,7 | 1,80 |
| bom | 05 - abrir consultório | teste 1.0 | ativo | 280,05 | 3,34% | 9 | 31,1 | 1,63 |
| bom | 14 - 01 V2 cadeira | teste 1.2 | ativo | 145,90 | 2,06% | 4 | 36,5 | 2,27 |
| sinal (2 dias) | 19 - H5-V2 fiscal pediu cadeira / 20 - ângulo novo 17 itens | teste 1.3 quadro hooks | ativos | ~41–43 cada | 2,5–3,0% | 2 cada | ~20–21 | 2,2–2,3 |
| médio | 02 - prazo dezembro | teste 1.0 | ativo | 284,19 | 2,87% | 8 | 35,5 | 1,48 |
| PERDEDOR | 14 - 01 V2 cadeira (escala isolada) | escala dentista 14 cadeira 28.10 | ativo | 261,32 | 2,40% | 5 | 52,3 | 0,95 |
| PERDEDOR | 04 - documentos do zero | teste 1.0 | conjunto pausado | 185,61 | 2,97% | 3 | 61,9 | 1,10 (7d 0,44) |
| PERDEDOR | 03 - fita zebrada | teste 1.0 | conjunto pausado | 90,42 | 2,82% | 1 | 90,4 | 0,52 |
| PERDEDOR | 15 - ângulo novo equipe sem você | teste 1.2 | ativo | 144,60 | 3,00% (CPM 60) | 3 | 48,2 | 1,11 |
| PERDEDOR | 12 - 01 H3 se entrasse agora | teste 1.2 | pausado | 31,70 | 1,12% | 0 | — | 0 |
| PERDEDOR | escala 25.10 (05 abrir consultório) / escala 26.10 (02 prazo dezembro) / escala 13 fiscal na recepção | escalas | pausadas | 116,81 / 64,01 / 43,23 | 2,2–2,8% | 2 / 1 / 0 | 58 / 64 / — | 0,80 / 0,97 / 0 |

### 3.2 Consultora BR (texto único RDC 216 "pare de montar checklist do zero"; título "Maleta da Consultora de Alimentos: tudo pronto pra RDC 216")
| | Anúncio | Gasto | CTR | CPM | Compras | CPA | ROAS |
|---|---|---|---|---|---|---|---|
| CAMPEÃO (amostra pequena) | 23 - CN5 V2 chef tablet (teste 1.1, ativo) | 48,76 | 1,72% | 39,9 | 4 | 12,2 | 5,97 |
| CAMPEÃO | CN5 (teste 1.0, ativo) | 147,68 | 1,47% | 36,8 | 5 | 29,5 | 2,55 |
| CAMPEÃO | CN3 (teste 1.0, ativo) | 146,95 | 1,95% | 42,0 | 6 | 24,5 | 2,47 |
| bom | CN4 (teste 1.0, ativo) | 148,95 | 1,32% | 26,1 | 6 | 24,8 | 2,30 |
| bom | CN2 (teste 1.0, ativo) | 149,41 | 1,86% | 48,8 | 5 | 29,9 | 2,18 |
| fraco | CN1 (teste 1.0, ativo; CPM R$77, CPC R$3,62) | 152,02 | 2,13% | 77,0 | 4 | 38,0 | 1,76 |
| PERDEDOR | 25 - ângulo novo CVS 3 (ativo) | 34,68 | 0,87% | 43,1 | 0 | — | 0 |
| PERDEDOR | escala consultora CN5 28.10 (pausada) | 85,39 | 1,11% | 30,6 | 1 | 85,4 | 0,55 |
| PERDEDOR | escala consultora CN1 28.10 (pausada) | 33,38 | 1,43% | 79,7 | 0 | — | 0 |

### 3.3 Advogado previdenciário (texto único "quanto do honorário... entra no seu caixa?" + Painel do Caso; título "+200 recursos para o escritório previdenciário")
| | Anúncio | Gasto | CTR | CPC | Visitas | Compras | CPA | ROAS |
|---|---|---|---|---|---|---|---|---|
| CAMPEÃO | 01 - honorário raio-x | 89,17 | 5,67% | 0,78 | 63 | 3 | 29,7 | 1,81 |
| bom | 05 - documentos do zero | 77,43 | 4,69% | 1,11 | 37 | 2 | 38,7 | 1,71 |
| médio | 02 - exigência 30 dias | 75,08 | 3,86% | 1,12 | 37 | 2 | 37,5 | 1,42 |
| fraco | 04 - rpv destaque | 90,28 | 1,99% | 2,01 | 40 | 2 | 45,1 | 1,18 |
| PERDEDOR | 03 - link do cliente (conjunto pausado) | 44,36 | 4,57% | 1,30 | 11 (≈32% dos cliques) | 0 | — | 0 |

Já existem 2 campanhas "escala advogado 01/02 ... cbo - 30.10" (ativas, R$2,36 gastos até a consulta).

### 3.4 Fono infantil (texto único "Ainda escreve relatório do zero?"; título "+200 recursos prontos para fono infantil")
| | Anúncio / conjunto | Campanha | Gasto | CTR | Compras | CPA | ROAS |
|---|---|---|---|---|---|---|---|
| CAMPEÃO | 04 | teste 1.5.4 | 412,73 | 2,22% | 25 | 16,5 | 2,80 |
| CAMPEÃO | 02 | teste 1.3.1 nova variação | 340,46 | 1,39% | 21 | 16,2 | 2,63 |
| CAMPEÃO | 06 | teste 1.5.2 (ativo) + escala fono 06 | 671,14 + 770,42 | 2,51% / 1,52% | 32 + 33 | 21,0 / 23,3 | 2,30 / 2,19 |
| CAMPEÃO | 08 | teste 1.5.2 + escala fono 08 | 536,74 + 1.094,34 | 2,27% / 2,26% | 26 + 42 | 20,6 / 26,1 | 2,51 / 1,94 |
| CAMPEÃO | 0 (conj. 03) | teste 1.5.1 | 580,00 | 2,67% | 30 | 19,3 | 2,38 |
| CAMPEÃO (ativo) | 01 (conj. 04) | teste 20.10 | 360,86 | 2,42% | 19 | 19,0 | 2,48 (7d 2,55) |
| CAMPEÃO (mapas) | 05 - 31 respiração oral / 02 - 28 gagueira | mapas 21.10 | 263,06 / 338,18 | 1,73% / 1,96% | 14 / 16 | 18,8 / 21,1 | 2,69 / 2,41 |
| sinal (3 dias) | 42 - 34 V2 espátula (ativo) | teste 1.6 | 85,03 | 1,62% (CPM 19) | 6 | 14,2 | 3,38 |
| médio (ativos) | 01 - 32 troca o R / 03 - 34 língua presa | mapas 23.10 | 258,11 / 255,65 | 3,01% / 2,01% | 8 / 8 | 32 | 1,41 / 1,63 |
| PERDEDOR | criativos 09, 12, 13 (CTR 0,41–0,48%) + 10, 11 | teste 1.5.3 | 89,49 total | 0,4–2,0% | 0 | — | 0 |
| PERDEDOR | 35 língua empurra, 36 chupeta, 37 ceceio, 38 voz rouca, 39 só come arroz | mapas 26.10 | 122,32 total | 0,5–1,3% | 1 | 122 | 0,15 |
| PERDEDOR | 28 gagueira isolado | escala isolado 23.10 | 454,40 | 1,93% | 12 | 37,9 | 1,20 |
| PERDEDOR | 01 — Cópia / validados | escala fono 12 / escala validados 23.10 / escala validados fono infantil | 145,84 / 63,41 / 314,45 | — | 2 / 1 / 8 | 73 / 63 / 39 | 0,51 / 0,58 / 1,32 |
| PERDEDOR | 02 (CTR 4,6% mas CPM R$98) | teste 1.5.5 | 238,47 | 4,60% | 4 | 59,6 | 1,03 |

### 3.5 Psicólogo Infantil (pausado; texto "A escola pediu relatório e você vai escrever do zero de novo?"; título "+200 recursos prontos para o psicólogo infantil")
| | Anúncio | Gasto | CTR | CPC | Compras | CPA | ROAS |
|---|---|---|---|---|---|---|---|
| CAMPEÃO | 03 - app primeiro | 153,31 | 2,16% | 3,48 | 6 | 25,6 | 1,76 |
| bom | 02 - atividade lúdica véspera | 120,40 | 1,18% | 5,02 | 5 | 24,1 | 1,54 |
| PERDEDOR | 05 - trava na hora de escrever | 26,03 | 0,52% | 13,02 | 0 | — | 0 |
| PERDEDOR | 01 - escola pediu relatório | 28,04 | 1,50% | 2,34 | 0 | — | 0 |
| inconclusivo | 04 - dívida de horas | 20,89 | 1,06% | 4,18 | 1 | 20,9 | 1,77 |

O pixel (psicopedagogia) registrou acessos novos em `maletadopsicologoinfantil.site` na noite de 29/10, sinal de que a página está sendo mexida/relançada (VERIFICAR).

### 3.6 Maletín del Psicólogo MX (cada vídeo com texto e título próprios)
| | Anúncio | Gasto | CTR | CPC | Visitas | Compras | Observação |
|---|---|---|---|---|---|---|---|
| CAMPEÃO (sinal) | mx04 niños ("100 actividades ilustradas con Lia y Nino") v29.10 | 23,23 | **11,21%** | 0,32 | 37 | 1 | maior CTR de todas as contas analisadas |
| CAMPEÃO (sinal) | mx02 nota de sesión v29.10 | 22,03 | 6,07% | 1,16 | 11 | 1 | |
| sinal | mx01 expediente (NOM-004, semáforo) v30.10 | 3,38 | 9,6% | 0,42 | 5 | 1 | na v29.10: R$26,12, CTR 3,5%, 0 compras |
| PERDEDOR | mx03 documentos ("Tus formatos de consulta, listos en Word") v29.10 | 16,49 | **0,42%** | 16,49 | 0 | 0 | |
| fraco | mx05 geral 200 v29.10 | 22,33 | 2,49% | 2,48 | 7 | 0 | |

Compras com valor R$46,12–46,26 cada (preço em MXN: VERIFICAR na Hotmart).

### 3.7 Valigetta del Dentista IT
Sem dados (R$0,53 e 7 impressões). Os 5 vídeos usam o mesmo texto ("App con il semaforo... Modelli pronti in Word e PDF... +115 risorse") e **o campo título está vazio em todos**. Ganchos: 01 "Se oggi entrasse l'ASL nel tuo studio...", 02 "RENTRI: il tuo studio deve esserci o no?", 03 consenso informato / Legge 219, 04 Lazio "fino al 7 febbraio 2027", 05 studio condiviso.

### 3.8 O que o campeão da casa (Vistoriador BR) faz diferente
- Criativo campeão (R$9.576, 501 compras, CPA R$19,1, ROAS 3,02): título "Vistoria sem esquecer nada", texto curto de **produtividade** ("Chega de perder tempo montando planilha, checklist e relatório separados... Você personaliza e leva pra campo no mesmo dia"), CTA "Ver detalhes". Não usa medo de fiscalização.
- As ofertas novas (dentista, consultora, fono) usam textos longos com lista de itens e, no dentista, medo de fiscalização. Vale testar o texto curto de produtividade como uma das 3 variações de texto (ver seção 5).
- **Escala por duplicação não funciona na conta 05:** campanhas com "escala" no nome tiveram ROAS 1,58 (fono) contra 1,98 dos testes; 0,88 contra 2,26 (consultora); 0,15 contra 2,55 (vistoriador); 1,56 contra 1,51 (dentista, empate só por causa da "escala dentista 24.10"). As duas únicas escalas boas (escala fono 06 e 08) eram cópias de conjuntos com 3–4 dias de dados.

## 4. Diagnóstico do gargalo por oferta

**Régua interna** (Vistoriador BR, a oferta que já escalou nas mesmas contas, mesmo checkout Wiapy): CTR ≈ 2,2%; visitas ≥ 90% dos cliques; checkout ≈ 12% das visitas; compra ≈ 58% dos checkouts; CPA ≈ R$19–23; ROAS 2,5–3,0. A etapa que mais se afasta da régua é o gargalo.

**Checkout e pixel por oferta** (lido nas estatísticas do pixel, por domínio): todas as ofertas BR (dentista, consultora, advogado, fono, psicólogo infantil, vistoriador) usam páginas próprias `.site` (maletadodentista.site, maletadaconsultora.site, maletadoadvogado.site, maletadafonoinfantil.site, maletadopsicologoinfantil.site, maletadovistoriador.site) e checkout **pay.wiapy.com**. MX usa maletindelpsicologo.site + **pay.hotmart.com**. IT usa valigettadeldentista.site + **pay.hotmart.com**.

| Oferta | Criativo | Página | Checkout | Preço/ticket | Pixel | **Gargalo principal** |
|---|---|---|---|---|---|---|
| Maleta do Dentista BR | OK (CTR 2,6–3,3%, CPC R$1,59) | OK (93% dos cliques viram visita; 11,9% das visitas iniciam checkout = régua) | **Fraco: só 39% dos checkouts viram compra** (régua 58%; fono 63%; mesmo checkout Wiapy) | ticket R$56 (≈ vistoriador R$57–62) | odonto, EMQ 6,1 (Compra só com IP/navegador/fbp/fbc, sem e-mail/telefone); **desde 29/10 o mesmo pixel recebe também a Valigetta IT (Hotmart)** | **CHECKOUT** (abandono). Depois: escala (só "fiscal chegou" segura CPA < R$30). |
| Consultora BR | **Fraco: CTR 1,54%, CPC R$2,54, CPM R$39** (pior CPC entre as ofertas com volume) | **Ótima: 20% das visitas iniciam checkout** (melhor do grupo) | OK (49–54%) | ticket R$64,6 (o maior) | consultora nutri | **CRIATIVO** (custo para trazer a visita). Escala duplicada falhou (ROAS 0,88). |
| Advogado (prev.) | **Ótimo: CTR 3,98%, CPC R$1,14** | **Fraca: só 57% dos cliques viram visita** (os outros ficam em 80–94%) | fraco (38%), amostra pequena (24 checkouts) | ticket R$56 | advogado | **PÁGINA** (carregamento/redirecionamento: perde 4 em 10 cliques antes de abrir). VERIFICAR velocidade no celular. |
| Fono infantil | médio (CTR 2,0%, CPC R$1,97), **cansando**: ROAS criação 1,85 → 14d 1,77 → 7d 1,55, com frequência baixa (1,3) | médio (81% dos cliques viram visita; 14,7% iniciam checkout) | **ótimo (63%)** | ticket R$48,7 | psicopedagogia (compartilhado com psicopedagogia e psicólogo infantil) | **CRIATIVO/ESCALA**: os vídeos campeões de 10–15/10 estão pausados e as escalas duplicadas pioraram; os "mapas" novos de 26/10 falharam. Secundário: perda de 19% entre clique e visita. |
| Psicólogo Infantil | **Fraco: CTR 1,52%, CPC R$4,01, CPM R$61** (o mais caro) | ótima (21% iniciam checkout) | ótimo (71%) | ticket R$41 | psicopedagogia | **CRIATIVO/CPM**. Página e checkout convertem; falta trazer clique barato. |
| Maletín Psicólogo MX | ótimo (CTR 6,0%; mx04 niños 11,2%) mas **CPM R$58** (alto para México: VERIFICAR) | **Fraca: 57% dos cliques viram visita**; 10% das visitas iniciam checkout | 3 de 7 checkouts compraram | ticket R$46 | psico latam: **só eventos de navegador (sem servidor/CAPI), sem nota de qualidade** | **PÁGINA + PIXEL** (e amostra mínima: R$118, 3 compras). Prioridade: velocidade de maletindelpsicologo.site e ligar a integração de servidor da Hotmart com o pixel. |
| Valigetta IT | sem dados; **título vazio** nos 5 anúncios | sem dados | Hotmart | €27/€19 segundo as notas (VERIFICAR na página) | **odonto, o mesmo do dentista BR** | **CONFIGURAÇÃO** antes de gastar: pixel compartilhado com o BR; conjunto "02 - rentri" usa um gancho que a própria pesquisa de 28/10 descartou (ver VERIFICAR); 5 conjuntos × R$60/dia = R$300/dia sem dado de compra. |

**Causas que valem para todas:**
1. **Escala por duplicação** (campanhas "escala ..." com 1 anúncio) quase sempre piora o CPA em relação ao teste de origem (seção 3.8). O que escalou de verdade (Vistoriador "maleta 06 - video — Cópia", R$9,6 mil, ROAS 3,0) foi uma cópia de campanha inteira com o vídeo campeão, não um anúncio isolado em CBO.
2. **Queda de 7 dias em todas as ofertas BR**, inclusive no Vistoriador (ROAS 2,36 em 14d → 1,89 em 7d), com frequência baixa (1,2–1,3). Não é saturação de público; pode ser leilão (fim de mês), criativos envelhecendo ou atraso de atribuição. VERIFICAR com as vendas da Wiapy por dia.
3. **Texto único por oferta**: só o vídeo varia. Não sabemos se o texto/título ajudam ou atrapalham; o campeão da casa usa texto curto de produtividade.
4. **Pixels compartilhados** entre ofertas diferentes (odonto: BR + IT; psicopedagogia: fono + psicopedagogia + psicólogo infantil; maleta do vistoriador: vistoriador + Painel Pro + "maletadoinspetorpredial.site"). Para otimização por Compra, o pixel aprende um comprador misto. O caso mais grave é BR + IT no mesmo pixel (país, idioma, moeda e checkout diferentes).
5. **Compras = atribuição da Meta**, não vendas confirmadas. Nenhuma venda nossa está registrada nas notas disponíveis; ROAS de equilíbrio depende das taxas Wiapy/Hotmart e impostos (VERIFICAR). Com taxa total de ~10–15%, o equilíbrio fica em ROAS ≈ 1,1–1,2; nessa hipótese, dentista (1,5), fono (1,85), consultora (2,0) e advogado (1,3) estariam acima, e MX (1,17) no limite. Hipótese, não dado.

## 5. Variações 3×3×3 propostas

Proposta, nada foi criado. Formato: **3 ganchos de vídeo (primeiros 3 s) × 3 textos × 3 títulos** por oferta. Montagem sugerida: 3 conjuntos ABO (1 por gancho, orçamento igual), cada um com 1 anúncio usando as 3 opções de texto e as 3 de título (o Gerenciador permite várias opções de texto por anúncio), 3–4 dias, corte por CPA. Os ganchos partem dos campeões da seção 3; os textos sempre incluem 1 versão curta de produtividade (padrão do Vistoriador campeão) e 1 versão "objeção/preço/garantia" para atacar o checkout. **Preço, garantia e bônus de cada oferta: VERIFICAR na página antes de escrever no anúncio** (páginas não abertas aqui).

### 5.1 Maleta do Dentista BR (gargalo: checkout)
| | Gancho (vídeo) | Texto | Título |
|---|---|---|---|
| 1 | "O fiscal chegou" (campeão; manter a cena e trocar só a 1ª frase falada) | Atual (Simulado de Inspeção + lista de POPs) | "+115 recursos prontos para a pasta da RDC 1.002" (atual) |
| 2 | "Faltam 17 itens na sua pasta" (ângulo 20, ROAS 2,19 em 2 dias) | Curto de produtividade: "Chega de montar POP, plano de resíduos e ficha de esterilizador do zero. Personaliza com o nome do consultório e imprime hoje." | "Simulado de inspeção: veja o que falta em 5 minutos" |
| 3 | "Vai abrir consultório?" (05, CTR 3,34%) | Objeção/checkout: o que vem dentro + preço + garantia + "acesso na hora no e-mail" | "Sua pasta da vigilância pronta hoje, em Word" |

Em paralelo (não é anúncio): ver na Wiapy o relatório de checkouts abandonados (Pix pendente? cartão recusado? preço diferente da página?), e separar o pixel do IT.

### 5.2 Consultora BR (gargalo: criativo)
| | Gancho | Texto | Título |
|---|---|---|---|
| 1 | CN5 V2 "chef com tablet" (CPA R$12 em 2 dias) | Atual (RDC 216, checklist, relatório com % de conformidade) | Atual "Maleta da Consultora de Alimentos: tudo pronto pra RDC 216" |
| 2 | CN3 (CPA R$24,5) com abertura nova mostrando o relatório saindo pronto | Renda: "Entregue relatório com a sua logo e o seu CRN e feche mais clientes" | "Checklist RDC 216 + relatório com a sua logo" |
| 3 | CN4 (CPM mais barato, R$26) | Curto de produtividade: "Pare de montar checklist do zero a cada cliente" (só 2 linhas) | "Atenda mais clientes sem montar documento do zero" |

Não repetir "CVS 3" (CTR 0,87%) nem CN1 (CPM R$77).

### 5.3 Advogado previdenciário (gargalo: página)
Antes dos criativos: medir a velocidade de maletadoadvogado.site no celular e checar se há redirecionamento; 43% dos cliques não chegam à página.
| | Gancho | Texto | Título |
|---|---|---|---|
| 1 | "Raio-X do honorário" (CTR 5,67%, CPA R$29,7) | Atual (Painel do Caso) | Atual "+200 recursos para o escritório previdenciário" |
| 2 | "Exigência do INSS: 30 dias correndo" (02) | Curto: "Quanto do seu honorário entra no caixa? Veja antes do cliente assinar." | "Veja quanto do honorário entra no caixa" |
| 3 | "Documentos do zero" (05, CTR 4,69%) | Tempo/cliente: "O cliente acompanha o caso pelo link e para de ligar" | "Do contrato ao RPV num painel só" |

### 5.4 Fono infantil (gargalo: criativo cansando + escala)
| | Gancho | Texto | Título |
|---|---|---|---|
| 1 | "34 V2 espátula" (língua presa; CPA R$14,2, ROAS 3,38) | Atual ("Ainda escreve relatório do zero?") | Atual "+200 recursos prontos para fono infantil" |
| 2 | "31 respiração oral" (ROAS 2,69) | Por condição: "Criança com respiração oral: avaliação, relatório pra escola e tarefas de casa prontas" | "Relatório pra escola pronto em minutos" |
| 3 | "28 gagueira" (ROAS 2,41 no teste; não isolar em escala) | Pais/WhatsApp: "100 tarefas de casa ilustradas pra mandar no WhatsApp" | "100 tarefas de casa ilustradas para os pais" |

Reativar como controle os vídeos 04 (1.5.4) e 02 (1.3.1), que tinham CPA R$16 e estão pausados, em vez de novas "escalas isoladas".

### 5.5 Psicólogo Infantil (gargalo: criativo/CPM)
| | Gancho | Texto | Título |
|---|---|---|---|
| 1 | "App primeiro" (03, CPA R$25,6) | Atual (relatório para a escola + app) | Atual "+200 recursos prontos para o psicólogo infantil" |
| 2 | "Atividade lúdica na véspera" (02) | Atividades primeiro: "100 atividades lúdicas ilustradas e 60 cartões para a sessão de amanhã" | "100 atividades lúdicas ilustradas para a sessão" |
| 3 | **Portar o mx04 "niños" do México** (atividades ilustradas com personagens; CTR 11,2%) | Curto: "A escola pediu relatório? O app monta a partir da sua avaliação" | "Relatório pra escola pronto a partir da sua avaliação" |

### 5.6 Maletín del Psicólogo MX (gargalo: página + pixel; criativo já bom)
| | Gancho | Texto | Título |
|---|---|---|---|
| 1 | mx04 niños "Lia y Nino" (CTR 11,2%) | Atual de cada vídeo | "100 actividades ilustradas para tu consulta infantil" |
| 2 | mx02 nota de sesión | Curto: "Termina tu sesión y tu nota ya está lista para firmar" | "Tu nota de sesión en minutos, lista para firmar" |
| 3 | mx01 expediente NOM-004 (semáforo) | Objeción/precio: qué incluye + precio en MXN + garantía (VERIFICAR en Hotmart) | "Tu expediente en regla según la NOM-004" |

Tirar o mx03 documentos (CTR 0,42%). Esperar ~10 compras antes de mexer em orçamento.

### 5.7 Valigetta del Dentista IT (antes de gastar: título e pixel)
| | Gancho | Texto | Título (hoje vazio) |
|---|---|---|---|
| 1 | "Se oggi entrasse l'ASL nel tuo studio..." (01; é o equivalente do campeão BR "fiscal chegou") | Atual (App con il semaforo + modelli Word/PDF + 115 risorse) | "La Valigetta del Dentista: +115 modelli pronti" |
| 2 | "Lazio: autorizzazione entro il 7 febbraio 2027" (04; gancho de PRAZO confirmado nas notas de 28/10) | Curto de produtividade: "Basta preparare i documenti dello studio da zero: modelli in Word con il nome del tuo studio, pronti oggi" | "Simulazione d'ispezione ASL in 5 minuti" |
| 3 | No lugar de "RENTRI": "Separatore di amalgama mancante: sanzione da €4.000 a €20.000" ou "Polizza valida solo con il 70% dei crediti ECM" (ambos das notas de 28/10; conferir redação na BASE-LEGAL-IT.md) | Consenso informato / Legge 219 (03) como texto | "Documenti dello studio in regola, in Word" |

## 6. Ranking 0–10

Critérios: resultado atribuído (ROAS e CPA contra a régua do Vistoriador), volume/amostra, tendência 7d × 14d, e quão fácil é corrigir o gargalo. Nota de desempenho do funil, não de mercado.

| # | Oferta | Nota | Por quê | Próximo passo (proposta) |
|---|---|---|---|---|
| ref. | Maleta do Vistoriador BR (fora da lista) | 8,0 | R$52 mil, 2.308 compras atribuídas, ROAS 2,53, CPA R$22,7; caindo em 7d (1,89) | Referência de criativo e de escala por cópia de campanha inteira |
| 1 | **Fono infantil** | **7,0** | Maior volume da lista (R$12,5 mil, 475 compras, ROAS 1,85); checkout melhor da casa (63%); campeões com CPA R$16–21; mas 7d caiu para ROAS 1,55 | Voltar campeões pausados (04, 02) como controle e rodar o 3×3×3 da seção 5.4; parar "escalas isoladas" |
| 2 | **Consultora BR** | **6,5** | ROAS 2,03 (testes 2,26), ticket mais alto (R$64,6), página que mais converte (20% das visitas iniciam checkout); amostra pequena (R$1,1 mil, 36 compras); CPC caro | Mais ganchos (CN5 V2 chef tablet), subir orçamento no ABO original em vez de duplicar |
| 3 | **Maleta do Dentista BR** | **6,0** | R$3,5 mil, 96 compras, ROAS 1,53; criativo e página na régua; só 39% dos checkouts compram; "fiscal chegou" é o único gancho com CPA < R$30 | Auditar checkout Wiapy; testar texto de objeção/preço; separar pixel do IT |
| 4 | **Advogado previdenciário** | **5,0** | 3 dias, R$379, 9 compras, ROAS 1,34; CTR 4% (melhor criativo BR); perde 43% dos cliques antes da página | Corrigir velocidade da página antes de escalar; manter "honorário raio-x" |
| 5 | **Psicólogo Infantil** | **4,5** | R$349, 12 compras, ROAS 1,41 (7d 0,99); página e checkout excelentes; clique caro (CPC R$4, CPM R$61); pausado | Relançar com gancho "app primeiro" + porte do mx04 "niños" |
| 6 | **Maletín del Psicólogo MX** | **4,0** | R$118, 3 compras, ROAS 1,17; CTR 6% (mx04 11%); 43% dos cliques não chegam à página; pixel sem servidor; CPM alto | Velocidade da página, integração de servidor Hotmart→pixel, esperar 10 compras |
| 7 | **Valigetta del Dentista IT** | **3,0** (prontidão, sem resultado) | Começou à 00:08 de 30/10: R$0,53, 7 impressões. Riscos de montagem: pixel compartilhado com o BR, título vazio, conjunto RENTRI, R$300/dia em 5 conjuntos | Corrigir título e conjunto 02 antes de gastar; avaliar com ~R$150–300 por conjunto |

Comparação com a versão anterior: não houve versão anterior desta pesquisa acessível (a v1 de 29/10 não estava neste ambiente).

## 7. VERIFICAR

1. **Vendas reais**: as notas disponíveis não registram nenhuma venda nossa. Conferir as compras atribuídas pela Meta contra Wiapy (BR) e Hotmart (MX/IT), por oferta e por dia, principalmente na queda dos últimos 7 dias.
2. **Preço, bumps e garantia** de cada página (maletadodentista.site, maletadaconsultora.site, maletadoadvogado.site, maletadafonoinfantil.site, maletadopsicologoinfantil.site, maletindelpsicologo.site, valigettadeldentista.site): não abertas (WebFetch/curl bloqueados pela rede). Tickets médios atribuídos: dentista R$56, consultora R$65, advogado R$56, fono R$49, psicólogo infantil R$41, MX R$46.
3. **ROAS de equilíbrio** por plataforma (taxa Wiapy, taxa Hotmart, impostos). A faixa 1,1–1,2 usada na seção 4 é hipótese.
4. **Checkout do dentista (Wiapy)**: por que só 39% dos checkouts viram compra, contra 58–63% nas outras ofertas no mesmo checkout (Pix pendente, cartão recusado, preço/oferta diferente da página, bumps).
5. **Pixel "odonto" compartilhado BR + IT**: desde 29/10 às ~23h (Brasília) recebe valigettadeldentista.site e pay.hotmart.com junto com maletadodentista.site e pay.wiapy.com. Decidir se cria um pixel só para o IT.
6. **Conjunto "02 - rentri" da Valigetta**: o anúncio pergunta "RENTRI: il tuo studio deve esserci o no?". As notas de 28/10 dizem que o RENTRI deixou de valer para studio individual (L.199/2025) e que "NÃO é gancho". Conferir a afirmação do vídeo e da página na BASE-LEGAL-IT.md.
7. **Título vazio** nos 5 anúncios da Valigetta (conferir se foi intencional).
8. **Normas citadas nos anúncios BR**: "RDC 1.002" (dentista), "prazo dezembro" (dentista), "RDC 216" (consultora), "CVS 3" (consultora), prazo de 30 dias da exigência do INSS (advogado). Não conferidas nesta pesquisa.
9. **Página do advogado**: por que só 57% dos cliques viram visita (velocidade, redirecionamento, bloqueio no navegador do Instagram).
10. **Página do MX**: idem (57%); e **pixel "psico latam" sem eventos de servidor** (data do último evento de servidor em branco) e sem nota de qualidade de correspondência.
11. **CPM de R$58 no México** (alto para o país): conferir se é efeito de orçamento baixo/fase de aprendizado.
12. **Queda geral de 7 dias** na conta 05 (todas as ofertas BR, inclusive Vistoriador), com frequência baixa.
13. **Atribuição mista** (7 dias clique × 1 dia visualização + 7 dias clique): compras entre campanhas não são 100% comparáveis.
14. **Valor de compra inclui bumps?** O ticket médio depende de o checkout enviar o valor total ao pixel.
15. **Outras contas**: só as contas 03 e 05 foram analisadas. Há outras contas ativas no mesmo gerenciador (ex.: conta 06) que não foram consultadas.
16. **Campanha "GC" Espanha** (conta 03, pixel "concursos latam", ativa desde 28/10: R$171, 5 compras, ROAS 2,10; 2 anúncios reprovados: "C3 mapa Ceuta Melilla" e "C6 texto corrido vs mapa") está fora da lista do prompt; não analisada a fundo.

---
Fim. Status: CONCLUÍDO (30/10/2026).
