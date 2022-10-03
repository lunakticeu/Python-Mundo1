#Faça um programa que leia uma frase e mostre:
# a) Quantas vezes aparece a letra "A"
# b) Em que posição a letra "A" aparece pela primeira vez
# c) Em qual posição a letra "A" aparece pela última vez

frase = input('Digite uma frase: ').strip().upper()

print(f'A letra "A" aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra "A" apareceu na posição: {frase.find("A")+1}')
print(f'A última letra "A" apareceu na posição: {frase.rfind("A")+1}')