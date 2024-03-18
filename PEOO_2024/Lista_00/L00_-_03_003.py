'''
PEOO - #00 - Lista de Exercícios de Fixação
Elabore scripts Python para resolver cada uma das questões a seguir:

Questão 03 - Escreva um script Python para “desenhar” um retângulo
formado por caracteres ‘*’ (asteriscos) tendo 5 asteriscos em cada lado.

Forma de Responder 003: Utilizando FOR, IF e PRINT
'''
for linha in range(1,6):
    if linha == 1 or linha == 5:
        print('*****')
    else:
        print('*   *')