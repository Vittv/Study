#Faça um programa que leia 2 valores e faça o usuário escolher em um menu de 5 opções:
n1 = int(input('First value: '))
n2 = int(input('Second value: '))
i = 0
while i != 5:

    i = int(input('''Choose: 
[1] sum
[2] multiply
[3] bigger
[4] new values
[5] close program
'''))
    if i == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))

    elif i == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))

    elif i == 3:
        if n1 > n2:
            print('{} is bigger than {}'.format(n1, n2))
        else:
            print('{} is bigger than {}'.format(n2, n1))

    elif i == 4:
        print('Please choose new values: ')

        n1 = int(input('First value: '))
        n2 = int(input('Second value: '))

    elif i == 5:
        print('Program closed')

    else:
        print('Invalid code. Try again')
