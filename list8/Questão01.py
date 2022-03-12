lista = []

def numeros(x):
  soma = 0
  for i in x:
    soma = soma + i
  media = soma / len(x)
  x.sort()
  menor = x[0]
  x.sort(reverse=True)
  maior = x[0]
  return menor, maior, media
print('Digite um número ou sair para parar de coletar: ')
while True:
  try:
    a = int(input(''))
    lista.append(a)
  except:
    break
r = numeros(lista)
print(f'Menor número: {r[0]}\nMaior número: {r[1]}\nMédia dos números: {r[2]}')