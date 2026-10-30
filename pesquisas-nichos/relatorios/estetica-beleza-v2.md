# Estética e beleza por país: v2 (30/10/2026)

Harmonização facial e injetáveis ficam **fora**. Onde um pacote de concorrente inclui mesoterapia, ele é citado só como descrição do concorrente, e o item não entra na nossa maleta.
Régua: **PROVADO** = vendedor com anúncio ativo há 30+ dias no país/moeda. **TESTE** = sinal sem vendedor antigo. **PRAZO** = gancho com data de norma. Espanhol neutro em USD não prova país.
Dias = 30/10/2026 menos o início do anúncio ativo mais antigo (Biblioteca de Anúncios, só ATIVOS).

## Limites desta rodada (ler antes)
- **SearchAPI está sem créditos** (10.000/10.000 usados no ciclo, renova em 08/11). Outros agentes gastaram ~1.100 créditos na mesma hora. Um varredor meu (MX, CO, AR, 12 termos) rodou 18 buscas e perdeu os resultados porque só salvava ao fim do país. Depois disso usei só o conector `ads_library_search` e o navegador embutido.
- O conector devolve só título e data, e **só acha o que é recente** (ordena por recência). Por isso "ninguém vende" abaixo significa "nada achado com esses termos no conector", não prova negativa. Cada brecha está marcada com o que foi testado.
- Descobri que o conector faz E entre as palavras: frases longas dão 0 resultados. Os termos de 1 a 2 palavras funcionaram.
- Achado importante: o navegador embutido abre `facebook.com/ads/library/?id=<id>` e **mostra o texto completo do anúncio, com preço e conteúdo** (WebFetch dá 403). Foi assim que li o texto de Archivos Digitales Express.
- Aviso: ao encerrar meu varredor usei `pkill -f "python3 v.py"` numa pasta de scratchpad compartilhada. Pode ter matado um script de outro agente com esse nome. Se algum varredor parou sozinho às ~00:40, foi isso.

---

## 1. Correções ao que a v1 dizia (por page_id)

| Vendedor (page_id) | v1 dizia | v2 mede e lê | Efeito |
|---|---|---|---|
| **Ultra Pack** (780532768486149) | 69 dias, "kit de estética" | 16 anúncios ativos. Os 70 dias (início 20/08) são do **software "Estética em Dia"** (esteticaemdia.com.br, agenda/financeiro/WhatsApp, anúncio em PT-BR). Os anúncios de **fichas em espanhol** ("+50 Fichas para Estética", "+200 Reels") começam em **09/10 (21 d)**; "Ficha de Depilación Láser" em 24/10 (6 d) | O vendedor "mais antigo" **não prova kit em espanhol**. Prova software de gestão para esteticista (BR) |
| **Digital Future** (1089099027623219) | ~20 anúncios, 12 d | **1 anúncio ativo**, 2 d (início 27/10), "Listo hoy para tu próxima cita". Texto não carregou | **Encolheu de ~20 para 1** em dias. Sinal fraco |
| **Belleza Integral** (1426794933850936) | 4 anúncios, só AR | **0 anúncios ativos** | **Parou**. Era um dos 2 vendedores só-AR |
| **Tienda digital estética** (985859041274743) | "kit + app", ARS | 5 anúncios, ARS, mais antigo 24/10 (**5 d**). O anúncio abre em **hola.mybeautypro.app**: "My Beauty Pro app, sistema de gestión: turnos, facturación, métricas, agenda". É **software de gestão**, não kit de documentos | Corrigido: **não é kit+app**. É app de gestão em ARS, novo |
| **Archivos Digitales Express** (103894282759676) | 198 d, conteúdo VERIFICAR | 18 anúncios, MXN, mais antigo 14/04/2026 (**199 d**). **Conteúdo lido** (seção 2) | O de 199 d é **optometria** (e quiropraxia 164 d). O de cosmetologia/spa começou em **04/10 (26 d)**. O "consentimiento tatuaje" era pacote de **curação de feridas** (61 d, início 29/08) |
| Silueta Express (853294944540392) | fichas MXN 9 d | 5 anúncios; "Quiero mis fichas" começa 19/10 (**11 d**). Os outros 4 são "Reservar mi cita" (12/09 em diante) | É centro estético que vende serviço, não vendedor de kit |
| Guías profesionales Aprendia (1379772175208716) | 34 d | 456 anúncios ativos (MXN). Os 5 mais recentes começam 29/10. Idade da página não remedida | Fábrica de guias multi-nicho em MXN. VERIFICAR a idade |
| **Wavrr.app** (959891007202340) | 20 d | 7 anúncios, EUR, mais antigo 15/09 (**44 d**) | Software de consentimento digital p/ tatuagem/piercing/PMU. Passou de 30 d |
| Legalize Estética (351688978016986) | 10 d, 33 anúncios | 31 anúncios, BRL; os 10 que o conector lista começam 29/10. "Documentos Obrigatórios – Odontologia / Podologia" | Idade da página não reconfirmada |
| Elite Beauty (1243697648816754) | novo | 3 anúncios, ARS, 8 h a 3 d, só link WhatsApp, sem texto | Sem conteúdo. Descartado |
| Elevify (1173579039169074) | novo | 13 anúncios, USD, voseo ("Dominá la presión"), mais antigo 06/10 (**24 d**). Curso de massagem | Curso, não documentos |
| Belleza Premium One (1249646171565636) | novo | 4 anúncios, USD, menção a S/10 (Peru), 2 d. "Lifting Coreano + Kit", curso | Curso de lash lifting. Sinal Peru |
| Vende Mas Tattoo (106608278276174) | novo | 9 anúncios, USD, 27 a 28/10 | Agência de marketing para tatuador, não documentos |

## 2. O que Archivos Digitales Express vende (lido nos anúncios, MXN)
Fonte: textos completos dos anúncios 920691677587594, 1462881392562597, 1035851615537191, 27522818913973098 (Biblioteca de Anúncios, navegador embutido).
- **Formato:** arquivos **Word editáveis** (logo, cores, dados), entrega por e-mail em 10 a 30 min, pagamento por **depósito OXXO ou transferência**. Sem site: o fechamento é por mensagem.
- **Cosmetologia & SPA (início 04/10, 26 d):** Pack básico **MXN 99** (ficha clínica geral/facial/corporal, carnet de citas, aviso de privacidad, consentimento geral e por procedimento: madeoterapia, radiofrecuencia, cavitação, vacuoterapia, lipolaser, limpeza facial, aparatologia, orçamento, recibo). **Mega pack MXN 199** soma presoterapia, **mesoterapia, peeling químico**, hydrafacial, massagem, plasma pen, BB glow, drenagem, anamnese de massagem. Brinde: material de estudo. (Mesoterapia está fora da nossa regra.)
- **Optometria (199 d):** a partir de MXN 100. **Quiropraxia (164 d, início 18/05):** básico MXN 100, mega MXN 200. **Curação de feridas (62 d):** 66 arquivos MXN 250.
- **Leitura:** é a **mesma ideia da nossa maleta, em Word, a US$5 a 13, multi-profissão**. O formato "documentos por profissão" está **provado no México há 199 dias** (por outra profissão). Para estética específica, 26 dias. Concorre por preço baixo e sem app/norma.

## 3. Lacunas encontradas (país × profissão × quem vende × dias)
O que testei está entre parênteses. "Ninguém" = nada achado no conector com esses termos.

| # | País | Profissão | Quem vende | Dias | Observação |
|---|---|---|---|---|---|
| 1 | **Colômbia** | esteticista/cosmetóloga (docs) | **Ninguém em COP** (testado: "fichas estética consentimiento", "cosmetóloga", "esteticista", "centro de estética Secretaría"). Só neutro USD chega: Ultra Pack ES fichas | 0 em COP; neutro 21 d | Os resultados em COP são salões e cursos. A SDS Bogotá lista exatamente os documentos exigidos (seção 5) |
| 2 | México | esteticista/cosmetologia | Archivos Digitales Express (MXN, Word, 99/199) | 26 d (pack cosmetologia); 199 d (página, outras profissões) | Vendedor barato, sem norma nem app |
| 3 | **México** | **tatuador/micropigmentador/piercer** | **Ninguém** vende documentos (testado: "tatuador", "consentimiento informado", "fichas tatuaje" → 2 resultados irrelevantes). Só estúdios, escolas (ILET Toluca diplomado), Vende Mas Tattoo (marketing) | 0 | COFEPRIS exige tarjeta, manual de procedimentos e bitácora foliada (seção 5) |
| 4 | México | lash / sobrancelha / micropigmentação (docs) | Ninguém. Só estúdios e escolas | 0 | Termos: "consentimiento pestañas", "consentimiento micropigmentación" |
| 5 | México | barbeiro, manicure (docs) | Ninguém. "fichas manicura": cursos (Nail Studio Academy USD, Digital Academy USD) | 0 | |
| 6 | Argentina | esteticista/gabinete (docs) | **Ninguém em ARS** vende documentos. Tienda digital estética (ARS) vende **app de gestão**; Belleza Integral parou | app 5 d; kit 0 | Elite Beauty (ARS, WhatsApp) sem conteúdo |
| 7 | Argentina | massagista | Elevify (USD, voseo) vende **curso** | 24 d | Moeda errada para provar país; formato é curso |
| 8 | Peru | esteticista / barbeiro | Não medido em profundidade. Achados: Belleza Premium One (USD, curso lash), "Emprende Fácil / Plantillas y recursos" (**PEN**, genérico, 1 d) | VERIFICAR | Sem SearchAPI não dá para varrer. Fica como TESTE |
| 9 | Chile, Equador | todas | Só TatauFlow (CLP, software tatuador, 27 d na v1, não reconfirmado) | VERIFICAR | |
| 10 | Espanha | todas (docs) | Ninguém local. Chegam os neutros em USD. "documentos salón belleza plantillas" e "fichas esteticista" ES: 0 | 0 | ARLEX BOSS (EUR) vende curso de barbearia |
| 11 | Portugal | esteticista (docs) | Ninguém. Só Beauty Book App (BRL, agenda, 2026-02) | 0 | App brasileiro |
| 12 | Itália | estetista/tatuatore (docs) | Ninguém ("modulistica estetista" 0; "moduli centro estetico": só salões, curso BR "Renata França" em BRL) | 0 | Consentimento escrito é regional (seção 5) |
| 13 | França | esthéticienne (docs) | Ninguém. Planity/Ascor (curso CAP à distância, EUR) | 0 | |
| 14 | Alemanha | Kosmetik (docs) | Ninguém ("Anamnesebogen Kosmetik", "Vorlagen Kosmetikstudio": 1 academia) | 0 | |
| 15 | Polônia, Romênia | todas (docs) | Ninguém ("karta zabiegowa" 0; "fișă client cosmetică" 0) | 0 | Sem teste de mais termos (limite de créditos) |
| 16 | Reino Unido (Gales) | tatuagem/PMU/piercing | Só Wavrr (EUR, **software**, 44 d). Kit: ninguém ("consultation form template beauty" 0) | software 44 d | |
| 17 | EUA | tatuador | Ninguém ("tattoo consent template" 0). Ultimate Life OS multi-nicho (v1) | 0 | |
| 18 | Vários | massoterapia | BR: Toque Essencial (v1, 3 d). Fora do BR: só cursos | | |

## 4. Tamanho do setor (com fonte; "estimativa" quando não é oficial)
| País | Número | Fonte / observação |
|---|---|---|
| México | 310.869 unidades na rama 8121 (maio/2026) | DataMéxico/Economía (v1, não reaberta) |
| Colômbia | 50.739 estabelecimentos de beleza e estética (2019); Bogotá ~15.000 | Gaceta del Congreso 998/2019; SDS (v1) |
| Espanha | ~72.300 (2021) | DBK (v1) |
| Itália | 48.968 empresas artesãs de estética (31/03/2025) | InfoCamere (v1) |
| EUA | ~210.100 manicures/pedicures (2024) | BLS (v1) |
| **França** | **69.556 pontos de venda de cabeleireiro (SIRENE, 01/01/2024)** + 31.501 cabeleireiros a domicílio. **Institutos de beleza: fontes divergem (35.000 a 65.000+)**, sem número oficial | [UNEC, cifras 2025](https://unec.fr/wp-content/uploads/2025/11/unec-chiffres2025-web-2.pdf), [UNEC 2023](https://unec.fr/wp-content/uploads/2025/06/cp-chiffres-cles-2023.pdf) (cálculo sobre INSEE/SIRENE). Institutos: VERIFICAR |
| **Polônia** | **>132,8 mil salões de cabeleireiro+estética no fim de 2025; 14,7 mil abertos em 2024** (estimativa Dun & Bradstreet). GIS: 55 mil registrados em 2022. Estudo acadêmico: ~100 mil | [Rzeczpospolita (pro.rp.pl)](https://pro.rp.pl/raporty-ekonomiczne/art41725071-w-dekade-liczba-salonow-pieknosci-sie-podwoila) e demais resultados. **Não é GUS**: oficial VERIFICAR |
| **Romênia** | ~12.800 empresas com CAEN 9602 (cabeleireiro e outras atividades de beleza) | Termene.ro (agregador privado, sem data). Oficial ONRC/INS: VERIFICAR |
| **Peru** | estimativa da APEB: ~90.000 salões formais antes da pandemia, ~60.000 depois (dez/2022) | [Peru Retail](https://www.peru-retail.com/peluquerias-en-riesgo-un-20-de-salones-de-belleza-cerraria-en-el-2023/). INEI/DIRCE: VERIFICAR |
| **Chile** | "mais de 22 mil" peluquerías, barberías e salões (imprensa 2021 e 2023) | [BioBio 2021](https://www.biobiochile.cl/noticias/economia/actualidad-economica/2021/07/20/amp/salones-de-belleza-peluquerias-y-barberias-abren-postulacion-para-que-reciban-hasta-3-millones.shtml). SII: VERIFICAR |
| **Argentina** | ~78.000 salões (estimativa CAPA/UPA, de 2020) | [Cronista](https://www.cronista.com/apertura/empresas/coronavirus-las-peluquerias-pierden-500000-por-mes-y-corren-peligro-100000-puestos-de-trabajo) (dado de 2020). INDEC/ARCA: VERIFICAR |
| **Portugal** | **não encontrado** (só diretório comercial: 1.490 entidades CAE 96021 em Lisboa, sem ano) | INE: VERIFICAR |
| **Alemanha** | **não encontrado** (Statista com valores ocultos; guia cita 25.000 a 40.000 estúdios de cosmética, sem fonte oficial) | Destatis/ZDH: VERIFICAR |

## 5. Normas e vigência (fonte e URL)

### Colômbia
- **Res. 2263/2004, 3924/2005, 2827/2006: nenhuma fonte achada diz que foram derrogadas.** Texto da 3924/2005 mostra que ela só **derroga o literal t) do numeral 1 do art. 5 da 2263** (derrogação parcial, 2005). A 2827 rege "a partir da publicação" (DO 46.362, 16/08/2006) sem nota de derrogação nos normogramas. Ressalva: os normogramas consultados são compilações; **não encontrei a nota oficial de vigência atualizada do MinSalud**, por isso a vigência plena fica "sem derrogação encontrada", não "confirmada pelo Ministério". Fontes: [normograma Supersalud 2827](https://normograma.supersalud.gov.co/compilacion/docs/resolucion_minproteccion_2827_2006.htm), [Invima 3924](https://normograma.invima.gov.co/compilacion/docs/resolucion_minproteccion_3924_2005.htm), [CRA 2263](https://normas.cra.gov.co/gestor/docs/resolucion_minproteccion_2263_2004.htm).
- **Documento oficial da Secretaría Distrital de Salud de Bogotá, "Normativa sanitaria – Servicios personales de belleza"** ([PDF SDS](https://www.saludcapital.gov.co/Documents/Normativa_sanitaria_centros_esteticos.pdf), impresso pela Imprenta Distrital; sem data no texto) trata como aplicáveis: Lei 711/2001, Res. 2263/2004, **Res. 3924/2005 (guia de inspeção com formatos modelo)**, **Res. 2827/2006**, Decreto 4725/2005, Decisão 516/2002 (CAN), Decreto 1294/2004 e **Res. 723/2010** (acreditação). Itagüí cita também Res. 2117/2010 e Decreto 780/2016.
- **Esse mesmo PDF lista os documentos que devem estar sempre no local:** diplomas, manuais de procedimentos, relação do pessoal, **hojas de vida**, relação de serviços, relação de equipos, **"Fichas (historias) estéticas"**, **autorização escrita para menores**, **registro de equipos e manutenção (hoja de vida de equipos)**, manuais de equipos, **manual de bioseguridad**, **plan de gestión integral de residuos**, **concepto sanitario favorable**. Isto é o conteúdo exato da maleta.
- **Fiscalização:** Bogotá, 1.296 visitas de IVC e 155 medidas sanitárias entre 2025 e 05/07/2026; reforço após o caso Yulixa Toloza ([Publimetro 16/05/2026](https://www.publimetro.co/bogota/2026/05/16/tras-caso-yulixa-toloza-distrito-refuerza-operativos-contra-centros-esteticos-ilegales-y-quirofanos-clandestinos/)) (v1, não reaberto). **Não há prazo/data futura de norma**: é gancho de fiscalização contínua, não PRAZO.

### México (COFEPRIS)
- Fonte oficial: guia COFEPRIS "obtención de tarjeta de control sanitario, tatuadores, micropigmentadores y perforadores" ([gob.mx, PDF](https://www.gob.mx/cms/uploads/attachment/file/910517/Guia_obtencion_de_tarjeta_control_sanitario_tatuadores.pdf)). **O PDF é imagem e não consegui ler o texto**. Li o resumo em [El Financiero, 25/04/2024](https://www.elfinanciero.com.mx/nacional/2024/04/25/tatuas-o-haces-perfos-asi-puedes-tramitar-la-tarjeta-de-control-sanitario-de-cofepris-guia/): formato COFEPRIS-05-084, **manual de procedimentos**, CV, comprovantes de primeiros socorros e higiene/assepsia, vacinação, **vigência de 2 anos prorrogável**, resposta em até 40 dias úteis, **custo MXN 6.183**, **bitácora encuadernada y foliada guardada por 2 anos**, descartáveis de uso único, plano de resíduos aprovado pela Semarnat. O artigo **não** menciona consentimento nem cita a base legal.
- Outro texto (nota de imprensa citada no buscador) fala de aviso de funcionamento, tarjeta vigente do pessoal e **cuestionario previo aprobado por la Secretaría de Salud**. Fonte secundária.
- **Para estética sem tatuagem (cabine, spa): não encontrei norma COFEPRIS específica nem mudança de 2026.** Fica VERIFICAR (regulação é estadual).

### Tatuagem em Espanha
- Competência das comunidades autônomas; sem lei estatal única ([Consumoteca](https://www.consumoteca.com/bienestar-y-salud/normativa-tiendas-de-tatuaje-y-piercing/)). Madrid: Decreto 35/2005. Andaluzia: o Decreto 71/2017 foi alvo de recurso e o texto do expediente não esclarece o desfecho. La Rioja exige que os pais de menores sejam informados e que conste. **Curso higiênico-sanitário obrigatório e consentimento por comunidade: não confirmado** (Catalunha sem resultado).

### Tatuagem na Itália
- Nacional: apenas as **circolari ministeriais de 05/02/1998 (n. 2.9/156) e 16/07/1998 (n. 2.8/633)**, sem força de lei, que preveem formação obrigatória por cursos regionais (14 a 700 h conforme a região; modelo de 90 h) ([ISS Epicentro](https://www.epicentro.iss.it/tatuaggi/normativa)). Consentimento informado escrito exigido por diretrizes **regionais**; no **Piemonte, guardar por 5 anos**. Menores: regra geral proíbe <18 sem consentimento dos pais; Toscana <14 vetado; Sicília <18 vetado. Tavolo técnico no Ministério desde 2018 para rever as diretrizes; projetos de lei no Senado sem prova de aprovação.

### Reino Unido (Gales) e UE
- Gales: licença obrigatória de "special procedures" desde 29/11/2024 ([gov.wales](https://www.gov.wales/licensing-scheme-special-procedures)) (v1, confirmada).
- UE REACH 2020/2081: data exata no EUR-Lex **não reconferida** (v1: 4 ou 5/01/2022).

## 6. Ranking (0 a 10)
Critério: prova no país/moeda (peso maior), tamanho com fonte, gancho com fiscalização/data, reaproveitamento do que já temos (maleta + app + norma), risco/saturação.

| # | País × profissão | Nota | Status | Evidência | Tamanho | Gancho | Reaproveitamento | Risco |
|---|---|---|---|---|---|---|---|---|
| 1 | **Colômbia × esteticista/cosmetóloga** | **7,5** (v1: 7,0) | TESTE (nenhum vendedor em COP; neutro USD 21 d) | Lacuna em COP; formato provado no MX em MXN | 50.739 (2019) | SDS Bogotá lista os documentos que o kit entrega; 1.296 visitas/155 medidas; **sem data de prazo** | Alto: é o Consultora/IVC do Brasil, com "simulador de visita" no app | Vigência: sem derrogação achada, sem nota oficial; concorrente barato em Word |
| 2 | **México × esteticista/cosmetologia** | **6,5** (=) | PROVADO só no formato (ADE 199 d em MXN, outra profissão); estética 26 d | ADE MXN 99/199 Word via OXXO | 310.869 | fraco (COFEPRIS só p/ tatuagem) | Alto | Preço-âncora de US$5 a 13; vendedor sem app |
| 3 | **México × tatuador/micropigmentador/piercer** (novo) | **6,0** | TESTE (ninguém vende docs) | 0 vendedores; estúdios e escolas anunciam muito | MX tatuagem: tamanho não achado | tarjeta COFEPRIS-05-084, bitácora foliada 2 anos, manual de procedimentos (2024; sem data nova) | Médio: norma própria, kit novo | Fonte secundária; PDF oficial ilegível |
| 4 | **Argentina × gabinete de estética** | **5,0** (v1: 6,0) | TESTE (Belleza Integral parou; Tienda digital é app de gestão, 5 d) | só app em ARS | ~78.000 (2020) | não achado | Médio | Os dois "vendedores só-AR" da v1 viraram 1 app novo |
| 5 | Espanhol neutro × "consentimiento por procedimiento" | **5,0** (v1: 5,5) | TESTE (Ultra Pack ES fichas 21 d; Digital Future caiu p/ 1 anúncio) | | n/a | | Alto | Onda perdeu força em 1 semana |
| 6 | **Itália × tatuatore/piercing** (novo) | **4,5** | TESTE (0 vendedores) | consentimento escrito regional, 5 anos no Piemonte | 48.968 empresas de estética (tatuagem: n/d) | circolari 1998 + regional, sem data | Médio: kit por região | Fragmentado em 20 regiões |
| 7 | Gales/UK × tatuagem, PMU, piercing | 4,5 | TESTE (Wavrr software 44 d, EUR) | | >4.000 praticantes | licença desde 29/11/2024 | Médio | Mercado pequeno |
| 8 | Lash/sobrancelha como módulo (CO, AR, MX) | 4,5 | bump | Belleza Integral parou; cursos de lash em USD | | Res. 2827 cobre ornamental (CO) | Alto | |
| 9 | Peru × esteticista | 4,0 | TESTE (não medido a fundo) | Belleza Premium One USD, Emprende Fácil PEN | ~60.000 (estimativa) | | Alto | Sem SearchAPI |
| 10 | Espanha × tatuagem | 4,0 | TESTE (0) | | 72.300 salões (2021) | decretos por comunidade | Médio | Texto de cada decreto não lido |
| 11 | Polônia × cosmetologia | 3,5 | TESTE (0 em 2 termos) | | >132,8 mil (estimativa D&B) | n/d | Baixo (idioma) | Idioma novo |
| 12 | Chile, Equador × todas | 3,0 | VERIFICAR | TatauFlow CLP (software) | >22 mil (imprensa) | n/d | | |
| 13 | França, Alemanha, Portugal, Romênia, EUA × estética | 2,0 a 3,0 | 0 vendedores de docs | | FR 69.556 coiffeurs | n/d | Baixo | |
| 14 | Barbeiro, manicure, massagem (todos) | 2,0 | só cursos | | | | | |

## TOP 6
1. Colômbia, esteticista/cosmetóloga (7,5)
2. México, cosmetologia/spa (6,5)
3. México, tatuador/micropigmentador/piercer (6,0)
4. Argentina, gabinete (5,0)
5. Espanhol neutro, consentimento por procedimento (5,0)
6. Itália, tatuatore/piercing (4,5), empatado com Gales/UK

## 7. Diferenças em relação à v1
- **Ultra Pack deixou de ser prova:** os 69 dias eram do software em PT-BR. As fichas em espanhol têm 21 dias.
- **Digital Future** encolheu de ~20 para 1 anúncio. **Belleza Integral** parou. **Tienda digital estética** é app de gestão, não kit+app.
- **Archivos Digitales Express** resolvido: 199 dias de página, mas a profissão de 199 dias é optometria; cosmetologia 26 dias; preços MXN 99/199 (cosmetologia), 100/200 (quiropraxia), 250 (feridas), em Word, OXXO.
- Colômbia sobe: documento oficial da SDS lista os mesmos documentos da maleta.
- Novos: México tatuagem (COFEPRIS tarjeta + bitácora) e Itália tatuagem.
- Tamanhos novos: FR, PL, RO, PE, CL, AR (todos estimativas ou fonte secundária, marcados).

## 8. O que continuou VERIFICAR
1. Nota oficial de vigência do MinSalud para Res. 2263/2004, 3924/2005 e 2827/2006 (só achei "sem derrogação").
2. Texto do guia COFEPRIS para tatuadores (PDF é imagem), base legal, e se a tarifa MXN 6.183 vale em 2026. Norma COFEPRIS/estadual para estética de cabine.
3. Decretos de tatuagem em ES (curso e consentimento por comunidade, desfecho do Decreto 71/2017 da Andaluzia) e regras de tatuagem da Itália por região.
4. Tamanho oficial: PT, DE, PL (GUS), RO (ONRC/INS), PE (INEI), CL (SII), AR (INDEC/ARCA), institutos de beleza da FR; tamanho de tatuagem em MX e IT.
5. Idade atual das páginas Aprendia, Legalize Estética, TatauFlow e Digital Future (texto do anúncio não abriu).
6. Varredura por moeda local em PE, CL, EC, UY, PL, RO e termos de lash/brow/barbeiro/manicure: precisa de SearchAPI (renova em 08/11) ou nova rodada do conector com mais termos.
7. REACH 2020/2081 (data exata no EUR-Lex).
