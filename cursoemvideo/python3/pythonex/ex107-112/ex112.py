# Aprimore o exercício 111, verificando se
# o valor dado (p) é monetário ou não:

from moeda import aumentar, diminuir, dobro, metade, moeda, resumo, leiaDinheiro

p = leiaDinheiro()
resumo(p, 80, 35)


# CÓDIGO DO PROFESSOR:

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)