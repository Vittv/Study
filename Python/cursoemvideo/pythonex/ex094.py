# Crie um programa que leie nome, sexo e idade de várias pessoas
# Guardando os dados de cada um em um dicionário e todos os 
# dicionários em uma lista. No final mostre:

# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média

nome = {}
sexo = {}
idade = {}
lista = []
mulheres = []
maiores = []
c = 0
z = 0

while True:
    nome['nome'] = str(input('Nome: ')).strip().capitalize()
    sexo['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade['idade'] = int(input('Idade: '))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    lista.append(nome.copy())
    lista.append(sexo.copy())
    lista.append(idade.copy())

    c += 1 

    if escolha in 'N':
        break

for i in range(0, len(lista), 3):
    z += lista[i + 2]['idade']
    
media = z / c

for i in range(0, len(lista), 3):    
    
    if lista[i + 1]['sexo'] in 'F':
        mulheres.append(lista[i]['nome'])

    if lista[i + 2]['idade'] > media:
        maiores.append(lista[i]['nome'])
        maiores.append(lista[i + 1]['sexo'])
        maiores.append(lista[i + 2]['idade'])

print(f'Foram cadastradas {c} pessoas.')
print(f'A média de idade é de {int(media)} anos.')
print(f'Lista de mulheres: {mulheres}')
print(f'Lista de todas as pessoas mais velhas que a média:')

for i in range(0, len(maiores), 3):
    
    print(f'Nome = {maiores[i]}; Sexo = {maiores[i + 1]}; Idade = {maiores[i + 2]};')