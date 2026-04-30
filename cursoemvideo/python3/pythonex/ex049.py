#Faça um programa que leia um valor e mostre sua tabuada:
n = int(input('Type a number to see its multiplication table: '))
for x in range(1, 11):
    print('{} x {:2} = {}'.format(n, x, n*x))
