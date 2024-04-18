''' Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = float(input("Digite um número real: "))

if n1 < 0 or n2 < 0:
    print("Esse número é inválido!")
else:
    s1 = (n1 * 2) * (n2/2)
    s2 = (n1 * 3) + n3
    s3 = (n3 * n3)

    print("O produto do dobro do primeiro com metade do segundo é de: ",s1,)
    print("A soma do triplo do primeiro com o terceiro é de: ",s2)
    print("O terceiro elevado ao cubo é de: ",s3)

