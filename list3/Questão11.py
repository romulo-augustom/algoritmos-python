print('Telefonou para a vítima?')
a = str(input())
if(a==('sim' or 'Sim')):
  a = +1
else:
  a = 0
print('Esteve no local do crime?')
b = str(input())
if(b==('sim' or 'Sim')):
  b = +1
else:
  b = 0
print('Mora perto da vítima?')
c = str(input())
if(c==('sim' or 'Sim')):
  c = +1
else:
  c = 0
print('Devia para a vítima?')
d = str(input())
if(d==('sim' or 'Sim')):
  d = +1
else:
  d = 0
print('Já trabalhou com a vítima?')
e = str(input())
if(e==('sim' or 'Sim')):
  e = +1
else:
  e = 0
if (a+b+c+d+e) > 4:
 print('Assassino')
elif 3 <= (a+b+c+d+e) <= 4:
 print('Cúmplice')
elif (a+b+c+d+e) >= 2:
  print('Suspeito')
elif (a+b+c+d+e) < 2:
  print('Inocente')