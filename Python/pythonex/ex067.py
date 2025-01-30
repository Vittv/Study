# Faça um programa que leia um valor e mostre sua tabuada, perguntando
# novamente por valores, até que um valor negativo seja dado:
while True:

    r = 0
    m = 0
    n = int(input('Type a value to see its multiplication table: '))

    if n < 0:
        print('Finished')
        break

    while m <= 9:

        if n >= 0:
            m += 1
        r = n * m
        print(f'{n} x {m} = {r}')





