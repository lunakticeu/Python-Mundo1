# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Dogite um número: '))
resto = num % 2 # resto da divisão

print('Número PAR' if resto == 0 else 'Número IMPAR')
