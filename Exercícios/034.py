#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.
n = float(input('Digite o valor do seu salário: '))
conta = n*10/100
resultado = conta + n
c2 = n*15/100
res = c2 + n
if n > 1250:
    print('Seu salário com o aumento será de R$ {:.2f}'.format(resultado))
else:
    print('Seu salário com o aumento será de R$ {:.2f}'.format(res))