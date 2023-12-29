#Desenvolva um programa que leia o comprimento de três retas.
#Diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('Analisador de Triângulo')
print('-='*20) #Até aqui é só para deixar bonito.
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triânculo!')
else:
    print('Os segmentos acima NÃO PODEM formar triânculo!')
