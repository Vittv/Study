#Refaça o desafio 51 usando o comando while em vez de for:
n = int(input('Digite um número: '))
r = int(input('Digite sua razão: '))
c = 1
while c <= 10:
    n += r
    c += 1
    print('{} ->'.format(n), end =' ')
print('END')