def MDC(a,b):
  mdc = 1
  for i in range(2, a+1):
    if a%i==0 and b%i==0 and i>mdc:
      mdc = i
  return mdc
def MMC(a,b):
  mult1=0
  verificaMMC = 0
  maiorNum = 0
  if a>b:
    maiorNum = a
  else:
    maiorNum=b
  for x in range(2,maiorNum+1):
    if verificaMMC==1:
      break
    else:
      mult1=a * x
    for y in range(2,maiorNum+1):
      if mult1==b * y:
        verificaMMC=1
        break
  return mult1
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(f'O MDC é {MDC(num1,num2)}')
print(f'O MMC é {MMC(num1,num2)}')