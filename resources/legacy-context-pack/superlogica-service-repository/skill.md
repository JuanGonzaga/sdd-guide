# superlogica-service-repository

## Objetivo
Separar regra de negócio de acesso a dados.

Service = regra de negócio.
Repository = acesso a dados.

## Quando usar
Ao criar ou editar arquivos em `Services/` ou `Repositories/`.

## Service
Responsabilidades:
- validar regra de negócio
- validar permissões quando aplicável
- coordenar fluxo
- chamar repositories
- preparar resposta para controller

## Repository
Responsabilidades:
- montar query
- chamar API externa quando aplicável
- persistir dados
- retornar dados crus ou estruturados
- não decidir regra de negócio

## Estrutura sugerida

```text
Services/<Grupo>/<Entidade>.php

Repositories/<Grupo>/
├── <Entidade>.php
└── Zend/
    └── <Entidade>.php
```

## Exemplo de Service

```php
class Services_Contratos_Contrato {

    private $repositoryContrato;

    public function __construct(
        Repositories_Contratos_Contrato $repositoryContrato
    ) {
        $this->repositoryContrato = $repositoryContrato;
    }

    public static function initServiceContrato() {
        return new Services_Contratos_Contrato(
            new Repositories_Contratos_Zend_Contrato()
        );
    }
}
```

## Anti-patterns
- Service montando SQL
- Repository validando regra de negócio
- Repository sem interface
- Service sem factory method
- Acesso à session dentro do Repository
- SQL string concatenada
