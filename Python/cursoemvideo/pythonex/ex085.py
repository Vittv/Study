# Faça um programa que coloque valores em uma lista
# depois mostrando uma lista par e uma impar dos mesmos:

lista = []
pares = []
impares = []
lista.append(pares)
lista.append(impares)

for i in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)

print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')