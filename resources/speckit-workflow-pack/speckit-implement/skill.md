# speckit-implement

## Objetivo
Executa as tasks da tasks.md, fase por fase, marcando [X] conforme conclui.

## Quando usar
Use esta skill dentro do fluxo SDD/Speckit, após a etapa anterior estar revisada.

## Comportamento
Implementar apenas o que está em tasks.md. Parar se uma task crítica falhar ou se houver inconsistência com spec/plan.

## Regras
- Não inventar regra de negócio.
- Não pular etapa do fluxo.
- Não implementar antes de existir spec, plan e tasks.
- Marcar explicitamente dúvidas e ambiguidades.
- Preservar rastreabilidade entre PRD, spec, plan, tasks e implementação.

## Artefatos esperados
```text
specs/<feature>/
  spec.md
  plan.md
  data-model.md
  tasks.md
  research.md
  contracts/
  checklists/
```

## Critério de qualidade
A saída deve ser revisável por humanos e permitir que outro desenvolvedor entenda a motivação, o escopo e o próximo passo sem depender de conversa solta.
