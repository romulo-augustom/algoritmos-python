dici = dict()

while True:
  nome = input('Nome do aluno: ')
  nota = float(input('Nota: '))
  dici[nome]=nota
  op = input('Deseja dar a nota de outro aluno? [s ou n]: ')
  if op=='N' or op=='n':
      break

for k, v in dici.items():
    print(f'{k}:{v}')
    print()
