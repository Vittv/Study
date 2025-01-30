# Faça um programa que mostre contagens de:
# 1 a 10 de 1 em 1, 10 a 0 de 2 em 2 e por fim
# o usuário escolhe inicio, fim e passo na terceira vez:

from time import sleep

def contador(inicio, fim, passo):

    if passo is None:
        passo = 1
    
    print('-' * 30)

    if inicio < fim and passo > 0:

        print(f'Contagem de {inicio} até {fim - 1} de {passo} em {passo}')
        for i in range(inicio, fim, passo):
            print(f'{i} ', end= '', flush=True)
            sleep(0.5)
        print('FIM!', end='')

    if inicio > fim and passo < 0:
        
        print(f'Contagem de {inicio} até {fim + 1} de {passo + 4} em {passo + 4}')
        for i in range(inicio, fim, passo):
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
        print('FIM!', end ='')

    if inicio != inicio and fim != fim and passo != passo:

        if inicio < fim and passo > 0:
        
            print(f'Contagem de {inicio} até {fim + 2} de {passo} em {passo}')
            for i in range(inicio, fim + 1, passo):
                print(f'{i} ', end='', flush=True)
                sleep(0.5)
            print('FIM!', end ='')

        if inicio > fim and passo < 0:

            print(f'Contagem de {inicio} até {fim + 2} de {passo} em {passo}')
            for i in range(inicio, fim - 1, passo):
                print(f'{i} ', end='', flush=True)
                sleep(0.5)
            print('FIM!', end ='')


    print()
 

inicio = 1
fim = 11
passo = 1

contador(inicio, fim, passo)

inicio = 10
fim = -1
passo = -2

contador(inicio, fim, passo)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)

