'''
PEOO - #00 - Lista de Exercícios de Fixação
Questão 15 - Escreva um script Python onde o usuário
informa a velocidade média que o seu carro (em km/h)
geralmente corre em uma viagem e a quilometragem
(em km) até o destino e tem como resposta em quantas
horas ele levará para fazer a sua viagem.
'''
velocidade_media = float(input("Digite a velocidade media (em km/h) que seu carro corre: "))
distancia = float(input("Digite a quilometragem (em km) até o seu destino: "))
print("Você levará aproximadamente",distancia/velocidade_media," hora(s)")