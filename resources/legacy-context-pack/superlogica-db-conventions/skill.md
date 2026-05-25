# superlogica-db-conventions

## Objetivo
Garantir que queries, nomes de tabela, nomes de coluna e acesso ao banco sigam as convenções do projeto.

## Convenção de nomenclatura

| Prefixo | Tipo |
|---------|------|
| ST_ | String / Varchar |
| ID_ | Inteiro / FK |
| DT_ | Date / Datetime |
| FL_ | Flag / Boolean |
| NM_ | Numérico |
| VL_ | Valor monetário |
| TX_ | Texto longo |
| BL_ | Binário |

Todo campo deve terminar com a abreviação da tabela.

Exemplos:
- `ID_CONTRATO_CTR`
- `ST_NOME_CLI`
- `DT_VENCIMENTO_CBR`
- `VL_DESCONTO_CBR`

## Tabelas
Tabelas devem seguir o padrão MAIÚSCULO com underline.

```sql
SELECT * FROM CONTRATOS_SEGUROS
```

## Queries
Usar query builder / Zend_Db_Select.

```php
$select = $model->select()
    ->from('CONTRATOS', array('ID_CONTRATO_CTR', 'ST_NUMERO_CTR'))
    ->where('FL_ATIVO_CTR = ?', 1);
```

## Nunca fazer
```php
$sql = "SELECT * FROM CONTRATOS WHERE ID_STATUS_CTR = " . $status;
```

## Anti-patterns
- Inventar nome de coluna
- SQL string concatenada
- Filtro manual de tenant
- SELECT * em produção
- Lógica de negócio no Model
- Tabelas em minúsculo
