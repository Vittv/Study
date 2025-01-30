#Crie um programa que leia o nome de uma pessoa e mostre diversas características:
nome = str(input('Digite seu nome completo: ')).strip()
pnom = nome.split()
pnom1 = pnom[0]
space = nome.count(' ')
fnom = len(nome)
print('Em letras maíusculas: {}'.format(nome.upper()))
print('Em letras minúsculas: {}'.format(nome.lower()))
print('O nome completo, sem espaços, possui {} letras.'.format(fnom-space))
print('O primeiro nome possui {} letras'.format(len(pnom1)))
