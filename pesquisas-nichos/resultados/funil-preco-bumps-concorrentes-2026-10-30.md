# Como os concorrentes vendem depois do clique: preço, bumps, garantia (30/10/2026)

> Status: EM ANDAMENTO (gravado aos poucos).

## Avisos de método
- A versão anterior (v1 de 29/10) e os relatórios citados em "Ler antes" NÃO estavam acessíveis neste ambiente. A lista de vendedores foi tirada das notas (`notas/*.md`), dos nomes citados nos prompts de `01-refazer-v2/` e `03-novas-lancadas/` e de `resultados/` (vazio no início desta pesquisa).
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). Medição feita só com o conector Meta (`ads_library_search`, anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
- **BLOQUEIO PRINCIPAL: as páginas de vendas NÃO puderam ser abertas.** A política de rede deste ambiente nega a saída para os sites dos vendedores e checkouts. Testados e negados (WebFetch "ENOTFOUND" e proxy "403 CONNECT"): psiorganizado.com, consultorioemdia.shop, kit-docs-odonto.lovable.app, www.lovable.app, pay.hotmart.com, hotmart.com, go.hotmart.com, payhip.com, www.facebook.com (Biblioteca de Anúncios em HTML), web.archive.org, en.wikipedia.org. Para liberar, o usuário precisa abrir as configurações do ambiente na nuvem (menu do ambiente na barra de título da sessão → Edit → Network access) e adicionar esses domínios em "Allowed domains", ou escolher um nível de acesso mais amplo (passo a passo: https://code.claude.com/docs/en/cloud-environments#network-access).
- O que deu para fazer: (a) medir pelo conector Meta os dias reais, o nº de anúncios ativos, a moeda da conta de anúncios e o título do link de cada anúncio (o título mostra gancho, prova social e às vezes preço); (b) usar trechos de resultados do WebSearch (páginas indexadas de Hotmart, Payhip, sites próprios) para preço, garantia e bônus quando aparecem. Tudo que veio só de trecho de busca está marcado "(trecho de busca)". O resto da ficha de funil (bumps, upsells, estrutura da página) ficou VERIFICAR.
- Atenção: o campo `currency` do conector é a moeda da CONTA DE ANÚNCIOS, não a moeda do preço. Uma conta em USD anunciando na Itália não quer dizer que o preço seja em dólar.
- Nenhuma compra feita nem formulário preenchido. O que não foi confirmado está marcado VERIFICAR.
- Nossos parâmetros de comparação: Valigetta del Dentista IT €27 (cheio) / €19 (oferta), bumps €9,90, garantia 15 dias.

## 1. Vendedores candidatos e medição (dias reais, nº de anúncios, moeda)

Medição feita em 30/10/2026 pelo conector Meta, por `page_id`, só anúncios ATIVOS. "Moeda conta" = moeda da conta de anúncios. "Títulos" = `ad_creative_link_title` dos anúncios ativos (é o que aparece no card do anúncio, abaixo da imagem).

| # | Vendedor (page_id) | País/idioma | Nicho | Nº anúncios ativos | Anúncio ativo mais antigo | DIAS REAIS | Moeda conta | Régua |
|---|---|---|---|---|---|---|---|---|
| 1 | Kit Studio Blindato - APP (1294553453740890) | IT / italiano | dentista | 28 | 17/09/2026 | 42 | USD | PROVADO |
| 2 | Kit di Documenti Psicologici (1316795101520270) | IT / italiano | psicólogo | 35 | 23/09/2026 | 36 | USD | PROVADO |
| 3 | Sorrisi in Regola (1063538733498593) | IT / italiano | dentista | 1 (achado por termo) | 21/10/2026 | 8 | EUR | TESTE |
| 4 | Recursos Legales PRO / Recursos Legales PRO Salud Mx (880855681786807) | MX / espanhol | catálogo jurídico-saúde (médico, dentista, psicologia, spa, farmácia, advogado) | 5 | 23/07/2026 | 98 | MXN | PROVADO |
| 5 | Psique y Ciencia (382519355660997) | MX / espanhol | psicólogo (kit de plantillas + curso de expediente) | 13 | 26/09/2026 (kit desde 28/09) | 33 (kit 31) | MXN | PROVADO (limite) |
| 6 | Aprende y Emprende en Casa (113921117042583) | MX / espanhol | "Pack Psicología", tanatologia, autohipnose | 5 | 01/09/2026 | 58 | MXN | PROVADO (multinicho) |
| 7 | Psicólogo Organizado (929581043578532) | CO / espanhol | psicólogo clínico | 7 | 06/05/2026 | 176 | COP | PROVADO |
| 8 | Qualitiva Soluciones (574842992375227) | CO / espanhol | habilitação Res. 3100 (IPS e consultórios) | 32 | 26/01/2026 | 276 | COP | PROVADO |
| 9 | Dt.Dental Software Odontologico (644396635996094) | CO / espanhol | dentista (SOFTWARE, não kit) | 19 | 02/07/2026 | 119 | COP | PROVADO (software) |
| 10 | Archivos Digitales Express (103894282759676) | MX / espanhol | estética (formatos) | VERIFICAR (achado por termo) | 11/09/2026 | 48+ | MXN | PROVADO (provável) |
| 11 | Formatos digitales (629381216925799) | MX / espanhol | formatos clínicos | VERIFICAR | 02/10/2026 | 27 | MXN | TESTE |
| 12 | Kit de Herramientas Terapéuticas (1303750612814915) | ES/LATAM / espanhol neutro | psicólogo (ferramentas de sessão) | 5 | 22/08/2026 | 68 | BRL (operador BR) | PROVADO em espanhol, NÃO prova Espanha |
| 13 | Lic. Zulma Laguna (778739435326228) | US / inglês | dentista (docs, SOPs, consentimentos) | 8 | 01/10/2026 | 28 | USD | TESTE (vira PROVADO em 31/10 se seguir ativo) |
| 14 | Dental Master Pro Max (1170940042761217) | US / inglês | dentista (marketing, "$27") | 1 | 06/06/2026 | 145 | BRL (operador BR) | PROVADO fraco (1 anúncio) |
| 15 | Childminder Resource Hut (564585390322776) | UK / inglês | childminder / creche (Ofsted, EYFS) | 35 | 01/07/2025 | 485 | GBP | PROVADO (o mais antigo da lista) |
| 16 | Health Connect (730699523450802) | UK / inglês | care (políticas CQC, assinatura) | 1 | 09/10/2026 | 20 | GBP | TESTE |
| 17 | Compliance Supports (227964520409222) | UK / inglês | care CQC (serviço) | VERIFICAR | 27/10/2026 | 2 | GBP | TESTE |
| 18 | CareDocs Direct (1178206642051081) | UK / inglês | care (políticas sob encomenda via Fiverr) | VERIFICAR | 06/09/2026 | 53 | GBP | PROVADO (serviço, não kit) |
| 19 | Simple Budget Excel / SimpleBudget.Excel (233823119815880) | IT / italiano (+ espanhol) | planilhas finanças / forfettario | 41 | 16/02/2025 | 620 | EUR | PROVADO (gancho forfettario "Non superare gli 85k" desde 23/08, 67 d) |
| 20 | Giulia Ferraresi (1299765756564104) | IT / italiano | "Kit Contabile Pratico 2027" | VERIFICAR | 22/10/2026 | 8 | USD | TESTE |

(continua)

## 2. Ficha de funil por vendedor (página de vendas)
(em preenchimento)

## 3. Padrões por país
(em preenchimento)

## 4. Comparação com nossos preços e recomendações por país
(em preenchimento)

## 5. Ranking 0–10 (o que copiar do funil dos concorrentes)
(em preenchimento)

## 6. VERIFICAR
(em preenchimento)
