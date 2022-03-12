print('Digite um número: ')
num = int(input())

for i in range(1,num+2):
  asterisco =''
  for y in range(1,i):
    asterisco+='*'

  print(asterisco)