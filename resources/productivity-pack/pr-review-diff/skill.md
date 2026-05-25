# pr-review-diff

## Objetivo
Revisar PR de verdade, usando diff.

## Comportamento
1. Fazer git fetch.
2. Comparar branch atual com master/main ou branch informada.
3. Rodar git diff.
4. Listar arquivos alterados.
5. Entender intenção da mudança.
6. Procurar bugs, regressões, inconsistências e impactos colaterais.

## Checklist
- regra de negócio quebrada
- condição invertida
- tratamento de null/array vazio
- query perigosa
- SQL injection/string concat
- falta de bind
- multi-tenant/licença
- compatibilidade com versão do PHP
- JS legado quebrando tela/modal/grid
- mudança que afeta fluxo antigo
- duplicação aceitável vs abstração desnecessária
- nomes confusos
- testes manuais necessários

## Formato de saída

Resumo geral:
Risco do PR: baixo / médio / alto

Problemas encontrados:
1. [Alto] Arquivo X
   Problema:
   Impacto:
   Sugestão:

Pontos positivos:
- ...

Testes recomendados:
- Cenário 1
- Cenário 2
