def numero(num):
  if num%2==0:
    return "True"
  if num%2!=0:
    return "False"
num = int(input('Digite um valor inteiro: '))
resp = numero(num)
if resp=="True":
  print(f'{numero(num)}, o número {num} é par.')
elif resp=="False":
  print(f'{numero(num)}, o número {num} é ímpar.')