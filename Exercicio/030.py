'''
Exercício Python 30:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
print('Vamos pensar em um número e descobrir se ele é IMPAR ou PAR.')
num = int(input('Digite um número: '))
result = num % 2 #resto da divisão desse número dividido por 2 ( o resto da divisão de números pares é igual a 0) 30/2 o resto é 0
if result == 0:
    print('Esse número é PAR!')
else:
    print('Esse número é IMPAR!')