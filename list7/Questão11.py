lista1=[]
lista2=[]
lista3=[]

print('Digite um número (sair para exibir): ')

while True:
  try:
    n1=float(input(' '))
    lista1.append(n1)
  except:
    break
soma=0
for i in lista1:
  soma+=i
media = soma/len(lista1)
for i in lista1:
  if i>media:
    lista2.append(i)
  elif i<media:
    lista3.append(i)

print(f'\nLista de números:{lista1}\nNúmeros acima da média:{lista2}\nNúmeros abaixo da média:{lista3}')