print('Digite alguns números, o programa termina quando 0 for inserido.')
a=1
b=0
while a>0:
    a = int(input('Digite os números: '))
    if 100<a<200:
        b+=1
print(f'{b} números estão entre 100 e 200')