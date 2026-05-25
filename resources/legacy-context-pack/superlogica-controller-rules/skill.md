# superlogica-controller-rules

## Objetivo
Garantir que controllers sejam finos: recebem parâmetros, delegam para Service/Helper e retornam resposta padronizada.

## Quando usar
Ao criar ou editar qualquer arquivo em `Controllers/`.

## Regras
- Controller não deve conter regra de negócio.
- Controller não deve acessar banco diretamente.
- Controller não deve instanciar Repository diretamente.
- Controller deve delegar para Service ou Helper.
- Controller deve retornar resposta padronizada.
- Não usar `$_GET`, `$_POST` ou `$_REQUEST` diretamente.

## Exemplo de estrutura

```php
public function indexAction() {
    $params = array_shift($this->_request->getParam('todos'));

    $service = Services_Contratos_Contrato::initServiceContrato();
    $dados = $service->getDados($params);

    return Superlogica_Response::success($dados);
}
```

## Anti-patterns
- `echo`, `print_r`, `var_dump`, `die`
- SQL dentro do controller
- validações complexas dentro da action
- retorno de array cru
- controller grande demais

## Checklist
- [ ] Recebe parâmetros pelo padrão do framework
- [ ] Delega para Service/Helper
- [ ] Retorna resposta padronizada
- [ ] Não contém regra de negócio
- [ ] Não acessa banco diretamente
