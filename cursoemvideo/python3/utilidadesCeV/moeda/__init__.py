def aumentar(p, pc, sit=False):
    aumento = p + (p * (pc / 100))
    if sit:
        return moeda(aumento)
    return aumento

def diminuir(p, pc, sit=False):
    diminui = p - (p * (pc / 100))
    if sit:
        return moeda(diminui)
    return diminui    

def dobro(p, sit=False):
    dobro = p * 2
    if sit:
        return moeda(dobro)
    return dobro

def metade(p, sit=False):
    metade = p / 2
    if sit:
        return moeda(metade)
    return metade

def moeda(p):
    moeda = f'R${p:.2f}'
    return moeda

def resumo(p, mai, men):
    aumento = p + (p * (mai / 100))
    diminui = p - (p * (men/ 100))
    dobro = p * 2
    metade = p / 2
    print(f'''
------------------------------
        RESUMO DO VALOR
------------------------------
Preço analisado:    R${p:.2f}
Dobro do preço:     R${dobro:.2f}
Metade do preço:    R${metade:.2f}
{mai}% de aumento:     R${aumento:.2f}
{men}% de redução:     R${diminui:.2f}
------------------------------''')