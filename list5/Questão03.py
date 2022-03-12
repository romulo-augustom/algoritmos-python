c = 1
fat = 1

num = int(input('Digite um número para cálculo fatorial: '))

while c<=num:
  fat*= c
  c+= 1

print(f'O fatorial de número {num} é = {fat}.')