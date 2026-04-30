# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os(com idade) em um dicionário. Se por acaso a CTPS for diferente
# de ZERO, o dicionário receberá também o ano da contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar:

from datetime import datetime

cidadao = {}

cidadao['Nome'] = str(input('Digite seu nome: ')).strip().capitalize()
cidadao['Ano de nascimento'] = int(input('Digite seu ano de nascimento: '))
cidadao['CTPS'] = int(input('Digite sua carteira de trabalho [0 para N/A]: '))

anoatual = datetime.now().year
idade = anoatual - cidadao['Ano de nascimento']


if cidadao['CTPS'] != 0:

    cidadao['Ano da contratação'] = int(input('Digite quando foi contratado: '))
    cidadao['Salário'] = float(input('Digite seu salário: R$'))


print(f'Nome: {cidadao["Nome"]}')
print(f'Idade: {idade}')
print(f'CTPS: {cidadao["CTPS"]}')

a = 35 - (anoatual - cidadao['Ano da contratação'])
aposentar = idade + a

if cidadao['CTPS'] != 0:

    print(f'Ano da contratação: {cidadao["Ano da contratação"]}')
    print(f'Salário: R${cidadao["Salário"]:.2f}')
    print(f'{cidadao["Nome"]} começando a trabalhar em {cidadao["Ano da contratação"]},')
    print(f'Se aposentará em {a} anos aos {aposentar} anos de idade.')

# CÓDIGO DO PROFESSOR:

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento? '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho [0 não tem].' ))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')