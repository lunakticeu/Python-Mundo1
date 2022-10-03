#Faça um algoritmo que leia o salário de um funcionário e
# mostre o seu novo salário, com 15% de aumento

salario = float(input('Digite o salário: R$ '))
aumento = salario+(salario * 0.15)

print('O salário de R${} com 15% de aumento é R${}'.format(salario, aumento))