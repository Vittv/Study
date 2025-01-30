def escreva(texto):
    print('~' * len(texto))
    print(texto)
    print('~' * len(texto))


escreva(' Gustavo Guanabara ')
escreva(' Curso de Python no Youtube ')
escreva(' CeV ')


# CÓDIGO DO PROFESSOR:

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')