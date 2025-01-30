#Faça um programa que leia um nome completo e mostre apenas o primeiro e último nome:
n = str(input('Insira seu nome: ')).strip().title()
n1 = n.split()
pr = n1[0]
ul = n1[-1]
print('Primeiro nome: {}'.format(pr))
print('Último nome: {}'.format(ul))

