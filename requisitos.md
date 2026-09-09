# Requisitos — Módulo de Empréstimos (BiblioTech)

## RF01 — Permissão para empréstimo

Um usuário poderá realizar um novo empréstimo quando:

- estiver ativo;
- não possuir pendências;
- possuir **menos de 3** empréstimos ativos.

Caso qualquer condição não seja atendida, o empréstimo deve ser recusado.

## RF02 — Multa por atraso

| Dias de atraso   | Multa                                |
|------------------|---------------------------------------|
| 0 ou menos       | R$ 0,00                               |
| 1 a 7 dias       | R$ 2,00 por dia                       |
| Acima de 7 dias  | R$ 14,00 + R$ 3,00 por dia excedente  |

Exemplos:

- 0 dias → R$ 0,00
- 3 dias → R$ 6,00
- 7 dias → R$ 14,00
- 8 dias → R$ 17,00
- 10 dias → R$ 23,00

## RF03 — Classificação de atraso

- 0 dias → "sem atraso"
- 1 até 7 → "atraso leve"
- 8 até 30 → "atraso moderado"
- mais de 30 → "atraso grave"
