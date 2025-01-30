#Faça um programa que converta metro para centímetro e milímetro:
m = float(input('Digite a medida em metros: '))
km = m*0.001
hm = m*0.01
dam = m* 0.1
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {}m corresponde a:'.format(m))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
