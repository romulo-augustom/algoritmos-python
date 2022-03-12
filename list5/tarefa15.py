n=0
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))

while n!=5:
  n = int(input('\nEscolha uma opção:\n1-Exibir a soma\n2-Exibir a subtração\n3-Exibir a multiplicação\n4-Exibir a divisão\n5-Sair\n:'))
  if n==1:
        print(f'A soma é {n1+n2}')
  elif n==2:
        print(f'A subtração é {n1-n2}')
  elif n==3:
        print(f'A multiplicação é {n1*n2}')
  elif n==4:
        print(f'A Divisão é {n1/n2}')
print('Fim do programa')