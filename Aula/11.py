'''
   ANSI
ESCAPE SEQUENCE

\033[m
STYLE
0 None
1 Bold (negrinha)
4 underline (sublinhado)
7 Negative (inverte fundo com letra)
TEXT
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 lilas
36 tiffany
37 cinza
BACK
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 lilas
46 tiffany
47 cinza
'''
'''
\033[0;30;41m #style;text;back
\033[4;33;44m #sublinhado;amarelo;azulm
\033[7;30m #inverter;branco (vai inverter a letra com o fundo)
'''
print('\033[1;30;40mOlá, bb!\033[m')