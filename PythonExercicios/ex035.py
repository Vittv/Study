#Faça um programa que calcule se 3 retas podem ou não fazer um triângulo:
'''n1 = float(input('Reta 1: '))
n2 = float(input('Reta 2: '))
n3 = float(input('Reta 3: '))
n4 = (n1+n2)>=n3
if n4:
    print('Com essas 3 retas é possível fazer um triângulo')
else:
    print('Com essas 3 retas não é possível fazer um triângulo')'''

#CÓDIGO DO PROFESSOR:

print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')