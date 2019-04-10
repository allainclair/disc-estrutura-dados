def main():
    NF = 6.0
    MF = 5.0
    aprovacao(NF, MF)


def funcao(param1, param2, param3):
    #declaracao1
    a = 1
    print(1)
    return a

def aprovacao(nota_final, media_final):
    if nota_final >= 6.0:
        print('aprovado')
    elif media_final >= 5.0:
        print('aprovado por exame')
    else:
        print('reprovado')


def soma(a, b):
    print(a + b)


if __name__ == '__main__':
<<<<<<< HEAD
    print('inicializacao', 'do programa')
    main()
    print('finalizacao')
#valor_da_soma = soma(2, 3)
#print(valor_da_soma)


=======
    #print('inicializacao')
    #main()
    #print('finalizacao')
    valor_da_soma = soma(2, 3)
    print(valor_da_soma)
>>>>>>> 48c36fc1ae28b06dd6914488e321f016704c758f
