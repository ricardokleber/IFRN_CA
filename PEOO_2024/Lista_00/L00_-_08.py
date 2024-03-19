'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 08 - Considerando que um servidor público terá um aumento em
seu salário de 9%, escreva um script Python onde o usuário informa seu
salário atual e tem como resposta o seu salário calculado com o
referido aumento.
'''
salario = float(input("Digite o valor do salário: "))
aumento = salario * 9 / 100
novosalario = salario + aumento 
print("O Novo Salário Será : %.2f" %novosalario)