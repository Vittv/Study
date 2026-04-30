#Faça um programa que mostre se um nome possui Silva ou não:
n = str(input('Insira seu nome: ')).strip()
n1 = n.lower()
n2 = 'silva' in n1
print('Seu nome possui Silva: {}'.format(n2))