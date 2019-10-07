#hacer un programa en el que el usuario intruduzca el nombre de la comida
#que ordeno en un restaurante y su precio despues su programa debe calcular 
#el subtotal el iva y la propina de toda la cuenta la salida del programa debe parecer
#a un ticket de restaurante .use un iva del 16% y una propina del 15% del sub total
#Los valores numericos debe tener 2 decimales.

comida_1= input('insertar comida')
print('comida 1', comida_1)
precio_1= float (input('insertar pecio'))
print('precio 1', precio_1)

comida_2= input('insertar comida')
print('comida 2', comida_2)
precio_2= float (input('insertar pecio'))
print('precio 2', precio_2)

comida_3= input('insertar comida')
print('comida 3', comida_3)
precio_3= float (input('insertar pecio'))
print('precio 3', precio_3)

comida_4= input('insertar comida')
print('comida 4', comida_4)
precio_4= float (input('insertar pecio'))
print('precio 4', precio_4)

comida_5= input('insertar comida')
print('comida 5', comida_5)
precio_5= float (input('insertar pecio'))
print('precio 5', precio_5)

subtotal= precio_1+precio_2+precio_3+precio_4+precio_5
print('subtotal',)

IVA=subtotal*0.16
subtotal1=subtotal+IVA
print('IVA',subtotal1)

propina=subtotal*.015
subtotal2=subtotal+propina
print('propina',subtotal2)

TOTAL=subtotal+subtotal1+subtotal2
print('TOTAL',TOTAL)
