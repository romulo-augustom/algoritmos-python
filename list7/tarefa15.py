matriz1 = ([0]*4, [0]*4, [0]*4, [0]*4)

for i in range(4):
  for j in range(4):
    matriz1[i][j] = int(input('Digite um número: '))

print(matriz1)

for i in range(4):
  lin=0
  for j in range(4):
    lin+=matriz1[i][j]
  print(lin, end=' ')

print('\n')

for i in range(4):
  col=0
  for j in range(4):
    col+=matriz1[i][j]
  print(col, end=' ')