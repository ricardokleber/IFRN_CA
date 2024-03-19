'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 19 - O sistema de avaliação de determinada
disciplina, é composto por quatro notas. A primeira
e a segunda tem peso 2, a terceira e a quarta tem
peso 3. Faça um script Python que solicita as quatro
notas de um aluno e calcula a sua média final na
disciplina.
'''
nota_1 = float(input("Digite o valor da sua PRIMEIRA nota: "))
nota_2 = float(input("Digite o valor da sua SEGUNDA nota: "))
nota_3 = float(input("Digite o valor da sua TERCEIRA nota: "))
nota_4 = float(input("Digite o valor da sua QUARTA nota: "))
media = ((nota_1*2 + nota_2*2 + nota_3*3 + nota_4*3)/10)
print("A Média Final é:",media)