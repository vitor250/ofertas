# Novos nichos, resto da Europa e Leste: V2 refeita do zero (30/10/2026)

**Status:** completo (30/10/2026). Seções 1 a 10.

**Método desta rodada**
- Conector Meta `ads_library_search` (só ATIVOS), `client_conversation_id` `Qm7Vt2Kx9Lp4Rw8Zn3Hc`. Ele devolve os anúncios mais novos primeiro e corta em 50, então o "dia" de uma página é o do anúncio mais antigo **que apareceu**.
- SearchAPI (`engine=meta_ad_library`, frase exata, devolve data de início, moeda, link): usei, mas a cota mensal compartilhada **zerou durante a rodada** (10.000/10.000 às ~12h UTC de 30/10; outros agentes rodando `medir_p1.py` na mesma chave consumiram ~1.100 créditos em uma hora). Consegui ~40 termos locais antes. O resto da cobertura foi pelo conector. A cota renova em 08/11.
- Páginas de vendedor abertas com navegador embutido e `curl` (preço e conteúdo). O que não abri está dito em cada linha.
- Dias = 30/10/2026 ~13h UTC menos o início do anúncio ativo mais antigo visível.

---

## 1. Descoberta principal: já existe vendedor da NOSSA pasta HACCP, em 11 países, com 4 a 5 dias

**Página:** Andrei Kowalski (page_id 1340912605769671), moeda **USD**, 18 anúncios ativos (conector, 30/10).
- Persona de operador BR, no mesmo padrão de Ioana/Sanja/Marieke. Loja: **concentrare.shop** (Shopify, mesmo domínio vende "ČITELNĚ", plano de caligrafia, a 279 Kč).
- Anúncios ativos em tcheco, eslovaco, romeno e francês. Início do mais antigo que apareceu: ~26–27/10/2026, ou seja, **4 a 5 dias**. Não é prova de 30 dias.
- Criativos (tradução minha): "Hoje de manhã, inspeção de higiene. Onde está a sua pasta HACCP?"; "7 miudezas pelas quais você leva multa até em café limpo"; "Amanhã vem o controle da DSVSA. O dossiê está pronto?" (RO); "O inspetor da DDPP está na porta. O que você mostra?" (FR); "Véspera da inspeção? Uma pasta em vez de uma pilha de papéis".
- Oferta lida no anúncio SK (aberto na Biblioteca): **"HACCP na stene" 6 em 1 para café e bistrô**: Plano HACCP pré-preenchido (só preencher os campos amarelos), folhas diárias "Dois assinaturas" (temperatura de manhã, limpeza à noite), tabela dos 14 alérgenos, bônus "Dia da inspeção", "Treinamento do pessoal", pasta modelo "Café Pod Lipou". **€15,99 em vez de €31,98**, Word + Excel + PDF, garantia de 30 dias.
- **Páginas de venda já montadas** (lidas por `curl` em concentrare.shop/pages/…; preço lido em cada uma):

| Página | Idioma / país provável | Preço lido | Observação |
|---|---|---|---|
| haccp-cz, haccp-restaurace, haccp-pekarna | CZ (café/bistrô, restaurante, padaria e confeitaria) | 369 Kč (riscado 1.490 Kč) | CZ com 3 sub-nichos |
| haccp-na-stene (+ -2) | SK | 12,90 € (ads dizem 15,99 €) | |
| haccp-pe-perete, -89, -md | RO e Moldávia | 74 lei (riscado 79/…) | |
| haccp-a-falon | **HU** | 5.490 Ft (lista 10.900/16.900) | página pronta, **0 anúncios em HU hoje** |
| haccp-na-zidu | HR/RS | 12,90 € | página pronta, **0 anúncios em HR hoje** |
| haccp-na-steni | SI | 12,90 € | página pronta |
| haccp-na-scianie | PL | 49,99 zł | |
| haccp-au-mur, -rb, -boulangerie | FR (café, padaria) | ~19 € (**VERIFICAR**) | |
| haccp-al-muro | IT | não lido | |
| haccp-duvarda | TR | 449–769 TL | |

- **Conector, anúncios ativos da página por país:** HU 0, GR 0, HR 0, BG 0, AT/CH/NL/BE 0. Ou seja, o operador **testa em CZ/SK/RO/FR e já deixou HU, HR/RS, SI, PL, IT, TR prontos**. **GR, BG, AT/CH, NL/BE, nórdicos e bálticos não têm página dele.**
- Leitura: HACCP deixou de ser "nicho vazio, sem vendedor de kit". O formato **pasta de 6 em 1 a €13–16** existe e está em teste por BR em CZ/SK/RO. Não é prova de venda, mas é um concorrente direto com preço abaixo do nosso €19–27.

### Outros dois operadores BR de HACCP (D0–D2)

| Página (page_id) | Moeda | Início | O que é |
|---|---|---|---|
| **Studio Facile** (1232011766670582) | USD | 29/10 ~12h UTC, **~1 dia**, 100+ anúncios na página; GR: HACCP "Το HACCP, με εικόνες" | Livro ilustrado de profissões técnicas; clonou o catálogo inteiro. Em CZ: "Hygiena potravin v obrázcích" |
| **Studio Digitale** (1385277191336074) | USD | 28/10, **~2 dias**, 166 anúncios na página | **Terceira** página BR de HACCP: "Hygiena potravin vysvětlena pomocí kreseb" (CZ), "Igiena alimentară, explicată prin desene" (RO). Também PL (odontologia, elétrica) e GR |
| PictoStudy Europe (1450567701465873) | USD | 29/10 | HACCP em grego (GR e RO) |

Nenhum chega perto de 30 dias. Todos são **livro ilustrado de estudo** (USD, produto diferente de pasta de conformidade), exceto Andrei Kowalski, que é **pasta de conformidade**.

---

## 2. Vendedores locais de HACCP/conformidade (conector, 30/10)

| País | Página (page_id) | Dias | Moeda | O que vende | Leitura |
|---|---|---|---|---|---|
| HU | **Kiss Anett – HACCP & élelmiszerbiztonsági tanácsadás** (1002509339621794) | **~178** | HUF | Consultoria HACCP (2 anúncios) | Serviço local com 6 meses de anúncio. Demanda paga existe; não é kit |
| HU | **Minerva 90** (140704262625169) | ~91 | HUF | Curso "Egészségügyi kártevőirtó tanfolyam" (controle de pragas) | Curso |
| HU | haccpvédelem (623382974191164) | ~46 | HUF | Página de HACCP (1 anúncio, criativo sem texto) | **VERIFICAR** produto |
| HU | AHACCP.ai (1242269788975227) / Sattva Guidance (358789431514149) | ~0,1 | HUF | "Antes da inspeção? Esteja pronto" / "HACCP feito de forma simples" | Novos, 30/10 |
| HU | Testo Magyarország (2186441621674840) | ~22 | EUR | "Papírmentes HACCP dokumentáció" (sensores + app) | Software/hardware |
| NL/BE | Apprendo Horeca, appHoreca, Octopus HACCP (FR, ~22 d) | 0–22 | EUR | Software de HACCP | Mercado B2B pago, mas software |
| CH | Blaze IQ (1143677515486709) | <1 | CHF | Etiquetas HACCP digitais | Software |
| GR | Apopsi, ΚΔΒΜ Προσόν, DP Studies (272 d), ΚΕΠΕΘ (140 d), Smarteching (133 d), Kitchen Pro (100 d) | 88–272 | EUR | **Cursos ΕΦΕΤ** (seminário obrigatório) e estudos de equipamento | Curso/serviço com meses de anúncio: **demanda grega de HACCP/ΕΦΕΤ é paga e antiga**, ninguém vende kit |

---

## 3. Tamanho: Eurostat `sbs_ovw_act`, nº de empresas, 2024 (API consultada em 30/10/2026)

**Correção importante:** a V1 disse que a Grécia estava "fora do dataset" e usou IBISWorld (~47 mil). **A Grécia está no Eurostat** (código EL): restauração **76.728**, não 47 mil.

| País | I56 Restauração | S96.02 Cabeleireiro/estética | Q86 Saúde (total) | Q8623 Dentistas | Q88 Assistência social s/ alojamento | P85 Educação | N79 Agências de viagem | R93 Esporte/lazer |
|---|---|---|---|---|---|---|---|---|
| **GR** | **76.728** | 20.251 | 67.255 | 11.486 | 2.536 | 24.108 | 4.612 | 8.506 |
| **NL** | 75.781 | **81.841** | 157.024 | 11.507 | **94.510** | 142.556 | 7.220 | 23.002 |
| **BE** | 50.738 | 24.106 | 59.097 | 6.712 | 3.267 | 10.689 | 2.175 | 13.450 |
| **CZ** | 48.091 | 43.396 | 26.779 | 5.556 | 932 | 27.766 | 6.656 | 23.085 |
| **RO** | 29.965 | 41.073 | 29.491 | 9.813 | 966 | 29.874 | 3.522 | 15.840 |
| **AT** | 30.929 | 18.884 | 64.874 | 4.341 | 18.567 | 24.311 | 2.491 | 9.561 |
| **HU** | 26.370 | 48.141 | 38.202 | 5.970 | 1.038 | 41.356 | 2.390 | 8.690 |
| BG | 19.441 | 15.904 | 14.302 | 5.366 | 427 | 4.549 | 1.842 | 4.024 |
| RS | 18.317 | 4.563 | 3.283 | 1.647 | 115 | 3.019 | 1.026 | 1.944 |
| HR | 17.784 | 10.187 | 6.146 | 2.468 | 332 | 5.253 | 3.150 | 2.819 |
| SK | 16.637 | 13.607 | 9.252 | 2.211 | 752 | 11.009 | 1.565 | 7.744 |

Fonte: Eurostat API `sbs_ovw_act`, `indic_sbs=ENT_NR`, 2024, `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&lang=EN&nace_r2=I56&indic_sbs=ENT_NR&sinceTimePeriod=2023&geo=EL` (troque `nace_r2` por S9602, Q86, Q8623, Q88, P85, N79, R93). Os valores incluem autônomos sem empregados, por isso NL Q88 e P85 são enormes (zzp/gastouders). SE, DK, NO, FI e bálticos: ver V1 (mesma fonte).

---

## 4. Ganchos legais confirmados nesta rodada (fonte, data, multa)

| Gancho | O que a fonte diz | Fonte | Status |
|---|---|---|---|
| **GR: treinamento obrigatório do pessoal de alimentos (Υ.Α. 110581/2025, ΦΕΚ Β' 2161/06-05-2025)** | Quadro único de treinamento obrigatório do pessoal de empresas de alimentos. Regime antigo valia até **31/12/2025**. Certificados novos valem **5 anos**, com exame eletrônico do ΕΦΕΤ. Taxa de **€50 por treinando** (decisão ΕΦΕΤ 347/26-6-2025, desde 01/09/2025) | [efet.gr: texto do ΦΕΚ](https://www.efet.gr/files/110581_2025_fek_2161_2025.pdf) · [e-nomothesia](https://www.e-nomothesia.gr/kat-agoranomikes-diatakseis/ya-110581-2025.html) | Confirmado como lei. Detalhe de carga horária (8 h manipulador / 20 h HACCP completo) vem de sites de cursos: **VERIFICAR** no ΦΕΚ |
| **GR: circular ΕΦΕΤ (decisão de diretoria 84/20-02-2026; documento 11/02/2026 e republicação 03/2026)** | Cria a **Categoria 2β**: empresas de risco alto (redes, hotéis grandes, restaurantes com mais de 250 cobertos/dia) podem usar treinamento interno de 20 h. Baixo e médio risco (mercearias, quiosques, cantinas escolares, pequenos hotéis só com café da manhã, açougues de bairro, padarias, restaurantes fora de rede) **são obrigados a usar os programas ΕΦΕΤ**. Todas devem mostrar registros de treinamento (presença, material, avaliação) na inspeção. O ΕΦΕΤ fiscaliza no local. O artigo não cita prazo | [cibum.gr: análise da circular](https://cibum.gr/nea/estiasi-tourismos-nea/dieykrinistiki-egkyklios-toy-efet-gia-tin-ypochreotiki-ekpaideysi-prosopikoy-epicheiriseon-trofimon/) · [efet.gr: PDF da circular](https://www.efet.gr/files/1497_11_02_2026_dieukrinistiki_egkiklios.pdf) | Confirmado por fonte secundária. O PDF do ΕΦΕΤ não pôde ser lido (compactado): **VERIFICAR** data e protocolo (fontes divergem: 11/02/2026 e 23/06/2026) |
| **NL: falso autônomo, multas** | Fiscalização plena desde 01/01/2025. Em 2026 não há multa por omissão (`verzuimboete`), só cobrança com "pouso suave" (3% do valor, 10% em casos extremos, até €6.709 por período). **"Vanaf 2027 vervallen ook deze laatste elementen van de zachte landing."** | [MKB Servicedesk 29/12/2025](https://www.mkbservicedesk.nl/nieuws/ondernemersnieuws/kabinet-past-koers-aan-in-2026-nog-geen-verzuimboetes-bij) · [PwC](https://www.pwc.nl/nl/actueel-en-publicaties/belastingnieuws/loonbelasting-en-sociale-verzekeringen/handhaving-schijnzelfstandigen-vanaf-tweeduizendzesentwintig.html) (PwC deu 403 ao fetch; trecho vem do resultado de busca) | Data 01/01/2027 confirmada em 2 fontes de imprensa especializada. Kamerbrief original: **VERIFICAR** |
| **NL: VBAR** | A parte "esclarecedora" do projeto foi **retirada**. Resta o `rechtsvermoeden` (presunção de vínculo até **€38/h**, referência 01/01/2026). Prazo europeu de publicação no Staatsblad: **31/08/2026**. Uma `Zelfstandigenwet` separada está em preparação. Artigo de 30/03/2026 | [Grant Thornton NL](https://www.grantthornton.nl/insights/legal-services/wet-dba/zzp-wetgeving-in-beweging-verduidelijkingsdeel-vbar-vervalt-kabinet-werkt-aan-nieuwe-zelfstandigenwet/) | Confirmado até 03/2026. Se foi publicado no Staatsblad em 08/2026: **VERIFICAR** |
| **CZ: multas por provozní řád (lei 258/2000)** | **§ 92m: até 1.000.000 Kč** por operar sem provozní řád aprovado, não treinar equipe ou não cumpri-lo. **§ 92f: até 3.000.000 Kč** por violar o § 21 (atividade que ponha a saúde em risco), **até 2.000.000 Kč** por falhas de higiene operacional ou cosmético fora da norma, **até 1.000.000 Kč** por não notificar o início/mudança/fim de serviço de cabeleireiro, cosmética etc. (§ 21 odst. 3), até 50.000 Kč por permitir trabalho em violação do § 19(3) | [zakonyprolidi.cz: lei 258/2000](https://www.zakonyprolidi.cz/cs/2000-258) (§ 21, 21a, 23, 92f, 92m) | **Confirmado em texto da lei** (resposta lida em 2 trechos; a numeração dos incisos pode mudar com emendas) |
| CZ: modelos oficiais e instrução do MZd | Instrução metodológica MZDR 3644/2025 (08/2025) e modelos oficiais grátis em 12/2025 | [mzd.gov.cz](https://mzd.gov.cz/?p=214739) | Da V1; não reaberto |
| HU: Nébih, inspeções sazonais | Verão 2024: 346 estabelecimentos, 48 processos, multas > 3 milhões de HUF | [economx](https://www.economx.hu/gazdasag/2024/07/25/nebih-ellenorzes-strandbufek-higenia-793478/) | Da V1; não reaberto |
| GR: inspeções fiscais AADE | 68.400 inspeções em 2025, 34,2% de infração | [naftemporiki](https://www.naftemporiki.gr/finance/economy/2063787/aade-19-473-epicheiriseis-piastikan-na-forodiafeygoyn-to-2025-sto-342-i-paravatikotita/) | Fiscal, não sanitário |

---

## 5. Medições de hoje por termo local (o que apareceu e o que NÃO apareceu)

SearchAPI (frase exata, só ativos, ~40 termos antes de a cota zerar) e conector. "0" = nenhum anúncio ativo naquele país com aquela frase. Isso mostra onde **ninguém anuncia**, mas a frase exata é estreita: um 0 não prova que ninguém venda, só que ninguém anuncia com essas palavras.

| País | Termo local | Resultado | Leitura |
|---|---|---|---|
| GR | `φυσικοθεραπευτ`, `νηπιαγωγ`, `πρότυπα εγγράφων`, `αξιολόγηση επαγγελματικού κινδύνου`, `ΑΜΑ Airbnb` | 0 | Ninguém anuncia kit para fisioterapeuta, educadora, documentos prontos ou avaliação de risco em grego |
| GR | `έτοιμα έγγραφα` | 4 anúncios, 1 página, <14 d | Só a Digital solutions (dentista) |
| GR | `βραχυχρόνια μίσθωση` | 12 anúncios: property managers e segurança (Perla Homes 154 d, Kolossos Security 154 d) | Só serviço |
| GR | `πυρασφάλεια` | 58 anúncios: lojas de extintores (Astoria 430 d, Fire Expert 385 d) | Produto físico |
| GR | `τεχνικός ασφαλείας` | 5 anúncios: cursos (ΚΔΒΜ Προσόν 84 d, Τεχνικές Σχολές Ηρακλείου 89 d) | Curso |
| GR | `ΕΦΕΤ` | 21 anúncios, 18 páginas: DP Studies 272 d, ΚΕΠΕΘ 140 d, Smarteching 133 d, Ινστιτούτο Ανάπτυξης Απασχόλησης 142 d, Kitchen Pro 100 d, ΚΔΒΜ Προσόν 88 d (todos EUR, 1 anúncio cada) | Cursos ΕΦΕΤ pagos há 3 a 9 meses. **Ninguém vende pasta de documentos** |
| CZ | `provozní řád` | 1 anúncio (academia, 22 d) | Zero vendedor |
| CZ | `kadeřn` | 0 | Zero |
| CZ | `hodnocení rizik`, `vzory dokumentů` | 2 e 3 anúncios, nenhum com ≥14 d | Zero |
| CZ | `šablony pro` | 15 anúncios, só marketing/IA (Darek Golebiowski 135 d) | Fora do tema |
| CZ | `fyzioterap` | 9: BioHeals (451 d, aterramento) | Fora do tema |
| CZ | `pečovatel` | 24: SunSet MSH 1.498 d (recrutamento de cuidadoras para a Áustria), Geroneai 204 d (IA para cuidadores) | Serviço |
| CZ/SK | `BOZP` | 132 anúncios (conector): Poradca podnikateľa (SK), Kloubíme (CZK), Novatraining.sk, Inštitút Bezpečnosti Práce, Dům Kotlů | Software, curso, assinatura; nenhum kit |
| SK | `prevádzkový poriadok` | 1: **MG Group, 154 d** (EUR; "3 povinnosti que 9 em 10 empresas ignoram": checklist do empregador, consultoria) | Serviço, 1 anúncio |
| SK | `kaderníč`, `opatrovateľ`, `ubytovanie Airbnb`, `vzory dokumentov` | 0 ou 1 | Zero |
| SK | `materská škola` | 22: escolas, imóveis | Zero kit |
| HU | `HACCP dokumentáció` (conector) | 10 anúncios, ver seção 2 | |
| HU | `munkavédelmi dokumentáció` (conector) | 8: Udvarfalvi (29 d), Kappel Tűz- és Munkavédelem (30 d, serviço), EHS Market (4 d), Viapan | **Vendedor local de documentos digitais** (ver abaixo) |
| HU | `kockázatértékelés` | 8: Udvarfalvi (29 d); Cubix (95 d, curso de IA) | |
| HU | `kész dokumentum` | 3: Digital solutions (dentista) | |
| HU | `kisadózó` | 12: **Pénzügyek Tudatosan** (22 d, n6, KATA/minimum wage) | Educação financeira para autônomo |
| HU | `óvodapedagógus` | 29 anúncios: Kincsek Művészeti Klub 202 d, Szukits Lite (livro de material para educadores, 32 d) | Produto de educadores existe, pequeno |
| HR | `procjena rizika`, `zaštita na radu` | 3 a 4: **Anparo** (26 d, serviço) | |
| HR | `predlošci`, `gotovi dokumenti`, `iznajmljivači` | 9 / 0 / (V1: serviço) | Zero kit |
| HR | `njegovatelj` | 11: recrutamento e cursos de cuidador (Marta Croatia 388 d) | |
| RS | `bezbednost i zdravlje na radu`, `procena rizika` | 1 e 4: Darmajf (32 d, consultoria), Lindström (51 d, EPI) | Serviço |
| RO | `evaluarea riscurilor` | 23: Centrul de Calificare (curso inspetor SSM), RiskMatrix AI (software contábil, RON), NIS2 | Curso/software |
| BG | `HACCP` | 47 anúncios, nenhum vendedor de documentos entre os 8 mais novos; sem BR, sem local | Brecha |
| NL | `modelovereenkomst` (conector) | 0 | Ninguém anuncia modelo de contrato com essa palavra hoje |
| NL | `RI&E` (conector) | 16.306 resultados: a busca tokeniza e traz ruído | Inconclusivo; usar V1 |
| DK | `egenkontrol` (conector) | 39: **wobase** (17 d, "Hvis Fødevarestyrelsen kom nu…", DKK, software), Enos Restaurant Management (17 d), Edokumentation | Software |
| AT | `Personenbetreuung` (conector) | 24: **Miina** (EUR, 10+ anúncios, 0 a 5 d: "Aufträge in deinem Bezirk", "Betreuen statt Kunden suchen") | Plataforma para cuidadoras autônomas; sem kit |
| AT/CH | `HACCP Vorlage` (conector) | 0 | Zero |
| AT/CH | `HACCP` (conector) | 180 resultados, só **Blaze IQ** (CHF, etiquetas digitais), vagas de cozinheiro | Software |

**Udvarfalvi Munkabiztonsági és Tűzvédelmi Iroda** (page_id 978606075526402), HU, HUF. Anúncio ativo mais antigo visível: **~29 d** (início 25/09/2026): "Holnapra kell a kockázatértékelés? Már ma este kész lehet." Loja **expresszmunkavedelem.hu/shop** (aberta por WebFetch em 30/10): downloads digitais .zip, IVA 0%. Pacotes **39.900 / 49.900 / 69.900 / 99.900 / 149.900 / 199.900 Ft** (Express Bázis a Ultima) e avulsos **7.900 Ft** (planilha de acidente de trabalho, Excel), **8.900 Ft** (coleção de modelos), **14.990 Ft** (temas de treinamento editáveis), **16.990 Ft** (avaliação de riscos geral com checklists, e a de construção), **24.990 Ft** (química, evacuação em Excel), **32.900 Ft** (coleção de avaliações prontas). Câmbio ~395–400 Ft/€ (**VERIFICAR**): pacotes de ~€100 a €500, avulsos de ~€20 a €83. É **prova de que pequena empresa húngara compra documento digital de segurança do trabalho**, mas a um ticket 4 a 20 vezes maior que o nosso, sem app. Só vi 1 anúncio; a idade da página e o nº de anúncios totais: **VERIFICAR**.

---

## 6. Brechas encontradas, uma a uma (país × profissão: quem vende e há quantos dias)

Legenda: **P** = prova (vendedor no país/moeda há 30+ d com kit/produto comparável); **T** = teste (sinal sem vendedor antigo); **S** = só serviço, software ou curso vendem; **0** = ninguém anuncia. "V1" = número da V1 de 29/10 que não foi remedido hoje.

| # | País | Profissão / norma | Quem vende (dias, moeda) | Tipo |
|---|---|---|---|---|
| 1 | **GR** | Restauração: HACCP + treinamento ΕΦΕΤ | Cursos ΕΦΕΤ: DP Studies 272 d, ΚΕΠΕΘ 140 d, Smarteching 133 d (EUR). Livro ilustrado BR em USD: Studio Facile ~1 d, PictoStudy ~1 d. **Pasta de documentos: ninguém** | S + T |
| 2 | **GR** | Fisioterapeuta, educadora de infância, documentos prontos, avaliação de risco | 0 anúncios com as frases locais | 0 |
| 3 | **GR** | Aluguel de curta duração (requisitos de 01/10/2025, multa €5–20 mil, imprensa) | Property managers 16 a 154 d (serviço). Kit: ninguém | S |
| 4 | **HU** | Segurança do trabalho (avaliação de riscos, treinamentos, evacuação) | Udvarfalvi ~29 d, HUF, 7.900 a 199.900 Ft (docs digitais); MUBI 91 d (software, V1); Kappel 30 d (serviço). **Kit a €19–27 por setor: ninguém** | P (preço alto) |
| 5 | **HU** | HACCP | Kiss Anett 178 d (consultoria), Minerva 91 d (curso), haccpvédelem 46 d (?), Testo 18 d (software); AHACCP.ai e Sattva ~0,1 d. Andrei Kowalski: página HU pronta (5.490 Ft), **0 anúncios** | S + T |
| 6 | **HU** | Cabeleireiro e estética (48.141 empresas) | Sem busca local com resultado nesta rodada (`kozmetikus`, `fodrász` não rodaram: cota). Nenhum vendedor visto | 0 (**VERIFICAR**) |
| 7 | **CZ** | Cosmética, cabeleireiro, manicure, tatuagem: provozní řád (multa até 1–3 mi Kč) | `provozní řád` 1 anúncio (academia), `kadeřn` 0. Sem vendedor de kit | 0 |
| 8 | **CZ** | HACCP / higiene alimentar | **Andrei Kowalski** ~4–5 d, USD, 369 Kč, 3 versões (café, restaurante, padaria); Studio Facile/Studio Digitale livros ilustrados ~1–2 d; Gastro poradenství 4 d (V1) | T (concorrência direta) |
| 9 | **SK** | HACCP | Andrei Kowalski ~4 d (12,90 a 15,99 €); Sanitas Food Safety (consultoria, <1 d) | T |
| 10 | **SK** | Segurança do trabalho / empregador | Poradca podnikateľa (modelos + €27/mês, V1), MG Group 154 d (checklist, serviço, 1 anúncio) | S/T |
| 11 | **RO** | HACCP | Andrei Kowalski ~4 d (74 lei, "Mâine vine controlul DSVSA"); Studio Digitale ~2 d; PictoStudy | T |
| 12 | **HR / RS** | HACCP | Andrei Kowalski: página `na zidu` pronta (12,90 €), 0 anúncios; sem vendedor local visível | 0 / T iminente |
| 13 | **BG** | HACCP / ХАСЕП | Nenhum vendedor entre os anúncios vistos (47); sem BR; Studio Digitale não visto em BG | 0 |
| 14 | **SI** | HACCP | Andrei Kowalski: página `na steni` pronta (12,90 €); sem anúncios vistos | T iminente |
| 15 | **NL / BE** | HACCP | Software: Apprendo Horeca, appHoreca, Octopus HACCP (22 d, FR). Kit: ninguém | S |
| 16 | **AT / CH** | HACCP | Blaze IQ (CHF, software). `HACCP Vorlage`: 0 | S |
| 17 | **NL** | ZZP / falso autônomo (multas voltam 01/01/2027) | V1: Sparsi 183 d, Polanski 70 d, Etcijfera 4 d (EUR, serviço/contador); `modelovereenkomst` 0 hoje. Kit: ninguém | S |
| 18 | **NL** | RI&E | V1: só software e consultoria. Remedição hoje inconclusiva (ruído) | S |
| 19 | **AT** | Cuidadoras 24 h (Personenbetreuung, ~57 mil, 98% de RO/SK/HR/HU) | Miina (plataforma, EUR, 0–5 d); Red Bear Digital (EUR) vende treino de memória para idosos **139 d** (1 anúncio; a página tem 5: livro infantil "Sophie & Wuschelwoo" ~9 d, Airfryer Kochbuch XXL ~67 d). Kit de documentos para cuidadora: ninguém | S + P fraco (idosos) |
| 20 | **AT/CH** | Assistência social a idosos (atividades) | The Resource Lab e Jaunty Adored (BR, USD, D0 na V1) | T |
| 21 | **DK, NO, FI, SE** | Autocontrole alimentar (egenkontrol / internkontroll / omavalvonta) | wobase 17 d e Enos 17 d (DKK, software); Firesafe 65 d, Byggdagboken 80 d (V1). Kit: ninguém | S |
| 22 | **EE, LV, LT** | HACCP, avaliação de risco | Sem remedição (cota); V1: zero | 0 (**VERIFICAR**) |
| 23 | **CZ** | Cuidadores (pečovatel) | SunSet MSH 1.498 d (recrutamento), Geroneai 204 d (IA) | S |
| 24 | **HR** | Segurança do trabalho | Anparo 26 d (serviço) | S |
| 25 | **Moeda/idioma errado** | Todos os BR (Studio Facile, Studio Digitale, PictoStudy, Andrei Kowalski) | Anunciam em **USD** com preço local no checkout (CZK, Ft, lei, zł). Local vendendo em moeda local: só consultoria/curso (HUF, CZK, RON, EUR) | observação |

---

## 7. Ranking 0 a 10

**Pesos:** prova no Meta 3, tamanho 2, gancho datado 2, ticket/LTV 1,5, reaproveitamento 1,5. Concorrente direto novo (Andrei Kowalski) tira nota de HACCP em CZ/SK/RO. Mercado com CPM alto (NL, AT/CH, nórdicos) perde um pouco.

| # | País × nicho | Prova | Tamanho (Eurostat 2024) | Gancho com data | Reaproveitamento | Risco | **Nota** |
|---|---|---|---|---|---|---|---|
| 1 | **GR × HACCP + treinamento ΕΦΕΤ (restaurante, café, padaria, açougue de bairro)** | Cursos ΕΦΕΤ pagos há 3 a 9 meses; kit: ninguém; Andrei Kowalski não tem GR | **76.728** (V1 estava errada) | Υ.Α. 110581/2025 (06/05/2025) + circular de 2026 (Cat. 2α/2β), certificado 5 anos, €50 por treinando | Alto: maleta HACCP base + anexo grego + registro de treinamento | 3 BR de livro ilustrado em D0–D1; cursos ΕΦΕΤ baratos; carga horária e circular **VERIFICAR** | **7,5** |
| 2 | **NL × ZZP: dossiê DBA** | 0 kits; contadores 70–183 d | ~1,2 mi ZZP; Q88 94.510 | **01/01/2027** (confirmado em 2 fontes), `rechtsvermoeden` até €38/h | Médio (motor semáforo) | CPM alto; lei ainda mudando (Zelfstandigenwet) | **6,5** |
| 3 | **HU × segurança do trabalho por setor (kit €19–27)** | Udvarfalvi ~29 d com preço 4 a 20 vezes maior; MUBI 91 d | todo empregador (**VERIFICAR** KSH) | Contínuo (Mvt.), sem data | Médio (motor do app = simulado de inspeção) | Vendedor local pode baixar preço | **6,5** |
| 4 | **HU × HACCP** | Consultoria 178 d; locais D0; Andrei: página pronta sem anúncios | 26.370 | Nébih (sazonal) | Alto | Janela fecha em dias | **6,0** |
| 5 | **CZ × estética/cabeleireiro/tatuagem: provozní řád + KHS** | 0 vendedores | 43.396 | Lei 258/2000 §92f/§92m: multa **até 1 a 3 mi Kč**; instrução MZd 08/2025 + modelos 12/2025 | Alto (motor do dentista: esterilização, registros, consentimentos) | Modelo oficial grátis | **6,0** |
| 6 | **BG × HACCP** | Nenhum vendedor visto, nenhum BR | 19.441 | Reg. 852/2004 (contínuo) | Alto | Sem prova de demanda; CPM baixo | **5,5** |
| 7 | **AT/CH × cuidadoras/idosos (registro + atividades)** | Red Bear 139 d (EUR); Miina plataforma | AT Q88 18.567; ~57 mil cuidadoras (secundária) | Fraco | Alto (conteúdo BR traduzido) | Coordenar com agente da DE | **5,5** |
| 8 | **HR/RS/SI × HACCP** | Andrei Kowalski com página pronta, sem anúncio | HR 17.784, RS 18.317, SI 8.688 | Reg. 852/2004 | Alto | Concorrente chega primeiro | **5,0** |
| 9 | **NL/BE × HACCP** | Só software | 75.781 / 50.738 | AFSCA/NVWA (**VERIFICAR**) | Alto | CPM alto | **5,0** |
| 10 | NL × RI&E | Só software/consultoria | 76 mil horeca | Contínuo | Médio | Ferramentas grátis | 5,0 |
| 11 | CZ/SK/RO × HACCP | Andrei Kowalski D4–5, 369 Kč / 12,90 € / 74 lei | CZ 48.091, RO 29.965, SK 16.637 | Reg. 852/2004 | Alto | **Concorrente direto mais barato** | 4,5 |
| 12 | GR × aluguel de curta duração | Só serviço | **VERIFICAR** nº de AMA | 01/10/2025, €5–20 mil | Baixo | Público não é profissional | 4,5 |
| 13 | Nórdicos × egenkontrol | Só software | pequeno | Contínuo | Médio | Software forte | 3,0 |
| 14 | Bálticos × qualquer | Sem dado | pequeno | — | — | — | 2,0 |

---

## 8. Top 8 e como montar

1. **Grécia × HACCP + registro de treinamento ΕΦΕΤ.** Nenhum kit, 3 cursos pagos há 4 a 9 meses, lei de 2025 + circular de 2026.
2. **Holanda × ZZP (dossiê DBA).** Data 01/01/2027.
3. **Hungria × segurança do trabalho por setor (versão de €19–27).** O vendedor local cobra €20 a €500.
4. **Hungria × HACCP.**
5. **Rep. Tcheca × estética/cabeleireiro/tatuagem (provozní řád + simulado KHS).** Multas de até 3 mi Kč.
6. **Bulgária × HACCP.**
7. **Áustria/Suíça × cuidadoras e idosos.**
8. **Croácia/Sérvia/Eslovênia × HACCP.**

**Montagem:** uma maleta HACCP base (852/2004 + 1169/2011, 14 alérgenos, registros) com **anexo nacional**. Diferenciar da pasta "HACCP na parede" (€13–16): app com simulado de inspeção e semáforo, contador de registros, formação com certificado, não só 6 arquivos. Preço de partida €19–27 continua defensável contra €13–16 só se o app for o motivo da compra.

---

## 9. Diferenças em relação à V1 (29/10)

1. **Havia vendedor de kit de HACCP.** A V1 concluiu "nenhum vendedor de kit". Hoje: **Andrei Kowalski** (USD, concentrare.shop), pasta HACCP 6 em 1 a €12,90–15,99, 18 anúncios, 4–5 dias, 11 países com página pronta. Ainda é T (não 30 d), mas é concorrente direto.
2. **Terceira página BR de HACCP:** Studio Digitale (2 d), além de Studio Facile (1 d) e PictoStudy.
3. **Grécia tem dado Eurostat:** 76.728 empresas de restauração (V1: "fora do dataset", 47 mil IBISWorld). Dentistas GR: 11.486.
4. **Circular do ΕΦΕΤ:** confirmada em fonte secundária (Categoria 2β, baixo/médio risco obrigados a usar programas ΕΦΕΤ, certificado 5 anos). Não resolve data nem protocolo.
5. **NL:** 01/01/2027 confirmado em MKB Servicedesk (29/12/2025); VBAR perdeu a parte esclarecedora, restou o `rechtsvermoeden` (€38/h), prazo europeu 31/08/2026.
6. **CZ:** multas confirmadas no texto da lei: §92m até 1 mi Kč, §92f até 1, 2 e 3 mi Kč.
7. **HU:** apareceu um vendedor local de documentos digitais de segurança do trabalho, **29 d**, preços €20–500.
8. **Red Bear Digital:** 139 d é do anúncio de treino de memória; a página também vende livro infantil e Airfryer.
9. **O que continua igual:** nórdicos/bálticos sem kit; NL e AT/CH só com software em HACCP.

---

## 10. O que continuou VERIFICAR

- **Cota SearchAPI zerada** (10.000/10.000 em 30/10, consumida também por outros agentes). Ficaram sem medir em frase local: AT (Evaluierung, Arbeitnehmerschutz, Brandschutz, Kleinunternehmer, Registrierkasse), CH, BE (FAVV/AFSCA), NL (zzp, gastouder, kapper, BHV), SE/NO/FI, bálticos, SI, RS, BG (frases locais), HU (`kozmetikus`, `fodrász`, `bölcsőde`, `gondozó`), RO (PFA, SSM, PSI, ANSVSA). Reabrir após **08/11**.
- **Idade real das páginas** (conector só mostra os 10 a 50 anúncios mais novos): Andrei Kowalski (viu 10 de 18; mais antigo visível ~4,1 d), Udvarfalvi (1 anúncio), haccpvédelem, Poradca podnikateľa, MG Group.
- **Preço do HACCP Andrei Kowalski:** anúncio SK diz €15,99; páginas SK/HR/SI dizem €12,90; FR parece ~€19. Checkout real não aberto.
- **Preço do HACCP de Studio Facile/Studio Digitale/PictoStudy:** páginas de venda não abertas.
- **Circular ΕΦΕΤ:** PDF oficial (efet.gr/files/1497_11_02_2026_dieukrinistiki_egkiklios.pdf) não pôde ser lido (compactado); data (11/02 ou 23/06/2026) e protocolo divergem entre fontes. **ΦΕΚ 2161/Β/2025:** carga horária de 8 h e 20 h só em sites de cursos.
- **Nº de empresas por regime:** quantos restaurantes gregos caem em Cat. 2α vs 2β; nº de AMA (alojamento local) na GR; nº de empregadores por país (segurança do trabalho); gastouders NL.
- **NL:** Kamerbrief original; se o `rechtsvermoeden` foi publicado no Staatsblad até 31/08/2026; PwC deu 403 ao fetch.
- **CZ multas:** numeração dos incisos de §92f/§92m (leitura por resumo do texto da lei, sem ver os parágrafos inteiros).
- **Câmbio HUF/€** usado (~395–400).
- **AT:** nº de cuidadoras 24 h (fonte secundária, MedUni Wien), confirmar na WKO.
- **Gancho legal** de HACCP em HU/BG/HR/RS/SI (inspeções nacionais com data) e de segurança do trabalho (HU Mvt. art. 54, SK 124/2006, CZ § 102, AT ASchG § 4): artigos citados de memória na V1, não reabertos hoje.
- **Estética HU e RO**, **idosos AT/CH** (Resource Lab, Jaunty Adored): sem remedição hoje.

## Fontes

- Meta Ad Library via conector (30/10/2026) e SearchAPI (parcial). page_ids: Andrei Kowalski 1340912605769671; Studio Facile 1232011766670582; Studio Digitale 1385277191336074; PictoStudy 1450567701465873; Udvarfalvi 978606075526402; Kiss Anett 1002509339621794; Minerva 90 140704262625169; haccpvédelem 623382974191164; Testo HU 2186441621674840; Red Bear Digital 1176826475517972; Miina 594692093718899; wobase 912171438641159; MG Group 971695762909040; Poradca podnikateľa 102965609846792; Anparo 100231561683889; Blaze IQ 1143677515486709.
- Sites abertos: concentrare.shop (páginas `/pages/haccp-*`), expresszmunkavedelem.hu/shop.
- Eurostat `sbs_ovw_act` (link na seção 3). Leis e artigos nas seções 4.
