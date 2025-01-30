# Faça um programa que monte uma tupla de 5 números aleatórios e mostre o maior e menor da lista:
from random import randint
lista = tuple(randint(1, 10) for i in range(5))
print(f'Lista de números aleatórios: {lista}')
print(f'Maior: {max(lista)} Menor: {min(lista)}')
