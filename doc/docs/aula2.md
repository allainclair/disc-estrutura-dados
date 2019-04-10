## "Revisão"

### Exercício da Nota Final e Média Final (NF e MF)

Um professor pretende saber se os seus alunos estão aprovados ou reprovados 
por meio de um programa em Python! O programa pede para o professor 
adicionar a Nota Final (NF) de um determinado aluno, se esse aluno não passar
com a Nota Final, o sistema também pede a Média Final (MF) desse aluno. Com
isso, o sistema pode informar se esse aluno passou ou não na disciplina do
professor. Escreva o **código fonte** em python para o professor! É 
necessário que as notas sejam dadas por meio do teclado com a função `input` 
e a saída seja impressa na tela com a função `print`.

```Python tab=
if NF >= 6.0:
    print('aprovado')
elif MF >= 5.0:
    print('aprovado')
else:
    print('reprovado')
```

### Exercício idade ano, meses para dias

Escreve um programa que leia a idade de uma pessoa expressa em anos, 
meses e dias e mostre-a expressa apenas em dias.

Transforme esse seu programa para uma função chamada `idade_dias(anos, 
meses, dias)` que recebe os 3 argumentos respectivamente e retorne a idade 
em dias.

Obs.: assumir que todos anos tenham 365 dias e que todos os meses tenham 30 
dias. (para facilitar o programa)

Ex:

```
Entrada: 10 (anos), 2 (meses), 3 (dias)
Saída: -- 
```

