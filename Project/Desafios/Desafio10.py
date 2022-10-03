#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Consedere U$1.00 = R$3.27

real = float(input('Digite o valor em real: '))
dolar = real / 3.27

print('Com {} reais é possível comprar {:.2f} doláres'.format(real, dolar))

