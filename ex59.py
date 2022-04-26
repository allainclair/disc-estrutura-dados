def tratar_numero(numero, pilha, fila):
    if numero > 0:
        pilha.append(numero)
    elif numero < 0:
        fila.append(numero)
    else:
        print('Zero nao eh valido')


def remover_pilha_para_fila(pilha, fila):
    elemento = pilha.pop()
    fila.append(elemento)


def remover_fila_para_pilha(pilha, fila):
    elemento = fila.pop(0)
    pilha.append(elemento)


def main():
    pilha = []
    fila = []
    opcao = '1'
    while opcao != '0':
        print('Opção 1')
        print('Opção 2')
        print('Opção 3')
        print('Opção 0 - SAIR')

        opcao = input('Escolha a opção: ')
        if opcao == '1':
            numero = int(input('Escolha um numero (positivo ou negativo): '))
            tratar_numero(numero, pilha, fila)
        elif opcao == '2':
            remover_pilha_para_fila(pilha, fila)
        elif opcao == '3':
            remover_fila_para_pilha(pilha, fila)

        print('pilha', pilha)
        print('fila', fila)


if __name__ == '__main__':
    main()
