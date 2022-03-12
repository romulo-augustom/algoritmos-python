import pg
x = int(input('Digite:\n 1-Para saber o juros\n 0-Para encerrar o programa\n'))
while x==1:
  ci = float(input('Digite o capital inicial: '))
  t = float(input('Digite o tempo de investimento em meses: '))
  j = float(input('Digite o juros: '))
  y = int(input('Digite:\n 1-Para saber o juros simples\n 2-Para saber o juros composto\n'))
  if y==1:
    print('O capital final será de',round(pg.js(ci,t,j),2),'reais')
  elif y==2:
    print('O capital final será de',round(pg.jc(ci,t,j),2),'reais')
  x = int(input('Digite:\n 1 - Para saber o juros\n 0 - Para encerrar o programa\n'))
if x==0:
  print('Fim do programa')