'''
Exercício Python 11:
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
cada litro de tinta pinta uma área de 2 metros quadrados.
'''
b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
area = b * h
tinta = area / 2
print(f'Em uma parede com {b} de largura e {h} de altura será necessário {tinta}l de tinta.')
