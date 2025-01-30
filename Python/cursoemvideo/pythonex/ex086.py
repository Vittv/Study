# Faça um programa que leia valores e monte uma matriz:

top = []
mid = []
bot = []

for i in range(3):
    top.append(int(input('Digite um número: ')))
for i in range(3):
    mid.append(int(input('Digite um número: ')))
for i in range(3):
    bot.append(int(input('Digite um número: ')))

print(f'[ {top[0]} ][ {top[1]} ][ {top[2]} ]')
print(f'[ {mid[0]} ][ {mid[1]} ][ {mid[2]} ]')
print(f'[ {bot[0]} ][ {bot[1]} ][ {bot[2]} ]')