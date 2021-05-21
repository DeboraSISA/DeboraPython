'''
Exercício Python 17:
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'Para o Cateto Oposto {co} e o Cateto Adjacente {ca} temos {h:.2f} como compromimento da Hipotenusa.')
