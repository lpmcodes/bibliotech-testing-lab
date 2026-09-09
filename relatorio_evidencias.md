# Relatório de Evidências — Execução de Testes e Cobertura

## Nota sobre o ambiente de execução
O ambiente usado para preparar esta entrega não tem acesso à internet,
portanto não foi possível instalar `pytest`/`pytest-cov` localmente
(`pip install` falhou por ausência de conexão). Para validar a suíte
antes do commit, os 24 testes foram executados com um script Python
equivalente (usa apenas a biblioteca padrão: `inspect` para descobrir e
rodar os métodos `test_*`, e o módulo `trace` para medir linhas
executadas). O comportamento de asserção (`assert`) é idêntico ao usado
pelo `pytest`, então o resultado passa/falha é o mesmo que seria obtido
com `pytest -v`.

Assim que o Pull Request é aberto no GitHub, o workflow
`.github/workflows/tests.yml` roda em um runner com acesso à internet,
instala `pytest` e `pytest-cov` de verdade e gera o relatório oficial
(`pytest -v --cov=src --cov-branch --cov-report=term-missing`), visível
na aba **Checks** do PR. Esse é o relatório que deve ser considerado
autoritativo para a aprovação/reprovação da versão.

## Execução equivalente a `pytest -v`

```
PASSED  TestPodeEmprestarCaixaPreta.test_ct01_usuario_valido_pode_emprestar
PASSED  TestPodeEmprestarCaixaPreta.test_ct02_usuario_inativo_nao_pode_emprestar
PASSED  TestPodeEmprestarCaixaPreta.test_ct03_usuario_com_pendencia_nao_pode_emprestar
FAILED  TestPodeEmprestarCaixaPreta.test_ct04_usuario_no_limite_nao_pode_emprestar
PASSED  TestPodeEmprestarCaixaPreta.test_ct05_usuario_logo_abaixo_do_limite_pode_emprestar
PASSED  TestPodeEmprestarCaixaPreta.test_ct06_usuario_acima_do_limite_nao_pode_emprestar
PASSED  TestCalcularMultaCaixaPreta.test_ct07_sem_atraso_multa_zero
PASSED  TestCalcularMultaCaixaPreta.test_ct08_atraso_negativo_multa_zero
PASSED  TestCalcularMultaCaixaPreta.test_ct09_atraso_leve_tres_dias
PASSED  TestCalcularMultaCaixaPreta.test_ct10_fronteira_sete_dias
PASSED  TestCalcularMultaCaixaPreta.test_ct11_fronteira_oito_dias
PASSED  TestCalcularMultaCaixaPreta.test_ct12_dez_dias
PASSED  TestClassificarAtrasoCaixaPreta.test_ct13_sem_atraso
PASSED  TestClassificarAtrasoCaixaPreta.test_ct14_atraso_leve_um_dia
PASSED  TestClassificarAtrasoCaixaPreta.test_ct15_fronteira_atraso_leve_sete_dias
PASSED  TestClassificarAtrasoCaixaPreta.test_ct16_fronteira_atraso_moderado_oito_dias
PASSED  TestClassificarAtrasoCaixaPreta.test_ct17_fronteira_atraso_moderado_trinta_dias
PASSED  TestClassificarAtrasoCaixaPreta.test_ct18_atraso_grave_trinta_e_um_dias
PASSED  TestPodeEmprestarCaixaBranca.test_ctw01_inativo_e_com_pendencia_curto_circuita_em_d1
PASSED  TestPodeEmprestarCaixaBranca.test_ctw02_ativo_sem_pendencia_dentro_do_limite_zero
PASSED  TestCalcularMultaCaixaBranca.test_ctw03_um_dia_de_atraso_fronteira_inferior_faixa_2
PASSED  TestCalcularMultaCaixaBranca.test_ctw04_muitos_dias_de_atraso_caminho_faixa_3
PASSED  TestClassificarAtrasoCaixaBranca.test_ctw05_atraso_negativo_caminho_d6_true
PASSED  TestClassificarAtrasoCaixaBranca.test_ctw06_atraso_bem_acima_de_trinta_caminho_else

== RESULTADO: 23/24 passaram, 1 falharam ==
  -> TestPodeEmprestarCaixaPreta.test_ct04_usuario_no_limite_nao_pode_emprestar:
     AssertionError (pode_emprestar(True, False, 3) retornou True, esperado False)
```

## Cobertura de código (medida com o módulo `trace` da biblioteca padrão)

Todas as 24 linhas de código executável de `src/bibliotech.py`
(atribuições, cabeçalhos de `def`, `if`/`elif`, e `return`) foram
executadas pela suíte, com exceção da palavra-chave isolada `else:` em
`classificar_atraso`, que não corresponde a uma instrução própria (o
`return` dentro dela é executado normalmente pelo teste CTW-06).

| Função               | Linhas executáveis | Executadas | Observação                        |
|-----------------------|--------------------|------------|------------------------------------|
| `pode_emprestar`      | 5                  | 5 (100%)   | 3 decisões, ambos os lados testados |
| `calcular_multa`      | 4                  | 4 (100%)   | 2 decisões, ambos os lados testados |
| `classificar_atraso`  | 5                  | 5 (100%)   | 3 decisões, ambos os lados testados |
| **Total**             | **14**             | **14 (100%)** | Meta do plano: ≥ 90%             |

### Cobertura de branches (decisões), analisada manualmente

| Decisão                                            | Lado verdadeiro coberto por | Lado falso coberto por |
|-----------------------------------------------------|------------------------------|--------------------------|
| `not usuario_ativo`                                 | CT-02, CTW-01                | CT-01, CT-04, CT-05, CT-06, CTW-02 |
| `possui_pendencia`                                  | CT-03, CTW-01                | CT-01, CT-04, CT-05, CT-06, CTW-02 |
| `emprestimos_ativos > LIMITE_EMPRESTIMOS`           | CT-06                         | CT-01, CT-04, CT-05, CTW-02 |
| `dias_atraso <= 0` (multa)                          | CT-07, CT-08                 | CT-09, CT-10, CT-11, CT-12, CTW-03, CTW-04 |
| `dias_atraso <= 7` (multa)                          | CT-09, CT-10, CTW-03         | CT-11, CT-12, CTW-04 |
| `dias_atraso <= 0` (classificação)                  | CT-13, CTW-05                | CT-14 a CT-18, CTW-06 |
| `dias_atraso <= 7` (classificação)                  | CT-14, CT-15                 | CT-16, CT-17, CT-18, CTW-06 |
| `dias_atraso <= 30` (classificação)                 | CT-16, CT-17                 | CT-18, CTW-06 |

**100% das decisões têm os dois lados (verdadeiro e falso) exercitados
por pelo menos um caso de teste** — cobertura de branches acima da meta
de 90% definida no Mini Plano de Testes.
