import random
rand=random.randint (1,10)
tent=0
while True:
  x = int(input('Adivinhe o número sorteado de 1 a 10: '))
  tent+=1
  if x==rand:
    print('Você acertou!')
    break
  else:
    print('Tente novamente!')
    
print (f'\nVocê tentou {tent} vezes até acertar.')



