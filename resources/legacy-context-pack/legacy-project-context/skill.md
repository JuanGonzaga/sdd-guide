Objetivo: impedir o Claude de "lançar moda" em código legado.

Aplicar em: projetos legados PHP/Zend com arquitetura própria, regras de negócio complexas e padrões já consolidados.

Stack de referência:
- PHP 7.2.x
- Zend Framework 1 customizado
- MySQL com convenção de nomes própria
- Frontend legado com Mootools, jQuery UI e classes JS internas
- Logging via helpers internos
- Multi-tenant com filtro automático em models compartilhados
- Encoding legado com arquivos ISO-8859-1 em alguns módulos

Princípio central:
O projeto já tem exemplo de quase tudo. Não inventar — encontrar e reusar.
Trabalhar dentro das limitações do legado, não contra elas.

Antes de propor solução:
1. Entender exatamente o que precisa ser feito.
2. Buscar referência no código existente.
3. Seguir o padrão observado.
4. Se não encontrar referência, parar e pedir orientação.

Não usar em PHP 7.2:
- typed properties
- arrow functions
- enums
- readonly
- constructor promotion
- match
- named arguments
- str_contains / str_starts_with / str_ends_with
- nova lib, novo framework ou abstração genérica desnecessária

Não fazer sem autorização explícita:
- converter encoding de arquivo
- refatorar código adjacente
- extrair classes ou métodos "enquanto está aqui"
- adicionar type hints em código que não os tem

Toda sugestão de código deve apontar:
- arquivo de referência
- trecho parecido
- motivo da escolha

Padrões arquiteturais:
- Controller → Service → Repository → Model
- Service instanciado via factory method estático
- Repository com interface + implementação concreta
- Respostas padronizadas
- Exceptions padronizadas
- Multi-tenant via mecanismo automático do projeto
