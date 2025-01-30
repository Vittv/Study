# Faça um programa que leia valores até mandar parar
# Não recebendo valores repetidos e depois os mostre na tela:

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor repetido, tente novamente.')

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')
