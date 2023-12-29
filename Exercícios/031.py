#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para a viagem até 200 km e R$0,45 para viagens mais longas.
distância = float(input('Digite a distância em Km desejada: '))
if distância <=200:
    pas = distância * 0.50
    print('Sua passagem custará: R${:.2f}'.format(pas))
else:
    pas2 = distância * 0.45
    print('Sua passagem custará: R${:.2f}'.format(pas2))
print('Obrigado por comprar conosco! Faça uma excelente viagem!')
