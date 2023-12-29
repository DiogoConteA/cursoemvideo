#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
#n = int(input('Digite o ano desejado: '))
#resultado = n % 2
#if resultado == 0:
#    print('O ano {} é Bissexto'.format(n))
#else:
#    print('O ano {} não é Bissexto'.format(n))
#Meu código conteve erro, pois não fiz a exceção.

from datetime import date
ano = int(input('Que ano deseja analisar? Coloque 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} NÃO é Bissexto'.format(ano))
