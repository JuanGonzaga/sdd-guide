# superlogica-service-repository

## Objetivo
Garantir que Services e Repositories sigam o padrão exato do projeto.
Service = lógica de negócio. Repository = acesso a dados. Nunca misturar.

## Services

### Estrutura básica
```php
class Services_Contratos_Contrato {

    private $repositoryContrato;

    public function __construct(
        Repositories_Contratos_Contrato $repositoryContrato
    ) {
        $this->repositoryContrato = $repositoryContrato;
    }

    public static function initServiceContrato(): Services_Contratos_Contrato {
        return new Services_Contratos_Contrato(
            new Repositories_Contratos_Zend_Contrato()
        );
    }
}
```

### Regras
- Service valida regra de negócio.
- Service delega persistência ao Repository.
- Service não monta SQL diretamente.
- Exceptions devem seguir o padrão do projeto.

## Repositories

### Estrutura
```text
Repositories/<Grupo>/
├── <Entidade>.php
└── Zend/
    └── <Entidade>.php
```

### Interface
```php
interface Repositories_Contratos_Contrato {
    public function buscarPorId($id);
}
```

### Implementação
```php
class Repositories_Contratos_Zend_Contrato
    implements Repositories_Contratos_Contrato {

    public function buscarPorId($id) {
        $model = new Models_Contratos();
        $select = $model->select()
            ->from('CONTRATOS', array('ID_CONTRATO_CTR'))
            ->where('ID_CONTRATO_CTR = ?', $id);

        $row = $model->fetchRow($select);
        return $row ? $row->toArray() : array();
    }
}
```

## Anti-patterns proibidos
- Service sem factory method
- Repository sem interface
- SQL string concatenada
- Lógica de negócio no Repository
- Acesso à session dentro do Repository
- Filtro manual de tenant quando o framework já resolve
