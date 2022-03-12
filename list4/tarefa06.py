a=int=0
b=int=0
c=int=0
for i in range(30):
  n = str(input('Digite seu sexo: ')).upper()
  if n=='MASCULINO'or n=='M'or n=='HOMEM'or n=='H':
   a=a+1
  elif n=='FEMININO'or n=='F'or n=='MULHER'or n=='M':
   b=b+1
  else:
   c=c+1
print(f'{a} pessoas se identificam com o sexo masculino.')
print(f'{b} pessoas se identificam com o sexo feminino.')
print(f'{c} pessoas não se identificam com os sexos masculino ou feminino.')