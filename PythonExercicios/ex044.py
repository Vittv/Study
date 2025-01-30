#Faça um programa que calcule o valor a ser pago por um produto, considerando preço normal e condição de pagamento:
n = float(input('Valor do produto: R$'))
c = str(input('''Selecione uma condição de pagamento:
[1] à vista no dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão) '''))
if c == '1':
    n1 = n - (n*10/100)
    print('Pagando à vista no dinheiro, o valor será de R${:.2f} (com 10% de desconto)'.format(n1))
elif c == '2':
    n2 = n - (n*5/100)
    print('Pagando à vista no cartão, o valor será de R${:.2f} (com 5% de desconto)'.format(n2))
elif c == '3':
    n3 = n
    print('Pagando duas vezes no cartão, cada parcela será de R${:.2f}, totalizando R${:.2f} (preço original)'.format((n/2), n))
elif c == '4':
    nn = float(input('Selecione em quantas parcelas vai pagar (pelo menos 3): '))
    j = n + (n * 20/100)
    p = j / nn
    print('Pagando em {} parcelas no cartão, cada parcela será de R${:.2f}, totalizando R${:.2f} (com 20% de juros)'.format(nn, j, p ))
else:
    n = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')

#CÓDIGO DO PROFESSOR:

'''print('{:=*40}'. format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print(FORMAS DE PAGAMENTO
[1] à vista no dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão)
opção = int(input('Qual é a forma de pagamento?'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
else:
    preço = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')'''
