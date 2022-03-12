print('Entre com vários números inteiros. \nPara finalizar o programa digite -999.')

maior = int(input('Digite um número inteiro: '))

while True:
  n = int(input('Digite um número inteiro: '))
  if n == -999 :
    break 
  elif n > maior:
    maior =n
print(f'O maior número digitado foi {maior}')