while True:
    nome = input('Nome: ')
    if nome == 'sair':
        break
    telefone = input('Telefone: ')
    arquivo = open('agenda.txt','a')
    arquivo.write(f'{nome}:{telefone}\n')
    arquivo.close()