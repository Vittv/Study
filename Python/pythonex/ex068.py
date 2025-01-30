# Faça um programa que jogue par ou ímpar contigo, apenas parando quando você perder, mostrando=lhe suas vitórias:
from random import randint

vit = 0

while True:

    p1 = int(input('Escolha um número (1 - 10): '))
    pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    comp = randint(1, 10)
    s = p1 + comp
    print(f'''Você escolheu {p1} e eu escolhi {comp}
{p1} + {comp} = {s}''')

    if s % 2 == 0 and pi == 'P':
        print(f'''{s} é Par, você GANHOU!
         ''')
        vit += 1
    elif s % 2 != 0 and pi == 'I':
        print(f'''{s} é Ímpar, você GANHOU!
         ''')
        vit += 1
    elif s % 2 == 0 and pi == 'I':
        print(f'''{s} é Par, você PERDEU depois de {vit} vitória(s) seguida(s)!
         ''')
        break
    elif s % 2 != 0 and pi == 'P':
        print(f'''{s} é Ímpar, você PERDEU depois de {vit} vitória(s) seguida(s)!
         ''')
        break
