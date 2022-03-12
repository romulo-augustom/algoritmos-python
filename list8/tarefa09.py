convi = set()
coleg = set()
print('Convidados da festa')
while True:
  x = input('Digite o nome do convidado ou 0 para sair: ')
  if x=='0':
    break
  convi.add(x)
print('Trabalham na sua empresa')
while True:
  x = input('Digite o nome da pessoa que trabalha com você ou 0 para sair: ')
  if x=='0':
    break
  coleg.add(x)
i = convi.intersection(coleg)
d = convi.difference(coleg)
d2 = coleg.difference(convi)
print(f'Foram no seu aniversário e trabalham com você:\n{i}\nForam ao seu aniversário e não são da empresa:\n{d}\nNão foram no seu aniversário mas trabalham na empresa:\n{d2}')