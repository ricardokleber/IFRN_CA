'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 02 - Escreva um script Python que imprima os números de 1 a 9
separados por vírgula em uma única linha

Forma de Responder 003: Utilizando FOR, RANGE, PRINT e IF
'''

for numero in range(1,10):
    if numero != 9:
        print(numero,end=',')
    else:
        print(numero)