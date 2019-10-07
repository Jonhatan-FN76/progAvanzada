P = float(input('Inserte la presion en pascales:'))
V = float(input('Inserte el volumen en litros:'))
T = float(input('Inserte la temperatura en celsius:'))

R = 8.314
t = T + 273.15

n = (P*V) / (R*t)

print('La cantidad de gas en esas condiciones es: %.2f' %(n), 'moles')