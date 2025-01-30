# Faça um programa que tenha um função chamado maior,
# recebendo vários parâmetros e mostrando informações
# sobre os mesmos:

from time import sleep

def maior(*valores):

    if not valores:
        valores = (0,)

    print('-=' * 30)

    total = len(valores)
    print('Analisando os valores passados...')
    
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        
    print(f'Foram informados {total} valores ao todo.')

    if valores:
        max_value = max(valores)
        print(f'O maior valor informado foi {max_value}.')
    else:
        print(f'O maior valor informado foi {max_value}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


# CÓDIGO DO PROFESSOR:

from time import sleep

def maior(* núm):

    print('-=' * 30)
    cont = maior = 0
    print('\nAnalisando os valores passados... ')
    
    for valor in núm:
        
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

# Programa Principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# Por usar um len(valores) em vez de um contador,
# meu programa funciona por parte. Mas quando não
# é dado valor algum, ele considera isso como 1 valor
# o que é errado, logo o uso de contador é uma opção
# melhor aqui, e também deixou o código mais simples.

# Acabei fazendo uma gambiarra com uma tupla (0,) para
# que a variável max_value funcionasse.
# Mesmo que eu tenha errado, acredito que cheguei perto
# da resolução do professor e deixarei aqui meus erros
# para comparar. É sempre bom documentar diferentes formas
# de se programar a mesma coisa.