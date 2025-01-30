# Faça um programa que tenha um função chamado maior,
# recebendo vários parâmetros e mostrando informações
# sobre os mesmos:

from time import sleep
import sys

def maior(*valores):

    if not valores:
        valores = (0,)

    print('-=' * 30)

    total = len(valores)
    print('Analisando os valores passados...')
    
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sys.stdout.flush()
        sleep(0.5)
    
    print(f'Foram informados {total} valores ao todo.')

    if valores:
        max_value = max(valores)
        print(f'O maior valor informado foi {max_value}.')
    else:
        print('O maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()