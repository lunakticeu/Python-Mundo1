import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#ceil arredonda o valor pra cima/floor arredonda para baixo
print('A raiz de {} é {} arredondada para cima'.format(num, math.ceil(raiz)))
print('A raiz de {} é {} arredondada para baixo'.format(num, math.floor(raiz)))
print('A raiz de {} é {:.2f} exatamente'.format(num, raiz))

#############################################################################################
import random
num2 = random.random()
print(num2)
