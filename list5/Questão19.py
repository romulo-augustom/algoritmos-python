pior=10
melhor=0
x=1
soma=0
final=0

nome=str(input('Digite seu nome: '))

while x<=7:
  nota=float(input('Digite a nota: '))

  if nota>melhor:
    melhor=nota

  if nota<pior:
    pior=nota

  soma+=nota

  x+=1

final=(soma)-(pior+melhor)

print(f'\nAtleta: {nome} \nMelhor Nota: {melhor} \nPior Nota: {pior} \nMédia: {final/5}')