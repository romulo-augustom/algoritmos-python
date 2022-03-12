# Converter uma temperatura fornecida pelo usuário de graus Farenheit para graus Celsius. 
# Utilize a seguinte fórmula: 
# C = (5 * (F-32) / 9). 
# Onde C é a temperatura em Celsius e F a temperatura em Farenheit.

print('Digite a temperatura em Farenheit: ')
F = float(input())

C = (5*(F-32)/9)

print(f'A temperatura em Celsius será: {C:.2f}')