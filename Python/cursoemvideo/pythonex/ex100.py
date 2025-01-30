from random import randint
from time import sleep

números = []

def sorteia():

    print('Sorteando 5 valores da lista: ', end='')
    
    for i in range(5):

        valores = randint(1, 10)
        números.append(valores)
        print(f'{valores} ', end='', flush=True)
        sleep(0.3)
    
    print('PRONTO!')


def somaPar():

    totalpar = 0

    for valor in números:

        if valor % 2 == 0:
            totalpar += valor
    
    print(f'Somando os valores pares de {números}, temos {totalpar}')


sorteia()
somaPar()

# CÓDIGO DO PROFESSOR:

# Foi idêntico tirando que ele especificou:
# def sorteia(lista) e def somaPar(lista)
# E ele também colocou números = list()
# embaixo depois de todas as funções
# em vez de antes como eu fiz