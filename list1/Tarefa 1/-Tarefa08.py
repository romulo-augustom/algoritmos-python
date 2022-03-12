# Faça um programa que receba do usuário dois números float e exiba na tela o resultado da divisão entre eles. 
# Limite o número de casas decimais em apenas uma. 

num1 = float(input('Digite o primeiro valor: '))

num2 = float(input('Digite o segundo valor: '))

print(f'A divisão entre {num1} e {num2} é : {num1/num2:.1f}')