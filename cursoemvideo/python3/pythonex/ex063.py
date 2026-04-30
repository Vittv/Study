#Faça um programa que mostre quantos termos quiser da Sequência de Fibonacci:
n = int(input('Quantos termos? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print(' -> {}'.format(t3), end='')
