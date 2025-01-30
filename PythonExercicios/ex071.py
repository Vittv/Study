# Faça um caixa eletrônico:

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} nota(s) de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

#CÓDIGO DO NICHOLAS:

'''n = float(input('Quanto quer sacar? R$'))
ncin = nvin = ndez = num = 0
rcin = rvin = rdez = rum = 0
if n >= 50:

    ncin = n / 50
    rcin = n % 50
    n = rcin
    print(f'{int(ncin)} nota(s) de R$50.00')

if n >= 20:

    nvin = n / 20
    rvin = n % 20
    n = rvin
    print(f'{int(nvin)} nota(s) de R$20.00')

if n >= 10:

    ndez = n / 10
    rdez = n % 10
    n = rdez
    print(f'{int(ndez)} nota(s) de R$10.00')

if n >= 1:

    num = n / 1
    rnum = n % 1
    n = rnum
    print(f'{int(num)} nota(s) de R$1.00')'''


