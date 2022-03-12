mas=0
fem=0
sexo=''

while sexo!='A':
  print('Digite M para sexo masculino \nDigite F para sexo feminino \nDigite A para finalizar o programa.')
  sexo=input().upper()

  if sexo!='M' and sexo!='F' and sexo!='A':
    print('Digite M ou F.')
  
  if sexo=='M':
    mas+=1
  elif sexo=='F':
    fem+=1

print(f'Foram digitados {mas} do sexo masculino.')
print(f'Foram digitados {fem} do sexo masculino.')