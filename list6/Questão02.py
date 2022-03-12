def area(base,altura):
  return base*altura
def perimetro(base,altura):
  return 2*(base+altura)
base=float(input('Digite a base do retângulo: '))
altura=float(input('Digite a altura do retângulo: '))
a = area(base,altura)
b = perimetro(base,altura)
print(f'A área do retângulo é {a}')
print(f'O perímetro do retângulo é {b}')