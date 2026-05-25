# speckit-clarify

## Objetivo
Identifica gaps na spec e faz perguntas cirúrgicas para fechar ambiguidades.

## Quando usar
Use esta skill dentro do fluxo SDD/Speckit, após a etapa anterior estar revisada.

## Comportamento
Ler spec.md, encontrar lacunas e fazer até 5 perguntas objetivas. Não planejar implementação antes das respostas.

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
