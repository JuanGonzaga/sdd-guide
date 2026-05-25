# superlogica-frontend-flow

## Objetivo
Garantir que Forms, Grids, modais e JavaScript sigam os padrões do projeto.
O frontend legado é PHP-driven: comportamentos são declarados no PHP, não em JS solto.

## Forms

```php
class Forms_Contratos_Detalhes extends Superlogica_Form {

    public function init() {
        parent::init();

        $location = new Superlogica_Location();
        $location->setController('contratos')
                 ->setAction('editar')
                 ->setApi(false);

        $this->addAttribs(array(
            'action' => $location->toString(),
            'method' => 'put',
            'aposCarregar' => 'Form.carregarComissionados'
        ));
    }
}
```

## Comportamentos JS
```php
'comportamentos' => 'Form.formatar Form.numeric'
```

## Grids
```php
class Grids_Contratos extends Superlogica_Js_Grid {

    public function __construct($dados) {
        parent::__construct($dados);

        $this->_colunas = array(
            'cliente' => array(
                'label' => 'Cliente',
                'tamanho' => '25%',
            ),
        );
    }
}
```

## Modais
Usar o padrão do framework:
- form renderizado em div oculta
- botão abre via `addFormDialog`
- não criar modal Bootstrap ou modal manual

## JavaScript
Usar classes do framework quando existirem.

```javascript
var Grids_Contratos = new Class({
    Extends: Superlogica_Js_Grid,

    _formatarColunaCliente: function(dados) {
        return '<b>' + dados.nome + '</b>';
    }
});
```

## Anti-patterns
- Lógica de negócio em JS
- Submit manual via $.ajax quando o form já resolve
- Modal Bootstrap/manual
- JS inline em .phtml
- Reinventar grid/form
