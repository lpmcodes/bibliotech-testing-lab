# Mini Plano de Testes — BiblioTech

## Identificação
- **Módulo sob teste:** `src/bibliotech.py` (regras de empréstimo)
- **Versão:** Pull Request `testes/equipe-qa` sobre a branch `main`
- **Equipe de QA:** Missão QA — BiblioTech
- **Data:** ver histórico de commits no GitHub

## Escopo
RF01 (permissão de empréstimo), RF02 (multa por atraso) e RF03
(classificação de atraso).

## Fora do escopo
Interface gráfica, banco de dados, autenticação/segurança e desempenho.

## Estratégia
- **Caixa preta:** casos de teste derivados exclusivamente de
  `requisitos.md`, com técnicas de particionamento em classes de
  equivalência (cenário válido / inválido) e análise de valor-limite.
- **Caixa branca:** após liberação do código, identificação de todas as
  decisões (`if`/`elif`) e garantia de que ambos os caminhos (verdadeiro
  e falso) de cada condição sejam exercitados.
- **Automação:** testes unitários com `pytest`; medição de cobertura de
  linhas e branches com `pytest-cov`; execução automática via GitHub
  Actions a cada push/PR.

## Ambiente
- Python 3.12
- pytest, pytest-cov
- GitHub + GitHub Actions (`.github/workflows/tests.yml`)

## Critério de entrada
- Código-fonte disponível em `src/bibliotech.py`.
- Requisitos RF01–RF03 definidos e sem ambiguidade em `requisitos.md`.

## Critérios de saída
- [x] Todos os requisitos críticos (RF01, RF02, RF03) possuem casos de
      teste de caixa preta e caixa branca.
- [x] Testes executados e resultados registrados (ver
      `docs/roteiro_testes.md` e `relatorio_evidencias.md`).
- [x] Defeitos encontrados registrados e comunicados no Pull Request.
- [x] Cobertura de linhas e branches ≥ 90% (ver `relatorio_evidencias.md`).
- [x] Pull Request criado com todas as evidências anexadas.

## Riscos
- Tempo limitado para explorar combinações adicionais de entradas.
- Ambiente de execução local sem acesso à internet impediu a instalação
  de `pytest`/`pytest-cov` durante o desenvolvimento; os resultados
  desta fase foram validados com um executor Python equivalente (ver
  `relatorio_evidencias.md`) e serão confirmados oficialmente pelo
  GitHub Actions, que tem acesso à internet para instalar as
  dependências.
- Um defeito real foi encontrado em RF01 (ver seção de defeitos); ele
  impacta a decisão de aprovação da versão.

## Entregáveis
1. Mini Plano de Testes (este documento).
2. Roteiros/casos de teste (`docs/roteiro_testes.md`).
3. Matriz de rastreabilidade (`docs/matriz_rastreabilidade.md`).
4. Testes automatizados em pytest + relatório de cobertura
   (`tests/test_bibliotech.py`, `relatorio_evidencias.md`).
5. Parecer final de QA sobre a liberação do BiblioTech
   (`docs/parecer_final_qa.md`).
