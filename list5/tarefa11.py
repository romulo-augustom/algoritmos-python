c=0
num=1
print(' Informe um número para verificar se é primo.\n Para finalizar o programa digite 0.\n ')
while num!=0:
  num=int(input('Digite o número: '))

  for x in range(1,num+1):
    if num%x==0:
      c+=1

  if num!=0:
    if c==2:
      print(f'\nO número {num} é PRIMO.\n')
    else:
      print(f'\nO número {num} NÃO É PRIMO.\n')

  c=0
print('\nFim do programa.')