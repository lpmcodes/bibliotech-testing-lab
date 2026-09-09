# bibliotech-testing-lab

Entrega da **Missão QA: testando o BiblioTech** — testes de caixa
preta e caixa branca sobre o módulo de empréstimos, com cobertura de
código e fluxo completo de Pull Request/CI.

## Estrutura

```
bibliotech-testing-lab/
├── README.md
├── requisitos.md                    # RF01, RF02, RF03
├── requirements-dev.txt
├── relatorio_evidencias.md          # resultados de execução + cobertura
├── src/
│   └── bibliotech.py                # módulo sob teste
├── tests/
│   └── test_bibliotech.py           # 24 casos (caixa preta + caixa branca)
├── docs/
│   ├── plano_testes.md              # Mini Plano de Testes
│   ├── roteiro_testes.md            # Casos de teste detalhados
│   ├── matriz_rastreabilidade.md
│   └── parecer_final_qa.md          # Parecer final sobre a liberação
├── PULL_REQUEST.md                  # PR preenchido, pronto para abrir no GitHub
└── .github/
    └── workflows/
        └── tests.yml                # CI: roda pytest + cobertura a cada push/PR
```

## Como rodar localmente

```bash
pip install -r requirements-dev.txt
pytest -v --cov=src --cov-branch --cov-report=term-missing
```

O teste `test_ct04_usuario_no_limite_nao_pode_emprestar` deve **falhar**
— isso é esperado e documentado: ele expõe um defeito real em RF01
(ver `docs/parecer_final_qa.md`).

## Como abrir o Pull Request

```bash
git init
git add .
git commit -m "test: adiciona testes caixa preta e caixa branca"
git branch -M main
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

Use o conteúdo de `PULL_REQUEST.md` como corpo do Pull Request no
GitHub — ele já está preenchido com requisitos testados, resumo de
caixa preta/branca, defeito encontrado, evidências e parecer da
equipe.

## Resultado resumido desta rodada

- 24 casos de teste (18 caixa preta + 6 caixa branca), cobrindo RF01,
  RF02 e RF03.
- 23 passaram, **1 falhou** (defeito real em RF01 — limite de
  empréstimos).
- 100% de cobertura de linhas e de branches no módulo `src/bibliotech.py`.
- Parecer da equipe: **não recomendamos aprovação** do PR até a
  correção do defeito (ver `docs/parecer_final_qa.md`).
