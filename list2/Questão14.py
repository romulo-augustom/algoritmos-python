# Crie um programa que recebe do usuário um número com casas decimais 
# e exiba na tela a parte inteira e a parte fracionária do número informado. 

print('Digite um número com casas decimais')
num = float(input())

inteira = int(num)
fracionaria = (num-int(num))

print(f'O valor digitado foi: {num}')
print(f'Sua parte inteira é: {inteira}')
print(f'Sua parte fracionária é: {fracionaria:.9f}')