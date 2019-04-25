def main():
    n1 = 'allan'
    n2 = 'joao'
    n3 = 'maria'
    n4 = 'jose'
    n5 = ' '
    l1, l2 = reverse_names(n1, n2, n3, n4, n5)
    print('l1:', l1)
    print('l2:', l2)


def reverse_names(name1, name2, name3, name4, name5):
    lista1 = []
    lista2 = []
    # lista1 = [name1, name2, name3, name4, name5]
    # lista2 = [name5, name4, name3, name2, name1]

    lista1.append(name1)
    lista1.append(name2)
    lista1.append(name3)
    lista1.append(name4)
    lista1.append(name5)

    lista2.append(name5)
    lista2.append(name4)
    lista2.append(name3)
    lista2.append(name2)
    lista2.append(name1)

    return lista1, lista2


if __name__ == '__main__':
    main()
