#Escreva um programa que pergunte o valor da casa, o salário do comprador e em quantos anos
#ele irá pagar. Calcule o valor a ser pago por mês, sabendo que não pode exceder 30% do salário:
c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Anos para pagar: '))
p = c / (a * 12)
if p > s * (30/100):
    print('A prestação mensal R${:.2f} excede 30% do valor do salário R${:.2f}\n'
          ',portanto, o empréstimo será negado. '.format(p, s))
elif p < s * (30/100):
    print('A prestação mensal R${:.2f} não excede 30% do salário R${:.2f}\n'
          ',portanto, o empréstimo será aprovado.'.format(p, s))