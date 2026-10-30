# Refazer: arbitragem de kits brasileiros validados para outros países

Ler antes: `3 - EU/pesquisas/arbitragem-kits-br-2026-10-29.md` (dias medidos pelo anúncio mais antigo de amostra de 50; preços estimados).
Partir do `escalalow-ofertas-validadas.json` (em `3 - EU/pesquisas/brechas-europa-2026-10-28/`). Para cada tipo de kit (receitas diabéticos, estimulação cognitiva, fichas de terapia infantil, catequese, atividades, alfabetização, quadros elétricos, STL, costura) varrer PT-PT, ES, IT, FR, DE, PL, RO, CZ, GR, EN. Medir por page_id os dias reais (Editura Gold, CareTable, ABA Tools, Catechesi 360, Mister Shop, Tłuste Gary) e trocar toda estimativa 'est.' por preço real.

## Saída
Salvar em `3 - EU/pesquisas/arbitragem-kits-br-v2-2026-10-30.md`, gravando aos poucos, com ranking 0–10 e lista final de VERIFICAR.

## Regras comuns (valem para todo agente)
- Data de referência: 30/10/2026. Idioma do relatório: português do Brasil.
- Contexto: o usuário vende kits low ticket de documentos + app por profissão (ex.: La Valigetta del Dentista IT €27/€19; Maletín del Psicólogo MX). Quer PEGAR TODAS AS BRECHAS: o que vende e ainda não é vendido, ou só há pouco, em cada país/idioma.
- Fora do escopo: harmonização facial e injetáveis.
- Régua: PROVADO = vendedor com anúncio ativo há 30+ dias NO país/idioma/moeda. TESTE = sinal sem vendedor antigo. PRAZO = gancho com data de norma. BRECHA = ninguém vende. Espanhol neutro não prova país.
- Ferramentas: `ads_library_search` (conector Meta, só anúncios ativos); consulte por `page_id` para medir DIAS REAIS, nº de anúncios e moeda. Use o SearchAPI quando o conector faltar (ver memory/pesquisa-europa.md e `medir.py`); se estiver sem crédito (zerado até 08/11), avise e siga com o conector.
- Abra a página de vendas dos vendedores relevantes (navegador embutido ou WebFetch) para PREÇO, plataforma, conteúdo, bumps e garantia. Não compre nada nem preencha formulários.
- Confirme tamanho de mercado e normas por busca web, com fonte oficial e URL.
- Nunca invente. O que não confirmar vai marcado VERIFICAR. Grave o arquivo de saída aos poucos para não perder se algo parar.
- Resposta final ao usuário: resumo curto (top da lista e diferenças em relação à versão anterior, se houver).
