print('Série de Fibonacci')

t1 = 1
t2 = 1

print(f'{t1} . {t2} .', end='')

for i in range(1,9):
  t3 = t1 + t2
  print(' {}. '.format(t3),end='')
  t1 = t2
  t2 = t3