num = int(input('Digite um número para cálculo fatorial: '))
fat = 1
for i in range(1,num+1):
  fat = fat*i

print(f' {num} fatorial é = {fat}')