#Faça um programa que mostre com quantos reais conseguirá comprar quantos dólares:
n = float(input('Você possui: R$'))
n1 = n/3.27
print('Com R${} você pode comprar ${:.2f}'.format(n, n1))