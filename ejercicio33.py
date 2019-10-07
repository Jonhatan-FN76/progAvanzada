undia = int(input('Introduce la cantidad de pan que comprara:'))
regular = undia * 3.49
preciodes = undia * (3.49 * 0.60)
total = regular - preciodes
print("El precio normal es: $%5.2f" %(regular))
print("El descuento de un dia: $%5.2f" %(preciodes))
print("El total a pagar es: $%5.2f" %(total))