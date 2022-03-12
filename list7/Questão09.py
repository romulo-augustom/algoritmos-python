import random
n=[]
t=[]
for v in range(10):
  n.append(random.randint(1,1000))

for i in range(5):
  c = int(input('Os números estão entre 1 e 1000\nTente acetar um dos números: '))
  t.append(c)
  if c in n:
    print('O número está na lista\n')
  else:
    print('O número não está na lista\n')

print (f'Os valores eram: {n}')
print (f'Os valores digitados foram: {t}')