# Crie um programa que calcula a aceleração média (a) de um carro durante um aumento de velocidade. 
# O usuário deve informar a velocidade inicial (Vi), a velocidade final (Vf) 
# e o tempo (Δt) gasto para que a velocidade passe de Vi para Vf.


print('Digite a velocidade inicial do carro: ')
Vi = float(input())

print('Digite a velocidade final do carro: ')
Vf = float(input())

print('Digite o tempo gasto para atingir a velocidade final: ')
t = float(input())

a = (Vf-Vi)/t

print(f'A aceleração média durante esse aumento de velocidade será: {a:.3f}')