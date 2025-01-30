#Faça um programa que leia inputs e mostre sua média e qual é o maior e qual é o menor:
r = 'y'
s = c = m = ma = mi = 0
while r in 'y':
    n = int(input('Enter a value: '))
    s += n
    c += 1
    if c == 1:
        ma = mi = n
    else:
        if n > ma:
            ma = n
        if n < mi:
            mi = n
    r = str(input('Would you like to continue? [Y/N] ')).lower().strip()[0]
m = s / c
print('You entered {} numbers and their average was {}'.format(c, m))
print('{} was max and {} was min'.format(ma, mi))
#CÓDIGO DO PROFESSOR:

'''resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))'''



