def maior(num1,num2,num3):
  if num1>=num2 and num1>=num3:
    return num1
  if num2>=num1 and num2>=num3:
    return num2
  if num3>=num1 and num3>=num2:
    return num3
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
print(f'O maior número digitado foi: {maior(n1,n2,n3)}')