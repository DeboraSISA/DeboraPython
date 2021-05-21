'''
Exercício Python 19:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random
a1 = input('Aluno 01: ')
a2 = input('Aluno 02: ')
a3 = input('Aluno 03: ')
a4 = input('Aluno 04: ')
lista = [a1, a2, a3, a4]
print(f'O aluno sorteado para apagar o quadro foi o "{random.choice(lista)}"')
