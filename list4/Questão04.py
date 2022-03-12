print('Digite um número X: ')
x = int(input())
print('Digite um número N: ')
n = int(input())
for i in range(1,x+1):
  if n%i==0:
   print(f'{n} é divisível por {i}')