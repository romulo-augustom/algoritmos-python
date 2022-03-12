lista = list()
while True:
  nome = input('Digite um nome (sair para exibir): ')
  if nome.lower()=='sair':
    break
  lista.append(nome)
lista.sort(reverse=True)
print(lista)