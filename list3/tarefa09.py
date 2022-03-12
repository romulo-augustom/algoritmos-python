import os
print('Digite o primeiro número: ')
num1 = float(input())
print('Digite o segundo número: ')
num2 = float(input())
print(' Digite 1 para somar. \n Digite 2 para subtrair.  \n Digite 3 para multiplicar.  \n Digite 4 para dividir.  \n Digite 5 para sair.')
op = int(input('=> '))
if(op==1):
  print(f'A soma entre {num1} e {num2} é: {num1 + num2}')
elif(op==2):
  print(f'A subtração entre {num1} e {num2} é: {num1 - num2}')
elif(op==3):
  print(f'A multiplicação entre {num1} e {num2} é: {num1 * num2}')
elif(op==4):
  print(f'A divisão entre {num1} e {num2} é: {num1 / num2}')
else:
 os.system('clear')
 print('Obrigado por utilizar a calculadora em Python! ')