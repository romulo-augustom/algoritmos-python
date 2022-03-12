def temp(c):
  return(c*(9/5)+32)
print('Escolha uma opção:\n 1-Para fazer a conversão de °C para °F\n 0-Para finalizar o programa\n')
esc = int(input('Digite: '))
while esc==1:
  c = float(input('\nDigite a temperatura em °C: '))
  print(f'{temp(c)} °F')
  print('\nEscolha uma opção:\n 1-Para fazer a conversão de °C para °F\n 0-Para finalizar o programa\n')
  esc = int(input('Digite: '))
if esc==0:
  print('Fim do programa')