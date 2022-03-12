print('Use M para o sexo Masculino.')
print('Use F para o sexo Feminino.')

ma = 0
fe = 0
x = 0

for i in range(30):
  soma = str(input('Digite seu sexo: ')).upper()
  if soma == 'M':
    ma = ma+1
  elif soma == 'F':
    fe = fe+1
  else:
    x=x+1

print(f'{ma} pessoas se identificam com o sexo masculino.')
print(f'{fe} pessoas se identificam com o sexo feminino.')
print(f'{x} pessoas não se identificam com os sexos masculino ou feminino.')