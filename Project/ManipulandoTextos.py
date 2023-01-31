frase = 'Curso em Vídeo Python'
frase2 = '     Curso em Vídeo Python    '

print('\nFatiamento de textos')
print(f'O caracter na posição 3 é: {frase[3]}')
print(f'Do caracter 13 até o final é: {frase[13:]}')
print(f'Do caracter 1 até o 14 é: {frase[1:15]}')
print(f'Do caracter 1 até o 14 pulando de 2 é: {frase[1:15:2]}')
print(f'Do caracter 1 até o final pulando de 3 é: {frase[1::3]}')

print('\nAnálise de textos')
print(f'O comprimento desta frase é: {len(frase)}')
print(f'Nesta frase tem {frase.count("o")} caracteres "o"')
print(f'Nesta frase tem {frase.upper().count("o")} caracteres "O" maiusculo')
print(f'Tem a palavra "Luninhas.py" em {frase}? : {"Luninhas.py" in frase}')
print(f'Qual é a posição da palavra "Vídeo"?: {frase.find("vídeo")}')
print(f'A frase2 tem {len(frase2)} caracteres')

print('\nTransformação de textos')
# remove espaços antes e depois da frase2
print(f'A frase2 tem {len(frase2.strip())} letras')
print(f'Trocando "Python por "Luninhas.py: {frase.replace("Python", "Luninhas.py")}"')

print('\nDivisão de textos')
print(f'Separando o texto em listas: {frase.split()}')
dividido = frase.split()
print(dividido[0])
print(f'Dentro da lista 2 "{dividido[2]}" mostre o caracter 3 "{dividido[2][3]}"')

print('\nEscrevendo frases')
print('''Duas formigas se encontraram e pararam para conversar:
- Oi, qual é o seu nome?
- Fu.
- Fu o quê?
- Fu Miga!''')


