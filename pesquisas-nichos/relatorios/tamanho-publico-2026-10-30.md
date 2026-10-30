# Tamanho real do público por profissão e país (30/10/2026)

Objetivo: dar um número com fonte e ano para cada par profissão × país que apareceu nos relatórios `-v2`, para calcular o teto de venda.
Pesquisa feita só por web (SearchAPI sem crédito até 08/11). Eurostat e SEP/DataMéxico/BLS foram lidos nas páginas/API oficiais; o resto está marcado.

## Como ler
- **Confiança:** OFICIAL = li a estatística do órgão público/conselho. SECUNDÁRIA = número oficial citado por terceiro (imprensa, entidade, diretório), não li a origem. VERIFICAR = não confirmei.
- **Conceito do número** muda o teto, por isso sempre aparece: *em atividade* (practising), *licenciados/colegiados* (têm registro, incluem quem não exerce), *ocupados* (pesquisa de força de trabalho, inclui informais), *unidades/empresas* (estabelecimentos), *títulos* (um profissional pode ter 2 títulos).
- **Nota de tamanho (0–10)** só mede o tamanho do universo, não a demanda: 10 = 500 mil ou mais; 9 = 200–500 mil; 8 = 100–200 mil; 7 = 60–100 mil; 6 = 40–60 mil; 5 = 25–40 mil; 4 = 15–25 mil; 3 = 8–15 mil; 2 = 3–8 mil; 1 = abaixo de 3 mil.
- **Teto de venda (hipótese minha, não dado):** universo em atividade × 0,2% a 0,5% de conversão em 12 meses × ticket. Exemplo: IT psicólogo 87.300 × 0,2–0,5% = 175 a 437 vendas, x €27 = cerca de €4,7 mil a €11,8 mil. Servem para comparar nichos, não para prometer receita.

## Fontes-mestre (lidas hoje)
- Eurostat `hlth_rs_prs2` (saúde; PRACT = em atividade, LIC = licenciados): https://ec.europa.eu/eurostat/databrowser/view/hlth_rs_prs2
- Eurostat `sbs_ovw_act` (empresas por atividade NACE, 2024): https://ec.europa.eu/eurostat/databrowser/view/sbs_ovw_act
- Eurostat `educ_uoe_perp01` (professores por nível, 2023/24): https://ec.europa.eu/eurostat/databrowser/view/educ_uoe_perp01
- INE Espanha, Estadística de Profesionales Sanitarios Colegiados 2024: https://www.ine.es/dyngs/Prensa/EPSC2024.htm
- DataMéxico/Secretaría de Economía (ENOE e DENUE, INEGI), 1T 2026: https://www.economia.gob.mx/datamexico
- BLS Occupational Outlook Handbook (jobs 2025): https://www.bls.gov/ooh/
- Superintendencia de Salud do Chile, Boletín RNPI 4/2025 (31/12/2025): https://www.superdesalud.gob.cl/app/uploads/2026/01/boletin-n4-2025-rnpi-enero-diciembre-2025.pdf

---
## 1. Psicólogos
| País | Universo | Conceito | Ano | Fonte | Confiança | Nota |
|---|---|---|---|---|---|---|
| México | 159.000 | ocupados | 1T 2026 | DataMéxico https://www.economia.gob.mx/datamexico/es/profile/occupation/psicologos | OFICIAL | 8 |
| Itália | 87.300 | psicólogos liberi professionisti ativos na ENPAP | 2024 | ENPAP, comunicado do bilancio 2024 (23/04/2025) https://www.enpap.it/DOC/PRESSAREAENPAP/02-CS-ENPAP_BILANCIO2024.PDF | OFICIAL | 7 |
| Itália | ~141.000 | iscritti ao CNOP (Albo completo) | s/ data | citado em carta no Quotidiano Sanità (não abri, 403) https://www.quotidianosanita.it/?p=140894 | SECUNDÁRIA | 8 |
| Espanha | 43.628 | psicólogos sanitários colegiados | 2024 | INE EPSC2024 (acima). Não inclui psicólogos sem habilitação sanitária | OFICIAL | 6 |
| França | ~89.800 | inscritos no RPPS | out/2024 | site comercial; DREES confirma a migração ADELI→RPPS mas não achei o número | VERIFICAR | 7 |
| Portugal | ~27.000 | inscritos na OPP | ~2023/24 | imprensa (O Cidadão); OPP não publicou número que eu conseguisse ler | SECUNDÁRIA | 4 |
| Polônia | sem registro | não existe rejestr de psicólogos (mp.pl, 2024); ~10 mil formados em 2025, 84 mil estudantes (SWPS) | 2025 | https://www.swps.pl/nauka-i-badania/nasze-dzialania/badania-i-wdrozenia/35334-jak-ksztalci-sie-psychologow-w-polsce-raport-uniwersytetu-swps-i-uniwersytetu-jagiellonskiego | VERIFICAR | ? |
| Alemanha | n/d | Psychotherapeuten por Kammer; não achei total | - | BPtK/KBV Bundesarztregister 2025 (PDF não lido) | VERIFICAR | ? |
| Chile | 101.314 | títulos de psicólogo no RNPI | 31/12/2025 | Superintendencia de Salud (boletim acima) | OFICIAL (títulos) | 8 |
| Peru | 57.566 | colegiados (não diz habilitados) | abr/2024 | La República (via busca) | SECUNDÁRIA | 6 |
| Argentina | ~63.800 | matriculados (Intramed); ~92 mil se usar 200 por 100 mil hab. | s/ data | não achei a origem | VERIFICAR | 7 |
| Colômbia | n/d | Colpsic/ReTHUS não publica total acessível | - | estudo Colpsic 2006–2021 (PDF não lido) | VERIFICAR | ? |
| EUA | 209.400 | empregos | 2025 | BLS | OFICIAL | 9 |

## 2. Dentistas
| País | Em atividade | Licenciados/colegiados | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|---|
| Alemanha | 71.983 | 106.448 | 2024 | Eurostat | OFICIAL | 7 |
| Itália | 51.680 | 66.250 | 2024 | Eurostat | OFICIAL | 6 |
| França | 48.413 | n/d | 2024 | Eurostat | OFICIAL | 6 |
| Polônia | 36.965 | 45.978 | 2024 | Eurostat | OFICIAL | 5 |
| Espanha | 33.300 | 42.860 | 2024 | Eurostat; INE (colegiados) | OFICIAL | 5 |
| Romênia | 21.647 | 22.761 | 2024 | Eurostat | OFICIAL | 4 |
| Portugal | 11.014 | 13.212 | 2024 | Eurostat | OFICIAL | 3 |
| Países Baixos | 10.414 | 11.264 | 2024 | Eurostat | OFICIAL | 3 |
| Bélgica | 9.260 | 14.647 | 2024/25 | Eurostat | OFICIAL | 3 |
| Hungria | 7.597 | 12.011 | 2024 | Eurostat | OFICIAL | 2 |
| Rep. Tcheca | 8.289 | n/d | 2024 | Eurostat | OFICIAL | 3 |
| Áustria | 5.898 | n/d | 2025 | Eurostat | OFICIAL | 2 |
| Irlanda | 2.670 | 3.945 | 2025 | Eurostat | OFICIAL | 1 |
| México | 76.188 consultórios dentais (unidades) | - | DENUE 2026 | DataMéxico https://www.economia.gob.mx/datamexico/es/profile/industry/offices-of-dentists (2025: 74.034) | OFICIAL | 7 |
| EUA | 161.400 empregos | - | 2025 | BLS | OFICIAL | 8 |
| Chile | 36.673 títulos de cirujano dentista | - | 31/12/2025 | RNPI | OFICIAL | 5 |
| Peru | 36–42 mil colegiados | - | s/ data | UPC; Congreso (Ley 32656 cria novo Colegio de Cirujanos Dentistas, 2026) | SECUNDÁRIA | 5 |
| Colômbia | ~85.800 inscritos ReTHUS | - | s/ data | diretório cliini.ai (terceiro; não confere com fonte oficial) | VERIFICAR | ? |
| Argentina | ~53.000 matriculados | - | s/ data | Intramed (origem não achada) | VERIFICAR | ? |
Empresas de consultório dentário (Eurostat Q86.23, 2024): IT 54.277, ES 37.619, FR 42.019, DE 38.047, PL 32.830, PT 11.561, RO 9.813, NL 11.507, HU 5.970, CZ 5.556, BE 6.712.
NOTA: o "dentistas" por ocupação (ENOE) da DataMéxico é de 2021 (147 mil, mistura médicos); não usar.

## 3. Fisioterapia / reabilitação / fono / TO / nutrição
| Profissão | País | Universo | Conceito | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|---|---|
| Fisio | Alemanha | 205.000 | em atividade | 2024 | Eurostat | OFICIAL | 9 |
| Fisio | França | 108.030 | em atividade | 2024 | Eurostat (DREES: 104.200 cinesiterapeutas, 01/01/2024) | OFICIAL | 8 |
| Fisio | Itália | 71.263 | em atividade | 2024 | Eurostat | OFICIAL | 7 |
| Fisio | Espanha | 64.700 (Eurostat) / 71.638 (INE colegiados 2024) | em atividade / colegiados | 2024 | Eurostat; INE. Os relatórios diziam 74.990 (INE 2025, não reconferido) | OFICIAL | 7 |
| Fisio | Polônia | 62.087 | em atividade | 2024 | Eurostat | OFICIAL | 7 |
| Fisio | Países Baixos | 34.013 | em atividade | 2024 | Eurostat | OFICIAL | 5 |
| Fisio | Bélgica | 27.594 | em atividade | 2024 | Eurostat | OFICIAL | 5 |
| Fisio | Rep. Tcheca / Áustria / Suécia / Dinamarca | 9.379 / 16.713 / 14.195 / 11.833 | em atividade | 2024 | Eurostat | OFICIAL | 3 / 4 / 3 / 3 |
| Fisio | Hungria / Irlanda / Romênia | 7.026 / 7.455 / 3.351 | em atividade | 2024/25 | Eurostat | OFICIAL | 2 |
| Fisio | Portugal | n/d | - | - | Eurostat sem o dado | VERIFICAR | ? |
| Fisio | EUA | 283.700 | empregos | 2025 | BLS | OFICIAL | 9 |
| Fisio (kinesiólogo) | Chile | 48.538 | títulos | 31/12/2025 | RNPI | OFICIAL | 6 |
| Fisio | Colômbia | ~49.100 | inscritos ReTHUS | s/ data | cliini.ai (terceiro) | VERIFICAR | ? |
| Fisio | México | n/d | DataMéxico "fisioterapeutas, audiólogos e logopedas" dá só 3.360 ocupados (1T 2026), amostra ENOE pequena e subestima | - | https://www.economia.gob.mx/datamexico/es/profile/occupation/fisioterapeutas-audiologos-y-logopedas | VERIFICAR | ? |
| Fono | Espanha | 12.196 | logopedas colegiados | 2024 | INE | OFICIAL | 3 |
| Fono | Itália | ~15.000 | logopedisti (24 por 100 mil hab.) | s/ data | entrevista da presidente da comissão do albo (Quotidiano Sanità) | SECUNDÁRIA | 4 |
| Fono | Chile | 24.756 | títulos | 31/12/2025 | RNPI | OFICIAL | 4 |
| Fono (SLP) | EUA | 193.400 | empregos | 2025 | BLS | OFICIAL | 8 |
| Fono | Polônia | n/d (~300 no setor saúde, dado de 2023, só parte) | - | - | logopeda.org.pl | VERIFICAR | ? |
| Fono | França | n/d | - | - | DREES (RPPS) não lido | VERIFICAR | ? |
| TO | Espanha / Chile / EUA | 9.287 / 20.784 / 169.600 | colegiados / títulos / empregos | 2024 / 2025 / 2025 | INE / RNPI / BLS | OFICIAL | 3 / 4 / 8 |
| Nutrição | Espanha | 8.075 | dietistas-nutricionistas colegiados | 2024 | INE | OFICIAL | 3 |
| Nutrição | Chile | 30.616 | títulos | 31/12/2025 | RNPI | OFICIAL | 5 |
| Nutrição | EUA | 86.300 | empregos | 2025 | BLS | OFICIAL | 7 |
| Nutrição | Colômbia | ~21.100 | ReTHUS | s/ data | cliini.ai | VERIFICAR | ? |
| Podologia | Espanha | 9.258 | colegiados | 2024 | INE (ruptura de série por depuração) | OFICIAL | 3 |

## 4. Médicos de consultório, enfermagem
| País | Universo | Conceito | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|---|
| México | 85.908 | consultórios médicos (unidades) | DENUE mai/2026 | DataMéxico https://www.economia.gob.mx/datamexico/es/profile/industry/offices-of-physicians | OFICIAL | 7 |
| EUA | 3.465.400 | enfermeiros RN | 2025 | BLS | OFICIAL | 10 |
| EUA NCLEX | 192.916 | formados nos EUA, 1ª tentativa, 2025 | 2025 | NCSBN (PDF não lido; via resumo). O "328 mil" da v1 continua sem fonte | SECUNDÁRIA | 9 |
| Enfermeiros (em atividade) | DE 1.045.000 · FR 607.644 (2023) · IT 407.750 · ES 280.200 · PL 219.881 · PT 77.139 | - | 2024 | Eurostat | OFICIAL | 10 / 10 / 9 / 9 / 9 / 7 |
| Chile | 95.837 (enfermeiros) / 72.263 (médicos) | títulos | 31/12/2025 | RNPI | OFICIAL | 7 |

## 5. Veterinários
| País | Universo | Conceito | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|---|
| EUA | 91.100 | empregos | 2025 | BLS | OFICIAL | 7 |
| México | 62.700 | ocupados | 1T 2026 | DataMéxico (ocupação 2232) | OFICIAL | 7 |
| Espanha | 37.836 | colegiados | 2024 | INE | OFICIAL | 5 |
| Empresas veterinárias (Eurostat M75.00, 2024) | IT 18.613 · ES 10.711 · FR 11.321 · DE 10.900 · PL 9.223 · BE 5.478 · RO 3.337 · NL 3.203 · PT 2.959 · CZ 2.942 | unidades | 2024 | Eurostat | OFICIAL | 4 / 3 / 3 / 3 / 3 / 2 / 2 / 2 / 1 / 1 |

## 6. Advogados, contadores, imobiliário
| Profissão | País | Universo | Conceito | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|---|---|
| Advogado | México | 445.000 | ocupados | 1T 2026 | DataMéxico https://economia.gob.mx/datamexico/es/profile/occupation/abogados | OFICIAL | 9 |
| Advogado | Itália | 211.464 ativos (228.641 iscritti Cassa Forense incl. aposentados em 2025; 233.260 em 2024) | ativos / iscritti | 2024-25 | Il Sole 24 Ore e Censis 2025 (via busca) | SECUNDÁRIA | 9 |
| Advogado | Espanha | 149.695 ejercientes (+88.692 não ejercientes) | colegiados | 2024 | CGAE via Aranzadi LA LEY (27/02/2025) | SECUNDÁRIA | 8 |
| Advogado | EUA | 863.700 | empregos | 2025 | BLS | OFICIAL | 10 |
| Advogado | Argentina | ~126.000 | matriculados | s/ data | v2, sem fonte lida | VERIFICAR | ? |
| Escritórios jurídicos (Eurostat M69.10, empresas 2024) | IT 182.616 · ES 87.275 · FR 86.738 · PL 59.720 · DE 59.655 · PT 32.782 · BE 25.859 · NL 23.954 · CZ 14.011 | - | 2024 | Eurostat (RO 184 e DE parecem diferença de classificação, não usar para comparar) | OFICIAL | - |
| Contador | México | 470.000 (subgrupo mais amplo: 534.000) | ocupados | 1T 2026 | DataMéxico https://www.economia.gob.mx/datamexico/es/profile/occupation/contadores-y-auditores | OFICIAL | 9 |
| Contador | EUA | 1.595.200 | empregos | 2025 | BLS | OFICIAL | 10 |
| Contador | Colômbia | 334.685 | contadores ativos com tarjeta profesional | jun/2025 | JCC via INCP https://incp.org.co/publicaciones/infoincp-publicaciones/2025/09/junta-central-de-contadores-presenta-informe-su-rendicion-de-cuentas-de-2024-y-2025/ | SECUNDÁRIA (relatório oficial citado pelo INCP) | 9 |
| Contador | Itália | 119.050 | iscritti ao Albo (commercialisti) | 31/12/2025 | Fondazione Nazionale Commercialisti, Rapporto 2026 https://www.fondazionenazionalecommercialisti.it/filemanager/active/01901/2026_07_16_Rapporto_2026_Scheda_di_sintesi.pdf?fid=1901 | OFICIAL | 8 |
| Contador | Argentina | ~140.000 | s/ data | v2, sem fonte lida | VERIFICAR | ? |
| Contabilidade (Eurostat M69.20, empresas 2024) | IT 135.640 · ES 65.444 · DE 55.605 · PL 53.173 · CZ 46.302 · NL 38.982 · HU 29.276 · PT 23.104 · FR 23.700 (classificação distinta) | - | 2024 | Eurostat | OFICIAL | - |
| Imobiliário | EUA | 530.600 | corretores | 2025 | BLS | OFICIAL | 10 |
| Imobiliário | México | n/d | NOM-247 + Profeco; universo não achado | - | - | VERIFICAR | ? |
| Imobiliárias (Eurostat L68.31, empresas 2024) | FR 83.705 · ES 58.106 · IT 41.751 · DE 28.460 · PT 21.055 · PL 18.089 · CZ 15.355 · NL 13.467 | - | 2024 | Eurostat | OFICIAL | - |
| Preparador de impostos | EUA | 879.698 | PTIN ativos | 2025 | IRS (da rodada anterior; não reaberto) | SECUNDÁRIA | 10 |

## 7. Professores, educação infantil, inclusão
| Profissão/País | Universo | Conceito | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|---|
| Polônia, nauczyciele | 511.000 | professores | 2024/25 | GUS https://stat.gov.pl/dla-mediow/informacje-prasowe/polska-szkola-w-liczbach-jak-wyglada-edukacja-w-roku-szkolnym-20242025,36,1.html | OFICIAL | 10 |
| México, docentes de educação básica | 1.237.782 | docentes | 2024/25 | SEP/SICE (da v2; não reaberto). DataMéxico 1T 2026: pré-escolar 250.000 ocupados | SECUNDÁRIA / OFICIAL | 10 |
| Espanha, docentes | 806.178 | docentes (MEFD 2025-26) | 2025-26 | v2, não reaberto. Eurostat 2024: ED02 102.393, ED1 248.253, ED2-4 344.203 | SECUNDÁRIA | 10 |
| Romênia, cadre didactice | 219.900 | pré-universitário | 2025/26 | INS via Edupedu (secundária) | SECUNDÁRIA | 9 |
| Chile, docentes de aula | 169.115 | docentes (CEM/Horizontal) | 2025 | secundária; não inclui educadoras de párvulos | SECUNDÁRIA | 8 |
| Itália, docenti di sostegno | "261 mil" na v1 | - | - | Sem fonte lida; parece alto. Eurostat IT: pré-escolar 123.988, primária 250.961, secundária 458.617 (total de professores) | VERIFICAR | ? |
| Alemanha, pessoal de Kita | 799.496 (Destatis, v1) vs 613.521 professores ED0 no Eurostat 2024 | - | 2024 | conceitos diferentes (o Destatis inclui cuidadores) | SECUNDÁRIA | 10 |
| França, CRPE | 49.524 (bac+3) + 38.130 (bac+5) candidaturas | 2026 | v1, não reaberto | SECUNDÁRIA | 7 |
| Pré-escola (Eurostat ED02, professores, 2024) | DE 369.434 · IT 123.988 · PL 123.331 · FR 113.887 · ES 102.393 · RO 37.896 · CZ 31.575 · HU 25.591 · PT 17.126 | - | 2024 | Eurostat | OFICIAL | 10 / 8 / 8 / 8 / 8 / 5 / 5 / 5 / 4 |
| EUA | pré-escolar 583.200 · especial 584.100 · cuidadores de crianças 1.010.300 · assistentes sociais 816.100 | empregos | 2025 | BLS | OFICIAL | 10 |
| Creches/day care (Eurostat Q88.91, empresas 2024) | NL 16.827 · FR 5.648 · IT 4.028 · PL 2.967 · IE 2.505 · DE 1.878 · PT 1.337 · ES 1.022 | - | 2024 | Eurostat (conceito estreito; não pega creche dentro de escola) | OFICIAL | 3 / 2 / 2 / 1 / 1 / 1 / 1 / 1 |
| Reino Unido, provedores Ofsted | 59.700 (24.700 childminders; 27.935 creches/pré-escolas) | provedores | 31/03/2026 | gov.uk (da v2, não reaberto) | SECUNDÁRIA | 6 (childminders: 4) |
| Austrália, serviços NQF | 18.197 | serviços aprovados | 01/07/2026 | ACECQA via busca (site deu 403) | SECUNDÁRIA | 4 |
| Austrália, NDIS | 26.282 registrados / 17.464 ativos | provedores | dez/2025 | NDIS Commission, só via resumo (PDF novo deu timeout) | SECUNDÁRIA | 5 |
| África do Sul, ECD | 42–50 mil programas | - | - | v2, não reaberto | VERIFICAR | 5 |
| Reino Unido, home care | 499.279 pessoas atendidas (dez/2025); nº de provedores não achado | - | dez/2025 | gov.uk, estatísticas trimestrais | VERIFICAR (provedores) | ? |
| Reino Unido, care homes | 13.475 | - | - | LocalGov, via v2 | SECUNDÁRIA | 3 |

## 8. Alimentos (HACCP), estética, ofícios
| Segmento | Universo | Ano | Fonte | Conf. | Nota |
|---|---|---|---|---|---|
| Restaurantes e food service (Eurostat I56.10, empresas) | FR 184.484 · IT 161.871 · DE 141.777 · ES 79.508 · PL 46.581 · CZ 44.743 · PT 35.576 · NL 35.390 · BE 34.565 · AT 27.576 · HU 18.851 · RO 16.103 · IE 9.735 | 2024 | Eurostat | OFICIAL | 10 / 10 / 10 / 7 / 6 / 6 / 5 / 5 / 5 / 5 / 4 / 4 / 3 |
| Cuidado: o ~179 mil da v2 (FR) e o ~101,5 mil lokali da v2 (PL) | divergem do Eurostat (FR 184 mil; PL 46,6 mil empresas, que contam empresas e não pontos de venda) | - | v2 | - | usar Eurostat para comparação entre países |
| México, restaurantes/estabelecimentos de alimentos | ~772 mil (subsetor) | - | v2, sem fonte lida | VERIFICAR | ? |
| Salões/beleza (Eurostat S96.02, empresas) | FR 161.574 · IT 140.985 · ES 140.439 · PL 103.068 · DE 88.079 · NL 81.841 · PT 54.384 · HU 48.141 · CZ 43.396 · RO 41.073 · BE 24.106 · AT 18.884 · IE 12.628 | 2024 | Eurostat | OFICIAL | 10 / 9 / 9 / 8 / 7 / 7 / 6 / 6 / 6 / 6 / 4 / 4 / 3 |
| Bem-estar físico (Eurostat S96.04) | FR 25.533 · HU 11.272 · PL 6.765 · DE 5.302 · NL 5.376 · RO 5.309 · PT 5.184 | 2024 | Eurostat | OFICIAL | 5 / 3 / 2 / 2 / 2 / 2 / 2 |
| México, peluqueiros/barbeiros/estilistas | 474.000 | 1T 2026 | DataMéxico (ocupação) | OFICIAL | 9 |
| México, unidades de beleza e cuidado pessoal (rama 8121) | 310.869 | mai/2026 | DataMéxico (v1, não reaberta) | SECUNDÁRIA | 9 |
| Colômbia, estabelecimentos de beleza | 50.739 | 2019 | Gaceta del Congreso 998/2019 (7 anos; desatualizado) | SECUNDÁRIA | 6 |
| Argentina, salões | ~78.000 | 2020 | Cronista (estimativa CAPA/UPA) | SECUNDÁRIA | 7 |
| Residências de idosos (Eurostat Q87.30, empresas) | IT 3.479 · PT 2.636 · ES 2.284 · DE 1.789 | 2023/24 | Eurostat | OFICIAL | 2 / 1 / 1 / 1 |
| Chile, ELEAM | 947 | - | CIPER (v2, não reconfirmado) | VERIFICAR | 1 |
| Reino Unido, landlords | ~2,8 milhões | - | fonte não oficial (v2) | VERIFICAR | ? |

## 9. Provas e concursos (universo anual)
| Prova | Número | Fonte | Conf. |
|---|---|---|---|
| Polônia, matura 2026 | 322.859 | imprensa (v2); CKE não reconferido | VERIFICAR |
| México, ENARM 2025 | 66.278 inscritos | v1, secundária | VERIFICAR |
| Espanha, OEP 2026 AGE | 27.232 plazas | RD 387/2026 (divergência entre fontes) | SECUNDÁRIA |
| Chile, Evaluación Docente | 169.115 docentes de aula no universo | ver seção 7 | SECUNDÁRIA |

---
## Ranking: onde o universo é grande o bastante para valer o kit (por nota de tamanho, só OFICIAL ou SECUNDÁRIA forte)
1. **EUA** em quase tudo (psicólogos 209 mil, fisio 284 mil, fono 193 mil, dentistas 161 mil, contadores 1,6 mi). É o maior teto, mas o idioma é inglês e é o mercado mais saturado; só vale com tese forte.
2. **México** (já temos psicólogo): psicólogo 159 mil, advogado 445 mil, contador 470 mil, peluqueiro 474 mil, dentista 76 mil consultórios, consultório médico 86 mil, veterinário 62,7 mil.
3. **Alemanha**: fisio 205 mil, dentistas 72 mil, Kita 369–800 mil. Brecha total de kit (v2), mas copy nativa.
4. **França**: fisio 108 mil, dentistas 48 mil, psicólogo ~90 mil (VERIFICAR), 184 mil restaurantes, 162 mil salões.
5. **Itália** (onde já vendemos): psicólogo 87 mil ativos (141 mil no Albo), advogado 211 mil, commercialista 119 mil, fisio 71 mil, dentista 52 mil, 162 mil restaurantes, 141 mil salões.
6. **Espanha**: fisio 65–72 mil, psicólogo sanitário 43,6 mil, dentistas 33 mil, advogados 150 mil, docentes 806 mil.
7. **Polônia**: fisio 62 mil, dentistas 37 mil, 511 mil professores, 103 mil salões.
8. **Chile**: psicólogos 101 mil títulos, fisio 48,5 mil, dentistas 36,7 mil, nutri 30,6 mil, fono 24,8 mil (todos OFICIAL).
9. **Colômbia**: contador 334.685 (único oficial); saúde sem número oficial.
Países pequenos (PT, HU, RO, IE, AT, NL, BE, CZ): universos de 2 a 20 mil em saúde; só vale com a tese de prazo.

## Correções em relação à versão anterior (números que estavam sem fonte)
- Fisio ES: 74.990 (INE 2025) agora tem duas leituras oficiais: 64.700 em atividade (Eurostat 2024) e 71.638 colegiados (INE 2024). Usar o menor para teto.
- Psicólogo IT: antes sem número. Agora 87.300 ativos na ENPAP (oficial) e ~141 mil no Albo (secundária).
- Psicólogo MX: antes sem número. 159.000 ocupados (DataMéxico 1T 2026).
- Dentista MX: antes sem número. 76.188 consultórios (DENUE 2026).
- Chile (kine, psico, dentista): a v2 calculava por % (psicólogos ≈99,6 mil, kine ≈47,7 mil, dentistas ≈29,2 mil). Contagem real do boletim: psicólogos 101.314, kine 48.538, dentistas 36.673 (títulos). O dentista estava subestimado em 20%.
- Veterinário MX: 62.700 ocupados confirmado (a nota antiga "43,5 mil" é do 2T 2023).
- NCLEX 328 mil (v1): continua sem fonte; usar 192.916.
- Tamanho IT sostegno 261 mil: NÃO confirmado; está marcado VERIFICAR (Eurostat dá 251 mil professores de primária no total do país, então o número não faz sentido como docentes de sostegno).
- Estética CO 50.739 é de 2019; MX 310.869 não foi reaberto.

## Lista final de VERIFICAR (o que não consegui confirmar)
1. Psicólogos: PL (sem registro), DE (total de Psychotherapeuten), FR (RPPS oficial), PT (número da OPP), CO (Colpsic), AR e PE (origem dos números).
2. Dentistas CO e AR, fisio/nutri/TO CO (todos só em diretório de terceiro), fisio MX (DataMéxico dá amostra pequena).
3. Fono: PL, FR (orthophonistes), IT (data da cifra de 15 mil).
4. Docenti di sostegno IT (261 mil).
5. Advogados e contadores AR (~126 mil e ~140 mil).
6. Corretores/imobiliário MX e landlords UK (~2,8 mi).
7. Home care UK (número de provedores CQC, só achei pessoas atendidas).
8. NDIS AU (PDF de jun/2026), ACECQA (403), NCSBN (PDF não lido), IRS PTIN (não reaberto).
9. HACCP: MX restaurantes (~772 mil); FR/PL divergem do Eurostat.
10. Docentes ES (806.178), MX (1.237.782), RO e CL são secundárias; confirmar em MEFD, SEP/SICE, INS, CEM.
11. Matura PL 322.859, ENARM 66.278.
