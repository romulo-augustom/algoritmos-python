tupla = ('Telefonou para a vítima (s ou n)?: ','Esteve no local do crime (s ou n)?: ' ,'Mora perto da vítima (s ou n)?: ','Devia para a vítima (s ou n)?: ' ,'Já trabalhou com a vítima (s ou n)?: ')

resp=dict()

sit=0

for i in range (5):
  r=str(input(tupla[i]))
  if r=='s':
     r=1
     sit+=r
  else:
     r=0
     sit+=r

if sit==2:
    print('Suspeita')
elif sit==3 or sit==4:
    print('Cúmplice')
elif sit==5:
    print('Assassino')
else:
    print('Inocente')