print('Digite uma letra: ')
letra = input().upper()
if letra.isalpha(): 
  if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
     print(f'"{letra}" é Vogal')
  else:
     print(f'"{letra}" é Consoante')
else:
  print(f'"{letra}" não é uma letra.')