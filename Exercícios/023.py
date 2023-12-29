#Faça um programa que leia um número de 0 a 9999 e mosre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

n = input('Digite um número de 0 a 9999: ')
s = '000' + n
print(f'Unidade: {s[-1]}')
print(f'Dezena: {s[-2]}')
print(f'Centena: {s[-3]}')
print(f'Milhar: {s[-4]}')

