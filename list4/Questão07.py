par=0
imp=0
for i in range(20):
  n = int(input('Digite um número inteiro: '))
  if n%2==0:
   par=par+1
  else:
   imp=imp+1
   
print(f'Foram digitados {par} números pares e {imp} números ímpares')