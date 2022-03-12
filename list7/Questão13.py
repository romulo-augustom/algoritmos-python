listabit = []

for i in range(8):
  listabit.append(int(input('Digite uma sequência de 8 bits (0 ou 1): ')))

print(f'Bits recebido do usuário: {listabit}\n ')

c=0

for i in listabit:
  if i==1:
    c+=1

if c%2==0:
  listabit.append(0)
if c%2!=0:
  listabit.append(1)

print(listabit)