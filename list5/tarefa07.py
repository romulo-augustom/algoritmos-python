num=0
media=0
ac=0
cont=0

print('Entrar com números positivos, para no fim calcular a média entre eles.\nInforme um número negativo para finalizar o cálculo.')

while num>=0:
  num=int(input('Digite um número: '))

  if num>0:
    cont+=1
    ac+=num

media= ac/cont
print(f'A média é {media}.')