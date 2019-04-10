def main():
    nota_final = input('Entre com a nota final do aluno: ')
    print('Nota final:', nota_final)

    tipo_da_nota_final = type(nota_final)
    print('Tipo da variavel nota_final', tipo_da_nota_final)
    nota_final_float = float(nota_final)
    
    if nota_final_float >= 6.0:
        print('Aluno passou com nota final!', nota_final)
    else:
        print('Aluno nao passou com nota final!', nota_final)
        media_final = input('Entre com a media final do aluno: ')
        print('Media final do aluno: ', media_final)
        print('Tipo da variavel media_final', type(media_final))

        if float(media_final) >= 5.0:
            print('Aluno passou com media final:', media_final)
        else:
            print('Aluno nao passou com media final:', media_final)


if __name__ == '__main__':
    main()
