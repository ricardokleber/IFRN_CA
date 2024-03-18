'''
PEOO - #00 - Lista de Exercícios de Fixação
 Elabore scripts Python para resolver cada uma das questões a seguir:
 
 Questão 01 - Escreva um script Python que imprime os nomes dos meses do ano um abaixo do outro.

 Forma de Responder 005: Utilizando uma LISTA (com os meses) e um FOR com um RANGE para contar
 até o número de itens da LISTA (usando LEN) e imprimir os meses de acordo com a posição na LISTA
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

for posicao in range(0,len(meses)):
    print(meses[posicao])