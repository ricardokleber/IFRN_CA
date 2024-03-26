def parouimpar(num):
    if num%2 == 0:
        return str(num)+' é um Número Par'
    else:
        return str(num)+' é um Número Ímpar'

for numero in range(1,11):
    print(parouimpar(numero))