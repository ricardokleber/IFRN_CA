lista = []
arquivo = open('agenda.txt','r')
for registro in arquivo.readlines():
    lista.append(registro.replace('\n',''))
arquivo.close()

print(lista)