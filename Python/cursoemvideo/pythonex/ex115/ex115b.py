from Python.cursoemvideo.pythonex.ex115.lib.sistema import nomes, idades, getnomes, getidades

nome = getnomes('Nome: ')
idade = getidades('Idade: ')
for i in nomes, idades:
    print(f'{nomes[i]} \t{idades[i]}')