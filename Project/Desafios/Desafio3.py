numero = input('Digite um numero: ')
#mostra o tipo da variavel
print(type(numero))

#convertendo um string para inteiro
n1 = int(input('Digite um numero: '))
# print(type(n1))

n2 = int(input('Digite mais um numero: '))
soma = n1+n2
# print(type(soma))

# mesma coisa
# print('A soma entre ', n1, ' e ', n2, ' vale ', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))

