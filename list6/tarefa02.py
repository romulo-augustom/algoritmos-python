def arearet(base,altura):
  return base*altura
def perimetroret(base,altura):
  return 2*(base + altura)

b = float(input('Digite a base do retângulo: '))
a = float(input('Digite a altura do retângulo: '))

print(f'A área do retângulo é {arearet(b,a)}')
print(f'O perímetro do retângulo é {perimetroret(b,a)}')