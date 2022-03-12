# Fazer um programa como o anterior, mas com juros compostos. Utilize a seguinte fórmula:
# SF = SI * (1+J)^N

import math

SI = float(input('Digite o saldo inicial: '))
J = float(input('Digite a taxa de juros: '))
N = int(input('Digite o número de meses: '))

print(f'O saldo final no investimento será = {SI*(1+(J/100))**N} ')