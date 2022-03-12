def numero(num):
  a=0
  for i in range(1,n+1):
    if num%i==0:
      a+=1
  if a<=2:
    return True
  if a>2:
    return False
print('Escolha uma opção:\n 1-Para saber se o número é primo ou não\n 0-Para encerrar o programa')
x = int(input())
while x==1:
    n=int(input('Digite o número: '))
    print(numero(n))
    if (numero(n))==True:
      print(f'{n} é primo.')
    if (numero(n))==False:
      print(f'{n} não é primo.')
    x=int(input('\nEscolha uma opção:\n 1-Para saber se o número é primo ou não\n 0-Para encerrar o programa\n'))
if x==0:
  print('Fim do programa')