# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# Solicitando e armazenando as notas do usuário nas variáveis
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibindo a média
print("A média das notas é:", media)