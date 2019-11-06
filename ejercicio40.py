#Exercise 40:Name that Triangle


long1 = float(input('Inserte longitud del primer lado:'))
long2 = float(input('Inserte longitud del segundo lado:'))
long3 = float(input('Inserte longitud del tercer lado:'))



if long1 == long2 == long3:
	triangulo = 'equilatero'
elif long1 == long2 or long1 == long3 or long2 == long3:
	triangulo = "isoseles"
else:
	triangulo = 'escaleno'
	
print('Tipo de triangulo:',(triangulo))

