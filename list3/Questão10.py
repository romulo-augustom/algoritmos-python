print('Digite um texto: ')
texto = input()
verificaNUM = texto.isdigit()
verificaLETRA = texto.isalpha()
verificaNUMeLETRA = texto.isalnum()
if verificaNUM == False and verificaLETRA == False and verificaNUMeLETRA == True:
 print(f'O texto "{texto}" contém letras e números.')
elif verificaNUM==True:
 print(f'O texto "{texto}" contém somente números.')
elif verificaLETRA==True:
 print(f'O texto "{texto}" contém somente letras.')