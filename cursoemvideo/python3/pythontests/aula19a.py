dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])   # Pedro
print(dados['idade'])  # 25

dados['sexo'] = 'M'  # dados = {'nome':'Pedro', 'idade':25, 'sexo':'M'}
del dados['idade']

filme = {'título':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }

print(filme.values())  # retornará Star Wards, 1977 e George Lucas
print(filme.keys())  # retornará título, ano e diretor
print(filme.items())  # retornará ambos

for k, v in filme.items():
    print(f'O {k} é {v}')  # O título é Star Wars
                           # O ano é 1977
                           # O diretor é George Lucas

# É possível colocar dicionários dentro de listas
# Nesse caso, cada dicionário se tornará 0, 1, 2 sucessivamente

locadora = []
locadora.append(filme)

print(locadora[0]['ano'])  # 1977


# Use {} para referenciar elementos e [] para declará-los

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade':22}
pessoas['nome'] = 'Leandro'  # MODIFICANDO ELEMENTOS
pessoas['peso'] = '98.5'  # ADICIONANDO ELEMENTOS
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k in pessoas.keys():  # Para values ou keys
    print(k)

for k, v in pessoas.items(): # Para items é necessário 2
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])  #  Rio de Janeiro
print(brasil[1]['sigla'])  # SP


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # No caso de dicionários, não se pode fazer
                                  # uma cópia usando estado[:], em vez disso
                                  # usa-se um comando exclusivo de dicionários:
                                  # estado.copy()
print(brasil)

for e in brasil:
    for k, v, in e.items():
        print(f'O campo {k} tem valor {v}.')