# Faça um programa que leia 5 valores, colocando-os em uma lista
# e mostrando qual o maior e menor e suas respectivas posições:

lista = list()

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

maxvalor = max(lista)
minvalor = min(lista)

maxpos = [i + 1 for i, v in enumerate(lista) if v == maxvalor]
minpos = [i + 1 for i, v in enumerate(lista) if v == minvalor]

print(f'Você digitou {lista}')
print(f'O maior valor foi {maxvalor} encontrado nas posições {maxpos}')
print(f'O menor valor foi {minvalor} encontrado nas posições {minpos}')
