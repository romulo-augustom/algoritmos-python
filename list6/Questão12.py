import pg
ci=float(input('Digite o capital inicial: R$ '))
j=float(input('Digite a taxa de juros: '))
t=float(input('Digite o tempo que o dinheiro ficará aplicado: (Em Meses) '))

x = int(input('Escolha uma opção:\n 1-Para calcular o juros simples.\n 2-Para calcular o juros compostos.\n 0-Para finalizar o programa. \n'))
while x==1:
  print(f'O capital final será de: R${pg.js(ci,t,j)} ')
if x==2:
  print(f'O capital final será de: R${pg.jc(ci,t,j)} ')
if x==0:
  print('Fim do programa')