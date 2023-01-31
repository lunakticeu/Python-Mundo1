# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância até o destino em Kms? '))

if (distancia <= 200):
    print('O preço de sua passagem custará R${:.2f}'.format(distancia * 0.5))
else:
    print('Sua viagem é longa né? A passagem custará R${:.2f}'.format(distancia * 0.45))
