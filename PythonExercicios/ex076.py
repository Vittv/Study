# Faça uma lista de nomes e preços de produtos:
tupla = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
        'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('='*39,)
print(f'{'LISTAGEM DE PREÇOS':^39}')
print('='*39)

for i in range(0, len(tupla), 2):  # Ele irá de 0 (Lápis) a 17(34.90), pulando de 2 em 2
    produto = tupla[i]  # Aqui não modificamos a ordem para mostrar os nomes
    preço = tupla[i+1]  # E aqui adicionamos um, já que os preços sempre estão à frente dos nomes
    print(f'{produto:.<30}R${preço:7.2f}')
print('='*39)
