#Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas
# b) O nome com todas as letras minúsculas
# c) Quantas letras ao total, sem considerar os espaços
# d) Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ')
maiusculo = nome.upper()
minusculo = nome.lower()
qtd_letras_sem_espaco = len(nome) - nome.count(' ')
primeiro_nome = nome.split()
qtd_letras_primeiro_nome = len(primeiro_nome[0])

print(f'a) O nome com todas as letras maiúsculas: {maiusculo}')
print(f'b) O nome com todas as letras minúsculas: {minusculo}')
print(f'c) Quantas letras ao todo, sem considerar espaços: {qtd_letras_sem_espaco}')
print(f'd) Quantas letras tem o primeiro nome: {qtd_letras_primeiro_nome}')
print(f'd) Quantas letras tem o primeiro nome: {nome.find(" ")}')
