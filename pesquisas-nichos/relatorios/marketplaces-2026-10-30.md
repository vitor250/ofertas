# Marketplaces onde o público já compra (30/10/2026)

## 0. Limites (ler primeiro)
- **Cobertura parcial e rasa.** WebSearch devolve só blogs; a maior parte veio de buscas ao vivo no navegador embutido (aba própria, já fechada). Etsy NÃO foi tocado (bloqueado, 403, ver lojas-sem-anuncio-2026-10-30.md).
- **Bloqueados / sem acesso (parei, não contornei):** Mercado Livre (exige login), Shopee BR (exige login/anti-tráfego), Amazon IT, DE e ES (página de erro anti-robô), TPT via WebFetch (403; pelo navegador funcionou), Kiwify e Eduzz (não têm marketplace público com busca: /marketplace dá 404). Digistore24 não testado (sem tempo/prioridade). Amazon BR na categoria "Livros" para nutricionista: 0 resultados.
- **Sem dado de vendas.** Só preço, nota e nº de avaliações. Avaliações não são vendas.
- **Não conferi anúncios** dos vendedores citados (sem SearchAPI até 08/11; conector Meta não usado). Tudo é VERIFICAR antes de chamar de concorrente.
- Gumroad e Payhip: a busca interna devolve lixo irrelevante (ver 2.3), então a leitura é "ninguém relevante", não "mercado vazio".

## 1. Ranking (0 a 10) do que esta rodada mostra
| # | Achado | Nota | Evidência | Status |
|---|---|---|---|---|
| 1 | **Hotmart fora do BR é só o catálogo BR traduzido** (IT, FR, EN mostram os mesmos vendedores, preço em BRL). Zero produto nativo de kit profissional em italiano, francês ou inglês | 8 | Buscas "dentista modelli" (IT), "dentiste modèles" (FR), "dentist forms" (EN): só resultados BR traduzidos, crochê, modelos de carro e moda; nenhum kit odontológico italiano/francês nativo | BRECHA (Hotmart não é canal de concorrência em IT/FR/EN) |
| 2 | **Amazon México: dentista e psicólogo sem produto digital/kit** | 7 | "formatos consultorio dental expediente clínico": 1 "Expediente Clínico Odontológico" impresso a MXN 429 + acessórios; psicólogo (livros): 0 resultados | BRECHA no marketplace; demanda real do MX já vem de anúncio (ver psicologo-mexico) |
| 3 | **Amazon EUA dentista: o que vende é formulário IMPRESSO e pacote de conformidade caro** | 6 | Registration forms book US$ 9,99; ADA claim forms US$ 22 a 40; **OSHA Documentation Package for Dental Offices US$ 350 (5,0, 2 aval.)** e **OSHA & HIPAA package US$ 560**, com manual impresso, USB editável e suporte. Mostra que dentista EUA paga US$ 350+ por pacote de norma | TESTE de preço alto para pacote de norma (EUA); não é nosso mercado |
| 4 | **Amazon EUA terapeuta: livros de notas já têm tração** | 5 | "Stress-Free Documentation for Mental Health Therapists" US$ 39,91, 4,6 (140); "Progress Notes Protocols Bible" US$ 34,99, 4,7 (83); cadernos SOAP/DAP US$ 6,90 a 14,99 (1 a 5 aval.) | PROVADO em EN (livro/caderno), saturado em cadernos baratos |
| 5 | **Amazon EUA veterinário: manual operacional e formulários impressos** | 5 | "Veterinary Clinic Management Binder" US$ 35,88; fichas Doctor Stuff US$ 30 a 62 (3 aval.); intake book US$ 9,99 | TESTE (demanda fraca em avaliações) |
| 6 | **Amazon BR psicólogo: livros de modelos já vendem** | 4 | "Laudo Psicológico e Outros Documentos Técnicos" R$ 67,88, nota 4,8 (**293 aval.**, o mais forte do achado); "Modelos de documentos Psicológicos" R$ 103,49 (4,4; 19); versão R$ 34,90 sem aval. Três e-books gratuitos de IA para prontuário (R$ 0). Confirma psicólogo BR como saturado e que o público paga ~R$ 35 a R$ 100 por modelos | SATURADO BR (já constava) |
| 7 | **Amazon BR dentista: nada** | 6 | "kit documentos dentista": só capinhas de documento, pastas e fotografia odontológica; nenhum livro/kit de documentos | BRECHA no marketplace (Hotmart BR já tem kits, ver relatório anterior) |
| 8 | **TPT (EUA): SLP/OT/psicólogo escolar vendem barato, volume por avaliação alto** | 4 | Consultation Forms SLP (Speech Dreams) US$ 4,00, 4,9 (**184 aval.**); SOAP Note Generator US$ 7; planilha de notas OT/PT/SLP; templates de laudo OT US$ 3 a 10 com 0 a 2 aval.; psicólogo escolar US$ 3 a 9,50, 1 aval. cada. Ticket mínimo; só o SLP tem um item de tração | PROVADO em EN para SLP, ticket baixo; não serve para nosso preço |
| 9 | **Gumroad e Payhip: sem vendedor relevante de kit profissional** | 3 | Gumroad "dental forms", "clinic templates", "speech therapy" devolveram livro de finanças, homeopatia, notas ENT (4,1; 9 aval.); Payhip "therapist": 1 loja irrelevante | Baixa evidência (busca interna fraca): VERIFICAR com consulta direta de lojas |

## 2. Detalhe por marketplace

### 2.1 Hotmart em outras línguas (IT, FR, EN)
- É o mesmo catálogo BR com a interface traduzida: preços em BRL, vendedores brasileiros.
- Itens úteis vistos: "Modelli del Consulente" (Matias Ezequiel Parodi, BRL 60, 15 modelos), **"Cartella Clinica TCC: Modelli Modificabili" (NeuroKit Clínico, BRL 65,52)**, "Pack de modèles d'anamnèse personnalisés" (Académie Lympha, BRL 65,52), Pack Canva Pediatria BRL 80 e Terapia BRL 100, "Therapy Form Packet" (Proteina Digital, BRL 100,65), "Pack Dentist" (Alex Camargo, BRL 40,85, 5,0 com 1 aval.), "The Millionaire Dentist Checklist" BRL 29,01. São títulos em tradução automática de produtos BR; não provam vendas em IT/FR/EN.
- Conclusão: Hotmart não concorre em IT/FR/EN; o concorrente nesses países é anúncio + site próprio (ver pesquisa-europa).

### 2.2 Amazon (livros e físicos)
- EUA (US$): dentista, terapeuta, veterinário e nutricionista em tabela acima. Nutricionista: só cadernos US$ 4,99 a 13,99 e "Health Coach Intake Forms" US$ 9,99 (sem avaliação); nada de kit estruturado.
- BR: psicólogo tem 2 a 3 livros de modelos com tração; dentista e nutricionista (livros) nada.
- México: dentista só ficha impressa MXN 429.
- IT, DE, ES: bloqueado, **VERIFICAR** (tentar KDP/Kindle por outro caminho depois).

### 2.3 Gumroad, Payhip, TPT
- Gumroad: busca client-side; consultas de profissão devolvem itens fora do nicho. Preços aparecem em BRL (R$ 683,91 etc.).
- Payhip: busca interna devolve uma loja irrelevante. Blogs de vendedores (mjresell) só falam de nichos genéricos (planners, contratos).
- TPT: ver item 8 acima. Nichos escolares (SLP, OT, psicólogo escolar, orientador) com muitos vendedores a US$ 3 a 20.

### 2.4 Não cobertos nesta rodada
Mercado Livre, Shopee, Kiwify, Eduzz, Digistore24, Amazon IT/DE/ES/FR, Etsy fora do inglês. Motivo: login obrigatório, anti-robô ou ausência de busca pública.

## 3. Lista final de VERIFICAR
1. Amazon IT/DE/ES/FR por outro caminho (KDP): quem vende "modulistica/Vorlagen/plantillas" por profissão e a que preço.
2. Mercado Livre e Shopee BR com login do próprio usuário (kits de documentos Word por profissão; vendas "+X vendidos" aparecem ali).
3. Lojas diretas no Gumroad/Payhip dos vendedores que já aparecem no Etsy (PrintyPin, TheTemplateShopAndCo etc.).
4. Pacote OSHA de dentista EUA (US$ 350 a 560): confirmar se é vendedor ativo e se anuncia (referência de teto de preço para pacote de norma).
5. NeuroKit Clínico (Cartella Clinica TCC), Académie Lympha, Alex Camargo no Hotmart: ver páginas de venda, bumps e anúncios.
6. Digistore24 (DE/FR/IT): ainda não olhado.
7. Etsy: 20 buscas pendentes do relatório anterior continuam bloqueadas.

## 4. Diferença em relação à versão anterior (lojas-sem-anuncio)
- Novo: Hotmart IT/FR/EN é espelho do BR (brecha para entrada nativa).
- Novo: referência de preço alto de pacote de norma (OSHA dental US$ 350 a 560) e de livros de documentação de terapeuta (US$ 35 a 40, 83 a 140 aval.).
- Novo: Amazon BR psicólogo com 293 avaliações em um livro de modelos (confirma saturação BR).
- Sem mudança: ranking de brechas do relatório anterior (IT/DE/FR/PL kit pago nativo segue a maior).
