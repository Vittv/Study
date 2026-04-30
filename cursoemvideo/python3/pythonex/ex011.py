#Faça um programa que meça a área de uma sala e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta cobre 2 metros quadrados:
c = float(input('Comprimento: '))
h = float(input('Altura: '))
a = c*h
b = a*4
s = b/2
print('A área dessa sala é de {} metros quadrados, dando {} metros quadrados por parede. '.format(b, a))
print('Para pintar cada parede precisará de {}l, totalizando {}l. '.format(a/2, s))