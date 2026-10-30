# Concorrentes que vendem sem anúncio: Etsy e Hotmart (30/10/2026)

## 0. Limites desta rodada (ler primeiro)
- **Cobertura parcial.** Cobri duas vitrines orgânicas com dado de volume: **Etsy** (buscas em inglês, 24 profissões) e **Hotmart marketplace** (PT-BR e ES, ~10 buscas). **Não cobri** SEO de sites próprios por país, Instagram, TikTok, YouTube nem e-mail (sem ferramenta confiável nesta rodada; WebSearch só devolve normas e templates gratuitos).
- **O Etsy bloqueou o navegador** (HTTP 403, tela anti-robô) depois de ~40 buscas. Parei, não tentei contornar. Os 12 grupos de profissões da segunda leva (esteticista, tattoo, quiropraxia, doula, corretor, contador, advogado, HACCP, vistoria, fotógrafo, professor particular, limpeza, psicólogo escolar, assistente social, ABA, farmácia, optometria, med spa, enfermagem, home care) **não rodaram**: ficam como pendência.
- **Volume aparente:** no Etsy usei **nº de avaliações da LOJA inteira** (proxy: aproximadamente 1 avaliação a cada 5 a 15 vendas, não verificado). A Etsy não mostra vendas por anúncio. Preços estão em **BRL** porque o Etsy abriu em "Etsy Brasil" (converte do preço original).
- **Hotmart:** nota e nº de avaliações do produto; vendas reais não aparecem. Várias páginas de produto não renderizam preço/avaliação via WebFetch.
- **Não conferi se esses vendedores anunciam** na Biblioteca (SearchAPI sem crédito; conector Meta não foi usado nesta rodada). "Sem anúncio" aqui significa "não os encontrei por anúncio, só pela vitrine": **VERIFICAR** cada um antes de tratar como concorrente orgânico puro.
- Resultados do Etsy em português/outros idiomas voltam traduzidos e misturados com anúncios em inglês; não dá para provar idioma original do anúncio.

## 1. Ranking de brechas (0 a 10)
Nota = quanto vale entrar agora, olhando o que as vitrines orgânicas mostram. Não é prova de demanda (régua do projeto: PROVADO só com anúncio 30+ dias).

| # | Brecha | Nota | Por quê (evidência desta rodada) | Status |
|---|---|---|---|---|
| 1 | **Kit de documentos por profissão em IT, DE, FR, PL (pacote Word pago, nativo)** | 8 | 5 buscas em italiano, alemão, francês, polonês e PT-PT por "pacote/kit Word editável" voltaram só modelos grátis de ordens profissionais, form-builders (Jotform) e software; nenhum vendedor nativo de kit pago. Em PT-PT os resultados foram só kits do Brasil (CRO/CPF). Os vendedores que já conhecemos nesses países (Kontrola Sanepidu PL, Protocollo Zero Sanzioni IT, família impultienda) vêm de anúncio, não de SEO. Ou seja, via orgânica vazia; o concorrente é anúncio. | BRECHA orgânica (PROVADO por anúncio nos países já mapeados) |
| 2 | **Dentista ES-LATAM (MX, CO, CL, PE) com app** | 7 | Hotmart ES: "Kit Formatos para Odontólogos" (Mili Garcia, BRL 42, sem avaliações), "Cofepris para Odontólogos / Consentimiento Informado" (BRL 472), "Formatos Gráficos para Odontólogos Azul" (BRL 167). Todos sem nota/avaliação visível = pouca tração. Nenhum com app. | TESTE (concorrente fraco) |
| 3 | **Nutricionista BR (kit de documentos + app)** | 7 | Hotmart PT: busca por "kit documentos nutricionista" e "anamnese nutricionista modelos editáveis" não trouxe nenhum kit de documentos de nutricionista; só "Pack Canva para Nutricionista 5 em 1" (BRL 17,90, 28 avaliações, é arte para Instagram). No Etsy o nicho tem vendedores de formulário (PrintyPin 1.806 avaliações, PerennialTemplatesCo 926, EnCDesigns 397, ~BRL 17 a 53), prova de demanda em inglês. | BRECHA no Hotmart BR; PROVADO fora (Etsy EN) |
| 4 | **Veterinário BR e ES (kit de documentos)** | 6 | Hotmart PT: só cursos de auxiliar veterinário; nenhum kit de documentos. No Etsy, vet forms existem mas com avaliações baixas (QuickBizDocs 163, demais 0 a 5). Demanda fraca no orgânico. | BRECHA com demanda incerta |
| 5 | **Esteticista / vigilância sanitária BR** | 6 | Hotmart PT: só arte para Stories e "Plataforma Regularize Já" (iREC, R$ 2.987, 95 avaliações, nota 4,9; produto caro de regularização, não kit). Já existe "Documentos para Regularização Sanitária, Área da Estética" (kit editável Word, achado por WebSearch). | TESTE |
| 6 | **Fonoaudiólogo / terapeuta ocupacional (documentação)** | 5 | Etsy EN tem demanda: AdultSpeechTherapy 1.082 avaliações (BRL 141), WiseSpreadsheetsShop 836 (BRL 29, multi-profissão, cartão barato), DigitalWhale1 340, SoulfulSystems 306. Fora do inglês, não achei nada nesta rodada. Fono é nosso nicho já construído (Fono Infantil). | PROVADO em EN; BRECHA em outras línguas (VERIFICAR) |
| 7 | **Personal trainer, massoterapia, creche domiciliar (kits de formulários)** | 4 | Etsy EN mostra demanda alta e preço baixo: TheTemplateShopAndCo (massagem) 2.131 avaliações a ~BRL 25; HumbleArtPrint 1.054 a ~BRL 13; StellarTemplateCo (home daycare) 1.177 a ~BRL 57; TuesdayTemplatesCo (PT/massagem/personal) 1.101 a ~BRL 17-28. Mercado de ticket mínimo e saturado em EN: quem é pequeno tem 0 a 5 avaliações. Pouco LTV. | SATURADO em EN |

**Saturados (não entrar sem diferencial):** psicólogo BR (ElloCursos Psicologia 3 kits R$ 67 com 178/101/80 avaliações; Adriana Brixner R$ 77 com 85; Alex Camargo R$ 29; JAQUELINE EWALD R$ 58,62), fisioterapeuta BR (pelo menos 12 vendedores individuais de "Kit de Documentos para Fisioterapeutas" entre R$ 15,90 e R$ 75, quase todos sem avaliação visível: guerra de preço), dentista BR (CliniPack, Kit Clínica Geral, Kit Fichas Odontológicas, 6 variações "Kit de Documentos Cirurgião Dentista" por paleta de cor da Izabela Ferreira). Dentista e terapeuta em inglês também (dezenas de lojas, de BRL 8 a BRL 395).

## 2. Mapa por vitrine

### 2.1 Etsy, dentista (inglês; busca "dental office forms template", 70 listagens)
- Vendedores de formulário com tração: **PrintyPin** (1.806 avaliações; consentimento odontológico BRL 39), **PrettyLegalForms** (711; manual do funcionário da clínica BRL 143), **QuickBizDocs** (163; pacotes operacionais "Daily Operations" até BRL 366 a 394, ancoragem alta, vende por pacotes de módulo, Word+PDF, A4+US Letter), **ScriblInk** (104; pacote Canva BRL 45), **BrightSideDigitalCo** (65; BRL 30 a 67), **TradeDocsStudio** (kit 12 formulários BRL 169), **ModernDentistry** (BRL 135).
- Padrão: milhares de listagens baratas (BRL 8 a 70) de formulário solto; os que passam de BRL 100 são pacotes de operação/manual. **Nenhum com app.** Quase todo conteúdo é HIPAA/EUA.
- Leitura: não há ataque a fazer em EN; a brecha é o mesmo produto em idioma/norma local.

### 2.2 Etsy, outras profissões (inglês)
| Profissão | Loja (avaliações da loja) | Faixa de preço | Obs. |
|---|---|---|---|
| Massoterapia | TheTemplateShopAndCo (2.131); HumbleArtPrint (1.054); EnCDesignsCA (397); OpenConceptStudio (275) | BRL 13 a 56 | formulários de consentimento/anamnese |
| Fisioterapia | TuesdayTemplatesCo (1.101); CaseManagersConnect (237); QuickBizDocs (163) | BRL 22 a 366 | |
| Fonoaudiologia | AdultSpeechTherapy (1.082); WiseSpreadsheetsShop (836); FarBeyondNutrition (62) | BRL 22 a 197 | anotações SOAP, metas |
| Terapia ocupacional | WiseSpreadsheetsShop (836); DigitalWhale1 (340); SoulfulSystems (306) | BRL 19 a 141 | |
| Nutrição | PrintyPin (1.806); PerennialTemplatesCo (926); WiseSpreadsheetsShop (836); EnCDesignsCA (397); digitalinsight (264, BRL 9) | BRL 9 a 53 | |
| Veterinária | QuickBizDocs (163, manual BRL 107); resto 0 a 5 | BRL 26 a 146 | nicho fraco |
| Personal trainer | TuesdayTemplatesCo (1.101); trainertoolbox (267); PracticalSheetsCo (134) | BRL 17 a 253 | |
| Creche domiciliar | StellarTemplateCo (1.177); WorkflowAtlasStudio (11) | BRL 33 a 90 | |
| Terapeuta/psicólogo | CounsellorCronan (19.687, mas é guia de estudo, não kit); SelfairyShop (2.425, Instagram); PerennialTemplatesCo (926); WiseSpreadsheetsShop (836); GroundedPracticeCo | BRL 24 a 225 | pacotes GDPR para UE existem em anúncios isolados |
- Nota: lojas multi-profissão (TuesdayTemplatesCo, WiseSpreadsheetsShop, PerennialTemplatesCo, PrintyPin) são o modelo "um vendedor, várias profissões": confirma que o kit por profissão pode ser a mesma estrutura replicada. Nenhuma tem app.

### 2.3 Hotmart marketplace, BR (PT)
- **Psicólogo:** ElloCursos Psicologia: Kit de Documentos Neuropsicopedagógicos (4,8 / 178 avaliações / R$ 67), Psicopedagógicos (4,6 / 101 / R$ 67), Psicológicos (4,3 / 80 / R$ 67); Adriana Brixner "Modelo de documentos psicológicos" (4,5 / 85 / R$ 77); Alex Camargo "Kit Documentos Premium Psicólogo" (R$ 29); JAQUELINE EWALD (R$ 58,62); "Consulta en Orden" (R$ 58,62, versão ES, João Paulo de Lima).
- **Educação especial/psicopedagogia:** J.A BERTOTTO é o maior em volume aparente: KIT SÓ ESCOLA AUTISMO 4,5 / 316 / R$ 37; KIT ESTIMULAÇÃO COGNITIVA 4,3 / 221 / R$ 34,90; KIT SÓ ESCOLA 4,4 / 243 / R$ 47; KIT EDUCAÇÃO ESPECIAL 4,6 / 130 / R$ 57; KIT DISLEXIA 4,6 / 91 / R$ 27,50; COMUNICAÇÃO ALTERNATIVA 4,6 / 76 / R$ 70. Janaina Calaça Kovaciu "Kit Habilidades Cognitivas" 4,6 / 197 / R$ 47. Mostra que kit infantil/educação tem muito mais tração que kit de documento clínico; anunciam? **VERIFICAR**.
- **Fisioterapeuta:** Guacira Schwambach R$ 49,90; Fisio Manfredini R$ 67,90; INSPFISO R$ 39,90; Letícia Sander R$ 15,90; Thais Avila R$ 29,90; Mailson Ventura R$ 67; Rafaela Menezes R$ 39,90; S&E R$ 75; Thiago Silveira R$ 59,99; "Pacote de Documentos Essenciais de Fisioterapia" (Gabriel Miranda 4,4 / 26 / R$ 21,50); Alex Camargo R$ 29; FISOS DOC R$ 65. Fragmentado, sem líder, sem avaliações.
- **Dentista:** CliniPack (sem preço visível), Kit Clínica Geral, Kit Fichas Odontológicas (anamnese, plano, TCLE, pós-procedimento, "testado por cirurgiã-dentista"), Izabela Araujo de Oliveira Ferreira "Kit de Documentos Cirurgião Dentista" em 6 cores. Nenhum com avaliações visíveis.
- **Regularização sanitária:** iREC "Plataforma Regularize Já" 4,9 / 95 / R$ 2.987 (ticket alto, estética/saúde).
- **Nutricionista, veterinário:** nenhum kit de documentos achado (ver brechas 3 e 4).

### 2.4 Hotmart marketplace, ES-LATAM
- "Maletín Clínico VIP: Pack Todo en Uno" (Caio Sousa; psicopedagogia: guia de testes, 20 modelos de laudo, anamnese, termos legais; Word + PDF), "Kit de recursos Psicoterapéuticos" (Psic. Denisse Peñafiel; consentimento informado, ficha clínica, notas, atividades). Preço não carregou: VERIFICAR.
- "Kit Documentos para Psicólogos – Español" (Alex Camargo, BRL 34,94), "Kit de Documentos para Psicólogos – Editables en Word" (BRL 53,28), "Consulta en Orden" (BRL 58,62), "Recetario y Formatos Imprimibles para Consultorio Médico" (BRL 40,85), "KIT FORMATOS PARA ODONTÓLOGOS" (Mili Garcia, BRL 42), "Cofepris Para Odontólogos" (BRL 472).
- Leitura: preços de BRL 35 a 60 (≈ US$ 7 a 11) e sem avaliações visíveis: concorrentes presentes mas fracos. Os vendedores fortes em ES com anúncio já estão nos relatórios `2 - ES/pesquisas` (Qualitiva, Recursos Legales PRO, Consultorio al Día, etc.).

### 2.5 Europa e Polônia (orgânico, WebSearch)
- **Itália (dentista):** só modelos grátis de ordens e associações (AIO Roma, ANOE, Ordem de Brescia/Biella) e softwares (DottAI, FormatDental). Nenhum kit pago nativo encontrado. Concorrente pago real vem de anúncios (família impultienda €19,99).
- **Alemanha (psicoterapeuta):** só modelos grátis (KBV, Psychotherapeutenkammer Berlin, BPtK) e um pacote EUA/inglês (AT Health, 58 formulários Word). Nenhum pacote nativo pago encontrado. Nota: Alemanha não está como prioridade nas filas anteriores; vale rever (VERIFICAR demanda por anúncio).
- **França (kinésithérapeute):** só modelos grátis da Ordem (formulário de consentimento em PDF), um pacote RGPD de freelancer (ComeUp, 11 documentos) e marketplace jurídico (dossierjuridique.fr, consentimento Word/PDF). Nenhum kit de documentos de kiné encontrado.
- **Portugal (dentista):** a busca devolve só kits do Brasil (CliniPack, Kit Clínica Geral, Kit Fichas Odontológicas) com CRO/CPF; nada para OMD/NIF/Lei 58/2019. Brecha clara para versão PT-PT.
- **Polônia (psicólogo):** só materiais públicos (KWP Radom), modelos genéricos RODO (firmove.pl) e livro de 80 modelos (ebookpoint). Sem kit pago por profissão no orgânico; a loja polonesa conhecida (Kontrola Sanepidu, sklep-haccp.pl) é de anúncio.

## 3. Diferenças em relação ao que já sabíamos
- Os vendedores de EN no Etsy vendem **formulário solto barato** (BRL 8 a 70) e raramente app; pacotes grandes de operação chegam a BRL 395. Confirma que nosso formato (kit + app, €19 a €27) tem espaço de preço acima do solto e abaixo dos pacotes.
- **Hotmart BR** é terreno fragmentado e sem avaliações nas profissões de saúde (fisio, dentista); só psicólogo/psicopedagogia/educação especial têm líderes (ElloCursos, Bertotto).
- **Nutricionista BR e veterinário BR** aparecem como lacunas na vitrine, o que não aparecia nos relatórios anteriores (a conferir contra anúncio).

## 4. VERIFICAR (lista final)
1. Se ElloCursos Psicologia, J.A Bertotto, Alex Camargo, Adriana Brixner, Kovaciu anunciam hoje na Biblioteca (BR) e há quantos dias: se não, são o concorrente orgânico puro do psicólogo BR.
2. Preço, avaliações e conteúdo reais de "Maletín Clínico VIP", "Kit de recursos Psicoterapéuticos", "Kit Formatos para Odontólogos" (Mili Garcia), "Cofepris Para Odontólogos", "Recetario y Formatos Imprimibles" (página da Hotmart não renderizou preço).
3. Confirmar com busca direta no Hotmart (ES e PT) e Kiwify/Eduzz se existe kit de **nutricionista**, **veterinário** e **esteticista** BR (a busca do marketplace é fraca; ausência não é prova).
4. Rodar as 20 buscas do Etsy que ficaram pendentes (esteticista, tattoo, quiropraxia, doula, corretor, contador, advogado, HACCP, vistoria, fotógrafo, professor, limpeza, psicólogo escolar, assistente social, ABA, farmácia, optometria, med spa, enfermagem, home care) quando o Etsy liberar ou por outro IP; usar avaliações da loja como proxy.
5. SEO e redes: ainda faltam por país as buscas de Google (nome de profissão + "modelo/kit/pack") com abertura das lojas próprias, e contagem de seguidores e frequência de postagem de perfis de Instagram/TikTok/YouTube que vendem kit por link na bio.
6. Alemanha como mercado de psicoterapeuta/kine: sem anúncio de vendedor conhecido nos relatórios; checar Biblioteca DE.
7. Portugal PT-PT dentista/psicólogo: checar Biblioteca PT (EUR) antes de classificar como BRECHA.
