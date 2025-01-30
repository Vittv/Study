# Aprimore o exercício 109 criando uma função no módulo
# moeda.py que crie uma tabela com todas as outras funções
# e seus valores que possa ser usada com um só comando 
# no exercício 110:

from moeda import aumentar, diminuir, dobro, metade, moeda, resumo

p = float(input('Digite o preço: R$'))
resumo(p, 80, 35)