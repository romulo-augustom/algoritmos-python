# Imprimir a média aritmética entre 4 números informados pelo usuário.

print('Digite o primeiro número: ')
num1 = float(input())

print('Digite o segundo número: ')
num2 = float(input())

print('Digite o terceiro número: ')
num3 = float(input())

print('Digite o quarto número: ')
num4 = float(input())

media = (num1+num2+num3+num4)/4

print(f'A média aritmética entre os 4 números digitados é: {media:.4f}')