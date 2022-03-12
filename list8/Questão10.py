import os

os.system('clear')

lista = list()


def insert():
	filmes = dict()
	os.system('clear')
	filmes['nome'] = input('Digite o nome do filme: ')
	filmes['genero'] = input('Digite o genero do filme: ')
	filmes['duração'] = input('Digite e a duração do filme: ')
	lista.append(filmes)

def exib(lista):
  os.system('clear')
  print (lista)

def search(lista):
  os.system('clear')
  x = str(input('Digite o nome do filme que deseja buscar: '))
  verifica = 0
  for i in lista:
      if i['nome'] == x:
          print(i)
          verifica+=1
  if verifica==0:
      print('Filme não encontrado')

def dele(lista):
  os.system('clear')
  x = str(input('Digite o nome do filme que deseja buscar: '))
  verifica = 0
  for i in lista:
      if i['nome'] == x:
          lista.remove(i)
          verifica = verifica + 1
  if verifica == 0:
      print('Filme não encontrado')  

while True:
   print('Escolha uma opção do menu:')
   print('[1] Inserir um novo filme')
   print('[2] Exibir todos os filmes')
   print('[3] Procurar filme pelo nome')
   print('[4] Excluir um filme')
   print('[5] Sair')
   x = str(input('Digite: ')) 
   if x=='1':
       insert()
   elif x=='2':
       exib(lista)
   elif x=='3':
       search(lista)
   elif x=='4':
       dele(lista)
   elif x=='5':
       print('Programa encerrado')
       break
    