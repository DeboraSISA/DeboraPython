'''
Exercício Python 29:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
from time import sleep
vel = int(input('Por favor, informe a velocidade atingida: '))
print('PROCESSANDO...')
sleep(1.5)
if vel > 80:
    print('VOCÊ FOI MULTADO!')
    print(f'O limite da via é de 80Km/h')
    print(f'A multa de ultrappasagem em {vel}Km/h é de R${(vel -80) *7:.2f}.')
else:
    print('Sempre dirija com segurança!')
