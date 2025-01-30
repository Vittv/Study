def area():
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    area = largura * comprimento
    print(f'A área de um terreno de {largura} x {comprimento} é de {area:.1f}m²')

print('Controle de Terrenos:')
print('-' * len('Controle de Terrenos:'))
area()
