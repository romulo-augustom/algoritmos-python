num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

mult1=0
verificaMMC=0
maiorNum=0

if num1>num2:
  maiorNum=num1
else:
  maiorNum=num2

for x in range(2,maiorNum+1):
  if verificaMMC==1:
    break
  else:
    mult1=num1*x

  for y in range(2,maiorNum+1):
    if mult1==num2*y:
      print(f'MMC = {mult1} ')
      verificaMMC=1
      break