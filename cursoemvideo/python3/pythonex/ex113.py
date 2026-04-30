# Reescreva a função leiaInt() incluindo a possibilidade
# da digitação de um número inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade:

def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
            return entrada
        
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')

def leiaFloat(msg):
    while True:
        try:
            entrada = float(input(msg))
            return entrada
        
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')


numerointeiro = leiaInt('Digite um Inteiro: ')
numeroreal = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numerointeiro} e o real foi {numeroreal}')


# CÓDIGO DO PROFESSOR:

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real:')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')