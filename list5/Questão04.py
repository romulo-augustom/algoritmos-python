x = int(input('Digite um número inteiro: '))
n = int(input('Digite outro número inteiro não-negativo: '))

num = x
res = 1

while res<n:
  num *= x
  res+=1

print(f'{x} elevado a {n} é = {num}')