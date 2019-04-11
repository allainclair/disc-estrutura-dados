## Algumas formas de `print` *

```Python tab=
print('Print com mais do que um argumento', arg1, arg2)

print('dez', 10, sep='')

print('Uso do operador "percentage" para string: %s %s' % (string1, string2))

# Python Version >= 3.7
string = 'uma string'
print(f'Uma string com interpotalacao: {string}')

print(
    'Evitar linhas de codigos muito extensas pois dificulta a leitura do seu '
    'codigo, entao essa eh uma forma de vc quebrar a linha. Existe uma regra '
    'de no maximo 79-80 colunas de codigo, tente usar ela, soh que nao tem '
    'problema se passar de 80 ou chegar ateh umas 85 colunas. Essa formatacao '
    'de codigo desse print pode ser usada nos codigos tambem.')

print(
    'para quebrar a linha '
    'use dessa forma')

funcao(
    argumento1, argumento2, argumento3, argumento4, argumento5, argumento6,
    argumento7, argumento8)
```

## Estrutura de dado **lista**

Podemos chamar até de vetor, *array*, arranjo, sequência, pois uma lista tem
uma **ordem definida** de elementos e os elementos de uma lista também **podem
ser repetidos**.

```Python tab=
lista_de_numeros = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
lista_de_letras = ['a', 'b', 'c', 'x', 'y', 'z']
lista_mista = [0, 1, 'a', 'b', 'c', 'string', 1.1]
people_list = ['allan', 'maria', 'jose', 'enzo', 'valentina']

lista_mista[3]
'b'

people_list[3]
enzo

len(people_list)
5

people_list.append('allan')

people_list.count('allan')

people_list.insert(1, 'lucas')

people_list.remove('allan')

lista_de_numeros + lista_de_letras

[-1, 0, 1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'x', 'y', 'z']

people_list.pop()
'lucas'
```

## PARAMOS AQUI!!!!!

