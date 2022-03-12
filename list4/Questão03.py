print('Digite um número')
n = int(input())
for i in range (n,0,-1):
  if n%i==0:
   print(f'{n} é divisível por {i}')