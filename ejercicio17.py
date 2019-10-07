masa = float(input('Introduce la masa del agua en gramos: '))
cambio_temp = float(input('Introduce el cambio de temperatura en grados celcius: '))

C = 4.186 
julios = masa * C * cambio_temp

print("\n El total de energia en julios es: ",(julios))

costo_kilowat_hora = 8.9 
kilowat_hora = julios / 3.6e+6 

costo = kilowat_hora * costo_kilowat_hora

print("\n El costo total es: $",(costo))