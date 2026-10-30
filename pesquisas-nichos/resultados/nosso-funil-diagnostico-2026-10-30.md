# Nosso funil: o que converte (diagnóstico 30/10/2026)

> Status: EM ANDAMENTO (gravado aos poucos).

## Avisos de método e ambiente
- **Somente leitura.** Usadas apenas ferramentas de consulta do conector Meta (listar contas, ler entidades e métricas). Nada foi criado, editado, ativado, pausado ou excluído.
- Os relatórios anteriores citados nas instruções (v1 de 29/10) e os arquivos do Desktop do usuário **não estavam acessíveis** neste ambiente (container na nuvem).
- **Vendas citadas:** as únicas "vendas registradas nos arquivos e memórias" acessíveis aqui são as das notas em `pesquisas-nichos/notas/` (`fila-ofertas.md`, `meta-varredura-low-ticket.md`, `pesquisa-europa.md`). Essas notas **não registram nenhuma venda nossa** (nem quantidade nem faturamento). Toda contagem de compra abaixo vem do pixel/atribuição da Meta (eventos `purchase` dentro da Meta), não de Hotmart/Kiwify/Stripe; por isso cada número de compra é "compra atribuída pela Meta" e precisa ser conferido na plataforma de pagamento (VERIFICAR).
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
| **Valigetta Dentista IT** (desde 30/10 00:08) | criação | 0,53 | — | — | 85 | 1,2 | 0 | 0 | 0 | 0 | — | — | — |
| **Maletín Psicólogo MX** (v29.10 + v30.10, desde 28/10) | criação ≈ 7d ≈ 14d | 118,28 | 6,0% (v29.10) | 0,97 | 57,8 | 1,36 | 124 | 71 (57%) | 7 (10%) | 3 (43%) | 39,43 | 1,17 | 46,2 |
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
(em preenchimento)

## 4. Diagnóstico do gargalo por oferta
(em preenchimento)

## 5. Variações 3×3×3 propostas
(em preenchimento)

## 6. Ranking 0–10
(em preenchimento)

## 7. VERIFICAR
(em preenchimento)
