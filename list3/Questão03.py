print('Digite o primeiro número: ')
num1 = float(input())
print('Digite o segundo número: ')
num2 = float(input())
print('Digite o terceiro número: ')
num3 = float(input())
if num1 > num2 and num1 > num3:
  print(f'O primeiro número "{num1}" é o maior entre eles.')
elif num2 > num1 and num2 > num3:
  print(f'O segundo número "{num2}" é o maior entre eles.')
elif num3 > num1 and num3 > num2:
  print(f'O terceiro número "{num3}" é o maior entre eles.')
else:
  print('Os maiores números são iguais.')