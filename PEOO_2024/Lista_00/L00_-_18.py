'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 18 - Escreva um script Python que calcula o IMC
(Índice de Massa Corporal) de uma pessoa. Para isso o
script deve solicitar o peso e a altura do usuário e
informar seu IMC ( a fórmula do IMC = peso / altura2 )
'''
peso = float(input("Digite o valor do seu peso: "))
altura = float(input("Digite a sua altura: "))
print("Seu IMC é : %.2f" % (peso / altura**2))