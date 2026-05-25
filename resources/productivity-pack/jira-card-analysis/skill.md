# jira-card-analysis

## Objetivo
Dado um ID de card Jira informado pelo usuário, buscar e organizar o contexto do card autonomamente.

## Entradas aceitas
- `IMC-1222`
- `1222`
- `card 1222`
- `issue 1222`
- prefixos diferentes, se informados explicitamente

## Regras
- Nunca inferir ID se o usuário não informou número.
- Nunca implementar nada apenas com base no card.
- Nunca inventar descrição, critério de aceite, branch ou regra de negócio.
- Nunca exibir tokens, senhas ou credenciais.
- Se não conseguir acessar o Jira, informar o erro e pedir para o usuário colar o conteúdo do card.

## Fluxo
1. Normalizar ID.
2. Buscar dados do card.
3. Converter descrição e comentários para texto.
4. Verificar anexos, links, subtasks e comentários relevantes.
5. Retornar análise estruturada.

## Saída esperada

## Card
ID:
Título:
Status:
Tipo / Prioridade / Componente:
Assignee / Reporter:
Criado / Atualizado / Due:

## Resumo

## Requisitos

## Critérios de aceite

## Comentários relevantes

## Impacto técnico provável

## Pontos de atenção

## Próximo passo recomendado
