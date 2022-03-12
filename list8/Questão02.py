def op(a,b):
    m = 1
    d = 2 
    while d <= a:
     if a % d == 0 and b % d == 0:
        m = d
     d += 1 
    
    if a > b:
      maior = a
    else:
      maior = b
    while True:
         if maior % a == 0 and maior % b == 0:
             break
         else:
             maior += 1
    return maior, m


while True:
    a = int(input('Digite um numero inteiro: '))
    b = int(input('Digite um numero inteiro: '))
    opi = op (a, b)
    print(f'MMC: {opi[0]}\nMDC: {opi[1]}')
    ca = str(input('\nDeseja fazer outra operação? ("s" para "sim")("n" para "não"): '))
    if ca=='n':
        print('Fim do programa.')