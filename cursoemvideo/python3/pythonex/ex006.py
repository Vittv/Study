#Faça um programa que leia um número e mostre seu dobro, triplo e raiz quadrada:
n = int(input('Digite um valor: '))
print('O dobro de {} é {} \nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
