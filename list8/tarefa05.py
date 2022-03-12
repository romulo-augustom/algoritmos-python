dici = dict()

q=int(input('Digite a quantida de alunos deseja cadastrar: '))
for i in range(q):
  nome = input('Nome do aluno: ')
  nota = float(input('Nota: '))
  dici[nome]=nota
for k,v in dici.items():
  print('\n',k,':',v)