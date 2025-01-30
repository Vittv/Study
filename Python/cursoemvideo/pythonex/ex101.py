# Faça um programa que receba o ano de nascimento como parâmetro
# e retorne um valor LITERAL como resposta:

from datetime import datetime

def voto(nasc):
    idade = datetime.now().year - nasc

    if idade < 16:
        resp = f'Com {idade} anos: NÃO VOTA'

    elif 16 <= idade <= 18:
        resp = f'Com {idade} anos: FACULTATIVO'
    
    elif idade > 65:
        resp = f'Com {idade} anos: FACULTATIVO'

    elif 65 > idade > 18:
        resp = f'Com {idade} anos: VOTO OBRIGATÓRIO'

    print(resp)
    return resp



print('-'*30)
nasc = int(input('Em que ano você nasceu? '))

voto(nasc)
