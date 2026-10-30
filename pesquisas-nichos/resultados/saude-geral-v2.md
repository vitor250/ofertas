# Saúde geral por país — v2 (30/10/2026)

> Status: EM ANDAMENTO (arquivo gravado aos poucos).

## Avisos de método
- A v1 (`pesquisas-nichos-2026-10-29/saude-geral.md`, 29/10) NÃO estava acessível neste ambiente (container na nuvem, sem Desktop). Usei a lista de itens VERIFICAR escrita no próprio prompt e as notas do usuário (`notas/*.md`).
- SearchAPI indisponível (sem chave aqui e créditos zerados até 08/11/2026). Medição feita com o conector Meta (`ads_library_search`, só anúncios ATIVOS). DIAS REAIS = 30/10/2026 − menor `ad_delivery_start_time` entre os anúncios ativos da página (consulta por `page_ids`).
- Régua: PROVADO = vendedor ativo há 30+ dias no país/idioma/moeda; TESTE = sinal sem vendedor antigo; PRAZO = gancho com data de norma; BRECHA = ninguém vende. Espanhol neutro não prova país.
- Base BR (EscalaLow 24/10 e lista validada de 213): ver seção "Referência Brasil".
- REDE: neste container o WebFetch e o curl estão BLOQUEADOS para quase todos os domínios (facebook.com, hotmart.com, payhip.com, cqc.org.uk, gob.mx, minsal.cl, boe.es etc. → 403/ENOTFOUND). Consequência: (1) não deu para abrir páginas de vendas nem o snapshot dos anúncios (o conector Meta não devolve texto nem link do anúncio, só página, título do link, datas e moeda); (2) normas e tamanhos vêm dos resumos do WebSearch com a URL da fonte — conferir no texto oficial antes de usar em copy. Preço/conteúdo só onde o título do anúncio ou a busca mostrou.

## Ranking 0–10
(preenchendo)

## Por profissão
(preenchendo)

## Vendedores registrados (page_id)
(preenchendo)

## Normas e prazos (fontes oficiais)
(preenchendo)

## Tamanho de mercado (fontes oficiais)
| Profissão / país | Número | Fonte (URL) | Status |
|---|---|---|---|
| ABA — EUA/mundo (BACB) | 85.587 BCBA, 5.246 BCaBA, 260.174 RBT em 01/07/2026 (fim de 2025: 81.566 BCBA / 246.109 RBT) | https://bacb.com/bacb-certificant-data · https://www.bacb.com/bacbs-2025-data/ | Confirmado (página oficial, via busca) |
| Fono — EUA (ASHA) | 235.443 profissionais CSD no fim de 2025 (inclui 14.296 audiologistas); SLP certificados ~218.646 (número de blog, conferir no PDF) | https://www.asha.org/siteassets/surveys/2025-asha-member-and-affiliate-profile.pdf | Total confirmado; nº de SLP = VERIFICAR |
| Fono — Chile (RNPI Superintendencia de Salud) | 13.645 fonoaudiólogos (2,28% dos inscritos; ano do corte não visível); boletins anteriores: 12.449 e 10.840 | https://www.superdesalud.gob.cl/app/uploads/2026/01/boletin-n4-2025-rnpi-enero-diciembre-2025.pdf | VERIFICAR o ano no boletim nº4/2025 |
| TO — Chile (RNPI) | 6.296 (boletim anterior: 5.264) | idem | VERIFICAR ano |
| Logopedas — Espanha (INE colegiados) | ~10.900 colegiados (INE, dado 2021); CSIF estima 11–12 mil; 92,7% mulheres (INE 2025) | https://ine.es/dyngs/Prensa/EPSC2025.pdf · https://www.csif.es/es/articulo/nacional/sanidad/86331 | Número 2025 = VERIFICAR na tabela EPSC 2025 |
| Logopedisti — Itália | ~15 mil inscritos (24/100 mil hab.), entrevista da presidente da Commissione d'albo | https://www.quotidianosanita.it/lavoro-e-professioni/il-nostro-viaggio-tra-le-professioni-sanitarie-i-logopedisti-intervista-alla-presidente-tiziana-rossetto/ | Sem data exata → VERIFICAR |
| Podologi — Itália | ~2.401 inscritos (audição na Câmara, nov/2024, Assoc. Italiana Podologi) | https://documenti.camera.it/leg19/documentiAcquisiti/COM12/Audizioni/leg19.com12.Audizioni.Memoria.PUBBLICO.ideGes.51507.26-11-2024-10-46-55.199.pdf | Fonte associativa |
| Fono / TO — Colômbia (ReTHUS) | não encontrado | — | VERIFICAR (Observatorio de Talento Humano MinSalud) |
| TO — Itália, EUA (AOTA) | não encontrado | — | VERIFICAR |

## VERIFICAR (lista final)
(preenchendo)
