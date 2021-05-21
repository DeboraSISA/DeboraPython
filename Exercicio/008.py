'''
Exercício Python 8:
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
num = float(input('Digite uma distancia em metros: '))
cm = num * 100
mm = num * 1000
print(f'A distancia {num:.1f}m é o equivalente a {cm:.1f}cm e {mm:.1f}mm de distancia.')
