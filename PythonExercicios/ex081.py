# Faça um programa que leia números e coloque-os em uma lista
# Mostre quantos valores a lista possui
# Mostre a lista em ordem decrescente
# E por fim mostre se o número 5 está ou não na lista:

lista = []
c = 0

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c += 1
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'Você digitou {c} valores.')
print(f'Em ordem decrescente: {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
