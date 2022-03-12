par=0
impar=0
num=1
print('Informe um número para verificar se é par ou ímpar.\nPara finalizar o programa digite 0.\n ')

while num!=0:
  num=int(input('Digite o número: '))

  if num%2==0 and num!=0:
    print(f'{num} é par.')
    par+=1

  elif num%2!=0 and num!=0:
    print(f'{num} é ímpar.')
    impar+=1

  elif num==0:
    print('Fim do programa.')
      
print(f'Foram digitados {par} números pares.')
print(f'Foram digitados {impar} número ímpares.')