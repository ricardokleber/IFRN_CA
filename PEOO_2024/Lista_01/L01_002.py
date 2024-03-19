'''
Faça um script Python que receba registros inseridos por um usuário
com os campos: aluno (string) e media (float) de 0 a 100.
A inclusão de registros deve parar quando o usuário digitar "pare"
como nome do aluno. Considerando que a média para aprovação é 60,
exiba, a partir dos registros, os nomes dos alunos aprovados e, em
seguida, os nomes dos alunos reprovados.
'''
alunos = {}
while True:
    aluno = input('Digite o nome do aluno ou "pare" para parar: ')
    if aluno == 'pare':
        break
    media = float(input(f'Digite a média de {aluno}: '))
    alunos[aluno] = media

print('''
Alunos Aprovados:
----------------
''')

for aluno,media in alunos.items():
    if media >= 60:
        print(f'{aluno}: Média = {media}')

print('''
Alunos Reprovados:
----------------
''')

for aluno,media in alunos.items():
    if media < 60:
        print(f'{aluno}: Média = {media}')


