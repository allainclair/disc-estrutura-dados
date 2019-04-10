'''
def idade_em_dias(anos, meses, dias):
    anos_em_dias = 0
    if anos > 0:
        anos_em_dias = anos * 365
    if meses > 0:
        meses_em_dias = meses * 30
    resultado = anos_em_dias + meses_em_dias + dias
    return resultado
'''
"""
Apas duplas
"""


def idade_em_dias(anos, meses, dias):
    return anos*365 + meses*30 + dias


def main():
    # 10 anos 3 meses 2 dias
    anos = 10
    meses = 3
    dias = 2

    anos_em_dias = anos*365
    print('Anos em dias', anos_em_dias)

    meses_em_dias = meses*30
    print('Meses em dias', meses_em_dias)

    resultado = anos_em_dias + meses_em_dias + dias
    print('Resultado', resultado)


if __name__ == '__main__':
    main()
