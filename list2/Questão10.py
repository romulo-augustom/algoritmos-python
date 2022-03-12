# Crie um programa que calcula a Energia Potencial Elástica (E) de molas. 
# O usuário deve informar todos os dados necessários e o programa deve exibir o resultado no final. 
# Considere a seguinte fórmula:
# E = 1/2*k*x^2
# Onde k é a constante elástica e x a elongação da mola. 

print('Digite a constante elástica: ')
k = float(input())

print('Digite a elongação da mola: ')
x = float(input())

E = 0.5*k*x*x

print(f'A Energia Potencial Elástica de molas será: {E:.3f}')