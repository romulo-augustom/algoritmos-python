matriz=[[0]*3,[0]*3,[0]*3]
matriz1=[[0]*3,[0]*3,[0]*3]
matriz2=[[0]*3,[0]*3,[0]*3]
for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input(f'Posição [{l}][{c}]:'))
for l in range(0,3):
  for c in range(0,3):
    matriz1[l][c] = int(input(f'Posição [{l}][{c}]:'))
matriz2[0][0]=matriz[0][0]+matriz1[0][0]
matriz2[0][1]=matriz[0][1]+matriz1[0][1]
matriz2[0][2]=matriz[0][2]+matriz1[0][2]
matriz2[1][0]=matriz[1][0]+matriz1[1][0]
matriz2[1][1]=matriz[1][1]+matriz1[1][1]
matriz2[1][2]=matriz[1][2]+matriz1[1][2]
matriz2[2][0]=matriz[2][0]+matriz1[2][0]
matriz2[2][1]=matriz[2][1]+matriz1[2][1]
matriz2[2][2]=matriz[2][2]+matriz1[2][2]

print(f'Primeira matriz: {matriz} ')
print(f'Segunda matriz: {matriz1} ')
print(f'Soma das matrizes: {matriz2} ')