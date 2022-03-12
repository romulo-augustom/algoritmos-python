print('Digite seu salário bruto: ')
salarioBRUTO = float(input())
print('Digite o valor da prestação: ')
prestaçao = float(input())
if prestaçao > salarioBRUTO*(30/100):
  print('O empréstimo não pode ser concedido.') 
else:
  print('O empréstimo pode ser concedido.')