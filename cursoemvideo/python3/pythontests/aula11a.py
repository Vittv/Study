

#Código para cores:
#\033[0;33;44m]

#STYLE: 0, 1, 4, 7
# 0 = None
# 1 = Bold
# 4 = Underline
# 7 = Negative

#TEXT: 30 - 37
#30 - WHITE
#31 - RED
#32 - GREEN
#33 - YELLOW
#34 - BLUE
#35 - PURPLE
#36 - CYAN
#37 - GREY

#BACK: 40 - 47
#40 - WHITE
#41 - RED
#42 - GREEN
#43 - YELLOW
#44 - BLUE
#45 - PURPLE
#46 - CYAN
#47 - GREY

#TESTES:
'''teste1 = \033[0;30;41m
teste2 = \033[4;33;44m
teste3 = \033[1;35;43m
teste4 = \033[30;42m
teste5 = \033[m
teste6 = \033[7;30m'''

'''print('\033[7;30mOlá, Mundo!\033[m')'''
'''a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))'''

nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {} {} {}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
