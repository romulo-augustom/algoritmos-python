op=1

while op!=0:
  print(' Escolha uma opção: \n 1-Para converter Celsius para Fahrenheit. \n 2-Para converter Fahrenheit para Celsius.\n 3-Sair do programa.\n ')
  escolha = int(input('Digite: '))

  if escolha==1:
    c = float(input('\nDigite a temperatura em Celsius: '))
    f = (c*9/5)+32
    print(f'A temperatura em Fahrenheit é {f} °F\n')
  
  elif escolha==2:
    f = float(input('Digite a temperatura em Fahrenheit: '))
    c = (f-32)*5/9
    print(f'A temperatura em Celsius é {c} °C\n')

  elif escolha==3:
    break
print('Fim do programa')
  



