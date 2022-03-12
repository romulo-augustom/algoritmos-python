x=1

while x!=0:
  print(f'Informe um número para calcular seu triplo.\nPara finalizar o programa digite 0. ')
  x = int(input())
  num = x*3
  if num!=0:
    print(f'O triplo de {x} é {num}')

print('Fim do programa.')
