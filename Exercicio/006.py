'''
Exercício Python 006:
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
num = int(input('Digite um número? '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print(f'O dobro do número {num} é {dobro}, o triplo {triplo} e sua raiz é {raiz:.2f}')
