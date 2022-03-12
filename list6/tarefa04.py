def numero(n):
  if n%2==0:
    resp=True
  elif n%2!=0:
    resp=False
  return resp

num = float(input('Digite um número: '))
resp = numero(num)
if resp==True:
  print(f'O número {num} é par.')
elif resp==False:
  print(f'O número {num} é ímpar.')
