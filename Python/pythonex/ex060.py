#Faça um programa que calcule o fatorial de um número:
n = int(input('Enter a value: '))
c = n
f = 1
print('Calculating {}!: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))