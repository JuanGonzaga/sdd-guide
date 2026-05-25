# pr-review-diff

## Objetivo
Revisar PR com base em diff real.

## Fluxo
1. Atualizar referências remotas.
2. Comparar branch atual com branch base.
3. Listar arquivos alterados.
4. Entender intenção da mudança.
5. Procurar bugs, regressões e impactos colaterais.
6. Sugerir testes manuais.

## Checklist
- regra de negócio quebrada
- condição invertida
- null safety
- array vazio
- query perigosa
- SQL injection
- falta de bind
- multi-tenant
- compatibilidade com versão do PHP
- JS legado quebrando tela/modal/grid
- mudança que afeta fluxo antigo
- duplicação aceitável vs abstração desnecessária
- nomes confusos

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
