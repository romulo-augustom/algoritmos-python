# Calcular a hipotenusa de um triângulo retângulo cujos cateto
# Observação: NÃO utilize a função math.hypot()

import math

print('Digite o valor de um cateto do triângulo: ')
cat1 = float(input())

print('Digite o valor do outro cateto do triângulo: ')
cat2 = float(input())

hipo = (cat1*cat1)+(cat2*cat2) 
hipotenusa = math.sqrt(hipo)

print(f'A hipotenusa desse triângulo é: {hipotenusa:.4f} ')