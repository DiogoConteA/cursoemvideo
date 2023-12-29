#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e,
# mostre seu status, de acordo com a tabela abaixo:
#a. Abaixo de 18.5: Abaixo do peso;
#b. Entre 18.5 e 25 : Peso ideal
#c. 25 até 30 : Sobrepeso;
#d. 30 até 40 : Obesidade;
#e. Acima de 40 : Obesidade mórbida.
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
res = altura**2
final = peso / res
print('Seu IMC é: {:.2f}'.format(final))
if final < 18.5:
    print('Você está ABAIXO DO PESO.')
elif final <=25:
    print('Você está no seu peso ideal.')
elif final <=30:
    print('Você está com SOBREPESO.')
elif final <=40:
    print('Você está no grau de OBESIDADE.')
else:
    print('Você está no grau de OBESIDADE MÓRBIDA')