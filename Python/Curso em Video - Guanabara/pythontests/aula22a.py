def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f += c
    return f

num = int(input('Digite um valor '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

# Criamos a pasta modulos para essa aula
# e usaremos a mesma para o resto dos códigos

# Nossa que legal, não esperava isso
# Enfim

# A modularização é importante para:

# Organização do código
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilização em outros projetos

# Vários módulos foram um PACOTE, conhecido como BIBLIOTECA em outras linguagens