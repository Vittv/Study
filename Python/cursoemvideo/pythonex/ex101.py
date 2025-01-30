# Faça um programa que receba o ano de nascimento como parâmetro
# e retorne um valor LITERAL como resposta:

def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'

    elif 16 <= idade <= 18 or idade > 65:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    
    elif 65 > idade > 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
