coluna1=coluna2=coluna3=coluna4=0
linha1=linha2=linha3=linha4=0
matriz=[[0]*4,[0]*4,[0]*4,[0]*4]
for l in range(0,4):
  for c in range(0,4):
    matriz[l][c] = int(input(f'Digite a posição [{l}][{c}]:'))
print(matriz)
for l in range(0,4):
  coluna1+=matriz[l][0]
  coluna2+=matriz[l][1]
  coluna3+=matriz[l][2]
  coluna4+=matriz[l][3]
print(f'A soma da 1º coluna é {coluna1}.\nA soma da 2º coluna é {coluna2}.\nA soma da 3º coluna é {coluna3}.\nA soma da 4º coluna é {coluna4}')
linha1+=matriz[0][0]+matriz[0][1]+matriz[0][2]+matriz[0][3]
linha2+=matriz[1][0]+matriz[1][1]+matriz[1][2]+matriz[1][3]
linha3+=matriz[2][0]+matriz[2][1]+matriz[2][2]+matriz[2][3]
linha4+=matriz[3][0]+matriz[3][1]+matriz[3][2]+matriz[3][3]
print('A soma da 1º linha é:',linha1,'\nA soma da 2º linha é:',linha2,'\nA soma da 3º linha é:',linha3,'\nA soma da 4º linha é:',linha4,)