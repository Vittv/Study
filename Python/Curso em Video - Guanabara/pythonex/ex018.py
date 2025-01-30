#Faça um programa que leia um ângulo qualquer e mostre seu seno, cosseno e tangente:
from math import radians, sin, cos, tan
ang = float(input('Valor do ângulo:'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno de {} é {:.2f}\nO cosseno é {:.2f}\ne a tangente é {:.2f}'.format(ang, sen, cos, tan))
