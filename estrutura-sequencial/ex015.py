''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto, quanto pagou ao INSS, quanto pagou ao 
sindicato, o salário líquido, calcule os descontos e o salário líquido, conforme a tabela abaixo:

•Salário Bruto : R$

•IR (11%) : R$

•INSS (8%) : R$

•Sindicato ( 5%) : R$ 

• Salário Liquido : R$ 

• Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

ganho_hora = float(input("Digite quanto você ganha por hora: "))

n_horas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = ganho_hora * n_horas

ir = ( salario_bruto * 11 ) / 100

inss = ( salario_bruto * 8 ) / 100

sindicato = ( salario_bruto * 11 ) / 100

descontos = ( ir + inss + sindicato)

salario_liquido =  salario_bruto - descontos

print("O seu salário bruto é de R$",f"{salario_bruto:.2f}")
print("Você pagou ao imposto de renda um total de R$",f"{ir:.2f}")
print("Você pagou ao inss um total de R$",f"{inss:.2f}")
print("Você pagou ao sindicato um total de R$",f"{sindicato:.2f}")
print("O total de descontos é de R$",f"{descontos:.2f}")
print("O seu salário líquido é de R$",f"{salario_liquido:.2f}")

