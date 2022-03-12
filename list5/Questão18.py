n = int(input('Digite a quantidade de múltiplos desejada: '))
i = int(input('Digite um número: '))
j = int(input('Digite outro número: '))

m=0
multi=0
while m<n:
  if multi%i==0 or multi%j==0:
    print(multi, end = ' ')
    m+=1

  multi+=1