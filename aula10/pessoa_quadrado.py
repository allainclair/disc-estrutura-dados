import math


def main():
    # l = []
    altura, peso, nome, idade = 160, 60, 'Maria', 31
    pessoa1 = Pessoa(altura, peso, nome, idade)
    pessoa1.print()

    print()

    pessoa2 = Pessoa(150, 50, 'Jao', 30)
    pessoa2.print()

    print()

    quadrado1 = Quadrado(1)
    quadrado1.print()

    print()

    quadrado2 = Quadrado(2)
    quadrado2.print()

    print()

    quadrado3 = Quadrado(3)
    quadrado3.print()


class Pessoa:
    def __init__(self, altura, peso, nome, idade):
        self.altura = altura
        self.peso = peso
        self.nome = nome
        self.idade = idade

    def print(self):
        print('Altura:', self.altura)
        print('Peso:', self.peso)
        print('Nome:', self.nome)
        print('Idade:', self.idade)


class Quadrado:
    def __init__(self, aresta):
        self.aresta = aresta

    def area(self):
        return self.aresta * self.aresta

    def perimetro(self):
        return self.aresta * 4

    def diagonal(self):
        return self.aresta * math.sqrt(2)

    def print(self):
        print('Aresta:', self.aresta)
        print('Area:', self.area())
        print('Perimetro:', self.perimetro())
        print('Diagonal:', self.diagonal())


if __name__ == '__main__':
    main()
