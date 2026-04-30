#Refaça o desafio 61 usando o comando while em vez de for, melhorando-o:
n = int(input('Digite um número: '))
r = int(input('Digite sua razão: '))
c = 1
t = 0
z = 10
while z != 0:
    t = t + z
    while c <= t:
        print('{} ->'.format(n), end=' ')
        n += r
        c += 1
    print('PAUSE')
    z = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(t))