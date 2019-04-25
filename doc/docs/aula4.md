## Operador IN

Operador que retorna uma avaliação booleana (True or False). Análogo à
notação de conjutos "pertence" (diferente de "está contido").

 ```Python
 VARIAVEL in ESTRUTURA_QUE_SUPORTA_IN
 ```

```Python tab=
10 in [1, 2, 3, 4]

11 in [1, 2, 11, 4]

'enzo' in ['allan', 'maria', 'jose', 'enzo', 'valentina']


[1, 2, 3, 4] in [1, 2, 3, 4]

lista_de_inteiros = [1, 2, 3, 4]
lista_mista = [[1, 2, 3, 4], 'a', 'b', 'c']

lista_de_inteiros in lista_mista
```

## Estruturas de repetição **

**FOR e WHILE**

### FOR ***

Análogo à notação de formação de conjuntos.

Exemplos:

* Para cada x pertencente ao conjunto {1, 2, 3, 4} crie um conjunto com o
  quadrado de x;

* Para cada x pertencente ao conjunto {1, 2, 3, 4} imprima o dobro de x;

* Para cada x pertencente ao conjunto {1, 2, 3, 4} imprima o dobro de x se x
 for par.

Então podemos dizer que da para ler um ** *for* ** da seguinte forma: "para
cada elemento na lista faça:"

```Python tab=
for ELEMENTO in ITERADOR:
    CORPO DO FOR
```

```C tab=
for (i=0; i<n; i++) {
    CORPO DO FOR
}
```

Um **iterador** é um "conjunto de elementos", podendo ser vazio, ter apenas um
elemento, ou mais do que um elemento. Se for vazio, o corpo (escopo) do `for`
não é executado. Caso contrário o corpo do `for` é executado em todos
elementos do iterador.

```Python tab=
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print('i: %s', i)
1
2
3
4
5
6
7
8
9
10

for letra in ['a', 'b', 'c', 'd']:
    print('letra:', letra)
a
b
c
d

letras = ['a', 'b', 'c', 'd', 'e', 'f']
for letra in letras:
    print('letra:', letra)
a
b
c
d
e
f
```

Outros exemplos com FOR:

```Python tab=
range(10)  # Funcao pronta (interna) do Python.
range(0, 10)

# Transformar o "range" em uma "list" (vetor).
# Para fins de aprendizado, vetor e lista (list) sao sinonimos.
list(range(10))
[0, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(5, 10, 2))
[5, 7, 9]

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tamanho = len(vetor)  # Funcao pronta (interna) do Python.
print(tamanho)
10
for i in range(tamanho):
    print('i: %s', vetor[i])


# Alernativa mais elegante.
for elemento in vetor:
    print('Elemento: %s', elemento)

# Alernativa elegante enumerada.
for i, elemento in enumerate(vetor):
    print('Elemento %s: %s', (i, elemento))

list(enumerate(vetor))
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]

nomes = ['joao', 'maria,' 'jose']
for i, elemento in enumerate(nomes):
    print('Elemento %s: %s', (i, elemento))

```
