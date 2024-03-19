'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 14 - Escreva um script Python que receba como
entrada um preço de uma mercadoria e o valor percentual
ofertado como desconto por um lojista e informe qual o
preço com desconto.
'''
valor_original = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
desconto = valor_original * percentual_desconto / 100
print("Valor a Pagar : %.2f" % (valor_original - desconto))