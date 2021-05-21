'''
Exercício Python 34:
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é
de 15%.
'''
a = float(input('Qual o valor do seu sálario? R$'))
if a > 1250.00:
    aumento = a + (a * 0.1)
if a <= 1250.00:
    aumento = a + (a * 0.15)
print(f'O seu salário R${a:.2f} teve um aumento e agora será R${aumento:.2f}.')
