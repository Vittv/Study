#Leia o peso e a altura de uma pessoa, calculando seu IMC e determinando diversas categorias com base no resultado:
w = float(input('Digite seu peso: '))
h = float(input('Digite sua altura: '))
imc = w/(h**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está com o seu peso IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está OBESO')
elif imc >= 40:
    print('Você está OBESO MÓRBIDO')