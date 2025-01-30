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

