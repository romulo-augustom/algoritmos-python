dici = dict()

while True:
  n = input('Digite o nome do candidato: ')
  dici[n]=0
  op = input('Deseja cadastrar outro candidato? [s ou n]: ')
  if op=='N' or op=='n':
    break

while True:
  print(f'\nCandidatos: ')
  for a,b in dici.items():
    print(a)
  voto = input('\nDigite 0 para encerrar a votação\nDigite seu voto: ')
  if voto=='0':
    break
  for a,b in dici.items():
    if a==voto:
      dici[a]= b+1

print(f'\n{dici}')