#Faça um programa que mostre sobre 4 pessoas:
#A média de idade:
#Quem é o homem mais velho:
#Quantas mulheres têm menos de 20 anos:
m = 0
mi = 0
id = 0
nm = ''
tm = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    m += idade
    if i == 1 and sexo in 'Mm':
        id = idade
        nm = nome
    if sexo in 'Mm' and idade > id:
        id = idade
        nm = nome
    if sexo in 'Ff' and idade < 20:
        tm += 1
mi = m/4
print('A média das idades é {}'.format(mi))
print('O homem mais velho se chama {} e tem {} anos'.format(nm, id))
print('{} mulheres têm menos de 20 anos'.format(tm))

