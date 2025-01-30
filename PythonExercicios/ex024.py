#Faça um programa que leia o nome de uma cidade e diga se ela possui Santo ou não no início do nome:
c = str(input('Insira o nome da cidade '))
cs = c.split()
cd = cs[0].title()
cf ='Santo'in cd
print('Sua cidade começa com Santo: {}'.format(cf))