#Faça um programa que determine se sua viagem e´longa ou curta e seu preço de acordo com a distância:
'''n = float(input('Digite a distância de sua viagem: '))
if n<=200:
    print('Sua viagem é curta e sua passagem custará R${:.2f}.'.format(n*0.50))
else:
    print('Sua viagem é longa e sua passagem custará R${:.2f}.'.format(n*0.45))'''

#CÓDIGO DO PROFESSOR:

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))