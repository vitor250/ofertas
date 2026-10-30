# Novos nichos: resto da Europa e Leste (v2, 30/10/2026)

Países: GR, CZ, SK, HU, HR, RS, BG, RO, AT, CH, BE, NL, nórdicos (SE, NO, DK, FI) e bálticos (EE, LV, LT).

## Avisos de método (ler primeiro)
- **A v1 não estava acessível.** O arquivo `3 - EU/pesquisas/novos-nichos-resto-europa-2026-10-29.md` não está neste ambiente. Usei só o que o prompt e as notas do usuário trazem dela: a conclusão "nenhum vendedor de kit com 30+ dias", os candidatos e os itens VERIFICAR.
- **SearchAPI indisponível** (sem chave aqui e sem crédito até 08/11/2026). Usei o conector Meta (`ads_library_search`), que só mostra anúncios ATIVOS.
- **Dias reais** = 30/10/2026 menos o `ad_delivery_start_time` mais antigo entre os anúncios ativos da página, consultando por `page_ids`.
  - Limite do conector: ele devolve no máximo 50 anúncios, os mais recentes primeiro.
  - Em páginas com mais de 50 ativos (Studio Facile 920, Digital solutions 251, Nova Skills 191, Studio Digitale 166), filtrei por termo dentro da página para medir a idade do produto. A idade da página inteira ficou sem medir.
- **Páginas de vendas não abertas.** O WebFetch está bloqueado pela rede desta sessão: deu ENOTFOUND em ahaccp.ai e edupedu.ro. Preço, plataforma, bumps e garantia dos concorrentes ficaram VERIFICAR.
- **Busca web encerrada antes do fim.** A cota compartilhada de buscas web acabou no meio da verificação de normas. Os itens restantes estão marcados VERIFICAR.

## Resumo e diferenças em relação à v1
1. **A v1 errou num ponto. Há vendedor de kit com 30+ dias na Romênia, para professor (RON).**
   - Școala Românească, astăzi: "KIT ÎNVĂȚĂTOR", **87 dias**.
   - EduMagic: "4 documente profesionale 99 lei", **45 dias**, 28 anúncios.
   - O gancho é de PRAZO: o portofoliu profesional virou obrigatório em 2026–2027 (Ordin 3.858/2026).
   - Há dinheiro carimbado para gastar: o prêmio de 1.500 lei vem num cartão Pluxee e vale até 31/08/2027.
   - Esse nicho não estava na lista de candidatos da v1.
2. **No resto, a v1 se confirma.** Ninguém vende kit com 30+ dias, nos idiomas locais, em HACCP (GR, CZ, SK, HU, RO, HR, BG, NL, BE, AT, CH, nórdicos, bálticos), RI&E, ZZP/DBA, provozní řád ou aluguel curto.
3. **O que mudou desde 29/10 foi uma onda de operadores de fora, todos cobrando em USD.**
   - **Andrei Kowalski** vende uma pasta HACCP para café e bistrô em SK, CZ, RO e FR, com 12 dias. É exatamente a ideia "maleta HACCP base + anexo nacional".
   - Megalojas multi-idioma entraram entre 27 e 29/10: Studio Facile, Studio Digitale, Nova Skills e Digital solutions, com 166 a 920 anúncios cada. O "Digital solutions" da v1 vende "+70 documentos para o consultório" em BG, GR e HU (desde 27/10, 3 dias).
   - Também entrou um gerador de HACCP por IA na Hungria (AHACCP.ai / Sattva Guidance, 0–1 dia).
4. **Idosos estão perto de virar PROVADO.**
   - Creative Box: 450 atividades para idosos em RO e HU, **23 dias**.
   - Kufřík aktivizace ("maleta de ativação"): CZ, em EUR, 6 dias.
   - Mozkové müsli: nativo da CZ, 16 dias.
5. **Grécia: há demanda provada de treinamento obrigatório EFET**, com cursos anunciados há 87 a 271 dias, mas zero kit.
   - O curso em si exige provedor aprovado pela EFET (Υ.Α. 110581/2025, mínimo de 20 h, taxa de €50 por aluno).
   - Um kit low ticket não substitui o curso. Serve como complemento: pasta HACCP de pequeno negócio e preparação.

## Ranking 0–10 (régua: PROVADO / TESTE / PRAZO / BRECHA)

| # | Nicho e país | Nota | Classe | Por quê | Próximo passo |
|---|---|---|---|---|---|
| 1 | **Kit do Professor (învățător/profesor): portofoliu profesional + planificări + evaluare + app, Romênia** | **7,5** | PROVADO + PRAZO | 2 nativos ativos há 45–87 dias em RON. Portfólio obrigatório desde 2026–2027 (Ordin 3.858/2026), conta para definitivat, gradații e inspecții. >180 mil professores receberam 1.500 lei no Pluxee; até 35% (525 lei) pode ir para material e assinaturas, prazo de uso 31/08/2027. O formato documentos + app encaixa direto. | VERIFICAR o preço do KIT ÎNVĂȚĂTOR e da EduMagic, checkout em RON e se dá para aceitar o cartão Pluxee (exige ser comerciante credenciado?). Oferta: "Portofoliul profesional gata în 1 weekend". Janela: nov/2026–ago/2027. |
| 2 | **Maleta HACCP para café/bistrô (base + anexo nacional): RO, CZ, SK, GR, HU** | **6,0** | TESTE (concorrente com 12 d) | Andrei Kowalski testa em 4 países ("Mâine vine controlul DSVSA", "Kde máte zložku HACCP?"). A GR tem demanda paga provada por cursos EFET. Ninguém nativo vende pasta pronta. Risco: onda de e-books ilustrados (Studio Facile/Digitale) e IA (AHACCP.ai) entrando agora. | Re-checar Andrei Kowalski em **17–18/11** (faz 30 d). Se continuar ativo, sobe para PROVADO e a nota vai a 7. Diferencial: anexo legal por país (DSVSA/ANSVSA RO, KHS/SZPI CZ, ÚVZ/ŠVPS SK, EFET GR, Nébih HU) + app de registros diários (temperatura, limpeza). |
| 3 | **Maleta de atividades para idosos / aktivizační pracovník em lar: CZ, RO, HU** | **6,0** | TESTE quase PROVADO | Creative Box com 23 d (RO+HU, USD); Kufřík aktivizace 6 d (CZ, EUR); Mozkové müsli 16 d (CZ, nativo). As notas de 28/10 já marcavam "estimulação cognitiva: nenhum nativo vende" como repetida entre países. | Re-checar Creative Box em **06–07/11**. Se seguir ativo, vira PROVADO. Produto: atividades por nível + fichas de registro de atividade (documentação do lar) + app. |
| 4 | **Psicólogo Eslováquia (lei 242/2025)**, da fila de 29/10 | **4,5** | BRECHA/TESTE | Rechecado: "psychológ dokumentácia" SK+CZ = 0 anúncios. Segue sem vendedor. | Mantém a posição da fila. |
| 5 | **Provozní řád pronto + pasta de inspeção KHS: cabeleireiro, manicure, pedicure, estética, massagem (CZ; SK "prevádzkový poriadok")** | **4,5** | BRECHA + gancho | Obrigatório pelo §21(3) da lei 258/2000 Sb., e a atividade não começa sem aprovação da KHS. O Ministério da Saúde passou a exigir o kolaudační souhlas (vistoria do imóvel) em 2025. Zero vendedor (CZ 21 resultados sem relação; SK 1). Contra: o próprio Ministério publicou modelo grátis (12/2025). | Só faz sentido como "Kufřík kadeřnice/kosmetičky" com mais documentos (registros de desinfecção, plano de limpeza, FAQ da vistoria). Faixa de multas VERIFICAR. |
| 6 | **Kit ZZP / opdrachtgever (dossiê anti-schijnzelfstandigheid): Holanda** | **4,5** | BRECHA + PRAZO | Em 2026 não há verzuimboete; a partir de **01/01/2027** a Belastingdienst volta a aplicá-la. O rechtsvermoeden (≤ €38/h) talvez valha desde 31/12/2026. Ninguém vende kit pago: só whitepaper grátis (Bndle), app (Etcijfera) e consultoria (Sparsi). Contra: holandês compra software e consultoria, e existem modelovereenkomsten grátis. | Teste barato só se houver tradutor jurídico NL. Datas exatas VERIFICAR. |
| 7 | **"+70 documentos do consultório" (médico/clínica): BG, GR, HU** | **4,0** | TESTE (3 d) | Digital solutions (USD) começou em 27/10, com consentimentos de estética ("16 лечения. 16 съгласия"). Sem prova. | Re-checar em 26–28/11. |
| 8 | **Preparação EFET + pasta HACCP de pequeno negócio: Grécia** | **4,0** | Demanda provada (cursos), kit = BRECHA | Cursos de 87 a 271 dias (DP Studies, KEK KEPETh, Smarteching). Mas o curso obrigatório só pode vir de provedor aprovado pela EFET. Só existe espaço para material de apoio, não para o curso. | Se fizer a maleta HACCP (#2), a GR entra como anexo nacional. Se existe prova/exame final e qual é o formato: VERIFICAR. |
| 9 | **Aluguel curto (Airbnb host): GR, HR** | **3,0** | Sem prova de kit | GR: só seminário por assinatura (Ευδόκιμος, "Airbnb & βραχυχρόνιες μισθώσεις, €25/mês", **57 d**) e gestoras. HR: construtores de site e agências. | Baixa prioridade. Normas gregas de STR 2025/2026 VERIFICAR. |
| 10 | **RI&E (avaliação de riscos): NL** | **2,0** | BRECHA fraca | 10 anúncios, nenhum vendedor. A RI&E costuma ser feita com ferramentas setoriais (VERIFICAR). | Descartar por ora. |
| 11 | **Nórdicos, bálticos, AT, CH, BE** (HACCP/egenkontroll) | **1,5** | Nada | Só SaaS (Quality Guard, Apprendo, Blaze IQ), cursos (Firesafe 65 d) e suplementos. | Descartar. |

**Candidatos da v1 sem anúncio:** PictoStudy (0 anúncios ativos).

## 1. Contraprova da v1 por idioma local (conector Meta, só ATIVOS, 30/10)

### 1.1 HACCP / higiene alimentar
| Busca | País | Total | Anunciantes relevantes | Dias reais | Moeda | Leitura |
|---|---|---|---|---|---|---|
| "HACCP" | GR | 91 | Studio Facile (e-book "Το HACCP, με εικόνες"); Apopsi Group (certificação EFET); TQS Group; Laba (curso) | Studio Facile: anúncios HACCP todos de 29/10 (≤1 d). A página tem 920 ativos em ~10 idiomas (bomba de calor, solda, primeiros socorros, unhas, nutrição) | USD | Onda nova de e-books ilustrados. Não prova. |
| page Studio Facile + "HACCP" | todos | 31 | Studio Facile (IT, PL, CZ, GR, PT, TR, AR) | todos de 29/10 | USD | Teste em massa. |
| "ΕΦΕΤ" | GR+CY | 21 | Só cursos de certificação (Σεμινάριο ΕΦΕΤ nível 1): DP Studies, Ινστιτούτο Ανάπτυξης Απασχόλησης, ΚΕΚ ΚΕΠΕΘ, Smarteching Education, ΚΔΒΜ Προσόν, EUROTRAINING.edu, ΚΕΚ ABC; Kitchen Pro = loja de equipamento | DP Studies 271 d; Ινστιτούτο 140 d; ΚΕΚ ΚΕΠΕΘ 139 d; Smarteching 132 d; Kitchen Pro 99 d; ΚΔΒΜ Προσόν 87 d; ABC 38 d | EUR | Demanda PROVADA por treinamento. Nenhum kit. |
| "φάκελος HACCP" / "HACCP έντυπα" | GR+CY | 0 / 4 | Só Studio Facile | ≤1 d | USD | BRECHA de kit em grego. |
| "εκτίμηση επαγγελματικού κινδύνου" | GR+CY | 2 | M.A. Hadjiyiannis Training (curso, Chipre) | – | EUR | BRECHA (avaliação de risco ocupacional). |
| "HACCP" | CZ+SK | 141 | **Andrei Kowalski** (pasta HACCP "zložka/dosar" para café/bistrô); **Studio Digitale** ("Hygiena potravin v obrázcích"); MVDr. Ivana Slamená – Sanitas Food Safety (consultora SK); Gastro poradenství ("HACCP na míru", consultoria); Laba Czech (curso) | Andrei Kowalski: 17 ativos, o mais antigo de 18/10 → **12 d** (SK, CZ, RO, FR). Studio Digitale: 166 ativos, todos de 28–29/10, multinicho (inclui "84 stran pro zubní ordinaci") | USD | Pasta HACCP multipaís em TESTE. |
| "HACCP" | RO | 79 | Andrei Kowalski ("Mâine vine controlul DSVSA. Aveți dosarul pregătit?", "Planul HACCP pe perete, nu în sertar", "Dosar de igienă pentru cafenea și bistro"); Studio Digitale; SGS | 12 d / ≤2 d | USD | Nenhum nativo. |
| "HACCP" | HU+HR+RS+BG+SI | 212 | **Sattva Guidance** ("HACCP készítés egyszerűen") e **AHACCP.ai** ("Rendelj professzionális HACCP-t") | 1 ativo cada, ambos de 29/10, criados no mesmo segundo (mesmo operador) → 0–1 d | HUF | Gerador por IA entrando. TESTE. |
| "HACCP" | NL+BE+AT+CH | 413 | Só SaaS: Quality Guard ("Digitaliseer voedselveiligheid"), Apprendo Horeca, Blaze IQ ("Digitale HACCP-Etiketten", CHF); vagas; indústria | – | EUR/CHF | Mercado de software. |
| "HACCP" | EE+LV+LT+FI+SE+DK+NO | 159 | Suplementos, indústria, vagas | – | – | Nada. |
| "egenkontroll" | SE+NO+DK | 8 | Firesafe (curso de autocontrole de incêndio, NO), Byggdagboken (app), UTAB Miljö | Firesafe 65 d | NOK/SEK | Nada de higiene. |
| "PictoStudy" | todos | 0 | – | – | – | Saiu do ar. |

### 1.2 Estética: provozní řád / prevádzkový poriadok
| Busca | País | Total | Achado | Leitura |
|---|---|---|---|---|
| "provozní řád" | CZ | 21 | Restaurante, imóveis, carros, academia. Nenhum vendedor de documento | BRECHA |
| "prevádzkový poriadok" | SK | 1 | MG Group ("Získajte prehľad zdarma", 153 d, EUR, serviço) | BRECHA |

### 1.3 Holanda: RI&E e ZZP/DBA
| Busca | País | Total | Achado | Leitura |
|---|---|---|---|---|
| "risico-inventarisatie" | NL+BE | 10 | Vagas, cosmético, Simple Check, Incontroll BV | Nenhum vendedor de modelo RI&E. |
| "modelovereenkomst zzp" | NL | 0 | – | Ninguém anuncia contrato-modelo. |
| "zzp schijnzelfstandigheid" | NL | 12 | Etcijfera (app: "Zzp'ers inhuren? Dit verandert op 31 december", "Rechtsvermoeden voor zzp'ers onder € 38 per uur", "Einde coulance schijnzelfstandigheid"); Bndle (whitepaper grátis "Zzp-inhuur 2026 & 2027"); Sparsi.nl; Polanski | Gancho de PRAZO usado só como isca grátis B2B. Nenhum kit pago. |

### 1.4 Idosos / estimulação cognitiva / ativação em lares
| Busca | País | Total | Anunciante | Dias reais | Moeda | Leitura |
|---|---|---|---|---|---|---|
| "stimulare cognitivă" | RO+MD | 30 | **Creative Box** ("Peste 450 de activități de stimulare pentru vârstnici"; em HU "Több mint 450 stimulációs feladat időseknek"); Nova Skills (megaloja, "12 volume · 1.600 de exerciții") | Creative Box: 5 ativos; página desde 21/09 (38 d, com kit de autismo); kit de idosos RO/HU desde 07/10 → **23 d**. Nova Skills: 191 ativos, criativo de idosos desde 11/10 (19 d) | USD | Perto de PROVADO. |
| "időseknek feladatok" / "memóriatréning" | HU | 0 / 0 | – | – | – | Nenhum nativo. |
| "trénink paměti" | CZ+SK | 22 | **Kufřík aktivizace** ("520 hotových aktivit pro seniory", "50 her pro celou skupinu"); **Mozkové müsli – trénink paměti** (nativo); Emilia Zabala ("Přes 1 200 úloh pro bystrou mysl"); Jana Laštovičková Art; Vitanest | Kufřík: 3 ativos, desde 24/10 → **6 d** (EUR). Mozkové müsli: 8 ativos, desde 14/10 → **16 d** (CZK). Emilia Zabala 14 d (USD). Jana Laštovičková 52 d (curso de arte, não é kit profissional) | EUR/CZK/USD | "Maleta" para ativação em lar acabou de entrar na CZ. TESTE. |

### 1.5 Romênia: professor (achado novo da v2)
| Busca | Anunciante | Dias reais | Nº ativos | Moeda | Oferta (texto do anúncio) |
|---|---|---|---|---|---|
| "documente gata completate", "planificări" | **Școala Românească, astăzi** (nativo, loja própria "Magazin") | **87 d** (desde 03/08/2026) | 2 | RON | "KIT ÎNVĂȚĂTOR – Portofoliu, planificări și evaluare, învățământ primar 2026–2027" |
| "portofoliul profesional" | **EduMagic** (nativo) | **45 d** (desde 14/09/2026) | 28 | RON | "Până la 4 documente profesionale 👉 99 lei, în loc de 199 lei. Poți plăti și cu cardul Pluxee"; "Un an întreg la 119 lei 👉 Cumpără cu prima didactică" |
| idem | eduagenda.ro | 0–1 d | – | RON | (sem texto) |
| "tanmenet" (HU, comparação) | Tus Beneficios, Kinetika Group (ARS), Nexa Hogar: materiais de aula em húngaro | ≤10 d | – | USD/ARS | Na Hungria o professor só tem operadores LATAM/BR novos. "pedagógus portfólió" = 0. |

### 1.6 Aluguel curto
| Busca | País | Total | Achado | Leitura |
|---|---|---|---|---|
| "βραχυχρόνια μίσθωση" | GR | 17 | Ευδόκιμος (seminário online, "Airbnb & Βραχυχρόνιες μισθώσεις", €25/mês, **57 d**); gestoras (L&M, Polis Guest, Perla Homes); Hosthub (SaaS) | Demanda por curso, não por kit. |
| "iznajmljivači apartmana" | HR+ME+SI | 30 | Svijet poduzetništva (site grátis para locador), NOVASOL, agências | Nada de kit. |

### 1.7 Operadores multinicho que entraram em 27–29/10 (todos USD, persona local)
| Página | Ativos | O que vende na região | Idade medida |
|---|---|---|---|
| Studio Facile | 920 | E-books ilustrados: HACCP, primeiros socorros, solda, bomba de calor, fotovoltaica, contabilidade (GR, CZ, PL, PT, IT, DK, TR, AR) | Recortes HACCP e CZ: 29/10 |
| Digital solutions (candidato da v1) | 251 | "+70 έτοιμα έγγραφα για το ιατρείο" (GR), "Кабинет в ред – +70 готови документа" (BG), "Rendelő Rendben – +70 kész dokumentum" (HU), "16 лечения. 16 съгласия", mapas de farmacologia | Recorte "+70": desde 27/10 (3 d) |
| Nova Skills | 191 | Farmacologia, idosos (RO), construção ("−92% la pachetul complet de management în construcții", "Devize… 79 lei"), mecânicos (BG) | Idosos 19 d; resto 28–29/10 |
| Studio Digitale | 166 | Higiene de cozinha (CZ, RO), dentista "84 stran pro zubní ordinaci", hidráulica, anatomia, psicologia | 28–29/10 |
| Andrei Kowalski | 17 | Pasta HACCP para café/bistrô (SK, CZ, RO, FR "inspecteur de la DDPP") | **12 d** |

## 2. Normas e tamanho de mercado (busca web, com URL)

### Grécia: treinamento obrigatório em higiene (Υ.Α. 110581/2025)
- **O que é a Υ.Α. 110581/2025.** Ministério do Desenvolvimento Rural e Alimentação, ΦΕΚ Β' 2161 de 06/05/2025. Cria o marco único de treinamento obrigatório do pessoal de empresas de alimentos.
- **Quem precisa treinar.** As empresas obrigadas a ter HACCP completo treinam quem manipula alimentos, aplicando obrigatoriamente os programas da EFET.
- **Provedores.** Precisam se registrar no arquivo de provedores aprovados da EFET, por plataforma eletrônica. Os pedidos começaram em 01/09/2025, para programas de 2026.
- **Duração e taxa.** O curso dura no mínimo 20 h. Taxa de €50 por aluno desde 01/09/2025.
- Fontes:
  - https://www.e-nomothesia.gr/kat-agoranomikes-diatakseis/ya-110581-2025.html
  - https://www.taxheaven.gr/circulars/50255/110581-25-04-2025
  - https://mitos.gov.gr/index.php/ΔΔ:Εκπαιδευτικά_Προγράμματα_Κατάρτισης_προσωπικού_επιχειρήσεων_τροφίμων
  - https://pin.gov.gr/wp-content/uploads/2025/07/ΕΝΗΜΕΡΩΣΗ.pdf
- **Circular EFET nº 7151 de 23/06/2026:** citada por terceiros. Conteúdo VERIFICAR.
- **Número de empresas de restauração (NACE 56):** 80.412 em 2019, segundo agregador que cita a Eurostat (https://d3fqfiq2w1ez7u.cloudfront.net/nmx/timeseries/greece-number-of-enterprises-of-food-and-beverage-services). O número oficial atual da ELSTAT não foi achado: **VERIFICAR**.

### Tchéquia: provozní řád (lei 258/2000 Sb.)
- **Quem precisa ter.** O §21(3) obriga a ter provozní řád quem opera holičství, kadeřnictví, manikúra, pedikúra e serviços kosmetické, masérské, regenerační a rekondiční. Estão entre as "atividades epidemiologicamente relevantes".
- **Aprovação antes de abrir.** A atividade não pode começar antes da aprovação definitiva pela KHS.
- **Vistoria do imóvel (2025).** O Ministério da Saúde publicou orientação: para aprovar o provozní řád é preciso apresentar o kolaudační rozhodnutí/souhlas.
  - https://mzd.gov.cz/wp-content/uploads/2025/02/MN-ke-schvaleni-PR-a-predlozeni-kolaudacniho-rozhodnuti.pdf
  - https://mzd.gov.cz/wp-content/uploads/2025/08/Vyklad-ke-schvaleni-PR-a-dolozeni-kolaudacniho-souhlasu.pdf
- **Modelo grátis do Ministério** (12/2025): https://mzd.gov.cz/wp-content/uploads/2025/12/PROVOZNI-RAD-VZOR_Kosmeticke-sluzby.doc
- **Multas da lei 258/2000:** a faixa "10 mil a 3 milhões Kč" aparece só numa aula da MU sem data. **VERIFICAR** no texto consolidado (e-Sbírka).
- **Número de salões na CZ:** **VERIFICAR**.

### Holanda: ZZP / VBAR / fim da "zachte landing"
- **VBAR encolheu.** Ficou só a parte do rechtsvermoeden: presunção de vínculo empregatício para quem cobra ≤ €38/h (referência 01/01/2026).
  - https://www.grantthornton.nl/insights/legal-services/wet-dba/zzp-wetgeving-in-beweging-verduidelijkingsdeel-vbar-vervalt-kabinet-werkt-aan-nieuwe-zelfstandigenwet/
- **Data de vigência incerta.** As fontes divergem: PwC fala em 01/07/2026, outras em 01/01/2027, e De Zaak em 31/12/2026.
  - https://www.pwc.nl/nl/actueel-en-publicaties/belastingnieuws/loonbelasting-en-sociale-verzekeringen/wetvbarnaartweedekamer.html
- **Fiscalização.**
  - A moratória acabou em 01/01/2025.
  - Em 2026 não há verzuimboete. A vergrijpboete já pode ser aplicada: 25% por culpa grave, 50% por dolo.
  - A verzuimboete volta em **01/01/2027**.
  - https://www.pwc.nl/nl/actueel-en-publicaties/belastingnieuws/loonbelasting-en-sociale-verzekeringen/handhaving-schijnzelfstandigen-vanaf-tweeduizendzesentwintig.html
  - https://dezaak.nl/personeel/schijnzelfstandigheid/hoe-gaat-de-belastingdienst-controleren-op-schijnzelfstandigheid-5-dingen-die-je-moet-weten/
  - https://www.mkbservicedesk.nl/nieuws/ondernemersnieuws/handhaving-schijnzelfstandigheid-in-2026-dit-is-wat-er-verandert-en-wat-niet
- **A Kamerbrief mais recente não foi lida: VERIFICAR.** Número de ZZP'ers (CBS): VERIFICAR.

### Romênia: portfólio do professor e prêmio Pluxee
- **Portofoliu profesional (Ordin nr. 3.858/2026).**
  - Metodologia-quadro publicada no Monitorul Oficial em 08/05/2026.
  - Obrigatório a partir de 2026–2027 para professores, diretores e inspetores.
  - Conta para definitivat, gradații, inspecții e avaliação anual.
  - Cada escola aprova, em até 60 dias, o próprio procedimento e o calendário de entrega.
  - Dados falsos geram responsabilidade disciplinar.
  - https://isj.vs.edu.ro/download/Ordin-Nr.-3.8582026-Portofoliu-profesional-pentru-profesori-directori-inspectori.pdf
  - https://www.edupedu.ro/oficial-din-anul-scolar-2026-2027-toti-profesorii-sunt-obligati-sa-depuna-portofoliul-profesional-care-va-conta-la-definitivat-gradatii-si-inspectii-ce-documente-trebuie-sa-contina/
  - https://alba24.ro/profesorii-obligati-sa-depuna-portofoliul-profesional-din-anul-scolar-2026-2027-la-ce-foloseste-si-ce-documente-va-contine-1135713.html
- **Prima de carieră didactică.**
  - 1.500 lei líquidos no cartão Pluxee.
  - No mínimo 65% (975 lei) vai para cursos credenciados. O resto pode ir para livros, assinaturas de plataformas educacionais e material didático.
  - Vale até 31/08/2027 para quem segue no ensino.
  - Mais de 180 mil beneficiários.
  - Uma manchete diz que é "a última prima pelo esquema atual".
  - https://www.edupedu.ro/prima-de-cariera-didactica-de-1-500-de-lei-calendarul-termenelor-si-regulile-pentru-profesori-este-ultima-prima-acordata-prin-actuala-schema-iar-minimum-975-de-lei-trebuie-folositi-pentru-cursuri/amp/
  - https://www.edupedu.ro/plata-primei-de-cariera-didactica-2026-a-fost-finalizata-anunta-ministerul-investitiilor-si-proiectelor-europene-peste-180-000-de-beneficiari-au-primit-cate-1-500-de-lei/amp/
  - https://www.edupedu.ro/oficial-prima-de-cariera-didactica-2026-profesorii-primesc-cei-1-500-de-lei-pana-la-31-august-si-ii-pot-folosi-pana-in-august-2027-daca-raman-in-invatamant/

## 3. Calendário de re-checagem (conector Meta, por page_id)
| Data | O quê | page_id | Vira o quê se seguir ativo |
|---|---|---|---|
| 06–07/11 | Creative Box (idosos RO/HU) | 1371420822713599 | PROVADO idosos RO/HU |
| 13/11 | Mozkové müsli (CZ) | 533669319834982 | Sinal nativo de 30 d |
| 17–18/11 | Andrei Kowalski (HACCP café/bistrô SK/CZ/RO/FR) | 1340912605769671 | PROVADO maleta HACCP multipaís |
| 23/11 | Kufřík aktivizace (CZ, EUR) | 1429706453550641 | PROVADO maleta de idosos CZ |
| 26–28/11 | Digital solutions "+70 documentos" (BG/GR/HU); AHACCP.ai/Sattva (HU) | 1406571882531997; 1242269788975227; 358789431514149 | TESTE vira PROVADO |
| Sempre | Școala Românească, astăzi; EduMagic | 105284268360774; 337381659683337 | Confirmar que continuam (já PROVADO) |

## 4. Lista final de VERIFICAR
1. **Romênia, professor.** Preço e conteúdo do "KIT ÎNVĂȚĂTOR" (Școala Românească astăzi) e da EduMagic ("4 documente 99 lei", assinatura 119 lei/ano). Plataforma, bumps e garantia (páginas não abertas: WebFetch bloqueado).
2. **Romênia, meio de pagamento.** Um vendedor estrangeiro consegue receber pelo cartão Pluxee da prima didactică (credenciamento de comerciante)? A Hotmart, ou outra plataforma, cobra em RON?
3. **Romênia, documentos exigidos.** Lista exata das 5 seções do portofoliu profesional (Ordin 3.858/2026) e se há modelo oficial grátis do Ministério ou das ISJ (risco de concorrência gratuita, como na CZ).
4. **Romênia, ano letivo seguinte.** A prima didactică continua em 2026–2027? Uma manchete diz que é "a última pelo esquema atual".
5. **Grécia, circular EFET nº 7151/23-06-2026:** conteúdo e se cria obrigação nova para pequenos estabelecimentos.
6. **Grécia, nº atual de empresas de restauração (ELSTAT/Eurostat, NACE 56).** Só há 80.412 (2019, agregador).
7. **Grécia, curso EFET:** existe exame final? Formato?
8. **Grécia, avaliação de riscos:** artigo que obriga a γραπτή εκτίμηση επαγγελματικού κινδύνου (provável ν. 3850/2010, art. 43) e multas. Não confirmado: a busca web acabou.
9. **Grécia, aluguel curto:** normas de segurança e registro (ΑΜΑ) 2025/2026 e multas.
10. **Tchéquia, multas da lei 258/2000 Sb.** para falta ou não cumprimento do provozní řád. Faixa "10 mil a 3 milhões Kč" sem data.
11. **Tchéquia, mercado:** nº de salões (kadeřnictví, kosmetika, pedikúra) e nº de aktivizační pracovníci / lares de idosos.
12. **Holanda:** Kamerbrief VBAR mais recente; data exata do rechtsvermoeden (31/12/2026, 01/07/2026 ou 01/01/2027); confirmação de que a verzuimboete volta em 01/01/2027; nº de ZZP'ers (CBS).
13. **Holanda, RI&E:** obrigação para quem tem 1+ funcionário, ferramentas setoriais grátis e exceções.
14. **Concorrentes sem página aberta:** preço e conteúdo de Andrei Kowalski (pasta HACCP), AHACCP.ai/Sattva (HUF), Creative Box (idosos), Kufřík aktivizace (EUR), Digital solutions (+70 documentos).
15. **Idade das páginas grandes** (Studio Facile 920, Digital solutions 251, Nova Skills 191, Studio Digitale 166). O conector só mostra os 50 anúncios mais recentes. Medir com SearchAPI depois de 08/11.
