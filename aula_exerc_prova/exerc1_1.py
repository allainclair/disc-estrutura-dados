def max3(a, b, c):
    if a > b:
        if a > c:
            max_ = a
        else:
            max_ = c
    else:
        if b > c:
            max_ = b
        else:
            max_ = c
    return max_


def max_list(list_):
    max_ = list_[0]
    for element in list_:
        if element > max_:
            max_ = element
    return max_


def categoria(idade):
    if idade < 5:
        print('Categoria indefinida')
    elif 5 <= idade <= 7:
        print('Infantil A')
    elif 8 <= idade <= 10:
        print('Infantil B')
    elif 11 <= idade <= 13:
        print('Juvenil A')
    elif 14 <= idade <= 17:
        print('Juvenil B')
    else:
        print('Adulto')

def when(pa, ia, pb, ib):
    n = 0
    flag = True
    while flag:
        print('N', n)
        fa = pa * (1 + ia)**n
        print('FA', fa)
        fb = pb * (1 + ib)**n
        print('FB', fb)
        print()
        if fa >= fb:
            flag = False
        else:
            n += 1  # n = n + 1
    return n


def reserve(n):
    div = n // 10
    rest = n % 10
    reverse_ = rest
    print('First reverse', reverse_)
    while div > 0:
        rest = div % 10
        print('rest', rest)
        div = div // 10
        print('rest', div)
        reverse_ *= 10
        reverse_ += rest
    return reverse_



def main():
    # retorno = max3(1, 2, 3)
    # print('max(1,2,3)', retorno)
    # assert retorno == 3
    # assert max3(4, 2, 3) == 4
    # assert max3(4, 5, 3) == 5
    # assert max3(10, 5, 3) == 10
    # assert max3(10, 5, 11) == 11
    # print('Tudo certo!!?')

    # list_ = [1, 2, 3, 4, 0]
    # assert max_list(list_) == 4
    # list_ = [1, 2, 3, 4, 0, 10]
    # assert max_list(list_) == 10
    # list_ = [1, 12, 3, 4, 0, 10]
    # assert max_list(list_) == 12

    # categoria(2)
    # categoria(5)
    # categoria(7)
    # categoria(10)
    # categoria(13)
    # categoria(15)
    # categoria(18)
    # categoria(19)
    # categoria(200)

    # pa = int(input('PA >'))
    # ia = float(input('IA >'))
    # pb = int(input('PB >'))
    # ib = float(input('IB >'))
    # pa, ia = 80_000, 0.03
    # pb, ib = 200_000, 0.015
    # return_ = when(pa, ia, pb, ib)
    # print('Quando vai passar A >= B', return_)

    print(reserve(123456))


if __name__ == '__main__':
    main()
