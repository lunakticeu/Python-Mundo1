#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule
# e mostre o comprimento da hipotenusa
import math

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
hipotenusa2 = math.hypot(oposto, adjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa2))