# Aprimore o ex086:

top = []
mid = []
bot = []
pares = []

for i in range(3):
    top.append(int(input('Digite um número: ')))
for n in top:
    if n % 2 == 0:
        pares.append(n)

for i in range(3):
    mid.append(int(input('Digite um número: ')))
for n in mid:
    if n % 2 == 0:
        pares.append(n)

for i in range(3):
    bot.append(int(input('Digite um número: ')))
for n in bot:
    if n % 2 == 0:
        pares.append(n)

print(f'[ {top[0]} ][ {top[1]} ][ {top[2]} ]')
print(f'[ {mid[0]} ][ {mid[1]} ][ {mid[2]} ]')
print(f'[ {bot[0]} ][ {bot[1]} ][ {bot[2]} ]')
print(f'A soma dos pares nesta matriz é {sum(pares)}')
print(f'A soma dos valores na terceira coluna é {top[2]+mid[2]+bot[2]}')
print(f'O maior valor na segunda linha é {max(mid)}')

# CÓDIGO DO PROFESSOR:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para [{l}, {c}]: '))
print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]

print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
        
print(f'O maior valor da segunda linha é {mai}')
