# Crie um programa que peça o tamanho em MB de um arquivo para download 
# e a velocidade de um link de Internet (também em Mbps). 
# Calcule e exiba o tempo aproximado de download do arquivo usando este link.

print('Digite o tamanho de um arquivo para download: (Em MB)')
arquivo = float(input())

print('Digite a velocidade de um link de Internet: (em Mbps) ')
velocidade = float(input())

tempo = arquivo/velocidade

print(f'O tempo aproximado de download do arquivo usando este link será: {tempo:.2f}segundos ')