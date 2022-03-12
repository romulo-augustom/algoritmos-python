lista = []

while True:
  nome = input('Digite um nome (sair para exibir): \n')
  if nome.lower()=='sair':
    break
  lista.append(nome)

n2 = input('Digite um nome para consultar na lista: ')

c=1

for n in lista:
  if n==n2:
    print('Nome consta na lista.')
    c=1
    break

  else:
    c=0


if c==0:
  print('Nome NÃO costa na lista. ')