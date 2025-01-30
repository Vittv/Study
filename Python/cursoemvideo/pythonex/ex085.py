# Faça um programa que coloque valores em uma lista
# depois mostrando uma lista par e uma impar dos mesmos:

lista = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input('Digite um valor: '))
    
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Lista de pares: {sorted(lista[0])}')
print(f'Lista de ímpares: {sorted(lista[1])}')