# Reescreva a função leiaInt() incluindo a possibilidade
# da digitação de um número inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade:

def leiaInt(msg):
    while True:
        try:
            entrada = int(input(msg))
            return entrada
        
        except ValueError:
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')

def leiaFloat(msg):
    while True:
        try:
            entrada = float(input(msg))
            return entrada
        
        except ValueError:
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')


numerointeiro = leiaInt('Digite um Inteiro: ')
numeroreal = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numerointeiro}')
print(f'O valor real digitado foi {numeroreal}')