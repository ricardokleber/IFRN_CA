'''
PEOO - #00 - Lista de Exercícios de Fixação
 Elabore scripts Python para resolver cada uma das questões a seguir:
 
 Questão 01 - Escreva um script Python que imprime os nomes dos meses do ano um abaixo do outro.

 Forma de Responder 004: Utilizando uma LISTA (com os meses) e um FOR com um RANGE para contar
 até 12 (0 a 11) e imprimir os meses de acordo com a posição na LISTA
 '''

meses = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro',
]

for posicao in range(0,12):
    print(meses[posicao])