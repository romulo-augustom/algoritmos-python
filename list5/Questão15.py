op=0
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))

while op!=5:  
  print('\n Escolha uma opção. \n 1 - Exibir a soma. \n 2 - Exibir a subtração. \n 3 - Exibir a multiplicação. \n 4 - Exibir a divisão. \n 5 - Sair.\n')
  op=int(input('Informe: '))

  if op==1:
    soma = n1 + n2
    print(f'\nA soma de {n1} + {n2} = {soma}')
  elif op==2:
    sub = n1 - n2
    print(f'\nA subtração de {n1} - {n2} = {sub}')
  elif op==3:
    multi = n1 * n2
    print(f'\nA multiplicação de {n1} * {n2} = {multi}')
  elif op==4:
    divi = n1 / n2
    print(f'\nA divisão de {n1} / {n2} = {divi}')
  elif op==5:
    break

print('Fim do programa')