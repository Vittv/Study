#Faça um programa que peça para dizer se você é M ou F e continue perguntando caso mande uma resposta errada:
s = str(input('Type gender: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Wrong code, please try again: ')).strip().upper()[0]
print('Gender {} successfully registered'.format(s))