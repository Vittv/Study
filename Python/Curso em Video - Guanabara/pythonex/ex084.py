# Faça um programa que leia dados e mostre
# o nome da pessoa mais pesada e o da mais leve:

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    
    if resp in 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')

for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')

for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
print()