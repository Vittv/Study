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