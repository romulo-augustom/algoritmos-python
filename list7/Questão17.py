listaSO=[]

while True:

  print('\nQual o melhor Sistema Operacional para uso em servidores?')
  x=int(input('0- Para SAIR\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n'))

  if x==0:
    break

  if x!=0 and x!=1 and x!=2 and x!=3 and x!=4 and x!=5 and x!=6:
    print('Gentileza digitar um número correspondente as opções.')

  else: 
    listaSO.append(x)

ws=listaSO.count(1)
unix=listaSO.count(2)
linux=listaSO.count(3)
net=listaSO.count(4)
mac=listaSO.count(5)
outro=listaSO.count(6)

lista2=[]

for i in range(1,7):
  if i==1:
    so='Windows Server'
    lista2.append([so,ws])
  if i==2:
    so='Unix'
    lista2.append([so,unix])
  if i==3:
    so='Linux'
    lista2.append([so,linux])
  if i==4:
    so='Netware'
    lista2.append([so,net])
  if i==5:
    so='Mac OS'
    lista2.append([so,mac])
  if i==6:
    so='Outro'
    lista2.append([so,outro])

maior=0
for i in lista2:
  if i[1]>maior:
    maior=i[1]

print('\nSistema Operacional     Votos     % ')
print('-------------------     -----    ----')
print(f'Windows Server            {ws}      {100*(ws/len(listaSO)):.1f}% ')
print(f'Unix                      {unix}      {100*(unix/len(listaSO)):.1f}% ')
print(f'Linux                     {linux}      {100*(linux/len(listaSO)):.1f}% ')
print(f'Netware                   {net}      {100*(net/len(listaSO)):.1f}% ')
print(f'Mac OS                    {mac}      {100*(mac/len(listaSO)):.1f}% ')
print(f'Outro                     {outro}      {100*(outro/len(listaSO)):.1f}% ')
print('-------------------     -----    ----')
print(f'Total                     {len(listaSO)}')

for i in lista2:
  if i[1]==maior:
    print(f'\nO Sistema Operacional mais votado foi o {i[0]}, com {i[1]} votos, correspondendo a {100*(i[1]/len(listaSO)):.1f}% dos votos. ')