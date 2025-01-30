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