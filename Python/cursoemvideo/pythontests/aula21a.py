# Tópicos da aula:

# Interactive Help
# docstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de resultados

# help() Interactive Help - Usado para descobrir informações
# sobre comandos built-in do python.

# Para acessar isso no vs code é necessário:
# Apertar Ctrl Shift P e digitar Python: Start REPL
# abrindo então o Python Console

# Três formas de usar o comando help:

# 1) Abrindo o Python Console e digitando help

# 2) Digitando help() diretamente no código

help(print)

# 3) Digitando print(comando.__doc__) no código

print(input.__doc__)

# docstrings:

from time import sleep
def contador(i, f , p):

    '''Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função criada por Gustavo Guanabara do canal CursoemVideo.
    '''

    c = i

    while c <= f:

        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2, 10 , 2)
help(contador)

# Parâmetros Opcionais:

def somar(a=0, b=0, c=0):

    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)     # Neste caso não há valor para o parâmetro 'c'
                # Adicionando o '=0' você inclui um Parâmetro Opcional
                # Indicando que caso c não receba valor, o mesmo é 0

somar()  # No caso de receber NENHUM parâmetro. Adicionando
         # 0 como parâmetro opcional para todos os parâmetros
         # fará com que o programa funcione sem erros.

somar(b=4, c=2) # Dará 6 pois a não foi informado, portanto, a=0
somar(c=3, a=2) # Dará 5 pois b não foi informado, portanto, b=0

''' Parando pra pensar nisso, poderíamos ter usado essa técnica no exercício
    de contagens. Na contagem personalizada onde o usuário digitaria os números
    que quisesse. Caso o valor de passo não fosse informado, poderíamos ter
    adicionado o valor 1 como parâmetro opcional de p.

    Seria uma forma mais elegante de resolver:
    Em vez de
        if p == 0:
            p = 1
            
    Fazer:
        def contagem(i, f, p=1) '''

# ESCOPO DE VARIÁVEIS:

def teste():
    x = 8
    print('Na função teste, n vale {n}.')
    print('Na função teste, x vale {x}.')


# Programa Principal

n = 2
print(f'No programa principal, n vale {n}') # -> Este comando funcionará, pois n
teste()                                     # está fora da função, sendo uma variável
                                            # de ESCOPO GLOBAL.

print(f'Na função teste, x vale {x}.') # -> Este comando não funcionará, por estar
                                      # tentando pegar um valor de variável que é
                                      # somente presente dentro de uma função.
                                      # Isso é chamado de ESCOPO LOCAL e também
                                      # apenas funcionará dentro da função.

# ESCOPO LOCAL

def teste(b):
    global a # -> Dessa forma, você transforma o a de dentro em a global,
             # logo, a == 8 até mesmo fora da função
    
    a = 8
    b += 4 # b == 9
    c = 2  # c == 2

    print(f'A dentro vale {a}') # a == 8
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# ESCOPO GLOBAL

a = 5
teste(a)
print(f'A fora vale {a}') # a == 5 || a == 8 SE O COMANDO GLOBAL A for usado
print(f'B fora vale {b}') # Não funciona
print(f'C fora vale {c}') # Não funciona


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')


# RETORNANDO VALORES

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

# PRÁTICA:

def fatorial(num=1):
    f = 1
    
    for c in range(num, 0, -1):
        f += c
    
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):

    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))

if par(num):
    print('É par!')
else:
    print('Não é par!')