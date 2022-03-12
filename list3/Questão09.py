import os
print('Digite um número real: ')
num1 = float(input())
print('Digite outro número real: ')
num2 = float(input())
print('Digite 1 para somar')
print('Digite 2 para subtrair')
print('Digite 3 para multiplicar')
print('Digite 4 para dividir')
print('Digite 5 para sair')
soma = num1+num2
sub = num1-num2
multi = num1*num2
divi = num1/num2
op = int(input())
if(op==1):
  print(f'O resultado de {num1} + {num2} = {soma}')
elif(op==2): 
  print(f'O resultado de {num1} - {num2} = {sub}')
elif(op==3):
  print(f'O resultado de {num1} x {num2} = {multi}')
elif(op==4):
  print(f'O resultado de {num1} / {num2} = {divi}')
elif(op==5):
  print(os.system('clear'))
  print('Obrigado por utilizar a calculadora em Python! ')
else:
  print('Opção inválida.')