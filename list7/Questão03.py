par = []
impar = []

print('Digite números inteiros (sair para exibir):')
while True:
  try:
    x=int(input(' '))
  except:
    break

  if (x%2) == 0:
    par.append(x)
  else:
    impar.append(x)

print(f'Números pares:{par} .\nNúmeros impáres:{impar}.' )