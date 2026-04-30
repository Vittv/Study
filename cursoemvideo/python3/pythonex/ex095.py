# Refaça o desafio 93, aprimorando-o e adicionando a opção de ver
# múltiplos jogadores, mostrando detalhes sobre os mesmos:

jogadores = []

while True:

    nome = str(input('Nome: ')).strip().capitalize()
    partidas = int(input('Partidas: '))

    gols = []
    
    for i in range(partidas):
        gol = int(input(f'Quantos gols na {i + 1}a partida? '))
        gols.append(gol)

    
    jogador = {'nome': nome, 'gols': gols, 'total': sum(gols)}
    jogadores.append(jogador)

    escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-'*30)

    if escolha in 'N':
        break

print('-'*40)
print(jogadores)

numjo = 0

print(f'{"cod":<5}{"nome":<16}{"gols":<20}{"total":>0}')

for jogador in jogadores:
    print(f'{numjo:<4} {jogador["nome"]:<15} {str(jogador["gols"]):<19} {jogador["total"]:>0}')
    numjo += 1

dados = int(input('Mostrar dados de qual jogador?' ))

if 0 <= dados < len(jogadores):
    
    for i in range(len(jogadores[dados]['gols'])):
        print(f'No jogo {i + 1} fez {jogadores[dados]["gols"][i]} gol(s)')
else:
    print("Jogador não encontrado!")


# CÓDIGO DO PROFESSOR:

time = list()
jogador = dict()
partidas = list()

while True:

    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar [S/N] ? ')).upper()[0]
        
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    if resp == 'N':
        break

print('-='*30)
print('cod', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    
    if busca == 999:
        break
    
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {time[busca["nome"]]}:')
        
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')

    print('-' * 40)
print('<< VOLTE SEMPRE >>')