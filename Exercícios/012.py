p = float(input('Valor do produto: R$ '))
r = p*5/100
f = p-r
print('O produto que custava R$ {} passará a custar com 5% de desconto R$ {:.2f}'.format(p, f))

#para simplificar a segunda e terceira linha poderiam estar jundas. r = p - (p * 5 / 100)
