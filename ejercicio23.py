from math import tan, pi
s = float(input('Inserte la longitud de un lado: '))
n = float(input('Inserte el numero de lados: '))

a = (n*s**2)/(4*tan(pi/n))

print('\n El area del poligono es: %.2f' %a ,'m2')

