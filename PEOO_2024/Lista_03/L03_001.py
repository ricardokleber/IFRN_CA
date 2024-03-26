def par():
    print('Número Par')

def impar():
    print('Número Ímpar')

for numero in range(1,11):
    print(str(numero)+' é um ',end='')
    if numero%2 == 0:
        par()
    else:
        impar()