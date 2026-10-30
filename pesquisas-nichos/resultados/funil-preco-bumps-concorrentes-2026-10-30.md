# Como os concorrentes vendem depois do clique: preço, bumps, garantia (30/10/2026)

> Status: CONCLUÍDO, com bloqueio (as páginas de vendas não puderam ser abertas; ver avisos).

## Avisos de método
- **A versão anterior (v1 de 29/10) e os relatórios citados em "Ler antes" NÃO estavam acessíveis** neste ambiente. Por isso não há comparação com a v1. A lista de vendedores foi tirada das notas (`notas/*.md`), dos nomes citados nos prompts de `01-refazer-v2/` e `03-novas-lancadas/` e de `resultados/` (vazio quando esta pesquisa começou). Novos vendedores foram achados por termo no conector Meta.
- **O SearchAPI estava indisponível** (sem chave aqui e créditos zerados até 08/11/2026). A medição foi feita só com o conector Meta (`ads_library_search`, anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
- **BLOQUEIO PRINCIPAL: as páginas de vendas NÃO puderam ser abertas.** A política de rede deste ambiente nega a saída para os sites dos vendedores e para os checkouts. Testados e negados (WebFetch "ENOTFOUND" e proxy "403 CONNECT"): psiorganizado.com, consultorioemdia.shop, kit-docs-odonto.lovable.app, www.lovable.app, pay.hotmart.com, hotmart.com, go.hotmart.com, payhip.com, www.facebook.com (Biblioteca de Anúncios em HTML), web.archive.org e en.wikipedia.org. Agentes irmãos também foram barrados em kiwify.com.br, impultienda.com e www.google.com. Para liberar, o usuário precisa abrir as configurações do ambiente na nuvem (menu do ambiente na barra de título da sessão → Edit → Network access) e adicionar esses domínios em "Allowed domains", ou escolher um nível de acesso mais amplo. Passo a passo: https://code.claude.com/docs/en/cloud-environments#network-access
- **A busca web acabou no meio da pesquisa.** O limite de 200 buscas por turno, dividido entre todos os agentes, se esgotou. Antes disso, poucas buscas deram resultado: as landing pages (lovable, vercel, sites próprios) quase não estão indexadas.
- O que deu para fazer:
  - (a) Pelo conector Meta: dias reais, nº de anúncios ativos, moeda da conta de anúncios e título do link de cada anúncio. O título mostra gancho, prova social, CTA e, às vezes, o PREÇO.
  - (b) Trechos de resultados de busca, quando apareceram (marcados "(trecho de busca)").
  - (c) Dados já registrados nas notas do usuário (marcados "(notas 28–29/10)").
  - Bumps, upsells, estrutura da página e garantia dos concorrentes ficaram quase todos VERIFICAR.
- **Atenção:** o campo `currency` do conector é a moeda da CONTA DE ANÚNCIOS, não a do preço. Uma conta em USD ou BRL anunciando na Itália é sinal de operador estrangeiro (provavelmente brasileiro). Não quer dizer que o preço seja em dólar ou em real.
- Câmbio: as conversões são APROXIMADAS (ordem de grandeza) e não foram checadas hoje. Elas estão marcadas "≈" e entram na lista VERIFICAR.
- Nenhuma compra feita e nenhum formulário preenchido.

## 1. Vendedores e medição (dias reais, nº de anúncios, moeda)

Medição em 30/10/2026 pelo conector Meta, por `page_id`, só anúncios ATIVOS. "Moeda conta" = moeda da conta de anúncios. Régua: PROVADO = 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo.

| # | Vendedor (page_id) | País / idioma | Nicho | Nº anúncios ativos | Anúncio ativo mais antigo | DIAS REAIS | Moeda conta | Régua |
|---|---|---|---|---|---|---|---|---|
| 1 | Kit Studio Blindato - APP (1294553453740890) | IT / italiano | dentista | 28 | 17/09/2026 | 42 | USD | PROVADO |
| 2 | Kit di Documenti Psicologici (1316795101520270) | IT / italiano | psicólogo | 35 | 23/09/2026 | 36 | USD | PROVADO |
| 3 | Sorrisi in Regola (1063538733498593) | IT / italiano | dentista e higienista | VERIFICAR (2 achados por termo) | 21/10/2026 | 8 | EUR | TESTE |
| 4 | Simple Budget Excel (233823119815880) | IT / italiano (e espanhol) | planilhas de finanças / forfettario | 41 | 16/02/2025 | 620 | EUR | PROVADO (gancho "Non superare gli 85k" ativo desde 23/08: 67 d) |
| 5 | Giulia Ferraresi (1299765756564104) | IT / italiano | "Kit Contabile Pratico 2027" | VERIFICAR | 22/10/2026 | 8 | USD | TESTE |
| 6 | Recursos Legales PRO / ...Salud Mx (880855681786807) | MX / espanhol | catálogo jurídico-saúde (médico, dentista, psicologia, spa, farmácia, advogado) | 5 | 23/07/2026 | 98 | MXN | PROVADO |
| 7 | Psique y Ciencia (382519355660997) | MX / espanhol | psicólogo (kit + curso de prontuário) | 13 | 26/09/2026 (kit desde 28/09) | 33 (kit 31) | MXN | PROVADO (no limite) |
| 8 | Aprende y Emprende en Casa (113921117042583) | MX / espanhol | "Pack Psicología", tanatologia, auto-hipnose | 5 | 01/09/2026 | 58 | MXN | PROVADO (multinicho) |
| 9 | Archivos Digitales Express (103894282759676) | MX / espanhol | estética (formatos) | VERIFICAR | 11/09/2026 | 48+ | MXN | PROVADO (provável) |
| 10 | Formatos digitales (629381216925799) | MX / espanhol | formatos clínicos | VERIFICAR | 02/10/2026 | 27 | MXN | TESTE |
| 11 | Psicólogo Organizado (929581043578532) | CO / espanhol | psicólogo clínico | 7 | 06/05/2026 | 176 | COP | PROVADO |
| 12 | Qualitiva Soluciones (574842992375227) | CO / espanhol | habilitação Res. 3100 (IPS e consultórios) | 32 | 26/01/2026 | 276 | COP | PROVADO |
| 13 | Dt.Dental Software Odontologico (644396635996094) | CO / espanhol | dentista (SOFTWARE, não kit) | 19 | 02/07/2026 | 119 | COP | PROVADO (software) |
| 14 | Kit de Herramientas Terapéuticas (1303750612814915) | espanhol neutro (aparece em ES) | psicólogo (ferramentas de sessão) | 5 | 22/08/2026 | 68 | BRL (operador BR) | PROVADO em espanhol; NÃO prova Espanha |
| 15 | Psicologia Brasileira (1257515014104811) | espanhol neutro (aparece em ES) | "100 SESSIONES TERAPÉUTICAS LISTAS" | VERIFICAR | 22/09/2026 | 37 | USD | PROVADO em espanhol; não prova país |
| 16 | Psicologia Sincera (115217541636995) | espanhol neutro | "200 SESSIONES TERAPÉUTICAS LISTAS" | VERIFICAR | 29/09/2026 | 30 | USD | limite |
| 17 | Miguel González (1263261563536702) | espanhol neutro | psicólogo ("Solo hoy por $15") | VERIFICAR | 08/10/2026 | 21 | BRL | TESTE |
| 18 | MenteCloud.com (1317896694749207) | CL / espanhol | psicólogo (plataforma) | 15+ | 23/10/2026 | 6 | CLP | TESTE |
| 19 | Lic. Zulma Laguna (778739435326228) | US / inglês | dentista (docs, SOPs, consentimentos) | 8 | 01/10/2026 | 28 | USD | TESTE (passa a PROVADO em 31/10 se continuar ativo) |
| 20 | Dental Master Pro Max (1170940042761217) | US / inglês | dentista (marketing, "$27") | 1 | 06/06/2026 | 145 | BRL (operador BR) | PROVADO fraco (1 anúncio) |
| 21 | Dental Marketing Vault (1361313653721768) | US / inglês | dentista (marketing, "$1") | VERIFICAR | 26/10/2026 | 3 | USD | TESTE |
| 22 | Childminder Resource Hut (564585390322776) | UK / inglês | childminder / creche (Ofsted, EYFS) | 35 | 01/07/2025 | 485 | GBP | PROVADO (o mais antigo da lista) |
| 23 | CareDocs Direct (1178206642051081) | UK / inglês | care (políticas sob encomenda via Fiverr) | VERIFICAR | 06/09/2026 | 53 | GBP | PROVADO (serviço, não kit) |
| 24 | Health Connect (730699523450802) | UK / inglês | care (gestão de políticas, assinatura) | 1 | 09/10/2026 | 20 | GBP | TESTE |
| 25 | Compliance Supports (227964520409222) | UK / inglês | care CQC (serviço) | VERIFICAR | 27/10/2026 | 2 | GBP | TESTE |
| 26 | Kontrola Sanepidu (388263394381460) | PL / polonês | salão/estética (procedimentos sanitários) | 12 | 01/10/2026 | 28 | PLN | Citado como 90+ d no prompt "criativos longevos", mas hoje o anúncio ativo mais antigo tem 28 d (trocou criativos) → VERIFICAR |
| 27 | Sophie Collins (1423844567472797) | PL / polonês | clone do Kontrola Sanepidu | VERIFICAR | 25/10/2026 | 4 | USD | TESTE |
| 28 | Wzory HACCP - sklep-haccp.pl (1024438174083225) | PL / polonês | HACCP (loja de .doc por tipo de negócio) | VERIFICAR | 05/10/2026 | 24+ | PLN | TESTE (loja provavelmente antiga, VERIFICAR) |
| 29 | Pedagog Online (108050164425367) | PL / polonês | ocena funkcjonalna (escola) | VERIFICAR | 18/10/2026 | 11+ | PLN | TESTE (por anúncio achado) |
| 30 | Docedentista (432219163846603) | aparece em PT | dentista | 5 (na busca PT) | 19/08/2026 | 71 | BRL | PT-BR que alcança Portugal; NÃO prova PT-PT → VERIFICAR |

**Não remedidos hoje (vêm das notas de 28–29/10; o conector não achou a página pelos termos usados):**
- Pani Andzia (~225 d) e Centrum Pedagogiczne (~150 d): PL, psicólogo escolar, 88–239 zł; COS a 149 zł.
- Ioana Mureșan: RO, dentista, 36 anúncios, 89 lei, início 22–28/10 (TESTE). Clonou para a Sérvia ("Sanja Marković", 1.990 RSD).
- Consultório em Dia (consultorioemdia.shop): PT, dentista, ~2,5 d em 29/10 (TESTE).
- Pflege DE a €7,90.
- Preços de consumidor em PT de €4,90 a €14,90.

**Achado importante (IT): os vendedores 1 e 2 são do mesmo operador.** As duas páginas criaram anúncios no mesmo minuto em três datas:
- 05/10/2026, entre 16:54:34 e 16:55:09 UTC;
- 07/10/2026, às 01:52 UTC;
- 21/10/2026, entre 18:23 e 18:28 UTC.

As duas usam o mesmo selo "⭐⭐⭐⭐⭐ 4.9/5" no título, conta em USD e o mesmo formato de nome ("Kit ... ").

## 2. Ficha de funil por vendedor (o que deu para ver sem abrir a página)

Legenda: ✔ = confirmado pelo título do anúncio ou pelas notas; VERIFICAR = só abrindo a página.

### 2.1 Kit Studio Blindato - APP (IT, dentista, PROVADO 42 d, 28 anúncios)
- Preço/moeda: €19,99 (notas 28/10). Âncora: VERIFICAR.
- Básico × completo, nº de documentos, bônus, bumps, upsells, checkout, garantia: VERIFICAR.
- Prova social ✔: "⭐⭐⭐⭐⭐ 4.9/5 · Kit Studio Blindato · 4,9 su 5" em boa parte dos anúncios.
- Ganchos de título ✔:
  - "🦷 Tutte le carte del tuo studio, già pronte"
  - "Stampa solo quello che ti serve"
  - "Ogni foglio della giornata, pronto"
- App ✔: "APP" está no nome da página (o que o app faz: VERIFICAR).
- Conteúdo: kit genérico, sem as normas italianas (notas 28/10). Esse é o nosso diferencial.
- Urgência: nenhuma no título.

### 2.2 Kit di Documenti Psicologici (IT, psicólogo, PROVADO 36 d, 35 anúncios)
- Preço/moeda: €19,99 (notas 28/10: "dentist and psychologist kits at €19.99, 30+ creatives"). Âncora: VERIFICAR.
- Nº de documentos ✔: "Oltre 270 documenti per psicologi 📄". O número grande é o gancho.
- Prova social ✔: "4.9/5 · 4,9 su 5" em quase todos os anúncios.
- Mesmo operador do 2.1 (ver acima).
- Bumps, upsells, garantia, checkout: VERIFICAR.
- Não tem a norma italiana de uso de IA (L.132/2025), que é o nosso gancho (notas).

### 2.3 Sorrisi in Regola (IT, 8 d, TESTE)
- Ganchos ✔:
  - "Meno carte, più pazienti"
  - "Il kit che mancava all'igienista": mira a higienista, não só ao dentista.
- Conta em EUR: pode ser um operador local ou europeu. VERIFICAR se é do usuário.

### 2.4 Simple Budget Excel (IT, planilhas, PROVADO 620 d, 41 anúncios)
- Escada de produtos ✔ (anúncio de catálogo): "Simple Budget Business | Gestor de Finanzas PRO BLACK | Pack Total | Finanzas Personales Sencillas – eBook | Gestor de Finanzas PRO | Gestor de Actividad PRO". Isso é básico × PRO × PRO BLACK + "Pack Total" (bundle) + e-book barato.
- Ganchos ✔:
  - "Non superare gli 85k per sbaglio" (desde 23/08)
  - "Quante tasse a giugno?"
  - "Sai davvero quanto guadagni?"
  - "L'utile è ciò che conta"
  - "Stima liquidità — da oggi"
  - "Da questo a questo. In 10 minuti."
- Preço: as notas citam "Excel competitor charges €69.97" no forfettario. É provável que seja este, mas falta confirmar (VERIFICAR).
- Consequência para o Termometro 85k: o gancho "não passe dos 85k" JÁ é usado há 67 dias. O nosso gancho tem que ser a "armadilha do 2º ano" (notas), não o limite de 85k.

### 2.5 Giulia Ferraresi (IT, 8 d, TESTE)
- ✔ "Kit Contabile Pratico 2027 · 7 quaderni + 8 bonus": ano no nome do produto e bônus empilhados no título. Conta em USD.

### 2.6 Recursos Legales PRO (MX, PROVADO 98 d, 5 anúncios): a ficha mais completa
- Preço no anúncio ✔ (tabela de catálogo):
  - Kit Consultorio Médico: MXN 499
  - Kit Cirujano Dentista: MXN 499
  - Kit Legal Psicología: MXN 499
  - Kit Spas y Cosmetología: MXN 699
  - PNOs Farmacia: Lite MXN 249 / Estándar MXN 699 / PRO MXN 999
- Escada básico × completo ✔: Lite / Estándar / PRO. Também "Colección Completa: $699 MXN | 6 Áreas Clave en un Solo Kit", para advogados.
- Nº de documentos ✔: "26 Formatos + 3 Guías | Obtenlo por $499 MXN".
- Gancho ✔: "¿Cambios gratis otra vez? | Define el Alcance" (dor do profissional).
- CTA ✔: "¡Comprar Ahora!", "Catálogo Legal Salud | Consulta Aquí".
- Câmbio ≈: MXN 499 ≈ US$ 25–28 ≈ €23–26 (VERIFICAR câmbio).
- Bumps, garantia, checkout: VERIFICAR.

### 2.7 Psique y Ciencia (MX, PROVADO 31–33 d, 13 anúncios)
- ✔ "Kit de Plantillas para Psicólogos | +10 documentos esenciales" roda junto com "¡Curso de expediente!" e "¡Curso de psicología!".
- Funil provável: kit barato na frente e curso como upsell ou segunda oferta. A ordem é VERIFICAR.
- Preço: VERIFICAR.

### 2.8 Aprende y Emprende en Casa (MX, PROVADO 58 d)
- ✔ "140+ Audios de Autohipnosis por 10 USD": preço em USD dentro do anúncio para a LATAM.
- ✔ "Pack Psicología", "Biblioteca de Tanatología y Duelo".

### 2.9 Psicólogo Organizado (CO, PROVADO 176 d, só 7 anúncios)
- Preço: COP 38.000, 22 modelos (notas 29/10). Câmbio ≈ US$ 9–10 (VERIFICAR).
- Ganchos ✔ (emocionais, de tempo e de dinheiro, nenhum de norma):
  - "Tu primer paciente llega con todo en orden 📁"
  - "Hay cosas que el título no te preparó para hacer"
  - "Psicólogo clínico, diagnosticar se te da bien. Registrar, ahora también ✅"
  - "Tus vacaciones no deberían tener pendientes clínicos"
  - "tu cerebro necesita descansar los domingos 🌙"
  - "¿Sabes cuánto ganas en realidad cada mes?": sugere planilha financeira no kit ou como bônus (VERIFICAR).
- Padrão: poucos anúncios e muito tempo no ar. É evergreen de verba baixa.

### 2.10 Qualitiva Soluciones (CO, PROVADO 276 d, 32 anúncios)
- Escada de valor ✔ pelos títulos:
  - "Documentos listos para adaptar" (produto)
  - "Evalúa tu cumplimiento de la Resolución 3100" (autoavaliação, isca)
  - "Agenda tu diagnóstico hoy" (consultoria)
  - "Curso Express de Habilitación IPS este sábado" (evento com data)
  - "Audita HC y mide adherencia a GPC" (ferramenta)
- Preços: VERIFICAR.

### 2.11 Dt.Dental (CO, software, PROVADO 119 d)
- Ganchos de norma com prazo ✔:
  - "El plazo de la 1888 ya venció"
  - "¿Cumples los 3 pasos de la 1888?"
  - "¿La Resolución 3100 te preocupa?"
  - "Prepárate hoy para la visita"
  - "Reporta tus RIPS sin descargar archivos JSON"
- No dentista CO, o nosso app concorre com SaaS: é preciso vender "pronto e barato" e não "sistema".

### 2.12 SaaS de prontuário MX (para comparar a oferta, não são kits)
- MedoraHealth ✔: "50 % en tu plan mensual · hasta el 31 de diciembre". Urgência com data real.
- Javier Camacho Vargas ✔: "Expediente clínico: prueba gratis 7 días". Teste grátis.
- Huli México ✔: "📋 Resumen de NOM 024 y NOM 004 para Salud". Isca de norma.
- My Doctor Diary ✔: "Tu consultorio, sin papeleo".

### 2.13 Espanhol neutro (operadores BR; não provam a Espanha)
- Kit de Herramientas Terapéuticas (68 d): CTA ✔ "Quiero mejorar mis sesiones".
- Psicologia Brasileira e Psicologia Sincera ✔: "100 / 200 SESSIONES TERAPÉUTICAS LISTAS". O número de sessões prontas é o gancho.
- Miguel González ✔: "Solo hoy por $15". Preço em USD e urgência diária.
- MenteCloud (CL) ✔: "¡Accede ahora! (4.9/5) ⭐⭐⭐⭐⭐". O mesmo selo 4.9/5 da Itália.

### 2.14 Lic. Zulma Laguna (US, dentista, 28 d)
- Preço: US$27, "Dental Kit in Free Canva" (notas 29/10).
- Ganchos ✔:
  - "Dental Docs, Done for You"
  - "Dental Protocols, Already Written"
  - "Not a Blank Template"
  - "See What's Inside the Dental Kit"
  - "Get Your Dental Clinic Inspection-Ready in 1 Hour 🦷📋"
  - "Lawyer-Reviewed Dental Consents & Forms 🦷⚖️": promessa de autoridade, VERIFICAR se é verdade.
  - "Transform Your Practice with Ready Dental SOPs"
- Outros dentistas nos EUA:
  - Dental Master Pro Max (145 d) ✔ "Get More Dental Patients For Just $27".
  - Dental Marketing Vault (3 d) ✔ "Halloween Dental Kit — $1": isca de US$1 sazonal.

### 2.15 Childminder Resource Hut (UK, PROVADO 485 d, 35 anúncios): o funil mais maduro da lista
- Loja com catálogo ✔: anúncios dinâmicos de produto ("{{product.name}}") e vários produtos.
- Upsell físico ✔: "GRAB a printer copy…", "GET A PRINTED COPY!!", "IN STOCK NOW!", "Key Rings", "The 2027 Calendars!", "NEW! The 2027 Childcare Calendar".
- Isca grátis ✔: "🚨 EYFS 2026 Get the FREE Guide".
- Prova social ✔: "Trusted by 40,000+ Early Years Pros".
- Edição anual e prazo de norma ✔:
  - "NEW! Inspection Ready - September 2026 - Action Plan & Guide"
  - "NEW - Safe Sleep - Ultimate Compliance Pack - 2026"
  - "NEW 2025 EYFS!! | Safeguarding Reforms! | Instant Download | Create Your Own Folder"
  - "Safeguarding Decoded - The Ultimate A-Z"
- Preços: VERIFICAR (a busca não achou a loja).
- Faixa de preço do mesmo nicho no UK (trecho de busca):
  - Payhip "OFSTED POLICIES & PROCEDURES PACK On Sale £19.99";
  - Childminding Association (Escócia) "Strong Foundations Pack" £15 para sócios e £35 para os demais;
  - HFL Education, auditoria de inspeção como serviço: £390 ou £32,50/mês.

### 2.16 Care no UK
- Health Connect ✔ "Complete Policy Management for £70 a month" (assinatura, 20 d).
- Compliance Supports ✔ "Full CQC Support — Save £701 Right Now" (âncora de desconto).
- CareDocs Direct ✔ "I will create professional care policies… for $25 on fiverr.com" (serviço a US$25, 53 d).

### 2.17 Kontrola Sanepidu (PL, 12 anúncios; 28 d hoje)
- Garantia longa ✔: "Procedury z 12-miesięczną gwarancją" (procedimentos com garantia de 12 meses). O que a garantia cobre é VERIFICAR (reembolso? aceitação na fiscalização? atualização?).
- Atualização anual ✔: "Kontrola Sanepidu | Aktualizacja na 2027".
- Ganchos ✔: "Procedury bez pisania od zera", "Sprawdź, czego brakuje w salonie" (checklist).
- Clone Sophie Collins (4 d) ✔: "Procedury gotowe do wywieszenia", "Wszystkie terminy na cały rok" (agenda anual de prazos), "Dokumentacja w jednym folderze".
- Outros no PL:
  - Magda Tercjak - Bezpieczny Salon ✔ "NAJWIĘKSZA PROMOCJA TYLKO DO 31.10" (promoção com data);
  - Wzory HACCP ✔ loja de .doc por tipo de negócio ("Dokumentacja HACCP dla pizzerii .doc", "Plan Higieny dla salonu kosmetycznego").

### 2.18 Hotmart e Gumroad em espanhol/português (trechos de busca; sem medição de anúncios)
- Gumroad SmartPsic ✔ "$55.60 $39.90": âncora riscada em USD para "Paquete Clínico 5 en 1 para Psicólogos".
- Hotmart (PT-BR) ✔ "Kit de Documentos Psicológicos" a R$ 97,00 com âncora de R$ 146,90.
- Hotmart (ES) ✔:
  - "Mini Pack de 195 Plantillas para Psicólogos";
  - "Maletín Clínico VIP: Pack Todo en Uno". O nome bate com o nosso "Maletín": VERIFICAR conflito de marca no MX;
  - "5 kits de plantillas para psicólogos", nota 4,0 com 35 avaliações.

### 2.19 Referência BR (EscalaLow, `escalalow-ofertas-validadas.json`)
- Preço das 146 ofertas validadas com preço: mediana R$27; quartis R$12,90 / R$27 / R$47. Os preços mais comuns são R$10, R$37, R$47, R$27 e R$67.
- Nichos profissionais: mediana R$27,45.
- Dentista: "Kit Completo de Documentos para Odontologia" a R$67, 238 d, 32 anúncios.
- Psicólogo: "Combo PSI Prático" R$37,90; "Kit Destrava Atendimento" R$37,90 (211 d, 52 anúncios); "Kit Acalmar" R$27.

## 3. Padrões por país

| País | Faixa de preço dos PROVADOS | Âncora / escada | Bumps e upsells vistos | Garantia vista | Prova social / urgência | Uso de app |
|---|---|---|---|---|---|---|
| IT | €19,99 (dentista e psicólogo, mesmo operador BR); planilhas fiscais ~€69,97 (notas, VERIFICAR) | Simple Budget: básico / PRO / PRO BLACK / Pack Total + e-book | Bundle "Pack Total"; "+8 bonus" (Giulia, teste) | VERIFICAR | "4.9/5 ⭐⭐⭐⭐⭐" em quase todos os anúncios; sem urgência | "APP" no nome do Kit Studio Blindato |
| MX | Kits MXN 499 (≈ €23–26); escada MXN 249 / 699 / 999; packs neutros US$10–15 | Lite / Estándar / PRO; "Colección Completa" | Curso de prontuário ao lado do kit (Psique y Ciencia) | VERIFICAR | Preço dentro do anúncio; SaaS com "50% hasta el 31 de diciembre" e "prueba gratis 7 días" | Concorrência de SaaS (Medora, Huli, My Doctor Diary) |
| CO | Psicólogo COP 38.000 (≈ US$9–10) | VERIFICAR | Qualitiva: documentos → autoavaliação → diagnóstico → curso | VERIFICAR | Ganchos de norma com prazo (Res. 1888, 3100); evento "este sábado" | Software Dt.Dental (RIPS, interoperabilidade) |
| ES | Nenhum vendedor nativo de kit de dentista ou psicólogo; só operadores BR em espanhol neutro (US$15 "Solo hoy") | — | — | — | "Solo hoy" | — |
| PL | Psicólogo escolar 88–239 zł (notas) | VERIFICAR | "Aktualizacja na 2027"; agenda anual de prazos (clone) | **12 meses** (Kontrola Sanepidu) | "Promoção só até 31.10" | Nenhum com app (notas) |
| UK | Packs £15–35; Payhip £19,99; assinatura £70/mês; serviço £390 | Edições anuais (2026, 2027) | Versão impressa, calendário 2027, chaveiros, guia grátis | VERIFICAR | "Trusted by 40,000+"; "Save £701" | — |
| US | US$27 (kit dentista e marketing dentista) | VERIFICAR | Isca de US$1 sazonal (teste) | VERIFICAR | "Lawyer-Reviewed", "Inspection-Ready in 1 Hour" | Canva grátis (Zulma) |
| RO | 89 lei (≈ €18) (notas, TESTE) | — | — | — | Gancho DSP (notas) | — |
| PT | Profissional: VERIFICAR; consumidor €4,90–14,90 (notas) | — | — | — | — | — |

**Padrões gerais:**
1. **O preço do kit de profissão provado gira em torno de US$/€ 20–27 nos países ricos e cai muito na LATAM pequena** (CO ≈ US$10).
2. **A âncora aparece como escada de produtos** (Lite/Estándar/PRO, PRO/PRO BLACK/Pack Total) mais do que como preço riscado. O preço riscado só foi visto no Gumroad e no Hotmart BR.
3. **Edição do ano e atualização** ("2026", "2027", "Aktualizacja na 2027") é o bump ou upsell mais repetido nos vendedores antigos (Childminder 485 d, Kontrola Sanepidu).
4. **A prova social "4.9/5"** é padrão dos operadores BR na Itália e no Chile. Ninguém a usa sem ter avaliações: precisamos de avaliações reais antes de copiar.
5. **Isca de autoavaliação ou checklist de inspeção** (Qualitiva, Kontrola, Zulma, Huli) é o gancho de quem dura 90+ dias.
6. **Garantia:** o único dado confirmado é a garantia de 12 meses do Kontrola Sanepidu. Todo o resto é VERIFICAR.

## 4. Comparação com nossos preços e recomendações por país

Nossos parâmetros: Valigetta del Dentista IT €27 (cheio) / €19 (oferta), bumps €9,90, garantia 15 dias. O preço do Maletín del Psicólogo MX não está nos arquivos: VERIFICAR.

### Itália (dentista, psicólogo, forfettario)
- **Faixa de preço:** manter **€19 efetivo**, em paridade com os €19,99 do concorrente BR (dentista e psicólogo), e **€27 como âncora** riscada ou como versão "completa". Não descer abaixo de €19: o concorrente já está lá e o nosso diferencial é a norma italiana (DGR Lazio 669/2026, curso de 16 h do datore, ECM/radioproteção), não o preço.
- **Escada sugerida** (padrão Simple Budget e Recursos Legales): Base €19 / Completo €27 / "Pacchetto Studio" €37–47, com o kit da equipe (higienista e assistente), que é o gancho do Sorrisi in Regola.
- **Bumps que faltam** (€9,90 continua coerente; nenhum concorrente mostra bump mais caro que isso, VERIFICAR):
  1. "Aggiornamento normativo 2027" (atualização anual; padrão Kontrola e Childminder).
  2. "Scadenzario adempimenti 2027" (agenda de prazos do ano; padrão do clone polonês e do calendário 2027 do Childminder): sedação DGR 669 até 07/02/2027, curso datore até 24/05/2027.
  3. Psicólogo: "Pack informativa uso IA (L.132/2025)".
  4. Bump de checklist "Pronto per l'ispezione" como isca ou como bump.
- **Garantia:** manter 15 dias (acima dos 14 dias do direito de arrependimento da UE; checar a regra de conteúdo digital, ver VERIFICAR). Somar uma promessa de **"aggiornamenti per 12 mesi"** como garantia de atualização, não de reembolso, no modelo do Kontrola Sanepidu.
- **Prova social:** os concorrentes estampam "4.9/5". Assim que tivermos avaliações reais, usar a nota no título do anúncio. Nunca inventar.
- **Termometro 85k:** o concorrente de planilha (620 d) já usa "Non superare gli 85k" e cobra ~€69,97 (VERIFICAR). Espaço para escada €29 / €49 / €69 e para o gancho próprio "trappola del secondo anno". Bump: "Calendario F24 2027"; upsell "versione 2027 (nuovo TUIR)".

### México (psicólogo; depois jornada e farmácias)
- **Faixa de preço:** o PROVADO cobra **MXN 499 por kit de profissão**, com escada MXN 249 / 699 / 999. Recomendado: **MXN 399–499 efetivo**, âncora MXN 899–999 ("colección completa"), e preço escrito no anúncio, como o Recursos Legales faz há 98 d.
- **Bumps** (equivalente a €9,90 ≈ MXN 190–200; VERIFICAR câmbio), faixa MXN 149–199:
  1. "Aviso de privacidad + consentimiento informado" (NOM-004/LFPDPPP; VERIFICAR o conteúdo exato com a base legal MX);
  2. "Control de ingresos del consultorio" (planilha; gancho "¿Sabes cuánto ganas?" do CO);
  3. "Curso/mini-aula de expediente clínico" como upsell (Psique y Ciencia).
- As notas dizem que os bumps no MX são opcionais. Recomendação: **ligar pelo menos 1 bump** antes de escalar.
- **Garantia:** sem dado de concorrente. Manter 15 dias (Hotmart permite de 7 a 30; VERIFICAR o mínimo atual).
- **Urgência:** só com data real. O SaaS usa "hasta el 31 de diciembre"; para jornada MX, a data da norma (01/01/2027) é a urgência legítima.

### Colômbia (psicólogo e dentista)
- **Faixa de preço:** o PROVADO de psicólogo cobra **COP 38.000** (≈ US$9–10). Recomendado: **COP 39.900–59.900**, âncora COP 97.000, bumps COP 14.900–19.900. O preço da Itália não serve aqui.
- **Dentista CO:** o gancho que dura 276 d é a **autoavaliação da Res. 3100** (Qualitiva). Pôr "Autoevaluación de habilitación" no app como isca ou bump, e vender "pronto e barato" contra o SaaS (Dt.Dental). Nunca prometer a data da Res. 914 (notas).

### Espanha
- Não há vendedor nativo de kit de dentista nem de psicólogo; só BR em espanhol neutro a ~US$15. Teste barato a **€19–27**, como na Itália, com bumps de €7,90–9,90 e diferencial de norma espanhola. A Espanha segue sem prova (régua).

### Polônia (psicólogo escolar)
- Concorrentes a 88–239 zł (notas). Mantém-se o plano de **79–99 zł**. Bump "Aktualizacja 2027 / nowe wzory" e **garantia de atualização de 12 meses**, que é o padrão local visto no Kontrola Sanepidu. Checar BLIK/checkout (notas).

### EUA (dentista)
- **US$27** é o preço provado (Zulma; Dental Master Pro Max 145 d). Bumps de US$9–12: SOP binder ou checklist de inspeção. Não usar "Lawyer-Reviewed" sem revisão real. Re-checar Zulma em 31/10–05/11.

### Reino Unido (se entrar com childminder ou care)
- Packs a **£15–29**, bumps de £7–9 e **edição anual** ("2027") como upsell. O líder (485 d) vende também versão impressa e calendário; a isca é um guia grátis.

### Romênia e Portugal
- RO: 89 lei (≈ €18) é o preço do operador que está expandindo (TESTE). Se entrar, €15–19 ou 79–89 lei.
- PT: sem preço profissional confirmado. Teste a €14,90–19,90 (VERIFICAR).

## 5. Ranking 0–10: o que copiar do funil dos concorrentes

Nota = força da prova (PROVADO, dias) × encaixe nas nossas ofertas × facilidade de aplicar.

| # | Ação | Onde | Prova | Nota |
|---|---|---|---|---|
| 1 | Manter €19 efetivo e €27 como âncora/completo; competir por norma italiana, não por preço | IT dentista e psicólogo | 2 PROVADOS a €19,99, mesmo operador, 36–42 d, 63 anúncios somados | **8,5** |
| 2 | Bump "Atualização 2027" (e promessa de 12 meses de atualização) | todos | Childminder 485 d; Kontrola Sanepidu "12-miesięczna gwarancja", "Aktualizacja na 2027" | **8,0** |
| 3 | Escada de 3 níveis (Base / Completo / Pacote equipe ou coleção) | IT, MX | Recursos Legales 98 d (249/499/699/999 MXN); Simple Budget 620 d (PRO / PRO BLACK / Pack Total) | **7,5** |
| 4 | Preço MX em MXN 399–499, escrito no anúncio, e pelo menos 1 bump ligado | MX psicólogo | Recursos Legales 98 d | **7,5** |
| 5 | Checklist/autoavaliação de inspeção como isca ou bump ("pronto para a fiscalização") | IT, CO, MX, US | Qualitiva 276 d; Kontrola; Zulma; Huli | **7,0** |
| 6 | Bump "agenda de prazos do ano" (scadenzario 2027) | IT, MX jornada, PL | Clone polonês "Wszystkie terminy na cały rok"; Childminder "2027 Calendar" | **7,0** |
| 7 | Nota de avaliação real (ex.: 4,9/5) no título do anúncio, assim que houver avaliações | IT, LATAM | Operador BR na IT (63 anúncios), MenteCloud CL | **6,5** |
| 8 | Preço CO baixo (COP 39.900–59.900) | CO psicólogo e dentista | Psicólogo Organizado 176 d a COP 38.000 (notas) | **6,5** |
| 9 | Upsell "curso/aula de prontuário" depois do kit | MX, CO | Psique y Ciencia (31–33 d) | **6,0** |
| 10 | Upsell "kit da equipe" (higienista, assistente) | IT dentista | Sorrisi in Regola (8 d, TESTE) | **5,5** |
| 11 | Urgência só com data real (norma ou campanha datada) | MX jornada, IT DGR 669 | MedoraHealth "hasta el 31 de diciembre"; "promoção até 31.10" (PL) | **5,5** |
| 12 | Isca grátis (guia da norma) para captar lista | IT, UK | Childminder "EYFS 2026 FREE Guide"; Huli "Resumen NOM 004" | **5,0** |
| 13 | Assinatura mensal de atualização | UK, IT | Health Connect £70/mês (20 d, TESTE) | **4,0** |
| 14 | Isca de US$1 sazonal | US | Dental Marketing Vault (3 d) | **2,5** |

## 6. VERIFICAR (lista final)
1. **Abrir as páginas de vendas** assim que a rede for liberada (domínios na seção de avisos) e preencher a ficha completa (preço, âncora, nº de documentos, bônus, bumps, upsells, checkout, garantia, estrutura, app) destes vendedores:
   - Kit Studio Blindato, Kit di Documenti Psicologici, Sorrisi in Regola, Simple Budget Excel (IT);
   - Recursos Legales PRO, Psique y Ciencia (MX);
   - Psicólogo Organizado (psiorganizado.com) e Qualitiva (CO);
   - Childminder Resource Hut (UK);
   - Kontrola Sanepidu (PL);
   - Lic. Zulma Laguna (US).
2. Confirmar que Kit Studio Blindato e Kit di Documenti Psicologici seguem a **€19,99** hoje (o dado é de 28/10) e se mostram âncora ou bump.
3. Confirmar que os dois kits italianos são do mesmo operador. Hoje a evidência é a criação de anúncios no mesmo minuto em 05/10, 07/10 e 21/10.
4. Confirmar se Simple Budget Excel é o "Excel competitor €69,97" das notas e qual é o preço de cada nível (PRO, PRO BLACK, Pack Total).
5. Sorrisi in Regola: é do usuário ou é concorrente? Mesma pergunta pendente sobre consultorioemdia.shop.
6. Zulma Laguna: re-checar em 31/10–05/11 (passa de 30 d em 31/10).
7. Kontrola Sanepidu: o prompt o lista como 90+ d, mas o anúncio ativo mais antigo hoje tem 28 d. Ver o histórico e o que cobre a "garantia de 12 meses".
8. Garantia legal na UE para conteúdo digital (direito de arrependimento de 14 dias e renúncia na entrega imediata; Diretiva 2011/83/UE). Checar a fonte oficial antes de mudar a garantia de 15 dias.
9. Hotmart: faixa de garantia permitida hoje (7 a 30 dias?) e regras de order bump por país e moeda.
10. Preço atual do Maletín del Psicólogo MX: não está nos arquivos.
11. Câmbio do dia para MXN, COP, PLN, RON e GBP (as conversões "≈" deste relatório são aproximadas).
12. Conflito de nome: "Maletín Clínico VIP" no Hotmart (ES) × o nosso "Maletín del Psicólogo".
13. Docedentista (BRL, 71 d em PT): é PT-PT ou PT-BR que vaza para Portugal?
14. Pani Andzia, Centrum Pedagogiczne e COS (PL): achar os page_ids (o conector não achou pelos termos usados) e remedir.
15. Ioana Mureșan (RO, 89 lei) e Sanja Marković (RS, 1.990 RSD): remedir em 12/11 e 27–28/11 (plano das notas).
16. "Lawyer-Reviewed" (Zulma) e "4.9/5" (operador BR na IT): são avaliações e revisões reais? Isso só serve de referência; não copiar sem ter o mesmo.
17. Archivos Digitales Express, Formatos digitales, Psicologia Brasileira e Sincera, Pedagog Online, Wzory HACCP: medir por page_id (nº de anúncios e dias), porque só foram vistos por termo.
