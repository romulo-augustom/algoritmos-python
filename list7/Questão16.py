matriz1=[[0]*3,[0]*3,[0]*3]
matriz2=[[0]*3,[0]*3,[0]*3]
matriz3=[[0]*3,[0]*3,[0]*3]

for i in range(3):
  for j in range(3):
    print(f'Digite a posição[{i}][{j}] da Primeira Matriz:')
    matriz1[i][j] = int(input())

for i in range(3):
  for j in range(3):
    print(f'Digite a posição[{i}][{j}] da Segunda Matriz:')
    matriz2[i][j] = int(input())

for i in range(3):
  for j in range(3):
    matriz3[i][j] = matriz1[i][j] + matriz2[i][j]

print('\nPrimeira Matriz: ')
for i in range(3):
  for j in range(3):
    print(matriz1[i][j], end=' ')
  print()

print('\nSegunda Matriz:')
for i in range(3):
  for j in range(3):
    print(matriz2[i][j], end=' ')
  print()

print('\nTerceira Matriz:')
for i in range(3):
  for j in range(3):
    print('{:2}'.format(matriz3[i][j]), end=' ')
  print()