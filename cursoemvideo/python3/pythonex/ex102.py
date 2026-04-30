# Crie uma função que calcule o fatorial de um número
# Mostrando ou não o cálculo de seu resultado:

def fatorial(n, show=False):
    
    '''-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.'''

    f = 1

    for c in range(n, 0, -1):
        f *= c

        if show:
            while n > 1:

                print(f'{n} x ', end='')
                n -= 1
            print(f'1 = ', end='')
            return f'{f}'
    
        elif not show:
            return f


print(fatorial(5, show=True))
help(fatorial)

# CÓDIGO DO PROFESSOR:

def fatorial(n, show=False):
    
    '''-> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.'''

    f = 1

    for c in range(n, 0, -1):
        
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= c
    return f

 
print(fatorial(5, show=True))
help(fatorial)



