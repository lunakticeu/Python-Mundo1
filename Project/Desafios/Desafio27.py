#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome: ').strip().split()

print(f'Primeiro nome: {nome[0]}')
qtd_nomes = (len(nome))
print(f'Último nome: {nome[qtd_nomes-1]}')


