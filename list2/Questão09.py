# Crie um programa que calcula a área de uma esfera. 
# Utilize a seguinte fórmula:
# A = 4 * * r^2

print('Digite o raio da esfera: ')

raio = float(input())
pi = 3.14
area = raio*raio*4*pi

print(f'A área da esfera de raio {raio} será: {area:.3f}')