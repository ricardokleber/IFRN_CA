def par():
    return 'Número Par'

def impar():
    return 'Número Ímpar'

for numero in range(1,11):
    print(str(numero)+' é um ',end='')
    if numero%2 == 0:
        print(par())
    else:
        print(impar())