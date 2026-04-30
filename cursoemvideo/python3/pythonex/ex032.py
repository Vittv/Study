#Faça um programa que mostre se o ano é bissexto ou não:
'''n = int(input('Digite aqui o ano: '))
if (n%4)==0:
    print('Este ano ({}) é bissexto.'.format(n))
else:
    print('Este ano ({}) não é bissexto.'.format(n))'''

#CÓDIGO DO PROFESSOR:

from datetime import date
ano = int(input('Que ano que analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))