''' Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

fahrenheit = float(input("Digite a temperatura em º Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print(fahrenheit,"º Fahrenheit em º Celsius é de: {:.2f}".format(celsius),"º.")