import os

os.system('cls')


def trab(empresa, foram):
    q = empresa.intersection(foram)
    return q
         

def ret(empresa, foram):
    w = empresa.difference(foram)
    return w
        

def yt(empresa, foram):
    e = foram.difference(empresa)
    return e

convidados = set()
empresa = set()
foram = set()

while True:
  os.system('clear')
  convidados.add(str(input('Digite o nome do convidado para adicionar a lista de convidados: ')))
  op = input('Deseja adicionar mais um convidado? [s ou n]: ')
  if op=='N' or op=='n':
      break

while True:
  os.system('clear')
  empresa.add(str(input('Digite o nome das pessoas que trabalham na sua empresa:')))
  op = str(input('Deseja adicionar mais uma pessoa? [s ou n]: '))
  if op == 'N' or op == 'n':
      break

while True:
  os.system('clear')
  foram.add(str(input('Digite o nome das pessoas que foram no seu aniversario: ')))
  op = input('Deseja adicionar mais uma pessoa? [s ou n]: ')
  if op=='N' or op=='n':
      break
trab(empresa, foram)


print('Os que foram no aniversario e trabalham na empresa são: ')
print(trab(empresa, foram))
print()
print('Os são trabalham na empresa e não foram são: ')
print(ret(empresa, foram))
print()
print('Os que foram no aniversario e não trabalham na empresa são: ')
print(yt(empresa, foram))