#print('oi')
#print('oi')
#print('oi')
#Para executar três vezes de forma mais simples, posso fazer:
#for c in range (0,3):#Ele exclui o último número na contagem, por isso começar do 0.
#    print('oi')
#print('FIM')#Esse print está fora do laço
#for c in range (0 , 3):
#    print('oi')
#    print('Fim') #Aqui o comando fim entra dentro do for. Dentro do laço.

#for c in range (1, 4):#Para contar até o número desejado, colocar um número a frente. Aqui ele vai contar até 3.
#    print(c)
#print('Fim')

#Se a contagem for regressiva:
#for c in range (6 , 0 , -1): #Aqui no final eu digo qual é a iteração. Aqui ele entende como tirar 1.
#    print(c)
#print('FIM')

#Contando numeros de dois em dois:
#for c in range (0, 7, 2):
#    print(c)
#print('FIM')

#Outro exemplo:
#n = int(input('Digite um número: '))
#for c in range (0, n+1): #Pra chegar no número digitado.
#    print(c)
#print('FIM')
#Consigo ler um valor em n e usar o n como parte de passagem para o for

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range (i, f+1, p):
#    print(c)
#print('Fim')

#Lendo somente uma vez mas ele será replicado 3 vezes por estar dentro do for
#for c in range (0, 3):
#    n = int(input('Digite um valor: '))
#print('Fim')
#O for acontecendo três vezes ele pede para digitar 3 vezes. Se fosse 1000 seria a mesma coisa.

#Somando todos os valores.
s=0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n #ou S = S + N
print('A soma de todos os valores foi {}'.format(s))