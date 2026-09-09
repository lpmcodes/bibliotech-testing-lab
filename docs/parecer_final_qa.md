# Parecer Final de QA — BiblioTech (módulo de empréstimos)

## Resumo da atividade
A equipe de QA elaborou e executou 24 casos de teste (18 de caixa preta
+ 6 de caixa branca) cobrindo os três requisitos em escopo (RF01, RF02,
RF03), documentou um Mini Plano de Testes, um roteiro de testes e uma
matriz de rastreabilidade, e mediu a cobertura de código da suíte
automatizada em `pytest`.

## Resultado dos testes
- 23 de 24 testes **passaram**.
- 1 teste **falhou**: `test_ct04_usuario_no_limite_nao_pode_emprestar`
  (RF01), evidenciando uma divergência real entre o comportamento do
  código e o requisito especificado.

## Defeito encontrado

**RF01 — Permissão para empréstimo**

- **Requisito:** um usuário só pode emprestar com **menos de 3**
  empréstimos ativos.
- **Comportamento observado:** a função `pode_emprestar` usa a
  condição `emprestimos_ativos > LIMITE_EMPRESTIMOS` (`3 > 3`), que é
  falsa quando `emprestimos_ativos == 3`, permitindo indevidamente um
  4º empréstimo simultâneo.
- **Comportamento esperado:** a condição deveria ser
  `emprestimos_ativos >= LIMITE_EMPRESTIMOS`.
- **Severidade:** Alta — permite violação direta de uma regra de
  negócio central (limite de empréstimos simultâneos), sem exigir
  nenhuma condição incomum para ser reproduzido.
- **Como reproduzir:** `pode_emprestar(True, False, 3)` retorna `True`;
  deveria retornar `False`.
- **Evidência:** caso de teste CT-04 em
  `docs/roteiro_testes.md` / `tests/test_bibliotech.py`.

## Cobertura de código
A suíte cobre 100% das linhas executáveis e ambos os caminhos
(verdadeiro/falso) de todas as decisões do módulo (`if`/`elif`),
superando a meta de 90% definida no Mini Plano de Testes. Detalhes em
`relatorio_evidencias.md`.

## Recomendação da equipe de QA

- [ ] Recomendamos aprovação
- [x] **Não recomendamos aprovação** — não nesta condição

**Justificativa:** o Pull Request não deve ser aprovado enquanto o
defeito em RF01 não for corrigido, pois ele permite que usuários
excedam o limite de empréstimos simultâneos definido pela regra de
negócio, o que pode gerar inconsistência de estoque/disponibilidade de
livros em produção. Recomenda-se:

1. Corrigir a condição em `src/bibliotech.py` para
   `emprestimos_ativos >= LIMITE_EMPRESTIMOS`.
2. Reexecutar a suíte de testes (`pytest -v --cov=src --cov-branch`)
   e confirmar que `test_ct04_usuario_no_limite_nao_pode_emprestar`
   passa a ser aprovado (verde).
3. Após a correção e nova execução verde no GitHub Actions, a versão
   pode ser considerada apta para aprovação do PR, do ponto de vista
   dos requisitos RF01, RF02 e RF03 aqui testados.

RF02 e RF03 não apresentaram divergências em relação aos requisitos
nos cenários testados.
