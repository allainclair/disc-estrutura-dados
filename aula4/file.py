def main():
    elemento = input('entre com um elemento da lista: ')
    print(f'O elemento lido foi: {elemento}')
    elemento = eval(elemento)
    lista = input('entre com a lista: ')
    print('A lista lida eh:', lista)

    tipo_da_lista = type(lista)
    print('Tipo da lista lida:', tipo_da_lista)

    lista = eval(lista)
    print('Tipo da lista lida:', type(lista))


    # print(f'Elemento na lista? {elemento_na_lista}')
    elemento_na_lista = elemento in lista
    elemento_na_lista = my_in(elemento, lista)

    if elemento_na_lista:
        resposta = 'Sim'
    else:
        resposta = 'Nao'

    print(f'Elemento na lista? {resposta}')


def my_in(elemento, lista):
    for elemento_lista in lista:
        if elemento_lista == elemento:
            return True
        else:
            print(
                f'elemento_lista != elemento. {elemento_lista} != {elemento}')
    return False


def main2():
    minha_lista = [1, 2, 3, 4, 5]
    minha_lista1 = [1, 2]
    print(minha_lista_dobrada)


def double(lista):
    doubled_list = []
    for elemento in lista:
        doubled_list.append(2*elemento)
    return doubled_list



if __name__ == '__main__':
    # main()
    main2()
