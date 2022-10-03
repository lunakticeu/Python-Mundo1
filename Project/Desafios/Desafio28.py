# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
jogador = int(input('Pensei em um número entre 0 e 5. Em qual número estou pensando? '))
pc = random.randint(0, 5) # seleciona um número int aleatorio entre 0 e 5 inclusive

if(pc == jogador):
    print('Você acertou!')
else:
    print('Você ERROU')
#ou
print('Você acertou!' if pc == jogador else 'Você ERROU')