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