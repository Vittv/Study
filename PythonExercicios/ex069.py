# Faça um programa que pergunte idade, sexo e se quer continuar.
# No final mostre quantos maiores de 18, quantos homens e quantas mulheres menores de 20:
print('Preencha seu cadastro')
adultos = homens = mulheres20 = 0

while True:

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    print(' ')

    if idade >= 18:
        adultos += 1

    if sexo == 'M':
        homens += 1

    if idade < 20 and sexo == 'F':
        mulheres20 += 1

    if escolha == 'N':
        print(f'''Ao todo temos {adultos} adulto(s),\n{homens} homem(ns) cadastrado(s) e
{mulheres20} mulher(es) menor(es) de 20 anos''')

        break

#CÓDIGO DO PROFESSOR:
'''
tot18 = toth = totm20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade > 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totdh} homens cadastrados')
print(f'Temos {totm20} mulheres com menos de 20 anos')'''