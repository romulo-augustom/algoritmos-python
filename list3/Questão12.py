print('Qual tipo de combustível deseja colocar? ')
print('Digite A para Álcool.')
print('Digite G para Gasolina.')
combustivel = str(input())
print('Digite a quantidade de litros de combustível desejado: ')
litros = float(input())
if combustivel == str('A') and litros <= 20.00:
 valor1 = (litros*1.90)-(litros*1.90*0.03)
 print(f'O valor a ser pago será: R$ {valor1:.2f}')
elif combustivel == str('A') and litros > 20.00:
 valor2 = (litros*1.90)-(litros*1.90*0.05)
 print(f'O valor a ser pago será: R$ {valor2:.2f}')
elif combustivel == str('G') and litros <= 20.00:
 valor3 = (litros*2.50)-(litros*2.50*0.04)
 print(f'O valor a ser pago será: R$ {valor3:.2f}')
elif combustivel == str('G') and litros > 20.00:
 valor4 = (litros*2.50)-(litros*2.50*0.06)
 print(f'O valor a ser pago será: R$ {valor4:.2f}')
 