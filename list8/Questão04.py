lista = list()

while True:
  contat = dict()
  contat['Nome'] = input('Digite o nome: ')
  contat['Idade'] = input('Digite a idade: ')
  contat['Email'] = input('Digite o e-mail: ')
  contat['Profissão'] = input('Digite a profissão: ')
  contat['Cidade'] = input('Digite a cidade: ')
  contat['Telefone'] = input('Digite o telefone: ')
  lista.append(contat)
  op = input('\nEscolha uma opção:\n1-Para cadastrar outro usuário\n0-Para exibir\n')
  if op=='0':
    break

for c in lista:
  for k, v in c.items():
     print(f'{k}:{v}')
  print()

