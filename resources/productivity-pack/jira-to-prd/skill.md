# jira-to-prd

## Objetivo
Transformar informações brutas de uma demanda em um PRD funcional claro, estruturado e revisável para uso manual posterior.

## Entradas aceitas
- ID de card Jira
- número isolado
- XML
- screenshots
- links Figma
- comentários do usuário
- regras de negócio complementares
- contexto manual

## Dependências
Quando um ID de card Jira for informado, usar primeiro a skill `jira-card-analysis`.

## Regras obrigatórias
- Não implementar código
- Não gerar plan.md
- Não gerar tasks.md
- Não criar solução técnica completa
- Não inventar regra de negócio
- Não assumir comportamento sem evidência
- Se faltar informação, marcar como `Informação não confirmada`

## Saída
Criar um arquivo markdown em:

```text
~/SDD/PRD-<CARD>.md
```

## Template

# PRD — <ID> — <Título>

## 1. Contexto
## 2. Objetivo
## 3. Problema atual
## 4. Comportamento esperado
## 5. Regras de negócio
## 6. Fluxo do usuário
## 7. Dados e integrações
## 8. XML / payloads relacionados
## 9. Referências de Figma
## 10. Critérios de aceite
## 11. Cenários de validação
## 12. Cenários de erro
## 13. Premissas
## 14. Dúvidas em aberto
## 15. Fora de escopo
## 16. Próximo passo recomendado

## Encerramento
Revise este PRD manualmente antes de seguir para o fluxo do Speckit.
