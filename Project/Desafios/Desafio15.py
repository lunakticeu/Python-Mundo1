#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kms = float(input('Quantos Kms foram percorridos com o veículo: '))
dias = int(input('Por quantos dias o veículo foi alugado: '))

preco = (kms * 0.15) + (dias * 60)

print('O preço a pagar por {}Kms percorridos e {} dias de uso é R${:.2f}'.format(kms, dias, preco))
