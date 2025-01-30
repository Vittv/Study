#Faça um programa que leia a idade de um jovem e determine  se já se alistou ou quando deverá se alistar:
'''from datetime import date
n = int(input('Digite seu ano de nascimento: '))
year = date.today().year
a = n+18
ia = year - n
print('Quem nasceu em {} tem {} anos em {}'.format(n, ia, year))
if year - n < 18:
    print('Aos {} anos, você precisará se alistar em {} anos'.format(ia, (abs(year - a))))
elif year - n == 18:
    print('Aos {} anos, você se alistará no ano atual de {}'.format(ia, year))
elif year - n > 18:
    print('Aos {} anos, você já se alistou há {} anos'.format(ia, year - a))'''

#Código do professor:

from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite seu sexo: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 'Feminino':
    print('Você é do sexo feminino, portanto não precisa se alistar')
elif sexo == 'Masculino' and idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif sexo == 'Masculino' and idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif sexo == 'Masculino' and idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
