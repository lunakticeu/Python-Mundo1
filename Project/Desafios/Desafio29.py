# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a sua velocidade em Km/h: '))

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! Você estava {velocidade - 80}kms acima do limite. Pague a multa de R${multa}')
else:
    print('Cuidado! Velocidade máxima' if velocidade == 80 else 'Abaixo da velocidade máxima')
