def salario(bruto):
  inss = bruto * (9/100)
  vt = bruto * (6/100)
  if bruto<=1903.98:
    sl = bruto - inss - vt
  elif 1903.99<=bruto<=2826.65:
    ir = bruto * (7.5/100)
    sl = bruto - inss - vt - ir
  elif 2826.66<=bruto<=3751.05:
    ir = bruto * (15/100)
    sl = bruto - inss - vt - ir
  elif 3751.06<=bruto<=4664.68:
    ir = bruto * (22.5/100)
    sl = bruto - inss - vt - ir
  else:
    ir = bruto * (27.5/100)
    sl = bruto - inss - vt - ir
  inss2 = sl * (8/100)
  seguro = sl * (0.8/100)
  FGTS = sl * (8/100)
  antecipação = sl * (3.2/100)
  gastoemp = sl + inss2 + seguro + FGTS + antecipação
  return gastoemp
x = float(input('Digite seu salário bruto: R$ '))
print(f'Seu gasto com o empregado é de: R$ {salario(x):.2f}')