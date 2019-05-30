class Stack:
    def __init__(self):
        self.list_ = []
        # self.list_ = List()

    def push(self, value):
        self.list_.append(value)

    def pop(self):
        return self.list_.pop()

    def reset(self):
        self.list_ = []


def calc_sufix(list_):
    print(list_)
    stack = Stack()
    for element in list_:
        print(stack.list_)
        if type(element) == int or type(element) == float:  # Eh numero.
            stack.push(str(element))
        else:  # Eh operador.
            value2, value1 = stack.pop(), stack.pop()
            value = eval(value1 + element + value2)
            stack.push(str(value))
    return stack.pop()


def main():
    l = [10, 10, '+', 2, '*', 10, 5, '-', '*']
    result = calc_sufix(l)
    print('Resultado:', result)


if __name__ == '__main__':
    main()
