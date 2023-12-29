#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário;
#e exceder, então o empréstimo será negado.
from time import sleep
print('-=' * 20 )
print('\33[33mBem vindo ao sistema do Banco.\33[m')
print('-=' * 20)
print('Aguarde enquanto o sistema carrega por completo...')
sleep(3)
casa =float(input('Digite o valor do imóvel: R$  '))
sal = float(input('Digite, por favor o seu salário: '))
pres = int(input('Em quantos anos pretende quitar o imóvel? '))
meses = pres*12
n = casa/meses
porcentagem = sal * 30 / 100
print('Aguarde enquanto o sistema processa seus dados...')
sleep(3)
if n <= porcentagem:
    print('PARABÉNS! O seu empréstimo foi \33[32mAPROVADO!!\n\33[m'
          'O valor de sua prestação será de: R$:{:.2f}\n'
          'O seu número de parcelas será de: {} meses'.format(n , meses))
else:
    print('Infelizmente o seu empréstimo foi \33[31mNEGADO.\n\33[m'
          'O valor da prestação é de R$:{:.2f} e excedeu a porcentagem mínima permitida de seu salário. '.format(n))
print('\33[33mObrigado por utilizar nosso banco, espero te ajudado.')
