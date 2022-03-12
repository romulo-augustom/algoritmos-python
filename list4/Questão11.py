n = int(input('Digite quantos números triangulares você deseja: '))

for i in range(1, n+1):
  print(i,'x',i+1,'x',i+2, '=',i*(i+1)*(i+2))