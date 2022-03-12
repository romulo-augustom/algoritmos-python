lista=[]
print('Digite um nome (0 para sair): ')
while True:
  x=input('')
  if x=='0':
    break
  elif x not in lista:
    lista.append(x)
print(f'Os nomes digitados foram: {lista}. ')