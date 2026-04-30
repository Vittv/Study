#Faça um programa que mostre se uma frase é um palíndromo ou não:
'''f = str(input('Digite uma frase: ')).replace(' ','').replace(',','').upper()
print('Invertendo a frase {}, temos: {}, logo'.format(f, f[::-1]))
if f == f[::-1]:
    print('A frase {} é um palíndromo'.format(f))
else:
    print('A frase {} não é um palíndromo'.format(f))'''

#CÓDIGO DO PROFESSOR:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('TEMOS um PALÍNDROMO')
else:
    print('NÃO TEMOS um PALÍNDROMO')