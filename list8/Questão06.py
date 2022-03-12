t = dict()

while True:
  nome = input('Nome do empregado: ')
  salario = float(input('Salario do empregado: '))
  t[nome]=salario
  op = input('Deseja colocar os dados de outro empregado? [s ou n]: ')
  if op=='N' or op=='n':
      break

while True:
    x = str(input('Digite o nome do empregado que deseja saber o salario: '))
    if x in t:
      print(t[x])
      op = input('Deseja saber sobre outro empregado? [s ou n]: ')
      if op == 'N' or op == 'n':
         break
    else:
      print('Não encontrado!')
      op = input('Deseja saber sobre outro empregado? [s ou n]: ')
      if op=='N' or op=='n':
         break       