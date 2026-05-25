# superlogica-controller-rules

## Objetivo
Garantir que controllers sigam o padrão exato do projeto. Controllers são finos:
recebem HTTP, delegam, retornam. Toda lógica vai para Service ou Helper.

## Quando usar
Ao criar ou editar qualquer arquivo em `Controllers/`.

## Estrutura obrigatória

### Herança
```php
class ContratosController extends Superlogica_Controller_Action
```

Nunca estender `Zend_Controller_Action` diretamente.

### Recebimento de parâmetros
```php
$params = array_shift($this->_request->getParam('todos'));
```

Parâmetros chegam encapsulados em `todos`. Nunca usar `$_GET`, `$_POST` diretamente.

### Actions por verbo HTTP
```php
public function indexAction()
public function postAction()
public function putAction()
public function deleteAction()
public function sincronizarAction()
```

### Delegação obrigatória
```php
public function indexAction() {
    $params = array_shift($this->_request->getParam('todos'));

    $service = Services_Contratos_Contrato::initServiceContrato();
    $dados = $service->getDados($params);

    return Superlogica_Response::success($dados);
}
```

## Anti-patterns proibidos
- Lógica de negócio no controller
- Acesso direto ao banco dentro do controller
- `echo`, `print_r`, `var_dump` ou `die()` em produção
- Retornar array cru sem resposta padronizada
- Instanciar Repository diretamente no controller
- Usar `$_GET`, `$_POST`, `$_REQUEST`

## Checklist
- [ ] Parâmetros recebidos via request do framework
- [ ] Controller delega para Service ou Helper
- [ ] Retorno padronizado
- [ ] Nenhuma lógica de negócio no controller
