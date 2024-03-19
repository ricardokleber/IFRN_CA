senhas = []
arquivo = open('rockyou.txt','r',errors='ignore')
for senha in arquivo.readlines():
    senhaok = senha.replace('\n','')
    senhas.append(senhaok)

while True:
    testar = input('Qual a senha a procurar? ')
    if testar == 'pare':
        break
    if testar in senhas:
        print(f'A senha {[testar]} está no arquivo')
    else:
        print(f'A senha{[testar]} NÃO está no arquivo')