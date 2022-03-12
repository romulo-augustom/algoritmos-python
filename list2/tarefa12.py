# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
# faça um programa que nos dê: 
##  salário bruto 
##  quanto pagou ao INSS 
##  quanto pagou ao sindicato 
##  o salário líquido


print('Quanto você ganha por hora? ')
valorPorHora = float(input())

print('Quantas horas você trabalhou no mês? ')
horasTRAB = int(input())

salarioBRUTO = valorPorHora*horasTRAB

print('O salário bruto será:', salarioBRUTO)
print('A quantia paga ao INSS será:', salarioBRUTO*(8/100))
print('A quantia paga ao sindicato será:', salarioBRUTO*(5/100))
print('A quantia paga ao IR será:', salarioBRUTO*(11/100))
print('O salario líquido será:', salarioBRUTO -(salarioBRUTO*(8/100)+salarioBRUTO*(5/100)+salarioBRUTO*(11/100)))