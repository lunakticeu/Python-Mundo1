#screva um programa que converta uma temperatura digitando em
# graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (celsius * 9/5) + 32

print('{} graus Celsius equivale a {} graus Fahrenheit'.format(celsius, fahrenheit))