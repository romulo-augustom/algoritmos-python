b=0
c=0
for i in range(100):
  a=int(input('Digite um número: '))
  if 100<=a<=200:
    b=b+1
  else:
    c=c+1

print(f'Foram digitados {b} números entre 100 e 200')
print(f'{c} números não estão entre 100 e 200')