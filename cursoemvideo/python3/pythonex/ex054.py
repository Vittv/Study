#Faça um programa que mostre dentre um grupo de 7 pessoas, quais são maiores e menores de idade:
from datetime import date
n = 0
s = 0
for i in range(7):
    a = int(input('Em que ano a {}ª pessoa nasceu? '.format(i+1)))
    id = (date.today().year) - a
    if id <= 21:
        n += 1
    else:
        s += 1
print('Dentre este grupo de 7, {} pessoas são maiores de idade'.format(s))
print('Dentre este grupo de 7, {} pessoas ainda não atingiram a maior idade'.format(n))
