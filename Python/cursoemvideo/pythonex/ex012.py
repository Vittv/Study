#Faça um programa que leia um valor e mostre seu desconto de 5%:
n = float(input('Qual é o preço do produto: R$'))
print('Preço com 5% de desconto: R${:.2f}'.format((n-5/100*n)))