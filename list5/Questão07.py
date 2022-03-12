print('Entrar com números positivos, para no fim exibir a média entre eles.\nAo informar um número negativo a sequência irá acabar. ')
a=1
b=0
c=0
while a>=0:
  a = int(input('Digite um número: '))
  if a>=0:
    c+=a
    b+=1
print(c/b)