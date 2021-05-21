'''
Exercício Python 12:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
num = float(input('Favor inserir o valor do produto: R$'))
desc = num * 0.05
new = num - desc
print(f'Você recebeu um desconto de 5%, agora pagará o valor de R${new:.2f}.')
