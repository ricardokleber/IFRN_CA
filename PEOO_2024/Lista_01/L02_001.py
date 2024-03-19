for numero in range(1,1001):
    pares = open('pares.txt','a')
    impares = open('impares.txt','a')
    if numero%2 == 0:
        pares.write(str(numero)+'\n')
    else:
        impares.write(str(numero)+'\n')
    pares.close()
    impares.close()