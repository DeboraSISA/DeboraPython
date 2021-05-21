'''
Exercício Python 13:
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Digite o valor do seu salário: R$'))
aum = salario * 0.15
new = salario + aum
print(f'O seu salário teve um acrescimo de 15% e agora o total é de R${new:.2f}.')
