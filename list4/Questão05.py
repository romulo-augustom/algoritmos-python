maior = int(input('Digite 10 número inteiros: '))
for i in range(9):
  n = int(input('Digite um número: '))
  if n> maior:
    maior = n
print(f' O maior número é o {maior}')