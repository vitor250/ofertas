# Refazer: novos nichos profissionais na Europa principal (PL, IT, FR, ES, PT, DE, RO, NL)

Ler antes: `3 - EU/pesquisas/novos-nichos-europa-2026-10-29.md` (feita só com o conector Meta; sem preço, sem texto de anúncio, tamanhos e normas sem fonte). Usar só como lista de candidatos.
Varrer país × profissão regulada (salões/estética sem injetáveis, HACCP/gastronomia, fisio, fono/ABA, veterinário, educação, aluguel de temporada, contabilidade). Medir dias reais por page_id, abrir páginas de vendas, confirmar tamanho e gancho legal com fonte.

## Saída
Salvar em `3 - EU/pesquisas/novos-nichos-europa-v2-2026-10-30.md`, gravando aos poucos, com ranking 0–10 e lista final de VERIFICAR.

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
