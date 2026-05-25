# superlogica-encoding-safe

## Objetivo
Evitar corrupção de caracteres em arquivos legados.

## Regra principal
Nunca converter encoding de arquivo sem autorização.

## Quando usar
Antes de editar arquivos PHP legados, especialmente quando houver acentos, cedilha ou strings de mensagem.

## Fluxo
1. Verificar encoding do arquivo.
2. Manter o encoding original.
3. Editar apenas o necessário.
4. Conferir se caracteres especiais não foram corrompidos.

## Comando útil

```bash
file arquivo.php
```

## Regras
- Se o arquivo está em ISO-8859-1, manter ISO-8859-1.
- Se está em UTF-8, manter UTF-8.
- Não reescrever arquivo inteiro sem necessidade.
- Não usar conversão automática sem certeza da origem.

## Anti-patterns
- Salvar arquivo ISO como UTF-8 sem autorização.
- Rodar conversão em massa.
- Misturar strings de encodings diferentes.
- Alterar encoding junto com mudança de regra de negócio.

## Checklist
- [ ] Verifiquei o encoding
- [ ] Mantive o encoding original
- [ ] Não corrompi acentos
- [ ] Não fiz conversão desnecessária
