# Receber do usuário o consumo de um carro (em litros por quilômetros) e a distância a ser percorrida. 
# Exibir quantos litros de combustível serão gastos. 

print('Digite o consumo de um carro: (em Km/L)')
consumo = float(input())

print('Digite a distância a ser percorrida: (em Km)')
km = float(input())

litros = km/consumo

print(f'Serão gastos {litros} litros de combustível')