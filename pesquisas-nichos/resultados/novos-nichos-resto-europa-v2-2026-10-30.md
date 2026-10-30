# Novos nichos: resto da Europa e Leste (v2, 30/10/2026)

Países: GR, CZ, SK, HU, HR, RS, BG, RO, AT, CH, BE, NL, nórdicos (SE, NO, DK, FI), bálticos (EE, LV, LT).

## Avisos de método (ler primeiro)
- A v1 (`3 - EU/pesquisas/novos-nichos-resto-europa-2026-10-29.md`) NÃO estava acessível neste ambiente. Usei só o que o prompt e as notas do usuário trazem dela (conclusão "nenhum vendedor de kit com 30+ dias", candidatos e itens VERIFICAR).
- SearchAPI indisponível (sem chave aqui e sem crédito até 08/11/2026). Usei o conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 menos o `ad_delivery_start_time` mais antigo entre os anúncios ativos da página (consulta por `page_ids`).
- Status: EM ANDAMENTO (arquivo gravado aos poucos).

## 1. Contraprova da v1 por idioma local

### 1.1 HACCP / higiene alimentar (log bruto, conector Meta, só ATIVOS, 30/10)
| Busca | País | Total ativos | Anunciantes relevantes | Dias reais (página) | Moeda | Leitura |
|---|---|---|---|---|---|---|
| "HACCP" | GR | 91 | Studio Facile (e-book ilustrado "Το HACCP, με εικόνες"); Apopsi Group (curso/certificação EFET); TQS Group; Laba (curso) | Studio Facile: anúncios HACCP todos de 29/10 (1 dia); página tem 920 ativos em ~10 idiomas e vários temas (bomba de calor, solda, primeiros socorros, unhas, nutrição) | USD | Onda nova de e-books ilustrados multinicho. NÃO prova. |
| page Studio Facile + "HACCP" | todos | 31 | Studio Facile (IT, PL, CZ, GR, PT, TR, AR) | todos 29/10 (≤1 dia) | USD | Teste em massa iniciado 29/10. |
| "provozní řád" | CZ | 21 | nenhum vendedor de documento (restaurante, imóveis, carros, academia) | – | CZK | BRECHA (ninguém vende provozní řád pronto em anúncio). |
| "ΕΦΕΤ" | GR+CY | 21 | Só CURSOS de certificação (Σεμινάριο ΕΦΕΤ, nível 1 "Υγιεινή και Ασφάλεια Τροφίμων"): DP Studies, Ινστιτούτο Ανάπτυξης Απασχόλησης, ΚΕΚ ΚΕΠΕΘ, Smarteching Education, ΚΔΒΜ Προσόν, EUROTRAINING.edu, ΚΕΚ ABC Success Lab; Kitchen Pro = loja de equipamento de cozinha | DP Studies 271d; Ινστιτούτο 140d; ΚΕΚ ΚΕΠΕΘ 139d; Smarteching 132d; ΚΔΒΜ Προσόν 87d; Kitchen Pro 99d; ABC 38d | EUR | Demanda PROVADA para treinamento EFET obrigatório (cursos 87–271 dias). Nenhum KIT de documentos/HACCP pronto em grego com 30+ dias. |
| "HACCP" | HU+HR+RS+BG+SI | 212 | **Sattva Guidance** ("HACCP készítés egyszerűen") e **AHACCP.ai** ("Rendelj professzionális HACCP-t"), ambos HUF; resto = indústria/suplementos/vagas | 1 anúncio ativo cada, ambos de 29/10 (criação no mesmo segundo → mesmo operador) → **0–1 dia** | HUF | Gerador de HACCP por IA na Hungria acabou de entrar. TESTE. |
| "HACCP" | RO | 79 | Andrei Kowalski ("Mâine vine controlul DSVSA. Aveți dosarul pregătit?"); Studio Digitale ("Igiena alimentară, explicată prin desene"); SGS (certificação) | ver CZ/SK (12 d) e ≤2 d | USD | Nenhum vendedor romeno nativo de dosar HACCP com 30+ dias. |
| "PictoStudy" | todos | 0 | – | – | – | Candidato da v1 sem anúncio ativo hoje. |
| "HACCP" | CZ+SK | 141 | **Andrei Kowalski** (pasta HACCP "zložka/dosar" p/ café e bistrô; SK, CZ, RO, FR); **Studio Digitale** (e-book "Hygiena potravin v obrázcích"); MVDr. Ivana Slamená – Sanitas Food Safety (consultora SK, EUR); Gastro poradenství ("HACCP na míru", consultoria, CZK); Laba Czech (curso) | Andrei Kowalski: 17 ativos, mais antigo 18/10 → **12 dias**. Studio Digitale: 166 ativos, todos 28–29/10 (≤2 dias), multinicho (dentista "84 stran pro zubní ordinaci", hidráulica, anatomia, psicologia, cogumelos) | USD | Kit-pasta HACCP para café/bistrô em teste multipaís há 12 dias (persona com nome eslavo, moeda USD = operador de fora). TESTE, não PROVADO. |

| "HACCP" | NL+BE+AT+CH | 413 | Só SaaS (Quality Guard NL/BE "Digitaliseer voedselveiligheid", Apprendo Horeca, Blaze IQ CHF "Digitale HACCP-Etiketten"), vagas e indústria | – | EUR/CHF | Mercado de software, sem kit low ticket. |
| "egenkontroll" | SE+NO+DK | 8 | Firesafe (curso de autocontrole de incêndio, NOK), Byggdagboken (app de obra), UTAB Miljö | Firesafe ~65 d | NOK/SEK | Nórdicos: nada de kit de higiene; o que existe é curso/SaaS. |

### 1.2 Holanda: RI&E e ZZP/DBA
| Busca | País | Total | Achado | Leitura |
|---|---|---|---|---|
| "risico-inventarisatie" | NL+BE | 10 | Nenhum vendedor de modelo RI&E (vagas, cosmético, "Simple Check", Incontroll BV) | BRECHA de anúncio, mas a RI&E na NL é feita com ferramentas setoriais gratuitas/reconhecidas (VERIFICAR). |
| "modelovereenkomst zzp" | NL | 0 | – | Ninguém anuncia contrato-modelo ZZP. |
| "zzp schijnzelfstandigheid" | NL | 12 | Etcijfera (app contábil: "Zzp'ers inhuren? Dit verandert op 31 december"; "Rechtsvermoeden voor zzp'ers onder € 38 per uur"; "Einde coulance schijnzelfstandigheid"), Bndle (whitepaper grátis "Zzp-inhuur 2026 & 2027"), Sparsi.nl (consultoria), Polanski | Há gancho de PRAZO sendo usado por empresas B2B (lead magnet grátis), nenhum kit pago. |

### 1.3 Idosos / estimulação cognitiva / ativação em lares
| Busca | País | Total | Anunciante | Dias reais (página) | Moeda | Leitura |
|---|---|---|---|---|---|---|
| "stimulare cognitivă" | RO+MD | 30 | **Creative Box** ("Peste 450 de activități de stimulare pentru vârstnici"; mesmo criativo em HU "Több mint 450 stimulációs feladat időseknek"); Nova Skills (megaloja multinicho, "12 volume · 1.600 de exerciții"); clínicas | Creative Box: 5 ativos; página desde 21/09 (**39 d**, mas com kit de autismo); kit idosos RO/HU desde 07/10 (**23 d**). Nova Skills: 191 ativos em ~15 idiomas, criativo de idosos desde 11/10 (19 d) | USD | Kit de atividades para idosos em teste perto de 30 dias em RO e HU. Re-checar 06–07/11 (vira PROVADO se seguir ativo). |
| "időseknek feladatok" / "memóriatréning" | HU | 0 / 0 | – | – | – | Nenhum vendedor húngaro nativo. |
| "trénink paměti" | CZ+SK | 22 | **Kufřík aktivizace** ("520 hotových aktivit pro seniory", "50 her pro celou skupinu", "Když se skupina nudí"); **Mozkové müsli – trénink paměti** (nativo); Emilia Zabala ("Přes 1 200 úloh pro bystrou mysl"); Jana Laštovičková Art (caderno de exercícios); Vitanest (centro de atividades) | Kufřík aktivizace: 3 ativos, desde 24/10 (**6 d**, EUR). Mozkové müsli: 8 ativos, desde 14/10 (**16 d**, CZK). Emilia Zabala: desde 16/10 (14 d, USD). Jana Laštovičková: 52 d (CZK, curso de arte/treino cerebral, não kit de profissional) | EUR/CZK/USD | "Kufřík" (= maleta) para aktivizační pracovník de lar de idosos acabou de entrar na CZ, em euro. Mesmo formato "maleta + atividades prontas". TESTE. |

### 1.4 Romênia: professor (achado novo da v2, não estava na lista de candidatos)
| Busca | Anunciante | Dias reais (página) | Nº ativos | Moeda | Oferta (texto do anúncio) |
|---|---|---|---|---|---|
| "documente gata completate", "planificări" (RO) | **Școala Românească, astăzi** (nativo) | **87 d** (anúncio mais antigo de 03/08/2026, ainda ativo) | 2 | RON | "KIT ÎNVĂȚĂTOR – Portofoliu, planificări și evaluare, învățământ primar 2026–2027" (loja própria "Magazin") |
| "portofoliul profesional" (RO) | **EduMagic** (nativo) | **45 d** (desde 14/09/2026) | 28 | RON | "Până la 4 documente profesionale 👉 99 lei, în loc de 199 lei. Poți plăti și cu cardul Pluxee"; "Un an întreg la 119 lei 👉 Cumpără cu prima didactică 👉 Abonamentul EduMagic" |
| idem | eduagenda.ro | 0–1 d | – | RON | (sem texto) |

Leitura: **PROVADO em RON** (2 vendedores nativos ≥45 dias), com dinheiro carimbado para gastar: a "prima de carieră didactică" de 1.500 lei vem num cartão Pluxee; até 35% (525 lei) pode ir para livros, assinaturas de plataformas educacionais e material didático, e o saldo vale até 31/08/2027 para quem segue no ensino. Mais de 180 mil beneficiários. Gancho de PRAZO: o **portofoliul profesional** passou a ser obrigatório a partir do ano letivo 2026–2027 (Ordin nr. 3.858/2026, Monitorul Oficial de 08/05/2026) e conta para definitivat, gradații e inspecții; cada escola fixa o calendário de entrega.

(continua)

## 2. Candidatos medidos
(em andamento)

## 3. Normas e tamanho de mercado (fontes oficiais)
(em andamento)

## 4. Ranking 0–10
(em andamento)

## 5. Lista final de VERIFICAR
(em andamento)
