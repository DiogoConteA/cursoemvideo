#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#a. O primeiro valor é maior;
#b. O segundo valor é maior;
#c. Não existe valor maior, os dois são iguais.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior {}'.format(n1))
elif n1 < n2:
    print('O segundo número é maior {}'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois números são iguais')
