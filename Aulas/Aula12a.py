#Condição Simples:
#nome = str(input('Qual é o seu nome? '))
#if nome == 'Diogo':
#    print('Que nome bonito!')
#print('Tenha um bom dia, {}!'.format(nome))

#Condição Composta:
#nome = str(input('Qual é o seu nome? '))
#if nome == 'Diogo':
#    print('Que nome bonito!')
#else:
#    print('Seu nome é bem nomral.')
#print('Tenha um bom dia, {}!'.format(nome))

#Estrutura Condicional Aninhada:
#nome = str(input('Qual é o seu nome? '))
#if nome == 'Diogo':
#    print('Que nome bonito!')
#elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' :
#    print('Seu nome é bem popular no Brasil.')
#else:
#    print('Seu nome é bem nomral.')
#print('Tenha um bom dia, {}!'.format(nome))

#Colocando um elife a mais:
nome = str(input('Qual é o seu nome? '))
if nome == 'Diogo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' :
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem nomral.')
print('Tenha um bom dia, {}!'.format(nome))