#Faça um programa que leia duas notas de um aluno e mostre se ele está aprovado, em recuperação ou reprovado:
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
if m < 5.0:
    print('Sua média é menor que 5 e você foi REPROVADO')
elif m > 5.0 and m < 6.9:
    print('Sua média ficou entre 5 e 6.9 e você está de RECUPERAÇÃO')
elif m >= 7.0:
    print('Sua média foi maior que 6 e você está APROVADO')