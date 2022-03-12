# Receber do usuário o raio de um círculo e exibir sua área e seu perímetro.

print('Qual o raio do círculo ?')

r = float(input())
area = 3.14 * r * r
perimetro = 3.14 * 2 * r

print(f'A área é {area:.3f}')
print(f'O perimetro é {perimetro:.3f}')