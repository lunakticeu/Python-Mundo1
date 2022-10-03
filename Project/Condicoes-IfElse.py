nome = str(input('Digite o seu nome: '))
if nome == 'Luna':
        print('Que nome lindo você tem!')
print(f'Bom dia, {nome}')
###########################################
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if (media>=6.0):
        print('Sua média foi boa!')
else:
    print('Sua média foi ruim! Estude mais!!')
#ou
print('Aprovado' if media >=6.0 else 'Reprovado')