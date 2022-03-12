vi = int(input('Digite o valor inicial do intervalo: '))
vf = int(input('Digite o valor final do intervalo: '))

soma = 0

for a in range (vi,vf+1,2):
  if a%2==0:
    soma=soma+a
print(f'Soma dos números pares nesse intervalo é = {soma}')