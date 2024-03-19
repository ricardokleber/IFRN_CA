'''
Faça uma agenda utilizando um script Python para armazenar 5 registros
(nome/telefone) informados pelo usuário em um dicionário.
Em seguida, exiba os 5 registros (um por linha).
'''
agenda = {}
for registro in range(1,6):
    nome = input('Nome a Incluir na Agenda: ')
    telefone = input(f'Telefone de {nome}: ')
    agenda[nome] = telefone

for nome,telefone in agenda.items():
    print(f'{nome}:{telefone}')
