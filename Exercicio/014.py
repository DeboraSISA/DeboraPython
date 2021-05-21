'''
Exercício Python 14:
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
c = float(input('Digite a temperatura em °c: '))
f = (c * 9/5) + 32
print(f'A temperatura {c:.2f}°c é equivalente a {f:.2f}°f.')
