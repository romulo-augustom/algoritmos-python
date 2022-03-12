lista1 = []
lista2 = []

for i in range(15):
  x = int(input('Digite um número: '))
  lista1.append(x)

m = int(input('\nDigite um número para multiplicar os outros números: '))

r = 0

for i in lista1:
  r = i * m
  lista2.append(r)

print(lista2)