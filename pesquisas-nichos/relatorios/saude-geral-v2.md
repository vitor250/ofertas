# Saúde geral por país, v2 (30/10/2026): refeita com medição por page_id e brechas

Fontes: conector Meta (ads_library_search, só ATIVOS, máx. 50 anúncios por chamada, por isso subconta anunciantes grandes) + SearchAPI (engine meta_ad_library, frase exata, com page_id; devolve link de destino e texto) + páginas de venda abertas + busca web. Dias = 30/10/2026 menos a data de início do anúncio ativo mais antigo do page_id. PROVADO = anúncio ativo 30+ dias no país/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma. Harmonização e injetáveis fora.
O que não consegui confirmar em fonte oficial está marcado VERIFICAR. Harmonização/injetáveis excluídos. Limite do SearchAPI: ~1.100 créditos no mês, chave compartilhada com outras buscas (houve erro 429; alguns termos ficaram sem medir e estão listados no fim).

## A. Medição real dos 4 itens que a v1 deixou VERIFICAR (por page_id)

| Item | Dias reais | Anúncios | Moeda | Preço e conteúdo (página aberta) | Plataforma |
|---|---|---|---|---|---|
| Care Daily (412861181906925), UK | 132 (início 19/06/2026, 8 anúncios ativos na busca do conector, 7 no SearchAPI) | 7-8 | GBP | Link de destino caredaily.co.uk (app React sem texto no HTML, não consegui ler preço). Títulos: "Domiciliary care policies, ready to customise", "Supported living policies. Not adapted. Written.", "Replace the folder. Start fresh.", "Your records deserve better than a ring binder." O anúncio mais novo (17/08) fala em registros. A página parece ser de SOFTWARE de gestão de cuidados (URL /company/careManagement-software), não só kit de políticas. | VERIFICAR (site próprio) |
| ABA Tools (108617997275390) | 133 (SearchAPI) / 125 em IT (frase "analista del comportamento"). O conector sozinho mostrou só 15 dias porque corta em 50 de 133 anúncios | 133 ativos (95 em IT) | USD | en.abatools.pro/pat: Practical Autism Transformation Toolkit. Básico US$ 9 (de 49), Completo US$ 17 (de 230), "expira hoje". it.abatools.pro/nap: "35 protocolli ABA naturalistici" (PRT+ESDM), Base € 9 / Completo € 17, 4 bônus, comunidade VIP, certificado, garantia 30 dias | pay.snappcheckout.com |
| Instituto Zasada (104705036318383), PL | 162 (início 20/05/2026; o anúncio de "dokumentacja" é de 06/07 = 115 dias; "kwestionariusz" 04/08 = 86 dias) | 30 | PLN | Loja própria e-learning.instytutlogopedyczny.pl: "Dokumentacja: Pakiet" 79 PLN; fichas avulsas 5-10 PLN (karta diagnozy 10, wywiad 10, karta zajęć 5); e-books ABC początkującego logopedy 129-172 PLN; pacote de 4 cursos 999 PLN. A maior parte dos 30 anúncios é CURSO/webinar de voz e respiração, a documentação é uma linha de produto secundária | WooCommerce próprio |
| Fonoaudiología Profesional (1283844954801148) | 16 (início 13/10/2026; ~12 dos 16 anúncios nasceram em 23-27/10) | 16 | USD | fonokitprofesional.online: FonoKit "Edición Argentina": AR$ 19.990 (de 54.990), 10 PDFs, 300 fichas, 500+ tarjetas, 20 sesiones armadas, 37 juegos, 336 pantallas teleterapia, 5 bonos, garantia 7 dias | checkout próprio (/checkout, sem domínio de pagamento externo) |

Leitura: o item 2 (ABA) sobe em força (133 dias, 133 anúncios, 2 idiomas). O item 4 (fono ES) continua TESTE (16 dias), mas a página é argentina em ARS, e Lenguaje en Juego (1366826673183986) é a edição México: MX$ 279 (de 699), 150 atividades, garantia 30 dias, 3 dias no ar. São a mesma fábrica de páginas (impultienda.ar), ou seja, vendedores BR adaptando por país.

## B. Tamanhos e datas de fiscalização (fonte oficial, URL)

| Tema | O que confirmei | Fonte | Status |
|---|---|---|---|
| UK home care: pessoas atendidas | 489.732 pessoas em home care regulado pela CQC na semana até 14/08/2026 (81,2% dos provedores responderam); 499.364 na semana até 14/05/2026; 505.886 em fev/2026 | gov.uk, Adult social care provider statistics, quarterly update to August 2026: https://www.gov.uk/government/statistics/adult-social-care-provider-statistics-england-quarterly-update-to-august-2026/adult-social-care-provider-statistics-england-quarterly-update-to-august-2026 | CONFIRMADO |
| UK: nº de provedores domiciliares | A página oficial não traz a contagem. Só tenho 11.951 (homecare.co.uk, secundário, jun/2026) | secundário | VERIFICAR |
| UK: adoção de registro digital | 83,6% dos locais adultos registrados na CQC têm registro digital em jun/2026 (todos os tipos) | mesma página gov.uk | CONFIRMADO (mercado já digitalizado, ameaça ao kit em papel/Word) |
| CQC frequência de inspeção | Busca web: CQC diz que inspecionará a maioria dos serviços domiciliares "pelo menos uma vez por ano", em fases; a Homecare Association alerta que ~60% nunca foram inspecionados ou há 4+ anos. A página oficial da CQC (cqc.org.uk/node/340) devolveu 403 e não li o texto; sem data de início | cqc.org.uk/node/340 (não lido) + imprensa (inkl/LocalGov) | VERIFICAR data. Sem gancho de PRAZO com data |
| NOM-004 (México) | Norma vigente: publicada no DOF em 15/10/2012, em vigor desde 13/12/2012. Não achei modificação em 2026 no DOF nem calendário de verificação da COFEPRIS. Um blog comercial fala em "decreto 2026 de digitalização obrigatória" sem fonte oficial: tratar como falso até prova | https://platiica.economia.gob.mx/normalizacion/NOM-004-SSA3-2012/ e DOF https://dof.gob.mx/normasOficiales.php?codp=4909&view=si | Vigência CONFIRMADA; data de fiscalização VERIFICAR (provavelmente inexistente). Sem PRAZO |
| México: consultórios médicos | 85.908 unidades econômicas "Consultorios médicos" no DENUE em maio/2026; 1,42 milhão de ocupados no 1T/2026 | https://www.economia.gob.mx/datamexico/es/profile/industry/offices-of-physicians | CONFIRMADO |
| ELEAM Chile | Reglamento = DS 20/2021 (Minsal). Prorrogado/modificado por Decreto 23/2023 (D.O. 30/09/2023), Decreto 9 (D.O. 22/04/2025, "prorroga vigencia y modifica") e Decreto 6 de 05/02/2025 (D.O. 09/07/2025). Os PDFs do Diário Oficial vêm sem texto extraível. Um blog de software (Macainn) diz: regulamento rige desde 01/10/2025 e ELEAM existentes têm até 01/10/2028 (incêndio: 2030). Não confirmei isso em texto oficial | https://www.diariooficial.interior.gob.cl/publicaciones/2025/04/22/44130/01/2635106.pdf ; https://www.diariooficial.interior.gob.cl/publicaciones/2025/07/09/44194/01/2666073.pdf ; https://www.diariooficial.interior.gob.cl/publicaciones/2023/09/30/43665/01/2384435.pdf | Existência dos decretos CONFIRMADA; data 01/10/2028 VERIFICAR (BCN consolidado) |
| ELEAM: tamanho | 947 ELEAM autorizados (CIPER, via busca da v1, não reconfirmado) | CIPER | VERIFICAR |
| Fono Polônia | Sem contagem oficial (GUS/MEN) na web. Estimativa da PZL: de cada 100 logopedas, 76 na educação, 12 na saúde, 12 em consultório próprio; ~300 logopedas no setor saúde (2023, anexo PZL). Projeto de lei do zawód logopedy em consulta (reunião 23/09/2025) | https://www.prawo.pl/zdrowie/gabinet-logopedy-ma-spelniac-wymogi-placowki-medycznej,520685.html ; https://logopeda.org.pl/resources/pliki/996_20230127_zalacznik_nr_1___szacunkowe_dane_dot_struktury_zatrudnienia_logopedow.pdf | Total VERIFICAR. Gancho: lei de regulação da profissão em tramitação, sem data |
| Fono/TO/ABA Itália | Sem contagem oficial achada (FLI/TSRM-PSTRP/ISTAT). Itália: albo de logopedisti obrigatório (TSRM-PSTRP, 19 profissões, ~230.000 inscritos no total, fonte secundária sem data). ABA não regulamentada; sem número de BCBA | busca web | VERIFICAR |
| Fono/TO Chile | Boletim RNPI da Superintendência de Salud existe (N°4/2025, posição 31/12/2025) mas o PDF não deu texto legível. Um trecho antigo e sem data mostra ~7.004 terapeutas ocupacionais (1,17% de 301.239) | https://www.superdesalud.gob.cl/app/uploads/2026/01/boletin-n4-2025-rnpi-enero-diciembre-2025.pdf | VERIFICAR |

Resumo: dos 3 "tamanhos oficiais" que a v1 deixou (fono, TO, ABA), nenhum saiu com número oficial confiável nesta rodada. Dos 3 "prazos de fiscalização" (CQC, NOM-004, ELEAM), nenhum virou gancho com data confirmada. NOM-004 provavelmente não tem prazo.

## C. Os vendedores novos da v1 (page_id) remedidos

| Vendedor (page_id) | País/moeda | Dias reais agora | Anúncios | Observação |
|---|---|---|---|---|
| Care Daily (412861181906925) | UK, GBP | 132 | 7-8 | confirmado; software/kit de políticas, preço não lido |
| CareDocs Direct (1178206642051081) | UK | 53 | 1 | "CareDocs Direct now offers bespoke policies" |
| Health Connect (730699523450802) | UK | não remedido (429/créditos) | | v1: £70/mês, 20d |
| Compliance Supports (227964520409222) | UK | não remedido | | v1: 87d |
| ABA Tools (108617997275390) | IT/US/GB, USD e EUR na página | 133 | 133 | US$9/17; €9/17; Snappcheckout |
| ABA in School (1849957218431496) | US | não remedido | | v1: 36d |
| Zasada (104705036318383) | PL, PLN | 162 (docs: 115) | 30 | pacote docs 79 PLN |
| Fonoaudiología Profesional (1283844954801148) | AR (ARS), anúncios em USD | 16 | 16 | AR$ 19.990 |
| Lenguaje en Juego (1366826673183986) | MX, MXN | 3 | 3 | MX$ 279 |
| Mah Souza (255170671023979) | ES | não remedido | | v1: 1d, 8 anúncios |
| IPSY-Psicopedagogia (118336271264296) | produto BR | 3 (31 criativos novos) | 31 | página real: R$ 47/mês, Stripe, em português do Brasil, SaaS de prontuário. O "US$37 / 6.857 páginas" da v1 NÃO apareceu na página: tratar como VERIFICAR e rebaixar |
| Nivel Pro Digital / Aurum Café (990571154140447) | PEN | 122 (73 criativos), MAS é curso de café ("La Biblia del Café", 400+ receitas) | 73 | v1 atribuiu "+500 atividades TO infantil, 70d" a essa página; não consegui reproduzir. TO no Peru: sem prova. Corrigido |
| Skillio, Centro Digital Terapeutico, GeriKit, GeriaVital, Sofía Mendonza | | não remedidos (créditos esgotados) | | Sofía Mendonza e GeriaVital reaparecem com 2d e 0d em CO/CL/PE |
| Kits Profesionales (692615883936217) | MX | 22 | 7 | "SUPER KIT DE FARMACIA 7.0", link WhatsApp, formatos editáveis |
| Formatos Profesionales (860792607114068) | MX | 0 ativos agora (v1: 149d) | 0 | parou de anunciar: sinal de 149d perdeu força |
| Archivos Digitales Express (103894282759676), EEK Digital, Aprendia, MirelMed, Vetdigital, Esencial VET, Dra Laura martin, Gilmara Santos | | não remedidos | | manter como na v1 |
| Geriactiva (1259324537268785) NOVO | MX/CO/CL/PE, anúncios em USD | 47 | 8-9 | geriactiva.impultienda.ar: R$ 91,16 (de 455,51) em REAIS, 5 volumes, 1.395+ páginas, depoimentos da Colômbia e do Chile, garantia 7 dias. Moeda errada (BRL na página para público LATAM) |
| Sarah lurdes (1422534284273441) NOVO | MX/CO/CL/PE | 23 | 11 | adultosmayoress.vercel.app, para fisio/TO/cuidador |
| Miriam Sousa (777617202100446) NOVO | MX (USD e BRL) | 6 | 2 | "+100 Materiales de Fonoaudiología" |
| Dra Fabiana Segura (1280402278479524) NOVO | MX (USD) | 7 | 2 | "+7 bonos regalo", fono |
| andribarrios.fono (101418542706668) NOVO | MX, MXN | 0-1 | 3 | perfil de fono, conteúdo não lido |
| Nexora (414482485088682) NOVO | MX, USD | 0 | 3 | "Oferta por lanzamiento", nicho fono, não lido |
| Laura Cortez (804639486075007) NOVO | ES/MX/AR | 3 | 1 | codigosonoro.site/oferta1, autismo, conteúdo não lido |
| SaludTotal ECE (194836527208362) NOVO | MX, MXN | 1 | 1 | software de expediente clínico "certificado ante la DGIS", teste 7 dias: concorrente SaaS |
| Cursos Profissionalizantes (786907757843547) / Formação Digital (813530711839179) NOVOS | ES | 346 / 101 | 3 / 3 | curso Hotmart de Cuidador de Personas Mayores em espanhol |

## D. Brechas encontradas, uma a uma (país, profissão, quem vende, dias)

Método: busca por frase exata no país (SearchAPI, até 2 páginas = ~120 anúncios, ordenados pelos mais antigos no meu resumo). "Ninguém" = zero anúncio ativo que seja kit/documento para o profissional, na amostra; uma frase só pode perder sinônimos, por isso as marcadas "frase única" precisam de uma 2ª checagem.

1. ABA/autismo terapeuta, Espanha e LATAM em espanhol (MX, CO, AR, CL): ninguém vende kit. Só curso grátis de lead da Corporación Internacional Líder (CIL, 25d, 9 criativos, MX/CO/AR) e Laura Cortez (3d, 1 anúncio, codigosonoro.site, conteúdo não lido). Quem prova a oferta é ABA Tools em inglês e italiano (133d). Brecha de IDIOMA.
2. ABA, França, Alemanha, Polônia: zero anúncios ativos para "ABA autisme", "ABA Autismus", "autyzm terapeuta" (frase única). Ninguém. Reaproveitar o kit ABA Tools em FR/DE/PL = brecha de idioma, sem prova local.
3. ABA, Reino Unido: ABA Tools 132d (inglês, mesma página /pat); Advance Therapy ABA Services (clínica, 87d). Já ocupado em inglês.
4. ABA, Itália: ABA Tools 125d no país + Dalla Luna (curso ABA, 467d, 18 criativos) + Humanitas (master, 87d). Kit de protocolo já vendido a €9/€17; pouco espaço de preço.
5. Terapia ocupacional, Itália: 12 anúncios, nenhum kit (STOcrescendo = clínica 210d; Olly Med 30d; Intandem = curso 14d). Ninguém. Frase "terapista occupazionale".
6. Terapia ocupacional, México, Colômbia, Argentina, Chile, Espanha: só clínicas e centros (Cecamux MX 325d é curso/clínica de TEA; Wawa CO 498d; Cimfyr AR 1371d; Clínica Medifis CL 602d; La Salle ES 199d). Nenhum kit/atividades de TO com 30d+. Peru: Nivel Pro NÃO é TO (é café). Ninguém.
7. Terapia ocupacional, França: Caaly (caaly.fr, "cahiers cursifs", produto físico de escrita) 377d; resto formação. Kit para o profissional: ninguém.
8. Fonoaudiólogo, República Tcheca: Vyslovujspravne.cz 161d (2 criativos, produto para pais, "ritual com animais") + Malvina.school 15d. Para o profissional: ninguém.
9. Fonoaudiólogo, Polônia: documentação só Zasada (115d, 79 PLN, produto secundário a cursos). Brecha de PRODUTO: nenhum vendedor com kit completo + app.
10. Fonoaudiólogo, México/Colômbia/Chile/Argentina: onda de 13/10 a 30/10. Fonoaudiología Profesional (16d, AR$ 19.990), Lenguaje en Juego (3d, MX$ 279), Miriam Sousa (6d), Dra Fabiana Segura (7d), andribarrios.fono (0-1d), Nexora (0d). Nenhum com 30d: TESTE, e já virando multidão (6 vendedores em 2 semanas, mesma fábrica de página).
11. Cuidador de idosos, MX/CO/CL/PE: Geriactiva 47d (8-9 criativos, +1.000 atividades; preço na página em R$ 91,16) e Sarah lurdes 23d (11 criativos). Brecha de MOEDA: página em reais, público em pesos. Nenhum vendedor nativo em MXN/COP/CLP.
12. Cuidador/ayuda a domicilio, Espanha: curso Hotmart "Cuidador de Personas Mayores" 346d (Cursos Profissionalizantes) e 101d (Formação Digital), mesmo link; INEFSO 153d e Formación Activa 198d (cursos de ayuda a domicilio). Documentos/kit para empresa de SAD ou residência: ninguém. Servicios del Fresno (115d) é prestadora, não vendedor.
13. Residências de idosos, Chile (ELEAM): 18 anúncios, só residências e ICCE capacita (curso, 69d). Kit normativo: ninguém.
14. Residências, Portugal (ERPI/lar de idosos): 12 e 41 anúncios, só residências, etiquetas (Tiketa 283d) e fornecedor de têxteis. Kit de documentos: ninguém.
15. Residências, Itália (RSA), França (EHPAD), Alemanha (Pflegeheim): amostras de 60 anúncios por termo, ordenadas por idade, sem kit nas 4 mais antigas; RSA é dominado por recrutamento e escritórios de reembolso, EHPAD por diretório (Cap Retraite 427d, 18 criativos). Ninguém na amostra; VERIFICAR com termos locais (Qualiscope/HAS, SGB XI/MDK, accreditamento RSA).
16. Home care/cuidador, Irlanda (HIQA): 5 anúncios, só recrutamento. Ninguém vende políticas. Brecha de país (mesma língua do Care Daily).
17. Home care, UK: só dois vendedores de política: Care Daily 132d e CareDocs Direct 53d. Mercado concentrado em poucos anúncios (frase "care policies" tem 5 anúncios ativos).
18. Home care, Austrália (aged care 3.850 e NDIS 6.933 anúncios): volume enorme, nada medido por falta de crédito. VERIFICAR.
19. Médico de consultório, México: SaludTotal ECE (software de expediente, 1d, teste 7 dias). Kits de formato/consultório: Recursos Legales PRO (v1: 98d, não remedido), Formatos Profesionales parou (0 anúncios ativos hoje). Colômbia/Chile/Argentina (historia clínica / ficha clínica): rodada falhou, VERIFICAR.
20. Psicopedagogo, MX/AR/CL/CO/PE/ES: na amostra do conector, só universidades, diplomados e congressos (Giunti ES/MX, UNILA, Inprodes). Kit para o profissional: ninguém. IPSY é BR em português, não conta.
21. Enfermagem (MX/CO/PE/CL/ES/PL/RO/CZ/NL), veterinário (MX/CO/ES/IT/DE/FR/UK), podólogo (MX/ES/CL/IT/FR/DE/PT) e fisio PL/HU: busca falhou por limite de API (429, créditos zerados). Não medi. Ficam como na v1.

## E. Ranking v2 (0 a 10)

| # | Nicho x país | Nota | v1 | Tipo | Evidência (dias reais) | Tamanho com fonte | Gancho com data | Reaproveitamento | Risco |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ABA/autismo, Itália (€) | 8,0 | 7,5 | PROVADO | ABA Tools 125d só no IT, 133 dias e 133 anúncios no total, € 9 / € 17, Snappcheckout | VERIFICAR (sem contagem oficial) | Nenhum confirmado (linee guida ISS não verificadas) | Kit de protocolos + app; já temos Léo & Bia/maleta | Preço âncora €9-17 derruba ticket; vendedor BR já escalado |
| 2 | Home care/care agency, UK (£) | 7,5 | 8,0 | PROVADO | Care Daily 132d, 7-8 criativos; CareDocs 53d; 2 vendedores só | ~490 mil pessoas em home care (gov.uk, ago/2026); nº de provedores VERIFICAR | CQC "1x ao ano" sem data oficial lida, VERIFICAR | Políticas + app de registros; reaproveita pasta RDC da Consultora (traduzido) | 83,6% dos locais já têm registro digital; Care Daily parece SaaS; preço não lido |
| 3 | ABA/autismo, ES-LATAM em espanhol | 7,0 | n/c | TESTE por tradução de PROVADO | Ninguém em espanhol; ABA Tools prova em EN/IT há 133d; CIL dá curso grátis 25d | VERIFICAR | Nenhum | Tradução do que já vende; mesma fábrica de páginas | Sem prova local; ABA Tools pode abrir espanhol a qualquer hora |
| 4 | Cuidador/atividades geriatria, MX/CO/CL/PE | 7,0 | 6,0 | PROVADO (47d) | Geriactiva 47d, 8-9 criativos; Sarah lurdes 23d; página em BRL | VERIFICAR (INEGI/DANE/Minsal não buscados) | Nenhum | Atividades + app; serve cuidador, TO, fisio | É atividade, não documento; concorrente BR já ocupa; ticket baixo |
| 5 | Fono, Polônia (PLN) | 6,5 | 7,0 | PROVADO (115d) | Zasada documentação 115d, 79 PLN, 30 anúncios (mas a maioria é curso) | VERIFICAR (PZL: ~76% educação, 12% saúde, 12% privado; sem total) | Lei do zawód em tramitação, sem data | Documentação + app + modelos | Língua difícil; ticket ~PLN 79; vendedor é instituto de cursos |
| 6 | Fono, ES-LATAM (MXN/ARS/USD) | 6,5 | 7,0 | TESTE | 6 vendedores novos, 0-16d (Fonoaudiología Profesional 16d, Lenguaje en Juego 3d, Miriam Sousa 6d...) | VERIFICAR (Chile: boletim Superintendencia existe, sem número lido) | Nenhum | Tradução do BR (Edukidz 560d); app Fono Infantil já existe | Onda de cópias da mesma fábrica: saturação rápida |
| 7 | Cuidador/ayuda a domicilio e residências, Espanha | 6,0 | n/c | Lacuna + curso PROVADO | Curso Hotmart de cuidador 346d; kit de documentos: ninguém | VERIFICAR | Nenhum | Kit para empresa de SAD/residência | Só curso prova demanda; norma autonômica varia |
| 8 | Médico de consultório + farmácia, México | 6,0 | 6,5 | PROVADO (v1: 98d, não remedido) | Kits Profesionales 22d (farmácia 7.0); Formatos Profesionales parou; SaludTotal ECE (SaaS) | 85.908 consultórios (DENUE mai/2026, economia.gob.mx) | NOM-004 vigente desde 13/12/2012; sem prazo de fiscalização achado | Kit normativo + semáforo | Sem PRAZO; SaaS de prontuário no mesmo termo |
| 9 | Residências de idosos, Chile (ELEAM) | 5,5 | 6,0 | Lacuna | 18 anúncios, só donos de residência; ICCE curso 69d | 947 ELEAM (CIPER, não reconfirmado) | 01/10/2028 só em blog, VERIFICAR no D.O.; decretos 6 e 9 de 2025 existem | Kit de residência, norma DS 20/2021 | Sem prova de compra |
| 10 | ABA, FR/DE/PL | 5,0 | n/c | Lacuna (frase única) | Zero anúncios | VERIFICAR | Nenhum | Tradução do kit | Possível falha de termo; sem prova |
| 11 | Enfermagem MX/PE (aluno) | 5,0 | 5,5 | TESTE | v1, não remedido | VERIFICAR | | | Estudante, satura |
| 12 | Enfermeira liberal, França | 5,0 | 5,5 | Lacuna | v1, não remedido | ~98.900 liberais (DREES 2023, resumo da v1) | | | Software forte |
| 13 | TO, ES-LATAM / Itália / França | 4,5 | 6,5 | Lacuna sem prova | Nivel Pro era café; só clínicas | VERIFICAR | Nenhum | | Rebaixado: a prova de 70d da v1 não se sustenta |
| 14 | Psicopedagogo ES-LATAM | 4,5 | 6,0 | Lacuna | IPSY é SaaS BR R$47/mês; sem kit em espanhol na amostra | VERIFICAR | Nenhum | | Rebaixado: prova BR, não ES |
| 15 | Veterinário, podólogo, Pflege DE, doula | 2,0 a 4,0 | 2,0 a 4,0 | | não remedidos | | | | como na v1 |

## F. Top 8 e diferenças em relação à v1
1. ABA Itália (8,0, subiu): 133 dias reais, 133 anúncios, €9/€17. O conector sozinho mostrava 15 dias porque corta em 50 anúncios.
2. Home care UK (7,5, desceu): prova de 132d confirmada, mas Care Daily parece software, preço ilegível, 83,6% de digitalização, sem data de CQC.
3. ABA em espanhol (7,0, novo): brecha de idioma, ninguém vende kit.
4. Cuidador/geriatria LATAM (7,0, subiu): Geriactiva 47d, página em reais.
5. Fono Polônia (6,5), 6. Fono ES-LATAM (6,5), 7. Cuidador Espanha (6,0, novo), 8. Consultório MX (6,0).
Mudanças: TO ES-LATAM caiu de 6,5 para 4,5 (Nivel Pro é curso de café, a prova de 70d não existe); Psicopedagogia caiu para 4,5 (IPSY é BR em português, R$ 47/mês); Formatos Profesionales (149d) parou de anunciar; Fono ES-LATAM virou onda de 6 vendedores novos; ELEAM e CQC continuam sem data oficial lida.

## G. O que continuou VERIFICAR
- Tamanho oficial de fono, TO e ABA (PL, IT, ES-LATAM): nenhum número oficial achado (Chile: boletim da Superintendencia existe, PDF ilegível para a ferramenta).
- Data de fiscalização CQC (página oficial deu 403); NOM-004 (nenhuma data, provavelmente não existe); ELEAM (01/10/2028 só em blog; textos do Diário Oficial ilegíveis, conferir na BCN).
- Preço e conteúdo da Care Daily (site é app JS sem texto); Health Connect, Compliance Supports, ABA in School, Mah Souza, Skillio, Centro Digital Terapeutico, GeriKit, GeriaVital, Recursos Legales PRO, EEK Digital, Aprendia, MirelMed, Vetdigital, Esencial VET, Archivos Digitales Express: não remedidos.
- Conteúdo de Laura Cortez, Nexora, andribarrios.fono, Miriam Sousa, Fabiana Segura: só título/moeda.
- Enfermagem, veterinário, podólogo, fisio PL/HU, AU (aged care/NDIS), fono FR/DE/NL/RO/HU/PT/ES-Espanha, historia clínica CO/CL/AR: medição falhou por limite de API.
- SearchAPI: 10.000 de 10.000 créditos usados no mês (outras buscas da chave consumiram), a chave só renova em 08/11/2026. Rodar de novo os itens acima depois disso.
