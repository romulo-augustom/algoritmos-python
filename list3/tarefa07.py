print('Digite o país em que nasceu: ')
nacio = str(input()).lower()
if nacio == 'argentina':
  print('Sua nacionalidade é argentino.')
elif nacio == 'bolivia' or nacio == 'bolívia':
  print('Sua nacionalidade é boliviano.')
elif nacio == 'brasil':
  print('Sua nacionalidade é brasileiro.')
elif nacio == 'chile':
  print('Sua nacionalidade é chileno')
elif nacio == 'colombia' or nacio == 'colômbia':
  print('Sua nacionalidade é colombiano.')
elif nacio == 'equador':
  print('Sua nacionalidade é equatoriano.')
elif nacio == 'guiana':
  print('Sua nacionalidade é guianenseo.')
elif nacio == 'guiana francesa':
  print('Sua nacionalidade é francês.')
elif nacio == 'peru':
  print('Sua nacionalidade é peruano.')
elif nacio == 'uruguai':
  print('Sua nacionalidade é uruguaio.')
elif nacio == 'venezuela':
  print('Sua nacionalidade é venezuelano.')
elif nacio == 'suriname':
  print('Sua nacionalidade é surinamês.')
else: 
  print('Nosso banco de dados não contém tal informação.')