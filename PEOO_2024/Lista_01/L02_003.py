arquivo = open('agenda.txt','r')
for registro in arquivo.readlines():
    print(registro,end='')
arquivo.close()