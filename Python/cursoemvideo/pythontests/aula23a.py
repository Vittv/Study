print('Oi')

print(x)  # - > NameError: x is not defined

# Erros são chamados de exceções

n = int(input('Número: '))
print(f'Você digitou o número {n}')

# Se eu digitar oito em vez de 8, recebemos uma EXCEÇÃO chamada ValueError
# causando essa exceção por não ser um valor inteiro.

a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')

# Se eu digitar 0 como denominador, eu recebei a EXCEÇÃO
# ZeroDivisionError: division by zero

r = 2 / '2' # - > TypeError

lst = [3, 6, 4]
print(lst[3])

# Como sempre começamos contagens pelo número 0, recebemos uma EXCEÇÃO
# chamada IndexError por colocar um valor que não pôde ser encontrado

import uteis

# Com a ausência do módulo importado, recebe-se a EXCEÇÃO ModuleNotFoundError

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível divir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')