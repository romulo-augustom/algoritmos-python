def perfeito(n):
  soma = 0
  for i in range(1,n):
    if n%i==0:
      soma+= i
  if soma==num:
    return True
  elif soma!=num:
    return False
print('Escola um opção:\n 1-Para saber se é perfeito ou não\n 0-Para encerrar o programa\n')
x = int(input('Digite: '))
while x==1:
  num = int(input('\nDigite o número: '))
  r = perfeito(num)
  if r:
    print(f'{num} é perfeito')
  else:
    print(f'{num} não é perfeito')
  print('\nEscola um opção:\n 1-Para saber se é perfeito ou não\n 0-Para encerrar o programa\n')
  x = int(input('Digite: '))
if x==0:
  print('Fim do programa')