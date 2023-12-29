# Gerando cores em Python.
# print('\033[31mOlá, Mundo!') #Cor vermleha.

# print('\33[31;43mOlá, Mundo!')#Letra vermelha com o fundo amarelo.

# print('\33[1;31;43m Olá, Mundo!')#Letra vermelha negrito com fundo amarelo.
# A barra de cor chega lá no final e não queremos isso.

# print('\33[1;31;43mOlá, Mundo!\033[m')#Aqui o fundo para no final da frase.

# print('\33[4;97;45mOlá, Mundo!\33[m')#Letra branca e fundo branco aqui nessa atualização são: 97;107.
# O padrão aqio 30;40, é a cor preta/black.

# a = 3
# b = 5
# print('Os valores são \033[31m {} \033[me \033[33m {} \033[34m!!!'.format(a,b))

# Outra forma de colocar cor:
# nome ='Diogo'
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m' , nome , '\033[m'))

nome = 'Diogo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome , cores ['limpa']))

