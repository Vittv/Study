#Faça um programa que multe caso o usuário tenha ultrapassado o limite de velocidade (7 reais por km ultrapassado):
v = float(input('Velocidade do carro: '))
m = (v-80)*7
if v>=80:
    print('Você não respeitou o limite de velocidade,\nportanto, deve pagar a multa de R${:.2f}.'.format(m))
else:
    print('Obrigado por respeitar o limite de velocidade.')