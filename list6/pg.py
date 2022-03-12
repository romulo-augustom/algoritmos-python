def js(ci,j,t):
  cf = ci + ci * (j/100) * t 
  return cf
  
def jc(ci,j,t):
  cf = ci * (1 + (j/100))**t
  return cf