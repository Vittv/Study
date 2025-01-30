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
    
def leiaDinheiro():
    dinheiro = input('Digite o preço: R$')
    if dinheiro.replace(',','.').isdigit():
        return float(dinheiro)
    else:
        print('Valor inválido. Digite novamente.')


# CÓDIGO DO PROFESSOR:

def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato == False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato == False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: {aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: {diminuir(preço, taxar, True)}')
    print('-' * 30)


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)


