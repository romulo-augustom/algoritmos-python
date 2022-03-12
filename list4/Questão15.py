print(' Série de Fibonacci')

n = int(input('Digite a quantidade de termos você deseja: '))

t1 = int(input('Digite o primeiro termo: '))
t2 = t1

print(f'{t1} . {t2} .', end='')


for i in range(1,n-1):
  t3 = t1 + t2
  print(' {}. '.format(t3),end='')
  t1 = t2
  t2 = t3