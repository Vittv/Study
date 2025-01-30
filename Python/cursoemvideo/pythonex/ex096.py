def area():

    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    area = largura * comprimento
    print(f'A área de um terreno de {largura}m x {comprimento}m é de {area:.1f}m².')

print('Controle de Terrenos')
print('-' * len('Controle de Terrenos:'))
area()

# CÓDIGO DO PROFESSOR:

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa Principal
print(' Controle de Terrenos ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)