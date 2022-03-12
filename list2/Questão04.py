# Fazer um programa no qual o usuário entra com o o número de meses o dinheiro será investido. 
# Seu programa deve imprimir o saldo final.
# Considere juros simples, os quais são informados no formato 10% (obviamente sem o símbolo %). 
# Utilize a seguinte fórmula:
# SF = SI + (SI * J * N)
# Onde SF é o saldo final, SI o saldo inicial, J os juros e N o número de meses.

import math

SI = float(input('Digite o saldo inicial: '))
J = float(input('Digite a taxa de juros: '))
N = int(input('Digite o número de meses: '))

print(f'O saldo final no investimento será = {SI+(SI*(J/100)*N)} ')