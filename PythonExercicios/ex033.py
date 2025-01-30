#Faça um programa que mostre o maior e menor número, entre 3 números:
'''n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
n4 = [n1, n2, n3]
print('O número {} é o maior dos três.'.format(max(n4)))
print('O número {} é o menor dos três'.format(min(n4)))'''

#CÓDIGO DO PROFESSOR:

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))