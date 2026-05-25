# legacy-project-context

## Objetivo
Impedir que o Claude Code invente arquitetura, regra ou padrão em projetos legados.

## Princípio central
O projeto já tem exemplo de quase tudo. Antes de propor qualquer solução, o agente deve buscar referências reais no código existente e seguir o padrão observado.

## Quando usar
Use esta skill antes de implementar qualquer demanda em monorepos, sistemas legados ou projetos com padrões internos consolidados.

## Regras obrigatórias
- Não inventar padrão quando existe código parecido.
- Não modernizar o legado sem necessidade.
- Não refatorar código adjacente sem autorização.
- Não criar camada, abstração ou biblioteca nova sem justificativa.
- Não assumir regra de negócio sem evidência.
- Se não encontrar referência confiável, parar e pedir orientação.

## Fluxo recomendado
1. Entender a demanda.
2. Buscar exemplos parecidos no código.
3. Citar arquivos de referência.
4. Explicar o padrão encontrado.
5. Só depois propor implementação.

## Padrões esperados
- Controller recebe HTTP e delega.
- Service concentra regra de negócio.
- Repository concentra acesso a dados.
- Model representa persistência.
- Testes e validações devem respeitar o padrão do projeto.

## Checklist
- [ ] Li o contexto da demanda
- [ ] Busquei referência no código
- [ ] Evitei modernização desnecessária
- [ ] Expliquei riscos
- [ ] Listei arquivos impactados
