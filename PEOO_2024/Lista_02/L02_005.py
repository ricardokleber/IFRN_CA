dicionario = {}
arquivo = open('agenda.txt','r')
for registro in arquivo.readlines():
    nome = registro.split(':')[0]
    telefone = int((registro.split(':')[1]).replace('\n',''))
    dicionario[telefone] = nome
arquivo.close()

print(dicionario)