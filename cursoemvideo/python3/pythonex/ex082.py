#  Faça um programa que leia numeros do usuario e coloque-os em uma lista
# Entao faça uma lista com os numeros pares e impares dessa mesma lista:

'''lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

    if escolha == 'N':
        break

print(f'Lista: {lista}')
print(f'Lista PAR: {listapar}')
print(f'Lista ÍMPAR: {listaimpar}')'''

# CÓDIGO DO PROFESSOR:

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')