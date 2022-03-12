def intercala(x,z):
    intercalada = []
    for a,b in zip(x, z):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada

lista1 = []
lista2 = []


while True:
  lista1.append(str(input('Digite uma cidade que ja visitou: '))) 
  op = input('Deseja informar outra cidade?? [s ou n]: ')
  if op=='N' or op=='n':
      print ('Agora outra pessoa informará')
      break
print()
while True:
  lista2.append(str(input('Digite uma cidade que ja visitou: ')))
  op = input('Deseja informar outra cidade?? [s ou n]: ')
  if op=='N' or op=='n':
      break

listaIntercalada = intercala(lista1, lista2)

print(f'As cidades visitadas foram: ')
print(listaIntercalada)
print()
print(f'As cidades visitadas apenas pela primeira pessoa foram: ')
print(lista1)
print()
print(f'As cidades visitadas apenas pela segunda pessoa foram: ')
print(lista2)