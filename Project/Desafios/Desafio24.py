#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input('Digite o nome de uma cidade: ').strip()

separado = cidade.upper().split()

print(f'Esta cidade começa com "SANTO"`: {separado[0] == "SANTO"}')