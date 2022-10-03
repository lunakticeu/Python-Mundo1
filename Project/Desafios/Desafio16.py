#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

import math
from math import trunc
num = float(input('Digite um número real: '))
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))
#ou
print('A porção inteira de {} é {}'.format(num, int(num)))
