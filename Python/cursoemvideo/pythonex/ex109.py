# Aprimore o exercício 108, adicionando um parâmetro
# a mais na funções do 107, informando se o valor
# retornado por elas será ou não formatado pela
# função moeda() desenvolvida no ex 108:

from moeda import aumentar, diminuir, dobro, metade, moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, sit=True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, sit=True)}')
print(f'Aumentando 10%, temos {aumentar(p, 10, sit=True)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13, sit=True)}')
