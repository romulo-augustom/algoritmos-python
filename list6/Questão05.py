def fat(num):
  a = 1
  while num>0:
    a*= num
    num-= 1
  return a
print('Escolha uma opção:\n 1-Para calcular o fatorial\n 0-Para encerrar o programa')
x = int(input())
while x==1:
  n1 = int(input('Digite um número para saber seu fatorial: '))
  print(f'O fatorial de {n1} é {fat(n1)}')
  print('\nEscolha uma opção:\n 1-Para calcular o fatorial\n 0-Para encerrar o programa')
  x = int(input())
if x==0:
  print('Fim do programa')