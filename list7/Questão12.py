lista1 = [2,5,7]
lista2 = []

for i in range(15):
  lista2.append(int(input('Digite um número: ')))

cons = 0
pos = 0

for i, x in enumerate(lista2):
  if x==lista1[0]:
    pos=i

cons+=1
pos+=1

if lista1[1]==lista2[pos] and lista1[2]==lista2[pos+1]:
  cons+=2
else:
  cons=0

if cons==3:
  print('A sequência da lista 1 está contida na lista 2.')
else:
  print('A sequência da lista 1 NÃO está contida na lista 2.')