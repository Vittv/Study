def mostralinha():

    print('----------------------')

mostralinha()
print('       SISTEMA DE ALUNOS       ')
mostralinha()
mostralinha()
print('    CADASTRO DE FUNCIONÁRIOS   ')
mostralinha()
mostralinha()
print('        ERRO DO SISTEMA        ')
mostralinha()

def lin():
    print('-' * 30)


# Programa Principal:
lin()
print('   CURSO EM VÍDEO   ')
lin()
lin()
print('   APRENDA PYTHON   ')
lin()
lin()
print('  GUSTAVO GUANABARA ')
lin()


def mensagem(msg):
    print('-----------------------------')
    print(msg)
    print('-----------------------------')

 
mensagem('SISTEMA DE ALUNOS')


def título(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


# Programa Principal
título('    CURSO EM VÍDEO    ')
título('    APRENDA PYTHON    ')
título('    GUSTAVO GUANABARA    ')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(a = 4, b = 5)  # É possível mudar a ordem contanto que seja explícito
soma(8, 9)
soma(2, 1)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1 


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def some(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


some(5, 2)
some(2, 9, 4)