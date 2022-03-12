# Crie um programa onde o usuário entra com a base e a altura de um retângulo 
# e o programa imprime o perímetro e sua área. 
# Sabe-se que perímetro = 2*(base + altura) e a area = base * altura

print('Digite a base do triângulo: ')
base = float(input())

print('Digite a altura do triângulo: ')
altura = float(input())

perimetro = 2*(base+altura)
area = base*altura

print(f'O perímetro do triângulo será: {perimetro:.3f} e a área será: {area:.3f}')