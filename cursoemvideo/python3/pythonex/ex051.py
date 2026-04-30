#Faça um programa que leia um número e sua razão e mostre 10 números de sua PA:
num = int(input('Digite um número: '))
r = int(input('Digite sua razão: '))
for i in range(1, 10 + 1):
    a = num + r * (i-1)
    print(a, end=' ')

#CÓDIGO DO PROFESSOR:

'''num = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
d = num + (10 - 1) * r
for c in range(num, d, r):
    print(d, end=' ')'''


