#Faça um programa que mostre a soma de todos os números ímpares e múltiplos de 3 entre 1 e 500:
n = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n += c  #aka n = n + c
        s += 1
print('A soma de todos os {} valores solicitados é {}'.format(s, n))
