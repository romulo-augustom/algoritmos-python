# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
# faça um programa que nos dê: 
##  salário bruto 
##  quanto pagou ao INSS 
##  quanto pagou ao sindicato 
##  o salário líquido

print('Quanta você ganha por hora ? ')
valorHORA = float(input())

print('Horas trabalhadas no mês: ')
horasTRAB = int(input())

salarioBRUTO = valorHORA*horasTRAB
print(f'O salário bruto será: R${salarioBRUTO:.2f} ')

INSS = salarioBRUTO*(8/100)
print(f'Quantia paga ao INSS: R${INSS:.2f}')

IR = salarioBRUTO*(11/100)
print(f'Quantia paga ao IR: R${IR:.2f}')

sindicato = salarioBRUTO*(5/100)
print(f'Quantia paga ao sindicato: R${sindicato:.2f}')

desconto = INSS+IR+sindicato

salarioLIQ = salarioBRUTO - desconto
print(f'O salário líquido será de R${salarioLIQ:.2f}')