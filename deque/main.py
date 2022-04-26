import random
import collections  # NAO USE ESSE MODULO, EH APENAS PARA EXEMPLO


class Deque:
    """NAO USE ESSA CLASSE, SOBRESCREVA ELA: faca sua propria implementacao
    de Deque. Eu irei copiar esse seu trecho (Classe Deque) de codigo para
    dentro dos meus testes.
    """
    def __init__(self):
        # Fila que pode tem "duas pontas" para exemplificar
        self.dq = collections.deque()

    def append(self, element):
        self.dq.append(element)

    def appendleft(self, element):
        self.dq.appendleft(element)

    def pop(self):
        """Retorna elemento da esquerda da direita (False se vazia)."""
        if len(self.dq) > 0:
            return self.dq.pop()
        else:
            return False
        # return self.dq.pop() if len(self.dq) > 0 else False

    def popleft(self):
        """Retorna elemento da esquerda da esquerda (False se vazia)."""
        return self.dq.popleft() if len(self.dq) > 0 else False


def test_simple():
    dq = Deque()  # Fila que tem "duas pontas"

    assert dq.append(10) is None  # Append 10 e nao retorna nada.
    assert dq.append(20) is None  # Append 20 e nao retorna nada.
    assert dq.append(30) is None  # ...
    assert dq.append(40) is None
    print(dq.dq)

    assert dq.pop() == 40  # Pop retorna 40 (pop tira da direita)
    print(dq.dq)
    assert dq.pop() == 30  # ...
    print(dq.dq)
    assert dq.pop() == 20
    print(dq.dq)
    assert dq.pop() == 10
    print(dq.dq)

    assert dq.pop() is False  # Deque vazia.
    assert dq.pop() is False  # ...

    assert dq.appendleft(40) is None
    assert dq.appendleft(50) is None
    print(dq.dq)

    assert dq.popleft() == 50
    print(dq.dq)

    assert dq.append(100) is None
    assert dq.append(200) is None
    print(dq.dq)

    assert dq.popleft() == 40
    print(dq.dq)
    assert dq.pop() == 200
    print(dq.dq)

    assert dq.appendleft(300) is None
    print(dq.dq)

    assert dq.pop() == 100
    print(dq.dq)
    assert dq.pop() == 300
    print(dq.dq)
    assert dq.pop() is False  # Deque vazia.
    assert dq.popleft() is False  # Deque vazia.


def test_random():
    NUM_ELEMENTS = 100_000_000
    dq = Deque()

    append, appendleft, = [], []
    for _ in range(NUM_ELEMENTS):
        element = random.randint(-1_000_000_000, 1_000_000_000)
        if random.random() > 0.5:  # Probabilidade de 50%
            dq.append(element)
            append.append(element)
        else:
            dq.appendleft(element)
            appendleft.append(element)

    for element in reversed(append):
        assert dq.pop() == element

    for element in reversed(appendleft):
        assert dq.popleft() == element

    assert dq.pop() is False  # Deque vazia.
    assert dq.popleft() is False  # Deque vazia.


def main():
    test_simple()
    test_random()


if __name__ == '__main__':
    main()
