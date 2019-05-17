class List:
    def __init__(self):
        self.first_node = None

    def __str__(self):
        """Metodo especial que eh chamado quando o print() eh usado no objeto."""
        node = self.first_node
        string = ''
        while node is not None:
            string += f'{node.value} '
            node = node.next
        return string

    def add_sorted(self, value):
        """Usar essa adicao desde o inicio para manter lista ligada."""
        pass

    def addat_end(self, value):
        """Adiciona ao final da lista ligada."""
        # Cria-se novo node.
        new_node = Node(value)

        if not self.empty():  # Se a lista nao eh vazia.
            # Var auxiliar para nao perder referencia do primeiro node.
            node = self.first_node
            # Se o "campo next" nao eh None continuamos andando na lista para
            # chegar ao ultimo node.
            while node.next is not None:
                node = node.next
            # Quando o "node" auxiliar esta com "node.next == None"
            # atribuimos a "node.next" o novo node.
            node.next = new_node
        else:  # Se a lista esta vazia, o novo node eh o primeiro node.
            self.first_node = new_node

    def addat_start(self, value):
        """Adiciona ao comeco da lista ligada."""
        new_node = Node(value)
        new_node.next = self.first_node  # Novo node ja aponta para o primeiro.
        self.first_node = new_node  # Primeiro node se torna o novo node.

    def empty(self):
        return self.first_node is None  # self.first_node == None

    def print_(self):
        aux_node = self.first_node
        string = ''
        while aux_node is not None:
            print(aux_node.value, end=' '),
            aux_node = aux_node.next
        print()
        return string


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def addat_start_tests():
    list_ = List()  # Nova lista.
    list_.addat_start(1)
    list_.addat_start(2)
    list_.addat_start(3)
    list_.addat_start(4)
    list_.addat_start(5)
    return list_


def addat_end_tests():
    list_ = List()  # Nova lista.
    list_.addat_end(1)
    list_.addat_end(2)
    list_.addat_end(3)
    list_.addat_end(4)
    list_.addat_end(5)
    return list_


if __name__ == '__main__':
    list_ = addat_start_tests()
    print('Addat start tests')
    print(list_)
    list_.print_()

    list_ = addat_end_tests()
    print('Addat end tests')
    print(list_)
    list_.print_()

