# Faça um programa que leia o nome e a quantidade de gols
# feitos por um jogador e mostre-os na tela:
# Caso não haja nome, substitue-o por <desconhecido>
# Caso não haja gols, substitue-os por 0:

def ficha(nome='<desconhecido>', gols=0):

    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


nome = str(input('Nome do Jogador: ')).strip().capitalize() or '<desconhecido>'
gols = int(input('Número de Gols: ') or 0)

print(ficha(nome, gols))


# CÓDIGO DO PROFESSOR:

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
