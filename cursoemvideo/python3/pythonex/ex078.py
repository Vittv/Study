# Faça um programa que leia 5 valores, colocando-os em uma lista
# e mostrando qual o maior e menor e suas respectivas posições:

list = []
max = 0
min = 0
for c in range(0, 5):
    list.append(int(input('Enter a value: ')))
    if c == 0:
        max = min = list[c]
    else:
        if list[c] > max:
            max = list[c]
        if list[c] < min:
            min = list[c]

print(f'You entered {list}')
print(f'Max was {max}, found at: ', end='')
for i, v in enumerate(list):
    if v == max:
        print(f'{i+1}..', end='')
print()

print(f' Min was {min}, found at: ', end='')
for i, v in enumerate(list):
    if v == min:
        print(f'{i+1}..', end='')
print()