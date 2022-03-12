num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

mdc=1

for i in range(2, num1+1):
  if num1%i==0 and num2%i==0 and i>mdc:
    mdc=i
print('MDC =', mdc)