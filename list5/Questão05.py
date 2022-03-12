a = int(input('Digite o início do intervalo: '))
b = int(input('Digite o final do intervalo: '))
c = 0
while a<=b:
    if a%2==0 :
      c = c + a
    a = a + 1
print(f'A soma dos números pares nesse intervalo é {c}. ')