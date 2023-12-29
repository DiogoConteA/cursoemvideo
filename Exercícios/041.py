#A Confederação nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta,
#e mostre sua categoria, de acordo com a idade:
#a. Até 9 anos : MIRIM;
#b. Até 14 anos : INFANTIL;
#c. Até 19 anos : JUNIOR;
#d. Até 20 anos : SÊNIOR;
#e. Acima : MASTER.
from datetime import date
print('-=' * 20)
print('Seja bem vindo ao sistema de categoria.')
n = int(input('Por favor, digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - n
if idade <= 9:
    print('Você tem {} anos.\nA sua categoria é: MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos.\nA sua categoria é: INFANTIL.'.format(idade))
elif idade >14 and idade <= 19:
    print('Você tem {} anos.\nA sua categoria é: JUNIOR.'.format(idade))
elif idade <=25:
    print('Você tem {} anos.\nA sua cateforia é: SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos.\nA sua categoria é: MASTER.'.format(idade))
print('Boa Sorte!')
print('-=' * 20)

#posso fazer direito nos elif
#elif idade <=14:
#elif idade<=19:
#O programa entende que ele é mais velho que a categoria anterior.
#Por esse motivo posso fazer direto.