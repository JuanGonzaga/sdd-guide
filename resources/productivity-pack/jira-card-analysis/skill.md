# jira-card-analysis

## Objetivo
Organizar o contexto de um card Jira informado pelo usuário.

## Entradas aceitas
- ID completo: `IMC-1222`
- número isolado: `1222`
- texto com número: `card 1222`, `issue 1222`, `ticket 1222`
- prefixo diferente quando informado explicitamente

## Regras
- Nunca inventar ID.
- Nunca implementar apenas com base no card.
- Nunca inventar descrição, critério de aceite, branch ou regra de negócio.
- Nunca exibir tokens, senhas ou credenciais.
- Se não houver acesso ao Jira, pedir que o usuário cole o conteúdo do card.

## Fluxo
1. Normalizar ID do card.
2. Buscar título, status, descrição, comentários, anexos e links.
3. Converter ADF para texto quando necessário.
4. Identificar critérios de aceite.
5. Separar dúvidas e ambiguidades.
6. Retornar resumo estruturado.

## Saída

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
