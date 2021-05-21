'''
Exercício Python 33:
Faça um programa que leia três números e mostre qual é o
maior e qual é o menor.
'''
a = int(input('Digite um número: '))
b = int(input('Outro número: '))
c = int(input('Mais um número: '))
#verificando quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando maior número:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor número é o {menor:.1f}.')
print(f'O maior número é o {maior}.')
