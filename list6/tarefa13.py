import math

def circulo(r):
  area = float(math.pi*(r**2))
  peri = float(2*(math.pi)*r)
  return (area,peri)

def retangulo(b,h):
  area = float (b*h)
  peri = float (2*(b+h))
  return (area,peri)

def paralelograma(b,h):
  area = float(b*h)
  peri = float(2*(b+h))
  return (area,peri)

def triangulo(b,h,a,c):
  area = float((b*h)/2)
  peri = float(b+a+c)
  return (area,peri)

while True:
  esc = int(input('Escolha uma opção para calcular a área e o perímetro:\n 1-Círculo. \n 2-Retângulo. \n 3-Paralelograma. \n 4-Triângulo. \n 5-Para sair do programa.\n '))
  if esc==1:
    try:
      raio = float(input('\nInsira o raio do círculo: '))
      x,y = circulo(raio)
      
      print(f'A área é: {x:.3} e o perímetro é: {y:.3} \n')

    except:
        print('Digite um valor. ')

  elif esc==2:
    base = float(input('\nInsira a base do retângulo: '))
    altura = float(input('Insira a altura do retângulo: '))
    x,y = retangulo(base,altura)
  
    print(f'A área é: {x:.3} e o perímetro é: {y:.3} \n')



  elif esc==3:
    base = float(input('\nInsira a base do paralelograma: '))
    altura = float(input('Insira a altura do paralelograma: '))
    [x,y] = paralelograma(base,altura)
   
    print(f'A área é: {x:.3} e o perímetro é: {y:.3} \n')

  elif esc==4:
    base = float(input('\nInsira a base do triângulo: '))
    altura = float(input('Insira a altura do triângulo: '))
    l2 = float(input('Insira o segundo lado: '))
    l3 = float(input('Insira o terceiro lado: '))
    [x,y] = triangulo(base,altura,l2,l3)
  
    print(f'A área é: {x:.2} e o perímetro é: {y:.2} \n')

  
  elif esc==5:
    print('Fim do programa.')
    break