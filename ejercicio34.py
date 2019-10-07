# Ejercicio 34
#Escriba un programa que lea un numero
#entero intoducido por el usuario. Su 
#programa debe desplegar un mensaje
#indicador si su numero entero es par o impar

entero= float(int(input('insertar un numero entero:')))

a = (entero / 2)
b = (entero % 2)

if b <= 0.0:
	print('es un numero par')
elif b >= 1:
	print('es un numero impar')