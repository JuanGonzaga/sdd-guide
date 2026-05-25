# Claude Code + SDD + Speckit Presentation

Landing page interativa criada para apresentar ao time uma abordagem estruturada de desenvolvimento com IA utilizando **Claude Code**, **Specification-Driven Development (SDD)**, **Speckit** e skills customizadas para projetos legados.

## Objetivo

Mostrar que IA não precisa ser usada no modo "vibe coding".

A proposta aqui é transformar Claude Code em um **ambiente operacional de engenharia**, com fluxo previsível, rastreável e reutilizável.

A apresentação cobre:

- O problema de usar IA sem processo
- Como Claude Code opera
- O que é Specification-Driven Development (SDD)
- Como o Speckit transforma o processo em execução
- Uso de skills customizadas
- Fluxo Jira → PRD → Spec → Plan → Tasks → Implement → Review
- Packs reais de skills para download

---

# Estrutura do projeto

```text
.
├── index.html
├── resources/
│   ├── legacy-context-pack.zip
│   ├── speckit-workflow-pack.zip
│   └── productivity-pack.zip
```

---

# O que existe em cada pack

## Legacy Context Pack

Skills focadas em projetos legados:

- `legacy-project-context`
- `superlogica-controller-rules`
- `superlogica-service-repository`
- `superlogica-db-conventions`
- `superlogica-frontend-flow`
- `superlogica-encoding-safe`

Objetivo:

Evitar que o agente:

- invente regra de negócio
- modernize código sem necessidade
- quebre padrões internos
- corrompa encoding
- ignore convenções de banco

---

## Speckit Workflow Pack

Pipeline completo de SDD:

- `speckit-specify`
- `speckit-clarify`
- `speckit-plan`
- `speckit-tasks`
- `speckit-implement`
- `speckit-analyze`
- `speckit-checklist`
- `speckit-constitution`
- `speckit-taskstoissues`

Objetivo:

Transformar desenvolvimento orientado por especificação em processo executável.

Fluxo:

```text
PRD
 ↓
Specify
 ↓
Clarify
 ↓
Plan
 ↓
Tasks
 ↓
Implement
 ↓
Analyze / Checklist
```

---

## Productivity Pack

Skills auxiliares para acelerar trabalho diário:

- `jira-card-analysis`
- `jira-to-prd`
- `pr-review-diff`

Inclui:

- parser ADF (`parse_adf.py`)
- geração de PRD
- análise estruturada de cards
- revisão técnica de diff

---

# Como subir no GitHub Pages

## 1. Criar repositório

Exemplo:

```text
claude-code-sdd-presentation
```

---

## 2. Subir os arquivos

A estrutura precisa ficar assim:

```text
repo/
├── index.html
└── resources/
```

---

## 3. Ativar GitHub Pages

No repositório:

**Settings**
→ **Pages**

Configuração:

```text
Source: Deploy from a branch
Branch: main
Folder: /(root)
```

Salvar.

---

## 4. Acessar

GitHub irá gerar algo como:

```text
https://SEU-USUARIO.github.io/claude-code-sdd-presentation/
```

---

# Como usar internamente

A apresentação foi pensada para times que:

- começaram a usar Claude Code
- ainda trabalham com prompts soltos
- não utilizam metodologia
- sofrem com retrabalho e inconsistência

Pode ser usada como:

- onboarding técnico
- workshop interno
- playbook operacional
- base para padronização do time

---

# Instalação local das skills

Exemplo:

```bash
mkdir -p ~/.claude/skills
```

Estrutura:

```text
~/.claude/skills/
  legacy-project-context/
    skill.md

  jira-to-prd/
    skill.md

  pr-review-diff/
    skill.md

  speckit-specify/
    skill.md
```

Depois:

```bash
claude
```

---

# Segurança

Os packs incluídos nesta versão foram sanitizados.

Mesmo assim, antes de compartilhar internamente ou externamente, revise:

- URLs privadas
- e-mails corporativos
- tokens
- paths internos
- regras de negócio confidenciais
- integrações específicas da empresa

---

# Filosofia

IA sem processo acelera erro.

IA com processo acelera engenharia.

---

# Stack

Projeto simples, sem dependências:

- HTML
- CSS
- JavaScript puro

Compatível com:

- GitHub Pages
- Netlify
- Vercel
- qualquer host estático

---

# Créditos

Projeto criado para evangelização interna de desenvolvimento orientado por IA com processo, rastreabilidade e consistência.
