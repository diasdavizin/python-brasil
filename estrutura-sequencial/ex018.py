'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).
'''

mb = float(input("Digite o tamanho do arquivo em MB: "))

mbps = float(input("Digite a velocidade em Mbps da internet: "))

minutos = ((mb / mbps) / 60)

print("O tempo aproximado de dowload do arquivo usando este link em minutos é de:",f"{minutos:.2f}","minutos.")