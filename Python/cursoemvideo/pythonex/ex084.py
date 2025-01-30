# Faça um programa que leia dados e mostre
# o nome da pessoa mais pesada e o da mais leve:

pessoas = []
c = 0

while True:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    pessoas.append([nome, peso])
    c += 1
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

pesado = pessoas[0][1]
leve = pessoas[0][1]

for p in pessoas:
    if p[1] > pesado:
        pesado = p[1]
    if p[1] < leve:
        leve = p[1]

pessoaspesadas = [p[0] for p in pessoas if p[1] == pesado]
pessoasleves = [p[0] for p in pessoas if p[1] == leve]

print(f'Ao todo {c} pessoas cadastradas.')
print('Pessoas mais pesadas:', end=' ')

for pessoa in pessoaspesadas:
    print(pessoa, end=', ')
print('\b\b')
print('Pessoas mais leves:', end=' ')

for pessoa in pessoasleves:
    print(pessoa, end=', ')
print('\b\b')