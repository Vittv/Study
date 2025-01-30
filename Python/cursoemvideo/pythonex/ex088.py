# Faça um programa que crie palpites de
# MEGA SENA, baseado no número de jogos que
# o usuário escolher: 

from random import randint
from time import sleep

jogos = int(input('Quantos jogos? '))
for p in range(jogos):
    lista = []
    
    while len(lista) < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)      
    print(f'Jogo {p + 1}: {sorted(lista)}')
    sleep(1)  