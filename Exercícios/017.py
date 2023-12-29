#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
co=float(input('O cateto oposto é: '))
ca=float(input('O cateto adjacente é: '))
conta = co**2 + ca**2
x = math.sqrt(conta)
print(f'A hipotenusa é igual a: {x}')

