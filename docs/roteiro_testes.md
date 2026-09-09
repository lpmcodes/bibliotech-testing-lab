# Roteiro de Testes — BiblioTech

Formato enxuto: ID | Requisito | Tipo | Dados de teste | Resultado esperado
| Resultado obtido | Status.

Cada linha corresponde a um teste automatizado equivalente em
`tests/test_bibliotech.py` (mesmo ID em comentário/nome do método).

## RF01 — Permissão para empréstimo (`pode_emprestar`)

| ID     | Tipo         | Dados (ativo, pendência, empréstimos) | Esperado | Obtido | Status  |
|--------|--------------|-----------------------------------------|----------|--------|---------|
| CT-01  | Caixa preta  | (True, False, 0)                        | True     | True   | Passou  |
| CT-02  | Caixa preta  | (False, False, 0)                       | False    | False  | Passou  |
| CT-03  | Caixa preta  | (True, True, 0)                         | False    | False  | Passou  |
| CT-04  | Caixa preta  | (True, False, 3) — fronteira superior   | False    | **True** | **Falhou** |
| CT-05  | Caixa preta  | (True, False, 2) — fronteira inferior   | True     | True   | Passou  |
| CT-06  | Caixa preta  | (True, False, 4)                        | False    | False  | Passou  |
| CTW-01 | Caixa branca | (False, True, 10) — prioridade de regra | False    | False  | Passou  |
| CTW-02 | Caixa branca | (True, False, 1)                        | True     | True   | Passou  |

> **CT-04 é o caso que expõe o defeito de RF01.** Ver detalhamento
> completo abaixo e o parecer final em `docs/parecer_final_qa.md`.

### Detalhamento — CT-04 (defeito encontrado)

```
ID:              CT-04
Requisito:       RF01
Título:          Usuário com exatamente 3 empréstimos ativos não pode
                 realizar outro empréstimo.
Tipo:            Caixa preta / valor-limite (fronteira superior)
Prioridade:      Alta
Pré-condição:    Sistema disponível; usuário ativo; sem pendências.
Dados de teste:  usuario_ativo = True
                 possui_pendencia = False
                 emprestimos_ativos = 3
Passos:          1. Executar pode_emprestar(True, False, 3).
Resultado esperado: False (requisito exige "menos de 3" empréstimos)
Resultado obtido:   True
Status:          [x] Falhou
Observação:      A implementação usa `emprestimos_ativos >
                 LIMITE_EMPRESTIMOS` (ou seja, `3 > 3`, que é falso),
                 permitindo indevidamente o 4º empréstimo. O correto
                 seria `>=`.
```

## RF02 — Multa por atraso (`calcular_multa`)

| ID     | Tipo         | Dias de atraso | Esperado | Obtido | Status |
|--------|--------------|-----------------|----------|--------|--------|
| CT-07  | Caixa preta  | 0               | R$ 0,00  | R$ 0,00 | Passou |
| CT-08  | Caixa preta  | -3 (robustez)   | R$ 0,00  | R$ 0,00 | Passou |
| CT-09  | Caixa preta  | 3               | R$ 6,00  | R$ 6,00 | Passou |
| CT-10  | Caixa preta  | 7 (fronteira)   | R$ 14,00 | R$ 14,00 | Passou |
| CT-11  | Caixa preta  | 8 (fronteira)   | R$ 17,00 | R$ 17,00 | Passou |
| CT-12  | Caixa preta  | 10              | R$ 23,00 | R$ 23,00 | Passou |
| CTW-03 | Caixa branca | 1 (fronteira inferior faixa 2) | R$ 2,00 | R$ 2,00 | Passou |
| CTW-04 | Caixa branca | 20 (caminho faixa 3)          | R$ 53,00 | R$ 53,00 | Passou |

## RF03 — Classificação de atraso (`classificar_atraso`)

| ID     | Tipo         | Dias de atraso | Esperado          | Obtido            | Status |
|--------|--------------|-----------------|-------------------|--------------------|--------|
| CT-13  | Caixa preta  | 0               | "sem atraso"      | "sem atraso"       | Passou |
| CT-14  | Caixa preta  | 1               | "atraso leve"     | "atraso leve"      | Passou |
| CT-15  | Caixa preta  | 7 (fronteira)   | "atraso leve"     | "atraso leve"      | Passou |
| CT-16  | Caixa preta  | 8 (fronteira)   | "atraso moderado" | "atraso moderado"  | Passou |
| CT-17  | Caixa preta  | 30 (fronteira)  | "atraso moderado" | "atraso moderado"  | Passou |
| CT-18  | Caixa preta  | 31              | "atraso grave"    | "atraso grave"     | Passou |
| CTW-05 | Caixa branca | -1 (robustez)   | "sem atraso"      | "sem atraso"       | Passou |
| CTW-06 | Caixa branca | 100 (caminho else) | "atraso grave" | "atraso grave"    | Passou |

## Resumo
- **Total de casos:** 24 (18 de caixa preta + 6 de caixa branca)
- **Passaram:** 23
- **Falharam:** 1 (CT-04 — defeito real em RF01)
