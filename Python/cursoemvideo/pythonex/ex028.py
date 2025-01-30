#Crie um programa que faça o computador pensar em um número de 0 a 5, e o usuário adivinhar qual número ele pensou:
'''import random
n = int(input('Em que número estou pensando (0 a 5)? '))
nl = [0, 1, 2, 3, 4, 5]
nr = random.choice(nl)
print('Eu pensei no número {}.'.format(nr))
if n==nr:
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente novamente.')'''

#CÓDIGO DO PROFESSOR:

from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))