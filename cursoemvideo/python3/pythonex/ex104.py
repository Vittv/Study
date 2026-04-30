# Faça um programa que leia apenas números inteiros
# e insista que você responda de novo, até receber um
# número inteiro:

def leiaint(prompt):
    print('-' * 30)

    while True:
        
        try:
            num = int(input(prompt))
            return num
        
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# CÓDIGO DO PROFESSOR:

def leiaint(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        
        if n.isnumeric():
            valor = int(n)
            ok = True
        
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[0;31m')
        
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')