#Faça um programa que mostre uma contagem regressive que comece de 10:
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('*BOOM*!!')