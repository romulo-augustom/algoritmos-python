media=0

n = int(input('Digite a quantidade de valores: '))

for i in range(n):
  b = int(input('Digite os números positivos: '))
  media=media+b

print(f'A média dos números digitados é: {media/n}')