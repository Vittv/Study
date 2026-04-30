# Crie um módulo com várias funções e faça um programa que
# importe e use as mesmas com sucesso:

from moeda import aumentar, diminuir, dobro, metade, moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13)}')
