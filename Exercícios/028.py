#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
#import random
#n = random.randint (0,5) #faz o computador "pensar"
#jogador = int(input('Digite o número pensado: '))
#if jogador == n:
#    print('PARABÉNS, VOCÊ ACERTOU!!')
#else:
#    print('QUE PENA, VOCÊ ERROU.')
#print(n)

#Na minha resposta eu não coloquei o int e errei o sinal de ==, tinha colocado jogador:=n:
#Resposta conforme o professor

from random import randint
from time import sleep #só para dar cara de game.
comp = randint(0,5) #faz o computador "pensar"
print('-=-' * 20) #só para ficar com cara de game.
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei: ')) # Jogador tenta adivinhar.
print('PROCESSANDO...')
sleep(3)
if jogador == comp:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, jogador))
