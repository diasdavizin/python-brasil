'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''

altura = float(input("Digite a sua altura: "))

peso_ideal = (72.7 * altura ) - 58

print("Sua altura é de: ", altura, "e o seu peso ideal é de:", f"{peso_ideal:.2f}", "kgs.")
