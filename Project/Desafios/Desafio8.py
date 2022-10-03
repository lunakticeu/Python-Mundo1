# Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm

num = float(input('Digite um valor em metros: '))

cm = num * 100
mm = num * 1000

print('{} metros em centimetros é {:.0f} e em milimetros é {:.0f}'.format(num, cm, mm))