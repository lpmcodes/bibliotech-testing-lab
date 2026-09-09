"""
Módulo de regras de empréstimo do BiblioTech.

RF01 - Permissão para empréstimo
RF02 - Multa por atraso
RF03 - Classificação de atraso
"""

LIMITE_EMPRESTIMOS = 3


def pode_emprestar(usuario_ativo, possui_pendencia, emprestimos_ativos):
    """
    RF01: Um usuário pode realizar um novo empréstimo quando:
      - está ativo;
      - não possui pendências;
      - possui MENOS DE 3 empréstimos ativos.
    """
    if not usuario_ativo:
        return False
    if possui_pendencia:
        return False
    # Existe um defeito proposital nesta condição.
    if emprestimos_ativos > LIMITE_EMPRESTIMOS:
        return False
    return True


def calcular_multa(dias_atraso):
    """
    RF02: Multa por atraso.
      0 ou menos dias  -> R$ 0,00
      1 a 7 dias       -> R$ 2,00 por dia
      Acima de 7 dias  -> R$ 14,00 + R$ 3,00 por dia excedente
    """
    if dias_atraso <= 0:
        return 0.0
    if dias_atraso <= 7:
        return dias_atraso * 2.0
    dias_excedentes = dias_atraso - 7
    return 14.0 + (dias_excedentes * 3.0)


def classificar_atraso(dias_atraso):
    """
    RF03: Classificação do atraso.
      0 dias      -> "sem atraso"
      1 a 7       -> "atraso leve"
      8 a 30      -> "atraso moderado"
      acima de 30 -> "atraso grave"
    """
    if dias_atraso <= 0:
        return "sem atraso"
    elif dias_atraso <= 7:
        return "atraso leve"
    elif dias_atraso <= 30:
        return "atraso moderado"
    else:
        return "atraso grave"
