'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
 utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
'''

h = float(input("Digite a sua altura: "))

sx = (input("Digite o seu sexo: "))
if sx == "homem":
    peso_ideal = (72.7 * h) - 58
    print("O peso ideal para um homem com altura", h, "é de:", peso_ideal,"kgs.")
elif sx == "mulher":
    peso_ideal = (62.1 * h) - 44.7
    print("O peso ideal para uma mulher com altura", h, "é:", peso_ideal,"kgs.")
else:
    print("Sexo inválido. Por favor, insira 'homem' ou 'mulher'.")