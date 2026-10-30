# Ofícios e negócios por país — v2 (30/10/2026)

> **Avisos de ambiente**
> - A v1 (`pesquisas-nichos-2026-10-29/oficios-negocios.md`) **não estava acessível** neste ambiente (container na nuvem, sem Desktop). Usei só o que o prompt cita dela (Andrei Kowalski; Studio Facile/PictoStudy; títulos vazios Más seguridad, Beatriz Guerra, Solunetpro) e as notas do usuário.
> - **SearchAPI indisponível** (sem chave aqui e créditos zerados até 08/11/2026). Medição feita com o conector Meta (`ads_library_search`, só anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
> - Régua: PROVADO = anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.
> - **WebFetch bloqueado pela rede deste container** (proxy recusa facebook.com, wikipedia, salute.gov.it, pictostudy.com etc.). Não consegui abrir NENHUMA página de vendas nem fonte oficial direto. Normas e mercados vieram só de busca web (WebSearch), com URL citada. Preço/checkout/bumps/garantia dos concorrentes ficam **VERIFICAR** (abrir no navegador do Mac).
> - O conector Meta não devolve o link de destino nem o texto do anúncio, só página, título do link, data de início e moeda da CONTA (não é a moeda do preço). Busca por palavra é ampla (não é frase exata).

Status: EM ANDAMENTO (gravando aos poucos)

## 1. Concorrentes da v1 a checar

Medição por `page_ids`, só anúncios ATIVOS, data de referência 30/10/2026.

| Página (page_id) | O que vende | Países/idiomas vistos | Nº anúncios ativos | Anúncio ativo mais antigo | Dias reais | Moeda da conta | Veredito |
|---|---|---|---|---|---|---|---|
| **Andrei Kowalski** (1340912605769671) | "Dossiê/pasta de higiene" para café e bistrô: simulado de inspeção sanitária. Ganchos: "L'inspecteur de la DDPP est à la porte", "Mâine vine controlul DSVSA", "Dnes ráno kontrola. Kde máte zložku HACCP?", "Planul HACCP pe perete, nu în sertar" | FR, RO, CZ, SK | 17 | 18/10/2026 | **11,8 d** | USD (conta típica de operador BR) | TESTE. Ainda não provado. É a Consultora traduzida em 4 países ao mesmo tempo. Preço/checkout: VERIFICAR (link não sai no conector, WebFetch bloqueado) |
| **Studio Facile** (1232011766670582) | Fábrica de e-books **ilustrados** ("X spiegato con i disegni", "Veja as páginas antes de descarregar"): cozinha profissional e higiene na cozinha (HACCP visual), toelettatura (banho e tosa), idraulico, elettricista, falegnameria, macellaio, saldatura, bombas de calor, fotovoltaico, contabilidade, primeiros socorros, consultório dentário, unhas, nutrição, LIS, física, matemática, vinho, cogumelos | IT (345), DK (98), PT, PL, CZ, GR e outros | **920** | todos os vistos criados em 29/10/2026 | **≈1 d** nos 150 vistos (o conector só mostra os 50 mais novos por consulta; não deu para achar anúncio antigo) | USD | TESTE em massa (estratégia "spray": 1 livro ilustrado × 20 ofícios × 10 idiomas). "PictoStudy" não aparece em anúncio nem em busca web: provável nome do site/checkout, VERIFICAR |
| **Solunetpro** (1118702291315648) | Formatos SG-SST "con normas 2025-2026" (Colômbia), "Primero recibes y luego pagas", "Para asesores con varias empresas" | CO | 15 | 16/10/2026 | **13,4 d** | COP | TESTE (vendedor local CO, pagamento contra entrega digital) |
| **Beatriz Guerra** (907895875729587) | Italiano: "Capisci il rischio, non andare a memoria" (sicurezza sul lavoro / rischio; aparece na busca "DVR valutazione dei rischi") | IT | 8 | 25/09/2026 | **34,8 d** (só 1 anúncio tão antigo; os outros 7 têm ≤12 d) | BRL (operador BR) | PROVADO fraco no IT (1 criativo 30+ d, poucos anúncios). Produto exato: VERIFICAR |
| **Más seguridad** (291789807354053) | Achado pela busca "NOM-035 formatos" (México). Títulos vazios (anúncio de imagem/vídeo sem link title). Rede de páginas irmãs: "Seguridad e higiene y más" (345679278628269, 3 anúncios, 361 d), "Seguridad e higiene y mas.9" (101919158005402, ≥4 anúncios, 13,9 d), "Seguridad e higiene y más" (1101519659721154, novos de 29/10), "Formatos digitales pro" (1301518069721501, novos de 29/10) | MX | 5 | **02/11/2025** | **361 d** | MXN | **PROVADO no MX** (2 páginas com 361 d e a rede abrindo páginas novas em out/2026 = escalando). Produto/preço: VERIFICAR (provável pacote de formatos de seguridad e higiene / NOMs STPS; a busca web não achou o site) |

Achados extras do mesmo tipo:
- **Marina cardozo** (1019209551268731, conta USD, 67 anúncios): fábrica multi-produto. FR: "Ton entreprise en règle en un après-midi" (aparece na busca **DUERP**, 6 anúncios, todos de 29/10 = 0,7 d). ES: "Las 45 actas, ya redactadas", "Dueño de negocio: tus reglas, por escrito y firmadas" (reglamento interno). PT: manual de habilidades. Tudo ≤2 d. TESTE.
- **Seguridad y Salud Ocupacional y Medio Ambiente** (108273737689362, conta PEN): "PACK DOCUMENTAL SG-SST + DASHBOARD Y SEÑALETICA", "Pack Completo ISO + Dashboards", mirando CO. 4 anúncios, mais antigo 23/10 (≈6 d). TESTE.
- **Studio in Ordine** (1441969015658409, EUR, IT): "Il faldone dello studio, già scritto" (pasta documental do consultório). 3 anúncios de 29/10. TESTE, nativo italiano.
- **Annie Portinari** (102222484836247, EUR, IT): "Se domani arrivasse un controllo ASL?", "Legionella in condominio", "Proteggi la reputazione del tuo hotel". 4 anúncios de 27/10. Parece consultoria (serviço), não kit. VERIFICAR.

## 2. Nichos por país

(em andamento)

## 3. Ranking 0–10

(em andamento)

## 4. VERIFICAR

(em andamento)

## 5. Fontes
