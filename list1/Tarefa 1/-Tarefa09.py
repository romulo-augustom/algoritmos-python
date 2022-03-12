# Crie um programa para ler dois números (num1 e num2) e imprimir as divisões entre eles. 
# Limite as casas decimais em 4. 
# Ex: num1=6 e num2=3, resultado -> 6/3 = 2 e 3/6 = 0.5

print ('Digite o primeiro numero :')
num1 = float(input())

print ('Digite o segundo numero :')
num2 = float(input())

print (f'A divisão entre {num1} e {num2} é: {num1/num2:.4f}')

print (f'A divisão entre {num2} e {num1} é: {num2/num1:.4f}')