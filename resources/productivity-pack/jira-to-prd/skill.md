# jira-to-prd

## Objetivo
Transformar demanda bruta em PRD funcional, claro, estruturado e revisável.

## Entradas aceitas
- ID de card Jira
- descrição manual
- XML
- screenshots
- links Figma
- comentários do usuário
- regras de negócio complementares
- contexto técnico

## Regras
- Não implementar código.
- Não gerar plano técnico completo.
- Não gerar tasks.
- Não inventar regra de negócio.
- Não assumir comportamento sem evidência.
- Quando faltar informação, marcar como `Informação não confirmada`.

## Saída esperada
Criar arquivo markdown em:

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
