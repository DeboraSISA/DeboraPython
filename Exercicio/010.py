'''
Exercício Python 10:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
real = float(input('Quanto você tem na carteira? R$'))
dollar = real / 5.35
print(f'O valor R${real:.2f} é equivalente a US${dollar:.2f}')
