def leiaDinheiro():
    dinheiro = input('Digite o preço: R$')
    if dinheiro.isnumeric():
        return float(dinheiro)
    else:
        print('Valor inválido. Digite novamente.')