"""
Suíte de testes do módulo de empréstimos do BiblioTech.

Organização:
  - Bloco 1: Testes de CAIXA PRETA (baseados apenas em requisitos.md)
  - Bloco 2: Testes de CAIXA BRANCA (complementam a cobertura de
    decisões/condições identificadas na leitura do código-fonte)

IDs de caso de teste seguem docs/roteiro_testes.md e
docs/matriz_rastreabilidade.md.
"""

import pytest

from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso


# ---------------------------------------------------------------------------
# BLOCO 1 — CAIXA PRETA (RF01, RF02, RF03)
# ---------------------------------------------------------------------------

class TestPodeEmprestarCaixaPreta:
    """CT-01 a CT-06 — ver docs/roteiro_testes.md"""

    def test_ct01_usuario_valido_pode_emprestar(self):
        # cenário válido: ativo, sem pendência, 0 empréstimos
        assert pode_emprestar(True, False, 0) is True

    def test_ct02_usuario_inativo_nao_pode_emprestar(self):
        # cenário inválido: usuário inativo
        assert pode_emprestar(False, False, 0) is False

    def test_ct03_usuario_com_pendencia_nao_pode_emprestar(self):
        # cenário inválido: usuário com pendência
        assert pode_emprestar(True, True, 0) is False

    def test_ct04_usuario_no_limite_nao_pode_emprestar(self):
        """
        Requisito: 'menos de 3 empréstimos ativos' -> com 3 empréstimos
        ativos, o empréstimo DEVE ser recusado (False).

        DEFEITO ENCONTRADO (RF01): a implementação usa
        `emprestimos_ativos > LIMITE_EMPRESTIMOS`, o que permite um 4º
        empréstimo apenas quando emprestimos_ativos == 3 retorna True
        (permitido), violando o requisito. Este teste é o caso de
        fronteira (valor-limite superior) que expõe o defeito e deve
        falhar (vermelho) até a correção do código de produção.
        Ver: docs/matriz_rastreabilidade.md e parecer final no PR.
        """
        assert pode_emprestar(True, False, 3) is False

    def test_ct05_usuario_logo_abaixo_do_limite_pode_emprestar(self):
        # fronteira inferior válida: 2 empréstimos ativos (< 3)
        assert pode_emprestar(True, False, 2) is True

    def test_ct06_usuario_acima_do_limite_nao_pode_emprestar(self):
        # bem acima do limite: ambas as versões (correta e com defeito)
        # concordam que deve ser recusado
        assert pode_emprestar(True, False, 4) is False


class TestCalcularMultaCaixaPreta:
    """CT-07 a CT-11 — ver docs/roteiro_testes.md"""

    def test_ct07_sem_atraso_multa_zero(self):
        assert calcular_multa(0) == 0.0

    def test_ct08_atraso_negativo_multa_zero(self):
        # valor fora do domínio esperado, mas útil para robustez
        assert calcular_multa(-3) == 0.0

    def test_ct09_atraso_leve_tres_dias(self):
        assert calcular_multa(3) == 6.0

    def test_ct10_fronteira_sete_dias(self):
        # limite superior da faixa "R$ 2,00/dia"
        assert calcular_multa(7) == 14.0

    def test_ct11_fronteira_oito_dias(self):
        # primeiro dia da faixa "acima de 7 dias"
        assert calcular_multa(8) == 17.0

    def test_ct12_dez_dias(self):
        assert calcular_multa(10) == 23.0


class TestClassificarAtrasoCaixaPreta:
    """CT-13 a CT-18 — ver docs/roteiro_testes.md"""

    def test_ct13_sem_atraso(self):
        assert classificar_atraso(0) == "sem atraso"

    def test_ct14_atraso_leve_um_dia(self):
        assert classificar_atraso(1) == "atraso leve"

    def test_ct15_fronteira_atraso_leve_sete_dias(self):
        assert classificar_atraso(7) == "atraso leve"

    def test_ct16_fronteira_atraso_moderado_oito_dias(self):
        assert classificar_atraso(8) == "atraso moderado"

    def test_ct17_fronteira_atraso_moderado_trinta_dias(self):
        assert classificar_atraso(30) == "atraso moderado"

    def test_ct18_atraso_grave_trinta_e_um_dias(self):
        assert classificar_atraso(31) == "atraso grave"


# ---------------------------------------------------------------------------
# BLOCO 2 — CAIXA BRANCA (cobertura de decisões/condições e caminhos)
# ---------------------------------------------------------------------------
#
# Estruturas identificadas em src/bibliotech.py:
#   pode_emprestar:
#     D1: if not usuario_ativo               -> T/F
#     D2: if possui_pendencia                -> T/F
#     D3: if emprestimos_ativos > LIMITE...  -> T/F
#   calcular_multa:
#     D4: if dias_atraso <= 0                -> T/F
#     D5: if dias_atraso <= 7                -> T/F
#   classificar_atraso:
#     D6: if dias_atraso <= 0                -> T/F
#     D7: elif dias_atraso <= 7              -> T/F
#     D8: elif dias_atraso <= 30             -> T/F
#
# Os testes do Bloco 1 já exercitam a maioria dessas decisões nos dois
# sentidos. Abaixo, casos adicionais garantem que TODAS as combinações
# de decisão e caminhos independentes sejam cobertas (>= 90% de linhas
# e branches, meta do Mini Plano de Testes).

class TestPodeEmprestarCaixaBranca:
    def test_ctw01_inativo_e_com_pendencia_curto_circuita_em_d1(self):
        """
        Garante que D1 (usuário inativo) é avaliada primeiro e retorna
        False imediatamente, sem depender das demais condições
        (ordem de prioridade das regras de negócio).
        """
        assert pode_emprestar(False, True, 10) is False

    def test_ctw02_ativo_sem_pendencia_dentro_do_limite_zero(self):
        # Caminho: D1=False, D2=False, D3=False -> True
        assert pode_emprestar(True, False, 1) is True


class TestCalcularMultaCaixaBranca:
    def test_ctw03_um_dia_de_atraso_fronteira_inferior_faixa_2(self):
        # Caminho: D4=False, D5=True (primeiro dia da 2ª faixa)
        assert calcular_multa(1) == 2.0

    def test_ctw04_muitos_dias_de_atraso_caminho_faixa_3(self):
        # Caminho: D4=False, D5=False -> faixa "acima de 7 dias"
        assert calcular_multa(20) == 14.0 + (13 * 3.0)


class TestClassificarAtrasoCaixaBranca:
    def test_ctw05_atraso_negativo_caminho_d6_true(self):
        assert classificar_atraso(-1) == "sem atraso"

    def test_ctw06_atraso_bem_acima_de_trinta_caminho_else(self):
        # Caminho: D6=False, D7=False, D8=False -> else "atraso grave"
        assert classificar_atraso(100) == "atraso grave"
