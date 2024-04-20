'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input("Digite F para Feminino ou M para Masculino: ")

if letra == "F":
  print("Sexo feminino.")
elif letra == "M":
  print("Sexo masculino.")
else:
  print("Sexo Inválido.")