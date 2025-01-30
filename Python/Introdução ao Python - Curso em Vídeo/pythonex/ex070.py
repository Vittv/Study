# Faça um programa que leia o nome e preço de um produto várias vezes ou não
# mostrando o total gasto, quantos produtos custaram mais de 1000 e
# qual o nome do produto mais barato

c = total = menor = cont = 0
barato = ' '
while True:

    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    total += preço

    if preço > 1000:
        c += 1

    if cont == 1 or preço < menor:
        barato = nome
        menor = preço

    if escolha == 'N':

        break

print(f'O total gasto foi de R${total:.2f}')
print(f'{c} produto(s) custou(aram) mais de R$1000.00')
print(f'{barato} foi o produto mais barato custando {menor}')


