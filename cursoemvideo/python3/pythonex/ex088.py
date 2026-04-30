# Faça um programa que crie palpites de
# MEGA SENA, baseado no número de jogos que
# o usuário escolher: 

from random import randint
from time import sleep

tickets = int(input('Quantos jogos? '))
for p in range(tickets):
    list = []
    
    while len(list) < 6:
        n = randint(1, 60)
        if n not in list:
            list.append(n)      
    print(f'Jogo {p + 1}: {sorted(list)}')
    sleep(1)

# CÓDIGO DO PROFESSOR:

from random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos quer que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)