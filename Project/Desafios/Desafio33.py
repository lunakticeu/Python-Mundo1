#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verifica quem é o menor
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f'O menor número é {menor}')

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior}')