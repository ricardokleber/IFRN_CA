'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 13 - Considerando que um supermercado dá um
desconto de 3% para quem pagar suas compras utilizando
PIX, escreva um script Python que recebe como entrada
o valor das compras de um usuário e informa quanto ele
pagará se usar o PIX e quanto foi o seu desconto.
'''
compras = float(input("Digite o valor da sua compra: "))
desconto = compras * 3 / 100
a_pagar = compras - desconto
print("O total a pagar é de: %.2f" % a_pagar)