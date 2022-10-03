#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

#{:.2f} indica 2 casas do número float após o ponto
print('O dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(dobro, triplo, raiz))
