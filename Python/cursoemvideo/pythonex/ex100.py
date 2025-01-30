from random import randint
from time import sleep
import sys

números = []

def sorteia():

    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        valores = randint(1, 10)
        números.append(valores)
    for núm in números:
        print(f'{núm} ', end='', flush=True)
        sys.stdout.flush()
        sleep(0.5)
    print('PRONTO!')


def somaPar():

    totalpar = 0

    for valor in números:

        if valor % 2 == 0:
            totalpar += valor
    print(f'Somando os valores pares de {números}, temos {totalpar}')


sorteia()
somaPar()