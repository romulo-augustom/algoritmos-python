import os

os.system('clear')

v1 = 0
v2 = 0

lista = list()
lista2 = list()
dados = dict()

def alt(v1,z):
    t = len(lista)
    v1 += z
    q = v1 /t
    return q

def pes(v2,x):
    o = len(lista)
    v2 += x
    p = v2 / o
    return p

def imc(a,b):
    p = b / (a ** 2)
    return (f'{p:.2f}')

def imcd(x,z):
    r = x / (z ** 2)
    dados['imc'] = r
    lista2.append(r)

def imcf(lista2):
    return min(lista2)

def imcg(lista2):
    return max(lista2)

while True:
  dados['Nome'] = input('Digite o nome do paciente: ')
  x = float(input('Digite o peso do paciente: '))
  dados['Peso'] = x
  z = float(input('Digite a altura do paciente: '))
  dados['Altura'] = z
  imcd(x,z)
  lista.append(dados)
  os.system('clear')

  a = alt(v1,z)
  b = pes(v2,x)

  print(lista)
  print(f'A média das alturas é: {alt(v1, z)}')
  print(f'A média dos pesos é: {pes(v2, x)}')
  print(f'A média IMCs é: {imc(a, b)}')
  print(f'O menor IMC é: {imcf(lista2)}')
  print(f'O maior IMC é: {imcg(lista2)}')

  d = input('Deseja cadastrar mais um paciente? [s ou n]: ')
  if d=='n' or d=='N':
      print('Programa fechado')
      break