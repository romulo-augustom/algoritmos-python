aprov = []
reprov = []

x = int(input('Escolha uma opção:\n1 - Para coletar os dados\n2 - Para encerrar o programa\n'))

while x==1:
  n = str(input('Digite o nome do aluno: '))
  m = float(input('Digite a nota do aluno: '))
  if m>=60:
    aprov.append(n)
  else:
    reprov.append(n)
  x = int(input('\nEscolha uma opção:\n1 - Para coletar os dados\n2 - Para encerrar o programa\n'))
  
print(f'\nAlunos com a nota acima da média:\n{aprov}\nAlunos com a nota abaixo da media\n{reprov}')