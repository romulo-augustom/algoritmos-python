tamC=1.5
tamJ=1.1
anos=0

while tamJ<tamC:
  tamC+=0.01
  tamJ+=0.04
  anos+=1

print(f'Serão necessários {anos} anos para que Juca seja maior que Chico.\nDepois de {anos} anos, Chico estará com {tamC:.2f}m e Juca estará com {tamJ:.2f}m  ')