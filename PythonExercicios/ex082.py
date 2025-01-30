lista = []
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
print(f'Lista ÍMPAR: {listaimpar}')

