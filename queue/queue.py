"""Implementar a fila usando lista ligada (List())"""

class Stack:
    def __init__(self):
        self.list_ = []
        # self.list_ = List()

    def empty(self):
        # if self.list_:
        #     return False
        # else:
        #     return True
        return False if self.list_ else True

    def push(self, value):
        self.list_.append(value)

    def pop(self):
        return self.list_.pop()

    def reset(self):
        self.list_ = []


class Queue:
    def __init__(self):
        self.list_ = []
        # self.list_ = List()

    def empty(self):
        # if self.list_:
        #     return False
        # else:
        #     return True
        return False if self.list_ else True

    def enqueue(self, value):
        self.list_.append(value)

    def dequeue(self):
        return self.list_.pop(0)

    def reset(self):
        self.list_ = []
        # self.__init__()


def revese(queue):
    stack = Stack()
    while not queue.empty():
        aux = queue.dequeue()
        stack.push(aux)
        print('queue', queue.list_)
        print('stack', stack.list_)
    while not stack.empty():
        aux = stack.pop()
        queue.enqueue(aux)
        print('queue', queue.list_)
        print('stack', stack.list_)
    return queue


def main():
    queue = Queue()
    print('Queue:', queue.list_)
    queue.enqueue(10)
    print('Queue:', queue.list_)
    queue.enqueue(20)
    print('Queue:', queue.list_)
    queue.enqueue(30)
    print('Queue:', queue.list_)
    queue.enqueue(40)
    print('Queue:', queue.list_)
    queue.enqueue(50)
    print('Queue:', queue.list_)
    queue.enqueue(60)
    print('Queue:', queue.list_)

    revese(queue)
    print('Queue:', queue.list_)


if __name__ == '__main__':
    main()
