''' Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math


m_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados (M²): "))

litros = m_quadrados / 3

latas = math.ceil(litros / 18)

valor = latas * 80

if m_quadrados <= 0:
    print("Digite uma área maior do que zero metros quadrados.")

print("Você precisará de ",latas,"latas de tinta.")
print("Você irá pagar um total de R$",valor,"nas",f"{latas:.2f}","latas de tinta.")
