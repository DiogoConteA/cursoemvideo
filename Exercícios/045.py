#Crie um programa que faça o programa jogar Jokenpô com você.
from random import randint
from time import sleep
print('\033[30;45m{:=^40}\033[m'.format('Bem-vindo ao JoKenPo'))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0 , 2)
print('''Suas Opções: 
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.')
elif computador == 2: #Computador jogou Tesoura.
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMOPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE.')