''' Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem 
compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; 
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os 
valores para cima, isto é, considere latas cheias.
'''

import math


m_quadrados = float(input("Digite o tamanho da área a ser pintada em metros quadrados (M²): "))

litros = m_quadrados / 6

latas = math.ceil(litros / 18)

galoes = math.ceil(litros / 3.6)


latas_cheias = int(litros // 18)
litros_restantes = litros % 18
galoes_necessarios = math.ceil(litros_restantes / 3.6)
    

valor_latas = latas * 80
valor_galoes = galoes * 25
valor_combinacao = (latas * 80) + (galoes * 25)

if m_quadrados <= 0:
    print("Digite uma área maior do que zero metros quadrados.")

print("\nOpção 1: Comprando apenas latas de 18 litros")
print(f"Quantidade de latas necessárias: {latas}")
print(f"Preço total: R${valor_latas:.2f}")

print("\nOpção 2: Comprando apenas galões de 3,6 litros")
print(f"Quantidade de galões necessários: {galoes}")
print(f"Preço total: R${valor_galoes:.2f}")

print("\nOpção 3: Misturar latas e galões")
print(f"Quantidade de latas necessárias: {latas}")
print(f"Quantidade de galões necessários: {galoes}")
print(f"Preço total: R${valor_combinacao:.2f}")
