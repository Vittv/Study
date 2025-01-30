#Faça um programa que dentre 5 pesos de pessoas, mostre o maior e o menor peso:
n = 0
s = 0
for i in range(1, 6):
    w = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        n = w
        s = w
    else:
        if w > n:
            n = w
        if w < s:
            s = w
print('O maior peso foi {}kg'.format(n))
print('O menor peso foi {}kg'.format(s))
