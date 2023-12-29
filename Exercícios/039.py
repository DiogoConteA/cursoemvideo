#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar;
#-Se é a hora de se alistar;
#-Se já passou do tempo do alistamento;
#Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date
print('Olá, seja bem-vindo!')
nascimento = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu no ano de {}, tem {} anos em {}.'.format(nascimento, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para você se alistar. Ainda é cedo.'.format(saldo))
    ano = atual + saldo
    print('Você se alistará no ano de: {}'.format(ano))
elif idade == 18:
    print('Está na hora de se alistar !!')
elif idade > 18:
    saldo = idade - 18
    print('Já se passaram {} anos do seu alistamento'.format(saldo))
    ano = atual - saldo
    print('Você se alistou no ano de: {}'.format(ano))