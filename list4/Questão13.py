a=int(input('Digite um número inteiro: '))
num=0
for i in range (1,a+1):
  if a%i==0:
    num+=1

if num<=2:
  print(f'{a} é primo')
else:
  print(f'{a} não é primo')