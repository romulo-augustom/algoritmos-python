lista=[]
print('Digite uma lista de nomes, para finalizar digite 0')
while True:
  x=input('')
  if x=='0':
    break
  elif x in lista:
    print('Digite outro nome, essse já está salvo')
  else:
    lista.append(x)
print(lista)