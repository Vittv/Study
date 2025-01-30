#Crie um programa que leia o comprimento do cateto oposto e adjacente de um triângulo retângulo e calcule a sua hipotenusa:
from math import sqrt
opo = float(input('Cateto oposto:'))
adj = float(input('Cateto adjacente:'))
hipo = sqrt((opo**2) + (adj**2))
print('A hipotenusa desse triângulo é {:.2f}cm'.format(hipo))