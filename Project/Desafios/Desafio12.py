#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: R$'))

desconto = preco -(preco * 0.05)

print('O valor de R${} após desconto de 5% é R${}'.format(preco, desconto))