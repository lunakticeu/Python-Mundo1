print('Oi Luna'*5)

nome = input('Qual é o seu nome?')
# print('Prazer de te conhecer{}'.format(nome))

#mostra 20 caracteres na mensagem
print('Prazer de te conhecer {:20}!'.format(nome))

#alinhamento a direita em 20 espaços
print('Prazer de te conhecer {:>20}!'.format(nome))
#alinhamento a esquerda em 20 espaços
print('Prazer de te conhecer {:<20}!'.format(nome))
#centralizado em 20 espaços
print('Prazer de te conhecer {:^20}!'.format(nome))

#coloca o sinal de = nos espaços em branco
print('Prazer de te conhecer {:=^20}!'.format(nome))

