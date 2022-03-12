#Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário a quantidade de tinta a ser comprada e os respectivos preços em 3 situações:
##  comprar apenas latas de 18 litros;
##  comprar apenas galões de 3,6 litros;
##  misturar latas e galões, de forma que o preço seja o menor.

import math

print('Digite o tamanho da área a ser pintada: (em m²)')
area = float(input())
litros = area/6

lata18 = math.ceil(litros/18)
print(f'Somente latas de 18 Litros: {lata18};  Valor: R${lata18*80} ')

galao3_6 = math.ceil(litros/3.6)
print(f'Somente galões de 3.6 Litros: {galao3_6};  Valor: R${galao3_6*25} ')

lata18_misto = litros//18
resto = litros%18
galao3_6_misto = math.ceil(resto/3.6)
print(f'Latas de 18 Litros: {lata18_misto:.0f}, Galões de 3.6 Litros: {galao3_6_misto} ')
print(f'Valor: R${(lata18_misto*80)+(galao3_6_misto*25)}')