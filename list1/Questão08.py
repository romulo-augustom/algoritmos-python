# Faça um programa que receba do usuário dois números float e exiba na tela o resultado da divisão entre eles. 
# Limite o número de casas decimais em apenas uma. 

print('Digite o primeiro numero ')
num1 = float(input())

print('Digite o segundo numero ')
num2 = float(input())

print(f'A divisão entre {num1} e {num2} é : {num1/num2:.1f}')