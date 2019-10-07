# calculadora de IMC

masa= float(input('insertar su masa en kg:'))
estatura= float(input('inserte estatura en metros:'))

imc = masa / estatura**2

if imc < 16:
	print('tienes delgadez severa')
elif imc >= 16 and imc < 17:
	print('tiene delgadez moderada')
elif imc >= 17 and imc < 18.5:
	print('tiene delgadez leve')
elif imc >= 18.5 and imc < 25:
	print('estado normal')
elif imc >= 25 and imc < 30:
	print('preobesidad')
elif imc >= 30 and imc < 35:
	print('obesidad leve')
elif imc >= 35 and imc < 40:
	print('obesidad media')
elif imc >= 40:
	print('obesidad morbida')
else:
	print('opcion invalida')

print('su imc fue de',imc)