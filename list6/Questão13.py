import pt

while True:
  esc = int(input('Escolha uma opção para calcular a área e o perímetro:\n 1-Círculo. \n 2-Retângulo. \n 3-Paralelograma. \n 4-Triângulo. \n 5-Para sair do programa.\n '))
  if esc==1:
    try:
      raio = float(input('\nInsira o raio do círculo: '))
      x,y = pt.circulo(raio)
      
      print(f'Área: {x:.3} \nPerímetro: {y:.3} \n')
    except:
        print('Digite um valor. ')

  elif esc==2:
    base = float(input('\nInsira a base do retângulo: '))
    altura = float(input('Insira a altura do retângulo: '))
    x,y = pt.retangulo(base,altura)
  
    print(f'Área: {x:.3} \nPerímetro: {y:.3} \n')


  elif esc==3:
    base = float(input('\nInsira a base do paralelograma: '))
    altura = float(input('Insira a altura do paralelograma: '))
    [x,y] = pt.paralelograma(base,altura)
   
    print(f'Área: {x:.3} \nPerímetro: {y:.3} \n')

  elif esc==4:
    base = float(input('\nInsira a base do triângulo: '))
    altura = float(input('Insira a altura do triângulo: '))
    l2 = float(input('Insira o segundo lado: '))
    l3 = float(input('Insira o terceiro lado: '))
    [x,y] = pt.triangulo(base,altura,l2,l3)
  
    print(f'Área: {x:.2} \nPerímetro: {y:.2} \n')
  
  elif esc==5:
    print('Fim do programa.')
    break