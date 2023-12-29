salario = float(input('Valor do salário: R$ '))
aumento = salario + (salario * 15 / 100)
print('O salário é {} e passará a ser com o aumento de 15%, R$ {:.2f} '.format(salario, aumento))
