# Perguntar para o usuário quantos irmão ele tem, quantas irmãs e exibir na tela o total de 
# filhos de seus pais. Ex: se o usuário tem 1 irmão e uma irmã, seus pais têm 3 filhos. 

print('Quantos irmãos você tem ? ')
irmaosQTD = int(input())

print('Quantas irmãs você tem ? ')
irmasQTD = int(input())

filhos = irmaosQTD + irmasQTD + 1

print(f'Se o usuário tem {irmaosQTD} irmãos e {irmasQTD} irmãs, seus pais tem', filhos, 'filhos ')