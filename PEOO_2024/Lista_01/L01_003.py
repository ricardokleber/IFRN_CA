'''
Faça um script Python que  receba registros inseridos por um usuário com
os campos: telefone (int) [que será usado como chave do registro] e os
campos nome (string) e cidade (string). A inclusão de registros deve parar
quando o usuário digitar "0" como telefone. Então o script deve solicitar
o telefone a consultar e, caso exista o registro, exibir os dados desse
registro. O script deve parar definitivamente se o usuário digitar "0"
como telefone a procurar.
'''
agenda = {}
while True:
    telefone = int(input('Telefone a inserir (só números ou digite "0" para parar): '))
    if telefone == 0:
        break
    nome = input(f'[{telefone}] Nome: ')
    cidade = input(f'[{telefone}] ({nome}) Cidade: ')
    agenda[telefone] = [nome,cidade]

while True:
    telefone = int(input('Telefone a consultar (só números ou digite "0" para parar): '))
    if telefone == 0:
        break
    if telefone in agenda.keys():
        print(f'[{telefone}] {agenda[telefone][0]} ({agenda[telefone][1]})')
    else:
        print('Telefone não consta na agenda')