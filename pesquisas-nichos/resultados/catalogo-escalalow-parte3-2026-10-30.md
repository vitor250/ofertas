# Catálogo EscalaLow, parte 3 (índices 106 a 158) — brechas por país

Data de referência: 30/10/2026. Fonte: `dados/escalalow-ofertas-validadas.json` (213 ofertas BR validadas), índices 106–158 (53 ofertas).

## Avisos de método (ler primeiro)
- A versão anterior (v1 de 29/10) e os arquivos do Desktop NÃO estavam acessíveis neste ambiente; este relatório parte do zero, usando o próprio JSON e as notas `fila-ofertas.md`, `pesquisa-europa.md` e `meta-varredura-low-ticket.md`.
- SearchAPI NÃO disponível (sem chave aqui e sem crédito até 08/11). Toda a medição de anúncios foi feita pelo conector Meta (`ads_library_search`, só anúncios ATIVOS).
- DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`). Nº de anúncios = `estimated_total_count` da busca por página.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.

## 1. Agrupamento das 53 ofertas em conceitos
(em construção)

## 2. Tabela completa (todas as ofertas 106–158)
(em construção)

## 3. Resultado por país dos conceitos pesquisados
(em construção)

## 4. Aprofundamento das brechas fortes (página de vendas, mercado, gancho legal)
(em construção)

## 5. Ranking 0–10 das brechas
(em construção)

## 6. Lista final de VERIFICAR
(em construção)

---
## ANEXO A — Diário de medições (conector Meta, 30/10/2026, só anúncios ativos)
Observação de método: a busca do conector ordena do anúncio mais novo para o mais velho e devolve no máximo 50; em termos com muitos resultados, vendedores antigos podem ficar fora da janela. Por isso usei frase exata (entre aspas) e termos de infoproduto ("curso", "PDF", "plantillas", "kit"), e medi DIAS REAIS por `page_ids` só nos vendedores relevantes. WebFetch das páginas de vendas foi BLOQUEADO pela rede do container (lovable.app, inovaba.com.br, alaincarboni.com etc. não resolvem; hotmart/kiwify com 403 no proxy). Preço e conteúdo vêm do texto do anúncio no JSON; o que não deu para abrir fica VERIFICAR.

### A1. Maleta do instalador de segurança eletrônica (153)
- ES-LATAM (MX/CO/AR/CL/PE), termo "instalación de cámaras de seguridad": 2.207 anúncios, quase todos de prestadores de serviço/lojas (ruído). Frase exata "instalador de cámaras" + PDF: 15 anúncios.
  - Iad Cursos Online (page 101583268685680, ARS): 13 ativos, mais antigo há ~93 dias (curso de eletricidade); anúncio específico "Aprendé Cámaras de Seguridad" há ~75 dias; "Convertite en instalador de CCTV" há ~44 dias. CURSO, não kit de documentos. PROVADO (AR, curso).
  - Academia Online PRO (114590668253097, USD neutro): 6 ativos, ~5 dias (guia de instalação/eletricidade). TESTE.
  - Bien laburado (1271362576071315, USD): 5 ativos, ~2 dias. TESTE.
  - CMDigital (962417550298160, USD): "Mega pack instalador de redes WiFi y cableado", ~17 dias. TESTE.
- ES (Espanha), "curso instalador cámaras": 0.
- EN (US/GB/AU/CA), "CCTV installer": 47 anúncios, todos prestadores de serviço; exceção InstallerDocs (1406430925887218, GBP), 1 anúncio, 0 dia (documentação para instaladores, VERIFICAR o que é).
- IT "corso videosorveglianza": 7, todos empresas de instalação/imobiliárias. Ninguém vende kit/curso. BRECHA.
- FR "formation vidéosurveillance": 2 (MaxioM, ~8 dias, parece DIY; SurveyCam, empresa local). BRECHA.
- PT "curso CCTV": 0 relevante. BRECHA.
- Leitura: nenhum vendedor de "maleta" (documentos + checklists) para instalador em nenhum país; em AR existe CURSO provado (Iad, ~75 d no anúncio de câmeras). Gancho legal possível na Europa: cartaz/aviso obrigatório de zona videovigiada e informação RGPD (ES LOPDGDD art. 22; IT GDPR + art. 4 Statuto dei Lavoratori para câmeras com funcionários; PT Lei 58/2019) → VERIFICAR com fonte oficial antes de usar.

### A2. Programas ABA / VB-MAPP (130) e plataforma IA psico/neuropsicopedagogia (120)
- Busca "VB-MAPP" em 15 países (LATAM, ES, EN, IT, PT, FR, DE, PL): 25 anúncios.
  - FR: **ABA Online** (page 1850476768389167, EUR): 44 ativos, mais antigo ~148 dias ("Mesurer avant d'intervenir : 8 grilles à télécharger"); vende grilles, livrets VB-MAPP, contrato, formações e app (Google Play). PROVADO FR (documentos + app + formação). Concorrente direto do modelo kit + app.
  - US: ABA Tools (108617997275390, USD) ~133 dias, 10+ anúncios; The Autism Helper "VB-MAPP Assessment Kit" ~101 dias. PROVADO EN-US (mercado TPT saturado).
  - IT: só cursos (Intandem Formazione "Corso VB-MAPP" ~14 d; Iescum; ICOTEA; Centro APP; ComportaMente). Nenhum kit low ticket. BRECHA IT para kit de programas/registros.
- "programas ABA" (LATAM + ES): 24 anúncios.
  - Conecta ABA (1467060063146717, USD neutro): 3 ativos, ~7 dias ("58 programas ABA listos para aplicar", "Programas ABA con registro incluido"). TESTE.
  - Mini Logros (1393263263878199, PEN): 3 ativos, ~1 dia ("Abres, aplicas y registras"). TESTE Peru.
  - PsicoKids and Teens (COP): diplomados ABA/TEA (curso). Abaedu Latam (BRL, curso de aplicador).
- "terapia ABA" ES+PT: nada de kit (NeuroIdea COP vazando). BRECHA ES e PT.
- PL "ABA autyzm materiały": **Pro-Edukacja.pl** (840454552492924, PLN) "PAKIET AUTYZM 2+2 GRATIS! Tylko 79 zł" com anúncio ativo há ~280 dias. PROVADO PL (pacote de formações/materiais sobre autismo para professores/terapeutas, 79 zł).
- Leitura: ABA é o único conceito desta faixa com vendedor de "documentos + app" provado fora do Brasil (FR, ABA Online, 148 d). Na LATAM há dois testes de "programas ABA listos" com 7 dias ou menos (USD e PEN), sinal de que a onda está começando. IT/ES/PT: só cursos, ninguém com kit.

### A3. Biblioteca de projetos ambientais (134)
- ES-LATAM+ES "plan de manejo ambiental" modelos: 2 anúncios sem relação. "ingeniero ambiental plantillas": 2 (página genérica de IA, MXN).
- "estudio de impacto ambiental" curso: 16 anúncios, todos de institutos/cursos (ISE-Ambiental PEN, Instituto Mexicano de Ingeniería Industrial MXN, FaunaLab MXN "Guía Integral de Monitoreo… Arrecifes", GeoCaps, Ecoambiental Group PEN). Nenhum pack de modelos low ticket. BRECHA LATAM (demanda existe via cursos; produto de modelos não existe). Europa não pesquisada a fundo: na UE o trabalho ambiental é assinado por técnico habilitado e os modelos variam por região (baixo encaixe).

### A4. Sistema de consultoria pronto (127)
- ES-LATAM+ES "plantillas para consultores propuesta contrato": 0. BRECHA em espanhol.
- EN "consulting templates": 350 anúncios (US/GB/AU/CA), com vendedores de PDF instantâneo (Dan Hart, Business Explained, USD). Mercado EN saturado/PROVADO por volume (dias não medidos).

### A5. Perito judicial (155)
- ES+LATAM "perito judicial": 220 anúncios; maioria cursos/diplomados (Instituto Dasein Meraki MXN "Diplomado Perito en Medicina Forense"), serviços (perito_judicial_edificacion EUR, PsicologosForenses.com ARS), "Guias profesionales - aprendia" (MXN, guias profissionais, VERIFICAR) e Ratio Studio "Guía Práctica de Daños y Perjuicios" (USD, para advogados). Nenhum "guia de marketing do perito" como o BR. TESTE fraco; produto BR é de posicionamento/marketing, pouco ligado a norma.

### A6. Projetoteca de pergolados/toldos (113) e projetos de marcenaria (138, 146, 125, 149)
- ES-LATAM+ES "proyectos de pérgolas": 331 anúncios, quase tudo fabricante/loja. Achado: **Planos y Diseños de Herrería** (page 1197011490158539, MXN), 7 ativos, mais antigo ~13 dias ("MEGA PACK DE PLANOS HERRERÍA Y CARPINTERÍA", "diseños para explorar, cotizar y fabricar"). Mesmo conceito do BR (catálogo para o profissional cotar), para herrero. TESTE MX.
- "planos de carpintería PDF" (LATAM+ES): 144 anúncios; Proyectos Carpinteros (USD, "+150 Proyectos de Carpintería", 10+ criativos novos), Al Interiorismo (USD, "50 planos + 5 regalos"), Metal & Madera (ARS), Elias Joel "Curso Melamina Pro 360 PDF" (ARS), Tienda Digital Perú (PEN). Mercado aquecido/competitivo em espanhol neutro.
- EN "woodworking plans": 714 anúncios; Weekend Woodshop (anunciante em BRL vendendo em inglês, "16,000+ plans"), Woodworking DIY Ideas (CZK), Wood Atlas Plans (EUR), The Backyard Woodworker (AUD), WoodSense, Go4Wood. SATURADO (inclusive por brasileiros).
- Leitura: marcenaria hobby já é oceano vermelho em EN e ES. O ângulo que sobra é o PROFISSIONAL (catálogo para serralheiro/herrero/instalador de toldos cotar no WhatsApp), que só tem 1 teste de 13 dias no México.

### A7. Gerador de apostilas para professores (118, 119)
- ES-LATAM+ES "generador de fichas docentes inteligencia artificial": 0. Ninguém anuncia gerador de apostilas/fichas com IA em espanhol. BRECHA (mas é software; exige produto SaaS).
- IT "schede didattiche pronte da stampare": 8 anúncios, todos recentes e de vendedores com conta em USD (padrão de brasileiro exportando): Attività Premium ("2.500 schede a 7,90 €", ~0 d), Prof di Scienze ("120 schede di scienze", ~1 d), Mondo Infanzia Didattica (~9 d); Edudoro.eu (empresa polonesa, PLN) ~58 dias. A onda BR de fichas prontas já chegou à Itália; gerador com IA ainda não.

### A8. Mapas mentais para concursos (154) e resumo esquematizado de psicologia (133)
- ES "mapas mentales oposiciones": 4 anúncios, só academias (Granapol Formación Policial, Academia Prefortia). Nenhum vendedor low ticket de mapas. BRECHA ES (oposiciones = mercado grande; ver CONSOLIDADO 28/10, nº 1 da Espanha foi simulador de opositores docentes).
- IT "mappe concettuali concorsi": 8; concorsi_essentials (EUR, ~4 d, "essentials" por concurso, ex.: ASMEL Istruttore amministrativo) = TESTE; Quizly (app de quiz); Ivan Lettura Veloce (método de estudo). BRECHA/TESTE IT.

### A9. Planilha de gestão financeira/precificação (157)
- ES-LATAM+ES "planilla excel costos precios negocio": 13. **Eve Uribe** (page 986872747852950, CLP) "Calcula y vende con seguridad"/"Haz rentable tu negocio", anúncios ativos há ~39 dias = PROVADO CL (≥30 d; nº total de anúncios não medido, VERIFICAR). Educateka (USD) ~35 d; Formatos digitales pro (MXN) novo; Kaptia (ARS) negócio de pan dulce.

### A10. Plantas de casas (129)
- ES-LATAM+ES "planos de casas PDF": 28. **Creativo AZ** (page 110852248404371, COP) com anúncios ativos há ~129 dias ("Adquiérelo ahora mismo", produto VERIFICAR); Aprendia: Guías Oficiales (MXN, "planos acotados, medidas por ambiente y metrados", ~13 d); Homtak (MXN, marketplace de casas, ~10 d); Prof Amanda Lacerda (USD, brasileira em espanhol, novo); Tienda Digital Perú (PEN). Mercado ativo em espanhol; produto BR (VGProjetos) é venda de projeto, não kit.

### B1. Papelaria personalizada 2027: calendários, encadernação, caixas (106, 107, 122)
- ES-LATAM+ES "calendarios 2027 para imprimir": 183 anúncios; muitos packs em USD neutro, todos de poucos dias (Maria Dibujos 3D "12 calendarios 2027 para imprimir y armar", Mente Viva, Decora con Pasión "Superpack viral", Megapack Digital, El Taller de Liz, Mentoría Global). Sazonal e disputado em espanhol neutro.
- IT "calendario 2027 da stampare": 1 (gráfica local). BRECHA sazonal IT (janela nov–jan). FR/DE/PL: não pesquisado (orçamento de buscas).

### B2. Papelaria de casamento editável no Canva (111)
- ES-LATAM+ES "invitaciones de boda editables Canva": 16. Pack de Plantillas (USD, "Pack de invitaciones listos para editar", ~2–3 d, 6 criativos), Mara Cursos y Packs Online (USD, ~44 d), PlayKids (PEN, ~33 d, genérico), Morador marketer (COP, curso de convites digitais). PROVADO fraco em espanhol neutro (USD, sem país definido). Europa não pesquisada.

### B3. Moldes para artesanato e costura (112, 114, 128, 145)
- "moldes de vestidos para niña PDF": 6 (Domina tu arte USD, Cursos PDF CLP), todos novos. TESTE.
- "bordado en papel moldes": 32. **Bordados en Papel** (page 1329354533602746, USD) com a MESMA copy do BR (145: "Creá piezas hermosas en solo 15 minutos, desde tu casa"), 6+ criativos de ~1 dia = clone BR em espanhol neutro. Recursos creativos (USD). TESTE (onda começando).

### B4. Receitas para vender: caseirinhos, geladinho (110, 147)
- "recetas de bolis gourmet para vender": 21. Máster Class Online (COP) anúncio há ~79 dias; Rincón Artesanal (USD) ~61 dias; Marcianitos Pro (ARS, "Tu negocio de marcianitos desde casa"), Dulcaria Repostería (USD, "Heladitos gourmet"), mega pack vips recetas (MXN). PROVADO em espanhol (CO/neutro); equivalente local do geladinho = bolis (MX), marcianitos (AR), helados de vasito (CO).

### B5. Estimulação cognitiva para idosos (124)
- ES-LATAM+ES "estimulación cognitiva adultos mayores cuadernillo": 31. Cognimente (PEN, "Libro de entrenamiento mental", 7 criativos novos), Tu Libro Digital (MXN, "+4.262 descargas"), Mejora tu Memoria (MXN), Recursos Didácticos (PEN). Ativo; dias dos principais não medidos (VERIFICAR).
- IT "stimolazione cognitiva anziani esercizi": 17. **Palestra Mentale** (page 1389699987550571, USD = brasileiro) "Un anno di laboratori, pronto da stampare", ~15 dias, voltado a educadores/animadores de RSA (profissional!); **Seduta Pronta** (1447072035149109, USD) "La seduta di domani, già pronta", ~2 dias (para terapeutas). Onda BR entrando na Itália. TESTE IT.
- FR "stimulation cognitive seniors exercices": 0. BRECHA FR.

### B6. Infantil: grafomotricidade, alfabetização, caligrafia, massinha (115, 136, 142, 143, 158)
- ES-LATAM+ES "grafomotricidad cuadernillo imprimible": 6. **Kid Genius Digital** (MXN) anúncio ativo há ~251 dias; **kidgenius_digital** (MXN) ~325 dias; **Stardex Educación** (MXN) ~269 dias; **Aprendo contigo en PDF** (PEN) ~124 dias. PROVADO MX e PE (longo prazo).
- IT "pregrafismo schede bambini": 4. **Mente Gentile** (page 1263061760225674, EUR) "Radici per la Primaria", ~41 dias = PROVADO IT em euro; Mondo Infanzia Didattica (USD, BR) ~9 d.
- FR "graphisme maternelle fiches à imprimer": 0. BRECHA FR (no termo testado).

### B7. Plantas medicinais/garrafadas (148) e protocolo capilar natural (132)
- ES-LATAM+ES "plantas medicinales recetas remedios PDF": 4. **Saber Digital** (USD) anúncio ativo há ~322 dias; Secretos Naturales (COP, "+900 remedios en PDF", ~2,5 d); Andrés Navarro (PEN, ~16 d). PROVADO em espanhol neutro (USD). Capilar não pesquisado à parte (mesmo público; tratar como bump).

### B8. Música para igreja: cifras simplificadas (121)
- ES+US "tocar en la iglesia acordes": 17. Colección Digital De Fe (ARS, "Cancionero con los Bonos", ~4 d), Tocar Desde Cero Guitarra (USD), Sam On Bass (USD), Viva Semente (BRL = brasileiro vendendo em espanhol, ~14 d). TESTE (ninguém ≥30 d visto).

### B9. Religioso: Odus Meji/Ifá (126) e Kit São Bento (150)
- "Odu Ifá libro PDF": 0; "Ifá Odun": 2 (Secretos de la Santería, MXN, ~10 d). TESTE pequeno (público santero MX/CU/VE/US; Cuba fora do Meta Ads). São Bento: não pesquisado (funil de quiz com kit físico, fora do modelo).

### B10. Estampas: artes cristãs para camisetas (137) e pano de prato (139)
- ES+US "diseños cristianos para sublimar camisetas": 6. **Creación Cristiana** (page 769199572940540, USD) "1000 Diseños Cristianos de calidad", ativo há ~95 dias = PROVADO (espanhol neutro); Fe y Diseño (BOB, Bolívia, "+20.000 diseños religiosos", ~23 d); Pixelpack (USD, "+2.000 diseños cristianos", ~3 d); Bendiciones creativas (USD).

### B11. Posts prontos por profissão (135 lash, 151 estética "Dra.", 144 personal trainer)
- ES-LATAM+ES "posts editables Canva para esteticistas": 95 (busca ampla); Mind Digital Studio (USD, "Tu marca de coach"), Pack Insta de Impacto (BRL = brasileiro em espanhol, "Plantillas Black Friday"). Mercado tomado por packs genéricos em USD/BRL.
- IT "post pronti Canva estetiste": 16; sem pack de posts para esteticista. Achados laterais relevantes: **Kit Studio Blindato - APP** (1294553453740890, USD; o concorrente BR do dentista/psicólogo na Itália agora anuncia "APP", ~8 d); **Paulina Vera** "Kit Immobiliare Pro" (USD, ~1 d = BR levando kit de corretor para a Itália); Marjposa Phytocosmesi (EUR, protocolos para centros de emagrecimento).

### B12. Macros de sublimação (123) e eletricista residencial (108)
- "plantillas sublimación CorelDRAW" (LATAM+ES): 18. **Smartsubli** (BRL = brasileiro vendendo em espanhol) "Diseño en todos los moldes con 1 clic", ~23 dias. TESTE (o próprio BR exportando).
- "instalaciones eléctricas residenciales paso a paso PDF": 10. **Faradayos** (USD) "Guía ilustrada de instalaciones eléctricas", ~56 dias; **Mentes Ganadoras - Packs Digitales** (ARS) "Mega Pack Electricidad", ~79 dias; Academia Online PRO (USD) ~5 d; CEDAP e ProAcademy (MXN, cursos). PROVADO (AR e espanhol neutro).

### Checagens finais (top do ranking)
- Psicólogo, AR/CL/PE/EC/UY "documentos clínicos psicólogo plantillas consentimiento informado": 0. "historia clínica psicología plantillas" (AR/CL/PE/EC/UY/ES): 3; **Psicoagenda** (ARS) ~22 dias (produto VERIFICAR: agenda/software?); Aprende y Emprende en Casa "Pack Psicología" (MXN) ~58 dias (México, já conhecido).
- "informe psicopedagógico plantilla" (LATAM+ES): 0.
- ABA, "hojas de registro ABA terapeutas" (LATAM+ES+US): só Conecta ABA (USD, ~5–7 d). Confirma: em espanhol só há 1 vendedor de kit ABA, com 1 semana.
- Estimulação cognitiva profissional: FR "animation EHPAD fiches activités": 1 = **The Resource Lab** (USD) "Votre semaine d'ateliers, déjà prête", ~10 dias (mesmo padrão de copy de "Palestra Mentale"/"Seduta Pronta" na Itália; provável mesmo operador BR, VERIFICAR). DE "Beschäftigung Senioren Demenz Material": 0. ES "talleres estimulación cognitiva residencias mayores listos": 0; LATAM "sesiones de estimulación cognitiva listas para terapeutas": 0. Palestra Mentale medida por página: 11 ativos, mais antigo ~15 dias, criativos novos há ~9 dias (escalando).
- Instalador CFTV: PL "kurs instalator monitoringu kamer": 0; DE "Videoüberwachung Kurs Errichter": 0.
- Grafomotricidade PL "karty pracy grafomotoryka": 9; vendedores nativos em PLN de longa data: **Pomoce dydaktyczne - Gugu Rabbit** ~807 dias, **ABC w dydaktyce** ~114 dias, Zakątek Pedagogicznych Inspiracji ~44 d, Przedszkolne EduStory (900 páginas PDF) ~3 d. PL = PROVADO e competitivo (nativo).
- Concursos ES "esquemas oposiciones PDF temario": 8; academias (Esfera, Junta de Andalucía, Prefortia, Pilar Fernández) + **Emma Schneider** (BRL = brasileira) "De 300 páginas a 42 esquemas", ~7 dias. TESTE ES (BR chegando).

### Idiomas não pesquisados (orçamento de buscas)
RO, CZ, SK, HU, GR, NL e TR não foram consultados com termos próprios; DE e PL só nos conceitos de topo. Aparições laterais: CZK em marcenaria (Woodworking DIY Ideas, Dřevo Chotyně). Os termos traduzidos estão na seção 1 para a próxima rodada.
