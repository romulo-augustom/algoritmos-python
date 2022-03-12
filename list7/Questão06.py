lista1 = []

def media(x):
  soma = 0
  for i in lista1:
    soma+=i
  media = soma / len(lista1)
  return media
  
print('Digite um número (sair para exibir): ')
while True:
  try:
    x = int(input(''))
    lista1.append(x)
  except:
    break
media = media(x)
lista1.sort()
menor = lista1[0]
lista1.sort(reverse=True)
maior = lista1[0]

print(f'A média dos números é: {media}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor} ')