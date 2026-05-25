# superlogica-frontend-flow

## Objetivo
Garantir que Forms, Grids, modais e JavaScript sigam o padrão do projeto.

## Regras
- Não colocar regra de negócio pesada no JavaScript.
- Não reinventar modal se o framework já fornece padrão.
- Não fazer submit manual se o Form do projeto já resolve.
- Não criar JS solto quando existe classe/padrão.
- Evitar inline JavaScript em views.

## Forms
Forms devem declarar comportamento, action e método seguindo o framework.

```php
$this->addAttribs(array(
    'action' => $location->toString(),
    'method' => 'put',
    'aposCarregar' => 'Form.callback'
));
```

## Grids
Grids devem estender a classe base do projeto.

```javascript
var Grids_Contratos = new Class({
    Extends: Superlogica_Js_Grid,

    _formatarColunaCliente: function(dados) {
        return '<b>' + dados.nome + '</b>';
    }
});
```

## Modais
Usar o padrão:
- form em div oculta
- botão abre via helper do framework
- callback após salvar quando necessário

## Checklist
- [ ] Respeitei Form/Grid do projeto
- [ ] Não criei modal manual
- [ ] Não coloquei regra de negócio no JS
- [ ] Mantive callbacks padronizados
