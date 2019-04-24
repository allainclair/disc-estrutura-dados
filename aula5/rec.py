def main():
    list_ = [1, 2, 3, 4]
    print('list_', list_)
    print(recursive_sum(list_))

    n = 3
    exp = 3
    print()
    print('N', n, 'exp', exp)
    print(recursive_exp(3, 3))


def recursive_sum(list_, i=0):
    n = len(list_)
    print('Tamanho da lista', n)
    print('i', i)
    if i < n:
        print('list_[i]', list_[i])
        print('Chamada recursiva...')
        ret = list_[i] + recursive_sum(list_, i + 1)
        print('Retorno da recursao i =', i, 'retorno:', ret)
        return ret
    else:
        print('Chamada nao recursiva, retorna 0')
        return 0


def recursive_exp(n, exp, i=0):
    print('i', i)
    if i < exp:
        print('Chamada recursiva...')
        ret = recursive_exp(n, exp, i + 1)
        print('Retorno da recursao i =', i, 'retorno:', ret)
        return n * ret
    else:
        print('Retorno nao recursivo, retorna 1')
        return 1


if __name__ == '__main__':
    main()
