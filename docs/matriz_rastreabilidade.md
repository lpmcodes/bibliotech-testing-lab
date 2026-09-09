# Matriz de Rastreabilidade — BiblioTech

| Requisito | Casos de teste vinculados                                              | Coberto? |
|-----------|--------------------------------------------------------------------------|----------|
| RF01      | CT-01, CT-02, CT-03, CT-04, CT-05, CT-06, CTW-01, CTW-02                 | Sim      |
| RF02      | CT-07, CT-08, CT-09, CT-10, CT-11, CT-12, CTW-03, CTW-04                 | Sim      |
| RF03      | CT-13, CT-14, CT-15, CT-16, CT-17, CT-18, CTW-05, CTW-06                 | Sim      |

## Perguntas de verificação

**Existe requisito sem teste?**
Não. RF01, RF02 e RF03 possuem, cada um, 8 casos de teste (6 de caixa
preta + 2 de caixa branca adicionais), cobrindo cenários válidos,
inválidos e valores de fronteira.

**Existe teste que não sabemos qual requisito verifica?**
Não. Todos os 24 casos (CT-01 a CT-18 e CTW-01 a CTW-06) estão
associados a exatamente um requisito, conforme tabela acima e os
comentários/nomes dos métodos em `tests/test_bibliotech.py`.

## Observação
RF01 é o requisito com maior relevância nesta rodada de testes: foi o
único em que o comportamento do código divergiu do especificado
(CT-04), reforçando a importância de testes de valor-limite exatamente
nos requisitos que definem contagens/limites ("menos de 3").
