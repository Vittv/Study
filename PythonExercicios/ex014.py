#Faça um conversor de celsius para fahrenheit e kelvin
temp = float(input('Informe a temperatura em °C:'))
F = (temp*9/5)+32
K = temp+273.15
print('Esta temperatura correponde a {:.1f}°F e {:.1f}K'.format(F, K))
