#Faça um programa que leia um frase e mostre quantas vezes a letra a aparece e onde ela aparece na primeira e última vez:
'''n = str(input('Digite uma frase: ')).strip()
n1 = n.lower()
n2 = n1.count('a')
n3 = n1.find('a')
n4 = n1.rfind('a')
print("Esta frase possui a letra A {} vezes".format(n2))
print('A letra A aparece pela primeira vez na posição {}'.format(n3))
print('A letra A aparece pela última vez na posição {}'.format(n4))'''

#Código do Professor:

n = str(input('Digite uma frase: ')).upper().strip()
print('Esta frase possui a letra A {} vezes'.format(n.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(n.find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(n.rfind('A')+1))
#o + 1 é pra indicar a primeira posição como 1 em vez de 0