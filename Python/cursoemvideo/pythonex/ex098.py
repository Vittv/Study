from time import sleep

def contador(inicio, fim, passo):
    
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
        
        print(f'Contagem de {inicio} até {fim + 2} de {passo} em {passo}')
        for i in range(inicio, fim + 1, passo):
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

