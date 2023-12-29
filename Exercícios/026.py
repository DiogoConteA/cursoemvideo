#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes apareceu a letra "a";
#Em que posição ela aparece pela primeira vez;
#Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))
print('A peimeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

