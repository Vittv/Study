#Faça um programa que leia a idade de uma pessoa e determine qual a sua categoria com base na mesma:
from datetime import date
year = date.today().year
n = int(input('Digite aqui seu ano de nascimento: '))
print('O atleta tem {} anos'.format(year - n))
if year - n <= 9:
    print('Classificação: MIRIM')
elif year - n <=14:
    print('Classificação: é INFANTIL')
elif year - n <=19:
    print('Classificação: é JUNIOR')
elif year - n <=25:
    print('Classificação: é SÊNIOR')
elif year - n > 25:
    print('Classificação: é MASTER')
