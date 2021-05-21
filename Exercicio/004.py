'''
Exercício Python 4:
Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele.
'''
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaço?', a.isspace())
print('É numero?', a.isnumeric())
print('É alphanumerico?', a.isalnum())
print('É alfabetico?', a.isalpha())
print('É maiuscula?', a.isupper())
print('É minuscula?', a.islower())
print('É capitalizada?', a.istitle())

