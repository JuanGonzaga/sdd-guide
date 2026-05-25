# superlogica-db-conventions

## Objetivo
Garantir que queries, tabelas e colunas sigam convenções do projeto.

## Prefixos comuns

| Prefixo | Uso |
|---|---|
| ST_ | String / texto curto |
| ID_ | Identificador / FK |
| DT_ | Data / datetime |
| FL_ | Flag / boolean |
| NM_ | Número / quantidade |
| VL_ | Valor monetário |
| TX_ | Texto longo |
| BL_ | Binário |

## Regras
- Não inventar nome de campo.
- Conferir campos existentes antes de usar.
- Usar query builder quando for o padrão do projeto.
- Usar bind em filtros.
- Evitar `SELECT *` em código de produção.
- Não concatenar variável em SQL.
- Respeitar multi-tenant pelo mecanismo do framework.

## Exemplo

```php
$select = $model->select()
    ->from('CONTRATOS', array('ID_CONTRATO_CTR', 'ST_NUMERO_CTR'))
    ->where('FL_ATIVO_CTR = ?', 1);
```

## Anti-pattern

```php
$sql = "SELECT * FROM CONTRATOS WHERE ID_STATUS_CTR = " . $status;
```

## Checklist
- [ ] Verifiquei os campos reais
- [ ] Usei bind
- [ ] Evitei SQL concatenado
- [ ] Respeitei multi-tenant
- [ ] Listei campos explicitamente
