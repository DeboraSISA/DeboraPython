'''
Exercício Python 28:
Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
n = random.randint(0, 5) # faz o pc pensar
from time import sleep
print(' ')
print('Vou pensar em um número de 0 a 5. Será que você adivinha???')
print('.' * 59)
num = int(input('tente escobrir que número pensei: '))
print('PROCESSANDO...')
sleep(2)
if num == n:
    print(f'VOCÊ ACERTOU, QUE SORTE!!!')
else:
    print(f'GANHEI!!! Eu não pensei {num}, pensei em {n}.')
    print('Mais Sorte na proxima!')
