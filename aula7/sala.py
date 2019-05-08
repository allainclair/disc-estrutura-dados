def main():
    # n = 0
    # n = 1
    # n = 3
    # n = 2
    # exp = 10
    # l = [1, 2, 3, 4]
    # i = 0
    # result = sum_rec(l, i)
    # print('Sum result:', result)

    n = 8
    result = recur_fibo(n)
    print('Fib:', result)


def factorial_iterative(n):
    value = 1
    for i in range(1, n+1):
        value = value * i  # value *= i
    return value


def factorial_recursive(n):
    if n > 1:
        # i = n - 1
        # ret = n * factorial_recursive(i)
        # return ret
        return n * factorial_recursive(n - 1)
    else:
        return 1


def exp_iterative(n, exp):
    value = 1
    for _ in range(exp):
        value = value * n  # value *= n
    return value


def exp_recursive(n, exp):
    if exp >= 1:
        # i = n - 1
        # ret = n * factorial_recursive(i)
        # return ret
        exp_minus_1 = exp - 1
        return n * exp_recursive(n, exp_minus_1)
    else:
        return 1


def sum_it(list_):
    acc = 0
    for element in list_:
        acc += element  # acc = acc + element
    return acc


def sum_rec(list_, i):
    size = len(list_)
    if i < size:
        return list_[i] + sum_rec(list_, i + 1)
    else:
        return 0


# def sum_rec(list_):
#     pass


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return recur_fibo(n-1) + recur_fibo(n-2)


if __name__ == '__main__':
    main()
