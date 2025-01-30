#Faça um programa que leia um número e mostre suas unidades, dezenas, centenas e milhares:
n = int(input('Digite um número: '))
u = n // 1%10
d = n // 10%10
c = n // 100%10
m = n // 1000%10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))