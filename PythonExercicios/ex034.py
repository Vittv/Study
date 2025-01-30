#Faça um programa que mostre quaanto será o seu aumento de salário, dependendo do quanto você já ganha:
'''n = float(input('Digite seu salário: R$'))
a1 = n+(n*(10/100))
a2 = n+(n*(15/100))
if n>=1250.00:
    print('Você receberá um aumento de 10%, totalizndo R${:.2f}'.format(a1))
else:
    print('Você receberá um aumento de 15%, totalizando R${:.2f}'.format(a2))'''

#CÓDIGO DO PROFESSOR:

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <=1250.00:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('Quem ganhava R${:.2f} passar a ganhar R${:.2f} agora'.format(salário, novo))