#Faça um programa que mostre a soma de 6 números inteiros pares, caso ímpares, desconsidere-os:
n = 0
s = 0
for i in range(6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        n += num
        s += 1
print('Você informou {} números pares e a soma foi {}'.format(s, n))