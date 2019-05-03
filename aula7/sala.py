def main():
    # n = 0
    # n = 1
    # n = 3
    # n = 4
    # result = factorial_recursive(n)
    # print('Factorial result:', result)

    n = 2
    l = []
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



def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return recur_fibo(n-1) + recur_fibo(n-2)


if __name__ == '__main__':
    main()
