## Missão QA — BiblioTech

### Requisitos testados
- [x] RF01
- [x] RF02
- [x] RF03

### Caixa preta
**Quantidade de testes:** 18
**Casos de fronteira utilizados:**
- RF01: 2 empréstimos (válido, fronteira inferior) e 3 empréstimos
  (fronteira superior — expôs o defeito).
- RF02: 7 dias e 8 dias (transição entre faixas de multa).
- RF03: 7/8 dias e 30/31 dias (transições entre classificações).

### Caixa branca
**Branches analisados:** 8 decisões no total (3 em `pode_emprestar`, 2
em `calcular_multa`, 3 em `classificar_atraso`); todas com os dois
lados (verdadeiro/falso) exercitados.
**Cobertura obtida:** 100% de linhas e 100% de branches em
`src/bibliotech.py` (ver `relatorio_evidencias.md`; meta do plano era
≥ 90%).

### Defeitos encontrados
**RF01 — Permissão para empréstimo.**
Comportamento observado: `pode_emprestar(True, False, 3)` retorna
`True`. Comportamento esperado: deveria retornar `False`, pois o
requisito exige **menos de 3** empréstimos ativos. A implementação usa
`emprestimos_ativos > LIMITE_EMPRESTIMOS` em vez de `>=`. Severidade
alta — permite empréstimo além do limite de negócio sem nenhuma
condição incomum. Detalhes em `docs/parecer_final_qa.md`.

### Evidências
**Resultado do pytest:** 23 de 24 testes passaram; 1 falhou
(`test_ct04_usuario_no_limite_nao_pode_emprestar`), evidenciando o
defeito acima. Log completo em `relatorio_evidencias.md`.

**Resultado de cobertura:** 100% de linhas e branches em
`src/bibliotech.py`. Detalhamento por decisão em
`relatorio_evidencias.md`.

### Parecer da equipe
- [ ] Recomendamos aprovação
- [x] Não recomendamos aprovação

**Justificativa:** o defeito em RF01 permite que um usuário exceda o
limite de 3 empréstimos simultâneos definido pela regra de negócio.
Recomendamos corrigir a condição para
`emprestimos_ativos >= LIMITE_EMPRESTIMOS`, reexecutar a suíte de
testes e confirmar pipeline verde antes de aprovar esta versão. RF02 e
RF03 não apresentaram divergências nos cenários testados.
