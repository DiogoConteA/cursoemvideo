#Escreva um programa que leia a velocidade de um carro.
#Se ele utrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
import math
v = float(input('Digite a velocidade do carro: ' ))
if v>80:
    print('Você excedeu o limite de velocidade e foi multado!')
    print('O valor da multa é de RS7,00 por km/h excedido.')
    n1 = v-80
    n2 = n1*7
    print('O valor da sua multa é:{:.2f} R$.'.format(n2))
else:
    print('Está tudo bem, você respeitou a velocidade')

#Resposta Professor
#velocidade = float(input('Qual é a velocidade atual do carro? '))
#if velocidade>80:
#    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
#    multa = (velocidade-80)*7]
#    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
#print('Tenha um bom dia! Dirija com segurança!')