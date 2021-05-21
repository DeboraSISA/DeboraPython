# import emoji
# nome = str(input('Digite seu nome: '))
#
# if nome == 'Debora':
#     print(emoji.emojize('Que nome lindo você tem! :heart_eyes:', use_aliases=True))
# else:
#     print(emoji.emojize('Seu nome é tão normal! :neutral_face:', use_aliases=True))
# print(f'Boa noite, {nome}')
#
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}.')
# if m >= 6:
#     print('Sua média foi boa! PARABÉNS!!!')
# else:
#     print('Sua média efoi ruim! Precisa estudar mais!')
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')
