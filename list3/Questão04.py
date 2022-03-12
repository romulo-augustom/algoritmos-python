print('Digite uma letra: ')
letra = input()
if letra.isalpha(): 
  if letra == 'a' or letra == 'A':
    print(f'A letra "{letra}" é VOGAL.')
  elif letra == 'e' or letra == 'E':
    print(f'A letra "{letra}" é VOGAL.')
  elif letra == 'i' or letra == 'I':
    print(f'A letra "{letra}" é VOGAL.')
  elif letra == 'o' or letra == 'O':
    print(f'A letra "{letra}" é VOGAL.')
  elif letra == 'u' or letra == 'U':
    print(f'A letra "{letra}" é VOGAL.')
  else:
    print(f'A letra "{letra}" é CONSOANTE.')
else: 
  print(f'"{letra}" não é uma letra.')
