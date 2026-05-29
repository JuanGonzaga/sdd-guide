# Claude Code + SDD + Speckit

Landing page interativa para apresentar um fluxo de desenvolvimento com IA baseado em Claude Code, Specification-Driven Development (SDD), Speckit e skills customizadas.

## Objetivo

Mostrar como transformar o uso de IA em um processo mais previsível, rastreável e revisável.

A apresentação cobre:

- problema de usar IA sem método
- Claude Code como agente operacional
- SDD como método de trabalho
- Speckit como pipeline executável
- skills de contexto para projetos legados
- fluxo de PRD, spec, plan, tasks, implement e review
- packs de skills para download
- módulo avançado de Claude Code: sandbox, hooks, memory, permissions, agents, MCP, cache e automações

## Estrutura

```text
.
├── index.html
├── README.md
└── resources/
    ├── legacy-context-pack.zip
    ├── speckit-workflow-pack.zip
    └── productivity-pack.zip
```

## Packs disponíveis

### Legacy Context Pack

Skills para orientar o Claude Code em projetos legados:

- legacy-project-context
- superlogica-controller-rules
- superlogica-service-repository
- superlogica-db-conventions
- superlogica-frontend-flow
- superlogica-encoding-safe

### Speckit Workflow Pack

Skills para executar o fluxo SDD:

- speckit-specify
- speckit-clarify
- speckit-plan
- speckit-tasks
- speckit-implement
- speckit-analyze
- speckit-checklist
- speckit-constitution
- speckit-taskstoissues

### Productivity Pack

Skills para produtividade no dia a dia:

- jira-card-analysis
- jira-to-prd
- pr-review-diff

Também inclui o helper `parse_adf.py`.

## Como publicar no GitHub Pages

1. Suba `index.html`, `README.md` e a pasta `resources/` na raiz do repositório.
2. Vá em **Settings → Pages**.
3. Configure:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root`
4. Salve e aguarde a publicação.

## Como instalar uma skill localmente

```bash
mkdir -p ~/.claude/skills
```

Exemplo de estrutura:

```text
~/.claude/skills/
  legacy-project-context/
    skill.md
```

Depois abra o Claude Code dentro do projeto:

```bash
claude
```

## Módulo avançado

A seção **Claude Code avançado** apresenta recursos que ajudam o time a operar com mais segurança e produtividade:

- `/sandbox`
- `CLAUDE.md` e memory
- hooks
- permissions
- `/compact`
- agents/subagents
- MCP
- cache
- automações via CLI

A ideia é mostrar que Claude Code não precisa ser usado apenas como chat de código. Ele pode funcionar como um ambiente operacional com contexto, regras, isolamento e automações.

## Stack

Projeto estático simples:

- HTML
- CSS
- JavaScript puro

Não há dependências externas.
