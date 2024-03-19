'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 20 - Dada a figura abaixo, faça um script Python
que calcule o valor hipotenusa (h) seguindo a fórmula.
O usuário deve entrar com os valores dos dois catetos.
hipotenusa = h | cateto oposto = co | cateto adjacente = ca
h2 = co2 + ca2
'''
co = float(input("Digite o valor do cateto OPOSTO: "))
ca = float(input("Digite o valor do cateto ADJACENTE: "))
soma_catetos = (ca**2) + (co**2)
raiz_hipotenusa = soma_catetos**(1/2)
print("O valor da hipotenusa é: %.2f" % raiz_hipotenusa)