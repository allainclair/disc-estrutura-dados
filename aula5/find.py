def main():
    e = 10
    l = [0, 2, 3, 10, 4, 5]
    esta_na_lista = find1(l, e)
    print('E estah na lista?', esta_na_lista)


def find(lista, elemento):
    return elemento in lista


def find1(lista, elemento):
    for e in lista:
        if e == elemento:
            return True
    return False


def encontrar_todos(lista, elemento):
    """Retorne todos os indicies do elemento na lista.
    O retorno eh em uma lista

    ex:
    entrada: encontrar_todos([1, 2, 2, 3, 4, 4, 2], 2)
    saida: [1, 2, 6]
    """

    for i, e in enumerate(lista):
        if e == elemento:
            return True

    return False


if __name__ == '__main__':
    main()
