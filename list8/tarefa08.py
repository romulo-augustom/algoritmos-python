c1 = set()
c2 = set()
print('Primeiro usuário')
while True:
  x = input('Digite o nome da cidade que você já visitou ou 0 para sair: ')
  if x=='0':
    break
  c1.add(x)
print('Segundo usuário')
while True:
  x = input('Digite o nome da cidade que você já visitou ou 0 para sair: ')
  if x=='0':
    break
  c2.add(x)
i = c1.intersection(c2)
d1 = c1.difference(c2)
d2 = c2.difference(c1)
print(f'As cidades visaitadas por ambos foram {i}\nAs cidades visitadas somente pelo primeiro foram {d1}\nAs cidades visitadas somente pelo segundo foram {d2}')