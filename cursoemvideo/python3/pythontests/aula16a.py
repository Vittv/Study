# Pode usar () ou não, vai dar no mesmo para as tuplas
# Mas geralmente tuplas são determinadas por (), listas por [] e dicionários por {}.
# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0])  # Hambúrguer
print(lanche[1])  # Suco
print(lanche[-2])  # Pizza
print(lanche[1:3])  # Começa no 1 e vai até o 3 - 1, logo: Suco, Pizza
print(lanche[2:])  # Pizza, Pudim
print(lanche[:2])  # Hambúrguer, Pizza
print(lanche[-2:])  # Pizza, Pudim
for comida in lanche:                                     # CASO N PRECISE DE POSIÇÃO
    print(f'Eu vou comer {comida}')

# Aqui você está indo de 0 (sempre o primeiro termo,
# a len(lanche), ou seja, como temos quatro itens, 4
# isso vai fazer com que ele vá até 3, pois o final é sempre
# subtraído por um, então por fim ficará:
# for cont in range(0, 4):

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')    # CASO PRECISE DE POSIÇÃO

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')     # CASO PRECISE DE POSIÇÃO
print('Comi pra caramba!')
print(sorted(lanche))  # Põe em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(f'O número 5 apareceu {c.count(5)} vezes nas duas tuplas')  # Conta quantas vezes o número em () aparece
print(c.index(8))  # Mostra em qual posição o número em () está
print(c.index(5, 1))

pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa)
print(f'{pessoa}')
