'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

n = float(input("Digite um número: "))

if n >= 1:
  print("Esse número é positivo.")
elif n < 0:
  print("Esse número é negativo.")
else:
  print("Esse número é o zero (0).")