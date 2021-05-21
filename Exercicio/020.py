'''
Exercício Python 20:
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
a1 = input('Aluno 01: ')
a2 = input('Aluno 02: ')
a3 = input('Aluno 03: ')
a4 = input('Aluno 04: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
