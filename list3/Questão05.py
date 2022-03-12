print('Digite a nota da primeira prova: ')
num1 = float(input())
print('Digite a nota da segunda prova: ')
num2 = float(input())
print('Digite a nota da terceira prova: ')
num3 = float(input())
media = (num1+num2+num3)/3
if media >= 6:
  print(f'A média das provas foi {media:.2f}, assim o aluno está APROVADO. ')
else:
  print(f'A média das provas foi {media:.2f}, assim o aluno está REPROVADO.')
