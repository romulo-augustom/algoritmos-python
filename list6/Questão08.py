def fdata(dia,mes,ano):
  x=' '
  if mes=='01':
    x=dia+" de janeiro de "+ano
  elif mes=='02':
    x=dia+" de fevereiro de "+ano
  elif mes=='03':
    x=dia+" de março de "+ano
  elif mes=='04':
    x=dia+" de abril de "+ano
  elif mes=='05':
    x=dia+" de maio de "+ano
  elif mes=='06':
    x=dia+" de junho de "+ano
  elif mes=='07':
    x=dia+" de julho de "+ano
  elif mes=='08':
    x=dia+" de agosto de "+ano
  elif mes=='09':
    x=dia+" de setembro de "+ano
  elif mes=='10':
    x=dia+" de outubro de "+ano
  elif mes=='11':
    x=dia+" de novembro de "+ano
  elif mes=='12':
    x=dia+" de dezembro de "+ano

  return x

dia = str(input('Digite o dia do mês: '))
mes = str(input('Digite o número do mês: '))
ano = str(input('Digite o ano: '))

data=fdata(dia,mes,ano)
print(data)