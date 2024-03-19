while True:
    print('''
    1. Inserir Aluno
    2. Listar Alunos
    3. Sair

    ''')
    opcao = int(input('Informe a Opção: '))
    if opcao == 3:
        break
    elif opcao == 1:
        matricula = input('Informe a Matrícula: ')
        nome = input(f'[{matricula}] Nome: ')
        arquivo = open('alunos.txt','a')
        arquivo.write(f'{matricula}:{nome}\n')
        arquivo.close()
    elif opcao == 2:
        arquivo = open('alunos.txt','r')
        for registro in arquivo.readlines():
            print(registro,end='')
    else:
        print('Opção Inválida')



