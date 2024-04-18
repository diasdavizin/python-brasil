# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Digite quanto você ganha por hora em R$: "))

n_horas = int(input("Digite o número de horas trabalhadas no mes: "))

soma = hora * n_horas 

print("O total de seu salário no mês é de R$ ",soma)