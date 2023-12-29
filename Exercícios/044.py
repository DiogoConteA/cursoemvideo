#Elabore um programa que calcule o valor a ser peago por um produto,
# considerando o seu preço normal e condição de pagamento:
#a. à vista dinheiro/cheque : 10% de desconto;
#b. à vista no cartão : 5% de desconto
#c. em até 2x no cartão: preço normal;
#d. 3x ou mais no cartão : 20% de juros.
#print('{:=^40}.format (' LOJA DO DIOGO' )) (forma resumida do primeiro print) atualizado:print(f'{"Lojas Gunabara":=^40}')
print('='* 10,'LOJA DO DIOGO', '='* 10)
compra = int(input('Qual o valor da compra: R$ '))
print('''Formas de pagamento:
[1]À vista dinheiro/cheque : 10% de desconto;
[2]À vista no cartão : 5% de desconto
[3]Em até 2x no cartão: preço normal;
[4]Em 3x ou mais no cartão : 20% de juros.''')
opção = int(input('Digite a opção escolhida: '))
if opção == 1:
    total = compra - (compra * 10 / 100)
elif opção == 2:
    total = compra - (compra * 5 / 100)
elif opção == 3:
    total = compra
    parcela = compra / 2
    print('Sua compra será parcelada em 2x de R$:{:.2f}'.format(parcela))
elif opção == 4:
    total = compra + (compra * 20 / 100)
    totparc = int(input('Em quantas parcelas deseja fazer? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} vezes 1de R$:{:.2f} COM JUROS'.format(totparc , parcela ))
else:
    total = compra
    print('\33[31mOPÇÃO INVALIDA. TENTE NOVAMENTE\33[m')
print('Sua compra com o valor de R$:{:.2f}, ficou por R${:.2f}.'.format(compra, total))




