lista = []

print('Digite um nome ou 0 para exibir: ')
while True:
  x = input('')
  if x=='0':
    break
  else:
    lista.append(x)

b = int(input('Escolha um opção:\n1-Para saber se um nome está na lista\n2-Para encerrar o programa\n'))

while b==1:
  n = str(input('Digite o nome que deseja procurar: '))
  if n in lista:
    print(f'{n} está na lista')
  else:
    print(f'{n} NÃO está na lista')