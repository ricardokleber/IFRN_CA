'''
PEOO - Lista de Exercícios de Fixação 01
Elabore scripts Python para resolver cada uma das questões a seguir:

Questão 02 - Escreva um script Python que imprima os números de 1 a 9
separados por vírgula em uma única linha

Forma de Responder 002: Utilizando uma LISTA, FOR, PRINT e IF/ELSE
'''

numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    if numero != 9:
        print(numero,end=',')
    else:
        print(numero)