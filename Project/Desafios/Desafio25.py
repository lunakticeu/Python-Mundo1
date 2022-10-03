#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input('Digite o seu nome: ').strip()
nome = nome.upper()
print(f'Seu nome tem a palavra "Silva"? {"SILVA" in nome}')