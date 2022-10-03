# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digire um angulo qualquer: '))

#math.radians(angulo)) = converte o angulo em radiano para calcular o seno/cosseno/tangente
seno = math.sin(math.radians(angulo))
cosseno =math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem seno {:.2f}'.format(angulo, seno))
print('O angulo de {} tem cosseno {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem tangente {:.2f}'.format(angulo, tangente))
