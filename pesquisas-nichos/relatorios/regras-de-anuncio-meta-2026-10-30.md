# Regras de anúncio da Meta por nicho e país (30/10/2026)

Escopo: o que a política de anúncios da Meta (e leis locais) permite ou restringe para vender kits de documentos + app a PROFISSIONAIS (dentista, psicólogo, fono, ABA, fisio, nutri, estética, advogado, contador, corretor, RH, professor, ofícios). Harmonização e injetáveis fora do escopo.

Método e limites (honesto):
- Fontes: artigos oficiais do Centro de Ajuda da Meta lidos pelo conector (ads_get_help_article) em 30/10/2026. As páginas de transparency.meta.com que tentei abrir por WebFetch deram 404 (URLs chutadas), então cito só facebook.com/business/help e help.instagram.com, que o conector devolveu. Nada foi testado em conta de anúncios (não alterei nada). "Risco" abaixo é leitura da política, não rejeição medida.
- SearchAPI sem crédito até 08/11; não usei. Navegador embutido não foi necessário (nenhuma aba aberta).
- Régua do ranking: nota 0-10 de FACILIDADE DE ANUNCIAR (10 = livre; 0 = bloqueio provável). Serve para descontar das notas de oportunidade dos relatórios v2, não para substituí-las.
- Prova indireta de que o formato passa: vendedores no ar há muito tempo com o mesmo tipo de oferta (ABA Tools 133 dias/133 anúncios em EN e IT; Care Daily UK 132 dias; Instituto Zasada PL 162 dias; Edukapol PL 544 dias; Geriactiva 47 dias; Nua Studio 53 dias, tudo dos v2). Isso mostra que kit para profissional passa na revisão, não que qualquer copy passe.

## 1. Mapa das políticas que importam para a gente

| # | Política | O que diz (resumo) | Fonte |
|---|---|---|---|
| P1 | Atributos pessoais | Proíbe anúncio que afirme ou IMPLIQUE atributos do espectador: deficiência, condição médica, saúde física ou mental, situação financeira vulnerável, idade, estado civil/familiar. Perguntas sobre atributos também violam. Pode usar "você/seu" se não mencionar atributo proibido. Exemplo da Meta: "Cansado de lidar com depressão?" viola. | https://www.facebook.com/business/help/2557868957763449 |
| P2 | Saúde e bem-estar | Não permite prometer curar/eliminar lista fechada de doenças, entre elas AUTISMO (nem por profissional de saúde; sintoma/manejo pode). Proíbe clickbait de saúde com resultado em prazo sem ressalva. Procedimentos cosméticos (inclui micropigmentação) só para 18+, antes/depois só em cosmético geral e 18+. Proíbe frases de inferioridade sobre aparência. | https://www.facebook.com/business/help/2489235377779939 |
| P3 | Categoria especial Moradia / Emprego / Produtos financeiros | Anúncio de "serviços imobiliários e busca de casa" conta como moradia; "programas de certificação profissional" e "entrevista/colocação garantida" contam como emprego; DICAS e educação sobre compra de imóvel não contam; "serviços de impostos e contabilidade" e financeiro só B2B NÃO contam. Exige escolher a categoria (restringe público: sem gênero, idade, CEP e lookalike) para anunciantes dos EUA ou públicos EUA/Canadá/Europa (lista inclui IT, ES, FR, DE, PL, PT, UK, RO). América Latina não está na lista. | https://www.facebook.com/business/help/399587795372584 e https://www.facebook.com/business/help/1537759006681893 |
| P4 | Verificação de serviços financeiros | Só para anúncio que PROMOVE produto financeiro (seguro, hipoteca, empréstimo, investimento, cartão). Exige verificação para Austrália, HK, Índia, Irlanda, Israel, ESPANHA, Taiwan, Tailândia, REINO UNIDO, EUA. Educação financeira e treinamento sem obter o produto ficam de fora. UK: FCA. | https://www.facebook.com/business/help/719892839342050 e https://help.instagram.com/1277459436206293 |
| P5 | Social issues, eleições ou política (SIEP) | Exige autorização + "paid for by". Regras de lei/política: defesa de mudança de lei, "legislação como regulamentos e decretos". Social issues (inclui economia, educação, saúde, imigração) fiscalizados em US, CA, UE, UK, SG, MM, NZ, TW. Anúncio que "principalmente vende produto/serviço" pode dispensar, MAS "isso não vale para produtos ou serviços sobre ou com menção a políticos, partidos, eleições ou LEGISLAÇÃO". Na UE, SIEP não pode rodar. Autorização eleição/política também exigida em BR, MX, CL, CO, AR, PE, IT, ES, FR, DE, PL, PT, RO, UK. | https://www.facebook.com/business/help/313752069181919 , https://www.facebook.com/business/help/253606115684173 , https://www.facebook.com/business/help/2150157295276323 |
| P6 | Conteúdo sensacionalista | Proíbe chocante, sensacionalista, "táticas chocantes ou assustadoras para chamar atenção"; lista é de imagem violenta, sangue, acidente, sofrimento. | https://www.facebook.com/business/help/304110064285796 |
| P7 | Ferramentas de negócio: informação proibida | Não enviar à Meta dado de saúde (inclui "saúde mental", "locais de tratamento"), financeiro ou dívida; nomes de eventos, conversões, públicos personalizados e parâmetros de URL não podem refletir isso. Core setup e data restrictions ajudam. | https://www.facebook.com/business/help/361948878201809 e https://www.facebook.com/business/help/414614186228298 |
| P8 | Anunciante e pagador (UE e outros) | Anúncio para a UE só publica com anunciante e pagador informados; aparece na Biblioteca de Anúncios (1 ano após última impressão). Vale também SG, TW, TH, MY, AU, IN. UK e América Latina não constam. | https://www.facebook.com/business/help/605021638170961 e https://www.facebook.com/business/help/721913190475838 |
| P9 | Rótulo "AI info" | Meta rotula automaticamente criativo gerado/editado por IA (detecta C2PA de ferramentas de terceiros). Em UE, Califórnia, NY, Índia e Taiwan o anunciante pode se autodeclarar e o rótulo aparece ao lado do "Patrocinado". Não é bloqueio. | https://www.facebook.com/business/help/1010479435004531 |
| P10 | Medicamentos controlados | Proibido sem autorização (só farmácia online/telessaúde/indústria, só US/CA/NZ). Não afeta kit de documentos; afeta qualquer criativo que "venda" medicamento. | https://www.facebook.com/business/help/263390265553560 |
| P11 | Adolescentes | UE/EEE/Suíça: anúncios para adolescentes pausados; sem segmentação detalhada para menores. Só relevante se app infantil for anunciado para menores (não deve). | https://help.instagram.com/496493705955763 |
| P12 | Segmentação por tema sensível (histórico) | Meta removeu em jan/2022 opções de segmentação por saúde, religião, orientação e política. Fonte secundária (imprensa), não achei o post oficial: VERIFICAR. Impacto: não dá para segmentar "pais de autistas" por interesse; com público profissional não faz falta (usar interesse de profissão/conselho). | https://searchengineland.com/meta-will-remove-targeting-options-for-sensitive-topics-on-january-19-378095 (secundária) |

## 2. As 7 armadilhas que mais machucam o nosso modelo (e como contornar sem violar)

1. Gancho de PRAZO com lei (P5). É o achado mais importante. Nossos ganchos "norma com data" (CNPCF 01/04/2027 MX, jornada 40 h MX, DL 170/2026 sostegno IT, RDC 1002 BR, Ley 27.802 AR, Res. 914 CO, Reforma26 PL) citam LEGISLAÇÃO. A Meta diz que a isenção de "venda de produto" não vale quando há menção a legislação. Risco: o anúncio cair como "política/social issue", pedir autorização e "paid for by" nos países onde se enforça, e na UE ser barrado (SIEP proibida na UE). Contorno: falar do DOCUMENTO e do requisito técnico ("o que a vigilância pede na inspeção", "documento exigido pela RDC 1002"), sem verbos de advocacia (apoiar, rejeitar, exigir mudança), sem nome de político/partido/ministro, sem "reforma/governo decidiu/lei nova polêmica". Testar 1 criativo com a lei no texto e 1 sem, em orçamento mínimo, antes de escalar. Status: VERIFICAR (a Meta não dá lista fechada).
2. Atributos de saúde do público final (P1/P2). Nosso comprador é o profissional, então "Você é fonoaudiólogo?" é livre (profissão não está na lista de atributos). Violam: "Seu filho tem autismo?", "Cansado de lidar com ansiedade?", "Pacientes com TEA precisam de..." dirigidos ao espectador como se fosse paciente/pai. Em ABA e fono infantil escrever sempre a partir do profissional ("seus atendimentos", "sua clínica"). Nunca prometer "cura/eliminar autismo" (P2, lista fechada, vale mesmo vindo de profissional); falar em "protocolos", "registro de evolução", "manejo de comportamento".
3. Categoria especial por semântica (P3). Corretor/imobiliário: "serviços imobiliários e busca de casa" entram em moradia; dica/educação não. O kit de contratos para corretor é ferramenta de profissional, mas o classificador pode ler "imóveis/aluguel" e exigir a categoria (na Europa isso trava gênero, idade, CEP e lookalike, o que piora CPA). Contador: tributação e contabilidade estão excluídos da categoria financeira, mas evite palavras de produto financeiro (empréstimo, crédito, investimento, seguro): na Espanha e no UK elas disparam verificação (P4). RH/DP: "vaga/emprego/contratação" empurra para Emprego; falar de "folha, jornada, rescisão" em vez de "vagas". Concursos/oposiciones/ECEP: "programas de certificação profissional" e "colocação garantida" estão listados em Emprego; o simulador de oposición pode ser lido assim (VERIFICAR com teste).
4. Medo e multa (P6). "Multa de €4.000" é dado factual e não é imagem chocante; a política mira imagem violenta e tática "assustadora". Evite fiscal batendo, algemas, sirene, tela vermelha de intimação, tom de ameaça. Prefira "o que o fiscal pede" + checklist.
5. Dados no pixel e na URL (P7). Parâmetros e eventos tipo "?nicho=autismo", evento "Purchase_Ansiedade", públicos personalizados "pacientes", "lista dívida" são proibidos. Para ofertas ao profissional o risco é baixo, mas em ABA/psico/fono nomear evento/URL com condição (autismo, depressão, TDAH) pode ser lido como dado de saúde. Usar nomes neutros (kit_aba_v1), core setup ligado, UTM sem condição.
6. Antes/depois e resultado (P2). Estética/PMU: antes/depois só 18+ e só cosmético geral; evitar "elimina", prazo de resultado e frase de inferioridade ("rugas feias"). Como o produto é kit de documentos, o criativo não deve mostrar procedimento em rosto; mostrar a pasta, o app, a ficha. Nutri: não mostrar "pinça de gordura" nem prometer perda de peso no criativo (P2).
7. IA em criativo (P9). Os b-rolls e imagens do ChatGPT/IA vão receber rótulo "AI info" (automático via C2PA) e, na UE, aparece ao lado do "Patrocinado". Não bloqueia; custo é de confiança. NÃO usar rosto de IA como "cliente real/depoimento" (decepção + política de alegações, que não consegui abrir: VERIFICAR texto oficial). Depoimentos devem ser reais (já é regra nossa).

## 3. Exigências de conta por região (não são rejeição, mas travam publicar)

| Região | Exigência | Fonte |
|---|---|---|
| UE (IT, ES, FR, DE, PL, PT, RO...) | Anunciante e pagador obrigatórios em todo anúncio novo/editado; nome exposto na Biblioteca. Por padrão a Meta preenche com o nome da Página; usar a razão social/marca que podemos expor | P8 |
| UE | SIEP não roda: anúncio lido como política/social issue é derrubado (ver armadilha 1) | P5 |
| UE, Califórnia, NY, Índia, Taiwan | Autodeclaração de IA opcional/possível, rótulo ao lado do "Patrocinado" | P9 |
| ES, UK, IE | Verificação só se promover produto financeiro (fora do nosso caso) | P4 |
| EUA/CA/UE (lista) | Categoria especial só se o anúncio for lido como moradia/emprego/crédito | P3 |
| BR, MX, CO, CL, AR, PE | Categoria especial de moradia/emprego/financeiro não é exigida pela lista da Meta; autorização de política/eleição existe (BR, MX, CL, CO, AR, PE constam). Social issues NÃO é fiscalizado em LatAm (só US, CA, UE, UK, SG, MM, NZ, TW). Logo o risco da armadilha 1 é MENOR na América Latina que na Europa | P3, P5 |
| Todas | Políticas valem também para a página de destino (a revisão olha landing); a lei local também vale: "o anunciante deve cumprir leis aplicáveis" (artigo de segmentação global) | https://www.facebook.com/business/help/1155157871341714 |

## 4. Leis locais de publicidade de saúde/profissões (fora da Meta)
As restrições nacionais sobre publicidade de dentistas, médicos, advogados etc. (ex.: regras de conselhos profissionais) miram o profissional que anuncia AO PACIENTE/CLIENTE. A nossa venda é do kit AO PROFISSIONAL, então não se aplicam diretamente. Porém, se o criativo se parecer com anúncio de clínica (paciente sorrindo, promessa de tratamento), a revisão automática pode tratá-lo como saúde. Não pesquisei norma por país aqui: VERIFICAR por país antes de qualquer anúncio que fale com o paciente final (não é nosso caso hoje).

## 5. Risco por nicho (resumo)

| Nicho | Gatilho principal | Risco | Nota de facilidade (0-10) |
|---|---|---|---|
| Dentista (IT, CO, MX, BR) | Gancho de norma (Res. 914 CO, RDC 1002 BR); imagem de consultório é segura | baixo | 8,5 |
| Contador / tributação (todos) | Tax e contabilidade excluídos da categoria financeira; evitar "crédito/empréstimo/investimento" (ES, UK verificam) | baixo | 8,5 |
| Fitness: pilates, yoga (ES) | Sessão pronta; sem promessa de emagrecimento | baixo | 8,5 |
| Fisio (IT, ES, CO, PL) | Tratamento de dor é saúde, mas direcionado ao profissional | baixo | 8,0 |
| Ofícios / HACCP / SST (FR, PL, IT, CO) | Multa/inspeção: tom factual; "reforma/lei" aciona P5 (UE) | baixo-médio | 7,5 |
| Educação / inclusão professor (PL, IT, MX, ES, CL) | "Aluno com deficiência" é atributo se dirigido ao espectador como aluno/pai; citar decreto/reforma aciona P5; educação é tema social | médio | 6,5 |
| Psicólogo (MX, IT, PL, BR) | Saúde mental (P1/P7): falar do consultório, nunca da ansiedade do público; eventos neutros | médio | 7,0 |
| Fono infantil (BR, ES-LATAM, PL) | Condição da criança (P1/P7); "criança" no criativo | médio | 6,5 |
| Geriatria / cuidador (ES, MX, CO, UK) | Idade e saúde do idoso (P1); ok se for para cuidador/empresa | médio | 6,5 |
| Estética esteticista (CO, MX) | Procedimentos, antes/depois só 18+, sem inferioridade (P2) | médio | 6,0 |
| Tatuador / piercer / PMU (MX, IT, ES, UK) | Micropigmentação é "cosmético" na política; imagem de agulha/pele pode cair em sensacionalismo (P6) | médio | 6,0 |
| Nutri (CO, AR, BR) | Perda de peso: sem negativo de aparência, sem prazo de resultado (P2) | médio | 6,0 |
| Advogado (MX CNPCF, IT atti, ES MASC) | Lei como gancho (P5, forte); imigração é tema social no exemplo oficial da Meta | médio-alto | 5,5 |
| Corretor imobiliário (MX Norma 247, FR, DE) | "Serviços imobiliários" = moradia (P3); categoria restringe público | médio-alto | 5,0 |
| RH / DP (MX jornada 40 h, ES) | Jornada de trabalho = lei trabalhista (P5) + "emprego" (P3) | médio-alto | 5,0 |
| Oposiciones / concursos / ECEP (ES, CL, RO, FR) | "Certificação profissional" e "colocação" em Emprego (P3); concurso público é política pública (P5) | alto | 4,5 |
| ABA / autismo (IT, ES-LATAM, FR/DE/PL) | Autismo está na lista de "não curar" (P2) e é atributo (P1). Prova positiva: ABA Tools 133 dias/133 anúncios (v2) mostra que passa com copy para o terapeuta | médio (alto se a copy escorregar) | 5,5 |
| Home care / care agency (UK) | Dirigir à agência (B2B); Care Daily 132 dias prova | baixo-médio | 7,0 |
| Médico + farmácia (MX) | Receita/controlados (P10): não vender medicamento, só documento | médio | 6,0 |
| Pastores / predicação (US-ES, LatAm) | Religião é atributo (P1) se dirigido ao espectador ("sua igreja"?); calendário litúrgico ok | médio | 6,5 |

Como usar: ajustar a nota de oportunidade dos v2 por esse fator (ex.: nota v2 8,5 de oposición PL educador × facilidade 6,5). Ranking final, melhor facilidade para pior: dentista, contador, pilates (8,5) > fisio (8,0) > ofícios/HACCP (7,5) > psicólogo, care UK (7,0) > fono infantil, geriatria, educação, pastores (6,5) > estética, tatuagem, nutri, médico MX (6,0) > ABA, advogado (5,5) > corretor, RH (5,0) > oposiciones (4,5).

## 6. Checklist de copy segura (aplicar em todo criativo)
- Sujeito = profissão do comprador ("fonoaudiólogo", "terapeuta ABA", "esteticista"), nunca o paciente.
- Zero pergunta sobre condição do espectador; zero "você tem/sofre de".
- Zero "cura", "elimina", "resolve em X dias" em contexto de saúde.
- Lei só como nome técnico do documento exigido, sem opinião, sem político, sem "reforma".
- Zero termos de crédito/seguro/investimento/vaga/imóvel à venda no texto e na landing, quando o produto não for isso.
- Eventos e URLs neutros; core setup ligado.
- Imagens: profissional, pasta, tela do app; sem procedimento em rosto, sem criança identificável em situação clínica, sem sangue/inspetor ameaçador.
- IA: aceitar o rótulo "AI info"; não simular cliente real.

## 7. LISTA FINAL DE VERIFICAR
1. Texto oficial da política de "alegações enganosas / resultados irrealistas / saúde pessoal e aparência": as URLs de transparency.meta.com que testei deram 404; falta citar o texto-fonte completo. O resumo vem do artigo de ajuda (saúde e bem-estar).
2. Ganchos de lei disparam SIEP? A Meta só diz que a isenção "não vale com menção a legislação"; falta teste real (1 criativo com lei, 1 sem) na UE e em MX/CO/BR.
3. Se "kit para corretor" e "simulador de oposición" são lidos como moradia/emprego (P3): só teste revela; sinal de custo é restrição de público e CPA.
4. Segmentação por interesse de saúde: post oficial da remoção de jan/2022 não localizado (só imprensa).
5. Regras nacionais de publicidade de cada conselho (CFO, CFP, ordens italianas, etc.) para o caso de anúncio falar com o paciente final: não pesquisadas.
6. Exigências específicas de MX (COFEPRIS) e CO (Invima/SIC) para criativo com procedimento estético/tatuagem: não pesquisadas.
7. Se a Meta já auto-aplica "AI info" nos nossos criativos hoje (depende do C2PA do arquivo): checar no "Sobre este anúncio".
8. Lista de países em que o "paid for by" da UE expõe razão social das nossas contas na Biblioteca: decidir qual nome mostrar (VERIFICAR com o usuário, é decisão de marca).
9. UK: fora da lista DSA de anunciante/pagador na lista que li; conferir se mudou.
10. Edição de 30/10/2026 não tem versão anterior para comparar (primeira rodada deste tema).
