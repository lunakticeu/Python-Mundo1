#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
from datetime import date
ano = int(input('Em qual ano estamos? Coloque 0 para analisar o ano atual '))

if (ano == 0):
    ano = datetime.date.today().year

# Ano bissexto é divisivel por 4 e não pode terminar em 00
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'Ano {ano} não é bissexto')

