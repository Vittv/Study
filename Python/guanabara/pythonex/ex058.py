#Refaça o desafio 28, desta vez, contando e mostrando o número de tentativas antes de adivinhar o que o computador escolheu:
from random import randint
comp = randint(0,10) #Makes the computer think
print('I will think of a number between 0 and 10, try to guess')
p1 = 1
player = 1
while player != comp:
    player = int(input('What number was I thinking? ')) #Player tries to guess
    if player != comp:
        p1 += 1
    if player == comp:
        print('CONGRATULATIONS! The number I had in mind was {}, you guessed it right after {} tries!'.format(comp, p1))

# CÓDIGO DO PROFESSOR:

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        if jogador > computador:
            print('Menos.. Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))



