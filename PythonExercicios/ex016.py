#Crie um programa que leia um número real e mostre a sua parte inteira:
from math import floor
num = float(input('Digite um número:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, (floor(num))))