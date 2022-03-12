from unittest import result


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

result = 0
for i in range(num2):
  result = result + num1

print(f'{num1} x {num2} = {result}')