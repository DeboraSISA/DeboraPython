'''
Manipulando Cadeias de Texto.
frase = 'Curso em Video Python'
Curso em Video Python
0123456789
°Fatiamento
frase = [9] -> decima letra da frase V
frase = [9:13] -> da decima até até a decima terceira (no caso do 9 até o 12) Vide
frase = [9:21]-> uma unidade acima da massa para poder mostrar a ultima.
frase = [9:21:2] -> vai mostrar pulando de 2 em 2 ( v, d, o, P, t, o.)
frase = [:5] -> mesmo que [0:5] no caso do 0 até o 4
frase = [15:] -> mesmo que [15:21]
frase = [9::3] -> Vai do 9: até o final, :3 vai pulando de 3 em 3 (V, e, P, h)
°Análise
len(frase) -> comprimento da frase (21 caracteres)
frase.count('o') -> conte quantos 'o' minusculos (3)
frase.count('o',0,13) -> considera do 0 até o 12 quantos 'o', no caso só 1.
frase.find('deo') -> quantas vezes encontrou 'deo' (la em video, posição 11)
frase.find('Android')-> se a string não existe ele da -1
'Curso'infrase -> Existe 'Curso' em frase (True)
°Transformação
frase.replace('Python', 'Android') -> vai procurar por Python e vai substituir por 'Android'
frase.upper()-> deixa em maiusculo tudo que não estava. CURSO EM VIDEO PYTHON
frase.lower()-> deixa em minusculo o que estava em maiusculo. curso em video python
frase.capitalize()-> vai deixar apenas a primeira letra maiuscula Curso em video python.
frase.title()->vai analisar quantas palavras tem e vai capitalizar cada uma. Curso Em Video Python.

frase = '   Aprenda Python  '
frase.strip()-> vai remover os espaços excedentes no começo e fim 'Aprenda Python'
frase.rstrip()->right direita, remove apenas os espaços da direita.'   Aprenda Python'
frase.lstrip()-> left esquerda, remove apenas os espaços da esqueda.'Aprenda Python  '

frase = 'Curso em Video Python'
°Divisão
frase.split()-> Onde tiver espaço vai criar uma divisão (ex abaixo)
Curso em Video Python
01234 01 01234 012345
  0   1    2     3
gera uma lista onde  cada elemento é separado pelo splitador( por padrão o space)
°Junção
'-'.join(frase)->juntar todas as frases com esse '-' caracter
Curso-em-Video-Python


'''