lista1 = []
lista2 = []
lista3 = []

print('Lista 1:')
for i in range(10):
  x=float(input('Digite 10 números: '))
  lista1.append(x)

print('\nLista 2:')
for i in range(10):
  y=float(input('Digite 10 números: '))
  lista2.append(y)

c,c2=0,0

for i in range(20):
  if i%2==0:
    n=lista1[c]
    c+=1
    lista3.append(n)
  else:
    n=lista2[c2]
    c2+=1
    lista3.append(n)

print(f'\nLista 3:\n{lista3}')