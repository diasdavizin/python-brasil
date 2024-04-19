# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o raio do círculo: "))

área = 3.14159 * (raio ** 2) 

print("A área do círculo com raio de: ",raio,"é de: {:.2f}".format(área))