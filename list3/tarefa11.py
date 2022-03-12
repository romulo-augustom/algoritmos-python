print('Responda com sim ou não')
a = str(input('Telefonou para a vítima?: '))
b = str(input('Esteve no local do crime?: '))
c = str(input('Mora perto da vítima?: '))
d = str(input('Devia para a vítima?: '))
e = str(input('Já trabalhou com a vítima?: '))
if a=='sim' or a=='Sim' or a=='SIM':
    a = 1
elif a=='NÃO' or a=='não' or a=='Não' or a=='nao' or a=='NAO' or a=='Nao':
    a=0

if b=='SIM' or b=='sim' or b=='Sim':
    b=1
elif b=='NÃO' or b=="não" or b=='Não' or b=='nao' or b=='NAO' or b=='Nao':
    b=0

if c=='sim' or c=='Sim' or c=='SIM':
    c = 1
elif c=='NÃO' or c=='não' or c=='Não' or c=='nao' or c=='NAO' or c=='Nao':
    c=0

if d=='sim' or d=='Sim' or d=='SIM':
    d = 1
elif d=='NÃO' or d=='não' or d=='Não' or d=='nao' or d=='NAO' or d=='Nao':
    d=0

if e=='sim' or e=='Sim' or e=='SIM':
    e = 1
elif e=='NÃO' or e=='não' or e=='Não' or e=='nao' or e=='NAO' or e=='Nao':
    e=0
s = a+b+c+d+e
if s==2:
    print('Você é suspeito')
elif 3<=s<=4:
    print('Você é cúmplice')
elif s==5:
    print('Você é o assassino')
else:
    print('Você é inocente')