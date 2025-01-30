#Faça um programa que jogue jokenpo com você:
'''from random import choice
o = ['Pedra', 'Papel', 'Tesoura']
n = str(input('Escolha um: Pedra, Papel, Tesoura: '))
r = choice(o)
if n == 'Pedra' and r == n or n == 'Papel' and r == n or n == 'Tesoura' and r == n:
    print('Você escolheu {} e eu escolhi {}! Empatamos!'.format(n, r))
elif n == 'Pedra' and r == 'Tesoura':
    print('Você escolheu {} e eu escolhi {}, Pedra quebra Tesoura, você venceu!'.format(n, r))
elif n == 'Pedra' and r == 'Papel':
    print('Você escolheu {} e eu escolhi {}, Papel cobre Pedra, você perdeu!'.format(n, r))
elif n == 'Papel' and r == 'Pedra':
    print('Você escolheu {} e eu escolhi {}, Papel cobre Pedra, você ganhou!'.format(n, r))
elif n == 'Papel' and r == 'Tesoura':
    print('Você escolheu {} e eu escolhi {}, Tesoura corta Papel, você perdeu!'.format(n, r))
elif n == 'Tesoura' and r == 'Papel':
    print('Você escolheu {} e eu escolhi {}, Tesoura corta Papel, você ganhou!'.format(n, r))
elif n == 'Tesoura' and r == 'Pedra':
    print('Você escolheu {} e eu escolhi {}, Pedra quebra Tesoura, você perdeu!'.format(n, r))'''

#CÓDIGO DO PROFESSOR:

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')