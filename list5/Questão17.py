num=-1
op=1
cont=1
soma=0
verificaTringular=0

while op!=0:
  num = int(input('Digite um número: '))

  while cont<=num:
    soma+=cont
    if soma==num:
      verificaTringular=1
      cont=num+1
    cont=cont+1


  if verificaTringular==1:
    print(f'{num} é um número triangular \n')
  else:
    print(f'{num} não é um número triangular \n')


  print('Digite 0 para finalizar ou qualquer outro número para continuar. \n')
  op=int(input(':'))
  verificaTringular=0
  cont=1
  soma=0

print('Fim do programa.')