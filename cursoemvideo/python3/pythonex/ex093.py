# Crie um programa que mostre o aproveitamento de jogadores de futebol
# Leia nome, quantas partidas jogou e quantos gols em cada partida.
# Por fim, tudo será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato:

jogador = {}
gol = []

jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {i + 1}? ')))

jogador['gols'] = gol
jogador['total'] = sum(gol)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')

for p, g in enumerate(gol):
    print(f'=> Na partida {p + 1}, fez {g} gol(s).')

# CÓDIGO DO PROFESSOR:

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')