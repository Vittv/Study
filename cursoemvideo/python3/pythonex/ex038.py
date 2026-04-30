#Escreva um programa que leia dois valores e mostre qual é o maior entre eles ou se são iguais:
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro valor {} é maior'.format(n1))
elif n1 < n2:
    print('O segundo valor {} é maior'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
