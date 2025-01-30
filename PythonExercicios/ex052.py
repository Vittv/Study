#Faça um programa que descubra se um número é primo:
'''n = int(input('Digite um número: '))
if n == 1:
    print('{} não é um número primo'.format(n))
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, 'não é um número primo')
            break
    else:
        print(n, 'é um número primo')'''

#CÓDIGO DO PROFESSOR:

'''num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[32m', end=' ')
        print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')'''




s = 0
n = int(input('Enter a value: '))
for i in range(1, n + 1):
    if n % i == 0:
        s += 1
print('{} was divisible {}x, therefore'.format(n, s))
if s == 2:
    print('{} IS a prime number'.format(n))
else:
    print('{} IS NOT a prime number'.format(n))