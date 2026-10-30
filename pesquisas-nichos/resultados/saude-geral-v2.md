# Saúde geral por país — v2 (30/10/2026)

Cobertura: home care/cuidadores, ABA/autismo, fono (fonoaudiologia/logopedia/orthophonie), TO, psicopedagogo, enfermagem, consultório médico, veterinário, podólogo e residências de idosos. Países: LATAM (MX, CO, CL, AR, PE, EC), EUA, Espanha, Itália, Portugal, França, Alemanha, Polônia e Reino Unido.

## Avisos de método (ler primeiro)
- **v1 inacessível.** A v1 (`pesquisas-nichos-2026-10-29/saude-geral.md`, de 29/10) NÃO estava disponível neste ambiente (container na nuvem, sem Desktop). Usei os itens VERIFICAR escritos no próprio prompt e as notas do usuário (`notas/*.md`). Por isso a comparação com a v1 se limita a esses itens (seção "Itens VERIFICAR herdados da v1").
- **SearchAPI indisponível.** Não há chave neste ambiente e os créditos estão zerados até 08/11/2026. Toda a medição foi feita pelo conector Meta (`ads_library_search`, que só mostra anúncios ATIVOS).
  - **DIAS REAIS** = 30/10/2026 − o menor `ad_delivery_start_time` entre os anúncios ativos da página, consultando por `page_ids`.
  - **Nº de anúncios** = `estimated_total_count` na busca por page_id. Quando passa de 50, os dias são um mínimo: tomei o anúncio mais antigo visto em qualquer busca.
- **O conector Meta não devolve o texto nem o link do anúncio.** Ele traz só a página, o título do link, as datas e a moeda. Preço e conteúdo só aparecem quando estão no título do link.
- **Rede bloqueada.** WebFetch e curl deram 403/ENOTFOUND em todos os domínios testados: facebook.com, hotmart.com, payhip.com, caredaily.co.uk, cqc.org.uk, gob.mx, dof.gob.mx, minsal.cl, bcn.cl, boe.es, ine.es, istat.it e outros.
  - Não deu para abrir nenhuma página de vendas nem o snapshot dos anúncios.
  - Normas e tamanhos vêm dos resumos do WebSearch, com a URL da fonte. Conferir no texto oficial antes de usar em copy.
- **WebSearch esgotado.** O limite de 200 buscas por turno, compartilhado com os agentes irmãos, acabou no meio da pesquisa. Os itens que dependiam de busca ficaram como VERIFICAR.
- **Régua.**
  - PROVADO = vendedor ativo há 30+ dias no país/idioma/moeda.
  - TESTE = sinal sem vendedor antigo.
  - PRAZO = gancho com data de norma.
  - BRECHA = ninguém vende.
  - Espanhol neutro (conta USD/BRL) não prova país. Conta em moeda local (MXN, COP, CLP, ARS, GBP, EUR) indica o país do operador, não necessariamente o do comprador.

## Resumo (top da lista)
1. **CO — Kit de habilitação para consultório (médico, fono, TO, psico, fisio), Res. 3100 — 7,5.** Qualitiva Soluciones está ativa há 276 dias, em COP, com "Documentos listos para adaptar" e "Evalúa tu cumplimiento de la Resolución 3100". A M&B tem 94 dias e um evento sobre habilitação em 27/11. Reaproveita o Dentista Colômbia que já está na fila.
2. **IT — Logopedista (materiali + documentazione + app) — 7,0.** A demanda por material está provada na Itália:
   - ABA Tools: 133 anúncios, o mais antigo em italiano com 91 dias.
   - Pubblicazioni Upbility: 61 dias, €7–€114.
   - Diario di una Logopedista: 37 dias.

   Ninguém vende a parte documental (anamnesi, consenso, relazione, privacy). São ~15 mil logopedistas. Reaproveita a operação na Itália (dentista e psicólogo).
3. **MX — Kit Consultorio Médico (NOM-004 + COFEPRIS) — 6,5.** Recursos Legales PRO Salud Mx: 99 dias, 5 anúncios, $499 MXN (o kit de psicologia também custa $499). Concorrência pequena e nenhuma com app. Reaproveita a infraestrutura do Psicólogo MX.
4. **LATAM — Podologia (fichas, protocolos e consentimentos + app) — 6,5.**
   - Educación Podológica: 139 dias, 24 anúncios, CLP. Vende pack de livros, não documentos.
   - Brasileiros já começaram a portar para o espanhol: Caminho da Podologia (17 dias) e Biblioteca Podológica PRO (2 dias).
   - Há ~4,7 mil anúncios de clínicas de podologia na LATAM, ou seja, uma base grande de profissionais.
5. **UK — Domiciliary care / supported living: políticas CQC + app — 6,5.** Care Daily: 132 dias, 8 anúncios, GBP. PRAZO: o novo framework da CQC, com a volta das KLOEs, deve entrar em vigor no fim de 2026 (fontes de mercado, VERIFICAR). Os concorrentes são B2B caros (OnCare, Croner, Care4Quality).

**Achado transversal: a onda de operadores brasileiros nos materiais terapêuticos.** Nas últimas 2 a 4 semanas, operadores com conta em USD ou BRL estão portando formatos brasileiros ("+500 atividades", "atlas visual", "biblioteca") para IT, FR, PL, PT e espanhol neutro:
- ABA Tools, Kit Terapia Occupazionale e Gotowe Zajęcia SI;
- Neuropratika, Orthomap e Actividades Kids;
- Caminho da Podologia, Vet Clinic Docs e María Elena;
- Acervo Pro, Espacio Integración e Kit Psicopedagógico Completo.

A janela de "primeiro a chegar" nessas profissões está fechando. Quase todos vendem atividades e livros, não documentos com app. A brecha do formato do usuário continua aberta.

**Aviso para o Psicólogo MX (fila nº 1):**
- **Psique y Ciencia** (page 382519355660997): 13 anúncios, 33 dias, MXN, "Kit de Plantillas para Psicólogos | +10 documentos esenciales", mais curso de expediente.
- **Recursos Legales PRO**: "Kit Legal Psicología $499 MXN".

São dois concorrentes diretos já ativos no México.

## Ranking 0–10
| # | País / idioma | Nicho | Régua | Evidência principal (page_id em "Vendedores") | Nota |
|---|---|---|---|---|---|
| 1 | Colômbia (COP) | Kit habilitação consultório/IPS (Res. 3100), estendido a médico, fono, TO, psico e fisio | PROVADO + PRAZO (visitas de verificação; "plazo de la 1888" VERIFICAR) | Qualitiva 276d / 36 anúncios no par; M&B 94d; Dt.Dental "El plazo de la 1888 ya venció" | **7,5** |
| 2 | Itália (EUR) | Logopedista: material + documentos + app | PROVADO (material) / BRECHA (documentos) | ABA Tools 91d em IT (133 anúncios no total); Upbility 61d; Arianna Allegretti 37d | **7,0** |
| 3 | México (MXN) | Kit Consultorio Médico (NOM-004 expediente, COFEPRIS) | PROVADO (pequeno) | Recursos Legales PRO 99d, 5 anúncios, $499 MXN; Formatos digitales 27d | **6,5** |
| 4 | LATAM espanhol (CLP/BRL) | Podologia: fichas, protocolos e consentimentos + app | PROVADO (livros) / TESTE (documentos) | Educación Podológica 139d, 24 anúncios; Caminho da Podologia 17d; Biblioteca Podológica PRO 2d | **6,5** |
| 5 | Reino Unido (GBP) | Domiciliary care / supported living: políticas CQC + app de registros | PROVADO + PRAZO (novo framework CQC, fim de 2026, VERIFICAR) | Care Daily 132d, 8 anúncios; CQC Compliance Services 88d (serviço) | **6,5** |
| 6 | França (FR) | Orthophonie: material + documentos | PROVADO (ABA Tools 125d em FR) / TESTE | ABA Tools 125d; Orthomap (BR) 13d; Paroles d'ortho 9d; Actividades Kids (BR) 7d | **6,0** |
| 7 | México (MXN) | Veterinária: formatos (consentimentos, historia clínica, receitas) | PROVADO (1 criativo) | Vetdigital 344d (1 anúncio); Formatos digitales 27d; Vet Clinic Docs (BR, espanhol) 59d | **6,0** |
| 8 | EUA/inglês (USD) | ABA para RBT/BCBA (atividades, data sheets, planos) | TESTE | ABA Tools EN desde 15/10 (~15d); ABA in School 36d; 85,6 mil BCBA e 260 mil RBT (BACB) | **5,5** |
| 9 | Argentina (voseo, USD/ARS) | Fono e psicopedagogia: material + informes | TESTE | Fonoaudiología Profesional 16 anúncios, 17d; Mind.espaciopsicopedagógico 3d; ~1,5 mil anúncios de centros psicopedagógicos | **5,5** |
| 10 | LATAM espanhol | Terapia ocupacional: sessões, atividades e documentos | TESTE | Mi Colega T.O 14 anúncios, 2d, US$17,99; Espacio Integración (BR) | **5,5** |
| 11 | Chile (CLP) | ELEAM: protocolos, registros e plano de emergência | BRECHA + PRAZO | Zero vendedor de kit. Decreto 20/2021 vigente desde 01/04/2025; fiscalização reforçada após o incêndio de Pitrufquén (set/2026) | **5,5** |
| 12 | Espanhol neutro / LATAM | ABA para terapeutas (programas, registros) | BRECHA | Zero vendedor em espanhol ("actividades ABA naturalistas" = 0). No BR: Inovaba 179d, ABA na Prática 33d | **5,0** |
| 13 | Espanha (EUR) | Logopedas, residências e podólogos | BRECHA | Só cursos (Fono Aprende, Wumbox); ~11 mil logopedas | **5,0** |
| 14 | Polônia (PLN) | Logopeda / integração sensorial (SI) | TESTE | Gotowe Zajęcia SI 13d (USD); ecossistema nativo de cursos (NODN Cognitus, Klamerka, LogoMowa) | **5,0** |
| 15 | México (MXN) | Enfermagem / kits hospitalares | TESTE / PROVADO fraco | Kits Profesionales 22d (farmacovigilância, laboratório, ambulâncias); EEK Digital 36d (1 anúncio, estudo) | **5,0** |
| 16 | Itália (EUR) | Terapia occupazionale | TESTE | Kit Terapia Occupazionale 2d (USD, "+500 attività") | **4,5** |
| 17 | Portugal (EUR) | Terapia da fala | TESTE | Neuropratika (BR) 7d | **4,0** |
| 18 | Itália (EUR) | OSS, infermieri, RSA | BRECHA sem sinal | Zero vendedor de material/documentos | **4,0** |
| 19 | Alemanha (EUR) | Logopädie / Ergo | PROVADO (editora nativa) | K2-Verlag 354d; idioma e concorrência estabelecida | **3,5** |
| 20 | EUA hispano | Home care / cuidadores | Sem sinal | Busca em espanhol só devolveu ruído | **3,5** |

## Por profissão

### Home care / cuidadores
- **Reino Unido:** Care Daily (GBP, 132d, 8 anúncios).
  - Títulos: "Domiciliary care policies, ready to customise"; "Supported living policies. Not adapted. Written."; "The children can't wait. Your policies shouldn't either." (children's homes); "Equip your carers. Keep your carers."; "Replace the folder. Start fresh."; "Your records deserve better than a ring binder."
  - Vende políticas + registros e treinamento, em formato pronto para personalizar.
  - Preço não visível: o site está bloqueado (VERIFICAR).
  - CQC Compliance Services (88d) vende serviço de registro, não é low ticket.
  - Concorrentes conhecidos por busca: OnCare (233 políticas para care home, 173 para domiciliary, 168 para supported living), Worknest, Croner-i, Care4Quality, CareDocs e um pacote de £499 no Payhip.
  - O low ticket (£19–£49) com app de inspeção é a brecha de preço.
- **EUA e América Latina (cuidadores):** nenhum vendedor de kit. As buscas em espanhol só trouxeram ruído (dramas, suplementos). BRECHA sem prova.

### ABA / autismo
- **ABA Tools** (page 108617997275390, conta em USD): 133 anúncios ativos, em vários idiomas.
  - "+500 Attività ABA Naturalistiche" (IT) e "+500 Naturalistic ABA Activities for Autism" (EN), criados em 15/10.
  - O anúncio em francês mais antigo tem 125d; em italiano, 91d ("Meno preparazione, sedute più leggere").
  - Padrão de operador brasileiro escalando. Não vende em espanhol.
- **EUA:** o Meta está dominado por clínicas de ABA. ABA in School tem 36d. Não apareceu vendedor de templates/data sheets para BCBA além do ABA Tools (EN, novo).
- **LATAM espanhol:** só clínicas dos EUA anunciando em espanhol e material para pais e professores:
  - Avanza Edu: anúncio com 479d, MXN.
  - Grupo Educare: 115d, MXN.
  - Mundo Apoyo Digital: "Kit de Autismo + TDAH", 15d, USD.

  Kit ABA para terapeutas em espanhol = BRECHA.
- **Referência BR:** Inovaba "Kit de Programas / documentos terapia ABA", 179d, R$47; ABA na Prática, 33d, R$27; +3.000 Atividades para autistas, 185d.

### Fono / logopedia / orthophonie
- **Itália:** três vendedores provados.
  - ABA Tools: 91d em IT.
  - Pubblicazioni Upbility: 61d, ~25 anúncios, ebooks/workbooks de €7,24 a €113,90.
  - Logopedista Arianna Allegretti / Diario di una Logopedista: 37d, 4 anúncios, "Materiali print-and-go per logopedisti".
  - Vocologica vende curso.
  - Ninguém vende documentação do logopedista.
- **França:**
  - ABA Tools: 125d.
  - Orthomap "Atlas visuel de l'orthophonie" (BRL): 13d.
  - Paroles d'ortho (EUR, nativo): "20 activités ludiques", 9d.
  - Actividades Kids (BRL): 7d.
  - Logo Pep's.
- **Espanha:** só formação (Fono Aprende em EUR; Wumbox em USD). BRECHA de material e documentos.
- **Argentina / espanhol neutro:**
  - Fonoaudiología Profesional (USD): 16 anúncios, 17d, "Material para fonoaudiólogas", "Abrís, imprimís, atendés" (voseo).
  - Fichas Materiales Didácticos (USD): anúncio de 65d.
  - Impulso digital packs (CLP): anúncio de 168d com "terapia de lenguaje imprimible".
  - Educación Online (USD): muitos anúncios novos para pais e docentes.
- **Chile:** 13.645 fonoaudiólogos (RNPI; o ano é VERIFICAR). Nos anúncios dominam centros e serviços.
- **Polônia:** ecossistema nativo de cursos e plataformas (Klamerka/Zaklamerkowani, NODN Cognitus, LogoMowa, Kursy Pedagogiczne). O clone brasileiro "Gotowe Zajęcia SI" está em teste há 13d.
- **Portugal:** Neuropratika (BRL), "+600 atividades visuais", 7d.
- **Alemanha:** K2-Verlag (editora, 354d).
- **EUA:** nenhum vendedor de material para SLP no Meta (o TpT domina fora do Meta).
- **Referência BR:** App Kit Fonoaudióloga Pro, 156d, R$17,9; App Clínico para Fonoaudiólogas, 46d; FonoLu Kids, 141 anúncios.

### Terapia ocupacional (TO)
- **LATAM:** Mi Colega T.O (conta CLP, preço US$17,99): 14 anúncios, ~2d. Oferece "+1.500 actividades por edad", "+180 sesiones listas en 1 minuto" e "Tareas para la casa". É novo. Espacio Integración (BRL) vende o "Pack Inicial para Terapeutas Ocupacionales".
- **Itália:** Kit Terapia Occupazionale (USD), "+500 attività", 2d.
- **Polônia:** Gotowe Zajęcia SI, 13d.
- **Referência BR:** "+150 Atividades de TO", 82d, R$27; "Protocolos clínicos para TO infantil", 47d; Mapas Mentais de TO, 14d.

### Psicopedagogo
- **Argentina:** base enorme (~1.556 anúncios ativos com "psicopedagogía", quase todos de centros e consultórios). Mind.espaciopsicopedagógico (ARS, "Cuadernillos/Recursos Psicope", 3d) é o único nativo vendendo material.
- **Operadores brasileiros em espanhol:**
  - Acervo Pro (BRL): "50+ recursos para psicopedagogos por $15", 1d.
  - Kit Psicopedagógico Completo (BRL): novo.
- **Referência BR:** Kit Destrava Atendimento, 207d, 49 anúncios, R$37,9; Clubinho da Família, 42 e 31 anúncios.

### Enfermagem
- **México:**
  - EEK Digital: "Kit Enfermería + EGEL Plus | $149.99" MXN, 36d, 1 anúncio (estudo).
  - Kits Profesionales (MXN, 22d): Kit Farmacovigilancia Hospitalaria 2026, Manuales Laboratorio Clínico 2026 e Protocolos de Ambulancias 2026.
  - Diplomados Gratis CCPE: "¿Tu registro clínico podría protegerte?" (gancho jurídico do registro de enfermagem).
- **Chile:** Enfermeras Alfa (CLP), conteúdo não visível.
- **Espanhol neutro, operador BR:** María Elena (BRL), "Estudia Instrumentación Quirúrgica de forma visual".
- **Itália:** zero.

### Consultório médico
- **México:**
  - Recursos Legales PRO Salud Mx: 99d, 5 anúncios. Catálogo: Kit Consultorio Médico $499, Kit Cirujano Dentista $499, Kit Legal Psicología $499, Spa/Cosmetología $699, PNOs Farmacia $249/$699/$999 (MXN). Também tem kits jurídicos de 26 formatos + 3 guias a $499 e de 6 áreas a $699.
  - Softwares (My Doctor Diary, MedoraHealth, Huli com "Resumen de NOM 024 y NOM 004") vendem a dor do expediente.
- **Colômbia:**
  - Qualitiva: 276d, consultoria + documentos para habilitação (Res. 3100) e auditoria de história clínica.
  - M&B Calidad y Gestión: 94d, preventa "Habilitación 360" e evento em 27/11.
  - JIT Consultings.
  - Dt.Dental (software): "El plazo de la 1888 ya venció".

### Veterinário
- **México:**
  - Vetdigital: 1 anúncio ativo há 344d ("INCLUYE REGALOS ⭐⭐⭐⭐⭐ (5/5)"). Um criativo evergreen indica venda constante. Conteúdo é VERIFICAR.
  - Formatos digitales (MXN): 7 anúncios, 27d.
  - Biblioteca Médica Digital e EduNova (USD): novos.
- **Espanhol neutro:** Vet Clinic Docs (BRL), "documentos y formularios para médicos veterinarios", 59d, 1 anúncio. Por busca web: "Pack Veterinaria" na Hotmart (1.500+ itens, "formatos 100% editables").
- **Espanha e Itália:** nada.
- **Referência BR:** Combo Veterinária, 19d; Atlas Visual da Anatomia Veterinária, 32d.

### Podólogo
- **LATAM:**
  - Educación Podológica (CLP): 139d, 24 anúncios, "Pack de 15 Libros de Podología + Bonos" / "Biblioteca Digital de Podología".
  - Caminho da Podologia (BRL, 17d em espanhol): "Menos papel en tu consulta podológica", "Tu consulta, más organizada". É o mesmo vendedor que no BR vende a "Biblioteca Podológica Profissional" por R$49,9.
  - Biblioteca Podológica PRO (BRL, 2d).
  - Salud y Bienestar (COP), "150+ Visual Podiatry Procedure Cards".
  - Dra. Valentina González (BRL).
- **Espanha, Portugal e Itália:** zero. A Itália tem ~2.401 podólogos.
- **Referência BR:** 60 Protocolos Clínicos de Podologia, 38d.

### Residências de idosos
- **Chile:** só os próprios ELEAM anunciando vagas e ICCE capacita (curso). Nenhum kit documental.
- **Espanha:** nenhum vendedor de protocolos de residência.
- **Itália:** nenhum vendedor para RSA/OSS (só um curso OSS regional).
- **Reino Unido:** Care Daily (care homes e supported living via políticas) e concorrentes B2B.
- **Referência BR:** "Combo Vitalício de Documentos para UAN, Consultoria, ILPIs", R$79,9; Regulariza Visa "+100 POPs editáveis", 148d, R$29,9.

## Vendedores registrados (page_id)
Medidos em 30/10/2026. "d" = dias reais do anúncio ativo mais antigo da página.

| page_id | Página | Moeda | Anúncios | Dias | Oferta (título do anúncio) | Régua |
|---|---|---|---|---|---|---|
| 574842992375227 | Qualitiva Soluciones (CO) | COP | 32 | 276 | Documentos listos para adaptar; Res. 3100 | PROVADO |
| 1105323405997653 | M&B Calidad y Gestión (CO) | COP | 4 | 94 | Habilitación 360; evento 27/11 | PROVADO (serviço) |
| 880855681786807 | Recursos Legales PRO Salud Mx | MXN | 5 | 99 | Kit Consultorio Médico $499 e outros | PROVADO |
| 382519355660997 | Psique y Ciencia (MX) | MXN | 13 | 33 | Kit de Plantillas para Psicólogos (+10 docs) | PROVADO (concorrente do Psi MX) |
| 629381216925799 | Formatos digitales (MX) | MXN | 7 | 27 | formatos (veterinária/consultório) | TESTE |
| 106843625785534 | Vetdigital (MX) | MXN | 1 | 344 | "INCLUYE REGALOS (5/5)" veterinária | PROVADO (1 criativo) |
| 1170526269488341 | Vet Clinic Docs | BRL | 1 | 59 | documentos/formulários veterinários (espanhol) | PROVADO fraco (espanhol neutro) |
| 1321426567716161 | EEK Digital (MX) | MXN | 1 | 36 | Kit Enfermería + EGEL Plus $149,99 | PROVADO fraco |
| 692615883936217 | Kits Profesionales (MX) | MXN | 7 | 22 | Farmacovigilancia / Laboratorio / Ambulancias 2026 | TESTE |
| 679234251930805 | Educación Podológica | CLP | 24 | 139 | Pack 15 Libros de Podología + Bonos | PROVADO |
| 836490686213835 | Caminho da Podologia | BRL | 3 | 17 | consulta podológica organizada (espanhol) | TESTE |
| 1356915250840498 | Biblioteca Podológica PRO | BRL | 1 | 2 | pack podologia (espanhol) | TESTE |
| 364507726755472 | Salud y Bienestar | COP | ? | ~6 | 150+ Visual Podiatry Procedure Cards | TESTE |
| 1485100974676859 | Mi Colega T.O | CLP (US$17,99) | 14 | 2 | +1.500 actividades / +180 sesiones TO | TESTE |
| 1361408630394815 | Espacio Integración | BRL | ? | ~5 | Pack Inicial para Terapeutas Ocupacionales | TESTE |
| 1283844954801148 | Fonoaudiología Profesional | USD | 16 | 17 | Material para fonoaudiólogas | TESTE |
| 1402620623198397 | Fichas Materiales Didácticos | USD | ? | 65 | material fono/autismo (anúncio de 65d) | PROVADO fraco (espanhol neutro) |
| 1122092400982131 | Impulso digital packs | CLP | ? | 168 | terapia de lenguaje imprimible (anúncio de 168d) | PROVADO (VERIFICAR conteúdo) |
| 101279499654041 | Educación Online | USD | muitos | ~15 | atividades para pais e docentes | TESTE |
| 103518728924695 | Mind.espaciopsicopedagógico (AR) | ARS | 5 | 3 | Cuadernillos Psicope | TESTE |
| 1417313931454645 | Acervo Pro | BRL | ? | 1 | 50+ recursos psicopedagogos $15 | TESTE |
| 1428675950328112 | Kit Psicopedagógico Completo | BRL | 1 | ~3 | kit psicopedagógico (espanhol) | TESTE |
| 112084827204914 | Avanza Edu (MX) | MXN | ? | 479 | autismo imprimibles (pais/escola) | PROVADO (educação) |
| 108720541890696 | Grupo Educare (MX) | MXN | ? | 115 | autismo (pais/escola) | PROVADO (educação) |
| 1108064889061132 | Mundo Apoyo Digital | USD | ? | 15 | Kit de Autismo + TDAH | TESTE |
| 1332747779914944 | María Elena | BRL | 4+ | ~8 | Instrumentación Quirúrgica visual (espanhol) | TESTE |
| 412861181906925 | Care Daily (UK) | GBP | 8 | 132 | políticas domiciliary/supported living/children | PROVADO |
| 107264267734802 | CQC Compliance Services (UK) | GBP | ? | 88 | CQC Registration Support (serviço) | PROVADO (serviço) |
| 1849957218431496 | ABA in School (EUA) | USD | 2+ | 36 | material ABA para special ed teachers | PROVADO fraco |
| 108617997275390 | ABA Tools | USD | 133 | 125 (FR) / 91 (IT) / ~15 (EN) | +500 atividades ABA naturalistas | PROVADO FR/IT |
| 713489862161038 | Pubblicazioni Upbility (IT) | EUR | ~25 | 61 | ebooks terapia €7–€114 | PROVADO |
| 2198276620184577 | Logopedista Arianna Allegretti (IT) | EUR | 4 | 37 | Materiali print-and-go per logopedisti | PROVADO |
| 1374023202459384 | Kit Terapia Occupazionale (IT) | USD | 5 | 2 | +500 attività | TESTE |
| 300436823837471 | Orthomap Atlas visuel de l'orthophonie | BRL | ? | 13 | atlas visual orthophonie (FR) | TESTE |
| 1241967982338858 | Actividades Kids | BRL | 6+ | 7 | stimulation du langage (FR) | TESTE |
| 815428784980420 | Paroles d'ortho (FR) | EUR | ? | 9 | 20 activités ludiques orthophonie | TESTE |
| 1436879739501520 | Gotowe Zajęcia SI (PL) | USD | 7 | 13 | +500 gotowych ćwiczeń SI | TESTE |
| 1872727082974748 | Klamerka / Zaklamerkowani.pl (PL) | PLN | 1 | 0 | plataforma de materiais/cursos para logopedas | — |
| 101523636053617 | Neuropratika (PT) | BRL | 5 | 7 | +600 atividades visuais | TESTE |
| 139567646066162 | K2-Verlag (DE) | EUR | 3+ | 354 | editora de material Logo/Ergo | PROVADO |
| 800794539774651 | Fono Aprende | EUR | muitos | — | formação em fono/logopedia (ES/CL) | curso |

## Normas e prazos (fontes oficiais via WebSearch; WebFetch bloqueado)
- **México, NOM-004-SSA3-2012 (expediente clínico).**
  - Segue a versão do DOF de 15/10/2012: https://dof.gob.mx/normasOficiales.php?codp=4909&view=si
  - Não achei projeto nem atualização em 2026.
  - Guarda mínima de 5 anos desde a última atenção (fonte comercial: https://agendapro.com/blog/nom-004/). VERIFICAR no DOF.
  - Sem PRAZO novo. Funciona como gancho de "cumplimiento", não de data.
- **Chile, ELEAM.**
  - Reglamento = Decreto 20/2021 Minsal, em vigor desde 01/04/2025: https://www.bcn.cl/leychile/navegar?idNorma=1214791
  - Modificado em fev/2025 e com prorrogações parciais: https://www.diariooficial.interior.gob.cl/publicaciones/2025/04/22/44130/01/2635106.pdf
  - Exigências de prevenção de incêndio valem 5 anos após a vigência (≈2030).
  - Autorização e fiscalização são da SEREMI de Salud.
  - O Minsal publicou o listado de ELEAM autorizados com corte em 14/09/2026: https://www.minsal.cl/ministerio-de-salud-publica-listado-de-eleam-que-cuentan-con-autorizacion-sanitaria/
  - O incêndio de Pitrufquén (16 mortos, set/2026) motivou um plano de reforço da fiscalização: https://www.minsal.cl/gobierno-anuncia-plan-para-reforzar-la-seguridad-y-ampliar-la-oferta-de-cuidados-para-personas-mayores/ e https://www.emol.com/noticias/Nacional/2026/09/15/1211496/residencias-adultos-mayores-fiscalizacion-pitrufquen.html
  - Gancho: "plano de emergência e registros prontos para a fiscalização". Não confirmei se o plano virou norma nova com data (VERIFICAR).
- **Reino Unido, CQC.**
  - O Single Assessment Framework (34 quality statements, sem intervalo fixo de inspeção) continua valendo.
  - O novo framework com a volta das KLOEs deve ter versão final no verão de 2026 e implementação no fim de 2026, segundo fontes de mercado: https://carelinelive.com/cqc-new-assessment-framework-adult-social-care/ · https://www.learnsignal.com/blog/cqc-single-assessment-framework-quality-statements/
  - A CQC também está mudando o registro de homecare para reduzir o backlog: https://shiftcare.com/uk/blog/cqc-registration-2026-whats-changed-how-submit-a-compliant-application
  - Data exata de go-live: VERIFICAR em cqc.org.uk.
- **Colômbia.**
  - Res. 3100/2019: habilitação, base dos anúncios da Qualitiva.
  - "Resolución 1888": o anúncio da Dt.Dental diz que o prazo já venceu. Número, assunto e data = VERIFICAR (a busca acabou).
  - Nota do usuário: nunca prometer a data da Res. 914 (03/01/2027).

## Tamanho de mercado (fontes oficiais)
| Profissão / país | Número | Fonte (URL) | Status |
|---|---|---|---|
| ABA — EUA/mundo (BACB) | 85.587 BCBA, 5.246 BCaBA e 260.174 RBT em 01/07/2026 (fim de 2025: 81.566 BCBA / 246.109 RBT) | https://bacb.com/bacb-certificant-data · https://www.bacb.com/bacbs-2025-data/ | Confirmado (página oficial, via busca) |
| Fono — EUA (ASHA) | 235.443 profissionais CSD no fim de 2025, dos quais 14.296 audiologistas; SLP certificados ~218.646 (número de blog, conferir no PDF) | https://www.asha.org/siteassets/surveys/2025-asha-member-and-affiliate-profile.pdf | Total confirmado; nº de SLP = VERIFICAR |
| Fono — Chile (RNPI, Superintendencia de Salud) | 13.645 fonoaudiólogos (2,28% dos inscritos; ano do corte não visível); boletins anteriores: 12.449 e 10.840 | https://www.superdesalud.gob.cl/app/uploads/2026/01/boletin-n4-2025-rnpi-enero-diciembre-2025.pdf | VERIFICAR o ano no boletim nº 4/2025 |
| TO — Chile (RNPI) | 6.296 (boletim anterior: 5.264) | idem | VERIFICAR o ano |
| Logopedas — Espanha (INE, colegiados) | ~10.900 colegiados (INE, dado de 2021); o CSIF estima 11–12 mil; 92,7% mulheres (INE 2025) | https://ine.es/dyngs/Prensa/EPSC2025.pdf · https://www.csif.es/es/articulo/nacional/sanidad/86331 | Número de 2025 = VERIFICAR na tabela EPSC 2025 |
| Logopedisti — Itália | ~15 mil inscritos (24 por 100 mil hab.), segundo entrevista da presidente da Commissione d'albo | https://www.quotidianosanita.it/lavoro-e-professioni/il-nostro-viaggio-tra-le-professioni-sanitarie-i-logopedisti-intervista-alla-presidente-tiziana-rossetto/ | Sem data exata → VERIFICAR |
| Podologi — Itália | ~2.401 inscritos (audição na Câmara, nov/2024, Associazione Italiana Podologi) | https://documenti.camera.it/leg19/documentiAcquisiti/COM12/Audizioni/leg19.com12.Audizioni.Memoria.PUBBLICO.ideGes.51507.26-11-2024-10-46-55.199.pdf | Fonte associativa |
| Fono / TO — Colômbia (ReTHUS) | não encontrado | — | VERIFICAR (Observatorio de Talento Humano, MinSalud) |
| TO — Itália; TO — EUA (AOTA) | não encontrado | — | VERIFICAR |
| Proxy de base (não é censo) | ~4.708 anúncios ativos com "podología" na LATAM; ~1.556 com "psicopedagogía"; ~1.200 com "fonoaudiología" (MX/CO/CL/AR/PE/EC) | conector Meta, 30/10 | Indica muitos profissionais anunciando o próprio serviço |

## Itens VERIFICAR herdados da v1 (status)
| Item | Status v2 |
|---|---|
| Tamanho oficial de fono | EUA (ASHA, total CSD) e Chile (RNPI) encontrados; Espanha (INE 2021) e Itália (estimativa da Commissione) parciais; Colômbia não encontrado |
| Tamanho oficial de TO | Chile 6.296 (ano VERIFICAR); EUA, Itália e Colômbia não encontrados |
| Tamanho oficial de ABA | **Confirmado:** BACB 85.587 BCBA e 260.174 RBT (01/07/2026) |
| Datas de fiscalização CQC | Novo framework (KLOEs) previsto para o fim de 2026 (fontes de mercado); data oficial = VERIFICAR |
| Datas de fiscalização NOM-004 | Sem atualização ou prazo em 2026 encontrado; norma de 15/10/2012 vigente |
| Datas de fiscalização ELEAM | Decreto 20/2021 vigente desde 01/04/2025; listado de autorizados com corte em 14/09/2026; plano de fiscalização pós-Pitrufquén (set/2026); norma nova com data = VERIFICAR |
| Preço/conteúdo Care Daily | Localizado: page 412861181906925, 8 anúncios, 132d, GBP, conteúdo pelos títulos; preço = VERIFICAR (site bloqueado) |
| Preço/conteúdo ABA Tools | Localizado: page 108617997275390, 133 anúncios, FR 125d / IT 91d / EN ~15d, "+500 atividades ABA naturalistas"; preço = VERIFICAR |
| Preço/conteúdo Instituto Zasada | **Não localizado** (Meta e web sem resultado com esse nome) → VERIFICAR o nome/página com o usuário |
| Preço/conteúdo Fonoaudiología Profesional | Localizado: page 1283844954801148, 16 anúncios, 17d, USD, "Material para fonoaudiólogas", voseo; preço = VERIFICAR |
| Registrar ~25 vendedores novos com page_id | **Feito:** 40 páginas na tabela de vendedores |

## Referência Brasil (EscalaLow, para arbitragem)
Ofertas de saúde validadas no BR (dias / anúncios / preço) que servem de modelo para portar:
- Kit Destrava Atendimento (psicopedagogia): 207–211d / 49–52 / R$37,9.
- Inovaba, Kit de Programas ABA: 179–183d / 16 / R$47.
- App Kit Fonoaudióloga Pro: 156d / R$17,9.
- Documentos de Psicomotricidade: 114–118d / 20 / R$15,9.
- Regulariza Visa, +100 POPs editáveis: 148d / R$29,9.
- +150 Atividades de TO: 82d / R$27.
- Kit Docs Odonto: 238d / 32 / R$67.
- 60 Protocolos de Podologia: 38d / R$27.
- Biblioteca Podológica Profissional: 14d / R$49,9.

No exterior, a lacuna é a mesma: atividades já estão sendo portadas; documentos + app por profissão, quase nada.

## VERIFICAR (lista final)
1. Preço e conteúdo de Care Daily, ABA Tools, Fonoaudiología Profesional, Vetdigital, Educación Podológica, Mi Colega T.O e Psique y Ciencia. É preciso liberar facebook.com e hotmart.com na rede, ou usar o navegador embutido no Mac.
2. Instituto Zasada: não localizado. Confirmar o nome ou a page com o usuário (ou na v1).
3. Data oficial do go-live do novo framework da CQC (KLOEs) em cqc.org.uk.
4. Chile: o plano pós-Pitrufquén gerou norma ou prazo para os ELEAM? Quantos ELEAM existem e quantos estão autorizados (listado de 14/09/2026)?
5. Colômbia: número, assunto e prazo da "Resolución 1888" citada pela Dt.Dental. Conferir também a Res. 3100 e a Res. 465/2025.
6. México: guarda de 5 anos e demais requisitos da NOM-004 no DOF; não há prazo novo.
7. Tamanhos:
   - fono e TO na Colômbia (ReTHUS);
   - TO nos EUA (AOTA) e na Itália;
   - logopedas na Espanha em 2025 (INE EPSC);
   - logopedisti na Itália (com data);
   - ano do corte do RNPI Chile;
   - médicos e veterinários no México;
   - podólogos na Espanha e no Chile;
   - logopedas na Polônia;
   - orthophonistes na França.
8. Re-checar os dias de quem estava abaixo de 30d em 12/11 e em 27–28/11:
   - Fonoaudiología Profesional (17d), Mi Colega T.O (2d), Kits Profesionales (22d);
   - Caminho da Podologia em espanhol (17d), Gotowe Zajęcia SI (13d), Orthomap (13d);
   - Kit Terapia Occupazionale (2d), Neuropratika (7d), Mind (3d).
9. Confirmar se ABA Tools e Kit Terapia Occupazionale são o mesmo operador. Os dois usam conta USD e o padrão "+500 atividades" em IT.
10. Conferir se Impulso digital packs (CLP, 168d) e Fichas Materiales Didácticos (USD, 65d) vendem material de fono de fato (só aparecem pelo termo da busca).

## O que bloqueou
- v1 e Desktop indisponíveis.
- SearchAPI sem chave e sem crédito até 08/11.
- WebFetch e curl bloqueados para todos os domínios: facebook, hotmart, payhip, sites oficiais.
- Cota de WebSearch (200 por turno, compartilhada) esgotada no meio da pesquisa.
- O conector Meta não traz o texto nem o link do anúncio, então preço, plataforma, bumps e garantia não foram vistos.
