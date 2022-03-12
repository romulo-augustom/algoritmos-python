# Crie um programa que recebe do usuário a quantidade de minutos que passaram da meia noite. 
# O programa deve exibir que horas são num formato de 24 horas. 
# Considere que o usuário informará somente valores inferiores a 1440, que equivale a um dia (60 minutos vezes 24 horas). 

print('Digite a quantidade de minutos que passaram da Meia noite: ')

t = float(input())
h = t/60

if h > 1440:
  print('Se passou mais de um dia.')
else: 
  print(f'Se passaram {int(h)}h:{(float(h)-int(h))*60:.0f}min depois da Meia noite ')