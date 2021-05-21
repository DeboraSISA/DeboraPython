'''
Exercício Python 16:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
import math
num = float(input('Digite um número: '))
print(f'A porçaõ inteira do número {num} é {math.trunc(num)}.')
