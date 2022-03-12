print('Digite seu peso: (em Kg)')
peso = float(input())
print('Digite sua altura: (em m)')
altura = float(input())
IMC = peso/(altura*altura)
if IMC < 18.5:
  print(f'IMC = {IMC:.5f} - Classificação: MAGREZA')
elif 18.5 <= IMC <= 24.9:
  print(f'IMC = {IMC:.5f} - Classificação: NORMAL')
elif 24.9 < IMC <= 29.9:
  print(f'IMC = {IMC:.5f} - Classificação: SOBREPESO')
elif 29.9 < IMC <= 39.9:
  print(f'IMC = {IMC:.5f} - Classificação: OBESIDADE')
elif 39.9 < IMC:
  print(f'IMC = {IMC:.5f} - Classificação: OBESIDADE GRAVE')
