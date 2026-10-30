# Brechas regionais dentro do país (norma muda por região/estado/cantão)
Data de referência: 30/10/2026. Método: WebSearch + WebFetch + conector Meta (`ads_library_search`, só ativos). SearchAPI sem crédito (não usado).
Limites desta rodada (honestidade): (a) a busca web trouxe sobretudo fontes secundárias; onde só há secundária, marcado VERIFICAR. (b) A busca da Biblioteca de Anúncios é por palavra aproximada e devolve muito ruído; só medi DIAS REAIS por page_id nos vendedores de MX. Nos demais, "sem vendedor visível" = nenhum anúncio relevante nas consultas feitas, NÃO prova de ausência. (c) Austria e Argentina/Colômbia/Canadá ficaram rasos (ver fim).
Escala 0-10 = urgência/prazo x tamanho do público x ausência de vendedor x encaixe no formato (documentos + app por profissão).

## RANKING

| # | Brecha | País | Nota | Régua | Prazo/gancho |
|---|---|---|---|---|---|
| 1 | Psicólogo IT: módulo regional (Lombardia = só comunicação à ATS; Lazio = checar autorização; outras regiões VERIFICAR) | IT | 8 | PRAZO + BRECHA (já em construção) | Lazio DGR 669/2026: 07/02/2027 (só dentistas/estudos com sedação; psicologia VERIFICAR) |
| 2 | Alquiler turístico por Comunidad Autónoma (kit do anfitrião/gestor) | ES | 7 | PRAZO + BRECHA | Cataluña: licenças HUT acabam nov/2028, pedido de prorrogação nov/2027-nov/2028; Madrid Decreto 27/2026 |
| 3 | Programa Interno de Protección Civil (PIPC) por estado | MX | 7 | TESTE (só serviços, todos <30 dias) | Sem data única; lei estadual |
| 4 | Autorización sanitaria de consultas/clínicas por CCAA (psicologia, dentista, fisio, estética) | ES | 6 | PRAZO frouxo + BRECHA | Reforma RD 1277/2003 aprovada 26/03/2026, CCAA ainda adaptam |
| 5 | Cottage food law por estado (kit "venda comida de casa") | US | 6 | TESTE/mercado grande, concorrência alta | Colorado HB26-1033 (04/06/2026); Oklahoma teto sobe 01/11/2026; Indiana 01/07/2026 |
| 6 | Hygieneplan + Hygieneverordnung por Bundesland (Zahnarzt/Arztpraxis) | DE | 6 | BRECHA (0 anúncios na consulta) | Sem prazo |
| 7 | Kita-Gesetze por Land (líder de creche) | DE | 5 | PRAZO por Land | MV: 1:5 na creche desde 01/01/2027 (fonte jornal, VERIFICAR); BY e NW alteraram leis em jul/2026 |
| 8 | Oposiciones docentes: programação didática por CCAA | ES | 5 | TESTE (1 anúncio na consulta) | Convocatórias 2027 por CCAA |
| 9 | Family day care / National Law + Food Safety Supervisor por estado | AU | 5 | PRAZO passou (27/02/2026) + TESTE | Já em vigor |
| 10 | Betriebsbewilligung de dentista por cantão | CH | 4 | BRECHA, mercado pequeno | Sem prazo |
| 11 | AVCB/PPCI por estado (consultório/clínica) | BR | 4 | VERIFICAR | MG Emenda 1/2026 |
| 12 | Ingresos Brutos por província (profissional) | AR | 4 | VERIFICAR | Mendoza RG ATM 27/2026 desde 01/10/2026 |
| 13 | Grundsteuer por Land (Bodenwert BW; Flächenmodell BY, HH, HE, NI) | DE | 4 | Mercado enorme, mas fora de "profissão" | Sem prazo novo |
| 14 | Quebec Loi 96 (profissionais/sites) | CA | 3 | VERIFICAR | sem fonte oficial confirmada |
| 15 | Colombia habilitación departamental | CO | 3 | VERIFICAR (Res. 1732/2026 não confirmada) | |

## DETALHE POR BRECHA

### 1. Itália: o regime muda por região (vale para dentista E para psicólogo)
- Já temos (BASE-LEGAL-IT.md da Valigetta): Lazio DGR 669/2026, BURL n. 64 de 11/08/2026, prazo peremptório 180 dias = 07/02/2027 (protocolar até 05/02). Fonte oficial: https://regione.lazio.it/sites/default/files/documentazione/2026/SAN-DGR-669-06-08-2026.pdf e ...-Allegato1.pdf. Revoga DGR 447/2015 e 1247/2025 (portal Lazio, https://www.regione.lazio.it/documenti/90709, atualizado 04/09/2026). Minha busca nova NÃO reconfirmou o prazo de 07/02/2027 em fonte web aberta: o cálculo vem do arquivo BASE-LEGAL (BURL + 180 dias). Manter como CONFIRMADO só pelo BURL já lido.
- Psicólogo (novo): Lombardia, nota regional de dez/2023 (citada por ATS Brescia): estúdio de profissional único, atendimento por hora marcada, fica fora da autorização sanitária; para psicólogos/psicoterapeutas exige-se comunicação de início de atividade à ATS (modelo MCISA02, requisitos estruturais) (fonte secundária via buscador; o PDF deu 403/404 na leitura direta: https://ats-brescia.it/system/files/field_blocco_redazionale/allegati/1256/paragrafi/21489/Nota%20Regionale%20Studi%20professionali%20Psicologi%2015%20Dicembre%202023.pdf). Lazio: só achei o modelo de pedido de autorização de estúdio médico (LR 4/2003 e RR 20/2019): https://regione.lazio.it/sites/default/files/2024-12/MODELLO%201bis_istanza_aut_studio_sett2021finale.pdf; não ficou claro se psicologia entra. Campania: nada conclusivo. Guia generalista também diz "varia por região".
- Mercado: ~65 mil inscritos no Albo dos dentistas (FNOMCeO, já no BASE-LEGAL). Psicólogos: nº não coletado agora, VERIFICAR (ENPAP/CNOP).
- Concorrência: consulta de anúncios IT "autorizzazione studio odontoiatrico regione" retornou 1 anúncio, de clínica de implantes (SkyDental3D), não de vendedor de documentos. Sem vendedor visível.
- Ação: adicionar à Valigetta dello Psicologo uma matriz "regione -> regime -> documento" (como já existe para o dentista em app-src/dati/regioni.json). Diferencial vs. genérico: o kit nacional não diz se o estúdio precisa de comunicação ou autorização.
- Outras profissões italianas com regime regional (hipótese, NÃO pesquisadas): veterinário, fisioterapista, centro estético, B&B/CIN, asilo nido. VERIFICAR.

### 2. Espanha: alquiler turístico (VUT) é 100% autonómico
- Norma por CCAA (fonte secundária Chekin/derecholocal; texto oficial a conferir): Madrid Decreto 79/2014 modificado em 25/03/2026 (Decreto 27/2026 segundo comentário jurídico; fonte jornal diz mínimo 25 m2, VERIFICAR); Baleares Ley 8/2012 + DL 3/2022; Andalucía Decreto 28/2016 + 31/2024; Canarias Ley 6/2025 (10/12/2025); Cantabria Decreto 50/2025 (24/07/2025); Asturias Decreto 4/2026 (02/02/2026); Galicia Decreto 12/2017. Páginas oficiais: https://www.comunidad.madrid/servicios/consumo/normativa-alojamientos-turisticos ; BOCM: https://www.bocm.es/boletin/CM_Orden_BOCM/2026/04/06/BOCM-20260406-1.PDF (apareceu na busca, não li; VERIFICAR se é o Decreto 27/2026).
- Cataluña: DL 3/2023; o Ajuntament de Barcelona diz que não renovará as 10.000 licenças que vencem em 2028 e que haverá "elimination of all HUTs" (https://ajuntament.barcelona.cat/turisme/en/application-decree-law-32023-tourist-use-flats-huts, sem dia/mês). Data exata: nov/2028 (fontes divergem entre 09/11 e 24/11): VERIFICAR no DOGC. Fora de Barcelona, prorrogação deve ser pedida ao município entre nov/2027 e nov/2028 (fonte secundária). TC validou o decreto em mar/2025 (STC 64/2025, secundária).
- Registro estatal (NRUA) e licença municipal são trâmites SEPARADOS do registro autonómico (várias fontes).
- Público: sem número oficial confiável (95.000 viviendas na Cataluña vem de entidade do setor, não oficial).
- Concorrência: consulta ES "licencia vivienda turística" retornou 26 anúncios, todos imobiliárias/gestoras de propriedade (Canari Apartment, MallorcaCharme etc.), nenhum kit de documentos. Dias não medidos.
- Ressalva de encaixe: não é "profissão" e a oferta tem de evitar parecer assessoria jurídica.

### 3. México: PIPC (Programa Interno de Protección Civil) por estado
- Obrigatório em CDMX (Ley de Gestão Integral de Riesgos y Protección Civil; inclui inmuebles públicos, privados y sociales) e no Edomex (Norma Técnica NTE-001-CGPC-2016, aplicação obrigatória a imóveis dos setores público/privado/social; norma de 2016, ver se há atualização). Vigência do PIPC varia por entidade (gob.mx). Fontes: https://www.proteccioncivil.cdmx.gob.mx/ ; NTE no portal de Atlacomulco (documento oficial municipal). Multas estaduais: NÃO encontradas, VERIFICAR.
- Anúncios (MX, ativos, medido por page_id): Consultores CMC "Cotiza tu PIPC hoy mismo" (início 29/10/2026, 1 dia), PRO-EME "¿Tu empresa está al corriente con Protección Civil?" (11 dias), AjibGroup "Protección civil para clínicas y hospitales" (até 23 dias, 17 anúncios, CTA WhatsApp). Todos serviço com orçamento/WhatsApp; nenhum com 30+ dias; nenhum kit de documentos de preço baixo. Classificação: TESTE; produto kit-PIPC editável por estado é BRECHA no low ticket.
- Ressalva: kit de PIPC normalmente exige responsável/tercero acreditado em alguns estados (VERIFICAR antes de prometer "pronto para entregar").
- Também existente: Impuesto sobre Nómina (ISN) estadual (CDMX 4%, BC 4,25%, fontes divergentes; BHR PDF jan/2026 lista mudanças 2026). Público: todos os empregadores; Mas é nicho contador, concorrência alta. Nota 4.

### 4. Espanha: autorização sanitária de consultas por CCAA
- Base: RD 1277/2003; reforma aprovada pelo Consejo de Ministros (notícia Infocop 26/03/2026): exige título/especialidade para certas intervenções, centros devem acreditar formação do pessoal, controle reforçado; "previsiblemente implicará procesos de adaptación" nas CCAA; sem prazos nem menção a clínicas dentais ou psicologia na notícia (https://www.infocop.es/el-gobierno-aprueba-la-modificacion-del-real-decreto-de-autorizacion-de-centros-sanitarios/).
- Normas autonómicas: Madrid Decreto 51/2006 (mod. Decreto 86/2018); Cataluña Decreto 151/2017; Andalucía Ley 2/1998 de Salud. Requisitos específicos por tipo de consulta: NÃO levantados, VERIFICAR.
- Gancho: "tu consulta, según tu comunidad". Prazo concreto: ausente. Nota 6 (mercado grande, sem data).

### 5. EUA: cottage food e licença de home daycare por estado
- Cottage food (nationalaglawcenter.org, trends, acesso 30/10/2026): TX SB 541 teto US$150k (antes 50k); NV AB 352 US$100k (antes 35k); IA US$50k (antes 35k); MN fee 50->30; ND SB 2386 vendas online (21/03/2025); VT HB 401 US$30k. Mais de metade dos estados mudou regra desde 2022. Fontes secundárias de 2026 (verificar nos sites de cada estado): Colorado HB26-1033 assinada 04/06/2026; Oklahoma teto 75k->250k em 01/11/2026; Indiana nova lei em 01/07/2026; Michigan vendas online mar/2026; Virginia HB 402.
- Home daycare: tamanho que exige licença varia (CA a partir de 4 crianças; IL não exige <4), razões, inspeções: fontes comerciais; VERIFICAR nos órgãos estaduais.
- Anúncios US: consultas "cottage food" e "start a home daycare" voltaram ruído (milhares de resultados irrelevantes); não deu para isolar vendedores. Mercado americano de templates é saturado (Etsy/Teachers Pay Teachers/guias), TESTE apenas. Nota 6 por tamanho, sem prova de brecha.

### 6/7. Alemanha: Länder legislam hygiene e Kita
- Hygiene: não há norma federal única; cada Land editou Hygieneverordnung com base no §23 IfSG (NRW: HygMedVO de 30/03/2012); exigências divergem; Hygieneplan escrito é obrigação derivada dessas verordnungen (fontes: ZWP online, medizinio.de, secundárias e de 2011-2016, VERIFICAR versões atuais). Anúncios DE "Hygieneplan Praxis Vorlage": 0 ativos. Sinal de BRECHA (conferir com termos "QM Zahnarztpraxis", "Hygienemanagement").
- Kita: Personalschlüssel diferem muito por Land. MV: 1 profissional para 5 crianças na creche a partir de 01/01/2027, Hort 1:21 em 01/08/2027 (jornal Nordkurier/anúncio do governo; PDF oficial redirecionou, VERIFICAR); Sachsen 1:4,5 na creche desde 08/2026 (secundária); Thüringen em vigor desde 01/01/2025 (§16 ThürKigaG); Bayern alterou BayKiBiG em 28/07/2026 (GVBl. 2026 S. 401, https://www.verkuendung-bayern.de/gvbl/2026-401/); NRW alterou KiBiz em 21/07/2026 (GV. NRW. 2026 S. 525, https://recht.nrw.de/gvnrw/2026-s525). KiQuTG federal expira no fim de 2026.
- Grundsteuer: 11 Länder usam o modelo federal; BW Bodenwertmodell; BY, HE, HH, NI modelos próprios; Thüringen muda Messzahlen em 2027 (secundárias).

### 8. Espanha: oposições docentes
- Não há convocatória nacional; cada CCAA define (CSIF/Campus Educación, secundárias). Previsões 2027: Madrid secundária +3.000 plazas, Canarias +1.100, CyL maestros +550; Cataluña adia maestros para 2027 (previsões, não firmes). 2026: CLM 543, C. Valenciana 1.959, Extremadura 304, Aragón 308 (maestros). Anúncios ES "programación didáctica LOMLOE oposiciones": 1 (Tutea Oposiciones, EUR). Mercado cheio de academias; kit autonômico por CCAA é TESTE.

### 9. Austrália
- Desde 27/02/2026 (apresentação do governo ACT, https://www.act.gov.au/__data/assets/pdf_file/0004/3028621/National-Child-Safety-Reforms-Information-Session-Feb-2026.pdf; só li o resumo do buscador, o PDF deu 403): todo trabalhador precisa de WWCC/WWVP válido antes de começar; afeta WA, ACT, NT; treino de proteção infantil obrigatório; registro nacional de trabalhadores. Nome e regras do WWCC variam por estado (WWCC NSW/VIC, Blue Card QLD). Food Safety Supervisor: obrigatório em NSW, VIC (classe 1-2), QLD, ACT? (fontes divergem sobre ACT), recomendado em WA/TAS/SA/NT. Nada sobre cottage food australiano. Anúncios "family day care": ruído, sem vendedor isolado. Nota 5.

### 10. Suíça
- Betriebsbewilligung diferente por cantão: Basel-Stadt (taxa CHF 700-3.500, https://www.bs.ch/themen/arbeit-und-steuern/arbeitsbewilligungen/medizinische-berufe/universitaere-medizinalberufe/bewilligungen-der-zahnmedizin); Fribourg exige para dentistas empregados em estrutura ambulatória (https://www.fr.ch/de/gsd/gesa/bewilligungen-ueberwachung-der-gesundheitsfachpersonen-und-institutionen/zahnarzt-zahnaerztin); Zürich: Praxisbewilligung por 10 anos e Betriebsbewilligung adicional para pessoa jurídica; Bern e Neuchâtel sem inspeção de consultórios (relatório 2017, VERIFICAR hoje). Mercado pequeno e trilíngue. Nota 4.

### 11-15. Brasil, Argentina, Canadá, Colômbia, Áustria
- BR: AVCB/PPCI é estadual. MG Emenda 1/2026 (16/01/2026) torna a renovação do AVCB/CLCB ato declaratório por autosserviço (https://bombeiros.mg.gov.br/storage/files/shares/EmendasErratas/Emenda_1_2026.pdf, resumo secundário); SP emite AVCB eletrônico (Via Fácil Bombeiros). Exigência específica para consultório: não encontrada. VERIFICAR. Anúncios BR não consultados.
- AR: IIBB por província (3% a 5% em serviços profissionais, sites comerciais, valores divergem); Mendoza: RG ATM 27/2026 exige mostrar a alíquota nas faturas a consumidor final desde 01/10/2026 (YoFacturo, secundária). Convenio Multilateral quando atua em mais de uma jurisdição. Matrícula/habilitação por província não pesquisada.
- CA: Loi 96 do Quebec; prazo de registro OQLF 01/06/2025 já passou; qualquer prazo 2026 para sites NÃO confirmado em fonte oficial (descartei alegação de vendor). VERIFICAR em oqlf.gouv.qc.ca.
- CO: a Res. 914 de 2025 trata de reprocessamento de dispositivos (DMER), e há rascunho de 2026 para revogá-la; "Res. 1732 de 2026" aparece como novo marco de habilitação mas NÃO confirmei vigência nem prazo; o prazo "03/01/2027 odonto" que constava na nossa pesquisa anterior não foi reconfirmado nesta busca. Habilitação é no departamento/distrito (REPS). VERIFICAR no normograma Supersalud/MinSalud.
- AT: busca devolveu só Alemanha. NÃO coberto.

## LISTA FINAL DE VERIFICAR
1. Lazio DGR 669/2026: reconfirmar prazo 07/02/2027 em fonte aberta (BURL já lido por nós) e se psicologia é afetada.
2. Lombardia nota psicólogos 15/12/2023 e 30/05/2022: ler PDF original (403/404 no fetch); nº de psicólogos na Itália.
3. Cataluña HUT: dia exato (09/11 vs 24/11/2028) no DOGC DL 3/2023; janela de pedido nov/2027-nov/2028.
4. Madrid Decreto 27/2026: texto no BOCM, prazo transitório, mínimo 25 m2.
5. RD 1277/2003 reforma (26/03/2026): BOE, prazos de adaptação por CCAA, impacto em dentista/psicologia.
6. MX PIPC: lei/regulamento por estado (CDMX, Edomex, Jalisco, NL), multas e se exige tercero acreditado; medir dias novamente em 15 dias.
7. US: ler leis estaduais (CO HB26-1033, OK, IN) nos sites oficiais; medir anúncios com termos exatos de nicho.
8. DE: Hygieneverordnungen atuais por Land; MV KiTaG 01/01/2027 no Gesetzblatt; novas buscas de anúncios ("Hygienemanagement Zahnarzt", "QM Praxis").
9. AU: nova lei nacional no site ACECQA; regras de FSS no ACT.
10. CH: situação de BE/NE; fees dos demais cantões.
11. BR/AR/CA/CO/AT: itens acima, todos sem fonte oficial lida.
12. Itália: outras profissões com regime regional (veterinário, fisio, estética, B&B/CIN, nidi) não pesquisadas.

## Diferença vs. versões anteriores
Primeira rodada deste tema (não havia versão anterior). Reaproveitei BASE-LEGAL-IT.md (Lazio/regime por região do dentista) e prazos-de-norma-2026-10-30.md.
