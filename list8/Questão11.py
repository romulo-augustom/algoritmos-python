lista = list()
prog = dict()

def cauc(x, z):
  resp = (z*100)/x
  return (f'{resp:.2f}%')
    

x = int(input('Digite a quantidade de espaço no HD em MB: '))

while True:
  prog['Nome'] = input('Digite o nome do programa: ')
  prog['Desenvolvedor'] = input('Digite o desenvolvedor: ')
  z = float(input('Digite o espaço utilizado do programa em MB: '))
  prog["Espaço"] = cauc(x,z)
  lista.append(prog)
  print(lista)
  d = input('Deseja inserir mais um programa? [s ou n]: ')
  if d=='n' or d=='N':
    break