'''
Exercício Python 18:
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = int(input('Digite o ângulo:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'Para o ângulo {angulo}° temos o Seno de {sen:.2f}, o Cosseno {cos:.2f} e a Tangente {tan:.2f}.')
