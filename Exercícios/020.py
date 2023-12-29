#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem dos sorteados.

#import random
#a1 = str(input('Nome do primeiro aluno: '))
#a2 = str(input('Nome do segundo aluno: '))
#a3 = str(input('Nome do terceiro aluno: '))
#a4 = str(input('Nome do quarto aluno: '))
#lista = [a1, a2, a3, a4]
#seq = random.shuffle(lista)
#print(f'A sequência de apresentação será:\n {lista}')

#simplificando

from random import shuffle
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A sequência de apresentação será: \n {lista}')

