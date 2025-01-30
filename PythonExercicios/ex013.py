#Faça um programa que leia um valor de salário e mostre seu aumento de 15%:
n = float(input("Salário do Funcionário: "))
s = n*5/100
b = n+s
print('O salário com 15% de aumento é {}'.format(b))
#bonus
preço = float(input('Quando custa o ventilador de teto?R$'))
pix = preço-(preço*5/100)
parcelado = preço+(preço*8/100)
print('À vista no pix custará R${:.2f} com 5% de desconto\nenquanto que parcelado em 12x será R${:.2f} com 8% de aumento'.format(pix, parcelado))