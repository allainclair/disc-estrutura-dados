def main():
    NF = 6.0
    MF = 5.0
    aprovacao(NF, MF)


def aprovacao(NF, MF):
    if NF >= 6.0:
        print('aprovado')
    elif MF >= 5.0:
        print('aprovado por exame')
    else:
        print('reprovado')


def soma(a, b):
    print(a + b)


if __name__ == '__main__':
    #print('inicializacao')
    #main()
    #print('finalizacao')
    valor_da_soma = soma(2, 3)
    print(valor_da_soma)




