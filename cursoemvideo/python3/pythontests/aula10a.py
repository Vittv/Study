'''nome = str(input('Qual é o seu nome? '))
if nome == 'Vitt':
    print('Seu nome é tão lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m>=6:
    print('Parabéns, com a média {:.1f}, você passou!'.format(m))
else:
    print('Infelizmente, com a média {}, você não passou.'.format(m))