listatm = []

for i in range(1,13):
  if i==1:
    t = float(input('Digite a temperatura do mês de Janeiro: '))
    m = 'Janeiro'
    listatm.append([m,t])
  
  if i==2:
    t = float(input('Digite a temperatura do mês de Fevereiro: '))
    m = 'Fevereiro'
    listatm.append([m,t])

  if i==3:
    t = float(input('Digite a temperatura do mês de Março: '))
    m = 'Março'
    listatm.append([m,t])

  if i==4:
    t = float(input('Digite a temperatura do mês de Abril: '))
    m = 'Abril'
    listatm.append([m,t])

  if i==5:
    t = float(input('Digite a temperatura do mês de Maio: '))
    m = 'Maio'
    listatm.append([m,t])

  if i==6:
    t = float(input('Digite a temperatura do mês de Junho: '))
    m = 'Junho'
    listatm.append([m,t])

  if i==7:
    t = float(input('Digite a temperatura do mês de Julho: '))
    m = 'Julho'
    listatm.append([m,t])

  if i==8:
    t = float(input('Digite a temperatura do mês de Agosto: '))
    m = 'Agosto'
    listatm.append([m,t])

  if i==9:
    t = float(input('Digite a temperatura do mês de Setembro: '))
    m = 'Setembro'
    listatm.append([m,t])

  if i==10:
    t = float(input('Digite a temperatura do mês de Outubro: '))
    m = 'Outubro'
    listatm.append([m,t])

  if i==11:
    t = float(input('Digite a temperatura do mês de Novembro: '))
    m = 'Novembro'
    listatm.append([m,t])

  if i==12:
    t = float(input('Digite a temperatura do mês de Dezembro: '))
    m = 'Dezembro'
    listatm.append([m,t])

ts=0
for x in listatm:
  ts+=x[1]

media = ts/12

print(f'\nA média das temperaturas foi: {media} °C ')

print('\nMeses em que a temperatura ficou acima da média: ')
for x in listatm:
    if x[1]>=media:
     print(f'Mês: {x[0]}')