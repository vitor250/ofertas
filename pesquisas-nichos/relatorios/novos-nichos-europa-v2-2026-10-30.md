# Novos nichos profissionais na Europa, v2 (30/10/2026)

Refeito do zero. A v1 (29/10) serviu só de lista de candidatos. Em construção: o arquivo é gravado aos poucos.

**Ferramentas desta rodada:** conector Meta `ads_library_search` (por page_id, status ACTIVE/INACTIVE/ALL) e SearchAPI `meta_ad_library` (devolve texto do anúncio, link de destino e data de início). Créditos SearchAPI em 30/10: 10.000 de franquia, 8.878 usados, sobram ~1.122 (renova em 08/11).
**Hoje = 30/10/2026 (unix 1793318400).** Dias = hoje menos a data de início de entrega mais antiga que a ferramenta mostrou.
**Régua:** PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. Espanhol neutro não prova país.

---

## A. Medição por page_id (conector Meta), correções da v1

### Kontrola Sanepidu (PL, PLN), page 388263394381460
- 70 anúncios no total (status ALL): **12 ativos hoje e 58 inativos**.
- O conector lista só os 50 mais novos por consulta. O anúncio mais antigo VISÍVEL começou em **28/01/2026 (275 dias)**. Há ~8 anúncios mais antigos que a ferramenta não mostra.
- **Correção da correção:** o conector só mostra os 50 mais novos, por isso eu li 275 dias. A **SearchAPI (page_id, status ALL) devolveu 724 dias** e ~42 anúncios agrupados (collation) com destino `http://www.kontrola-sanepidu.pl/`. A v1 estava certa: **724 dias (início ~nov/2024)**.
- **Dos 12 ativos hoje, o mais antigo começou em ~02/10/2026 (28 dias)**; os criativos de jan–jul/2026 já foram desligados. Ou seja: vendedor com 275+ dias de histórico, mas hoje com ativos recentes. Pelo critério por-anúncio (cada criativo ativo há 30+ dias) NÃO passa hoje: ele rotaciona criativos (lotes em jan, fev, abr, jul, set, out/2026). Pelo critério por-página (a página anuncia o mesmo produto há 724 dias, 12 criativos ativos hoje) passa com folga. Uso o critério por-página.
- Ganchos nos títulos: "Procedury z 12-miesięczną gwarancją", "Aktualizacja na 2027", "Sprawdź, czego brakuje w salonie", "Procedury bez pisania od zera", pacotes por serviço (beauty, fryzjer/barber, tatuaż, masaż/fizjoterapia, stomatologia, mezoterapia, umowa najmu stanowiska).

### sklep-haccp.pl, "Wzory HACCP" (PL, PLN), page 1024438174083225
- 44 anúncios no total, **12 ativos hoje**. Mais antigo visível: **13/03/2026 (231 dias)**. Mais antigo entre os ativos hoje: ~05/10/2026 (24 dias; os 12 ativos começaram entre 05/10 e 28/10). Os 32 anúncios de mar–mai/2026 estão inativos.
- Títulos: "Gotowa dokumentacja HACCP", "Nie pisz HACCP od zera", "HACCP dla sklepów i gastronomii", "Dokumentacja HACCP dla pizzerii .doc", "Plan Higieny dla salonu kosmetycznego", "Jak legalnie sprzedawać żywność z domu?".

(Seções B em diante serão adicionadas abaixo.)

### Protocollo Zero Sanzioni (IT, EUR), page 1067984506407525
- 44 anúncios no total. Pelo conector, dos 20 mais novos o mais antigo era 04/09/2026 (55 dias); os 24 restantes não aparecem.
- **A v1 dizia 29 dias. Errado. A SearchAPI (page_id, status ALL) devolveu 163 dias e ~33 anúncios agrupados, destino `https://www.protocollozerosanzioni.com/new`.** Início ~20/05/2026. PROVADO (EUR, italiano).
- Títulos: "6 strumenti per metterti in regola, a 27€", "Se non ti serve, ti rimborso i 27€" (garantia), "Una sola irregolarità può costarti fino a 8.000€", "Affitti brevi in regola in 3 fasi", "Sei davvero in regola con il tuo affitto breve?".

### Kit Oste (IT, EUR), page 1390563777470996
- 29 anúncios, todos lidos. Mais antigo: **09/10/2026 = 21 dias** (confirma a v1). SaaS com 14 dias grátis + isca "Checklist GRATUITA: i 10 obblighi 2026" + "Cruscotto per host" + "A fine mese, cosa resta?" (conta do host). Não provado (<30d), mas prova interesse em recorrência.

### Outras páginas medidas pelo conector
- **Orthomap Atlas visuel de l'orthophonie** (FR, moeda **BRL** = operador brasileiro), page 300436823837471: 110 anúncios; os 6 mais novos vão de 14/10 a 30/10/2026. Início real VERIFICAR (conector só mostra os mais novos).
- **Vet Clinic Docs** (ES, BRL), page 1170526269488341: **1 anúncio só**, início ~02/09/2026 (58 dias). Sinal fraco.
- **Kit de Documentos para Fisioterapeutas** (ES, USD), page 1288195784387072: 24 anúncios, começaram em 28–30/10/2026 (2 dias). Entrante novo.
- **Estética em Regra** (PT, EUR), page 1385184828015054: SearchAPI status ALL = 13 anúncios, o mais antigo **4 dias**; loja Shopify (`/products/estetica-em-regra`), copy "32 dossiers completos — avaliação, informação para a cliente, ...". (No conector o match mostrava ~13 dias; vale a SearchAPI.) Títulos "Um dossier para cada procedimento", "Um consentimento para cada procedimento". Entrante novo.
- **Școala Românească astăzi** (RO, RON), page 105284268360774: 52 anúncios; o mais antigo que vi começou em **25/08/2026 = 66 dias** (há mais antigos não visíveis). Vende "Magazin" de kits para professores: "Kit Comisia metodică a educatoarelor 2026–2027", "Kit Comisia SCIM", "Kit Comisia CEAC". **PROVADO em RO (RON, romeno).** Site `scoalaromaneascaastazi.ro` abre, mas a página inicial é só revista/artigos; a loja não apareceu (preço VERIFICAR).

## B. Ganchos legais e mercado confirmados (com fonte)

| Item | Fato | Fonte |
|---|---|---|
| PL, beleza/cabeleireiro/tatuagem | O **GIS publicou em 12/08/2026** (v1.0), atualizou em 19/08 e 18/09/2026 (v4.0) as "Zalecenia i wymagania higieniczno-sanitarne" para serviços fryzjerskie, kosmetyczne, tatuaż e piercing. A base legal citada pela PSSE é o art. 16 da ustawa de 5/12/2008 (procedimentos escritos para quem rompe a continuidade da pele); a v1 dizia "art. 11" e isso NÃO se confirma. Os guias são "recomendações", não obrigatórios; o setor critica a imprecisão (barbeiros e máquinas elétricas) | https://www.gov.pl/web/gis/zalecenia-i-wymagania-higieniczno-sanitarne-glownego-inspektora-sanitarnego-w-zakresie-swiadczenia-uslug-beauty ; https://www.rmf24.pl/fakty/polska/news-fryzjer-bez-golarki-wytyczne-sanepidu-zszokowaly-branze,nIdn,1013339 (12/08/2026) ; https://www.gov.pl/web/psse-trzebnica/wymagania-dla-salonow-beauty |
| PL, PKD | PKD 2025 em vigor desde 01/01/2025; PKD 2007 pode ser usado até **31/12/2026**; 96.02 foi dividido em 96.21 (cabeleireiro) e 96.22 (estética). Nº de empresas: não achei (VERIFICAR no REGON/GUS) | https://www.wiadomoscikosmetyczne.pl/biznes-kosmetyki/salony-beauty-musza-uwazac-na-automatyczna-zmiane-kodow-pkd-na-czym-to-polega-2538464 |
| PL, HACCP | Reg. CE 852/2004 exige procedimentos baseados em HACCP; lei polonesa de 25/08/2006 sobre segurança alimentar, alterada em 2025 (Dz.U. 2025 poz. 1424, citado por documentos do PSSE; VERIFICAR). Registro no PPIS 14 dias antes do início. Sem prazo novo. Nº de estabelecimentos: não achei | https://www.gov.pl/web/psse-gdansk/zalatwianie-spraw4 (e demais páginas PSSE) |
| PL, pré-escola | Rozporządzenie MEN assinado em **11/03/2026** (Nowacka); a nova podstawa programowa do pré-escolar vale a partir de **01/09/2026** (reforma "Kompas Jutra"). Nº Dz.U. (ORE cita poz. 378) VERIFICAR | https://www.gov.pl/web/edukacja/nowe-podstawy-programowe-wychowania-przedszkolnego-i-ksztalcenia-ogolnego-dla-szkoly-podstawowej-wraz-ze-zmianami-w-ramowych-planach-nauczania-dla-publicznych-szkol-podstawowych--rozporzadzenia-podpisane |
| IT, affitti brevi | CIN obrigatório desde **02/11/2024**; sanções desde **02/01/2025** (art. 13-ter c.9 DL 145/2023). Multa 800–8.000 € segundo TeamSystem; outras faixas só em site não oficial. Detector de gás/CO e extintor 13A (6 kg, 1 por 200 m² e por andar). SCIA ao SUAP para mais de 2 apartamentos (L. 178/2020 c.595 alterada pela Lei de Orçamento 2026). Nenhuma fonte confirmou "autorização dal 2028" (continua VERIFICAR). Controle ativo: Carabinieri VCO, 07/2026, multas >15 mil € | https://www.diritto.it/affitti-brevi-faq-turismo-2026-cin-sicurezza-scia/ ; https://www.teamsystem.com/magazine/horeca/sanzioni-cin-affitti-brevi-e-turistici/ ; https://www.verbanonews.it/aree-geografiche/lombardia/2026/07/14/controlli-dei-carabinieri-nelle-case-vacanze-del-verbano-cusio-ossola-multe-per-oltre-15mila-euro/1027603/ |
| IT, tamanho | CIN: 370 mil emitidos em dez/2024; 538.674 estruturas registradas (data não clara). Nº de 2026 (694 mil da v1) NÃO confirmado: VERIFICAR no BDSR | https://www.immobiliare.it/news/economia/tasse-imposte-e-normative/affitti-brevi-oltre-100mila-cin-rilasciati-in-una-settimana-230549/ |
| ES, veterinário | RD 666/2023 (BOE nº 172, 20/07/2023); PRESVET: registro de prescrições de antibióticos; MAPA diz que de 02/01/2025 a mai/2026 ~16.460 clínicos de pequenos animais registraram ~3,22 milhões de prescrições. Existe pedido de moratória e minuta de alteração do RD (estado VERIFICAR). Nº de veterinários: VERIFICAR | https://www.boe.es/eli/es/rd/2023/07/18/666 ; MAPA PRESVET https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/Higiene-de-la-produccion-primaria-ganadera/medicamentos-veterinarios/Presvet.aspx |
| PL, fisio | ~55.770 com direito de exercer (prawo.pl, ano do artigo incerto). Sem número 2026 oficial: VERIFICAR (KIF) | https://www.prawo.pl/zdrowie/ (artigo sobre registro) |

### Produto e preço do concorrente (página aberta)
- **sklep-haccp.pl** (loja Sky-Shop): pizzaria PDF 99,90 zł; manual GHP/GMP loja 83,80 zł; GHP/GMP gastronomia 83,80 zł; restaurante DOC 156,45 zł; HACCP+GHP/GMP para venda de bolos em casa, kebab, creche com catering e food truck, cada um 199 zł. Formato PDF e DOC/DOCX. A página não cita lei com data.
- **Kontrola Sanepidu** "tylko 39 zł": preço lido no título do anúncio (v1); o site de destino ainda não abri.

### Páginas de venda abertas (preço, plataforma, conteúdo) em 30/10/2026
**Kontrola Sanepidu** (http://www.kontrola-sanepidu.pl/), carrinho próprio, operador de pagamento não identificado, política de devolução linkada (texto não lido):
- Pakiet salon beauty 144 zł (de 282,90); Pakiet fryzjerski/barberski 144 zł; **Pakiet gabinety fizjoterapii i rehabilitacji 144 zł (de 418,20)**; Pakiet masażu 144 zł; **Pakiet podologiczny 144 zł**; pacote completo dedicado beauty 375 zł (de 971,70); Poradnik "przygotowanie salonu beauty do kontroli w 2027 r." 39,36 zł; Procedura Manicure/Pedicure 49 zł cada; Alergeny w gastronomii 114,39 zł; **HACCP/GMP/GHP fast food, food truck, pré-escola com catering e com cozinha própria: 232,47 zł cada**.
- Serviço extra "Aktualne wzory dokumentów 2027": DOCX editável preenchido com dados da empresa + impressão e envio (preço não exibido).
- Não cita nenhuma lei com data. **Correção da v1: o "39 zł" é só o guia de 2027; o pacote principal custa 144 zł (~€34).**

**Protocollo Zero Sanzioni** (https://www.protocollozerosanzioni.com/): **€27 pagamento único** ("valor €382": Protocollo €97 + 5 bônus), PDF + Excel, checkout próprio em /checkout (Stripe/PayPal/cartões), garantia 30 dias "senza domande", atualizações por e-mail, conteúdo "aggiornato a febbraio 2026". Contém: protocolo em 3 fases (diagnóstico, adequação, "blindatura" fiscal), checklist CIN/SCIA/segurança, calculadora fiscal, kit documental + 10 e-mails para hóspedes (IT/EN), checklist por nº de imóveis, mapa normativo das 20 regiões, guia anti-controle. Não cita leis com número.

**Estética em Regra** (PT): **€19,90** (de €55,90), pagamento único, Shopify. 32 dossiês de procedimentos (20 só médicos e 12 médicos+estética), ficha de avaliação, consentimentos RGPD, material visual, mapa da consulta, Canva editável + PDF A4, 3 brindes (checklist de inspeção, guia de logotipo, 30 mensagens de WhatsApp). Garantia 30 dias. Avisa que NÃO é aprovado por ASAE/ERS. (Atenção: parte dos dossiês parece médica/injetável; nós cortamos isso.)

**sklep-haccp.pl** (PL): ver acima, 83,80 a 199 zł.

### Tamanhos confirmados (fonte)
| Mercado | Número | Fonte |
|---|---|---|
| PL salões de beleza e cabeleireiros | **~138,8 mil** (meados de 2026; +6 mil no 1º semestre). Fim de 2025: >132,8 mil (Dun & Bradstreet). Número oficial CEIDG/REGON: VERIFICAR | https://www.wiadomoscikosmetyczne.pl/ogloszenia/salony-kosmetyczne-w-polsce-jest-ich-juz-138-8-tys-2537864 (cita rp.pl) |
| PL pré-escola | 138.743 professores em pré-escolas (dados MEN de 22/04/2025, 92.136 deles professores de educação pré-escolar); GUS 2024/25: 14 mil pré-escolas + 7 mil turmas pré-escolares em escolas | resultado de busca sobre GUS "Oświata i wychowanie 2024/2025" (https://wartowiedziec.pl/edukacja-kultura-i-sport/78439-mniej-uczniow-wiecej-wyzwan-gus-o-stanie-polskiej-oswiaty); PDF primário do GUS: VERIFICAR |
| IT estruturas de aluguel curto/turístico | **703.917 estruturas na BDSR, ~88,4% com CIN** (dados de 31/03/2026) | https://www.ministeroturismo.gov.it/wp-content/uploads/2026/04/Infografica-Marzo-2026.pdf |
| RO cadres didactice | 219.900 no pré-universitário em 2025/26 (INS); sem corte por învățători/educatoare | https://www.edupedu.ro/incepe-scoala-2026-2027-pentru-29-milioane-de-elevi-si-copii-cati-profesori-ii-asteapta-si-cate-scoli-mai-are-romania-dupa-comasarile-din-ultimul-an/ |
| ES logopedas | 12.811 (INE 2025; coluna da tabela ambígua, VERIFICAR) ; veterinários 36.989 (INE 2023, último que achei) | https://ine.es/dyngs/Prensa/es/EPSC2025.htm |
| PL fisioterapeutas | ~55,8 mil com direito de exercer (prawo.pl, ano incerto) | prawo.pl |
| PL gastronomia | não achei contagem nacional: VERIFICAR | |

### Ganchos de prazo universais (e-fatura), válidos para qualquer profissional autônomo
| País | Prazo | Fonte |
|---|---|---|
| ES Verifactu | 01/01/2027 (sociedades) e **01/07/2027** (autônomos e demais), RDL 15/2025 (BOE 03/12/2025). Convalidação no Congresso: VERIFICAR | https://www.legaltoday.com/actualidad-juridica/noticias-de-derecho/nueva-prorroga-verifactu-no-sera-obligatorio-hasta-2027-para-sociedades-y-otros-contribuyentes-2025-12-04/ |
| FR facture électronique | recepção **01/09/2026** para todas as empresas com TVA (inclui micro); emissão: grandes e ETI 01/09/2026, **PME e micro 01/09/2027** | https://www.cegid.com/fr/facturation-electronique/facture-electronique-obligatoire/calendrier-facture-electronique/ (fonte de editor de software; texto oficial DGFiP: VERIFICAR) |
| PL KSeF | grandes 01/02/2026; demais 01/04/2026; microempresas (venda mensal <10 mil zł) com tolerância até 30/09/2026 e obrigação plena 01/01/2027, mas há projeto de adiar microempresas até 31/12/2027 (status VERIFICAR) | https://jpk.info.pl/faktury/e-faktura-ustrukturyzowana-ksef/harmonogram/ ; https://czasopismo.legeartis.org/2026/02/odroczenie-ksef-mikroprzedsiebiorcow-31-grudnia-2027-obowiazek-wystawiania-faktur/ |

## C. Medições extras do conector (30/10/2026)
- **Zgodny Gabinet** (PL, PLN), page 1228451337028686: 21 anúncios, o mais antigo começou em 08/10/2026 = **22 dias**. Vende "Dokumentacja dla masażysty mobilnego/fizjoterapeuty mobilnego" e massagem seca, **199 zł "pierwsze 5 pakietów"**, "5 dokumentów, 10 plików", "42 sekcje i moduły", Word e PDF. Não provado (<30d).
- **FizjoTeczka** (PL, moeda **USD** = operador estrangeiro/BR), page 716677868202484: 20 anúncios, começaram em 28/10/2026 (**2 dias**). "Wzory dokumentów dla gabinetu fizjoterapii".
- **Dentista PL por operadores de moeda USD, entrantes novos** (sem medir idade): "Lek. dent. Katarzyna Malinowska" (page 1321292424409638, "Wydruk lub ekran, jak wolisz") e "Sophie Collins" (page 1423844567472797, "Dokumenty przed pierwszym pacjentem"). A janela de documentos para gabinete na Polônia está sendo ocupada agora, por operadores com perfil BR/USD.
- **Itália, BRL**: "Beatriz Guerra" (page 907895875729587, moeda BRL), "Capisci il rischio, non andare a memoria", começou hoje. Operador brasileiro entrando na IT em tema de risco/DVR (produto VERIFICAR).
- **Romênia, USD**: "Cupa Emotiilor" (page 1397039396826105), "4 jocuri terapeutice la prețul unuia", 13 anúncios no match; dos 10 que li, o mais antigo começou ~27/10/2026 (3 dias). Material terapêutico/psico.
- **NL**: "Jouw.Logopedist" (EUR, page 104325905805722, "toolkit" para pais/logopedistas, 54 anúncios no match; idade não medida). Nenhum vendedor de pacote de documentos/HACCP/sjablonen encontrado (3 buscas, 0 resultados).
- **DE**: busca "Vorlagen Praxis Dokumente" devolveu 5 anúncios, nenhum vendedor de kit (só software e IA). Confirma o vazio de kit de documentos em alemão.

## D. BRECHAS (país × profissão), uma a uma
Legenda: [V2] = medido nesta rodada; [v1] = veio da v1 e não foi remedido; **zero** = o termo devolveu 0 anúncios ativos naquele país em 30/10 (não prova que ninguém vende com outra palavra: VERIFICAR com 1 busca extra antes de investir).

| # | País | Profissão | Quem vende | Dias / moeda | Leitura |
|---|---|---|---|---|---|
| 1 | PL | Fisioterapeuta, massagista, podólogo | Kontrola Sanepidu (pacote 144 zł, fisio/masaż/podologia) [V2]; Zgodny Gabinet 199 zł [V2]; FizjoTeczka [V2] | 724 d PLN; 22 d PLN; 2 d USD | Fecha rápido. Já há prova nativa e entrante USD |
| 2 | PL | Dentista | Kontrola Sanepidu (Stomatologia, abr/2026) [V2]; 2 páginas USD novas [V2] | idade só da 1ª: ≥200 d; USD 0–6 d | Janela fechando |
| 3 | PL | Veterinário | **ninguém** (2 buscas, zero) [V2] | | Brecha aberta. Sem gancho de data confirmado |
| 4 | PL | Logopeda (kit de documentos/fichas) | só cursos (Kursy Pedagogiczne, NODN Cognitus); kit: ninguém [V2] | | Brecha de produto; mercado de curso é ativo |
| 5 | PL | Creche (żłobek/klub dziecięcy) | **ninguém** (zero) [V2]. Kontrola Sanepidu só vende HACCP de pré-escola/cozinha | | Brecha aberta |
| 6 | PL | Aluguel de curta duração | **ninguém** (zero, SearchAPI exato) [V2] | | Brecha. Sem gancho nacional confirmado |
| 7 | PL | Gastronomia/loja/comida caseira (HACCP) | sklep-haccp.pl 231 d; Kontrola Sanepidu (fast food, food truck, pré-escola) 232 zł; HACCP od zera 14 d; Mierz Wysoko 53 d [V2] | PLN | Provado, concorrido |
| 8 | PL | Professora pré-escola | cursos (NODN Cognitus ativo com "Kompas Jutra", 6 criativos); kit de planejamento: não medido | PLN | Gancho 01/09/2026 forte; vendedor de kit VERIFICAR |
| 9 | IT | Host de affitti brevi | Protocollo Zero Sanzioni 163 d €27 [V2]; Kit Oste 21 d SaaS [V2] | EUR | Provado; nada para outras profissões |
| 10 | IT | Fisioterapista (modulistica) | **ninguém** [V2, SearchAPI exato zero] | | Brecha |
| 11 | IT | Veterinário (consenso informato) | **ninguém** [V2 zero] | | Brecha |
| 12 | IT | Logopedista (schede) | kit: **ninguém** no exato [V2]; ABA Tools (USD) 91 d [v1] | | Brecha parcial |
| 13 | IT | Estetista / tatuatore / parrucchiere / osteopata | **ninguém** em buscas de kit [v1 + V2 parcial; várias não rodaram por 429] | | Brecha provável. VERIFICAR |
| 14 | IT | HACCP | só consultoria/SaaS: Facile Sicurezza 644 d, Vega Formazione 363 d, Aqagroup 127 d, NORMA HACCP 125 d (SaaS) [V2]; nenhum kit de documentos com app | EUR | Mercado de serviço, brecha de kit+app |
| 15 | IT | DVR | Vega Formazione 237 d (formação) [V2]; Beatriz Guerra BRL hoje [V2] | | Operador BR entrando |
| 16 | DE | Qualquer profissão (kit de documentos) | **ninguém** [V2 + v1] | | Brecha total em alemão; custo: copy nativa |
| 17 | NL | HACCP, sjablonen, documentos de prática | **ninguém** [V2 zero] | | Brecha; gancho não pesquisado |
| 18 | FR | Orthophoniste | Orthomap (BRL, 110 anúncios, início VERIFICAR); Paroles d'ortho 106 d [v1] | BRL / EUR | BR provando na FR |
| 19 | FR | Micro-crèche, kiné, vétérinaire, esthéticienne | kit: **ninguém** achado; resultados só de publicidade de creche [V2 parcial] | | Brecha provável. VERIFICAR |
| 20 | RO | Professora (educatoare, învățător, comissões SCIM/CEAC) | Școala Românească astăzi ≥66 d RON [V2] | RON | Provado |
| 21 | RO | Terapia/psico | Cupa Emotiilor 3 d USD [V2] | USD | Entrante |
| 22 | RO | HACCP, logoped, kinetoterapeut | HACCP: Andrei Kowalski USD 7 d [v1]; logoped "Materiale Educaționale Logopedice" 38 d RON [v1] | | Não remedido |
| 23 | PT | Esteticista | Estética em Regra 4 d EUR €19,90 [V2] | EUR | Entrante |
| 24 | PT | Fisio, vet, terapeuta da fala, alojamento local | **ninguém** [v1; V2 sem confirmação por 429] | | Brecha provável. VERIFICAR |
| 25 | ES | Fisioterapeuta | Kit de Documentos para Fisioterapeutas 2 d USD [V2] | USD, idioma neutro | Não prova país |
| 26 | ES | Veterinário | Vet Clinic Docs 1 anúncio, 58 d BRL [V2] | BRL | Sinal fraco; gancho forte (PRESVET) |
| 27 | Todos | Autônomo qualquer | Prazos e-fatura: ES 01/07/2027, FR 01/09/2026 e 01/09/2027, PL 01/01/2027 [V2 só o gancho]. Vendedores de kit/app para isso: **não medidos** (SearchAPI sem crédito) | | VERIFICAR |

## E. Ranking 0–10 (régua: prova 0–3, tamanho 0–2, gancho 0–2, ticket/LTV 0–2, reaproveitamento 0–1)
| # | País × nicho | Nota | Tipo | Evidência (page, dias, anúncios, preço) |
|---|---|---|---|---|
| 1 | **PL: beleza, cabeleireiro, tatuagem, massagem, podologia, fisio** (procedimentos Sanepid + simulado) | **8,5** | PROVADO | Kontrola Sanepidu, page 388263394381460: 724 d (SearchAPI), ~42 anúncios agrupados, 12 ativos hoje, 144 zł pacote, 375 zł completo |
| 2 | **IT: host de affitti brevi** | **8,5** | PROVADO | Protocollo Zero Sanzioni, page 1067984506407525: 163 d, ~33 anúncios, €27, garantia 30 d |
| 3 | **PL: HACCP gastronomia/loja/comida caseira** | **7,5** | PROVADO | sklep-haccp.pl 231 d, 44 anúncios, 83,80–199 zł; Kontrola Sanepidu 232,47 zł |
| 4 | **RO: kits para cadre didactice** (comissões, portofoliu 2026–27) | **7,0** | PROVADO (preço VERIFICAR) | Școala Românească astăzi, page 105284268360774: ≥66 d, 52 anúncios, RON |
| 5 | **PL: fisio/massagem (kit clínico + app)** | **7,0** | TESTE (provado só via Kontrola) | Kontrola 144 zł; Zgodny Gabinet 22 d 199 zł; FizjoTeczka 2 d USD |
| 6 | **PL: pré-escola (nova podstawa 01/09/2026)** | **6,5** | PRAZO/TESTE | Regulamento 11/03/2026; 138.743 professores; vendedor de kit não medido |
| 7 | **ES: veterinário (PRESVET)** | **6,0** | PRAZO/TESTE | Vet Clinic Docs 58 d BRL (1 anúncio); RD 666/2023; 36.989 vets (INE 2023) |
| 8 | **FR: orthophonie (Fono Infantil)** | **6,0** | TESTE | Orthomap BRL, 110 anúncios, idade VERIFICAR |
| 9 | **IT/PT/ES/FR: Consultora Alimentos (simulador de inspeção)** | 6,0 | TESTE | HACCP IT só serviço/SaaS (Facile Sicurezza 644 d etc.); nenhum kit+app |
| 10 | **PT: estética** | 5,5 | TESTE | Estética em Regra 4 d €19,90 |
| 11 | **DE / NL: kit de documentos para qualquer profissão** | 5,0 | BRECHA | Zero vendedores; sem prova de demanda |
Pesos usados no #1: prova 3 + tamanho 2 + gancho 1 (GIS 12/08/2026 é recomendação, não norma com data de multa) + ticket 1,5 + reuso 1 = 8,5. No #2: 3+2+1,5+1,5+0,5 = 8,5. Não houve nota acima de 9 porque nenhum gancho trouxe norma nova com data de vigência E multa no mesmo país onde há vendedor provado.

## F. O que continua VERIFICAR
1. **SearchAPI sem créditos**: usage 10.000/10.000 em 30/10 (outros agentes rodaram em paralelo, vi jobs MX; minhas rodadas em paralelo tomaram 429). Renova em 08/11. Por isso as varreduras de produto/profissão (IT, FR, DE, ES, PT, RO, NL, lista de ~150 termos) ficaram incompletas: só ~48 retornaram sem 429 e a maioria deu zero.
2. Datas de início reais de: Orthomap (FR), Școala Românească (>66 d), Protocollo Zero Sanzioni (163 d vale como piso), Vet Clinic Docs. Ordem do conector é do mais novo ao mais antigo (máx. 50).
3. Preço da Școala Românească (loja não abriu), de Zgodny Gabinet (199 zł lido no anúncio), FizjoTeczka, Orthomap, Kit Oste.
4. Número oficial de salões (REGON/CEIDG), fisioterapeutas (KIF), gastronomia (GUS), veterinários ES 2025 (INE), pré-escola GUS/SIO.
5. Texto do Dz.U. da podstawa programowa pré-escolar (ORE cita poz. 378/2026; gov.pl não dá número) e o artigo exato da ustawa 5/12/2008 (PSSE cita art. 16; a v1 dizia art. 11).
6. "Autorização dal 2028" para affitti brevi (GoHomes): nenhuma fonte confirmou.
7. KSeF microempresas (projeto de adiar até 31/12/2027) e convalidação do RDL 15/2025 (Verifactu).
8. Se a data de obrigação do CIN é 02/11/2024 com multas desde 02/01/2025 (diritto.it) ou 01/01/2025 (outras fontes).
9. Qualquer "zero" da seção D: refazer com 1–2 sinônimos locais quando houver crédito.
