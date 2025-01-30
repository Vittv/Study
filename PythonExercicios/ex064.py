#Faça um programa que te dê quantos inputs quiser e mostre o total de inputs e a sua soma:
s = 0
c = 0
n = int(input('Enter a value [999 to STOP]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Enter a value [999 to STOP]: '))
print('The sum of all {} values is {}'.format(c, s))
