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

contador(1, 11, 1)
contador(10, -1, -2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)


# CÓDIGO DO PROFESSOR:

from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p *= 1

    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:

        cont = 1
        while cont <= f:

            print(f'{cont}', end='', flush=False)
            sleep(0.5)
            cont += p
        print('FIM!')

    else:
        cont = i
        while cont >= f:
            
            print(f'{cont} ', end='', flush=False)
            sleep(0.5)
            cont += p
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

# A resolução do Gustavo acabou sendo melhor por usar while.
# O uso do while fez com que os números sempre ficassem corretos.
# O for loop acaba fazendo só até 1 número antes do número escolhido como fim.
# Além de que usando while x <= y, você garante que o último número da lista
# será escrito.