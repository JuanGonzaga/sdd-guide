# superlogica-encoding-safe

## Objetivo
Evitar corrupção de dados por conversão incorreta de encoding.
Muitos arquivos legados podem estar em ISO-8859-1.

## Regra principal
Nunca converter encoding de um arquivo sem autorização explícita.

Se o arquivo está em ISO-8859-1, edite em ISO-8859-1.
Se está em UTF-8, edite em UTF-8.

## Identificar encoding

```bash
file arquivo.php
```

## Editando arquivo existente
- Manter o mesmo encoding.
- Não reescrever o arquivo inteiro sem necessidade.
- Não misturar encodings.

## Criando arquivo novo
- Verificar encoding dos arquivos vizinhos.
- Criar no mesmo padrão do módulo.

## JSON/API
Antes de retornar dados ISO em JSON, converter conforme padrão do projeto.

## Anti-patterns
- Salvar arquivo ISO como UTF-8 sem autorização
- Usar iconv/mb_convert_encoding sem certeza do encoding
- Adicionar declare encoding em arquivo legado
- Remover mb_internal_encoding de código que já usa

## Checklist
- [ ] Verifiquei o encoding
- [ ] Mantive o encoding original
- [ ] Não corrompi strings com acentos
