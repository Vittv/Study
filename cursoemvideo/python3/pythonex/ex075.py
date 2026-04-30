# Faça um programa que leia 4 números e mostre diversas informações:
num = (int(input('Digite o primero número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o quarto número: ')))

p = 0

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es)')

if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3, 0) + 1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')

for i in num:
    if i % 2 == 0:
        p += 1
        if p == 1:
            print(f'Os valores pares desta tupla foram no total {p}, sendo eles: {i}', end='')
        else:
            print(f', {i}', end='')

if p == 0:
    print('Não foram digitados valores pares nesta tupla.')
else:
    print('')
