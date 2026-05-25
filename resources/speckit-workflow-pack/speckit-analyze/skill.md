# speckit-analyze

## Objetivo
Audita consistência entre spec, plan e tasks.

## Quando usar
Use dentro do fluxo SDD/Speckit, respeitando a ordem das etapas.

## Comportamento
Encontrar contradições, lacunas e tarefas sem requisito correspondente.

## Regras
- Não inventar regra de negócio.
- Não pular etapa do fluxo.
- Não implementar antes de existir spec, plan e tasks.
- Registrar dúvidas explicitamente.
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
A saída deve ser revisável por humanos e permitir que outro desenvolvedor entenda motivação, escopo, decisões e próximo passo.
