#Faça um programa que baseado em dias e km rodados, determine o preço a se pagar no aluguel de um carro(60 por dia, 0.15 por km):
dia = int(input('Quantos dias alugados?'))
km = float(input("Quantos km rodados?"))
pf = (dia*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(pf))