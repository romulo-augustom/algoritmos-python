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
  return sl
x = int(input('Digite:\n 1 - Para saber seu salário liquido\n 0 - Para encerrar o programa\n'))
while x==1:
  b = float(input('Digite seu salário bruto e no lugar da virgula utilize ponto: '))
  print('Seu salário liquido é',round(salario(b),2),'reais')
  x = int(input('Digite:\n 1 - Para saber seu salário liquido\n 0 - Para encerrar o programa\n'))
if x==0:
  print('Fim do programa')