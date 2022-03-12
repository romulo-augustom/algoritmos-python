def salarioBruto(x):
  inss = x*(9/100)
  vale = x*(6/100)
  if x<=1903.98:
    imposto = 0
  elif x>=1903.99 and x<=2026.65:
    imposto = x*(7.5/100)
  elif x>=2026.66 and x<= 3751.05:
    imposto = x*(15/100)
  elif x>=3751.06 and x<=4664.68:
    imposto = x*(22.5/100)
  elif x>4664.68:
    imposto = x*(27.5/100)

  salarioLiquido = x - (inss+vale+imposto)
  inss_empregador = x*(8/100)
  seg_acidente = x*(0.8/100)
  fgts = x*(8/100)
  ant_multa = x*(3.2/100)

  valor_empregador = salarioLiquido + inss_empregador + seg_acidente + fgts + ant_multa + inss + vale + imposto

  return valor_empregador

salario = float(input('Digite seu salário bruto: R$ '))

print(f'O valor pago pelo empregador é: R$ {salarioBruto(salario):.2f}')