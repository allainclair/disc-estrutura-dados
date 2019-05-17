## Listas

É uma estrtura de dado genérica (tipo abstrado de dado), que pode ser implementada
de forma a ser estática ou dinâmica.

```
[1, 1, 2, 3, 5, 8, 11, 21, 34, 55]

['joao', 'maria', 'jose']

[1.0, 2.1, 'maria', 10, 'joao']
```

### Operações em qualquer lista

* Criar lista;
* Adicionar;
* Ler;
* Modificar/Atualizar;
* Excluir;
* Excluir lista completa (usa-se o excluir).

### Implementação

* Estática: tamanho fixo imutável;
* Dinâmica: tamanho variável mutável.

#### Estática

A lista é previamente criada em memória, logo seu tamanho é definido no começo e não
pode nem diminuir ou aumentar seu tamanho alocado em memória. Geralmente é usado
espaço em memória contíguo.

![lista-estatica](../images/list/lista-estatica.svg)

```Python tab=
SIZE = 10
lista = [0]*SIZE
lista
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista[1] = 10
lista
[0, 10, 0, 0, 0, 0, 0, 0, 0, 0]
lista[5] = 20
lista
[0, 10, 0, 0, 0, 20, 0, 0, 0, 0]
```

#### Dinâmica

A lista pode ser iniciada sem elementos, e seu tamanho pode aumentar e diminuir
de acordo com a vontade do usuário da lista.

```Python tab=
lista = []
lista
[]
lista.append(10)
lista
[10]
lista.append(11)
lista
[10, 11]
lista.insert(0, 12)
lista
[12, 10, 11]
```

```Python tab=
list_ = []  # Criar.
list_.append(10)  # Adicionar ao final.
list_.insert(0, 10)  # Adicionar 10 no indice 0.
a = list_[1]  # Ler.
list_[1] = 100   # Atualizar.
del list_[1]  # Excluir/Deletar pelo indice.
list_.remove(10)  # Excluir/Deletar valor.
del list_  # Excluir lista completa.
```

## Lista ligada

* Uma lista dinâmica chamada de **lista ligada**;
* Dados em memória não são contíguos.


![lista-dinamica](../images/list/lista-dinamica.svg)


Esse tipo de listas **não são acessadas por índices**, apenas é possível "caminhar"
pela lista para manipular elas, ou seja, para ler, adicionar, modificar e excluir
elementos da lista ligada.

![linked-list](../images/list/linked-list.svg)

Geralmente são implementadas de forma dinâmica e não contígua.

Usa-se registros com campos que apontam para outros registros para ligar os nós
da lista. 

Registro (ou classe) com campos "valor e próximo".

![linked-list-reg](../images/list/linked-list-reg.svg)